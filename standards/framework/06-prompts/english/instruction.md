---
subject: english
phase: instruction
mode: hard
grades: 5-11
cefr: A1+ to B2
version: 1.0
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

## Step 2: Lock CEFR tier from the grade

Read the grade from the textbook cover or unit header. Lock tier from this table — never re-negotiate after lock.

| Grade | CEFR | Vocab | Avg Sentence | Bloom/PISA | Story Words |
|-------|------|-------|--------------|------------|-------------|
| G5–6 | A1+/A2 | 600–1200 | 9–12 words | L1–L3 / L1–L2 | 260–380 |
| G7 | A2+/B1 | 1200–2500 | 12–15 words | L1–L4 / L1–L2 | 380–550 |
| G8 | A2+/B1 | 1400–2700 | 12–15 words | L1–L4 / L1–L2 | 400–580 |
| G9–10 | B1/B1+ | 2500–4000 | 15–20 words | L2–L5 / L2–L3 | 550–750 |
| G11 | B2 | 4000–5500 | 18–25 words | L2–L6 / L3 | 700–900 |

**English is locked to HARD mode. Do not branch on difficulty.**
No classify.md step. No preview-easy.md. Pipeline always loads the full Hard phase set.

## Step 3: Load phase prompts in order

Read each file and hold its rules in context before building that phase:

1. `preview-hard.md` → Phase 0-A (8 swipe cards)
2. `flashcards.md` → Phase 0-B (10 reference cards)
3. `memory-sprint.md` → Phase 1 (5 warm-up items)
4. `reading.md` → Phase 2 (story + 3 checkpoints)
5. `game-breaks.md` → Phase 3 (3 games)
6. `real-life.md` → Phase 4 (pro-role scenario)
7. `consolidation.md` → Phase 5 (4-link mnemonic)
8. `final-challenge.md` → Phase 6 (boss fight)
9. `reflection.md` → Phase 7 (closing)

## Step 4: Build each phase

Feed previous outputs forward. Every phase may reference content produced in earlier phases.
Use only the textbook page as content source. Never invent grammar rules or vocabulary items not present in the source chapter.

## Step 5: Verify

Before outputting, check:
- [ ] CEFR tier locked and all outputs match tier parameters (sentence length, tenses, vocab)
- [ ] Tenses: grade-allowed set only — never a banned tense
- [ ] UZ↔EN bridge present (G5–6: every card; G7+: preview Cards 2, 5, 7 minimum)
- [ ] Stress + IPA on all 2+-syllable words with non-initial stress or UZ/RU mispronunciation (not below G7)
- [ ] 55/45 national-pride balance — Uzbekistan 55%, global 45%
- [ ] No meta-talk, no preamble, no "Here is the…" opener
- [ ] ASCII boxes consistent (~53 chars wide) on all swipe cards
- [ ] Tags on every Q, checkpoint, and boss item: `[Bloom: LX | PISA: LX]`
- [ ] Phase 1: tap-only formats only (MC4, T/F, YNNG) — no fill-in, no typing
- [ ] Phase 2: zero segment labels in the narrative — beats invisible
