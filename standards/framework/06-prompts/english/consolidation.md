---
subject: english
phase: consolidation
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Consolidation — English (Phase 5)

**STANDALONE MODE:** If pasted alone, silently classify the unit (4-signal method), silently extract metadata, then produce only the consolidation (memory palace stations) output below. Stop when the phase is complete.

---

You are building the Consolidation phase (Phase 5) for an English homework session. Purpose: lock the session's concepts into long-term memory using a mnemonic technique before the Final Challenge.

English is always Hard mode. Consolidation always fires — skip logic does not apply.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for Memory Palace location concreteness — grade-anchored)

## Output

One mnemonic exercise. Stations per level (see table). ~3 minutes total.

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Level | Stations | Technique emphasis |
|:-:|:-:|---|
| A1 | 3 | Simple image pairing (Peg or Palace with concrete locations) |
| A1+ | 3 | Simple image pairing |
| A2 | 4 | Link System or Palace |
| A2+ | 4 | Link System or Palace |
| B1 | 4 | Palace, Link, or Radiant Summary |
| B1+ | 4 | Palace, Radiant Summary, or Link |
| B2 | 4 (abstract) | Radiant Summary or Link with abstract connections |

A1/A1+ keeps image anchors very concrete. B2 pushes abstract conceptual links (e.g., linking grammar rules to logical consequences rather than physical images).

---

## Pick a technique based on content structure

| Content structure | Technique | How to build |
|-------------------|-----------|-------------|
| **Hierarchical** (word families, grammar rule-sets) | **Radiant Summary** | Center = main concept. 3–5 branches = sub-rules or word variants. Each branch has one image + the rule. Student fills in missing branches. |
| **Sequential** (tense chain, verb form chain) | **Link System** | Steps of the tense/form pattern chained into a vivid story. Each step links to the next through an exaggerated image or action. |
| **Spatial** (job vocab, neighbourhood words, prepositions, topic vocabulary) | **Memory Palace** | Concepts placed at locations in a real Uzbek space. See location guidance below. |
| **Discrete** (random unconnected new words) | **Peg System** | Each word paired with a vivid, impossible image. Student recalls word from image and image from word. |
| **Numeric** (dates, centuries, historical years) | **Major System** | Digits mapped to consonant sounds. Build a word/phrase from the digits. |

Pick ONE technique. Keep it to the station count from the level table above — this is a quick lock, not a deep exercise.

---

## Memory Palace — Uzbek location anchors (grade-anchored)

When choosing Palace technique, use Uzbek locations. Grade shapes the concreteness of the location choice:

- **G5–6:** Prefer the student's own maktab corridor or mahalla street for maximum concreteness. Named landmarks are fine but secondary.
- **G7–11:** Use named national landmarks — Registan, Chorsu bozor, Bibi-Khanym mosque, Hazrati Imam library — for cross-session consistency and cultural anchoring.

Standard palace image anchors:
- Registan gate: a doppi-wearing horse blocking the entrance, shouting the grammar formula
- Chorsu bozor dome: a giant schwa symbol rolling through the vegetable stalls
- Bibi-Khanym arch: a figure in a chapan writing an IELTS essay on the ancient tiles
- Hazrati Imam library: a shelf where every book spine spells an irregular verb
- Student's maktab corridor: lockers labelled with target tenses, each glowing a different colour

Apply SMASHIN' SCOPE qualities where natural: Substitution, Movement, Association, Absurdity (replace Sexuality for student content), Humour, Imagination, Number, Colour, Order, Positive image, Exaggeration.

Each station benefits from an inline SVG illustration: render the location as a simple line drawing with the station's image overlaid. A visual anchor doubles retention over text-only description.

---

## Example: 4-station Memory Palace (Registan, B1 level — present perfect unit)

> Technique: Memory Palace — Registan, Samarkand

> **Station 1 — Registan gate (Kok-Gumbaz portal)**
> Concept: "have/has + V3 = result NOW matters"
> Image: A giant flying carpet labelled "V3" has just landed at the gate. It is still steaming — it arrived from the past but it's HERE now.

> **Station 2 — Central courtyard (open square)**
> Concept: present perfect banned when time is named ("last Tuesday")
> Image: A calendar page labelled "LAST TUESDAY" is handcuffed to a guard who will not let "have" through the gate. The verb "have" is waiting outside, sad.

> **Station 3 — Tilla-Kori minaret (left tower)**
> Concept: ever / yet / already / just — placement after "have"
> Image: Four tiny acrobats standing on each other's shoulders: JUST (bottom), ALREADY, YET, EVER (top, waving a flag). They never leave the minaret.

> **Station 4 — Sherdor facade (right archway)**
> Concept: have vs has — subject decides
> Image: A lion (has — single, powerful, grammar boss) on the left arch. A flock of doves (have — plural) flying out of the right arch. The arch knows its subject.

---

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- Stations count per level table above.
- ONE technique only per session
- ~3 minutes total — this is a calm moment before the Final Challenge
- No scoring in this phase
- Images must be vivid, exaggerated, and culturally anchored (UZ 55% / global 45%)
- Language: student-facing English. Station labels in English. UZ location name in parentheses.
- Technique choice must match the content structure — never default to Palace unless content is spatial
- G5–6: prefer student's own maktab/mahalla for Palace technique (grade anchor — concrete first)
- G7–11: prefer named national landmarks for Palace technique (grade anchor — cultural consistency)
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
