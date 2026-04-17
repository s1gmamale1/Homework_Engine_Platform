"""Layered prompt composition.

Implements §06 "Prompt composition (per phase call)" exactly:

    [1] SYSTEM              frameworks/system/phase_worker_base.md
    [2] UNIFIED FRAMEWORK   frameworks/unified/schema.md
    [3] SUBJECT FRAMEWORK   frameworks/subjects/{subject}.md
    [4] PHASE SPEC          {framework_ref}
    [5] GAME MECHANICS      frameworks/games/{game_id}.md  (only if referenced)
    [6] LESSON INPUT        lesson.md
    [7] DYNAMIC CONTEXT     { grade, lang, subject, lesson_id, ... }
    [8] TASK                "Produce phase X output. Return JSON matching schema Y."

Per §11 cache discipline:
  - System message = concat(Layer 1..5)  — static, cached
  - User message   = concat(Layer 6..8)  — dynamic, per-call

For Stage 01 (Extractor), we use a simpler 4-layer structure per §05:
    SYSTEM   frameworks/system/extraction.md
    CONTEXT  { subject, grade, lang, lesson_id }
    INPUT    raw extracted text
    TASK     "Produce lesson JSON matching schema."

For Stage 03 (Assembler), prompt composition is bypassed entirely when
using deterministic template rendering (§07 default path).
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import FRAMEWORKS_DIR


@dataclass
class Prompt:
    system: str
    user: str

    @property
    def prefix_hash(self) -> str:
        """SHA256 of the system message — used to monitor cache stickiness (§13)."""
        return hashlib.sha256(self.system.encode("utf-8")).hexdigest()

    @property
    def full_hash(self) -> str:
        return hashlib.sha256((self.system + "\n" + self.user).encode("utf-8")).hexdigest()


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _layer_sep(label: str) -> str:
    return f"\n\n<!-- ═══ {label} ═══ -->\n\n"


# ══════════════════════════════════════════════════════════════════════
# Stage 02 — Phase Worker prompt
# ══════════════════════════════════════════════════════════════════════
def compose_phase_prompt(
    *,
    subject: str,
    phase_id: str,
    framework_ref: str,          # relative to project root, e.g. "frameworks/unified/phase_1.md"
    games_used: list[str],       # game_ids, e.g. ["01_Memory_Sprint"]
    lesson_md: str,
    dynamic_context: dict[str, Any],
    task_instruction: str,
) -> Prompt:
    system_parts: list[str] = []

    # Layer 1 — phase_worker_base.md
    system_parts.append(_layer_sep("LAYER 1 · SYSTEM (phase_worker_base)"))
    system_parts.append(_read(FRAMEWORKS_DIR / "system" / "phase_worker_base.md"))

    # Layer 2 — unified/schema.md
    system_parts.append(_layer_sep("LAYER 2 · UNIFIED FRAMEWORK (schema)"))
    system_parts.append(_read(FRAMEWORKS_DIR / "unified" / "schema.md"))

    # Layer 3 — subjects/{subject}.md
    subject_path = FRAMEWORKS_DIR / "subjects" / f"{subject}.md"
    if not subject_path.exists():
        raise FileNotFoundError(
            f"Subject framework not found: {subject_path}. "
            f"Only 14 of 32 subjects currently have frameworks; see README."
        )
    system_parts.append(_layer_sep(f"LAYER 3 · SUBJECT FRAMEWORK ({subject})"))
    system_parts.append(_read(subject_path))

    # Layer 4 — phase spec
    phase_path = Path(framework_ref)
    if not phase_path.is_absolute():
        phase_path = FRAMEWORKS_DIR.parent / framework_ref
    system_parts.append(_layer_sep(f"LAYER 4 · PHASE SPEC ({phase_id})"))
    system_parts.append(_read(phase_path))

    # Layer 5 — game docs (only if referenced)
    for game_id in games_used:
        game_path = FRAMEWORKS_DIR / "games" / f"{game_id}.md"
        if not game_path.exists():
            raise FileNotFoundError(f"Game doc not found: {game_path}")
        system_parts.append(_layer_sep(f"LAYER 5 · GAME MECHANIC ({game_id})"))
        system_parts.append(_read(game_path))

    system = "".join(system_parts)

    # User message = Layers 6..8 (dynamic)
    user_parts = [
        _layer_sep("LAYER 6 · LESSON INPUT"),
        lesson_md,
        _layer_sep("LAYER 7 · DYNAMIC CONTEXT"),
        json.dumps(dynamic_context, ensure_ascii=False, indent=2),
        _layer_sep("LAYER 8 · TASK"),
        task_instruction,
    ]
    user = "".join(user_parts)

    return Prompt(system=system, user=user)


# ══════════════════════════════════════════════════════════════════════
# Stage 01 — Extractor prompt
# ══════════════════════════════════════════════════════════════════════
def compose_extraction_prompt(
    *,
    context: dict[str, Any],
    raw_input: str,
    task_instruction: str,
) -> Prompt:
    system_parts = [
        _layer_sep("SYSTEM (extraction)"),
        _read(FRAMEWORKS_DIR / "system" / "extraction.md"),
    ]
    user_parts = [
        _layer_sep("CONTEXT"),
        json.dumps(context, ensure_ascii=False, indent=2),
        _layer_sep("INPUT (raw textbook content)"),
        raw_input,
        _layer_sep("TASK"),
        task_instruction,
    ]
    return Prompt(system="".join(system_parts), user="".join(user_parts))
