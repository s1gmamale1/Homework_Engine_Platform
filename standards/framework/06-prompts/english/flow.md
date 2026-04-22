# English — Prompt Flow

## Step 0: Classify

Run `classify.md` on the textbook unit → output Mode (EASY/HARD) + CEFR Level.

---

## Easy (5 phases)

```
classify → preview-easy → flashcards → memory-sprint → game-breaks → reflection
```

Used for: vocabulary-only units, recognition-task units, review chapters with no new grammar.

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-easy.md` | 5 panels: Summary, Explanation, Examples, Real-Life, Industry |
| 2 | `flashcards.md` | Front/Back cards — count from CEFR tier |
| 3 | `memory-sprint.md` | Tap-only items (MC/TF/YNNG) — count from CEFR tier |
| 4 | `game-breaks.md` | 2 games (1 Adaptive Quiz + 1 other) |
| 5 | `reflection.md` | Summary + question + spaced rep + closing |

**Skipped:** Reading, Real-Life, Consolidation, Final Challenge.

---

## Hard (8 phases)

```
classify → preview-hard → flashcards → memory-sprint → reading → game-breaks → real-life → consolidation? → final-challenge → reflection
```

Used for: units introducing new grammar, production tasks, multi-paragraph reading, Word→Structure teaching.

| Step | Prompt | Output |
|------|--------|--------|
| 1 | `preview-hard.md` | 8 panels: Summary, Explanation, Examples, Real-Life Research, Word→Structure, Industry, Mental Model, Why This Matters |
| 2 | `flashcards.md` | Front/Back cards — count from CEFR tier |
| 3 | `memory-sprint.md` | Tap-only items from prior unit |
| 4 | `reading.md` | One continuous narrative + 3-5 checkpoints |
| 5 | `game-breaks.md` | 3 games (1 Adaptive Quiz + 2 others) |
| 6 | `real-life.md` | 1 scenario, 4-6 sub-questions, first-person pro-role |
| 7 | `consolidation.md` | Mnemonic lock (SKIP if single grammar/vocab concept) |
| 8 | `final-challenge.md` | Boss fight, 4-6 questions, HP by grade |
| 9 | `reflection.md` | Summary + question + spaced rep + closing |

---

## Assembly

All phase outputs are assembled into a single `.md` file — that is the final homework. Each phase becomes a section in order. Stamp Mode + CEFR Level at the top of the assembled file.

---

## Notes

- Covers: English G5-11
- CEFR level drives quantitative parameters (card count, sentence length, tenses, word count)
- Grade drives cultural anchors (pro-roles in real-life.md, location concreteness in consolidation.md)
- Games: Adaptive Quiz (mandatory), Tile Match, Memory Match, Sentence Fill
- Teaching: CPA for grammar, UZ↔EN bridge required, no invented content
- All content student-facing English; UZ bridge lines use formal "Siz"
