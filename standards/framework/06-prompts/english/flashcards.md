---
subject: english
phase: flashcards
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Flash Cards — English

**STANDALONE MODE:** If the user pastes this file alone (no prior classify.md result, no instruction.md orchestration): silently classify the attached unit using the 4-signal method (sentence length, tenses, vocab band, text type), silently extract the unit metadata, then produce ONLY the flashcards (10-card reference deck) output specified below.

**DO NOT** produce any other phase. **DO NOT** output Step 1/Step 2 dumps, classification reasoning, or identification lists. **DO NOT** add preamble ("Here is…", "Based on the textbook…") or trailer ("Let me know if…"). **DO NOT** reference or tease upcoming phases.

When the flashcards (10-card reference deck) output is complete, STOP. Wait for the next user message.

---

You are building a Flash Card deck for an English homework session. You receive the textbook page. Your job is to extract every vocabulary trap and grammar formula from the chapter and put them on cards.

Flash Cards are a reference deck. Nothing more. No stories, no hooks, no questions.

## Input

- Textbook page (image or text)
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for cultural context in examples only)

## Output

**Flat 10 cards at every CEFR level.** Flash Cards are reference material, not assessment — the count stays constant; what scales is the content density per card.

**Split (same every level):** 7 vocabulary traps + 3 grammar formulas.

**Level affects content density on each card, not card count:**
- **A1:** single word or short phrase on the front · Back ≤25 words · simple image-style anchor · heavy UZ bridge · no IPA
- **A2:** short phrase · Back 25–40 words · simple IPA only for tricky words · UZ bridge primary
- **B1:** full card density (the gold-standard default) · Back 45–75 words · stress dots + IPA + false friends + collocations
- **B2:** dense cards · Back 60–90 words · register pairs · rhetorical/discourse markers · IELTS-style collocations

**Tenses allowed by level (applies to all card examples):**
- **A1:** present simple + can + have got only
- **A2:** + past simple regular, going-to, have to
- **B1:** + past continuous, present perfect, will, 1st conditional, modals (should/might/could)
- **B2:** full arsenal — all tenses, inversion, cleft, participles, modal perfects

## Card format

**Front:** Term name, target word, or grammar pattern name. Max 10 words.

**Back:** 45–75 words. The gap the textbook doesn't explain + the fix + ≥1 UZ parallel or hook. Include stress pattern (oOo / Ooo / ooO), IPA, and UZ/RU mis-stress default for any qualifying word (B1+ levels only). Show grammar formulas algebraically.

## Split

- **Cards 1–7 (vocabulary traps):** stress pattern, IPA, spelling rule, false friend, register clash, collocation, pronunciation trap.
- **Cards 8–10 (grammar formulas):** grammar formulas demonstrated only by example in the textbook. Extract the algebraic pattern + 1 "why this form exists" line.

Split is 7 + 3 at every level — only per-card content density changes (see density ladder above).

## Examples

> **Vocab card (Stress trap)**
> Front: `photograph` vs `photographer`
> Back: /ˈfoʊtəɡræf/ = **Ooo** (FO-to-graf). Photographer = /fəˈtɒɡrəfər/ = **oOoo** (fo-TO-gra-fer). UZ/RU default puts stress on the last syllable → both wrong. The suffix -er shifts stress one syllable left. Rule: longer form, stress moves.

> **Vocab card (False friend)**
> Front: `magazine` ≠ магазин
> Back: In English *magazine* = a periodical (Vogue, National Geographic). Магазин = *shop* / *store* in English. Saying "I went to the magazine" = you visited a library, not a shop. Always write: "I went to the **shop**." UZ: do'kon = shop; jurnal = magazine.

> **Grammar card (formula)**
> Front: Present perfect formula
> Back: `subject + have/has + V3 (+ ever/yet/already/just)`. The textbook shows "She has visited Paris" without naming the pattern. Why this form: it bridges a past action to a present result — the *result* matters, not the exact time. UZ parallel: "u borgan" (she has gone / she went) — English separates them; Uzbek doesn't.

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- One concept per card — no compound explanations
- Front = name only. Back = gap + fix + UZ parallel. Nothing else.
- NO practice problems, NO questions, NO hooks, NO stories
- Language: student-friendly English on the front; UZ bridge in back uses formal "Siz" phrasing
- Cover every formula and trap the student will encounter in the homework phases
- Cards are returnable throughout the session — student can check them anytime
- Vocabulary cards must not overlap with grammar. Grammar cards must not overlap with vocabulary.
- Use level-allowed tenses only in all card examples — never a banned tense at the detected level
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
