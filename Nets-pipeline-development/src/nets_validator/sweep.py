"""Validator sweep — the §14 cron/queue consumer.

Iterates phase_outputs that haven't been validated yet by the current
validator model, runs the rubric, writes validation_results row.

Never updates task_queue. Never blocks the main pipeline.
"""
from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from typing import Any

from nets_pipeline.config import Settings
from nets_pipeline.db import DB
from nets_pipeline.logging_setup import get_logger
from nets_pipeline.storage import Storage

from .client import ValidatorClient
from .rubric import system_prompt as rubric_system_prompt
from .rubric import user_prompt as rubric_user_prompt

log = get_logger(__name__)


@dataclass
class SweepResult:
    evaluated: int
    pass_n: int
    flag_n: int
    fail_n: int
    errors: int


async def run_sweep(
    *,
    settings: Settings,
    limit: int = 100,
    concurrency: int = 4,
    subject: str | None = None,
    lang: str | None = None,
) -> SweepResult:
    """Validate up to `limit` phase_outputs that lack a record for the
    current validator model."""
    db = DB(settings)
    await db.open()
    storage = Storage(settings)
    client = ValidatorClient(settings)

    try:
        candidates = await _find_candidates(
            db,
            validator_model=client.model_name,
            limit=limit,
            subject=subject,
            lang=lang,
        )
        log.info(
            "sweep_start",
            validator=client.model_name,
            candidates=len(candidates),
            subject=subject,
            lang=lang,
        )

        sem = asyncio.Semaphore(concurrency)
        counts = {"pass": 0, "flag": 0, "fail": 0, "error": 0}

        async def _one(row: dict[str, Any]) -> None:
            async with sem:
                try:
                    verdict = await _validate_one(
                        row=row, client=client, db=db, storage=storage
                    )
                    counts[verdict] = counts.get(verdict, 0) + 1
                except Exception as e:
                    counts["error"] += 1
                    log.error(
                        "sweep_error",
                        lesson_id=row["lesson_id"],
                        phase_id=row["phase_id"],
                        error=str(e),
                    )

        await asyncio.gather(*[_one(r) for r in candidates])

        result = SweepResult(
            evaluated=len(candidates) - counts["error"],
            pass_n=counts["pass"],
            flag_n=counts["flag"],
            fail_n=counts["fail"],
            errors=counts["error"],
        )
        log.info("sweep_complete", **result.__dict__)
        return result
    finally:
        await db.close()


async def _find_candidates(
    db: DB,
    *,
    validator_model: str,
    limit: int,
    subject: str | None,
    lang: str | None,
) -> list[dict[str, Any]]:
    where = [
        "po.schema_valid = true",
        "NOT EXISTS ("
        "  SELECT 1 FROM validation_results vr"
        "  WHERE vr.lesson_id = po.lesson_id"
        "    AND vr.phase_id  = po.phase_id"
        "    AND vr.validator_model = %s"
        ")",
    ]
    params: list[Any] = [validator_model]
    if subject:
        where.append("l.subject = %s")
        params.append(subject)
    if lang:
        where.append("l.lang = %s")
        params.append(lang)

    sql = f"""
        SELECT po.lesson_id, po.phase_id, po.output_json,
               l.subject, l.grade, l.lang
        FROM phase_outputs po
        JOIN lessons l ON l.lesson_id = po.lesson_id
        WHERE {" AND ".join(where)}
        ORDER BY po.created_at ASC
        LIMIT %s
    """
    params.append(limit)

    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(sql, params)
        return list(await cur.fetchall())


async def _validate_one(
    *,
    row: dict[str, Any],
    client: ValidatorClient,
    db: DB,
    storage: Storage,
) -> str:
    lesson_md = storage.read_lesson(row["lesson_id"])

    sys_p = rubric_system_prompt()
    usr_p = rubric_user_prompt(
        lesson_md=lesson_md,
        phase_output=row["output_json"],
        phase_id=row["phase_id"],
        subject=row["subject"],
        grade=int(row["grade"]),
        lang=row["lang"],
    )

    call = await client.call(system_prompt=sys_p, user_prompt=usr_p)
    output = call.output_json

    if "error" in output:
        raise RuntimeError(
            f"Validator returned error: {output.get('error')} - {output.get('reason')}"
        )

    verdict = output.get("verdict", "flag")
    if verdict not in ("pass", "flag", "fail"):
        verdict = "flag"

    await _write_result(
        db=db,
        lesson_id=row["lesson_id"],
        phase_id=row["phase_id"],
        validator_model=client.model_name,
        verdict=verdict,
        verdict_summary=output.get("verdict_summary", ""),
        rubric_scores=output.get("rubric_scores", {}),
        raw_response=output,
    )

    log.info(
        "validation_complete",
        lesson_id=row["lesson_id"],
        phase_id=row["phase_id"],
        verdict=verdict,
        tokens_in=call.tokens_in,
        tokens_out=call.tokens_out,
        latency_ms=call.latency_ms,
    )
    return verdict


async def _write_result(
    *,
    db: DB,
    lesson_id: str,
    phase_id: str,
    validator_model: str,
    verdict: str,
    verdict_summary: str,
    rubric_scores: dict[str, Any],
    raw_response: dict[str, Any],
) -> None:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            INSERT INTO validation_results
              (lesson_id, phase_id, validator_model, verdict,
               verdict_summary, rubric_scores, raw_response)
            VALUES (%s, %s, %s, %s, %s, %s::jsonb, %s::jsonb)
            ON CONFLICT (lesson_id, phase_id, validator_model) DO UPDATE SET
              verdict = EXCLUDED.verdict,
              verdict_summary = EXCLUDED.verdict_summary,
              rubric_scores = EXCLUDED.rubric_scores,
              raw_response = EXCLUDED.raw_response,
              validated_at = now()
            """,
            (
                lesson_id,
                phase_id,
                validator_model,
                verdict,
                verdict_summary,
                json.dumps(rubric_scores),
                json.dumps(raw_response),
            ),
        )
