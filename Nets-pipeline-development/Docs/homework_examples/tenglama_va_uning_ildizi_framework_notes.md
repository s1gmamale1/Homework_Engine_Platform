# Framework Calibration & Session Notes — TENGLAMA VA UNING ILDIZI

**Subject:** Algebra G7 · Chapter IV, Lesson 1
**Companion file:** `tenglama_va_uning_ildizi.md` (the homework itself)
**Created:** 2026-04-18
**Purpose:** Document the design decisions, framework rules applied vs. broken, and systemic findings from hand-crafting this reference homework. Use this as calibration material when (a) auto-generating future homeworks via the pipeline, (b) restructuring the UNIFIED framework, or (c) hand-crafting reference homeworks for other lessons.

---

## Part 1 · Session overview

### What we set out to do

Build a **reference-quality gold-standard homework** for Grade 7 Algebra's introductory equation lesson ("Tenglama va uning ildizi"), following an Apple-like simplicity philosophy:

> *"Simple but perfect. A 7th grader should be able to understand it, actually learn from it, and find it easy to follow."*

Three core filter questions used on every design decision:

1. **Can a 7th grader understand this?**
2. **Will they actually learn something?**
3. **Is it easy to follow?**

If an element failed any one, it was cut or rewritten — even if the framework required it.

### Why this specific lesson

- **Small concept surface** — 5 new vocabulary words + 1 procedure + 3 outcome cases. Makes it a good stress-test of the framework's ability to handle *tight* lessons (much of the framework is calibrated for rich procedural lessons).
- **Introductory / pre-solving** — the student cannot yet systematically solve equations. This exposes framework rules that assume solving capability (Phases 2, 4, 6 all had issues).
- **Cultural anchor is natural** — al-Khwarizmi was born in Khorezm and gave algebra its name. Fits the National Pride module without forcing it.

### Constraints the user locked in

- **Language:** Uzbek (Latin)
- **Mode:** Homework is software delivered by an LMS (interactive, not paper)
- **Teacher assumption:** The teacher teaches the concept in class first. Homework is post-teaching practice + consolidation, not initial instruction.
- **Prior knowledge:** Student has 3 complete chapters of algebra behind them + G6 math. Not a blank slate.
- **Duration target:** 30–35 minutes.
- **Framework posture:** Use the UNIFIED framework as a library, not as law. Break rules that don't serve the lesson.

---

## Part 2 · Major decisions and course corrections

Listed roughly in the order they came up. Each was a real moment where my initial approach was wrong and the user pushed back (or I caught it on my own) and we corrected.

### Decision 1 · Pivoted away from the batch pipeline

**Before:** Earlier in the project we'd built a 9-phase Kimi-powered pipeline to auto-generate homeworks in bulk (Biology was the pilot).

**What happened:** A manual audit of the Biology §1 homework revealed systemic scope drift — the pipeline generated content from later chapters because the schemas didn't enforce current-lesson scope. The user decided that before scaling, we needed to first **build by hand what a perfect homework looks like** for each subject, then use those as calibration targets.

**Decision:** Drop the batch effort for this session. Start over with Grade 7 Algebra, hand-crafted, one lesson.

**Lesson for future:** Reference homeworks per subject must exist BEFORE the auto-generation pipeline can be trusted. The framework alone is not a sufficient specification — it needs worked examples as ground truth.

### Decision 2 · Reframed Phase 4 from "drop" to "keep and redefine"

**Before:** My first sketch said "drop Phase 4 entirely — the student can't set up equations from scratch yet."

**What happened:** I walked it back. The issue wasn't Phase 4's existence but its Algebra framework-specified purpose (*"Problem must require setting up an equation or inequality from scratch"*). For a pre-solving lesson, this purpose is wrong. But Phase 4's *actual* role — transfer application via first-person expert POV — can be satisfied with a verification scenario.

**Final design:** Phase 4 became *"Al-Khwarizmi Olympiad Judge"* — student verifies 3 competitors' claims. Fits first-person expert POV, uses only checking (no construction), naturally carries the heritage anchor.

**Lesson for future:** When a framework rule fails, question the rule's letter (the specific activity it mandates) before questioning the rule's spirit (what the phase is for). Often the spirit still applies; only the letter needs a novice-mode variant.

### Decision 3 · Corrected the "checking only" framing

**Before:** My Phase 0-A hook said *"Today you learn to check without solving."* I treated the lesson as 100% about checking.

**What happened:** The user pushed back — *"I keep doubting if it is really checking instead of solving. Can you recheck?"*

**Audit result:** Went through all 15 textbook exercises. Found:
- ~70–80% are pure substitution checking
- ~20–30% require light reasoning (no-root proofs, identity recognition, equivalence detection)

The lesson also formally defines what *solving* means — it's not anti-solving, it's introducing *checking* as a tool alongside the definition of solving.

**Revised framing:** The lesson is **40% formalize vocabulary, 30% learn the checking tool, 20% recognize edge cases, 10% set up next lesson.** Phase 0-A hook was rewritten to be honest about this scope rather than narrowing to just "checking."

**Lesson for future:** Over-narrow framing makes the hook crisp but misrepresents the lesson. When the user doubts a reductive framing, trust the doubt and re-audit against the source material.

### Decision 4 · Corrected assumption about student's prior knowledge

**Before:** I was implicitly treating the student as a near-blank slate — "they haven't met equations formally."

**What happened:** The user: *"There is 3 more chapters before this in the same book, so they are all kind of connected."*

**Audit result:** Pulled the textbook TOC. Student completed:
- Chapter 1 (15 topics): Algebraic expressions, variables, formulas, coefficients, polynomials
- Chapter 2: Short multiplication formulas including `(a+b)²`
- Chapter 3: Algebraic fractions
- G6 math: Simple equation solving via inverse operations

**What changed in the design:** The lesson isn't *introducing* variables or the idea of equations. It's **formalizing a familiar pattern and giving it precise vocabulary.** Kid-questions shifted from "what's an equation?" (naive) to "I've been using x for months, why formally define it now?" (legitimacy question).

**Lesson for future:** Always check prior-chapter scope before designing. A lesson's teaching goal depends heavily on what the student walks in knowing.

### Decision 5 · Retracted three framework critiques as too-broad

During Phase 2 stress-test I had made three claims I later walked back:

| Initial claim | Retraction |
|---|---|
| "Drop Phase 4 entirely" | Phase 4 works as a verification scenario; Algebra-framework's specific phrasing is what's broken, not the phase itself |
| "Phase 3 should be one game, not three" | Three games can drill three distinct sub-skills (pattern recognition, accuracy, equivalence); not padding if designed carefully |
| "Phase 0-A's 8 panels fail 'easy to follow'" | Too broad — Panels 1-5 are content-adjacent and useful; only Panels 6-8 (BOST confirmation, industry, mathematician) are ceremony for a tight concept |

**Lesson for future:** When stress-testing the framework, distinguish between "rule is wrong for all lessons" vs. "rule is over-specified for this lesson type." Most framework issues fall in the second category.

### Decision 6 · Committed to the kid-questions methodology

A turning point mid-session. Instead of starting from "what does the framework say Phase X should contain," I started from "what questions does a 7th grader naturally ask when learning this?"

Final kid-questions list (ranked by confusion-if-unanswered):

| # | Question | Priority |
|---|---|---|
| 1 | Wait — I've been using x for months. Why formally define "equation" NOW? | HIGH |
| 2 | How is `tenglama` different from `tenglik` and `formula`? | HIGH |
| 3 | How is `ildiz` different from just "the answer"? | HIGH |
| 4 | Can equations really have NO answer? | HIGH |
| 5 | And some have INFINITE answers?! | HIGH |
| 6 | Why check when I can solve? | HIGH |
| 7 | If two equations have the same root, are they the same? | MEDIUM |
| 8 | What if I make an arithmetic error while checking? | MEDIUM |
| 9 | Why is it called "root"? | LOW-MEDIUM |
| 10 | How is this different from 6th grade? | LOW |

Every phase was then designed to land at least one of these questions. Phases that didn't answer a kid-question got cut or redesigned.

**Lesson for future:** Start every homework design with a kid-questions list *before* reading the framework specs. Let the kid-questions drive; use framework rules as a library to pick from.

### Decision 7 · Accepted the distinction between "illustrative" and "worked" examples on flashcards

**Framework rule (§4.5):** Flashcards must NOT contain worked examples.

**Tension:** A definition card like "Ildiz = value that makes equality true" is jargon for a 12-year-old without seeing it played out once. Card 3 (Ildiz) included the substitution check as an illustrative example. Strictly interpreted, this breaks the framework rule.

**User's call:** Keep the illustrative example (Option A). Break the framework rule. Document the tension as a framework calibration issue — the rule's intent is probably to ban *practice problems* (things the student is expected to reproduce), not *illustrative examples* (one-off demonstrations of meaning).

**Lesson for future:** Framework rules often conflate two subtly different things. When pressure-testing, separate the rule's target (what it's trying to prevent) from its stated form (what it literally says). Often the target is right but the form is too broad.

### Decision 8 · Kept all 9 phases

After flip-flopping on Phase 4, the final decision: all 9 phases retained. Each earned its spot by serving at least one kid-question and passing the 3 core filter questions. None included for framework compliance alone.

---

## Part 3 · Framework rules applied as-specified

These rules from the UNIFIED-Buzan framework served the lesson well and were honored without modification.

| Phase | Rule | Source |
|---|---|---|
| 0-B | Reference-deck rules: no practice, no quizzes, one concept per card, returnable throughout homework | UNIFIED §4.5 |
| 0-B | Dual coding (each card has term + icon + example) | Buzan general principle |
| 1 | Tap-only formats (MC / T-F / YNNG) — no typing, no drag-drop | UNIFIED §5.1 |
| 1 | ≥2 formats mixed per sprint | UNIFIED §5.1 |
| 1 | ≤2 min hard cap | UNIFIED §5.1 |
| 1 | Primacy effect — most fundamental items first | Buzan MIG |
| 1 | Current-chapter only (2026-04-15 update, line 633) | UNIFIED §5.1 |
| 1 | Speed bonus (<5s = +10 XP), streak bonus (3-in-a-row = +10 XP), no penalty for wrong | UNIFIED §5.1 |
| 2 | ONE continuous narrative, no labels ("Muammo:", "Kurash:", etc.) | UNIFIED §5.2 |
| 2 | Problem → Struggle → Discovery → Solution arc woven invisibly | UNIFIED §5.2 |
| 2 | Stranger Test (reader who hasn't seen textbook can follow using only story logic) | UNIFIED §5.2 line 734 |
| 2 | 3 comprehension checkpoints, max 2 retries, simplified variant on 3rd wrong | UNIFIED §5.2 |
| 2 | Variable named before first equation appears | Algebra framework §4.2 |
| 3 | Dual-catalog (≥1 Interactive + ≥2 Default) | UNIFIED §5.3 |
| 3 | Von Restorff Anchor on middle slot (Mystery Box = the memorable game) | UNIFIED §5.3 |
| 3 | Cortical diversity ≥2 modalities (Tile Match = Visual/Spatial; Mystery Box = Strategic; Adaptive Quiz = Verbal/Logical) | UNIFIED §5.3 |
| 3 | Games pulled from 17-mechanic library (Tile Match #03, Mystery Box #08, Adaptive Quiz #07) | UNIFIED game specs |
| 4 | First-person expert POV ("Siz — yordamchi sudyasiz") | UNIFIED §5.4 |
| 4 | Wise Status with heritage anchor (al-Khwarizmi Olympiad framing) | UNIFIED §5.4 |
| 4 | Justification required, not just verdict | UNIFIED §5.4 |
| 4 | Tricky questions with plausible wrong answers (Sardor's "yagona" trap) | UNIFIED §5.4 |
| 5 | Technique selection via content-structure table — Hierarchical → Radiant Summary | UNIFIED §5.5 + Algebra §4.5 |
| 5 | Active interaction only (drag-and-drop, no passive reading) | UNIFIED §5.5 |
| 5 | SMASHIN' SCOPE ≥6/12 (we scored 10/12) | UNIFIED §5.5 line 1057 |
| 5 | Formative gate — no pass/fail, attempt sufficient | UNIFIED §5.5 |
| 5 | *"Yana bir marta"* framing, never *"Hali emas!"* in Phase 5 | UNIFIED §5.5 line 1055 |
| 5 | Content source = `keywords_80_20` from Story Mode | UNIFIED §5.5 line 778 |
| 5 | Algebra-specific Step Reconstruction addition (45 sec) | Algebra §4.5 |
| 6 | HP = 100 for G5–8 band | UNIFIED §5.6 |
| 6 | 40/40/20 Easy/Medium/Hard distribution | UNIFIED §5.6 |
| 6 | No MC for G7+ | Algebra §4.6 + UNIFIED §5.6 |
| 6 | TEFCAS framing (*"Hali emas! Miyangiz Feedback oldi."*) | UNIFIED §5.6 |
| 6 | Socratic hints (prompt questions, never reveal method) | UNIFIED §5.6 |
| 6 | Combo bonus (3 correct → 2× next damage) | UNIFIED §5.6 |
| 6 | Notebook Capture accepted as submission | Algebra §5 |
| 7 | TEFCAS-framed prompts | UNIFIED §5.7 |
| 7 | Accuracy-adaptive prompt templates (≥80% / 60-79% / <60%) | UNIFIED §5.7 |
| 7 | BOST goal resurfacing from Phase 0-A | UNIFIED §5.7 |
| 7 | Spaced repetition schedule display (1d / 3d / 7d / 21d) | UNIFIED §5.7 |
| 7 | National Pride closing gated at ≥60% accuracy | UNIFIED §5.7 |
| 7 | TEFCAS encouragement for <60% (no pride inflation) | UNIFIED §5.7 |
| 7 | Privacy: student-only with teacher seeing aggregate themes | UNIFIED §5.7 |
| 7 | "First time on topic" curiosity hook (line 1574) | UNIFIED §5.7 |
| 7 | Al-Khwarizmi heritage anchor (Algebra framework: mandatory 1 per 3 sessions) | Algebra §3.4 |

**Framework rules used: ~45.** These are the parts of the framework that worked — keep them.

---

## Part 4 · Framework rules broken (with reasoning)

Rules we deliberately did NOT follow, organized by phase with justification.

### Phase 0-A

| Rule | Why broken | Proposed resolution |
|---|---|---|
| 8 panels of 5–10 sentences each (§4.4) | 8 panels of ceremony before any teaching fails Q3 for a tight conceptual lesson. Compressed to 3 screens. | Framework should define "compact 0-A" variant (3–4 screens) for short conceptual lessons; keep 8 panels for rich procedural lessons |
| 5-second gate quote lock (§4.4) | Ceremony without content value for this lesson's scale | Make gate quote OPTIONAL per lesson type |
| Industry Application panel (§4.4) | Couldn't make it serve the lesson's actual content without feeling bolted-on | Should be optional per lesson |
| Panel 7 Industry Application + Panel 8 Mathematician Spotlight as separate panels | Compressed into later phases (Phase 4 has the Olympiad/industry hook, Phase 7 closing has al-Khwarizmi) where they carry more weight | Allow content panels to migrate to other phases when those phases can hold them more naturally |

### Phase 2

| Rule | Why broken | Proposed resolution |
|---|---|---|
| CPA progression (Concrete → Pictorial → Abstract) (§5.2, Algebra §4.2) | Lesson concept is symbolic from day one — no natural concrete-object phase | CPA should be flagged as inapplicable to definitional / formalization lessons (as opposed to arithmetic or geometry lessons where it fits) |
| "Amir Temur Campaign" G7 narrative frame (Algebra §4.2) | Classroom setting is more relatable and lets the story focus on the math | Narrative frame should be optional per lesson type, not prescribed |

### Phase 4

| Rule | Why broken | Proposed resolution |
|---|---|---|
| "Problem must require setting up an equation or inequality from scratch" (Algebra §4.4) | Student hasn't been taught equation construction yet. Forcing this would test a skill outside the lesson. | Algebra framework needs a **verification-mode variant** for pre-solving lessons where the student verifies a claim instead of constructing an equation |
| W5H scaffold mandatory for G7–8 (UNIFIED §5.4) | Single-skill verification across 3 instances doesn't have the multi-factor structure W5H is designed for | Algebra framework agrees (W5H only for multi-factor scenarios) — UNIFIED should match |

### Phase 6

| Rule | Why broken | Proposed resolution |
|---|---|---|
| "Equation solving (show steps)" as required Boss question type (Algebra §4.6) | Student hasn't been taught systematic solving. Requiring it would test out-of-scope skill | Allow "substitution proof" and "equation construction from a given root" as valid Boss question types for pre-solving lessons |
| "Modeling question — student writes equation from scenario" (Algebra §4.6) | Same — beyond this lesson's skill scope | Allow "construction without scenario" as valid L5 task for introductory lessons |
| 3-tier Sub/Big/Mythical Boss system (UNIFIED §5.6) | Using only Sub Boss. Big/Mythical are cross-lesson aggregates that don't apply to a single-lesson homework | Document that Big/Mythical are LMS-runtime features, not lesson-content features |

### Phase 1 & others

| Rule | Why broken | Proposed resolution |
|---|---|---|
| National Pride injection in Phase 1 (~1 in 5 items) | Forcing professional framing on a vocabulary check would fail Q1 | National Pride should be load-bearing where it fits naturally (Phase 4, Phase 7 closing) and NOT mandated per phase |

### Phase 7

| Rule | Why broken | Proposed resolution |
|---|---|---|
| Hesitation-triggered logic (per-concept stuck detection) | Requires LMS runtime tracking of hesitation time per question — not static content | Document as LMS runtime feature, not homework content |
| Streak-triggered celebration (≥5 correct) | Adds ceremony without serving Q2 for this lesson's scale | Make optional |

**Framework rules broken: 12.** Most were over-specifications for short conceptual lessons or rules requiring solving skill the student doesn't have yet.

---

## Part 5 · Systemic findings for framework restructuring

Across the 12 broken rules, three root causes emerged. These are the priority items for framework revision.

### Finding 1 · Missing "introductory lesson" mode

**Problem:** Framework acknowledges introductory lessons exist (*"Why Chain banned in intro lessons"* line 1419, *"first time on topic"* variant line 1574) but does not systematically re-spec Phases 2, 4, and 6 for the case where the student cannot yet perform the lesson's procedure.

**Impact:** When designing a lesson that introduces a concept before the procedure (common for first-lessons-of-chapter), Phases 2/4/6 need novel-mode variants that the framework currently doesn't define. This led to 4 of the 12 rule breaks in this session.

**Proposed restructure:** Add a formal "novice mode" to the framework for Phases 2, 4, and 6:

- **Phase 2 novice mode:** Arc ends in verification (student uses the new tool), not solution (full algebraic execution)
- **Phase 4 novice mode:** "Check-a-claim" scenario, student verifies peer or expert claim rather than constructing an equation
- **Phase 6 novice mode:** Boss swaps "solve with steps" for "construct an example" or "prove a property" at the L5 slot

Each phase gets two variants: **procedural mode** (student has the skill) and **novice mode** (student is learning the concept for the first time). Current framework defaults are all procedural mode.

### Finding 2 · Scope-binding is not enforced at the schema layer

**Problem:** Framework relies on prose instructions like "stay in current lesson" but JSON schemas don't require `concept_ref` or `textbook_ref` fields tying each generated item to a specific lesson concept. This is the exact root cause observed in the earlier Biology §1 pilot where the pipeline drifted into §4, §8, §15 content.

**Impact:** In hand-crafted work (like this homework) scope is self-enforced by the human designer. But for auto-generation via the pipeline, scope drift is effectively unconstrained. The current homework's schemas would accept a Phase 3 game about photosynthesis even if the lesson is about equations, because there's no `concept_ref` field being validated.

**Proposed restructure:**

- Add required `concept_ref` field to every phase schema (Phases 2, 3, 4, 5, 6)
- `concept_ref` must match a concept in an **extraction manifest** produced by Stage 1 (Extract)
- Make `extraction.md` a proper gated contract that produces a structured concept manifest — not just a prose description
- Add a validator check that every generated item's `concept_ref` is in the manifest

This is the highest-leverage change for making the auto-generation pipeline trustworthy.

### Finding 3 · Phase 0-A over-specification for short lessons

**Problem:** 8-panel, 5–10-sentences-per-panel mandate disproportionately front-loads short conceptual lessons. For a 30-min homework on a tight concept (like this one), 8 panels is ~30-40% of the total time before any practice begins.

**Impact:** Three rules broken in Phase 0-A alone (panel count, gate quote lock, Industry panel).

**Proposed restructure:** Phase 0-A should scale with lesson type:

| Lesson type | 0-A size |
|---|---|
| Tight conceptual (formalize vocabulary, introduce a definition) | 3 screens |
| Standard procedural (learn a procedure, apply it) | 5–6 panels |
| Rich multi-concept (multi-step procedure + application) | 8 panels |

Add guidance in §4.4 about which type applies.

---

## Part 6 · New rules and distinctions proposed

Small additions that emerged from this session that would improve the framework.

### New distinction · "Illustrative example" vs "Worked example"

**Context:** Framework §4.5 bans "worked examples" on flashcards. This conflates two different things.

**Proposed distinction:**
- **Worked example** = a problem the student is expected to reproduce (practice). Ban this on flashcards — belongs in Phase 3.
- **Illustrative example** = a one-off demonstration of what a term means (definition clarity). Allow this on flashcards — it's dual coding.

**Example from this homework:**
- Card 3 (Ildiz) includes *"ildiz = 10. Tekshirish: 4(10) − 15 = 10 + 15 → 25 = 25 ✓"* — this is illustrative (shows what a "root" looks like once), not worked (student is not expected to reproduce this check from the card).

### New rule · Intro-lesson narrative arc exception

**Context:** Phase 2's required arc is Problem → Struggle → Discovery → **Solution** (full algebraic solution per current §5.2 language).

**Proposed amendment:** For intro lessons, the arc's final beat is **Application of the new tool**, not solution. Example: *"Sevinch used the new checking tool to verify all three equations — one has 1 root, one has none, one has infinite."* That's a valid arc ending for a pre-solving lesson.

### New rule · Heritage anchor placement flexibility

**Context:** Algebra framework says al-Khwarizmi is mandatory 1 per 3 sessions across Phase 0-A Panel 8 OR Phase 5 mnemonics.

**What we did:** Moved al-Khwarizmi from Phase 0-A (where it would feel forced as a panel for a tight lesson) to Phase 7 closing (where it lands after the kid has earned the cultural connection) + Phase 4 (as the Olympiad framing's natural context).

**Proposed amendment:** Allow heritage anchor to move to any phase where it lands naturally, as long as **one strong landing per session** is achieved. Don't require a specific phase.

---

## Part 7 · Methodology for designing the next reference homework

A checklist distilled from this session, to apply when building the next hand-crafted homework.

### Phase 0 — Before you design anything

1. **Read the lesson** in the textbook carefully. Extract:
   - The exact definitions taught
   - The worked examples shown
   - The exercises at the end
   - Any side panels ("Eslaymiz," etc.)
2. **Read the prior chapters' TOC** — what does the student already know?
3. **Check what comes next in the textbook** — what's this lesson setting up for?
4. **Classify the lesson type:**
   - Tight conceptual (formalize vocabulary, introduce definition) → use compact formats
   - Standard procedural (learn a procedure, apply it) → use full framework defaults
   - Rich multi-concept → use expanded formats

### Phase 1 — Kid-questions map

5. **Brainstorm 8-12 natural kid-questions** — what would a student of this age, at this point in the curriculum, actually ask?
6. **Rank them HIGH / MEDIUM / LOW** by how confused the student would be if unanswered.
7. **The HIGH-priority questions drive the design.** Every phase of the homework must address at least one.

### Phase 2 — Phase-by-phase design

8. **For each phase, draft the content before consulting the framework.** What does *this lesson* need at this point?
9. **Then compare your draft to the framework's rule for that phase.** Document where you used a rule, broke a rule, and why.
10. **Apply the 3 core filter questions** (Q1 understand / Q2 learn / Q3 easy to follow) to every element. Cut whatever fails any of them.
11. **Stress-test across phases:**
   - Does Phase 0-B prepare the kid for what Phase 1 tests?
   - Does Phase 2's story teach what Phase 3's games drill?
   - Does Phase 6 test only what was taught in Phases 0-B through 5?
   - Does Phase 7 resurface BOST + the lesson's actual learning?

### Phase 3 — Framework calibration

12. **Document every rule you used** (for framework validation).
13. **Document every rule you broke** with specific reason.
14. **Flag new rules or distinctions** that would improve the framework.
15. **Write the clean homework file + the calibration-notes file as separate artifacts.**

---

## Part 8 · Open questions and follow-ups

Items we didn't resolve in this session and should think about later.

1. **Should we build compact 0-A as a first-class framework variant, or keep it as case-by-case override?** Decision needed before the next hand-crafted math lesson.

2. **What's the naming convention for novice-mode vs procedural-mode phase variants?** E.g., do we call them `phase_2_novice.md` / `phase_2_procedural.md` or keep one file with sections?

3. **Does the pipeline need separate schemas for novice vs procedural mode?** Or can the same schema with added fields (`lesson_type`, `concept_ref`) handle both?

4. **How many more hand-crafted reference homeworks before we trust the pipeline?** The user said "start with math" — suggests at least a few more from math + one per subject family before scaling.

5. **The framework's `keywords_80_20` extraction method** is documented but the pipeline doesn't enforce that Phase 5's content actually comes from Phase 2's keywords. Should we hand-extract keywords for this reference homework as a test?

6. **Al-Khwarizmi etymology** (*"al-jabr"* = "reunion of broken parts") is currently on Phase 7's closing line only. Is once per lesson enough, or should the etymology resurface in Phase 0-A as the heritage anchor?

7. **Checkpoint retry logic in Phase 2** — framework says max 2 retries then simplified variant. We didn't spec what "simplified variant" looks like for each of our 3 checkpoints. This would need to be designed before the homework can actually ship.

8. **For auto-generation** — when the pipeline generates a homework in the future, should it *first* consult the relevant reference homework as a style/calibration anchor, *then* generate? This is a training-data-like use but at inference time.

---

## Part 9 · Summary in one paragraph

We built a reference-quality homework for Grade 7 Algebra's introductory equation lesson by starting from kid-questions and using the UNIFIED framework as a library. Of ~57 framework rules touched, we applied ~45 as-specified and broke ~12 deliberately — most breaks traced to three root causes (missing introductory-lesson mode, scope-binding not enforced at schema layer, Phase 0-A over-spec for short lessons). All 9 phases were kept; each earned its spot by answering at least one priority kid-question. The output is a ~33-minute homework where every element passes the three-question filter: a 7th grader can understand it, will actually learn from it, and finds it easy to follow. The major framework changes this session suggests are (a) formal novice-mode variants for Phases 2/4/6, (b) schema-level `concept_ref` enforcement for pipeline scope-binding, and (c) tiered Phase 0-A sizing by lesson type.
