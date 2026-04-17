"""Postgres helpers.

Wraps psycopg3 async connection pool. Exposes narrow functions for the
4 tables defined in migrations/001_init.sql:

  - lessons       : canonical extracted lesson
  - phase_outputs : per-phase JSON deliverable + metrics
  - task_queue    : batch queue (claim with SELECT ... FOR UPDATE SKIP LOCKED)
  - session_log   : append-only audit

Per §10 "State is a database, not a message" — sessions read/write rows,
never pass state to each other in-memory.
"""
from __future__ import annotations

import json
from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

from psycopg import AsyncConnection
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool

from .config import Settings


class DB:
    def __init__(self, settings: Settings) -> None:
        self._pool = AsyncConnectionPool(
            conninfo=settings.database_url,
            min_size=1,
            max_size=max(settings.max_concurrent_tasks * 2, 4),
            kwargs={"row_factory": dict_row},
            open=False,
        )

    async def open(self) -> None:
        await self._pool.open()

    async def close(self) -> None:
        await self._pool.close()

    @asynccontextmanager
    async def conn(self) -> AsyncIterator[AsyncConnection]:
        async with self._pool.connection() as c:
            yield c

    # ──────────────────────────────────────────────────────────────
    # lessons
    # ──────────────────────────────────────────────────────────────
    async def upsert_lesson(
        self,
        *,
        lesson_id: str,
        subject: str,
        grade: int,
        lang: str,
        pdf_uri: str,
        md_uri: str,
        md_hash: str,
    ) -> None:
        async with self.conn() as c, c.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO lessons
                  (lesson_id, subject, grade, lang, pdf_uri, md_uri, md_hash, extracted_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, now())
                ON CONFLICT (lesson_id) DO UPDATE SET
                  md_uri = EXCLUDED.md_uri,
                  md_hash = EXCLUDED.md_hash,
                  extracted_at = EXCLUDED.extracted_at
                """,
                (lesson_id, subject, grade, lang, pdf_uri, md_uri, md_hash),
            )

    # ──────────────────────────────────────────────────────────────
    # phase_outputs
    # ──────────────────────────────────────────────────────────────
    async def upsert_phase_output(
        self,
        *,
        task_id: str | None,
        lesson_id: str,
        phase_id: str,
        output_json: dict[str, Any],
        schema_valid: bool,
        prompt_hash: str,
        tokens_in: int,
        tokens_out: int,
        cost_usd: float,
        latency_ms: int,
        cache_hit_pct: float,
    ) -> None:
        async with self.conn() as c, c.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO phase_outputs
                  (task_id, lesson_id, phase_id, output_json, schema_valid,
                   prompt_hash, tokens_in, tokens_out, cost_usd, latency_ms, cache_hit_pct)
                VALUES (%s, %s, %s, %s::jsonb, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (lesson_id, phase_id) DO UPDATE SET
                  task_id = EXCLUDED.task_id,
                  output_json = EXCLUDED.output_json,
                  schema_valid = EXCLUDED.schema_valid,
                  prompt_hash = EXCLUDED.prompt_hash,
                  tokens_in = EXCLUDED.tokens_in,
                  tokens_out = EXCLUDED.tokens_out,
                  cost_usd = EXCLUDED.cost_usd,
                  latency_ms = EXCLUDED.latency_ms,
                  cache_hit_pct = EXCLUDED.cache_hit_pct,
                  created_at = now()
                """,
                (
                    task_id,
                    lesson_id,
                    phase_id,
                    json.dumps(output_json),
                    schema_valid,
                    prompt_hash,
                    tokens_in,
                    tokens_out,
                    cost_usd,
                    latency_ms,
                    cache_hit_pct,
                ),
            )

    # ──────────────────────────────────────────────────────────────
    # session_log (append-only audit)
    # ──────────────────────────────────────────────────────────────
    async def log_event(
        self,
        *,
        task_id: str | None,
        stage: str,
        event: str,
        phase_id: str | None = None,
        payload: dict[str, Any] | None = None,
    ) -> None:
        async with self.conn() as c, c.cursor() as cur:
            await cur.execute(
                """
                INSERT INTO session_log (task_id, stage, phase_id, event, payload)
                VALUES (%s, %s, %s, %s, %s::jsonb)
                """,
                (
                    task_id,
                    stage,
                    phase_id,
                    event,
                    json.dumps(payload or {}),
                ),
            )

    # ──────────────────────────────────────────────────────────────
    # task_queue — claim with SKIP LOCKED (per §10)
    # ──────────────────────────────────────────────────────────────
    async def claim_next_task(self) -> dict[str, Any] | None:
        async with self.conn() as c, c.cursor() as cur:
            await cur.execute(
                """
                SELECT task_id, subject, grade, lang, lesson_id, pdf_uri, status, attempts
                FROM task_queue
                WHERE status = 'pending'
                ORDER BY subject, grade, lang, lesson_id
                FOR UPDATE SKIP LOCKED
                LIMIT 1
                """,
            )
            row = await cur.fetchone()
            if row is None:
                return None
            await cur.execute(
                "UPDATE task_queue SET status = 'extracting', attempts = attempts + 1 "
                "WHERE task_id = %s",
                (row["task_id"],),
            )
            return row

    async def set_task_status(
        self, task_id: str, status: str, last_error: str | None = None
    ) -> None:
        async with self.conn() as c, c.cursor() as cur:
            await cur.execute(
                "UPDATE task_queue SET status = %s, last_error = %s WHERE task_id = %s",
                (status, last_error, task_id),
            )
