---
subject: english
phase: final-challenge
mode: hard
grades: 5-11
cefr: A1+ to B2
version: 1.0
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Final Challenge (Boss) — English (Hard only, all grades)

You are building the Final Challenge for an English homework session. This is the boss fight — HP combat. The student proves mastery of everything taught in this session.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Grade: G5–G11 (English)

## Output

3–5 boss questions with HP damage tags. Mix of difficulty tiers.

---

## HP and Damage

| Grade | HP |
|-------|:--:|
| G5–6 | **80** |
| G7–8 | **100** |
| G9–10 | **150** |
| G11 | **150** |

| Difficulty | Damage | Distribution |
|-----------|:------:|:----------:|
| Easy | -10 HP | 40% |
| Medium | -20 HP | 40% |
| Hard | -30 HP | 20% |

---

## Question counts by grade

- G5–6: 3 questions
- G7–8: 4 questions
- G9–10: 5 questions
- G11: 5 questions

---

## Question Construction

Every question tagged: `[UZ-ENG{G}-UNIT{N}-{SEQ}] | Bloom: L{N} | PISA: L{N} | Damage: -XX HP`

**Must include:**
- ≥1 reading/vocab-in-context Q (student reads a short text extract and answers)
- ≥1 production Q (write a paragraph, dialogue, or transform a sentence)
- G9–10: 1 short essay (~80 words, argument or description, grade-allowed tenses)
- G11: 1 IELTS Task-2 argument essay (~150 words, 4-para: intro + 2 body + conclusion) + 1 register transformation (informal→formal) + 1 rhetorical analysis (name the device, explain the effect)

**MC restriction:**
- G5: up to 30% MC allowed (max 1 question out of 3)
- G6+: **NO MC.** All open-ended with written production.

**Difficulty scaling:**
- Easy (-10 HP): single-skill recognition or controlled production (fill one blank in a fixed frame)
- Medium (-20 HP): 2-step task (read + produce OR identify + explain)
- Hard (-30 HP): multi-step with context (read + analyse + write + justify using grade-allowed tenses)

**Visual question variants (G7+):** a Hard-tier boss question may present an inline SVG instead of plain text — an IPA chart for the student to read and produce, a sentence-diagram tree with one branch missing, or a timeline diagram showing a tense sequence the student must convert to prose. Reserve for one question maximum per boss.

---

## Example: G7 — 4-question distribution (present perfect unit)

> **Q1** `[UZ-ENG7-UNIT4-01] | Bloom: L2 | PISA: L1 | Damage: -10 HP`
> Read the sentence: "Scientists have discovered a new species in the Zarafshon river delta."
> What tense is used, and why is it correct here — not past simple?

> **Q2** `[UZ-ENG7-UNIT4-02] | Bloom: L3 | PISA: L2 | Damage: -10 HP`
> Write 2 sentences about Tashkent IT Park using present perfect. Each sentence must use a different time adverb (already / yet / just / ever / never / recently).

> **Q3** `[UZ-ENG7-UNIT4-03] | Bloom: L4 | PISA: L2 | Damage: -20 HP`
> A student wrote: "She has visited Paris last summer." Find the error, explain why it is wrong, and rewrite the sentence correctly. Then write a second sentence about the same topic using past simple correctly.

> **Q4** `[UZ-ENG7-UNIT4-04] | Bloom: L5 | PISA: L3 | Damage: -30 HP`
> You are a BBC Tashkent junior reporter. Write a 40-word news paragraph about the Samarkand UNESCO Heritage Festival using at least 2 present perfect sentences and 1 past simple sentence. Your paragraph must flow naturally — not a list of grammar examples.

---

## Hint Ladder (applies to all questions)

If student is stuck:
- Hint 1: -5 HP. Remind which grammar rule or vocabulary item applies.
- Hint 2: -5 HP. Show the formula structure or the first clause.
- Hint 3: -5 HP. Show the frame; student completes the content.

## Failure Response

Wrong answer → "Hali emas!" / "Not yet" — never "Noto'g'ri" / "Wrong."
Show WHY the correct answer is correct. Route back to the relevant Preview card.

---

## Rules

- Question count: 3 (G5–6) / 4 (G7–8) / 5 (G9–10, G11)
- Distribution 40/40/20 (easy/medium/hard)
- All questions from THIS chapter's content only
- Every question tagged with full inline tag format
- G6+: no MC — all open-ended production
- Model answers use grade-allowed tenses only — never a banned tense
- Hints cost HP, not free
- Language: student-facing English
- "Hali emas!" / "Not yet" — never "Noto'g'ri"
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
