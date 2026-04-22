---
subject: english
phase: flashcards
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.2
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Flash Cards — English

**STANDALONE MODE:** If pasted alone, silently classify the unit (4-signal method), silently extract metadata, then produce only the flashcard deck below. Stop when the 10 cards are written.

You are building a Flash Card reference deck for an English homework session. The student opens the deck before the homework starts and returns to it anytime during the session. It is a cheat-sheet of language traps — pronunciation, false friends, collocations, register, grammar formulas — extracted from the chapter.

## Input

- Textbook page (image or text)
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for cultural context in examples only)

## Output

**10 cards** at every level. Split: **7 vocabulary + 3 grammar**. Level affects per-card density, not count:

| Level | Vocab card Back length | IPA | Stress dots | Register / collocation |
|-------|:----------------------:|:---:|:-----------:|:----------------------:|
| A1 | ≤25 words | no | no | no — UZ bridge only |
| A2 | 25–40 words | tricky words only | no | light |
| B1 | 45–75 words (gold standard) | yes | yes | yes |
| B2 | 60–90 words | yes | yes | yes + rhetorical/discourse |

**Tenses in examples** — use only the level-allowed set:

- **A1:** present simple + can + have got
- **A2:** + past simple regular, going-to, have to
- **B1:** + past continuous, present perfect, will, 1st conditional, modals
- **B2:** full arsenal (all tenses, inversion, cleft, participles, modal perfects)

## Pre-Flight — scan the unit for traps

Silently scan the chapter for items in these 5 categories, then pick the top 10 (7 + 3):

1. **Pronunciation traps** — 2+ syllable words with non-initial stress, silent letters, schwa, -tion / -sion rules
2. **False friends** — EN word that looks like a UZ or RU word but means something different (magazine ≠ магазин, actually ≠ актуально, principal ≠ principle)
3. **Register clashes** — formal/informal pairs (gonna/going to, kids/children)
4. **Collocations the book uses but doesn't name** — make a decision, earn a living, take part in
5. **Grammar patterns shown by example only** — extract the formula algebraically

If the unit yields fewer than 7 real vocab traps, output fewer cards. A short deck of real traps beats a padded deck of dictionary definitions.

## Card template

Every vocabulary card fills these 5 fields:

```
┌─────────────────────────────────────────────────────┐
│  {single term — max 10 words}                       │
├─────────────────────────────────────────────────────┤
│  PRONUNCIATION: /IPA/ — Ooo (stress dots)           │
│  UZ BRIDGE:     {UZ word/phrase} = {EN equivalent}  │
│  TRAP:          {what UZ/RU speakers get wrong}     │
│  COLLOCATION:   {3 natural phrases using the word}  │
│  FROM THE BOOK: {verbatim sentence, target bolded}  │
└─────────────────────────────────────────────────────┘
```

Every grammar card fills these 5 fields:

```
┌─────────────────────────────────────────────────────┐
│  {pattern name — e.g. "Past simple negative"}       │
├─────────────────────────────────────────────────────┤
│  FORMULA:       {algebraic pattern}                 │
│  WHY:           {one-line reason the form exists}   │
│  UZ BRIDGE:     {UZ suffix or structure equivalent} │
│  WRONG WAY:     {learner error with ❌}             │
│  FROM THE BOOK: {verbatim sentence, target bolded}  │
└─────────────────────────────────────────────────────┘
```

Write the labels exactly as shown: `PRONUNCIATION:` · `UZ BRIDGE:` · `TRAP:` · `COLLOCATION:` · `FROM THE BOOK:` for vocabulary; `FORMULA:` · `WHY:` · `UZ BRIDGE:` · `WRONG WAY:` · `FROM THE BOOK:` for grammar.

The `FROM THE BOOK:` line is always a real sentence from the attached chapter with the target word or form in **bold**. If the word doesn't appear in the chapter, use a different word — the card must trace to the source.

## Examples

### Stress trap

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

### False friend

```
┌─────────────────────────────────────────────────────┐
│  magazine ≠ магазин                                 │
├─────────────────────────────────────────────────────┤
│  PRONUNCIATION: /ˌmæɡəˈziːn/ — ooO (ma-ga-ZEEN)     │
│  UZ BRIDGE:     jurnal = magazine · do'kon = shop   │
│  TRAP:          RU магазин = shop / store in EN,    │
│                 NOT magazine. "I went to the        │
│                 magazine" = you went to a library,  │
│                 not a shop.                         │
│  COLLOCATION:   fashion magazine, read a magazine,  │
│                 appear in a magazine                │
│  FROM THE BOOK: "Daniel took photos for a fashion   │
│                  **magazine**." (p. 34)             │
└─────────────────────────────────────────────────────┘
```

### Grammar formula

```
┌─────────────────────────────────────────────────────┐
│  Past simple — negative formula                     │
├─────────────────────────────────────────────────────┤
│  FORMULA:       subject + didn't + base verb        │
│  WHY:           English splits past-negative into   │
│                 helper "did" + base. Only ONE past  │
│                 marker — "did" — never two.         │
│  UZ BRIDGE:     UZ suffix "-ma-di" = EN "didn't" +  │
│                 base. ishla-madi = didn't work.     │
│  WRONG WAY:     ❌ "She didn't got money"            │
│                 ❌ "She no got money"                │
│  FROM THE BOOK: "He **didn't use** buses or planes."│
│                  (p. 34)                            │
└─────────────────────────────────────────────────────┘
```

## Rules

- One concept per card
- Cover every trap the student will meet in later phases of this homework
- Language: student-friendly English on the front; UZ bridge uses formal "Siz"
- Level-allowed tenses only in every example
- Cards stay accessible throughout the session — the student can return to them anytime
- **Visuals:** Generate inline SVG where a visual aids the teaching — stress-dot patterns (Ooo / oOoo as rendered dots), IPA charts, word-family trees (suffix branching off a root). Mermaid for decision trees or grammar-rule flowcharts. Keep under 300×200px, legible on mobile, placed immediately after the text it illustrates.
