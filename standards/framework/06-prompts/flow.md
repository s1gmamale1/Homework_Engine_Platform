# Prompt Flow — How Homework Gets Built

## Step 0: Classify

Run `classify.md` on the textbook page → outputs **EASY** or **HARD**.

---

## Easy Flow (5 phases)

```
classify → preview-easy → flashcards → memory-sprint (5 items) → game-breaks (2 games) → reflection
```

| Step | Prompt file | What it produces |
|------|-------------|-----------------|
| 1 | `preview-easy.md` | 5 panels (Concept, Explanation, Examples, Origin, Industry) |
| 2 | `flashcards.md` | 5-8 cards (name + formula) |
| 3 | `memory-sprint.md` | 5 tap-only items (MC/TF/YNNG) |
| 4 | `game-breaks.md` | 2 games (Adaptive Quiz mandatory + 1 other) |
| 5 | `reflection.md` | Summary + question + spaced rep + closing |

**Skipped:** Real-Life, Consolidation, Final Challenge.

---

## Hard Flow (8 phases)

```
classify → preview-hard → flashcards → memory-sprint (7 items) → game-breaks (3 games) → real-life → consolidation (if 2+ concepts) → final-challenge → reflection
```

| Step | Prompt file | What it produces |
|------|-------------|-----------------|
| 1 | `preview-hard.md` | 7 panels (+ Word→Formula/Phenomenon→Formula + Why This Matters) |
| 2 | `flashcards.md` | 8-12 cards |
| 3 | `memory-sprint.md` | 7 tap-only items |
| 4 | `game-breaks.md` | 3 games (Adaptive Quiz mandatory + 2 others) |
| 5 | `real-life.md` | 1 scenario, 4-6 sub-questions, first-person expert |
| 6 | `consolidation.md` | Mnemonic lock (SKIP if single concept) |
| 7 | `final-challenge.md` | Boss fight, 4-6 questions, HP combat |
| 8 | `reflection.md` | Summary + question + spaced rep + closing |

---

## Assembly

Each step feeds the next. Output of preview → informs flashcards → informs sprint → etc. Final homework = all phase outputs concatenated in order.

## Per-subject folders

Same flow, different content rules:

| Folder | Subjects |
|--------|----------|
| `math-algebra/` | Matematika G5-6, Algebra G7-9 |
| `physics/` | Fizika G7-11 |
| *(future)* | Chemistry, Biology, Geometry, History, Languages |

Each folder has the same file set. `flashcards.md` and `reflection.md` are universal (copied across).
