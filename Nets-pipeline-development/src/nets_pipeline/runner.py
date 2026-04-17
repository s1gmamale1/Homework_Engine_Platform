"""Micro Cycle runner — orchestrates one (subject, grade, lang, lesson) task.

Per §04:
  STAGE 01  Extraction   1 call  · sequential · blocking
  STAGE 02  Phase        N calls · parallel (scheduler)
  STAGE 03  Assembly     1 call  · sequential · blocking

Status transitions in task_queue (§03):
  pending → extracting → phasing → assembling → done
                                              ↘ failed

Resume semantics (§03 principle 5):
  If a lesson already has a frozen md_hash in `lessons`, Stage 01
  is skipped (one canonical lesson per §01). Otherwise Stage 01 runs.
  Stages 02/03 are always idempotent (upserts / file overwrites).
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

from .db import DB
from .kimi_client import KimiClient
from .logging_setup import get_logger
from .phase_graph import PhaseSpec
from .scheduler import run_lesson_phases
from .stages.assemble import assemble_homework
from .stages.extract import extract_lesson
from .storage import Storage

log = get_logger(__name__)


@dataclass
class MicroCycleResult:
    task_id: str
    lesson_id: str
    homework_path: str
    phases_succeeded: int
    phases_failed: int


async def run_micro_cycle(
    *,
    task: dict[str, Any],
    phase_specs: dict[str, PhaseSpec],
    kimi: KimiClient,
    db: DB,
    storage: Storage,
    call_semaphore: asyncio.Semaphore | None,
) -> MicroCycleResult:
    """Run the full Micro Cycle for a single task.

    Raises on any unrecoverable failure. Caller (batch worker) sets
    task_queue.status='failed' on exception.
    """
    task_id = task["task_id"]
    lesson_id = task["lesson_id"]
    subject = task["subject"]
    grade = task["grade"]
    lang = task["lang"]
    pdf_uri = task["pdf_uri"]

    # ──────────────────────────────────────────────────────────────
    # STAGE 01 — Extract (skip if already frozen)
    # ──────────────────────────────────────────────────────────────
    existing = await _find_frozen_lesson(db, lesson_id)
    if existing:
        log.info("stage_01_skipped", lesson_id=lesson_id, reason="already_frozen")
    else:
        await db.set_task_status(task_id, "extracting")
        await extract_lesson(
            task_id=task_id,
            lesson_id=lesson_id,
            subject=subject,
            grade=grade,
            lang=lang,
            pdf_uri=pdf_uri,
            kimi=kimi,
            db=db,
            storage=storage,
        )

    # ──────────────────────────────────────────────────────────────
    # STAGE 02 — Phases (parallel per scheduler)
    # ──────────────────────────────────────────────────────────────
    await db.set_task_status(task_id, "phasing")
    phase_results = await run_lesson_phases(
        task_id=task_id,
        lesson_id=lesson_id,
        subject=subject,
        grade=grade,
        lang=lang,
        specs=phase_specs,
        kimi=kimi,
        db=db,
        storage=storage,
        call_semaphore=call_semaphore,
    )

    if not phase_results.results:
        raise RuntimeError(
            f"All phases failed for {lesson_id}: {phase_results.failed}"
        )

    # ──────────────────────────────────────────────────────────────
    # STAGE 03 — Assemble
    # ──────────────────────────────────────────────────────────────
    await db.set_task_status(task_id, "assembling")
    homework_path = await assemble_homework(
        lesson_id=lesson_id,
        db=db,
        storage=storage,
    )

    await db.set_task_status(task_id, "done")
    return MicroCycleResult(
        task_id=task_id,
        lesson_id=lesson_id,
        homework_path=homework_path,
        phases_succeeded=len(phase_results.results),
        phases_failed=len(phase_results.failed),
    )


async def _find_frozen_lesson(db: DB, lesson_id: str) -> dict[str, Any] | None:
    """Return the lessons row if it exists and has a md_hash (i.e. Stage 01
    previously completed)."""
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            "SELECT lesson_id, md_uri, md_hash FROM lessons "
            "WHERE lesson_id = %s AND md_hash IS NOT NULL",
            (lesson_id,),
        )
        return await cur.fetchone()
