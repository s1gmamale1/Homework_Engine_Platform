# History — Homework Builder Instruction

You are building a homework session for History — **O'zbekiston Tarixi** or **Jahon Tarixi**. Follow these steps in order.

## Step 1: Identify and extract the lesson

You receive a lesson reference in one of these forms:

- Chapter-section reference (e.g., `"O'zbekiston Tarixi, §NN Chigʻatoy Ulusining Tashkil Topishi"`)
- Page range (e.g., `"O'zbekiston Tarixi, pp. 53–63"`)
- Lesson title + subject

**Find and read the corresponding textbook pages.** Extract:

- **Topic name** (chapter + section)
- **Sub-topics** (from "BUGUN DARSDA" or equivalent listing)
- **Key figures** — rulers, scholars, chroniclers, dynasties
- **Key dates** — years explicitly mentioned
- **Key places** — cities, regions, routes with historical significance
- **Key terms** — new vocabulary introduced (flagged in textbook boxes like "Tarixiy atamalarni eslab qoling")
- **Primary sources** — quotes, chronicler excerpts, documents the chapter cites
- **Maps, images, artifacts** — note what visuals appear and what they depict
- **End-of-section questions** — the textbook's own comprehension prompts

The extraction is the raw material for every subsequent phase. **If a fact isn't in the extraction, it cannot appear in the homework.**

## Step 1.5: Detect lesson length — single or split

> **SCOPE GATE — read first.**
> This step applies **only to `O'zbekiston Tarixi 7-sinf`**. The 2-class-period lesson convention (`N-M-mavzular:`) exists in that one textbook only. For **every other** grade/subject combination — all other grades of O'zbekiston Tarixi, all grades of Jahon Tarixi — treat the input as a single-homework pipeline: set `lesson_length: single`, `part: 1`, `of_parts: 1`, and **skip the rest of this step entirely**. Do not inspect pages, do not split, do not run the pipeline twice.
>
> Proceed below only if the input is confirmed `O'zbekiston Tarixi, 7-sinf`.

---

Inspect the chapter header of the extraction:

| Header pattern | Interpretation | Action |
|---|---|---|
| `^\d+-mavzu:` (e.g., `5-mavzu:`) | **Single-class lesson** | 1 homework. Set `lesson_length: single`, `part: 1`, `of_parts: 1`. Proceed to Step 2. |
| `^\d+-\d+-mavzular:` (e.g., `6-7-mavzular:`) | **Double-class lesson** | 2 homeworks. Set `lesson_length: double`. Split the extraction by page, then run the full pipeline **twice** — once per part. |

Rationale: in O'zbekiston Tarixi 7-sinf, the textbook allocates 2 class periods to most lessons (plural `mavzular` signature). Students attend class on two different days — one homework per class period so they return each night, not once.

### Split math (page-based, front-loaded)

Let `P = total_pages`, `first = first_page`, `last = last_page`.

- **Part 1 pages:** `first` → `first + ceil(P/2) - 1`
- **Part 2 pages:** `first + ceil(P/2)` → `last`

Worked examples:

| Chapter | Pages | Part 1 | Part 2 |
|---|---|---|---|
| Eftaliylar (6-7-mavzular) | 18–23 (6 pp) | 18–20 | 21–23 |
| Turk xoqonligi (8-9-mavzular) | 24–31 (8 pp) | 24–27 | 28–31 |
| 7-page chapter | 50–56 | 50–53 (4 pp) | 54–56 (3 pp) |
| 5-page chapter | 10–14 | 10–12 (3 pp) | 13–14 (2 pp) |

### Seam-snap rule

Raw page-half cuts may fall mid-paragraph or mid-causal-chain. **Snap the split to the nearest textbook callout boundary within ±1 page of the page-half target.** Callout markers in Uzbek textbooks:

- `Ma'lumot uchun`
- `Mulohaza uchun`
- `Ijodiy faoliyat`
- `Bilasizmi?`
- `O'rganganimizdan xulosa chiqaramiz`
- Image captions / figure blocks

If no callout falls within ±1 page, use the raw page-half split.

### Pipeline behavior for `double`

- **Part 1 pipeline** receives Part 1 extraction only. **No Part 2 content may leak** into any Part 1 phase.
- **Part 2 pipeline** receives Part 2 extraction **plus** Part 1 Memory Palace station list **plus** Part 1 BOST goal (for recap + goal-chain).
- Each Part is a complete independent 7-phase homework with its own score (Sprint 10% / Games 50% / Boss 40%).
- Student-facing label: **`1-qism`** / **`2-qism`** on every phase header of the output.

### Carryover rules (apply only when `part == 2`)

- **Memory Palace:** Part 2 Preview opens with a ~60-second **recap walk** of Part 1 stations (list + one-line anchor per station — not a full rebuild), then extends with new stations. Part 2 Consolidation walks the **full combined palace** (Part 1 + Part 2 stations).
- **BOST goal:** Part 2 Reflection references the Part 1 goal in addition to mirroring the Part 2 goal.
- **Boss:** Part 2 Boss **may** (optional, not required) include **1 synthesis question at the Hard tier** spanning Part 1 + Part 2 content. Part 1 Boss must not reference any Part 2 content.

## Step 2: Determine parameters

Fix these for this session:

- **Subject** — `O'zbekiston Tarixi` or `Jahon Tarixi`
- **Milliylik intensity** — `high` (O'zbekiston, 55/45 national/global) or `low` (Jahon, 20/80)
- **Lesson length** — `single` or `double` (from Step 1.5)
- **Part** — `1` or `2` (for `double`); `1` for `single`
- **Of parts** — `1` (single) or `2` (double)
- **Consolidation gating** — count the distinct interlocking concepts in the extraction. If ≥2 → Phase 5 BUILDs. If 1 → Phase 5 SKIPs. (Almost always BUILD for History.)

## Step 3: Build each phase in order

Call each phase prompt in sequence. Each phase receives the extraction + all prior phase outputs.

| # | Phase | Prompt file | Weight | Key rule |
|---|---|---|:-:|---|
| 0-A | Preview | `preview.md` | — | 4 panels (1, 2, 3, 6) + gate quote + Memory Palace |
| 0-B | Flash Cards | `flashcards.md` | — | 8 cards in 3 clusters with Xotira tasviri |
| 1 | Memory Sprint | `memory-sprint.md` | 10% | 7 items, 3 formats mixed, ≥1 Aytilmagan |
| 3 | Game Breaks | `game-breaks.md` | 50% | 3 games (Tile + Memory + Sentence Fill); Von Restorff on Game 2 |
| 5 | Consolidation | `consolidation.md` | — | Memory Palace walkthrough (conditional on ≥2 concepts) |
| 6 | Final Challenge | `final-challenge.md` | 40% | 5 Boss Qs, 100 HP combat, NO multiple choice, ≥1 primary source analysis |
| 7 | Reflection | `reflection.md` | — | Silent analytics + BOST mirror + closing line |

**Skipped phases (never build for History):**

- Phase 2 Reading (language-family only)
- Phase 4 Real-Life (narrative absorbs transfer)

## Step 4: Verify

Before shipping, check every item:

- [ ] Scope gate honored: split logic ran **only for `O'zbekiston Tarixi 7-sinf`**; all other grades/subjects went straight to single-homework path
- [ ] Lesson-length detection correct (within scope): `N-mavzu:` → `single` (1 homework); `N-M-mavzular:` → `double` (2 homeworks, page-halved with seam-snap)
- [ ] If `double`, pipeline ran **twice** (Part 1 + Part 2) with independent extractions
- [ ] Part 1 output contains **zero Part 2 content** (no forward leak of figures, events, quotes, or dates from the second half)
- [ ] Part 2 Preview opens with **60-second recap walk** of Part 1 Memory Palace stations, then extends numbering
- [ ] Part 2 Consolidation walks the **full combined palace** (all Part 1 + Part 2 stations, in order)
- [ ] Part 2 Reflection BOST mirror references **both** Part 1 and Part 2 goals
- [ ] Every phase header in the output carries `1-qism` or `2-qism` label when `double`
- [ ] Phases in correct order: 0-A → 0-B → 1 → 3 → 5 → 6 → 7
- [ ] Phase 2 and Phase 4 absent
- [ ] Language: Uzbek, formal `Siz` throughout. **Zero `sen`.**
- [ ] Gate quote Milliylik ratio matches subject (55/45 high, 20/80 low)
- [ ] All facts from the textbook extraction — no invented names/dates/quotes
- [ ] Preview: all 4 panels (1, 2, 3, 6) are single-layer — no Qatlam 1/2 split anywhere
- [ ] Panel 1: full-depth narrative, every textbook fact represented, paragraph count driven by lesson density
- [ ] Panel 2: clarifies 3–5 confusion points + fills gaps; no taxonomy/types list; does not restate Panel 1; mind map included only if visual genuinely clarifies complex structure
- [ ] Memory Palace has 5–10 thematic stations used consistently across Preview, Flash Cards palace tags, and Consolidation walkthrough
- [ ] **Preview Mermaid code blocks are properly closed** with ` ``` ` before next section
- [ ] Flash Cards: 3 clusters, Xotira tasviri on every card, no standalone date cards
- [ ] Sprint: 7 items, ≥2 formats mixed, ≥1 "Aytilmagan" YNNG
- [ ] Game Breaks: 3 games, 40/40/20 difficulty, Von Restorff anchor on Game 2 **tagged as Hard**, dual-catalog waiver noted inline
- [ ] Consolidation: BUILDs (≥2 concepts) or SKIPs correctly; when BUILD, **walks ALL Preview palace stations (no skipping)**, includes **self-check prompt after every station**, and ends with **"Hit all N stations?" verification prompt**
- [ ] Final Challenge: 5 questions, 100 HP, 40/40/20 damage, **damage values exactly −10 / −20 / −30 (no other values)**, **no multiple choice**, ≥1 primary source question, ≥1 causal-framework question, Hint 3s use **diagnostic questions, never answer templates**
- [ ] **Phase 6 output does NOT leak Phase 7 content** (no Reflection, no closing messages, no XP awards inside Phase 6)
- [ ] Reflection: BOST mirror references the actual Panel 6 goal; closing line matches score (Milliylik on ≥60%, TEFCAS on <60%)
- [ ] Every assessment item carries `[Bloom | PISA | Skill]` (Boss also `Damage`)
- [ ] **PISA tags include L level** — `Reading L1`, `Reading L2`, `Creative Thinking L2`, etc. Never just `Reading` or `Creative Thinking` alone
- [ ] Standards code format: `UZ-TARIX-G-TOPIC-PHASE-##`
- [ ] No frozen games referenced (Why Chain, Territory Conquest, Reaction Chain, etc.)
- [ ] No bazaar/village/shopkeeper/farmer clichés

## Output

Ship a markdown document with phases in order, plus a metadata JSON sibling:

```json
{
  "lesson_id": "slug_from_topic",
  "subject": "O'zbekiston Tarixi | Jahon Tarixi",
  "family": "ijtimoiy-fanlar",
  "textbook_ref": { "pages": "NN–MM", "chapter": "...", "section": "..." },
  "milliylik_intensity": "high | low",
  "lesson_length": "single | double",
  "part": 1,
  "of_parts": 1,
  "parent_mavzu_range": "6-7",
  "consolidation_built": true,
  "weight_map": { "sprint": 10, "games": 50, "boss": 40 },
  "verification_passed": true
}
```

For `double` lessons, emit **two** JSON files (one per part). Set `part_info` fields per part:

- Part 1: `"part": 1`, `"of_parts": 2`, `textbook_ref.pages` covers Part 1 page range only.
- Part 2: `"part": 2`, `"of_parts": 2`, `textbook_ref.pages` covers Part 2 page range only.

`parent_mavzu_range` is set on both (e.g., `"6-7"`) when `double`; `null` when `single`.

Ship only if every verification checklist item passes.
