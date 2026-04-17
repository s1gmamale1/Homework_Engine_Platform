"""Session runner — the §15 Step 2 primitive.

One generic function (`run_session`) used by all three stages (Extractor,
Phase Worker, Assembler). Matches §08 "Session Anatomy" exactly:

    SESSION
    ├─ compose_prompt()     (done by caller; Prompt object passed in)
    ├─ call_model()         (Kimi API, structured output mode)
    ├─ validate_output()    (JSON Schema check, bounded retry)
    ├─ persist()            (runner's responsibility — see stages/)
    └─ emit_log()           (structured event per §13)

The runner itself does NOT know what stage it's serving. Callers in
`stages/extract.py`, `stages/phase.py`, `stages/assemble.py` compose the
prompt and schema_id, then hand off to `run_session`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .db import DB
from .kimi_client import CallResult, KimiClient
from .logging_setup import get_logger
from .prompt import Prompt
from .validator import SchemaValidationError, validate

log = get_logger(__name__)


@dataclass
class SessionResult:
    output_json: dict[str, Any]
    call: CallResult
    prompt_hash: str
    schema_valid: bool


class SessionError(Exception):
    pass


async def run_session(
    *,
    prompt: Prompt,
    schema_id: str,
    kimi: KimiClient,
    db: DB,
    task_id: str | None,
    stage: str,                 # 'extract' | 'phase' | 'assemble'
    phase_id: str | None,       # None for extract/assemble
    retry_on_schema_fail: bool = True,
    max_tokens: int = 8000,
) -> SessionResult:
    """Run one session: call Kimi, validate, log. Persisting to domain
    tables is the caller's responsibility (stages/*.py) since the row
    shape differs by stage.

    Every failure mode writes a 'fail' event to session_log — whether
    the cause is a Kimi API error, a schema violation, or anything else.
    This keeps the audit stream complete per §13.
    """
    await db.log_event(
        task_id=task_id,
        stage=stage,
        phase_id=phase_id,
        event="start",
        payload={"prompt_hash": prompt.full_hash, "schema": schema_id},
    )

    try:
        return await _run_session_body(
            prompt=prompt,
            schema_id=schema_id,
            kimi=kimi,
            db=db,
            task_id=task_id,
            stage=stage,
            phase_id=phase_id,
            retry_on_schema_fail=retry_on_schema_fail,
            max_tokens=max_tokens,
        )
    except SessionError:
        # Schema-validation failures already logged 'fail' via _log_fail
        # inside the body. Don't double-emit.
        raise
    except Exception as e:
        # Any other failure (Kimi API, timeout, network, JSON parse) —
        # make sure session_log captures it before we propagate.
        await db.log_event(
            task_id=task_id,
            stage=stage,
            phase_id=phase_id,
            event="fail",
            payload={
                "reason": "api_or_runtime_error",
                "error_type": type(e).__name__,
                "error": str(e)[:500],
            },
        )
        raise


async def _run_session_body(
    *,
    prompt: Prompt,
    schema_id: str,
    kimi: KimiClient,
    db: DB,
    task_id: str | None,
    stage: str,
    phase_id: str | None,
    retry_on_schema_fail: bool,
    max_tokens: int,
) -> SessionResult:
    # --------------------------------------------------------------
    # Attempt 1 — plain call
    # --------------------------------------------------------------
    call = await kimi.call(
        system_prompt=prompt.system,
        user_prompt=prompt.user,
        max_tokens=max_tokens,
    )

    try:
        validate(call.output_json, schema_id)
        schema_valid = True
    except SchemaValidationError as first_err:
        schema_valid = False
        if not retry_on_schema_fail:
            await _log_fail(db, task_id, stage, phase_id, first_err, call)
            raise SessionError(f"Schema validation failed: {first_err}") from first_err

        # --------------------------------------------------------------
        # Attempt 2 — re-prompt with the specific error (per §11)
        # --------------------------------------------------------------
        await db.log_event(
            task_id=task_id,
            stage=stage,
            phase_id=phase_id,
            event="retry",
            payload={"reason": "schema_invalid", "errors": first_err.errors},
        )
        retry_user = (
            prompt.user
            + "\n\n<!-- ═══ SCHEMA RETRY ═══ -->\n\n"
            + "Your previous output failed schema validation with:\n"
            + "\n".join(f"- {e}" for e in first_err.errors)
            + "\n\nReturn a corrected JSON object matching the schema. JSON only."
        )
        call = await kimi.call(
            system_prompt=prompt.system,
            user_prompt=retry_user,
            max_tokens=max_tokens,
        )
        try:
            validate(call.output_json, schema_id)
            schema_valid = True
        except SchemaValidationError as second_err:
            await _log_fail(db, task_id, stage, phase_id, second_err, call)
            raise SessionError(
                f"Schema validation failed twice: {second_err}"
            ) from second_err

    await db.log_event(
        task_id=task_id,
        stage=stage,
        phase_id=phase_id,
        event="success",
        payload={
            "tokens_in": call.tokens_in,
            "tokens_out": call.tokens_out,
            "tokens_cached": call.tokens_cached,
            "cache_hit_pct": round(call.cache_hit_pct, 2),
            "cost_usd": round(call.cost_usd, 6),
            "latency_ms": call.latency_ms,
        },
    )

    log.info(
        "session_complete",
        task_id=task_id,
        stage=stage,
        phase_id=phase_id,
        tokens_in=call.tokens_in,
        tokens_out=call.tokens_out,
        cache_hit_pct=round(call.cache_hit_pct, 2),
        cost_usd=round(call.cost_usd, 6),
        latency_ms=call.latency_ms,
    )

    return SessionResult(
        output_json=call.output_json,
        call=call,
        prompt_hash=prompt.full_hash,
        schema_valid=schema_valid,
    )


async def _log_fail(
    db: DB,
    task_id: str | None,
    stage: str,
    phase_id: str | None,
    err: SchemaValidationError,
    call: CallResult,
) -> None:
    await db.log_event(
        task_id=task_id,
        stage=stage,
        phase_id=phase_id,
        event="fail",
        payload={
            "reason": "schema_invalid",
            "errors": err.errors,
            "raw_response": call.raw_content[:2000],
        },
    )
