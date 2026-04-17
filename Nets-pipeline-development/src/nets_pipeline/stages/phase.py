"""Stage 02 — Phase Worker.

Per §06:
  Each phase worker is the same code. Only the prompt differs, and the
  prompt is composed at runtime from files on disk.

Pipeline for one phase call:
  1. Load lesson.md (Layer 6) from storage — Stage 01 must have run
  2. Look up phase spec from phase_graph (framework_ref, games_used)
  3. Compose layered prompt (Layers 1-8 per §06)
  4. run_session → Kimi returns JSON matching schemas/{phase_id}.json
  5. Upsert phase_outputs row with output_json + metrics

Dynamic game selection for Phase 3 is NOT handled here; the phase spec
in phase-graph.yaml provides a (possibly empty) games_used list and the
worker uses whatever is there. Step 5 scheduler / Step 4 pilot work
through Phase 0-B which has no games.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..config import SCHEMAS_DIR
from ..db import DB
from ..kimi_client import KimiClient
from ..logging_setup import get_logger
from ..phase_graph import PhaseSpec
from ..prompt import compose_phase_prompt
from ..session import run_session
from ..storage import Storage

log = get_logger(__name__)


@dataclass
class PhaseResult:
    phase_id: str
    lesson_id: str
    output_json: dict[str, Any]
    schema_valid: bool
    cost_usd: float
    cache_hit_pct: float
    latency_ms: int


async def run_phase(
    *,
    task_id: str | None,
    lesson_id: str,
    phase_spec: PhaseSpec,
    subject: str,
    grade: int,
    lang: str,
    national_balance_state: dict[str, Any] | None,
    kimi: KimiClient,
    db: DB,
    storage: Storage,
) -> PhaseResult:
    """Run one phase of Stage 02 for a single lesson."""
    # 1. Load lesson.md (Layer 6)
    lesson_md = storage.read_lesson(lesson_id)

    # 2. Dynamic context (Layer 7)
    dynamic_context: dict[str, Any] = {
        "subject": subject,
        "grade": grade,
        "lang": lang,
        "lesson_id": lesson_id,
        "phase_id": phase_spec.id,
    }
    if national_balance_state is not None:
        dynamic_context["national_balance_state"] = national_balance_state

    # 3. Schema id = phase id (frameworks/schemas/{phase_id}.json)
    schema_id = phase_spec.id

    # 4. Task instruction (Layer 8)
    # Inject the ACTUAL schema — Layer 4 (phase spec) may contain an
    # illustrative JSON example with different field names. The schema
    # below is the machine-enforced contract and wins any conflict.
    schema_text = (SCHEMAS_DIR / f"{schema_id}.json").read_text(encoding="utf-8")
    task_instruction = (
        f"Produce the output for phase '{phase_spec.id}' "
        f"({phase_spec.name}) for this lesson.\n\n"
        f"**OUTPUT CONTRACT — this schema is the single source of truth.**\n"
        f"Match every field name, required property, type, enum, and length "
        f"constraint EXACTLY. If any JSON example earlier in this prompt "
        f"conflicts with this schema, the schema wins.\n\n"
        f"```json\n{schema_text}\n```\n\n"
        f"Return a single JSON object matching the schema above. "
        f"JSON only — no prose, no markdown fences around the output."
    )

    # 5. Compose layered prompt
    prompt = compose_phase_prompt(
        subject=subject,
        phase_id=phase_spec.id,
        framework_ref=phase_spec.framework_ref,
        games_used=list(phase_spec.games_used),
        lesson_md=lesson_md,
        dynamic_context=dynamic_context,
        task_instruction=task_instruction,
    )

    # 6. Run session
    result = await run_session(
        prompt=prompt,
        schema_id=schema_id,
        kimi=kimi,
        db=db,
        task_id=task_id,
        stage="phase",
        phase_id=phase_spec.id,
    )

    output = result.output_json

    # Pipeline-level failure signal from the model
    if "error" in output:
        raise RuntimeError(
            f"Phase {phase_spec.id} returned error for {lesson_id}: "
            f"{output.get('error')} - {output.get('reason')}"
        )

    # 7. Persist phase_outputs row
    await db.upsert_phase_output(
        task_id=task_id,
        lesson_id=lesson_id,
        phase_id=phase_spec.id,
        output_json=output,
        schema_valid=result.schema_valid,
        prompt_hash=result.prompt_hash,
        tokens_in=result.call.tokens_in,
        tokens_out=result.call.tokens_out,
        cost_usd=result.call.cost_usd,
        latency_ms=result.call.latency_ms,
        cache_hit_pct=result.call.cache_hit_pct,
    )

    log.info(
        "phase_complete",
        lesson_id=lesson_id,
        phase_id=phase_spec.id,
        subject=subject,
        grade=grade,
        lang=lang,
        tokens_in=result.call.tokens_in,
        tokens_out=result.call.tokens_out,
        cache_hit_pct=round(result.call.cache_hit_pct, 2),
        cost_usd=round(result.call.cost_usd, 6),
        latency_ms=result.call.latency_ms,
    )

    return PhaseResult(
        phase_id=phase_spec.id,
        lesson_id=lesson_id,
        output_json=output,
        schema_valid=result.schema_valid,
        cost_usd=result.call.cost_usd,
        cache_hit_pct=result.call.cache_hit_pct,
        latency_ms=result.call.latency_ms,
    )
