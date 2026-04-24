"""HTML injector — stamps content_json into perfect_homework.html template.

Pure functions, no side effects. Template is read ONCE at module import and
cached in memory. See CONTRACTS.md §5 for the injector contract.
"""

import json
import re

from ..config import TEMPLATE_PATH

# Read template ONCE at module load (not per request)
with open(TEMPLATE_PATH, "r", encoding="utf-8") as _f:
    _TEMPLATE = _f.read()

# Mapping: content_json key -> JS constant name in template
_ARRAY_CONSTANTS = [
    ("panels",           "PANELS"),
    ("quotes",           "QUOTES"),
    ("flashcards",       "FLASHCARDS"),
    ("memory_sprint",    "MS_QUESTIONS"),
    ("gb_adaptive_quiz", "GB_ADAPTIVE_QUIZ"),
    ("gb_why_chain",     "GB_WHY_CHAIN"),
    ("gb_memory_match",  "GB_MEMORY_MATCH"),
    ("boss_questions",   "BOSS_QUESTIONS"),
]


def _esc(s) -> str:
    """Escape text for safe insertion into HTML content."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inject(
    content_json: dict,
    meta_override: dict | None = None,
    runtime_context: dict | None = None,
) -> str:
    """Inject content_json into the Perfect Homework HTML template.

    content_json: full schema per CONTRACTS §1
    meta_override: optional {title, subject_display, section, cefr_level} to force
                   specific values. If None, uses content_json['meta'].
    runtime_context: optional dict — if provided, inject the AI tutor runtime hook
                     (window.NETS_CTX + runtime.js) before </body>. Used for live
                     preview; omit for standalone export.

    Returns: rendered HTML string.
    """
    html = _TEMPLATE
    meta = meta_override or content_json.get("meta") or {}

    # 1. Replace title h1 (first occurrence only)
    title = meta.get("title", "Homework")
    subject_display = meta.get("subject_display", "")
    section = meta.get("section", "")

    html = re.sub(
        r"<h1>.*?</h1>",
        f"<h1>NETS · {_esc(title)}</h1>",
        html,
        count=1,
    )

    # 2. Replace caption div (first occurrence — the one at top of homework)
    if subject_display or section:
        caption_text = f"{subject_display}"
        if section:
            caption_text += f" · {section}"
        html = re.sub(
            r'<div class="caption">.*?</div>',
            f'<div class="caption">{_esc(caption_text)}</div>',
            html,
            count=1,
        )

    # 3. Replace each array constant
    for (key, const_name) in _ARRAY_CONSTANTS:
        data = content_json.get(key, [])
        if data is None:
            data = []
        # Shape adapter: template expects quotes as [{t, a}] objects.
        # If content_json has plain strings, wrap them into {t: str, a: ""}.
        # If empty, inject a single placeholder so runQuoteSequence doesn't crash.
        if key == "quotes":
            data = [
                q if isinstance(q, dict) else {"t": str(q), "a": ""}
                for q in data
            ]
            if not data:
                data = [{"t": "Bilim — aql va sabrning mevasidir.", "a": ""}]

        # Shape adapter: contract uses [[left, right]] arrays; template expects
        # [{a, b, confirmQ, correct}] objects. Convert + back-fill missing fields.
        if key == "gb_memory_match":
            adapted = []
            for pair in data:
                if isinstance(pair, dict):
                    # Already object-shaped — ensure required fields exist.
                    a = pair.get("a") or pair.get("left") or ""
                    b = pair.get("b") or pair.get("right") or ""
                    adapted.append({
                        "a": a,
                        "b": b,
                        "confirmQ": pair.get("confirmQ") or f"{a} ↔ ?",
                        "correct": pair.get("correct") or b,
                    })
                elif isinstance(pair, list) and len(pair) >= 2:
                    a, b = pair[0], pair[1]
                    adapted.append({
                        "a": a,
                        "b": b,
                        "confirmQ": f"{a} ↔ ?",
                        "correct": b,
                    })
            data = adapted

        # Empty-array placeholders to prevent template runtime crashes on new homeworks
        if not data:
            if key == "panels":
                data = [{
                    "id": 1,
                    "title": "PANEL 1 — Ko'rib chiqish",
                    "pages": [{"blocks": [{"type": "p", "text": "Bu bosqich hali to'ldirilmagan."}]}]
                }]
            elif key == "flashcards":
                data = [{"term": "Joylashtirilmagan", "def": "Kontent tayyorlanishi kutilmoqda.", "cluster": "QOIDA"}]
            elif key == "memory_sprint":
                data = [{
                    "type": "KO",
                    "prompt": "Bu bosqich hali to'ldirilmagan.",
                    "subtitle": "",
                    "tags": "[Bloom: L1 | PISA: L1]",
                    "explain": "Builder'da savollarni qo'shing.",
                    "options": ["OK"],
                    "correct": 0,
                }]
            elif key == "gb_adaptive_quiz":
                data = [{"q": "Bu bosqich hali to'ldirilmagan.", "tags": "[Bloom: L1 | PISA: L1]", "tier": "EASY", "ans": ["ok"], "capture": False}]
            elif key == "gb_why_chain":
                data = [{"q": "___ ni to'ldiring.", "inv": "ok", "reprompts": ["Ko'chiringiz."]}]
            elif key == "gb_memory_match":
                data = [["—", "—"], ["—", "—"]]
            elif key == "boss_questions":
                data = [{"q": "Bu bosqich hali to'ldirilmagan.", "tags": "[Bloom: L1 | PISA: L1 | Damage: -10 HP]", "ans": ["ok"], "hint": "Builder'dan savollarni qo'shing.", "dmg": 10}]
        replacement = f"const {const_name} = {json.dumps(data, ensure_ascii=False)};"
        pattern = rf"const {const_name}\s*=\s*\[.*?\];"
        html = re.sub(pattern, lambda _, r=replacement: r, html, count=1, flags=re.DOTALL)

    # 4. Replace RL_SCENARIO (object, not array). Fallback if missing to avoid template crash.
    rl = content_json.get("real_life")
    if not rl:
        rl = {
            "badge": "VAZIFA · Joylashtirilmagan",
            "story": "Bu bosqich hali to'ldirilmagan. Builder orqali ssenariy qo'shing.",
            "q1": {"prompt": "Savol kutilmoqda.", "ans": "ok", "fb": "OK"},
            "q2": {"prompt": "Savol kutilmoqda.", "fields": [{"id": "x", "label": "Javob", "ans": "ok"}], "fb": "OK"},
            "q3": {"prompt": "Savol kutilmoqda.", "ans": "ok", "fb": "OK"},
            "q4": {"prompt": "Savol kutilmoqda.", "fields": [{"id": "y", "label": "Javob", "ans": "ok"}], "fb": "OK"},
            "q5": {"prompt": "Savol kutilmoqda.", "open": True, "fb": "OK"},
            "q6": {"prompt": "Savol kutilmoqda.", "ans": "ok", "fb": "OK"},
            "endTitle": "Vazifa bajarildi!",
            "endSub": "Kontent builder'da to'ldirilgandan keyin to'liq tajriba paydo bo'ladi.",
        }
    if rl:
        rl_json = f"const RL_SCENARIO = {json.dumps(rl, ensure_ascii=False)};"
        # Try primary pattern (with // BOSS marker)
        primary = re.search(r"const RL_SCENARIO\s*=\s*\{.*?\};\s*// BOSS", html, flags=re.DOTALL)
        if primary:
            html = html[: primary.start()] + rl_json + "\n// BOSS" + html[primary.end():]
        else:
            # Fallback: find object literal followed by const/var/let/function/comment
            fallback = re.search(
                r"const RL_SCENARIO\s*=\s*\{.*?\}\s*(?=\s*(const|var|let|function|//))",
                html,
                flags=re.DOTALL,
            )
            if fallback:
                html = html[: fallback.start()] + rl_json + "\n\n" + html[fallback.end():]

    # Optional runtime hook (only when served live, not exported standalone)
    if runtime_context:
        ctx_json = json.dumps(runtime_context, ensure_ascii=False)
        runtime_snippet = (
            f'<script>window.NETS_CTX = {ctx_json};</script>\n'
            f'<script src="/static/runtime/runtime.js"></script>\n'
        )
        # Inject before closing </body>
        html = html.replace('</body>', runtime_snippet + '</body>', 1)

    return html


def verify_template() -> dict:
    """Check that all expected JS constants exist in the template. For startup validation."""
    missing = []
    for (_, const_name) in _ARRAY_CONSTANTS:
        if not re.search(rf"const {const_name}\s*=\s*\[", _TEMPLATE):
            missing.append(const_name)
    if not re.search(r"const RL_SCENARIO\s*=\s*\{", _TEMPLATE):
        missing.append("RL_SCENARIO")
    return {"ok": len(missing) == 0, "missing": missing}
