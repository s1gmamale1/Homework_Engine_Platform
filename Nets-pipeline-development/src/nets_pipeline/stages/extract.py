"""Stage 01 — Extractor.

Per §05:
  Input:  Source PDF (or pre-OCR'd text) + task metadata
  Output: Canonical lesson.md (frozen, hash-addressable) + row in lessons table

Pipeline:
  1. Read PDF → raw text
  2. Compose extraction prompt (SYSTEM / CONTEXT / INPUT / TASK)
  3. run_session → Kimi returns JSON matching schemas/lesson.json
  4. Write body_md to storage (lesson.md)
  5. Upsert lessons row with md_uri + md_hash

lesson.md on disk contains only body_md — the chapter rendered as
faithful markdown (headings/tables/lists/formulas/vocabulary sections
all inline). Structured metadata (vocabulary[], formulas[], etc.)
lives in the phase_outputs-equivalent or is discarded after Stage 01,
since phase workers read lesson.md verbatim (§06 Layer 6).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..config import SCHEMAS_DIR
from ..db import DB
from ..kimi_client import KimiClient
from ..logging_setup import get_logger
from ..pdf_reader import read_pdf
from ..prompt import compose_extraction_prompt
from ..session import run_session
from ..storage import Storage

log = get_logger(__name__)


@dataclass
class ExtractResult:
    lesson_id: str
    lesson_md_path: Path
    lesson_md_hash: str
    lesson_json: dict[str, Any]   # full extractor output; may be persisted or discarded


async def extract_lesson(
    *,
    task_id: str | None,
    lesson_id: str,
    subject: str,
    grade: int,
    lang: str,
    pdf_uri: str,
    kimi: KimiClient,
    db: DB,
    storage: Storage,
) -> ExtractResult:
    """Run Stage 01 for a single (subject, grade, lang, lesson) task."""
    pdf_path = Path(pdf_uri)
    raw_text = read_pdf(pdf_path)
    source_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

    context = {
        "subject": subject,
        "grade": grade,
        "lang": lang,
        "lesson_id": lesson_id,
        "source_hash": source_hash,
    }
    schema_text = (SCHEMAS_DIR / "lesson.json").read_text(encoding="utf-8")
    task_instruction = (
        f"Produce the lesson JSON for this {subject} grade {grade} ({lang}) "
        f"chapter.\n\n"
        f"**OUTPUT CONTRACT — this schema is the single source of truth.**\n"
        f"Match every field name, required property, type, and constraint "
        f"EXACTLY.\n\n"
        f"```json\n{schema_text}\n```\n\n"
        f"Return a single JSON object matching the schema above. JSON only."
    )

    prompt = compose_extraction_prompt(
        context=context,
        raw_input=raw_text,
        task_instruction=task_instruction,
    )

    # Extraction output is usually much larger than any phase output
    # (it carries the full chapter body verbatim). Use Kimi K2's max
    # completion budget to reduce the chance of truncation mid-stream.
    result = await run_session(
        prompt=prompt,
        schema_id="lesson",
        kimi=kimi,
        db=db,
        task_id=task_id,
        stage="extract",
        phase_id=None,
        max_tokens=16000,
    )

    lesson_json = result.output_json

    # Pipeline-level failure signal from the model
    if "error" in lesson_json:
        raise RuntimeError(
            f"Extractor returned error for {lesson_id}: "
            f"{lesson_json.get('error')} - {lesson_json.get('reason')}"
        )

    body_md = lesson_json.get("body_md")
    if not body_md or not isinstance(body_md, str):
        raise RuntimeError(
            f"Extractor output missing body_md for {lesson_id}. "
            f"Schema validation should have caught this."
        )

    lesson_path, lesson_hash = storage.write_lesson(lesson_id, body_md)

    await db.upsert_lesson(
        lesson_id=lesson_id,
        subject=subject,
        grade=grade,
        lang=lang,
        pdf_uri=pdf_uri,
        md_uri=str(lesson_path),
        md_hash=lesson_hash,
    )

    log.info(
        "extract_complete",
        lesson_id=lesson_id,
        subject=subject,
        grade=grade,
        lang=lang,
        md_hash=lesson_hash[:12],
        word_count=lesson_json.get("word_count"),
        cache_hit_pct=round(result.call.cache_hit_pct, 2),
        cost_usd=round(result.call.cost_usd, 6),
    )

    return ExtractResult(
        lesson_id=lesson_id,
        lesson_md_path=lesson_path,
        lesson_md_hash=lesson_hash,
        lesson_json=lesson_json,
    )
