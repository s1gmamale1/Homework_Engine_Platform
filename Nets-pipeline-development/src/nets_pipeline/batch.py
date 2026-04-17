"""Macro Loop — batch runner.

Per §03:
  "The runner is a worker loop over a task table. It's not an 'AI
   orchestrator'. It's a queue consumer with idempotency and retry
   semantics."

N worker coroutines pull from task_queue concurrently via
SELECT ... FOR UPDATE SKIP LOCKED. Each claims one task, runs the
Micro Cycle, commits the final status. On crash, a non-terminal
status survives and the next run reclaims it.
"""
from __future__ import annotations

import asyncio
from typing import Any

from .config import Settings, load_settings
from .db import DB
from .kimi_client import KimiClient
from .logging_setup import configure_logging, get_logger
from .phase_graph import PhaseSpec, filter_phases, load_phase_graph
from .runner import run_micro_cycle
from .storage import Storage

log = get_logger(__name__)


async def run_batch(
    *,
    settings: Settings | None = None,
    subject: str | None = None,
    grade_min: int | None = None,
    grade_max: int | None = None,
    lang: str | None = None,
    phase_ids: list[str] | None = None,
) -> dict[str, int]:
    """Claim and process tasks until the queue is empty (for the given filters).

    Returns counts of {done, failed, claimed}.
    """
    settings = settings or load_settings()
    configure_logging(settings.log_level)

    db = DB(settings)
    await db.open()
    kimi = KimiClient(settings)
    storage = Storage(settings)

    all_specs = load_phase_graph()
    phase_specs = (
        filter_phases(all_specs, phase_ids) if phase_ids else all_specs
    )

    counts = {"done": 0, "failed": 0, "claimed": 0}
    call_semaphore = asyncio.Semaphore(settings.max_concurrent_tasks)

    try:
        workers = [
            asyncio.create_task(
                _worker_loop(
                    worker_id=i,
                    settings=settings,
                    phase_specs=phase_specs,
                    kimi=kimi,
                    db=db,
                    storage=storage,
                    call_semaphore=call_semaphore,
                    subject=subject,
                    grade_min=grade_min,
                    grade_max=grade_max,
                    lang=lang,
                    counts=counts,
                )
            )
            for i in range(settings.max_concurrent_tasks)
        ]
        await asyncio.gather(*workers)
    finally:
        await db.close()

    log.info("batch_complete", **counts)
    return counts


async def _worker_loop(
    *,
    worker_id: int,
    settings: Settings,
    phase_specs: dict[str, PhaseSpec],
    kimi: KimiClient,
    db: DB,
    storage: Storage,
    call_semaphore: asyncio.Semaphore,
    subject: str | None,
    grade_min: int | None,
    grade_max: int | None,
    lang: str | None,
    counts: dict[str, int],
) -> None:
    """Single worker: claim → run → commit, until the queue is empty."""
    while True:
        task = await _claim_next_filtered(
            db,
            subject=subject,
            grade_min=grade_min,
            grade_max=grade_max,
            lang=lang,
        )
        if task is None:
            log.info("worker_idle_exit", worker_id=worker_id)
            return

        counts["claimed"] += 1
        log.info(
            "task_claimed",
            worker_id=worker_id,
            task_id=task["task_id"],
            lesson_id=task["lesson_id"],
        )

        try:
            result = await run_micro_cycle(
                task=task,
                phase_specs=phase_specs,
                kimi=kimi,
                db=db,
                storage=storage,
                call_semaphore=call_semaphore,
            )
            counts["done"] += 1
            log.info(
                "task_done",
                worker_id=worker_id,
                task_id=task["task_id"],
                lesson_id=task["lesson_id"],
                homework_path=result.homework_path,
                phases_ok=result.phases_succeeded,
                phases_fail=result.phases_failed,
            )
        except Exception as e:
            counts["failed"] += 1
            await db.set_task_status(
                task["task_id"], "failed", last_error=str(e)[:500]
            )
            log.error(
                "task_failed",
                worker_id=worker_id,
                task_id=task["task_id"],
                lesson_id=task["lesson_id"],
                error=str(e),
            )


async def _claim_next_filtered(
    db: DB,
    *,
    subject: str | None,
    grade_min: int | None,
    grade_max: int | None,
    lang: str | None,
) -> dict[str, Any] | None:
    """Filtered version of DB.claim_next_task.

    Reclaims both 'pending' tasks and any stuck in intermediate states
    whose updated_at is older than 10 minutes (crash recovery per §03).
    Iteration order: subject → grade → lang → lesson (§03, for cache stickiness).
    """
    where_parts: list[str] = [
        "(status = 'pending' "
        "OR (status IN ('extracting','phasing','assembling') "
        "AND updated_at < now() - interval '10 minutes'))"
    ]
    params: list[Any] = []

    if subject is not None:
        where_parts.append("subject = %s")
        params.append(subject)
    if grade_min is not None:
        where_parts.append("grade >= %s")
        params.append(grade_min)
    if grade_max is not None:
        where_parts.append("grade <= %s")
        params.append(grade_max)
    if lang is not None:
        where_parts.append("lang = %s")
        params.append(lang)

    where_clause = " AND ".join(where_parts)

    sql = f"""
        SELECT task_id, subject, grade, lang, lesson_id, pdf_uri, status, attempts
        FROM task_queue
        WHERE {where_clause}
        ORDER BY subject, grade, lang, lesson_id
        FOR UPDATE SKIP LOCKED
        LIMIT 1
    """

    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(sql, params)
        row = await cur.fetchone()
        if row is None:
            return None
        # Atomically move the row out of 'pending' so another worker can't
        # re-claim it after this transaction commits. Status is set to
        # 'extracting' here even though Stage 01 may be skipped later
        # (see runner._find_frozen_lesson). The runner will re-assert
        # 'phasing' / 'assembling' as it progresses.
        await cur.execute(
            "UPDATE task_queue SET status = 'extracting', "
            "attempts = attempts + 1 WHERE task_id = %s",
            (row["task_id"],),
        )
        return row
