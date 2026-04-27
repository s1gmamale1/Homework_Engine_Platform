---
name: phase-weights
status: v0.1 draft — validated against §22 only
layer: 4 (difficulty)
source: UNIFIED §22 session + easy-mode.md + hard-mode.md
---

# Phase Weights

Scoring weights per mode per family. All values are **proposals pending pilot calibration**.

## Pass Threshold

| Mode | Pass threshold |
|------|:--------------:|
| Easy | 60% of graded components |
| Hard | 60% of graded components |

## Easy Mode — All Families

Structure is identical across all 4 families in Easy mode.

| Phase | Component | Scoring Weight |
|-------|-----------|:--------------:|
| 0-A | Preview | — (not scored) |
| 0-B | Flash Cards | — (not scored) |
| 1 | Memory Sprint | 20% |
| 3 | Game Breaks | 50% |
| 7 | Reflection | — (analytics / 30% implicit routing) |
| | **Total graded** | **70%** |

> Note: Reflection contributes 30% implicitly for session routing purposes (remediation decisions). It is not graded as a scored component.

Phases 2, 4, 5, 6 are **skipped** in Easy mode.

---

## Hard Mode — Per Family

### Aniq Fanlar (Math)

Active phases: Sprint → Games → Real-Life → (Consolidation) → Boss

| Phase | Component | Scoring Weight |
|-------|-----------|:--------------:|
| 0-A | Preview | — |
| 0-B | Flash Cards | — |
| 1 | Memory Sprint | 10% |
| 3 | Game Breaks | 30% |
| 4 | Real-Life Challenge | 30% |
| 5 | Consolidation | — (conditional; not scored separately) |
| 6 | Final Challenge (Boss) | 30% |
| 7 | Reflection | — |
| | **Total graded** | **100%** |

### Tabiy Fanlar (Science)

Active phases: Sprint → Games → Real-Life → (Consolidation) → Boss

| Phase | Component | Scoring Weight |
|-------|-----------|:--------------:|
| 0-A | Preview | — |
| 0-B | Flash Cards | — |
| 1 | Memory Sprint | 10% |
| 3 | Game Breaks | 30% |
| 4 | Real-Life Challenge | 30% |
| 5 | Consolidation | — (conditional; not scored separately) |
| 6 | Final Challenge (Boss) | 30% |
| 7 | Reflection | — |
| | **Total graded** | **100%** |

### Til Fanlar (Language)

Active phases: Sprint → Reading → Games → Boss  
Phase 4 (Real-Life) and Phase 5 (Consolidation) are skipped.

| Phase | Component | Scoring Weight |
|-------|-----------|:--------------:|
| 0-A | Preview | — |
| 0-B | Flash Cards | — |
| 1 | Memory Sprint | 10% |
| 2 | Reading | 15% |
| 3 | Game Breaks | 45% |
| 6 | Final Challenge (Boss) | 30% |
| 7 | Reflection | — |
| | **Total graded** | **100%** |

### Ijtimoiy Fanlar (History)

Active phases: Sprint → Games → Boss  
Phases 2, 4, 5 are skipped.

| Phase | Component | Scoring Weight |
|-------|-----------|:--------------:|
| 0-A | Preview | — |
| 0-B | Flash Cards | — |
| 1 | Memory Sprint | 10% |
| 3 | Game Breaks | 50% |
| 6 | Final Challenge (Boss) | 40% |
| 7 | Reflection | — |
| | **Total graded** | **100%** |

---

## Summary Grid

| Family | Mode | Sprint | Reading | Games | Real-Life | Boss | Total |
|--------|------|:------:|:-------:|:-----:|:---------:|:----:|:-----:|
| All | Easy | 20% | — | 50% | — | — | 70% |
| Aniq Fanlar | Hard | 10% | — | 30% | 30% | 30% | 100% |
| Tabiy Fanlar | Hard | 10% | — | 30% | 30% | 30% | 100% |
| Til Fanlar | Hard | 10% | 15% | 45% | — | 30% | 100% |
| Ijtimoiy Fanlar | Hard | 10% | — | 50% | — | 40% | 100% |

---

## Notes

- Consolidation (Phase 5) fires conditionally (≥2 interlocking concepts). It is folded into the Games weight when active; it does not carry an independent weight.
- "Not scored" phases (Preview, Flash Cards, Reflection) still gate or inform routing — they are excluded from the percentage denominator.
- Easy mode's 70% total (rather than 100%) reflects the omission of Boss and Real-Life scoring. The 30% gap is absorbed by Reflection routing logic, not re-distributed to remaining components.
- All weights are proposals. Pilot calibration will determine final values.

## Cross-references

- `00-core/hp-damage-baseline.md` — Boss phase (Phase 6) damage and HP values
- `03-modes/easy-mode.md` — Easy mode component list and scaling
- `03-modes/hard-mode.md` — Hard mode component list per family
- `04-difficulty/per-family-difficulty.md` — Grade-band Bloom targets and HP overrides
