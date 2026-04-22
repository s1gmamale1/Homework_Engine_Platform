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

## What these cards ARE and what they are NOT

These cards are a **reference deck** the student reads BEFORE the homework starts. They are the student's "cheat sheet" — information to absorb, not questions to answer.

They are **NOT**:
- Fill-in-the-blank exercises (that's Sentence Fill, Phase 3)
- Short-answer questions (that's Memory Sprint, Phase 1)
- Practice problems of any kind
- Cloze deletions (Anki-style gap cards)

If your output looks like a sentence with `__________` and the student's job is to fill it in, you are producing the WRONG PHASE. Delete and restart.

---

## Pre-Flight — list the 10 traps BEFORE writing any card

Before producing any card, output nothing yet. Silently do this:

1. Scan the attached unit for pronunciation traps (2+ syllable words with non-initial stress, silent letters, schwa, -tion/-sion rules)
2. Scan for false friends with Russian or Uzbek (magazine, actually, principal, library, sympathy, etc.)
3. Scan for register clashes (formal/informal pairs in the unit)
4. Scan for collocations the textbook uses but doesn't name (make a decision, earn a living, take part)
5. Scan for grammar patterns demonstrated by example only (extract formulas)

Pick the **top 10 traps** from those five categories: 7 vocabulary traps + 3 grammar formulas.

If the unit has fewer than 7 real vocab traps — DO NOT PAD with simple dictionary-style words ("receptionist = a person at reception"). Output fewer cards instead. Padding with simple definitions is worse than a shorter deck.

---

## Card Format — MANDATORY STRUCTURED TEMPLATE

Every vocabulary card uses this **EXACT ASCII-box template with 5 labeled fields**. These field labels REPLACE any old "GAP:" / "FIX:" / "Answer:" labels.

```
┌─────────────────────────────────────────────────────┐
│  {single term — max 10 words, never a sentence}     │
├─────────────────────────────────────────────────────┤
│  PRONUNCIATION: /IPA/ — Ooo (stress dots)           │
│  UZ BRIDGE:     {UZ word/phrase} = {EN equivalent}  │
│  TRAP:          {what UZ/RU speakers get wrong}     │
│  COLLOCATION:   {3 natural phrases using the word}  │
│  FROM THE BOOK: {actual sentence from unit, target  │
│                  word bolded — copy verbatim}       │
└─────────────────────────────────────────────────────┘
```

Grammar formula cards use a parallel 5-field template:

```
┌─────────────────────────────────────────────────────┐
│  {pattern name — e.g. "Past simple negative"}       │
├─────────────────────────────────────────────────────┤
│  FORMULA:       subject + didn't + base verb        │
│  WHY:           {one-line reason the form exists}   │
│  UZ BRIDGE:     {UZ suffix or structure equivalent} │
│  WRONG WAY:     {what learners typically say}       │
│  FROM THE BOOK: {actual sentence from unit, target  │
│                  form bolded — copy verbatim}       │
└─────────────────────────────────────────────────────┘
```

**The field labels are mandatory.** Write exactly `PRONUNCIATION:`, `UZ BRIDGE:`, `TRAP:`, `COLLOCATION:`, `FROM THE BOOK:` (or `FORMULA:`, `WHY:`, `UZ BRIDGE:`, `WRONG WAY:`, `FROM THE BOOK:` for grammar). Never invent alternative labels. Never use `GAP:`, `FIX:`, `Note:`, `Rule:`, `Answer:`.

**If a word lacks a real trap, do not create a card for it.** A word like "manager" or "pilot" with no stress issue, no false friend, no register clash, no interesting collocation — skip it. Padding with these simple words is a failure mode, not a feature.

---

## WRONG OUTPUT — reject and rewrite if you produce anything like this

```
┌─────────────────────────────────────────────────────┐
│  NEGATIVE FORM                                      │
├─────────────────────────────────────────────────────┤
│  GAP: She __________ (not get) any money for work.  │
│  FIX: She didn't get any money for work.            │
│  UZ: U ish uchun pul olmadi.                        │
└─────────────────────────────────────────────────────┘
```

This is a Sentence Fill exercise (Phase 3), not a flash card. Three problems:

1. **The labels `GAP:` and `FIX:` are banned.** Use `FORMULA:`, `WHY:`, etc. from the mandatory template.
2. **The front "NEGATIVE FORM" is too vague.** Name the actual grammar pattern: "Past simple — negative formula".
3. **The content is a sentence with a blank.** Flash cards have no blanks. Ever.

If you produce output like this, stop, delete the card, and rewrite using the mandatory template above.

## Split

- **Cards 1–7 (vocabulary traps):** stress pattern, IPA, spelling rule, false friend, register clash, collocation, pronunciation trap.
- **Cards 8–10 (grammar formulas):** grammar formulas demonstrated only by example in the textbook. Extract the algebraic pattern + 1 "why this form exists" line.

Split is 7 + 3 at every level — only per-card content density changes (see density ladder above).

## Examples (use these exact shapes — Front = name, Back = teaching)

### Card 1 — Stress trap (vocabulary) — use this exact shape

```
┌─────────────────────────────────────────────────────┐
│  photographer                                       │
├─────────────────────────────────────────────────────┤
│  PRONUNCIATION: /fəˈtɒɡrəfər/ — oOoo (fo-TO-gra-fer)│
│  UZ BRIDGE:     suratkash = photographer            │
│  TRAP:          UZ/RU default stresses last         │
│                 syllable → wrong. "-er" shifts      │
│                 stress one syllable LEFT.           │
│  COLLOCATION:   professional photographer,          │
│                 wedding photographer, work as a     │
│                 photographer                        │
│  FROM THE BOOK: "Daniel worked as a **photographer**│
│                  for a fashion magazine." (p. 34)   │
└─────────────────────────────────────────────────────┘
```

### Card 2 — False friend (vocabulary) — use this exact shape

```
┌─────────────────────────────────────────────────────┐
│  magazine ≠ магазин                                 │
├─────────────────────────────────────────────────────┤
│  PRONUNCIATION: /ˌmæɡəˈziːn/ — ooO (ma-ga-ZEEN)     │
│  UZ BRIDGE:     jurnal = magazine · do'kon = shop   │
│  TRAP:          RU магазин = shop/store in English, │
│                 NOT magazine. "I went to the        │
│                 magazine" = you went to a library,  │
│                 not a shop.                         │
│  COLLOCATION:   fashion magazine, read a magazine,  │
│                 appear in a magazine                │
│  FROM THE BOOK: "Daniel took photos for a fashion   │
│                  **magazine**." (p. 34)             │
└─────────────────────────────────────────────────────┘
```

### Card 8 — Grammar formula (pattern name) — use this exact shape

```
┌─────────────────────────────────────────────────────┐
│  Past simple — negative formula                     │
├─────────────────────────────────────────────────────┤
│  FORMULA:       subject + didn't + base verb        │
│  WHY:           English splits past-negative into   │
│                 helper "did" + base verb. Only ONE  │
│                 past marker — "did" — never two.    │
│  UZ BRIDGE:     UZ suffix "-ma-di" = EN "didn't" +  │
│                 base. ishla-madi = didn't work.     │
│  WRONG WAY:     ❌ "She didn't got money"            │
│                 ❌ "She no got money"                │
│  FROM THE BOOK: "He **didn't use** buses or planes."│
│                  (p. 34)                            │
└─────────────────────────────────────────────────────┘
```

**Notice every example:** Front = single term or pattern name only. Back = 5 mandatory labeled fields. Zero `__________` blanks. Zero `GAP:` / `FIX:` labels. Every `FROM THE BOOK:` line is an actual textbook sentence with the target form bolded — never invented.

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- One concept per card — no compound explanations
- Front = term/word/formula NAME only. No sentence. No blank. No question mark.
- Back = pure teaching (IPA, stress, UZ bridge, formula, register, collocation). NO sentence with a blank. NO "correct answer" reveal.
- **NEVER** use the labels `GAP:` / `FIX:` / `Note:` / `Rule:` / `Answer:` on the card
- **NEVER** include `__________` blanks — those belong to Sentence Fill (Phase 3), not Flash Cards
- NO practice problems, NO questions, NO hooks, NO stories
- If a card looks like a fill-in-the-blank with a "correct answer" below it — DELETE and rewrite as a reference card
- Skip simple dictionary-style vocabulary (receptionist = a person at a reception). Only build a card if there is a real TRAP to warn about (stress, false friend, register, collocation, spelling, grammar formula)
- Language: student-friendly English on the front; UZ bridge in back uses formal "Siz" phrasing
- Cover every formula and trap the student will encounter in the homework phases
- Cards are returnable throughout the session — student can check them anytime
- Vocabulary cards must not overlap with grammar. Grammar cards must not overlap with vocabulary.
- Use level-allowed tenses only in all card examples — never a banned tense at the detected level
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
