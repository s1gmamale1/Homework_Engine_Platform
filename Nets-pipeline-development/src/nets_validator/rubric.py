"""Rubric prompt composition for the validator.

Layers:
  SYSTEM  frameworks/system/validator.md   (static rubric persona)
  USER    <lesson.md> + <phase_output JSON> + <task context>

The rubric (validator.md) is operator-authored — same pattern as the
main pipeline's framework files. Edit the rubric file, next sweep uses
the new rules. No code change needed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from nets_pipeline.config import FRAMEWORKS_DIR


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def system_prompt() -> str:
    return _read(FRAMEWORKS_DIR / "system" / "validator.md")


def user_prompt(
    *,
    lesson_md: str,
    phase_output: dict[str, Any],
    phase_id: str,
    subject: str,
    grade: int,
    lang: str,
) -> str:
    context = {
        "phase_id": phase_id,
        "subject": subject,
        "grade": grade,
        "lang": lang,
    }
    return (
        "<!-- ═══ CONTEXT ═══ -->\n\n"
        f"{json.dumps(context, ensure_ascii=False, indent=2)}\n\n"
        "<!-- ═══ LESSON (ground-truth for factual grounding) ═══ -->\n\n"
        f"{lesson_md}\n\n"
        "<!-- ═══ PHASE OUTPUT TO VALIDATE ═══ -->\n\n"
        f"{json.dumps(phase_output, ensure_ascii=False, indent=2)}\n\n"
        "<!-- ═══ TASK ═══ -->\n\n"
        "Apply the 4 rubrics (language_register, framework_compliance, "
        "factual_grounding, age_appropriate) to the phase output above. "
        "Return the JSON verdict object specified in your system prompt. "
        "JSON only — no prose, no markdown fences."
    )
