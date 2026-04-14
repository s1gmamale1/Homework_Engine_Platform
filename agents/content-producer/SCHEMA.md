# SCHEMA — Output Format

## Output: One `.docx` Per Chapter

**Naming:** `{Subject}_Grade{N}_Ch{N}_{lang}.docx`
**Examples:** `Matematika_Grade5_Ch1_uz.docx` · `Biologiya_Grade7_Ch3_uz.docx`

---

## Document Structure Summary

| Phase | Items | Bloom's | PISA | Answers | XP |
|-------|-------|---------|------|---------|-----|
| Header | Metadata table | — | — | — | — |
| 0-A Theme Preview | 8 components (summary, explanation, examples, origin, hook, relevance, industry, resources) | — | — | No (exploration) | 0 |
| 0-B Flash Cards | All formulas + concepts + rules for this chapter | — | — | No (reference) | 0 |
| — | **[ START MY HOMEWORK ]** | — | — | — | — |
| 1 Memory Sprint | 5-8 recall items (flexible format) | L1 | L1 | Yes | 100/correct |
| 2 Story Mode | 3 segments + 3 checkpoints | L1-L2 | L1-L2 | Yes | 0 |
| 3 Game Breaks | 3 games × 4-6 items | L1-L3 | L1-L2 | Yes | 50-400/game |
| 4 Real-Life Challenge | 1 scenario + 3 questions | L3-L4 | L2-L3 | Yes | 100-400 |
| 5 Consolidation | 5 memory anchors (Buzan) | L1-L2 | — | — | 0 |
| 6 Final Boss | 3-5 questions + hints + rubric | L3-L5 | L2-L4 | Yes | 1×-5× |
| 7 Reflection | 3 prompts + summary + next lesson | — | — | No | 0 |

---

## Docx Formatting

- **Heading 1:** Document title
- **Heading 2:** Phase labels (e.g., "1-FAZA: XOTIRA SPRINT — 2 daqiqa")
- **Heading 3:** Segments, game names, boss questions
- **Bold:** Section labels, game names, answer markers (✅ Javob:)
- **Italic:** Socratic hints, metadata tags, teacher notes
- **Numbered lists:** Questions within each phase
- **Tables:** Header metadata, optional per-phase info blocks
- **All text in assignment language** (uz or ru)

---

## Progress Tracking: STATUS.md

Alongside the docx files, maintain a `STATUS.md` with:
- Table of all chapters: file name, status (✅/🔄/❌), timestamp, issues
- Total progress counter
- This file is the agent's heartbeat — updated after every docx creation

See SKILLS.md for the exact STATUS.md format.
