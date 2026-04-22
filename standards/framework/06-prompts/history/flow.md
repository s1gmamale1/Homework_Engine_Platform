# History — Prompt Flow

## Flow

```
preview → flashcards → memory-sprint → game-breaks → consolidation? → final-challenge → reflection
```

All sessions run the same 7-phase flow. **Consolidation (Phase 5) is conditional** on ≥2 interlocking concepts — almost always builds for History.

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview.md` | 4 panels (1, 2, 3, 6) + gate quote + Memory Palace (5–10 thematic stations) |
| 2 | `flashcards.md` | 8 cards in 3 clusters (Names / Frameworks / Modern Echoes) with Xotira tasviri on every card |
| 3 | `memory-sprint.md` | 7 tap-only items: 3 MC + 2 T/F + 2 YNNG, ≥1 "Aytilmagan" correct, Buzan Primacy ordering |
| 4 | `game-breaks.md` | 3 games: Tile Match (cause↔effect) + Memory Match (⭐ Von Restorff anchor on Slot 2) + Sentence Fill (≥1 source-quote fill) |
| 5 | `consolidation.md` | Memory Palace full walkthrough — all stations, self-check per station, final verification prompt (SKIP if single-concept lesson) |
| 6 | `final-challenge.md` | Boss fight, 5 questions, 100 HP, damage −10/−20/−30, NO multiple choice, ≥1 primary source analysis, ≥1 causal-framework question, Hint 3s = diagnostic questions |
| 7 | `reflection.md` | 5 parts: summary + BOST goal mirror + thinking question + spaced repetition + Milliylik/TEFCAS closing line |

**Skipped phases** (never built for History):

- Phase 2 Reading — language-family only
- Phase 4 Real-Life — narrative absorbs transfer
- Panel 4 Origin — the lesson's narrative IS the origin

---

## Assembly

All phase outputs are assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order.

Orchestrator: `instruction.md` handles extraction → parameters → phase build loop → verification checklist.

---

## Notes

- **Covers:** O'zbekiston Tarixi (G5–11) + Jahon Tarixi (G6–11)
- **Subject parameter:** `O'zbekiston Tarixi` or `Jahon Tarixi` — passed to every phase prompt
- **Milliylik intensity:** `high` (O'zbekiston, 55/45 national/global) or `low` (Jahon, 20/80)
- **Games:** Tile Match + Memory Match + Sentence Fill. Default Pool only — dual-catalog rule waived for History v1 because Interactive games (Why Chain, Territory Conquest, Reaction Chain) are frozen to v2+. No Adaptive Quiz, no Notebook Capture (non-calc family).
- **Teaching:** Buzan-heavy recall scaffolding — Memory Palace built in Preview, walked in Consolidation; Xotira tasviri hooks on every flashcard; primary source analysis + Historian's Method in Panel 3
- **Weights:** Sprint 10% + Games 50% + Boss 40% = 100% graded
- **Pass threshold:** 60% overall
- **Boss format:** short answer + open reasoning only (no multiple choice); Hint 3s are diagnostic questions, never answer templates
- **All content in Uzbek, "Siz" formal; never "sen".** Pipeline/meta language stays English.
