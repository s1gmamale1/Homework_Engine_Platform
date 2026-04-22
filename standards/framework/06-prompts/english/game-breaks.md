---
subject: english
phase: game-breaks
mode: hard
grades: 5-11
cefr: A1+ to B2
version: 1.0
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Game Breaks — English (Phase 3)

You are building the Game Breaks (Phase 3) for an English homework session. This is where active practice begins. The student applies what they learned in Preview through gamified repetition.

## Input

- Textbook page (image or text)
- Preview + Flash Cards + Sprint + Reading outputs (from previous steps)
- Grade: G5–G11 (English)
- English is always Hard mode → always **3 games**

## Output

3 games. Each game has 4–6 items. Every item tagged `[Bloom: LX | PISA: LX]`.

---

## Available Games (v1 pool — pick from these only)

| Game | How it works | Good for |
|------|-------------|----------|
| **Tile Match** | Student drags pairs to match. 4–6 pairs. | Word ↔ meaning, term ↔ UZ bridge, collocation ↔ context |
| **Sentence Fill** | Statement with a gap; student selects the missing piece. | Grammar slot, correct tense form, register choice |
| **Memory Match** | 4×4 flip grid, find matching pairs. | Vocab ↔ definition, form ↔ name, IPA ↔ word |
| **Speed Sort** | Items to sort into two or more categories before time. | Tense sort, register sort (formal/informal), word-class sort |

**Banned games (never reference):** Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker. No exceptions.

## Game Selection

English has no mandatory game. Pick based on what fits the chapter content:
- Vocabulary-heavy chapter → Tile Match (word ↔ meaning pairs)
- Grammar-pattern chapter → Sentence Fill (fill the correct tense/form)
- Mixed vocab + grammar → Tile Match + Sentence Fill + Speed Sort
- G11: must include ≥1 IELTS collocation match or academic cloze item

---

## Construction per game

### Tile Match
- 4–6 pairs
- Left tile: target word, phrase, or grammar pattern name
- Right tile: UZ bridge, definition, or real-world use example
- G5–6: word ↔ UZ meaning · G7–8: collocation ↔ natural context · G9–10: formal ↔ informal register pair · G11: academic collocation ↔ citation context
- Tile Match pairs may carry inline SVG anchors (a tiny stress-dot diagram, IPA glyph, or word-family mini-tree on the left tile) whenever the visual speeds recognition.

### Sentence Fill
- 4–6 items
- Show a sentence or short dialogue with one piece missing
- Gap must test grammar understanding — not random word removal
- G5–6: "She ___ (go) to school every day." (answer: goes) · G7–8: "By the time we arrived, they ___ (already/leave)." · G9–10: modal + perfect gap · G11: inversion or cleft gap

### Memory Match
- 4×4 grid (8 pairs)
- Flip two cards, find matching pairs
- G5–6: word ↔ picture clue · G7–8: IPA ↔ word · G9–10: idiom ↔ meaning · G11: rhetorical device ↔ example

### Speed Sort
- 6–10 items sorted into 2 categories
- G5–6: present/past sort · G7–8: formal/informal register sort · G9–10: defining/non-defining relative clause sort · G11: active/passive, or academic/general register sort

---

## Example: Tile Match (5 pairs, G7 tier)

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

- 3 games always (English = Hard mode always)
- Every item tagged: `[Bloom: LX | PISA: LX]`
- Bloom L1–L3, PISA L1–L2 for all Game Breaks items
- G11 must include ≥1 IELTS collocation or academic cloze item
- Full answer key for every game
- Current chapter content only — no items from other chapters
- Language: student-facing English. No Uzbek inside game items unless it's a UZ↔EN bridge tile.
- No frozen/removed games (see banned list above)
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
