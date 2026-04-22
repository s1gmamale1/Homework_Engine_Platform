---
subject: english
phase: instruction
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# English — Homework Builder Instruction

You are building a homework session for English (G5–G11). Follow these steps in order.

## Step 1: Identify the lesson

You receive a grade + unit reference (e.g., "Grade 7 English, Unit 4 — Jobs and Workplaces").

Find and read the corresponding textbook pages. Extract:
- Topic name and unit title
- 2–3 big ideas a student could name in one breath
- 10 vocabulary items (traps, stress patterns, spelling, false friends, register)
- Grammar formulas shown only by example (extract algebraically)
- Page refs for every example you will use
- Target tenses present in the chapter
- One UZ↔EN bridge per big idea

## Step 2: Detect CEFR level

Run `classify.md` on the unit. Measure all four signal axes (sentence length, tenses, vocabulary band, text type). Output one level: `A1` · `A1+` · `A2` · `A2+` · `B1` · `B1+` · `B2`.

**Carry this detected level forward through all phases.** All quantitative parameters (question counts, word counts, card counts, tense complexity) are driven by this level — not by the grade.

Grade-default reference for mismatch checking:

| Grade | Default level |
|:-:|:-:|
| G5 | A1 |
| G6 | A1+ |
| G7 | A2+/B1 |
| G8 | B1 |
| G9 | B1+ |
| G10 | B1+/B2 |
| G11 | B2 |

If the detected level differs from the grade default, log the mismatch here before proceeding. Signals override grade default when they disagree by more than one level.

## Step 3: Identify grade (for cultural anchors only)

Read the grade from the textbook cover or unit header. The grade drives:
- Phase 4 pro-roles (real-life.md)
- Memory Palace location concreteness (consolidation.md — G5–6 may use student's own maktab/mahalla)

Note if grade default level and classify.md detected level differ. Do not re-negotiate the detected level.

## Step 4: Load phase prompts in order

Read each file and hold its rules in context before building that phase:

1. `preview-hard.md` → Phase 0-A (swipe cards — count from CEFR level table)
2. `flashcards.md` → Phase 0-B (reference cards — count from CEFR level table)
3. `memory-sprint.md` → Phase 1 (warm-up items — count from CEFR level table)
4. `reading.md` → Phase 2 (story + checkpoints — length from CEFR level table)
5. `game-breaks.md` → Phase 3 (3 games — items per game from CEFR level table)
6. `real-life.md` → Phase 4 (pro-role scenario — questions from CEFR level table, role from grade)
7. `consolidation.md` → Phase 5 (mnemonic — stations from CEFR level table)
8. `final-challenge.md` → Phase 6 (boss fight — questions + HP from CEFR level table)
9. `reflection.md` → Phase 7 (closing — micro-exercises from CEFR level table)

## Step 5: Build each phase

Feed previous outputs forward. Every phase may reference content produced in earlier phases.
Use only the textbook page as content source. Never invent grammar rules or vocabulary items not present in the source chapter.

Apply the detected CEFR level for all quantitative parameters. Apply the grade for cultural anchors (pro-roles in Phase 4, location concreteness in Phase 5).

## Step 6: Verify

Before outputting, check:
- [ ] CEFR level detected and logged (Step 2). Mismatch with grade default noted if present.
- [ ] All quantitative outputs match the detected level parameters (question count, word count, card count, tense set)
- [ ] **Level-appropriate question counts?** (from classify.md → phase tables)
- [ ] **Grade-appropriate pro-roles?** (from grade → real-life.md pro-role table)
- [ ] Tenses: level-allowed set only — never a banned tense
- [ ] UZ↔EN bridge present (A1: every card; A2+: preview Cards 2, 5, 7 minimum)
- [ ] Stress + IPA on all 2+-syllable words with non-initial stress or UZ/RU mispronunciation (B1+ levels only)
- [ ] 55/45 national-pride balance — Uzbekistan 55%, global 45%
- [ ] No meta-talk, no preamble, no "Here is the…" opener
- [ ] ASCII boxes consistent (~53 chars wide) on all swipe cards
- [ ] Tags on every Q, checkpoint, and boss item: `[Bloom: LX | PISA: LX]`
- [ ] Phase 1: tap-only formats only (MC4, T/F, YNNG) — no fill-in, no typing
- [ ] Phase 2: zero segment labels in the narrative — beats invisible
