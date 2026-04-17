"""Phase scheduler — §15 Step 5.

For ONE lesson: read phase-graph.yaml, topologically sort the phases,
and run them in parallel waves via asyncio. Within a wave, phases run
concurrently (asyncio.gather). Waves run sequentially.

Per §04:
  "If all phases are independent, all run in parallel. If some depend
   on others, the runner honors a topological order and parallelizes
   within each tier."

This module does NOT handle multiple lessons — that's the batch runner
(§15 Step 7). One lesson at a time here.

Concurrency:
  - Within a lesson, all phases in a wave can run in parallel.
  - An optional asyncio.Semaphore can be injected by the batch runner
    to cap total in-flight Kimi calls across all concurrent lessons
    (§11 "bounded by Kimi rate limits").
"""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

from .balance import build_tracker
from .db import DB
from .kimi_client import KimiClient
from .logging_setup import get_logger
from .phase_graph import PhaseSpec, topological_waves
from .stages.phase import PhaseResult, run_phase
from .storage import Storage

log = get_logger(__name__)


@dataclass
class LessonPhaseResults:
    lesson_id: str
    results: dict[str, PhaseResult]
    failed: dict[str, str]        # phase_id -> error message


async def run_lesson_phases(
    *,
    task_id: str | None,
    lesson_id: str,
    subject: str,
    grade: int,
    lang: str,
    specs: dict[str, PhaseSpec],
    kimi: KimiClient,
    db: DB,
    storage: Storage,
    call_semaphore: asyncio.Semaphore | None = None,
    stop_on_first_failure: bool = False,
) -> LessonPhaseResults:
    """Run every phase for a lesson in the right order.

    Returns partial results if phases fail (unless stop_on_first_failure=True).
    The batch runner decides whether a partial success → lesson failed.
    """
    waves = topological_waves(specs)
    balance = build_tracker(lesson_id=lesson_id, subject=subject)

    log.info(
        "lesson_phases_start",
        lesson_id=lesson_id,
        subject=subject,
        grade=grade,
        lang=lang,
        waves=[[p for p in w] for w in waves],
        balance_plan=balance.plan,
    )

    results: dict[str, PhaseResult] = {}
    failed: dict[str, str] = {}

    for wave_idx, wave in enumerate(waves):
        # Skip phases whose dependencies failed in earlier waves
        runnable = [
            pid for pid in wave
            if not any(dep in failed for dep in specs[pid].depends_on)
        ]
        skipped = [pid for pid in wave if pid not in runnable]
        for pid in skipped:
            failed[pid] = "skipped: upstream dependency failed"

        if not runnable:
            continue

        tasks = [
            _run_one_phase(
                task_id=task_id,
                lesson_id=lesson_id,
                phase_spec=specs[pid],
                subject=subject,
                grade=grade,
                lang=lang,
                national_balance_state=balance.dynamic_context_for(pid),
                kimi=kimi,
                db=db,
                storage=storage,
                semaphore=call_semaphore,
            )
            for pid in runnable
        ]
        wave_results = await asyncio.gather(*tasks, return_exceptions=True)

        for pid, outcome in zip(runnable, wave_results):
            if isinstance(outcome, BaseException):
                failed[pid] = f"{type(outcome).__name__}: {outcome}"
                log.error(
                    "phase_failed",
                    lesson_id=lesson_id,
                    phase_id=pid,
                    wave=wave_idx,
                    error=str(outcome),
                )
                if stop_on_first_failure:
                    return LessonPhaseResults(
                        lesson_id=lesson_id, results=results, failed=failed
                    )
            else:
                results[pid] = outcome

    log.info(
        "lesson_phases_complete",
        lesson_id=lesson_id,
        succeeded=len(results),
        failed=len(failed),
    )
    return LessonPhaseResults(lesson_id=lesson_id, results=results, failed=failed)


async def _run_one_phase(
    *,
    task_id: str | None,
    lesson_id: str,
    phase_spec: PhaseSpec,
    subject: str,
    grade: int,
    lang: str,
    national_balance_state: dict[str, Any],
    kimi: KimiClient,
    db: DB,
    storage: Storage,
    semaphore: asyncio.Semaphore | None,
) -> PhaseResult:
    """Wrap run_phase with the optional shared semaphore + balance state."""
    if semaphore is None:
        return await run_phase(
            task_id=task_id,
            lesson_id=lesson_id,
            phase_spec=phase_spec,
            subject=subject,
            grade=grade,
            lang=lang,
            national_balance_state=national_balance_state,
            kimi=kimi,
            db=db,
            storage=storage,
        )
    async with semaphore:
        return await run_phase(
            task_id=task_id,
            lesson_id=lesson_id,
            phase_spec=phase_spec,
            subject=subject,
            grade=grade,
            lang=lang,
            national_balance_state=national_balance_state,
            kimi=kimi,
            db=db,
            storage=storage,
        )
