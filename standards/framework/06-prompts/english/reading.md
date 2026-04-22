---
subject: english
phase: reading
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Reading / Story Mode — English (Phase 2)

**STANDALONE MODE:** If pasted alone, silently classify the unit (4-signal method), silently extract metadata, then produce only the reading (story + checkpoints) output below. Stop when the phase is complete.

---

You are building the Reading phase (Phase 2) for an English homework session. This is ONE continuous narrative. The student reads it. The grammar and vocabulary arrive through story — never through labels.

## Input

- Textbook page (image or text)
- All previous phase outputs (Preview + Flash Cards + Sprint)
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for cultural setting, 55/45 UZ/global balance)

## Output

ONE continuous narrative + checkpoints (count from CEFR level table).

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Level | Word count | Paragraphs | Checkpoints |
|:-:|:-:|:-:|:-:|
| A1 | 100–200 | 1 | 3 |
| A1+ | 150–250 | 1–2 | 3 |
| A2 | 200–350 | 2 | 3 |
| A2+ | 280–420 | 2–3 | 3 |
| B1 | 380–550 | 3 | 3 |
| B1+ | 450–650 | 3 | 4 |
| B2 | 550–900 | 3–4 | 4–5 |

**Tenses allowed by level:**
- **A1:** present simple + can + have got only
- **A2:** + past simple regular, going-to, have to
- **B1:** + past continuous, present perfect, will, 1st conditional, modals (should/might/could)
- **B2:** full arsenal — all tenses, inversion, cleft, participles, modal perfects

---

## Narrative Construction

**Structure:** Problem → Struggle → Discovery → Solution. These beats are INVISIBLE INGREDIENTS — baked into the narrative. Do NOT label them. Do NOT write "Problem:" or "Segment 1:" anywhere. A reader should only notice the story, never the frame.

**Grammar delivery:** The chapter's target grammar appears in natural use, as a real speaker would use it. Never explain the grammar inside the narrative. Never make a character suddenly "announce" a rule.

**Vocabulary:** Target vocab items from this chapter (count from Flash Cards deck), bolded on first occurrence only. Do not gloss, define, or translate inline. The story context carries the meaning.

**Tenses:** Level-allowed set only. Never a banned tense — not even in dialogue.

**Setting:** Uzbekistan context for at least 55% of stories. Preferred: Silk Road city, Chorsu bozor, Samarkand school, Tashkent IT Park, Fergana village, Zarafshon riverbank, modern mahalla.

**Stranger Test:** A newcomer to the topic must be able to follow the plot without any prior knowledge of the chapter. The story stands alone.

---

## Example opening paragraph (B1 level, ~80 words, for voice reference)

> Kamola **arrived** at the Hilton Tashkent lobby at 8:55, five minutes before her first shift as a junior receptionist. The marble floor **reflected** the morning light, and guests **were already** moving in every direction. Her supervisor, Mr. Yusupov, handed her a printed schedule. "You **have worked** here for three days now," he said. "Today you **handle** the 9 a.m. check-ins alone." Kamola took a breath. She **had practised** every phrase the night before. Now it was real.

---

## Checkpoint Questions

Checkpoints count per level table above. Cover:
1. Main idea (what the narrative is about)
2. Inference (what the text implies but doesn't state)
3. Purpose (why a character did something OR why a particular word/form was used)
4. (B1+/B2 only) Language analysis — identify and explain a grammar or vocabulary choice in the text
5. (B2 only) Evaluation — assess the writer's approach or a character's decision

Format:
> **Q1.** What is the main challenge [character] faces in this story?
> [Bloom: L1–L2 | PISA: L1–L2]

Checkpoint 2 (inference) is the ideal spot for an inline sentence-structure SVG: split a single load-bearing sentence from the narrative into subject / verb / object branches so the student can literally see the grammar pattern they must infer.

---

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- ONE narrative only. Not multiple stories, not segmented passages.
- Zero segment labels — beats are invisible.
- Vocab items bolded on first occurrence, not glossed. Count from Flash Cards deck.
- Tenses: level-allowed set only. No exceptions.
- Grammar must appear naturally — never as a named demonstration inside the story.
- 55/45 national-pride balance. Modern 2020+ contexts for global settings.
- No bazaar/shopkeeper/farmer clichés in pro-role contexts.
- Checkpoints count per level table, each tagged `[Bloom: LX | PISA: LX]`.
- Checkpoint tags range: L1–L2 for main idea, L2–L3 for inference/purpose, L3–L4 for language analysis, L4–L5 for evaluation.
- Do NOT include a word count label inside the output — just meet it.
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
