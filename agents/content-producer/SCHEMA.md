# SCHEMA — Output Format

## Output: One `.docx` Per Chapter

**Naming:** `{Subject}_Grade{N}_Ch{N}S{S}_{lang}.docx`
**Examples:** `Matematika_Grade5_Ch1S1_uz.docx` · `Biologiya_Grade7_Ch3_uz.docx`

## CRITICAL: Real .docx Output

You MUST produce a real Microsoft Word .docx file using the `python-docx` library.
**Plain text files with a .docx extension are NOT acceptable.**

```python
# Install if needed
pip install python-docx pdfplumber

# Minimal template
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
doc.add_heading('NETS Uy Vazifasi — Matematika, 5-sinf, 1-bob', level=0)  # Title
doc.add_heading('PHASE 0-A: MAVZU KO\'RIGI / Theme Preview', level=1)     # Phase header
doc.add_paragraph('Gate quote here', style='Intense Quote')                 # Quote
doc.add_paragraph('Content here', style='List Number')                      # Numbered item
doc.add_paragraph('Bullet here', style='List Bullet')                       # Bullet
doc.save('Matematika_Grade5_Ch1S1_uz.docx')
```

---

## Heading Style Map

| Element | Style | Example |
|---------|-------|---------|
| Document title | `Title` (level=0) | NETS Uy Vazifasi — Matematika, 5-sinf |
| Phase headers | `Heading 1` | PHASE 0-A: MAVZU KO'RIGI / Theme Preview |
| Sub-sections (segments, games) | `Heading 2` | 1-segment. Concrete |
| Questions / numbered items | `List Number` | 1. Savol: 325 146 da 2 qaysi xonada? |
| Bullet items (flash cards, W5H) | `List Bullet` | • 1-karta. 1 million = 1 000 000 |
| Answer markers | **Bold** in paragraph | **✅ Javob:** 20 000 |
| Hints | *Italic* in paragraph | *Hint: chapdan o'ngga yuz minglardan boshlang* |
| Metadata | `Normal` with bold labels | **Fan:** Matematika **Sinf:** 5 |

---

## Inline Tags — MANDATORY on Every Question

Every question, checkpoint, and game item MUST carry an inline tag at the end:

```
[Bloom: L1 | PISA: L1]                    — Phase 1 items
[Bloom: L1-L2 | PISA: L1-L2]              — Phase 2 checkpoints
[Bloom: L1-L3 | PISA: L1-L2]              — Phase 3 game items
[Bloom: L3-L4 | PISA: L2-L3]              — Phase 4 questions
[Bloom: L3-L5 | PISA: L2-L4 | Damage: -10 HP]  — Phase 6 boss questions
```

A question without a tag is INCOMPLETE. Do not skip this.

---

## Document Structure Summary

| Phase | Items | Bloom's | PISA | Answers | XP |
|-------|-------|---------|------|---------|-----|
| Header | Metadata table | — | — | — | — |
| 0-A Theme Preview | 8 components + gate quote + BOST goal | — | — | No | 0 |
| 0-B Flash Cards | 5-7 cards (G5) with visuals + 1 Common Mistake card | — | — | No | 0 |
| — | **[ MENING UY VAZIFAMNI BOSHLASH ]** | — | — | — | — |
| 1 Memory Sprint | 5-8 warm-up items from CURRENT chapter | L1 | L1 | Yes | 100/correct |
| 2 Story Mode | 3 CPA segments + 3 checkpoints (Muammo→Kurash→Kashfiyot→Yechim) | L1-L2 | L1-L2 | Yes | 0 |
| 3 Game Breaks | 3 games × 4-6 items (≥1 Interactive, ≥2 Default) | L1-L3 | L1-L2 | Yes | 50-400/game |
| 4 Real-Life Challenge | 1 scenario + W5H + 3 questions + Wise Status (30%) | L3-L4 | L2-L3 | Yes | 100-400 |
| 5 Consolidation | Buzan technique by content type + SMASHIN' SCOPE check | L1-L2 | — | — | 0 |
| 6 Final Boss | 3-5 Qs + hints + rubric (40/40/20 damage distribution) | L3-L5 | L2-L4 | Yes | 1×-5× |
| 7 Reflection | Summary + 3 prompts + BOST recall + spaced rep + closing | — | — | No | 0 |

---

## Progress Tracking: STATUS.md

After every docx, update STATUS.md:
- Table: file name, chapter, status (✅/🔄/❌), timestamp, issues
- Total progress counter
- This is your heartbeat — external monitoring reads it
