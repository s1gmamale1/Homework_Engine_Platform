# NETS Framework — Component Architecture

**Version:** 0.1 (proposal, derived from §22 reference implementation)
**Date:** 2026-04-21
**Status:** Draft — pending stress tests against §24 Algorithm lesson + first non-Math lesson
**Supersedes:** monolithic structure of `NETS-Homework-Engine-UNIFIED-Buzan.md`

---

## TL;DR

Move from a monolithic UNIFIED spec + delta subject frameworks to a **layered component architecture**. Each phase is a standalone component spec with explicit inputs, outputs, and adaptable parameters. Subject families and lesson archetypes are adapter layers. A builder pipeline composes homework from components. Localized changes no longer cascade through the codebase.

---

## Why move off the monolith

Current state:
- `NETS-Homework-Engine-UNIFIED-Buzan.md` ~ 600+ lines, covers all phases, all rules, all examples
- Subject-specific frameworks are "delta" layers that reference UNIFIED
- Tier Overlay, Grading System, Quick Reference sit alongside
- Matrix v0.3 (routing layer) sits on top

Problems surfaced by §22 build:
1. **Change amplification.** Removing "Story Mode" as a universal phase required edits in UNIFIED, Matrix, and potentially every subject framework.
2. **Rule scatter.** The capture rule, pronoun policy, and passing threshold live in multiple sections of UNIFIED — impossible to see all of them at once.
3. **Subject coupling.** Algorithm archetype baked into UNIFIED even though it doesn't apply to Language/History.
4. **Verification drift.** Compliance checks are implicit across sections, not enumerated in one place.
5. **No builder contract.** A new content agent has to read hundreds of lines of prose before producing a single homework.

The monolith was right for v1 (establish the WHAT). For v2 (scale to all subjects and grades), we need layers.

---

## Lessons from §22 (what to bake into components)

Pattern found in §22 → Applies to which component:

| Learning from §22 | Component it belongs in |
|-------------------|-------------------------|
| Story Mode cross-passes with Real-Life → merged | Phase component (Real-Life absorbs narrative for Sciences) |
| Capture applies to any calc step, not just Adaptive Quiz | Core primitive (capture-rule) |
| Aniq Fanlar Phase 3 requires Adaptive Quiz | Family adapter (Aniq Fanlar) |
| Concept Intro skips Consolidation | Archetype × Phase weight matrix |
| Final Challenge format adapts by archetype (light/standard/full) | Phase-06 component + archetype adapter |
| Metacognition is a skill axis (from L5 eval questions) | Core primitive (skill taxonomy) |
| Modern professional context only, no bazaar | Core primitive + family context examples |
| Single deep scenario > multiple shallow | Phase-04 component (Real-Life) |
| Phase 3 = real practice, Phase 1 = warm-up | Phase-01 + Phase-03 component |
| 60% pass threshold + weakest-skill routing | Core primitive (routing-algorithm) |
| 6 skill axes (memory, translation, problem-solving, critical-thinking, application, metacognition) | Core primitive (skill taxonomy) |
| Phase weights 10/30/30/30 (Concept Intro) | Archetype × weight layer |
| Game Break requires 2 default + 1 interactive | Phase-03 component |
| Notebook Capture mock UX (camera icon + confirm) | Phase-03 + Phase-04 shared UX spec |
| Variant generator rule (keep Bloom, scale coeffs 0.3-0.6) | Core primitive (remediation) |

---

## Architecture — 5 layers

```
┌─────────────────────────────────────────────────────────┐
│ Layer 5 — BUILDER                                        │
│ Pipeline: textbook → classify → compose → verify → ship │
└──┬──────────────────────────────────────────────────────┘
   │ reads
┌──▼──────────────────────────────────────────────────────┐
│ Layer 4 — DIFFICULTY                                     │
│ Per subject, per grade-band difficulty tables            │
│ HP pools, damage tiers, phase weights, Bloom/PISA target│
└──┬──────────────────────────────────────────────────────┘
   │ parameterizes
┌──▼──────────────────────────────────────────────────────┐
│ Layer 3 — ARCHETYPES (per family)                        │
│ Aniq: Concept / Algorithm / Application / Review         │
│ Til:  Lexical / Grammar / Receptive / Productive / Rev.  │
│ Ijtim: Narrative / Causal / Comparative / Review         │
└──┬──────────────────────────────────────────────────────┘
   │ selects & weights
┌──▼──────────────────────────────────────────────────────┐
│ Layer 2 — FAMILIES (subject adapters)                    │
│ Aniq Fanlar · Tabiy Fanlar · Til Fanlar · Ijtimoiy Fanlar│
│ Family-specific rules, phase routing, context examples   │
└──┬──────────────────────────────────────────────────────┘
   │ adapts
┌──▼──────────────────────────────────────────────────────┐
│ Layer 1 — PHASES (components)                            │
│ 0-A · 0-B · 1 · 2 · 3 · 4 · 5 · 6 · 7                    │
│ Each is a self-contained spec with interface contract    │
└──┬──────────────────────────────────────────────────────┘
   │ inherits
┌──▼──────────────────────────────────────────────────────┐
│ Layer 0 — CORE PRIMITIVES                                │
│ Pronoun policy · Bloom/PISA tagging · Skill taxonomy     │
│ Capture rule · Routing algorithm · Passing threshold     │
│ HP/damage baseline · Context policy · Variant generator  │
└─────────────────────────────────────────────────────────┘
```

Dependencies flow upward only. A phase component doesn't know about subjects. A family adapter doesn't know about the builder. Changes at each layer are local.

---

## File structure (proposed)

```
standards/framework/
  00-core/                              # shared primitives
    pronoun-policy.md
    bloom-pisa-tagging.md
    skill-taxonomy.md                   # 6 axes, with definitions + examples
    capture-rule.md                     # "any calc step = capture"
    routing-algorithm.md                # 60% threshold, weakest-skill re-route
    passing-threshold.md
    hp-damage-baseline.md               # grade-band HP, 40/40/20 distribution
    context-policy.md                   # modern professional only
    variant-generator.md                # remediation variant rules

  01-phases/                            # phase components (each standalone)
    phase-0a-preview.md
    phase-0b-flashcards.md
    phase-01-memory-sprint.md
    phase-02-reading.md                 # language family only
    phase-03-game-breaks.md
    phase-04-real-life.md
    phase-05-consolidation.md
    phase-06-final-challenge.md
    phase-07-reflection.md              # silent analytics + routing

  02-families/                          # subject-family adapters
    family-aniq-fanlar.md               # Math subjects
    family-tabiy-fanlar.md              # Natural Sciences
    family-til-fanlar.md                # Languages
    family-ijtimoiy-fanlar.md           # Social Sciences

  03-archetypes/                        # lesson archetypes per family
    aniq-fanlar/
      concept-intro.md
      algorithm.md
      application.md
      review.md
    til-fanlar/
      lexical-intro.md
      grammar-intro.md
      receptive.md
      productive.md
      review.md
    ijtimoiy-fanlar/
      narrative-intro.md
      causal-analysis.md
      comparative.md
      review.md

  04-difficulty/                        # difficulty mapping
    per-family-difficulty.md            # Math 80 HP G5-6 etc
    phase-weights.md                    # 10/30/30/30 per archetype
    item-tier-distribution.md           # 40/40/20 easy/med/hard

  05-builder/                           # pipeline spec
    homework-builder.md                 # steps: classify → compose → verify
    verification-checklist.md           # all compliance gates in one place
    output-schema.md                    # the .md homework format

  NETS-Framework-Architecture.md        # THIS FILE (top-level index)
  NETS-Homework-Engine-UNIFIED-Buzan.md # shrinks to brief INDEX/pointer, frozen as v2.0-final
  NETS-Phase-Family-Matrix.md           # deprecated; content migrated to 02-families + 03-archetypes
```

---

## Component contract (what each Phase component must specify)

Every phase component file is structured identically so a builder agent can parse any of them with the same logic:

```markdown
# Phase XX — Name

## Purpose (WHAT)
One-sentence mission of this phase.

## Structure (HOW)
The shape: how many items, what formats, what order.

## Cognitive load
Bloom range · PISA range · time budget

## Inputs (required from prior phases or content source)
- Textbook content
- Prior phase outputs (if any)
- Subject family tag
- Archetype tag
- Grade band

## Outputs (consumed by later phases)
- Question-level data (correct/incorrect, time, skill tags)
- Phase aggregate (score %, skill breakdown)

## Adaptable parameters
| Parameter | Default | Override per family | Override per archetype |
|-----------|---------|---------------------|------------------------|
| Item count | 6 | Language: 8 | Review: 10 |
| Format restrictions | MC/T-F/YNNG | Language: add Gap-fill | - |

## Subject-specific examples
- Aniq Fanlar: ...
- Til Fanlar: ...
- etc.

## Verification rules
- Rule 1 (with test)
- Rule 2 (with test)

## Integration points
- Entry hook (called by previous phase)
- Exit hook (calls next phase)

## UX/animation spec (for HTML demos)
- Card chrome: shared
- Transitions: shared
- Phase-specific: ...
```

---

## Family adapter contract

Each family file is structured:

```markdown
# Family — [Name]

## Archetypes available
List of archetypes valid for this family.

## Phase route per archetype
Matrix of which phases fire at which weight.

## Family-specific rules
Overrides or additions to core primitives.
Example: "Aniq Fanlar Phase 3 requires Adaptive Quiz."

## Context examples
Modern professional contexts appropriate for this family.
Example: Aniq Fanlar → IT Park, UAV sector, solar engineering, Metro design.
Language → Literary analysis, news media, business correspondence.

## Subjects in this family
List of subjects that use this adapter (e.g., Matematika, Algebra, Geometriya).

## Overrides by subject (delta layer)
Subject-specific nuances (e.g., Matematika G5-6 uses 80 HP instead of 100).
```

---

## Difficulty layer contract

Difficulty varies by subject. Math G8 is different from Physics G11 even within sciences.

```markdown
# Per-Family Difficulty

## Grade bands
G1-4 · G5-8 · G9-11

## Bloom target distribution (per archetype × grade band)
Concept Intro G5-8: L1=20%, L2=40%, L3=30%, L4=10%
Algorithm G9-11: L1=10%, L2=30%, L3=40%, L4=20%
...

## PISA target
Varies by topic.

## HP pool
G1-4: 50 · G5-8: 100 · G9-11: 150
(subject-specific overrides: Matematika G5-6 = 80)

## Damage tier distribution
40% easy · 40% medium · 20% hard
```

---

## Builder pipeline (Layer 5)

Stateless composer. Input: textbook section (PDF + text). Output: homework .md + metadata.

```
1. CLASSIFY
   ├─ subject → family tag
   ├─ section content → archetype tag (is new object introduced?)
   └─ grade → difficulty band

2. LOAD
   ├─ core primitives (always)
   ├─ phase components (all that fire per archetype × family)
   ├─ family adapter (applies overrides)
   ├─ archetype spec (applies phase weights)
   └─ difficulty layer (applies Bloom/PISA targets)

3. EXTRACT
   ├─ pdf → structured chapter JSON (objects, terms, examples)
   └─ identify 5-7 atomic skills from the section

4. COMPOSE (per phase, in order)
   ├─ for each phase component that fires:
   │    ├─ read its inputs
   │    ├─ apply subject/archetype/difficulty adaptations
   │    ├─ generate content (via LLM or template)
   │    ├─ tag every item with [Bloom | PISA | Skill]
   │    └─ validate against component's verification rules
   └─ assemble into homework .md

5. VERIFY
   ├─ run core primitive compliance (pronoun, capture, context)
   ├─ run framework compliance checklist (tagging, format, fidelity)
   ├─ run language compliance (Uzbek grammar, terminology)
   └─ reproducibility check (generate 3×, structural similarity ≥ 95%)

6. SHIP
   ├─ write homework .md
   ├─ write metadata (schema, capture rubrics, variant pool)
   └─ log to nets_lessons + nets_phase_outputs
```

---

## Verification metrics (Layer 5 gate)

Every homework passes through a single verification manifest:

| Gate | What it checks | Source |
|------|----------------|--------|
| Schema valid | JSON conforms to `output-schema.md` | builder layer |
| Tagging coverage | Every question has [Bloom \| PISA \| Skill] | phase verification rules |
| Pronoun compliance | Zero "sen" / "ты" hits | core `pronoun-policy.md` |
| Context compliance | No bazaar/village/farmer clichés | core `context-policy.md` |
| Format rules | Phase 1 = MC/T-F/YNNG only; Phase 3 = 3 games, correct mix | phase components |
| Capture rule | Every calc step has capture marker | core `capture-rule.md` |
| Textbook fidelity | No content beyond source chapter | core |
| Cognitive variety | Bloom distribution within target range | difficulty layer |
| Reproducibility | 3× regeneration ≥ 95% structural match | builder |
| Language QA | Grammar + terminology + register | external validator |

If any gate fails → homework rejected, builder retries with corrections.

---

## Subject classification (automatic at pipeline entry)

Subject-family assignment is deterministic from the textbook folder path or metadata:

| Folder path pattern | Family |
|---------------------|--------|
| `**/Algebra/**`, `**/Geometriya/**`, `**/Matematika/**` | Aniq Fanlar |
| `**/Fizika/**`, `**/Kimyo/**`, `**/Biologiya/**` | Tabiy Fanlar |
| `**/Ona tili/**`, `**/Rus tili/**`, `**/Ingliz tili/**` | Til Fanlar |
| `**/Tarix/**`, `**/Ozbekiston tarixi/**`, `**/Jahon tarixi/**` | Ijtimoiy Fanlar |

Archetype classification uses section content (grep for first-appearance terms, method definitions, comparison keywords — see `03-archetypes/` detection rules).

---

## Homework-level difficulty (emergent, per subject)

Different subjects produce different "hardness profiles" even at the same grade. A Math algorithm homework feels different from a Language productive homework. The difficulty layer makes this explicit:

| Family | Dimensions that dominate difficulty |
|--------|--------------------------------------|
| Aniq Fanlar | Number complexity, multi-step reasoning, algorithm choice |
| Tabiy Fanlar | Process complexity, formula application, experimental inference |
| Til Fanlar | Vocabulary obscurity, grammar depth, productive output length |
| Ijtimoiy Fanlar | Causal chain depth, comparative scope, primary source density |

Each family's difficulty doc encodes these as ordered dimensions so the builder can dial them.

---

## Migration plan

**Phase A — Freeze & draft** (1-2 days)
- Mark current `NETS-Homework-Engine-UNIFIED-Buzan.md` as v2.0-final (historical)
- Extract §22 learnings into `00-core/` primitive drafts
- Create `01-phases/` component drafts (most fields derivable from §22 experience)

**Phase B — Family skeleton** (1 day)
- Fully populate `02-families/family-aniq-fanlar.md` (we have the data)
- Skeleton drafts for til/ijtimoiy/tabiy (TBD on first lesson from each)

**Phase C — Archetype + difficulty** (1 day)
- `03-archetypes/aniq-fanlar/concept-intro.md` fully specced (from §22)
- Others as skeletons

**Phase D — Builder & verification** (1-2 days)
- `05-builder/homework-builder.md` — pipeline steps
- `05-builder/verification-checklist.md` — single-page compliance gate

**Phase E — Deprecate** (final)
- `NETS-Homework-Engine-UNIFIED-Buzan.md` shrinks to an index pointing at components
- `NETS-Phase-Family-Matrix.md` content migrates into 02-families + 03-archetypes

**Total:** ~1 week of doc work. Agents can be deployed in parallel to draft the skeletons.

---

## Stress tests (validate before locking)

Before declaring this architecture v1.0, we need:

1. **§24 Algorithm homework (Aniq Fanlar).** Stress-tests the Algorithm archetype column, the "capture on any calc" rule, and Consolidation activation for multi-method lessons.
2. **First Til Fanlar lesson.** Stress-tests the Reading phase (replaces Story Mode), the Lexical/Grammar archetypes, and productive output UX.
3. **First Ijtimoiy Fanlar lesson.** Stress-tests the Narrative/Causal archetypes and the Real-Life-skip rule for History.

If any of these produces a pattern that doesn't fit the proposed structure, the component spec gets revised BEFORE we migrate the rest.

---

## Open questions

1. **Tabiy Fanlar rule** — does Adaptive Quiz mandatory + capture on calc apply there too? (Flagged from §22, not yet answered.)
2. **Phase weights 10/30/30/30** — validated against §22 gut-feel. Needs pilot data to calibrate.
3. **Metacognition axis** — new 6th skill. Confirm or fold into critical-thinking.
4. **Family-specific archetype expansions** — Language's Lexical/Grammar/Receptive/Productive split is my proposal. History's Narrative/Causal/Comparative likewise. Validate against real lessons.
5. **Difficulty layer per-subject granularity** — one subject per file, or shared family doc with subject overrides?
6. **Component versioning** — do individual phase components get their own semver, or one shared framework version?

---

## Changelog

| Version | Date | Notes |
|---------|------|-------|
| 0.1 | 2026-04-21 | First draft. Derived from §22 reference implementation. Pending stress tests. |

---

*End of architecture document. This file is the top-level index for future revisions.*
