---
subject: english
phase: game-breaks
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Game Breaks — English (Phase 3)

**STANDALONE MODE:** If pasted alone, silently classify the unit (4-signal method), silently extract metadata, then produce only the game breaks (3 games) output below. Stop when the phase is complete.

---

You are building the Game Breaks (Phase 3) for an English homework session. This is where active practice begins. The student applies what they learned in Preview through gamified repetition.

## Input

- Textbook page (image or text)
- Preview + Flash Cards + Sprint + Reading outputs (from previous steps)
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for game content complexity calibration)
- English is always Hard mode → always **3 games**

## Output

3 games. Items per game by detected CEFR level. Every item tagged `[Bloom: LX | PISA: LX]`.

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Level | Items per game |
|:-:|:-:|
| A1 | 4 |
| A1+ | 4 |
| A2 | 4–5 |
| A2+ | 5 |
| B1 | 5–6 |
| B1+ | 6 |
| B2 | 6 |

---

## Available Games (v1 pool — pick from these only)

| Game | How it works | Good for |
|------|-------------|----------|
| **Tile Match** | Student drags pairs to match. Items per level above. | Word ↔ meaning, term ↔ UZ bridge, collocation ↔ context |
| **Sentence Fill** | Statement with a gap; student selects the missing piece. | Grammar slot, correct tense form, register choice |
| **Memory Match** | 4×4 flip grid, find matching pairs. | Vocab ↔ definition, form ↔ name, IPA ↔ word |
| **Speed Sort** | Items to sort into two or more categories before time. | Tense sort, register sort (formal/informal), word-class sort |

**Banned games (never reference):** Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker. No exceptions.

## Game Selection

English has no mandatory game. Pick based on what fits the chapter content:
- Vocabulary-heavy chapter → Tile Match (word ↔ meaning pairs)
- Grammar-pattern chapter → Sentence Fill (fill the correct tense/form)
- Mixed vocab + grammar → Tile Match + Sentence Fill + Speed Sort
- B2 level: must include ≥1 IELTS collocation match or academic cloze item

---

## Construction per game

### Tile Match
- Items per level from table above
- Left tile: target word, phrase, or grammar pattern name
- Right tile: UZ bridge, definition, or real-world use example
- A1: word ↔ UZ meaning · A2: collocation ↔ natural context · B1: formal ↔ informal register pair · B2: academic collocation ↔ citation context
- Tile Match pairs may carry inline SVG anchors (a tiny stress-dot diagram, IPA glyph, or word-family mini-tree on the left tile) whenever the visual speeds recognition.

### Sentence Fill
- Items per level from table above
- Show a sentence or short dialogue with one piece missing
- Gap must test grammar understanding — not random word removal
- A1: "She ___ (go) to school every day." (answer: goes) · A2: tense-choice between two forms · B1: modal + base verb choice · B2: inversion or cleft gap
- Use level-allowed tenses only in all model answers

### Memory Match
- 4×4 grid (8 pairs)
- Flip two cards, find matching pairs
- A1: word ↔ picture clue · A2: IPA ↔ word · B1: idiom ↔ meaning · B2: rhetorical device ↔ example

### Speed Sort
- Items sorted into 2 categories (count per level table above)
- A1: present/past sort · A2: formal/informal register sort · B1: defining/non-defining relative clause sort · B2: active/passive, or academic/general register sort

---

## Example: Tile Match (5 pairs, B1 level)

| Left tile | Right tile |
|-----------|------------|
| `have/has + V3` | present perfect |
| `photographer` | oOoo — /fəˈtɒɡrəfər/ |
| `magazine` | journal/periodical (NOT a shop) |
| `She has worked there.` | present result, no time given |
| `Hilton Tashkent` | 5-star hotel, Uzbekistan context |

Answer key: 1↔c, 2↔d, 3↔e, 4↔b, 5↔a *(adjust to actual pairing format)*

---

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- 3 games always (English = Hard mode always)
- Every item tagged: `[Bloom: LX | PISA: LX]`
- Bloom L1–L3, PISA L1–L2 for all Game Breaks items
- B2 level must include ≥1 IELTS collocation or academic cloze item
- Full answer key for every game
- Current chapter content only — no items from other chapters
- Language: student-facing English. No Uzbek inside game items unless it's a UZ↔EN bridge tile.
- Use level-allowed tenses only in all model answers — never a banned tense
- No frozen/removed games (see banned list above)
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
