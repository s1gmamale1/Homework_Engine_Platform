---
subject: english
phase: reflection
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Reflection — English (Phase 7)

You are building the Reflection phase (final phase) for an English homework session. This is a quiet closing — no scoring, no pressure. Summarize what was learned, surface the weak spot, set up next review.

## Input

- All previous phase outputs
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for UZ location references and language calibration)
- English is always Hard mode

## Output

6 parts, ~2 minutes total.

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Level | Micro-exercises |
|:-:|:-:|
| A1 | 2 |
| A1+ | 2–3 |
| A2 | 3 |
| A2+ | 3 |
| B1 | 3 |
| B1+ | 3–4 |
| B2 | 4 |

Micro-exercises at A1/A2 are simpler (tap-level, one-word answers acceptable). At B1/B2 they are sentence-level.

---

## 1. Today's Results (2–3 lines)

List the session's topics with status markers:
- ✅ Strong topic — student showed mastery in Game Breaks or Boss
- ⚠️ Weak topic — student needed hints or made errors in Boss

Format:
> ✅ Present perfect formula — demonstrated correctly in Boss Q2
> ⚠️ Time adverb placement (yet / already) — error in Boss Q3

## 2. Micro-exercises

Count per level table above. Target the weak topics ONLY. Each has an answer.
- Tap-level difficulty at A1/A2 — not a second boss fight. Max 1 sentence per exercise.
- Sentence-level at B1/B2 — short production, not analysis.
- Cover the gap the student showed, using level-allowed tenses only.

Example (B1 weak topic: time adverb placement):
> a. Put "already" in the correct place: "She has finished the report." → She has **already** finished the report.
> b. True or False: "I haven't eaten yet" means I am still hungry now. → True.
> c. Complete: "Have you ___ been to Registan?" (ever/already) → ever.

## 3. BOST Check-In

> "Today you learned [goal from Preview Panel 2's key rule] — can you name it in one line?"

Student responds freely. Not scored. The goal string is pulled from Preview Panel 2's key rule.

Example: "Today you learned that present perfect = a bridge from a past action to a present result — can you name it in one line?"

## 4. Metacognitive Prompts (pick 3, rotate across sessions)

- "What was the hardest moment in today's session, and why?"
- "If a friend asked you to explain [today's grammar] in 30 seconds, what would you say?"
- "Where in your week this week could you actually use this?"
- "What does [today's key vocab word] mean in your life right now — not in English class?"
- "What would you search for to find out more about this topic?"

## 5. Spaced Repetition Schedule

> "Review these items: tomorrow · day 3 · day 7 · day 21"

List 2–3 specific items from this session the student should revisit — based on what appeared in the homework and what was weak.

Example:
> - Present perfect vs past simple contrast (appeared in Boss Q3)
> - Stress pattern: photographer /fəˈtɒɡrəfər/ (flashcard 1 — IPA noted)
> - Time adverbs: yet / already / just / ever — placement rules (weak topic from ⚠️)

## 6. Closing Line

- Score ≥60%: "Your precision builds the Third Renaissance."
- Score <60%: "Every session makes the next one easier. See you tomorrow."

Never punitive. Never "you failed."

---

## Example: B1 level reflection — past simple unit

> ✅ Past simple irregular verbs (go/went, see/saw, have/had) — Boss Q1 correct
> ⚠️ Did + base verb in questions — Boss Q2 error: "Did she went?" instead of "Did she go?"
>
> **Micro-exercises:**
> a. Fix: "Did she went to the IT Park?" → Did she **go** to the IT Park?
> b. True or False: "Did" already carries the past — so the main verb stays base form. → True.
> c. Write a question: ask about Kamola's job using did. → Did Kamola work at the Hilton last year?
>
> **BOST:** "Today you learned that did = the time machine — it carries all the past — can you name it in one line?"
>
> **Spaced repetition:** did + base verb rule · went/saw/had irregular trio · base verb after modal helpers

---

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- ~2 minutes, 6 parts
- Not scored — calm close
- Micro-exercises count per level table. Target weak topics only, not a full review.
- Micro-exercise complexity matches level: A1/A2 = tap or one-word; B1/B2 = short sentences.
- BOST string pulled from Preview Panel 2 — not invented
- Language: student-facing English. UZ bridge allowed in metacognitive prompts.
- Closing line is tied to score performance — never generic
- Summary must reference actual content from this session, not generic placeholders
- Use level-allowed tenses only in micro-exercise model answers — never a banned tense
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
