# SCHEMA — Output Format

## Output: One `.md` Per Chapter

**Naming:** `{Subject}_Grade{N}_Ch{N}S{S}_{lang}.md`
**Examples:** `Matematika_Grade5_Ch1S1_uz.md` · `Biologiya_Grade7_Ch3_uz.md`

---

## Markdown Heading Conventions

| Element | Markdown | Example |
|---------|----------|---------|
| Document title | `# H1` | `# NETS Uy Vazifasi — Matematika, 5-sinf, 1-bob` |
| Phase headers | `## H2` | `## PHASE 0-A: MAVZU KO'RIGI / Theme Preview` |
| Sub-sections (segments, games) | `### H3` | `### 1-segment. Concrete` |
| Questions / numbered items | `1.` numbered list | `1. Savol: 325 146 da 2 qaysi xonada?` |
| Bullet items (flash cards, W5H) | `- ` bullet list | `- 1-karta. 1 million = 1 000 000` |
| Answer markers | `**bold**` | `**✅ Javob:** 20 000` |
| Hints | `*italic*` | `*Hint: chapdan o'ngga yuz minglardan boshlang*` |
| Metadata | Bold labels | `**Fan:** Matematika **Sinf:** 5` |
| Inline tags | Plain text in brackets | `[Bloom: L1 \| PISA: L1]` |
| Horizontal rules | `---` | Between phases |

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
| 0-A Theme Preview | 8 panels (1-5: 8-10 sentences each; 6-8: 5-10 sentences) + gate quote + BOST goal | — | — | No | 0 |
| 0-B Flash Cards | Formulas, concepts, rules, terms ONLY (no practice items) + 1 Common Mistake card | — | — | No | 0 |
| — | **[ MENING UY VAZIFAMNI BOSHLASH ]** | — | — | — | — |
| 1 Memory Sprint | 5-8 tap-only items: MC, True/False, Yes/No/Not Given. NO typing. | L1 | L1 | Yes | 100/correct |
| 2 Story Mode | 3 CPA segments as flowing narrative (use arc as invisible blueprint, NO section labels) + 3 checkpoints | L1-L2 | L1-L2 | Yes | 0 |
| 3 Game Breaks | 3 games × 4-6 items (≥1 Interactive, ≥2 Default) | L1-L3 | L1-L2 | Yes | 50-400/game |
| 4 Real-Life Challenge | 1 scenario + W5H + 3 questions + Wise Status (30%) | L3-L4 | L2-L3 | Yes | 100-400 |
| 5 Consolidation | Buzan technique by content type + SMASHIN' SCOPE check | L1-L2 | — | — | 0 |
| 6 Final Boss | 3-5 Qs + hints + rubric (40/40/20 damage distribution) | L3-L5 | L2-L4 | Yes | 1×-5× |
| 7 Reflection | Summary + 3 prompts + BOST recall + spaced rep + closing | — | — | No | 0 |

---

## Pronoun Policy

All Uzbek content uses **"Siz"** (formal/respectful). Never "sen". See UNIFIED §4.4 Design Rules.

---

## Progress Tracking: STATUS.md

After every .md file, update STATUS.md:
- Table: file name, chapter, status (✅/🔄/❌), timestamp, issues
- Total progress counter
- This is your heartbeat — external monitoring reads it
