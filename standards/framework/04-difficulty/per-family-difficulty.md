---
name: per-family-difficulty
status: v0.1 draft — validated against §22 only
layer: 4 (difficulty)
source: UNIFIED §17 lines 3365-3399 + 02-families/family-aniq-fanlar.md + 00-core/hp-damage-baseline.md
---

# Per-Family Difficulty Parameters

Damage values and base HP pools are defined in `00-core/hp-damage-baseline.md`. This file documents **family-specific HP overrides**, **session durations**, **Bloom targets by mode × grade band**, and **game availability by grade**.

---

## HP Pool by Family and Grade Band

| Family | G1–4 | G5–6 | G7–8 | G9–11 |
|--------|:----:|:----:|:----:|:-----:|
| Aniq Fanlar — Matematika | 50 | **80** (override) | n/a | n/a |
| Aniq Fanlar — Algebra | n/a | n/a | 100 | n/a |
| Aniq Fanlar — Geometriya | n/a | n/a | 100 | n/a |
| Aniq Fanlar — Algebra va Analiz | n/a | n/a | n/a | 150 |
| Aniq Fanlar — Geometriya (Advanced) | n/a | n/a | n/a | 150 |
| Tabiy Fanlar (Bio / Physics / Chem) | 50 | 100 | 100 | 150 |
| Til Fanlar (English / Ona Tili / Rus) | 50 | 100 | 100 | 150 |
| Ijtimoiy Fanlar (History subjects) | 50 | 100 | 100 | 150 |

> The Matematika G5–6 override (80 HP) is the only subject-specific HP override currently defined. All other subjects inherit the grade-band defaults from `00-core/hp-damage-baseline.md`.

---

## Session Duration by Grade Band

Source: UNIFIED §17.2.

| Grade Band | Standard Mode | Extended Mode | Recovery Mode |
|------------|:-------------:|:-------------:|:-------------:|
| G1–2 | 15–20 min | 30 min | 10–15 min |
| G3–4 | 20–25 min | 35–40 min | 15–20 min |
| G5–8 | 20–30 min | 40–50 min | 15–20 min |
| G9–11 | 25–30 min | 45–50 min | 20–25 min |

Pre-session (Phase 0-A + 0-B) adds ~3–5 min (optional, student-paced, not counted toward XP or assessment).

---

## Bloom Target Distribution by Mode and Grade Band

Targets expressed as the predominant Bloom range expected across graded components in that mode.

| Grade Band | Easy mode | Hard mode |
|------------|-----------|-----------|
| G1–4 | L1–L2 (Remember / Understand) | L2–L3 (Understand / Apply) |
| G5–6 | L2–L3 (Understand / Apply) | L3–L4 (Apply / Analyze) |
| G7–8 | L3 (Apply) | L3–L5 (Apply / Analyze / Evaluate) |
| G9–11 | L3–L4 (Apply / Analyze) | L4–L6 (Analyze / Evaluate / Create) |

These are session-level targets. Individual item tiers within the Boss follow the 40/40/20 distribution (see `04-difficulty/item-tier-distribution.md`).

---

## Bloom Targets by Family — Hard Mode Focus

Families differ in which Bloom levels are prioritised in hard-mode phases.

| Family | Sprint focus | Games focus | Real-Life / Reading focus | Boss focus |
|--------|-------------|-------------|--------------------------|------------|
| Aniq Fanlar | L1–L2 (recall) | L3–L4 (apply / analyze) | L4–L5 (analyze / evaluate) | L3–L6 (tiered, 40/40/20) |
| Tabiy Fanlar | L1–L2 (recall) | L3–L4 (apply / analyze) | L4–L5 (analyze / evaluate) | L3–L6 (tiered) |
| Til Fanlar | L2 (understand) | L3–L4 (apply / analyze) | L3–L4 (Reading comprehension) | L3–L5 (tiered) |
| Ijtimoiy Fanlar | L1–L2 (recall) | L3–L4 (apply / analyze) | — (skipped) | L3–L5 (tiered) |

---

## Game Availability by Grade

Source: UNIFIED §17.1. Family-specific modifications noted.

| Game / Component | G1–2 | G3–4 | G5–6 | G7–8 | G9–11 |
|------------------|:----:|:----:|:----:|:----:|:-----:|
| Memory Sprint | 4 Qs, simplified | Standard | Standard | Standard | Standard |
| Story Mode | Heavy visuals | Balanced | Balanced | Text-heavy | Text-heavy |
| Tile Match | 4 pairs | 6 pairs | 6–8 pairs | 8 pairs | 8 pairs |
| Sentence Fill | Full word bank | Full word bank | Partial word bank | No word bank | No word bank |
| Memory Palace | Not available | Intro (3 items) | Full (5 items) | Full | Full |
| Flashcards | Simple | Standard | Standard | Standard | Self-directed |
| Adaptive Quiz | Simplified | Standard | Standard | IRT-calibrated | IRT-calibrated |
| Mystery Box | Not available | 3 boxes | 3–5 boxes | 5 boxes | 5 boxes |
| Movement Breaks | REQUIRED | REQUIRED | Optional | Disabled | Disabled |
| Why Chain | 2 levels | 3 levels | 3–4 levels | 4–5 levels | 5+ levels |
| Peer Teaching | Not available | Not available | Available | Available | Available |
| Real-Life Challenge | Simplified | Standard | Standard | Extended | Extended |
| Final Boss | 50 HP, MC ok | 50 HP, MC ok | 100 HP (80 Mat), mixed | 100 HP, open | 150 HP, open |
| Reflection Journal | 1 prompt, verbal | 1 prompt | 2 prompts | 2 prompts | 3 prompts |
| Creative Lab | Not available | Not available | Available (L3+) | Available (L3+) | Available (L3+) |

---

## Aniq Fanlar — Subject Delta Overrides

| Subject | Grade Range | HP | Notable Modifiers |
|---------|:-----------:|:--:|-------------------|
| Matematika | G1–4 | 50 | MC allowed in Boss; Movement Breaks REQUIRED |
| Matematika | G5–6 | 80 | No MC in Boss; HP override from default 100 |
| Algebra | G7–9 | 100 | No MC; IRT-calibrated Adaptive Quiz mandatory |
| Geometriya | G7–9 | 100 | No MC; Puzzle Lock (Interactive) preferred in Slot 3 |
| Algebra va Analiz | G10–11 | 150 | No MC; Flash Cards self-directed; Why Chain 5+ levels; Capture ≥1 per 2 sessions |
| Geometriya (Advanced) | G10–11 | 150 | No MC; Proof-based Final Challenge only; Spatial Puzzle Lock preferred Slot 3 |

---

## Notebook Capture Frequency by Grade

Applies to Aniq Fanlar and Tabiy Fanlar (calculation/derivation phases).

| Grade Band | Minimum Capture Frequency |
|------------|--------------------------|
| G1–4 | Not available |
| G5–8 | ≥ 1 capture per 3 sessions |
| G9–11 | ≥ 1 capture per 2 sessions |

Full capture rule: `00-core/capture-rule.md`.

---

## Cross-references

- `00-core/hp-damage-baseline.md` — canonical HP values, damage table, hint tax, combo bonus
- `04-difficulty/item-tier-distribution.md` — 40/40/20 distribution and Bloom targets per tier
- `04-difficulty/phase-weights.md` — scoring weights per mode per family
- `02-families/family-aniq-fanlar.md` — full Aniq Fanlar mode routing and family rules
- UNIFIED §17 — full game availability matrix and session duration table (source of §17.1 and §17.2 tables above)
