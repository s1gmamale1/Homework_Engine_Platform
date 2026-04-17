"""Terminal observability dashboard.

Per §13 "Observability & Failure Modes":
  Track tokens, latency, cost, cache-hit percentage, schema validation,
  raw response. Target cache-hit > 70%.

Data is already in Postgres (phase_outputs + session_log + task_queue).
This module runs SQL aggregations and renders plain-text tables.

No TUI framework dependency. "Even a terminal-only view is fine." (§15)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .db import DB


@dataclass
class QueueSummary:
    status_counts: list[tuple[str, int]]


@dataclass
class CostRollup:
    total_cost_usd: float
    total_tokens_in: int
    total_tokens_out: int
    total_tokens_cached: int
    phases_counted: int
    avg_cache_hit_pct: float
    avg_latency_ms: float


@dataclass
class PhaseBreakdown:
    phase_id: str
    count: int
    avg_cost_usd: float
    avg_latency_ms: float
    avg_cache_hit_pct: float
    schema_fail_rate: float


@dataclass
class SubjectBreakdown:
    subject: str
    lessons_done: int
    lessons_failed: int
    total_cost_usd: float


@dataclass
class RecentFailure:
    task_id: str
    lesson_id: str
    subject: str
    grade: int
    lang: str
    last_error: str
    attempts: int


# ══════════════════════════════════════════════════════════════════════
# Query functions
# ══════════════════════════════════════════════════════════════════════


async def queue_summary(db: DB) -> QueueSummary:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            "SELECT status, COUNT(*) AS n FROM task_queue GROUP BY status ORDER BY status"
        )
        rows = await cur.fetchall()
    return QueueSummary(status_counts=[(r["status"], r["n"]) for r in rows])


async def cost_rollup(db: DB) -> CostRollup:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            SELECT
              COALESCE(SUM(cost_usd), 0)::float         AS total_cost,
              COALESCE(SUM(tokens_in), 0)::bigint       AS tokens_in,
              COALESCE(SUM(tokens_out), 0)::bigint      AS tokens_out,
              COALESCE(AVG(cache_hit_pct), 0)::float    AS avg_cache,
              COALESCE(AVG(latency_ms), 0)::float       AS avg_latency,
              COUNT(*)::bigint                           AS n
            FROM phase_outputs
            """
        )
        r = await cur.fetchone()

    # Estimate cached tokens from avg cache %
    cached_est = int(r["tokens_in"] * (r["avg_cache"] / 100.0)) if r["tokens_in"] else 0
    return CostRollup(
        total_cost_usd=float(r["total_cost"] or 0.0),
        total_tokens_in=int(r["tokens_in"] or 0),
        total_tokens_out=int(r["tokens_out"] or 0),
        total_tokens_cached=cached_est,
        phases_counted=int(r["n"] or 0),
        avg_cache_hit_pct=float(r["avg_cache"] or 0.0),
        avg_latency_ms=float(r["avg_latency"] or 0.0),
    )


async def phase_breakdown(db: DB) -> list[PhaseBreakdown]:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            SELECT
              phase_id,
              COUNT(*)                                            AS n,
              AVG(cost_usd)::float                                AS avg_cost,
              AVG(latency_ms)::float                              AS avg_latency,
              AVG(cache_hit_pct)::float                           AS avg_cache,
              SUM(CASE WHEN NOT schema_valid THEN 1 ELSE 0 END)::float
                / NULLIF(COUNT(*), 0)                             AS fail_rate
            FROM phase_outputs
            GROUP BY phase_id
            ORDER BY phase_id
            """
        )
        rows = await cur.fetchall()
    return [
        PhaseBreakdown(
            phase_id=r["phase_id"],
            count=int(r["n"]),
            avg_cost_usd=float(r["avg_cost"] or 0.0),
            avg_latency_ms=float(r["avg_latency"] or 0.0),
            avg_cache_hit_pct=float(r["avg_cache"] or 0.0),
            schema_fail_rate=float(r["fail_rate"] or 0.0),
        )
        for r in rows
    ]


async def subject_breakdown(db: DB) -> list[SubjectBreakdown]:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            SELECT
              tq.subject,
              SUM(CASE WHEN tq.status = 'done' THEN 1 ELSE 0 END)   AS done_n,
              SUM(CASE WHEN tq.status = 'failed' THEN 1 ELSE 0 END) AS failed_n,
              COALESCE(SUM(po.cost_usd), 0)::float                  AS cost
            FROM task_queue tq
            LEFT JOIN phase_outputs po ON po.lesson_id = tq.lesson_id
            GROUP BY tq.subject
            ORDER BY tq.subject
            """
        )
        rows = await cur.fetchall()
    return [
        SubjectBreakdown(
            subject=r["subject"],
            lessons_done=int(r["done_n"] or 0),
            lessons_failed=int(r["failed_n"] or 0),
            total_cost_usd=float(r["cost"] or 0.0),
        )
        for r in rows
    ]


async def recent_failures(db: DB, limit: int = 10) -> list[RecentFailure]:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            SELECT task_id, lesson_id, subject, grade, lang, last_error, attempts
            FROM task_queue
            WHERE status = 'failed'
            ORDER BY updated_at DESC
            LIMIT %s
            """,
            (limit,),
        )
        rows = await cur.fetchall()
    return [
        RecentFailure(
            task_id=str(r["task_id"]),
            lesson_id=r["lesson_id"],
            subject=r["subject"],
            grade=int(r["grade"]),
            lang=r["lang"],
            last_error=(r["last_error"] or "")[:120],
            attempts=int(r["attempts"]),
        )
        for r in rows
    ]


# ══════════════════════════════════════════════════════════════════════
# Rendering
# ══════════════════════════════════════════════════════════════════════


def render_queue(s: QueueSummary) -> str:
    if not s.status_counts:
        return "task_queue is empty."
    lines = ["Status         Count", "-" * 24]
    for status, n in s.status_counts:
        lines.append(f"{status:<12}  {n:>6}")
    return "\n".join(lines)


def render_cost(c: CostRollup, target_cache_hit: float) -> str:
    target_pct = target_cache_hit * 100.0
    cache_status = "✓" if c.avg_cache_hit_pct >= target_pct else "⚠"
    lines = [
        "Cost rollup across phase_outputs",
        "-" * 40,
        f"Total cost:        ${c.total_cost_usd:,.4f}",
        f"Phases counted:    {c.phases_counted}",
        f"Tokens in:         {c.total_tokens_in:,}",
        f"Tokens out:        {c.total_tokens_out:,}",
        f"Tokens cached~:    {c.total_tokens_cached:,}",
        f"Avg cache hit:     {c.avg_cache_hit_pct:>5.1f}%  "
        f"(target {target_pct:.0f}%)  {cache_status}",
        f"Avg latency:       {c.avg_latency_ms:>8.0f} ms",
    ]
    return "\n".join(lines)


def render_phases(rows: list[PhaseBreakdown]) -> str:
    if not rows:
        return "No phase_outputs yet."
    header = (
        f"{'phase_id':<10} {'n':>5} {'avg cost':>10} "
        f"{'avg ms':>9} {'cache%':>8} {'schema fail%':>13}"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.phase_id:<10} {r.count:>5} "
            f"${r.avg_cost_usd:>9.6f} "
            f"{r.avg_latency_ms:>8.0f} "
            f"{r.avg_cache_hit_pct:>7.1f} "
            f"{r.schema_fail_rate * 100:>12.1f}"
        )
    return "\n".join(lines)


def render_subjects(rows: list[SubjectBreakdown]) -> str:
    if not rows:
        return "No tasks seeded yet."
    header = f"{'subject':<20} {'done':>6} {'failed':>8} {'cost':>12}"
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.subject:<20} {r.lessons_done:>6} "
            f"{r.lessons_failed:>8} ${r.total_cost_usd:>10.4f}"
        )
    return "\n".join(lines)


def render_failures(rows: list[RecentFailure]) -> str:
    if not rows:
        return "No failed tasks."
    lines = ["Recent failures", "-" * 80]
    for r in rows:
        lines.append(
            f"{r.lesson_id}  [{r.subject} G{r.grade} {r.lang}]  "
            f"attempts={r.attempts}"
        )
        lines.append(f"  → {r.last_error}")
    return "\n".join(lines)
