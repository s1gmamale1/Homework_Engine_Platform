---
subject: english
phase: final-challenge
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Final Challenge (Boss) — English (Hard only, all grades)

You are building the Final Challenge for an English homework session. This is the boss fight — HP combat. The student proves mastery of everything taught in this session.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for HP override rules — see below)

## Output

Boss questions with HP damage tags (count from CEFR level table). Mix of difficulty tiers.

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Level | HP | Question count | Essay requirement |
|:-:|:-:|:-:|---|
| A1 | 60 | 3 | none |
| A1+ | 60–80 | 3 | none |
| A2 | 80 | 3–4 | none |
| A2+ | 80 | 4 | none |
| B1 | 100 | 4 | 80-word paragraph |
| B1+ | 100–150 | 4–5 | 80-word paragraph |
| B2 | 150 | 5 | 150-word IELTS Task-2 |

**Grade HP override (applied when grade HP differs from level HP — take the higher value):**
- G5–6 grade default: 80 HP
- G7–8 grade default: 100 HP
- G9–11 grade default: 150 HP

When a G5 student has a detected level of A2 (HP 80) but grade default is also 80, these align. If a G7 student has a detected level of A1 (HP 60) but grade default is 100, take 100 — never punish higher-grade students with lower HP on detected-easier units.

**Tenses allowed by level (applies to all model answers):**
- **A1:** present simple + can + have got only
- **A2:** + past simple regular, going-to, have to
- **B1:** + past continuous, present perfect, will, 1st conditional, modals (should/might/could)
- **B2:** full arsenal — all tenses, inversion, cleft, participles, modal perfects

---

## Damage table (all levels)

| Difficulty | Damage | Distribution |
|-----------|:------:|:----------:|
| Easy | -10 HP | 40% |
| Medium | -20 HP | 40% |
| Hard | -30 HP | 20% |

---

## Question Construction

Every question tagged: `[UZ-ENG{G}-UNIT{N}-{SEQ}] | Bloom: L{N} | PISA: L{N} | Damage: -XX HP`

**Must include:**
- ≥1 reading/vocab-in-context Q (student reads a short text extract and answers)
- ≥1 production Q (write a paragraph, dialogue, or transform a sentence)
- B1 level: 1 short essay (~80 words, argument or description, level-allowed tenses)
- B2 level: 1 IELTS Task-2 argument essay (~150 words, 4-para: intro + 2 body + conclusion) + 1 register transformation (informal→formal) + 1 rhetorical analysis (name the device, explain the effect)

**MC restriction:**
- A1 level: up to 30% MC allowed (max 1 question out of 3)
- A2+ and above: **NO MC.** All open-ended with written production.

**Difficulty scaling:**
- Easy (-10 HP): single-skill recognition or controlled production (fill one blank in a fixed frame)
- Medium (-20 HP): 2-step task (read + produce OR identify + explain)
- Hard (-30 HP): multi-step with context (read + analyse + write + justify using level-allowed tenses)

**Visual question variants (B1+ levels):** a Hard-tier boss question may present an inline SVG instead of plain text — an IPA chart for the student to read and produce, a sentence-diagram tree with one branch missing, or a timeline diagram showing a tense sequence the student must convert to prose. Reserve for one question maximum per boss.

---

## Example: B1 level, 4-question distribution (present perfect unit)

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

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- Question count and HP from level table above. Grade HP override applies (take the higher value).
- Distribution 40/40/20 (easy/medium/hard)
- All questions from THIS chapter's content only
- Every question tagged with full inline tag format
- A1: up to 30% MC allowed. A2+ and above: no MC — all open-ended production
- Model answers use level-allowed tenses only — never a banned tense
- Hints cost HP, not free
- Language: student-facing English
- "Hali emas!" / "Not yet" — never "Noto'g'ri"
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
