"""Stage 03 — Assembler.

Per §07:
  The Assembler doesn't "generate" content — it composes what already
  exists. Default path is a deterministic template renderer with zero
  LLM calls. Escalate to an LLM pass only if output is seam-ridden.

This implementation is the deterministic path. It:
  1. Loads all phase_outputs for the lesson
  2. Loads the lessons row for metadata (subject, grade, lang)
  3. Renders each phase's JSON into the student-facing Markdown format
     (matches frameworks/system/assembly.md template exactly)
  4. Writes homework.md to object storage

One render_* function per phase, dispatched by phase_id. Adding a
new phase = add one renderer + phase-graph entry.
"""
from __future__ import annotations

import json
from typing import Any, Callable

from ..db import DB
from ..logging_setup import get_logger
from ..storage import Storage

log = get_logger(__name__)


# ══════════════════════════════════════════════════════════════════════
# Per-phase renderers — each returns a Markdown string (one phase section)
# ══════════════════════════════════════════════════════════════════════


def _render_phase_0a(o: dict[str, Any]) -> str:
    q = o.get("gate_quote", {})
    panels = o.get("panels", [])
    bost = o.get("bost_goal", "")
    out = [
        "## 0-A FAZA: MAVZU KO'RIGI — 2-3 daqiqa",
        "",
        f'🗣️ Iqtibos: "{q.get("text", "")}" — {q.get("author", "")}',
        "",
    ]
    for panel in panels:
        num = panel.get("number")
        title = panel.get("title", "")
        content = panel.get("content", "")
        out.append(f"📋 {num}-panel. {title}")
        out.append(content)
        out.append("")
    if bost:
        out.append(f'🎯 BOST Maqsad: "{bost}"')
        out.append("")
    return "\n".join(out)


def _render_phase_0b(o: dict[str, Any]) -> str:
    out = ["## 0-B FAZA: FLESH KARTALAR — 1-2 daqiqa", ""]
    for c in o.get("cards", []):
        prefix = "⚠️ Keng tarqalgan xato:" if c.get("is_common_mistake") else ""
        line = (
            f"- {c.get('number')}-karta. {prefix} "
            f"{c.get('concept', '')} — {c.get('visual_description', '')}"
        ).strip()
        out.append(line)
    out.extend(["", "**[ MENING UY VAZIFAMNI BOSHLASH ]**", ""])
    return "\n".join(out)


def _render_phase_1(o: dict[str, Any]) -> str:
    out = ["## ⚡ 1-FAZA: XOTIRA HURRASI — 2 daqiqa", ""]
    for q in o.get("questions", []):
        out.append(f"Savol {q.get('number')}")
        out.append(q.get("prompt", ""))
        for opt in q.get("options") or []:
            out.append(opt)
        out.append(f"✅ Javob: {q.get('answer', '')}")
        tag = q.get("tag", {})
        out.append(
            f"[{tag.get('id', '')}] | Bloom: {tag.get('bloom', '')} | "
            f"PISA: {tag.get('pisa', '')}"
        )
        out.append("")
    rule = o.get("adaptation_rule", "")
    if rule:
        out.append(f"⚙️ Moslashtirish: {rule}")
        out.append("")
    return "\n".join(out)


def _render_phase_2(o: dict[str, Any]) -> str:
    out = ["## 📖 2-FAZA: HIKOYA REJIMI — 5-7 daqiqa", "", o.get("story_text", ""), ""]
    for cp in o.get("checkpoints", []):
        out.append(f"🔒 Checkpoint {cp.get('number')}: {cp.get('question', '')}")
        out.append(f"✅ Javob: {cp.get('answer', '')}")
        tag = cp.get("tag", {})
        out.append(f"[Bloom: {tag.get('bloom', '')} | PISA: {tag.get('pisa', '')}]")
        out.append("")
    return "\n".join(out)


_GAME_EMOJI = {
    "01_Memory_Sprint": "⚡",
    "02_Spaced_Flashcards": "🃏",
    "03_Tile_Match": "🧩",
    "04_Sentence_Fill": "✏️",
    "05_Memory_Palace": "🏰",
    "06_Story_Mode": "📖",
    "07_Adaptive_Quiz": "📊",
    "08_Mystery_Box": "🎁",
    "09_Why_Chain": "❓",
    "10_Peer_Teaching": "👥",
    "11_Real-Life_Challenge": "🌍",
    "12_Reflection_Journal": "🪞",
    "13_Tic_Tac_Toe_AI": "❌⭕",
    "14_Notebook_Capture": "📓",
    "17_Reaction_Chain": "🔗",
    "18_Puzzle_Lock": "🔓",
    "21_Final-Boss": "👹",
}


def _render_phase_3(o: dict[str, Any]) -> str:
    out = ["## 🎮 3-FAZA: O'YIN TANAFUSLARI — 6-9 daqiqa", ""]
    for g in o.get("games", []):
        game_id = g.get("game_id", "")
        emoji = _GAME_EMOJI.get(game_id, "🎮")
        out.append(f"{emoji} {g.get('title', game_id)}")
        for item in g.get("items", []):
            content = item.get("content")
            if isinstance(content, (dict, list)):
                out.append(f"  {json.dumps(content, ensure_ascii=False)}")
            else:
                out.append(f"  {content}")
            if item.get("hint"):
                out.append(f"  💡 Ko'rsatma: {item['hint']}")
        out.append(f"✅ Javob: {g.get('answer_key', '')}")
        out.append("")
    return "\n".join(out)


def _render_phase_4(o: dict[str, Any]) -> str:
    scn = o.get("scenario", {})
    out = [
        "## 🌍 4-FAZA: HAQIY HAYOT MUAMMOSI — 3-5 daqiqa",
        "",
        f"{scn.get('emoji', '')} Vaziyat: {scn.get('title', '')}",
        "",
        scn.get("body_text", ""),
        "",
    ]
    for q in o.get("questions", []):
        out.append(f"{q.get('number')}. {q.get('text', '')}")
        tag = q.get("tag", {})
        out.append(f"[Bloom: {tag.get('bloom', '')} | PISA: {tag.get('pisa', '')}]")
    out.append("")
    out.append("✅ To'liq javob kaliti:")
    out.append(o.get("full_answer_key", ""))
    out.append("")
    return "\n".join(out)


def _render_phase_5(o: dict[str, Any]) -> str:
    technique = o.get("technique", "")
    out = [
        "## 🏰 5-FAZA: XOTIRA SAROYI — 2-3 daqiqa",
        "",
        o.get("entry_card", ""),
        "",
        f"🧠 Mnemonic technique: {technique}",
        "",
    ]
    for ex in o.get("exercises", []):
        out.append(f"**Exercise {ex.get('number')}: {ex.get('title', '')}**")
        for item in ex.get("items", []):
            out.append(
                f"- {item.get('label', '')} — {item.get('concept', '')} "
                f"({item.get('vivid_image', '')})"
            )
        out.append("")
    if o.get("transition_line"):
        out.append(o["transition_line"])
        out.append("")
    return "\n".join(out)


def _render_phase_6(o: dict[str, Any]) -> str:
    out = [
        "## 👹 6-FAZA: YAKUNIY BOSS — 5-10 daqiqa",
        "",
        f"Boss HP: {o.get('boss_hp', '')}",
        "",
    ]
    for q in o.get("questions", []):
        out.append(f"⚔️ BOSS SAVOL {q.get('number')} ({q.get('difficulty', '')})")
        out.append(q.get("question_text", ""))
        out.append("Sokrat ko'rsatmalari:")
        for i, hint in enumerate(q.get("socratic_hints", []), 1):
            out.append(f"{i}) {hint}")
        rub = q.get("rubric", {})
        out.append(
            f"✅ Rubrika: {rub.get('full', '')} | "
            f"{rub.get('partial', '')} | {rub.get('minimal', '')}"
        )
        tag = q.get("tag", {})
        out.append(
            f"[{tag.get('id', '')}] | Bloom: {tag.get('bloom', '')} | "
            f"PISA: {tag.get('pisa', '')} | {tag.get('transition_skill', '')}"
        )
        out.append(f"💰 Damage: {q.get('damage', '')} HP")
        out.append("")
    return "\n".join(out)


def _render_phase_7(o: dict[str, Any]) -> str:
    out = ["## 🪞 7-FAZA: AKS ETTIRISH — 2-3 daqiqa", "", "📊 BUGUNGI NATIJALAR:", ""]
    r = o.get("results", {})
    for t in r.get("strong_topics", []):
        out.append(f"✅ {t} — Zo'r!")
    for t in r.get("weak_topics", []):
        out.append(f"⚠️ {t} — Mashq kerak")
    out.append("")
    out.append("🔧 Mikro-mashqlar:")
    for ex in o.get("micro_exercises", []):
        out.append(f"{ex.get('number')}. {ex.get('exercise', '')} (j: {ex.get('answer', '')})")
    out.append("")
    if o.get("bost_recall"):
        out.append(f"🎯 BOST: {o['bost_recall']}")
        out.append("")
    out.append("💭 Refleksiya:")
    for i, p in enumerate(o.get("reflection_prompts", []), 1):
        out.append(f"{i}. {p}")
    out.append("")
    sched = o.get("spaced_repetition_schedule", [])
    if sched:
        out.append(f"📅 Keyingi takrorlash: {', '.join(sched)}")
    out.append("")
    if o.get("closing_line"):
        out.append(o["closing_line"])
        out.append("")
    return "\n".join(out)


_RENDERERS: dict[str, Callable[[dict[str, Any]], str]] = {
    "phase_0a": _render_phase_0a,
    "phase_0b": _render_phase_0b,
    "phase_1": _render_phase_1,
    "phase_2": _render_phase_2,
    "phase_3": _render_phase_3,
    "phase_4": _render_phase_4,
    "phase_5": _render_phase_5,
    "phase_6": _render_phase_6,
    "phase_7": _render_phase_7,
}

# Rendered order in the final homework.md (matches frameworks/system/assembly.md)
_PHASE_ORDER: list[str] = [
    "phase_0a",
    "phase_0b",
    "phase_1",
    "phase_2",
    "phase_3",
    "phase_4",
    "phase_5",
    "phase_6",
    "phase_7",
]


# ══════════════════════════════════════════════════════════════════════
# Assembly entry point
# ══════════════════════════════════════════════════════════════════════


async def assemble_homework(
    *,
    lesson_id: str,
    db: DB,
    storage: Storage,
) -> str:
    """Compose homework.md from phase_outputs. Returns the file path as string."""
    # 1. Load lesson metadata
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            "SELECT subject, grade, lang FROM lessons WHERE lesson_id = %s",
            (lesson_id,),
        )
        lesson_row = await cur.fetchone()
        if lesson_row is None:
            raise RuntimeError(f"No lesson row for '{lesson_id}' — run Stage 01 first")

        await cur.execute(
            "SELECT phase_id, output_json FROM phase_outputs WHERE lesson_id = %s",
            (lesson_id,),
        )
        rows = await cur.fetchall()

    phase_outputs: dict[str, dict[str, Any]] = {
        r["phase_id"]: r["output_json"] for r in rows
    }
    missing = [p for p in _PHASE_ORDER if p not in phase_outputs]
    if missing:
        log.warning(
            "assembler_missing_phases",
            lesson_id=lesson_id,
            missing=missing,
        )

    # 2. Compose final markdown
    subject = lesson_row["subject"]
    grade = lesson_row["grade"]
    title_line = f"## NETS HOMEWORK ENGINE — DEMO LESSON"
    header = [
        title_line,
        f"{subject} · {grade}-sinf",
        f"lesson_id: {lesson_id}",
        "",
        "---",
        "",
    ]
    parts: list[str] = ["\n".join(header)]

    for pid in _PHASE_ORDER:
        o = phase_outputs.get(pid)
        if o is None:
            parts.append(f"<!-- Phase '{pid}' missing from phase_outputs -->\n")
            continue
        renderer = _RENDERERS[pid]
        parts.append(renderer(o))
        parts.append("\n---\n")

    rendered = "\n".join(parts)

    # 3. Write to storage
    path = storage.write_homework(lesson_id, rendered)
    log.info(
        "assemble_complete",
        lesson_id=lesson_id,
        subject=subject,
        grade=grade,
        path=str(path),
        phases_rendered=len(phase_outputs),
        phases_missing=len(missing),
    )
    return str(path)
