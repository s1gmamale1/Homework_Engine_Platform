---
subject: english
phase: test-preview-bundle
mode: hard
grades: 5-11
cefr: detected inline (A1 to B2)
purpose: chat-mode standalone preview test — bundles classify + preview-hard + execution directive
version: 1.0
not-for-pipeline: true
use-for-pipeline: instruction.md + classify.md + preview-hard.md as separate steps
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Preview Test — English (Standalone Chat Bundle)

**THIS IS A STANDALONE CHAT-TEST PROMPT.** You will output ONE thing only: the complete 8-panel Preview phase in the exact format specified below. Do NOT output the identification list. Do NOT stop at classification. Do NOT ask clarifying questions. Detect the level silently and proceed directly to producing the 8 panels.

---

## Step 1: Read the attached unit

Extract silently (do NOT output these): unit number, unit title, 2–3 big ideas, 10 vocabulary traps, grammar formulas shown only by example, target tenses, page refs.

## Step 2: Detect CEFR level silently

Measure four signals on the unit: avg sentence length (≤6→A1, 7–9→A1+, 9–12→A2, 11–14→A2+, 12–16→B1, 15–20→B1+, 18–25→B2), tenses present, B1+ vocab proportion, text type. Pick the mode level across the four signals. If tied, pick higher. **Do NOT output the level as a separate step** — log it internally and use it to parameterize the output below.

Grade-default priors (use only if signals are ambiguous): G5→A1, G6→A1+, G7→A2+/B1, G8→B1, G9→B1+, G10→B1+/B2, G11→B2.

## Step 3: PRODUCE 8 PANELS — this is your only output

Begin output immediately with the header. No preamble like "Here is the preview" or "Based on the textbook".

---

### OUTPUT HEADER (produce exactly this format)

```
# UNIT {N}.{L} — {Unit Title}
**Standard:** UZ-ENG{G}-UNIT{N}-{SEQ}
**Textbook:** {publisher}, pages {range}  ·  **CEFR:** {detected level}
**Duration:** 2–3 min (no timer, no XP, no penalty)
**UI:** 8 swipe cards, progress dots, [ START MY HOMEWORK ] on Card 8
```

### 8 PANELS IN ORDER (each in a ~53-char-wide ASCII box, ~18 lines tall)

#### Panel 1 — 📖 Summary
2 big ideas in plain student-English. Optional 1-line attributed quote (≤125 chars) — prefer Navoiy, Ibn Sino, Malala, Obama, Rowling.
Sentence count by level: A1: 4–5 · A2: 6–7 · B1: 8–10 · B2: 10–12.

#### Panel 2 — 💡 Better Explanation
The hidden rule or trick the book never states. One mental model OR one algebraic grammar formula (e.g. `(Wh-) + did + subject + base verb + ?`).
**Mandatory UZ↔EN bridge** — map the English structure to the Uzbek equivalent.
**SVG strongly encouraged:** past/present/future timeline, stress-dot pattern (Ooo/oOoo), or sentence-diagram tree.
B1+ levels only: add stress pattern + IPA for 2+-syllable trap words.

#### Panel 3 — 📝 Examples
3 examples lifted from the chapter with page refs. Bold the target form. One example must demonstrate Panel 2's rule. Never invent. Annotate any spelling trap or false friend on the line.

#### Panel 4 — 🌍 Real-Life Research
How this concept lives in the world right now + one Uzbekistan parallel. 2020+ sources (BBC, Tashkent IT Park, NASA Artemis, Samarkand tourism). Concrete, dateable.

#### Panel 5 — 💭 Word → Structure Translation
Teach the student HOW to read an English sentence, identify the target, and produce it.
Mini-cases by level: A1: 1 · A2: 2 · B1: 2–3 · B2: 3.
Each mini-case: real-world sentence → extract pattern → show UZ↔EN mapping → produce.
**SVG strongly encouraged:** sentence-diagram tree or word-family tree.

#### Panel 6 — ⚡ Industry Application
2–3 roles from the grade-appropriate pro-roles list:
- **G5–6:** Chorsu bozor helper, school monitor, mahalla football captain, Samarkand kid-tourist guide
- **G7–8:** Tashkent IT intern, Hilton receptionist, BBC Tashkent reporter, airline ground staff
- **G9–10:** BBC stringer, UN interpreter trainee, Uzbekistan Airways customer-service lead, IELTS tutor
- **G11:** IELTS Task-2 essayist, TEDx Tashkent speaker, UCAS personal-statement writer, startup pitcher

For each role: concrete task + what breaks if English is wrong.

#### Panel 7 — 🧠 Mental Model
One visual or analogy that compresses the lesson into a single image. "did = time machine", "present perfect = bridge past→now", "passive = spotlight on action", "modals = remote control for certainty".
**Apply UZ↔EN bridge to the analogy itself.**
**SVG strongly encouraged:** render the analogy (bridge, spotlight, remote, time machine) or a Buzan mind map.

#### Panel 8 — 🚀 Why This Matters + What's Next
Two parts:
1. What BREAKS if you don't know this (mistimed verb, failed interview, embarrassing false friend)
2. What OPENS UP (DTM confidence, competitive applications, clear speaking)

End with BOST prompt: `Bugun [topic] ni nimani bilmoqchisiz?`
Include the 9-phase table (0-A ✓, 0-B → 7 queued) + [ START MY HOMEWORK ] CTA.

---

### Each panel closes with (inside the box at the bottom):
`[ ● ○ ○ ○ ○ ○ ○ ○ ]   Swipe →` (filled dot advances: Card 1 = ●○○○○○○○, Card 2 = ○●○○○○○○, etc.)

### Immediately OUTSIDE the box:
`[Bloom: LX | PISA: LX]`

### After Card 8:
`🇺🇿 Did you know? {≤40 words, real 2020+ Uzbekistan statistic tied to the topic}`

---

## HARD CONSTRAINTS (do not violate)

- **Language:** student-friendly English. Formal "Siz" in UZ bridge lines only — never "sen".
- **Avg sentence length:** A1 ≤9 words · A2 9–12 · B1 12–16 · B2 18–25.
- **Tenses allowed by level:**
  - A1: present simple + can + have got only
  - A2: + past simple regular, going-to, have to
  - B1: + past continuous, present perfect, will, 1st conditional, modals (should/might/could)
  - B2: full arsenal (all tenses, inversion, cleft, participles, modal perfects)
- **Never use a banned tense** — not even in examples.
- **UZ↔EN bridge MANDATORY on Panels 2, 5, 7** at minimum. A1 levels: every panel.
- **55/45 Uzbekistan/global balance.** No cowboy/cricket/baseball clichés.
- **Every panel uses bold target form on real chapter examples.** Never invent sentences not in the source.
- **SVG priority:** SVG > Mermaid > ASCII. Use SVG for timelines, stress dots, IPA charts, sentence diagrams, word-family trees, collocation grids, Buzan mind maps. Keep under 300×200px.
- **ASCII boxes** for the 8-panel UI chrome — they are the card layout, not the teaching visual.
- **No meta-talk.** No "Here is the preview". No trailing "Let me know if…". Output starts with the `# UNIT` header.

## Value-Add Law

Every panel MUST do at least ONE of:
- (a) REVEAL what the textbook shows but never explains (stress pattern, spelling rule, grammar formula by example, false friend, register clash, collocation)
- (b) SIMPLIFY a complex rule via ≤1-sentence mental model, analogy, or explicit UZ↔EN bridge

A panel that only restates the textbook → DELETE and replace.

---

**START OUTPUT NOW.** Begin with the `# UNIT` header. No preamble.
