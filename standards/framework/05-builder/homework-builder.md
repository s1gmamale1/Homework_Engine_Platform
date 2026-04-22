---
name: Homework Builder — Stateless Production Pipeline
status: v0.1 draft — validated against §22 only
layer: 5 (builder)
source: UNIFIED §10 (lines 2789-2908) + Architecture doc (lines 284-360)
---

# Homework Builder — Stateless Production Pipeline

Input: textbook section (PDF + text + metadata).
Output: homework `.md` + metadata JSON.

The builder is **stateless**: each session is composed independently from the component inventory. No session-to-session memory. Reproducibility is enforced by verification (Step 5).

---

## Component inventory (what gets loaded)

| Layer | Folder | Files |
|-------|--------|-------|
| 00 Core primitives | `00-core/` | ai-constraints.md, anti-cheat.md, capture-rule.md, content-architecture.md, context-policy.md, core-principles.md, difficulty-adaptation.md, edge-cases-recovery.md, gamification-economy.md, hp-damage-baseline.md, integration-points.md, pisa-framework.md, pronoun-policy.md, research-citations.md, routing-algorithm.md, skill-taxonomy.md, teacher-controls.md, variant-generator.md |
| 01 Phase components | `01-phases/` | phase-0a-preview.md, phase-0b-flashcards.md, phase-01-memory-sprint.md, phase-02-reading.md, phase-03-game-breaks.md, phase-04-real-life.md, phase-05-consolidation.md, phase-06-final-challenge.md, phase-07-reflection.md |
| 02 Family adapters | `02-families/` | family-aniq-fanlar.md, family-tabiy-fanlar.md, family-til-fanlar.md, family-ijtimoiy-fanlar.md |
| 03 Mode specs | `03-modes/` | easy-mode.md, hard-mode.md |
| 04 Difficulty layer | `04-difficulty/` | phase-weights.md |

---

## Step 1 — CLASSIFY

Determine three tags before any loading occurs.

### 1a. Subject → family tag

Assignment is deterministic from the textbook folder path or subject metadata field:

| Folder path pattern | Family tag |
|---------------------|------------|
| `**/Algebra/**`, `**/Geometriya/**`, `**/Matematika/**` | `aniq-fanlar` |
| `**/Fizika/**`, `**/Kimyo/**`, `**/Biologiya/**` | `tabiy-fanlar` |
| `**/Ona tili/**`, `**/Rus tili/**`, `**/Ingliz tili/**` | `til-fanlar` |
| `**/Tarix/**`, `**/Ozbekiston tarixi/**`, `**/Jahon tarixi/**` | `ijtimoiy-fanlar` |

If no path match: fall back to subject field in the textbook metadata JSON. If still ambiguous: HALT and request human classification. Do not guess.

### 1b. Section content → mode tag

| Mode | Detection rule | Source |
|------|---------------|--------|
| `easy` | Section introduces a new term/definition not present in any prior section AND involves no systematic procedure | `03-modes/easy-mode.md` §Detection rule |
| `hard` | Section teaches a systematic procedure (grep for: "formula", "algorithm", "method", "usul", "qoida") OR references ≥2 prior sections | `03-modes/hard-mode.md` §Detection rule |

Teacher can override mode tag manually at pipeline entry. Teacher tag always wins.

Default when ambiguous:
- G5-6: `easy` unless teacher overrides.
- G9-11 STEM: `hard` unless teacher overrides.
- G7-8: run keyword grep; if ≥1 hit → `hard`, else → `easy`.

### 1c. Grade → difficulty band

| Grade range | Band |
|-------------|------|
| G1-4 | `elementary` |
| G5-6 | `lower-secondary` |
| G7-8 | `mid-secondary` |
| G9-11 | `upper-secondary` |

Difficulty band feeds Step 2 (Bloom/PISA targets) and Step 4 (calibration).

---

## Step 2 — LOAD

Load files in this order. Later layers override earlier layers on any conflict.

```
1. Core primitives (always, all files from 00-core/)
2. Phase components (filtered by mode spec — see active components table)
3. Family adapter (from 02-families/ matching family tag)
4. Mode spec (from 03-modes/ matching mode tag)
5. Difficulty calibration (from 04-difficulty/phase-weights.md)
```

### Active component selection by mode

**Easy mode** (`03-modes/easy-mode.md`): loads 5 components.

| # | Component file | Fires |
|---|---------------|-------|
| 1 | phase-0a-preview.md | Always |
| 2 | phase-0b-flashcards.md | Always |
| 3 | phase-01-memory-sprint.md | Always |
| 4 | phase-03-game-breaks.md | Always |
| 5 | phase-07-reflection.md | Always |

Skipped in easy mode: phase-02-reading.md, phase-04-real-life.md, phase-05-consolidation.md, phase-06-final-challenge.md.

**Hard mode** (`03-modes/hard-mode.md`): loads 6-8 components, family-filtered.

| # | Component file | Family filter |
|---|---------------|--------------|
| 1 | phase-0a-preview.md | ALL |
| 2 | phase-0b-flashcards.md | ALL |
| 3 | phase-01-memory-sprint.md | ALL |
| 4 | phase-02-reading.md | `til-fanlar` only |
| 5 | phase-03-game-breaks.md | ALL |
| 6 | phase-04-real-life.md | `aniq-fanlar` + `tabiy-fanlar` only |
| 7 | phase-05-consolidation.md | `aniq-fanlar` + `tabiy-fanlar` only, if ≥2 concepts |
| 8 | phase-06-final-challenge.md | ALL |
| 9 | phase-07-reflection.md | ALL |

---

## Step 3 — EXTRACT

Parse the textbook section into structured content. This step produces the raw material that Step 4 draws from.

```
INPUT:  textbook section PDF (or pre-extracted text)
OUTPUT: chapter_extract.json

chapter_extract.json fields:
  - section_id         (e.g. "MAT.7.3.2")
  - title              (section heading from textbook)
  - concepts[]         (named objects, definitions, theorems)
  - terms[]            (key vocabulary with textbook definition)
  - formulas[]         (symbolic expressions + description)
  - examples[]         (worked examples from textbook)
  - exercises[]        (practice problems from textbook)
  - atomic_skills[]    (5-7 minimal learnable sub-skills identified from above)
  - keywords_80_20[]   (3-8 keywords carrying ~80% of section meaning — Buzan gate)
```

Atomic skill identification rule: one atomic skill = one thing a student can do correctly or incorrectly in isolation. Break formulas, algorithms, and definitions until each piece is independently testable. Target count: 5-7. If fewer than 5 are identifiable, the section is likely too thin for a full homework — flag for teacher review.

Buzan dual-coding annotation: for each concept and formula, identify available encoding channels (VRB, VIS, SPA, AUD, KIN). Feed into Preview panel and Flash Card generation in Step 4.

---

## Step 4 — COMPOSE

For each active phase component, in session order (0-A → 0-B → 1 → ... → 7):

```
FOR each active phase component:
  1. Read component file (already loaded in Step 2)
  2. Read component's `inputs` and `verification rules` sections
  3. Pull required items from chapter_extract.json
  4. Apply family adapter overrides (from 02-families/ doc)
  5. Apply difficulty calibration (Bloom/PISA targets from 04-difficulty/)
  6. Generate content:
       - Template items (Tier 1): fill structured templates from component file
       - LLM items (Tier 2):      prompt LLM with component spec + extract + adapter rules
       - LLM creative (Tier 3):   prompt LLM for narrative/scenario with full context
  7. Tag every item:   [Bloom: LX | PISA: LX | Skill: <atomic_skill_id>]
     Boss questions also carry: [Damage: -XX HP]
  8. Validate item against component's verification rules
     → If item fails: regenerate (max 3 attempts), then flag for human review
  9. Append validated items to homework draft
```

### Phase-specific composition notes

**Phase 0-A (Preview):** Must include genetic method + two-layer explanation. Easy mode: 3-5 panels. Hard mode: 5-8 panels. Panels 1-4 must include teaching methodology flag for verification gate.

**Phase 0-B (Flash Cards):** Easy: 5-8 cards. Hard: 8-12 cards. Every card tagged with `keywords_80_20` from extract.

**Phase 1 (Memory Sprint):** 5 items (easy) or 7 items (hard). ONLY formats: Multiple Choice, True/False, Yes/No/Not Given. Must mix ≥2 formats. No fill-in-blank, gap-fill, drag-and-drop, typing, or open-ended items — these are banned in Phase 1.

**Phase 2 (Reading):** Til Fanlar (hard mode) only. ONE continuous flowing story — arc beats are invisible ingredients baked into narrative, not labeled sections.

**Phase 3 (Game Breaks):** Easy: 2 games (lighter difficulty). Hard: 3 games. Hard mode game mix rule: ≥1 from Interactive Catalog (6 games) + ≥2 from Default Pool (16 mechanics). Adaptive Quiz mandatory for Aniq Fanlar (with capture markers). Never reference removed games: Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker.

**Phase 4 (Real-Life):** ONE deep immersive scenario. Modern professional context only. No bazaar/village/farmer/shopkeeper clichés. Capture markers on all solve steps.

**Phase 5 (Consolidation):** Fires only when ≥2 distinct concepts/methods were introduced in the section.

**Phase 6 (Final Challenge / Boss):** HP values: G1-4 = 50, G5-8 = 100, G9-11 = 150. Matematika G5-6 override = 80 HP. Damage: Easy = -10, Medium = -20, Hard = -30. Distribution: 40% Easy / 40% Medium / 20% Hard. No Multiple Choice for G6+ in Final Boss. G5 allows up to 30% MC.

**Phase 7 (Reflection):** Analytics only, not graded. Select 1 prompt from 3-prompt pool in extract.

---

## Step 5 — VERIFY

Run the full verification checklist in `verification-checklist.md`. All gates must pass.

```
Gate sequence:
  1. Schema valid          → structural/automated
  2. Tagging coverage      → regex scan
  3. Pronoun compliance    → keyword scan
  4. Context compliance    → keyword scan
  5. Format rules          → automated (Phase 1 formats, Phase 3 game count)
  6. Capture markers       → automated (Math/Science families)
  7. Textbook fidelity     → embed-diff + flagged for human review
  8. Cognitive variety     → Bloom distribution check
  9. Reproducibility       → 3× regeneration structural diff
  10. Language QA          → external validator
  11. Teaching methodology → content review (Preview panels 1-4)
```

**On any gate failure:**
- Log the failing gate + which phase/item failed.
- Rebuild only the failing component (not the entire session).
- Retry up to 3 times with error-specific correction prompts.
- After 3 retries without passing: HALT, mark homework as `DRAFT — manual review required`, output partial result with failure annotation.
- Do not ship a homework that has failed any gate.

---

## Step 6 — SHIP

Write two outputs.

### 6a. Homework `.md` file

Format: per `output-schema.md` (this directory).
Destination: `Homeworks/` folder (or n8n output node, see `infra/n8n/`).
Filename convention: `HW-{SUBJECT}{GRADE}-{CHAPTER}-{SECTION}-{LANG}.md`
Example: `HW-MAT7-CH3-S2-UZ.md`

### 6b. Metadata JSON

Written alongside the `.md` file. Contains:
- Session config (lesson_id, subject, grade, mode, family, timestamp, textbook_ref)
- Capture rubrics (per phase, for Math/Science)
- Variant pool (alternate items for remediation path)
- Verification log (gate results + any retry history)

### 6c. Status log

Append entry to `Homeworks/STATUS.md`:
```
| lesson_id | subject | grade | mode | status | timestamp | gates_passed |
```

For n8n production implementation, see `infra/n8n/` pipeline nodes. The builder steps map 1:1 to n8n workflow nodes: Classify → Load → Extract → Compose → Verify → Ship.
