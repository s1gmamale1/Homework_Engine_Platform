# NETS Phase × Family Matrix

**Version:** 0.4 (draft)
**Date:** 2026-04-21
**Branch:** Cheeks
**Relationship to UNIFIED-Buzan:** Routing layer on top of UNIFIED. UNIFIED defines *what* each phase is. This matrix defines *when* each phase runs and at *what depth*, based on subject family and lesson archetype.

**⚠️ DEPRECATED (2026-04-21):** This matrix has been fully decomposed into the component architecture:
- Phase routing → `03-modes/easy-mode.md` + `03-modes/hard-mode.md`
- Family-specific rules → `02-families/family-*.md`
- Phase weights → `04-difficulty/phase-weights.md`
- Data collection → `01-phases/phase-07-reflection.md`
- Skill taxonomy → `00-core/skill-taxonomy.md`
- Routing algorithm → `00-core/routing-algorithm.md`

This file is preserved for historical reference. Use the component files as authoritative sources.

Rules that were locked in the final session before decomposition (carried forward to v0.4):
- **Capture rule** — applies to any calculation step in any phase (not just Adaptive Quiz)
- **Aniq Fanlar Phase 3 rule** — Adaptive Quiz is mandatory and the only capture-bearing game
- **Phase weights proposal** — 10/30/30/30 (Memory Sprint / Game Breaks / Real-Life / Final Challenge)
- **Skill taxonomy** — 6 axes (memory · translation · problem-solving · critical-thinking · application · metacognition)
- **Territory Conquest** — restored to active Interactive Catalog (7 games)
- **Single-deep-scenario preference** — for Phase 4 Real-Life over multiple shallow scenarios
- **§22 reference implementation** — all 7 active phases fully designed, HTML demo in progress

---

## TL;DR

NETS homework runs a fixed 9-slot phase skeleton. Any given homework uses only **6-8 of the slots** based on two tags: **subject family** and **lesson archetype**. This gives reproducible structure plus adaptive depth — no padding on light lessons, no underinvestment on heavy ones.

---

## Design principle — Path C

Three paths were considered when deciding whether to keep all 7 phases universally:

| Path | Approach | Verdict |
|------|---------|---------|
| A | All 7 phases at full weight, always | Rejected — bloats light lessons, kills simplicity |
| B | Pick-and-choose phases per homework | Rejected — destroys reproducibility, agents drift toward skipping effortful phases |
| C | Fixed skeleton, variable weight per tag | **Adopted** — reproducible shape, adaptive depth |

Under Path C, the student always sees the same ritual. The content agent always has deterministic rules for which phases fire and at what weight. Subject family + lesson archetype drive the routing, not content-agent judgment.

---

## Phase status legend

| Symbol | Meaning |
|:---:|---|
| 🟢 MUST | Every homework, every subject family |
| 🟡 SUBJECT | Required by some families, skipped in others |
| 🟠 LESSON | Required by some lesson archetypes, skipped in others |
| 🔴 DEFER | Parked, not in v1 |

---

## Universal phase matrix

| # | Phase | Status | Description |
|---|-------|:---:|---|
| 0-A | **Preview** (panels + optional mind map / state diagram) | 🟢 MUST | 3-8 panels adaptive. Mind map renders inside a panel when concept is process/relational. Teaching happens here — before any testing. |
| 0-B | **Flash Cards** | 🟢 MUST | Atomic recall only — vocab, formulas, single facts. Minimum 2-3 cards. |
| 1 | **Memory Sprint** | 🟢 MUST | Light warm-up. MC / True-False / Yes-No-Not-Given only. Tap-only. |
| 2 | **Reading** | 🟡 Languages only | IELTS-style narrative + comprehension. Replaces the old "Story Mode" for language family. |
| 3 | **Game Breaks** | 🟢 MUST | 3 games: 2 default + 1 interactive (interactive slot reserved, may defer to Premium tier). |
| 4 | **Real-Life Challenge** | 🟡 SUBJECT | Math: applied word problems. Sciences: narrative-process-style (photosynthesis pattern, per Good_Demos biology reference) + questions. History: skipped (narrative already in Preview). Languages: skipped (Reading covers it). |
| 5 | **Consolidation** | 🟠 LESSON | Fires when lesson introduces ≥2 interlocking concepts needing integration. |
| 6 | **Final Challenge** | 🟢 MUST | Adaptive difficulty — see adaptive spec below. Replaces fixed-HP "Final Boss" as the default. |
| 7 | **Reflection** | 🟢 MUST | Silent data collection + Duolingo-style routing. Not student self-reflection prose. |

A typical homework runs 6-8 of the 9 slots. Slot 2 fires only for Languages. Slot 4 fires for Math/Sciences. Slot 5 fires for multi-concept lessons.

---

## Subject family route map

| Family | Active phases | Inactive/skipped |
|--------|---------------|-------------------|
| **Aniq Fanlar** (Math) | 0-A · 0-B · 1 · 3 · 4 · (5) · 6 · 7 | 2 (Reading) |
| **Tabiy Fanlar** (Natural Sciences) | 0-A · 0-B · 1 · 3 · 4 (narrative+apply) · (5) · 6 · 7 | 2 |
| **Til Fanlar** (Languages) | 0-A · 0-B · 1 · 2 (Reading) · 3 · (5) · 6 · 7 | 4 |
| **Ijtimoiy Fanlar** (Social / History) | 0-A · 0-B · 1 · 3 · (5) · 6 · 7 | 2, 4 |

Parentheses = lesson-archetype-dependent (see next section).

---

## Lesson archetype classification

Every section of every textbook in every grade falls into one of four archetypes. Classification is deterministic, not judgment-based — the agent inspects the section's content at pipeline entry.

| Archetype | Definition | Detection rule |
|-----------|-----------|----------------|
| **Concept Intro** | Introduces a new object, term, or definition | The section's key term appears for the first time in the textbook (grep across prior sections → zero hits) |
| **Algorithm** | Teaches a systematic method for an object defined earlier | Section's key object was introduced in a prior section; this section focuses on procedural steps |
| **Application** | Applies known methods in new contexts | All objects/methods exist earlier; this section's exercises mix them into new scenarios |
| **Review** | Revisits multiple prior sections explicitly | Section title contains "review/consolidation/summary" OR references ≥2 prior sections by name |

### Archetype × phase depth

**Legend:** ● essential (full depth) · ◐ medium · ○ light · — skip

| Phase | Concept Intro | Algorithm | Application | Review |
|-------|:---:|:---:|:---:|:---:|
| 0-A Preview | ● | ◐ | ○ | ○ |
| 0-B Flash Cards | ● | ● | ○ | ◐ |
| 1 Memory Sprint | ◐ | ● | ◐ | ● |
| 2 Reading (Languages) | ● | ○ | ◐ | — |
| 3 Game Breaks | ◐ | ◐ | ◐ | ◐ |
| 4 Real-Life | ● | ◐ | ● | ◐ |
| 5 Consolidation | — | ◐ | ● | ● |
| 6 Final Challenge | ◐ (light) | ● | ● | ● (full boss) |
| 7 Reflection | ● | ● | ● | ● |

Read rows: every phase that appears in the homework shows up with varying depth.
Read columns: Concept Intro front-loads teaching; Algorithm/Review front-load drilling.

---

## Final Challenge — adaptive spec

Renamed from "Final Boss" to reflect that the HP-combat format is not universal.

| Lesson archetype | Format | HP mechanic | Purpose |
|------------------|--------|-------------|---------|
| Concept Intro | **Light checkpoint** — one integrated problem, no combat framing | None | Closure, "you got it" |
| Algorithm | **Standard boss** — 3-5 questions, HP bar, tiered damage | Yes (grade-based HP) | Skill verification |
| Application | **Standard boss** — applied scenario with HP | Yes | Method-choice validation |
| Review | **Full boss** — max HP, all damage tiers, longest fight | Yes (+ checkpoint mid-boss) | Summative assessment |

HP table (from UNIFIED-Buzan, unchanged): G1-4 = 50 HP · G5-8 = 100 HP · G9-11 = 150 HP.
Damage tiers (unchanged): Easy –10 · Medium –20 · Hard –30.
Distribution: 40/40/20 (easy/medium/hard).

Concept Intro checkpoints skip the HP mechanic entirely — completion, not combat.

---

## Story Mode retirement — rationale

"Story Mode" as a universal phase is removed in v0.3 because it cross-passed with Real-Life Challenge. The narrative function splits cleanly:

- **Languages:** old Story Mode becomes **Reading Phase** (Slot 2) — IELTS-style comprehension.
- **Sciences:** narrative folds into Real-Life Challenge using the "Good_Demos biology/photosynthesis" pattern — tell the process as a compact story, then ask questions from it.
- **Math:** narrative embeds in Preview (Babylonian-farmer style) + applied story in Real-Life Challenge.
- **History:** narrative already lives in Preview. No replacement needed.

---

## Flash Cards vs Mind Maps

Both visual-recall tools are supported but serve different purposes:

| Tool | Purpose | Where it renders |
|------|---------|------------------|
| **Flash Cards** | Atomic recall — vocabulary, formulas, single facts | Phase 0-B (own phase) |
| **Mind Map / State Diagram / Process Flow** | Relational knowledge — state machines, cause-effect chains, hierarchies | Inside a Preview panel (Phase 0-A) |

### Rendering strategy

Mind maps are emitted as **Mermaid DSL** inside the panel content. Frontend renders them with Mermaid.js. Example:

```
graph LR
  A[x² = d] --> B{d > 0?}
  B -->|yes| C[2 real roots: ±√d]
  B -->|no| D{d = 0?}
  D -->|yes| E[1 root: 0]
  D -->|no| F[No real roots]
```

Advantage: pipeline stays text-based (agent-friendly); frontend handles visual rendering.

---

## Data collection framework

Reflection (Phase 7) is the silent analytics layer. It runs invisibly at session end and drives routing decisions. Four data layers:

### Layer 1 — Per-question data

| Field | Type | Purpose |
|-------|------|---------|
| `question_id` | string | Unique within homework |
| `phase_id` | enum | 0a, 0b, 1, 2, 3, 4, 5, 6 |
| `bloom_level` | L1-L6 | Tagged at generation |
| `pisa_level` | L1-L6 | Tagged at generation |
| `skill_tags` | array | [creativity, problem-solving, critical-thinking, memory, application, translation] |
| `correct` | boolean | Student answer vs expected |
| `time_seconds` | int | Time spent |
| `attempts` | int | Retries used |
| `hints_used` | int | 0+ |
| `difficulty` | enum | easy / medium / hard |

### Layer 2 — Per-phase data

| Field | Purpose |
|-------|---------|
| `phase_score_pct` | % correct in this phase |
| `phase_time_seconds` | Total time |
| `phase_completed` | Did student finish all items |
| `phase_skill_breakdown` | { creativity: X%, memory: Y%, ... } |

### Layer 3 — Per-session data

| Field | Purpose |
|-------|---------|
| `session_id` | UUID |
| `lesson_id` | Links to `nets_lessons` |
| `overall_score_pct` | Total % correct across graded phases |
| `passed` | boolean — `overall_score_pct ≥ 60` |
| `vs_student_avg` | Delta vs student's prior subject average |
| `route_decision` | Next-step recommendation |
| `skill_deltas` | Skill changes vs last session |

### Layer 4 — Routing algorithm

```
IF overall_score_pct < 60:
    identify weakest phase(s) by phase_score_pct
    identify failed questions within those phases
    queue remediation: Preview (relevant panels) → Flash Cards → failed questions only
    mark lesson as "remediation-required"
ELIF overall_score_pct ≥ 60 AND > student_subject_avg:
    advance to next lesson
    update student_subject_avg
ELSE:
    advance to next lesson; flag regression signal
```

Passing threshold: **60%** overall.

---

## Content quality metrics (framework validation)

Run post-generation, before homework reaches any student.

| Metric | Measurement |
|--------|-------------|
| **Schema validity** | JSON output conforms to `phase_N.json` schema (automated) |
| **Framework compliance** | Per-phase checklist: pronouns, format counts, tagging (automated + spot-check) |
| **Tagging coverage** | Every question has `[Bloom: LX \| PISA: LX]` (automated) |
| **Textbook fidelity** | No fact introduced that isn't in the source chapter (embed-diff + human review) |
| **Pronoun policy** | Zero "sen" / "ты" hits (automated regex) |
| **Cultural appropriateness** | No bazaar/village/shopkeeper clichés in Phase 4 (keyword scan + review) |
| **Cognitive variety** | Bloom levels span L2-L6 (no all-L1-recall homework; automated distribution check) |
| **Format rules** | Phase 1 = MC/T-F/YNNG only. Phase 3 = 3 games with correct mix (automated) |
| **Reproducibility rate** | Generate same lesson 3× — structure ≥95% identical, content variety 30-60% (automated diff) |

---

## Language quality metrics (Uzbek / Russian)

| Metric | Measurement |
|--------|-------------|
| **Grammar correctness** | External validator (Claude Opus / GPT-5) + native-speaker spot review |
| **Terminology consistency** | Subject-specific glossary match (e.g., "kvadrat tenglama" used consistently) |
| **Register** | Formal "Siz" / "Вы" throughout (automated) |
| **Translation quality** (bilingual) | Uzbek ↔ Russian pairs semantically equivalent (human review v1) |
| **Textbook term alignment** | Vocabulary matches textbook's exact terms where available |

---

## Open questions (to close before v1.0)

1. **Skill taxonomy lock-in** — final list of skills tracked. Current proposal: creativity, problem-solving, critical-thinking, memory, application, translation.
2. **Consolidation trigger rule** — formal definition of "lesson introduces ≥2 interlocking concepts" so agents tag deterministically.
3. **Data storage** — metrics in same Postgres as pipeline (`nets_session_data`, `nets_question_data`), or separate analytics store?
4. **Interactive games** — included in v1 or deferred to Premium tier?
5. **Mind map rendering stack** — Mermaid.js confirmed, or custom SVG for zero external deps?
6. **Remediation routing granularity** — re-route to exact failed questions, or to the parent phase?
7. **Boss HP for Review lessons** — same as UNIFIED table or boosted (e.g., ×1.5)?

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2026-04-20 | Initial proposal: "keep all 7 phases universally at full weight" |
| v0.2 | 2026-04-20 | Added lesson archetype classification + phase-weight matrix per archetype |
| v0.3 | 2026-04-20 | Removed Story Mode as universal phase (→ Reading for Languages, Real-Life narrative for Sciences/Math, Preview for History/Math). Moved mind maps inside Preview panels. Final Boss → Final Challenge with adaptive difficulty. Confirmed Reflection as silent analytics + routing layer. |

---

## Reference implementation

**Section 22 (Grade 8 Algebra · Kvadrat Tenglama)** is the v0.3 reference implementation. It is:
- Subject family: **Aniq Fanlar** (Math)
- Lesson archetype: **Concept Intro** (quadratic equation appears for the first time)
- Active phases: 0-A · 0-B · 1 · 3 · 4 · 6 (light checkpoint) · 7
- Skipped: 2 (Reading — Math family), 5 (Consolidation — single-concept intro)

This homework doubles as:
- Training data for the content-producer agent
- Gold standard for regression testing
- Benchmark for subject-family adaptation when we port the matrix to the next family

---

*End of v0.3 matrix document. Future revisions go above this line.*
