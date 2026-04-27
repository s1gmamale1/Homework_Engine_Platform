---
name: Phase 6 — Final Challenge
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.6 (lines 1099-1240) + §22 session + Matrix v0.4
---

# Phase 6 — Final Challenge

## Purpose (WHAT)

Summative assessment gate and session closure moment: the peak of cognitive load for the session. The student must demonstrate competence at their target PISA level to pass. Format adapts to the lesson archetype — light checkpoint for Concept Intro, HP-combat boss for Algorithm/Application, full boss with mid-boss checkpoint for Review.

## Structure (HOW)

**Adaptive format — archetype drives format selection:**

| Lesson archetype | Format | HP mechanic | Question scope | Purpose |
|-----------------|--------|-------------|---------------|---------|
| Concept Intro | **Light Checkpoint** — 1 integrated problem, 5–6 questions chained, no combat framing | None | Current lesson only | "You got it" closure |
| Algorithm | **Standard Boss** — 3–5 questions, HP bar, tiered damage, 40/40/20 distribution | Yes (grade-based HP) | Current lesson only | Skill verification |
| Application | **Standard Boss** — applied scenario with HP | Yes (grade-based HP) | Current lesson only | Method-choice validation |
| Review | **Full Boss** — max HP per grade band, all damage tiers, checkpoint mid-boss | Yes (grade-based HP) | All reviewed content + checkpoint mid-boss | Summative assessment |

**HP pools and damage values: see `00-core/hp-damage-baseline.md` for authoritative values.**

Summary for reference (do not use as override — source of truth is hp-damage-baseline.md):
- G1–4 = 50 HP · G5–8 = 100 HP · G9–11 = 150 HP
- Matematika G5–6 override = 80 HP
- Easy = –10 HP · Medium = –20 HP · Hard = –30 HP
- Hint tax: G1–4 = –5 HP (boss regains) · G5–8 = –10 HP · G9–11 = –15 HP
- Distribution: 40% Easy / 40% Medium / 20% Hard

**3-Tier Boss System (updated 2026-04-07):**

| Boss Tier | Trigger | Difficulty | Hints | Reward |
|-----------|---------|------------|-------|--------|
| **Sub Boss** | End of every homework session (default) | Calibrated to student's PISA level | Socratic tutoring available | Standard XP + stars |
| **Big Boss** | Weekly (replaces that week's final Sub Boss) | One tier above student's current PISA level | Same as Sub Boss | 2× XP + weekly badge + streak freeze if >80% |
| **Mythical Boss** | Random, <5% chance per session — cannot be predicted, forced, or farmed | PISA L5–6 regardless of student level | **Zero hints. One attempt only.** | 5× XP + exclusive title + avatar frame + Hall of Fame entry |

The remainder of this specification (HP, damage, question schema, failure flow, stars) applies to Sub Boss and Big Boss. Mythical Boss overrides are noted inline where they differ.

**Light Checkpoint structure (Concept Intro archetype):**

1. One integrated problem presented as a narrative scenario using the lesson's key concept.
2. 5–6 chained sub-questions, each building on the previous answer.
3. No HP bar, no combat framing. Completion-gated only.
4. On first wrong answer → targeted hint (automated). On second wrong answer → stronger hint. On third wrong answer → reveal + remediation flag raised in Phase 7.
5. Time budget: 5–6 min. No stars calculated (completion only).

**Standard Boss structure (Algorithm / Application archetypes):**

1. HP bar displayed at top with boss avatar. Student's role: dealmaker / challenger / analyst (professional framing — never "warrior" for older grades).
2. Questions served in 40/40/20 order (Easy → Medium → Hard) with explicit PISA-level and Bloom-level tags visible to student as color-coded difficulty indicators.
3. Combo bonus: 3 correct in a row → 2× damage on next question.
4. On incorrect answer → Socratic tutoring activates (Tier 3 AI): *"Hali emas!"* TEFCAS framing — CHECK (where is the gap?) → ADJUST (different approach?) → re-attempt. AI asks guiding questions; never gives the answer.
5. If boss not defeated after all questions (HP > 0): identify failed standards, map to textbook sections, regenerate questions (same standards, different numbers/context), student re-attempts. No question cap on re-attempts.
6. Time budget: 8–10 min (Standard) / 10–15 min (Extended).

**Full Boss structure (Review archetype):**

- All Standard Boss rules apply.
- Scope extended: questions span all reviewed content in the Review session, not just the current chapter.
- Mid-boss checkpoint: after ~50% HP depleted, a brief pause — performance summary shown, student can review flagged hints before continuing.
- Extended failure flow: if boss not defeated, AI maps failures to the specific Story Mode or Preview segments the student needs, routes back for targeted re-study before boss regeneration.

**Question schema (every boss question must conform):**

```json
{
  "question_text": "...",
  "standard_ref": "UZ-SUBJECT-GRADE-DOMAIN-NN",
  "textbook_ref": { "chapter": "...", "section": "...", "page": "..." },
  "pisa_level": 3,
  "pisa_domain": "...",
  "pisa_content": "...",
  "pisa_process": "...",
  "pisa_context": "...",
  "transition_skill": "L2->L3: ...",
  "blooms_level": "apply",
  "difficulty_tier": "medium",
  "correct_answer": "...",
  "scoring_rubric": {
    "full_marks": "...",
    "partial_marks": "...",
    "no_marks": "..."
  },
  "solution_steps": ["1. ...", "2. ...", "3. ..."],
  "socratic_hints": ["...", "...", "..."],
  "common_errors": [
    { "error": "...", "misconception": "...", "remediation_hint": "..." }
  ]
}
```

**Inline tags on every question (mandatory):** `[Bloom: LX | PISA: LX | Damage: -XX HP]`

**PISA-tiered damage system:**

| Difficulty | Damage | PISA Level | Bloom's Level |
|-----------|--------|-----------|--------------|
| Easy | –10 HP | L3 | Apply |
| Medium | –20 HP | L4 | Analyze |
| Hard | –30 HP | L5–6 | Evaluate / Create |

**Question type restrictions by grade:**

| Grade band | Allowed question types |
|-----------|----------------------|
| G1–4 | Multiple choice + short answer |
| G5+ | Short answer + open reasoning. **No MC for G5+.** G5 exception: up to 30% MC allowed. |
| G9–11 | Open reasoning + extended response only |

**Calculation capture rule:** For questions requiring multi-step calculation, the student's solve steps are captured for rubric scoring. See `00-core/capture-rule.md` for capture trigger conditions and rubric schema.

**Failure flow:**

```
IF boss NOT defeated (HP > 0 after all questions):
  1. IDENTIFY failed learning objectives
  2. MAP failures to specific textbook sections and standards
  3. ACTIVATE Socratic Tutoring (Tier 3 AI) — TEFCAS framing:
     - "Hali emas! Miyangiz Feedback oldi."
     - CHECK: "Keling, tekshiramiz — qayerda tushunmovchilik bor?"
     - ADJUST: "Buni boshqacha yondashsangiz nima o'zgaradi?"
     - AI guides, NEVER gives answers
     - Routes to specific Story Mode / Preview segment
  4. REGENERATE boss questions (same standards, different numbers/context)
  5. Student re-attempts → SUCCESS

Mythical Boss override: steps 3–5 do NOT apply. No tutoring. No regeneration.
Failure message only: "The Mythical Boss retreats... for now." Small participation XP awarded.

IF boss defeated → proceed to Phase 7, calculate Mastery Stars.
```

**Mastery Star calculation (Sub Boss and Big Boss only):**

| Stars | Criteria | Unlocks |
|-------|----------|---------|
| 1 Star | Boss defeated (any number of attempts) | Chapter complete |
| 2 Stars | Boss defeated in ≤2 attempts, >50% HP remaining | Bonus avatar item |
| 3 Stars | Boss defeated on first attempt, no hints used, >80% HP remaining | Special badge progress |

Light Checkpoint: no stars. Completion only.

**Scoring weight:** Phase 6 contributes 30% of total session score.

**Failure language — TEFCAS (Phase 6 register):**
- *"Hali emas!"* (Not yet!) — the only acceptable failure phrase in Phase 6. Never "Noto'g'ri", never "Xato".
- Socratic tutoring walks the student through TEFCAS: Check → Adjust → Success.

## Cognitive load

- **Bloom range:** L3 (Apply) → L6 (Create). Peak cognitive load for the session.
- **PISA range:** L3 (standard) → L5–6 (Hard tier / Mythical Boss).
- **Scoring:** Yes — 30% of total session score.
- **Time budget:** 5–6 min (Light Checkpoint) / 8–10 min (Standard, Standard mode) / 10–15 min (Standard, Extended mode).
- **AI Tier:** Tier 3 (Socratic tutoring on failure — premium AI). Tier 1 for pre-generated question delivery.

## Inputs

- Textbook chapter content (primary source for question generation — current chapter for Sub Boss; all reviewed content for Big Boss/Review archetype).
- Student's current PISA level per subject (from prior session records or onboarding assessment).
- Student's HP pool (from grade band + subject override — see `00-core/hp-damage-baseline.md`).
- Lesson archetype tag (determines format: Light Checkpoint vs Standard Boss vs Full Boss).
- Boss tier tag (Sub Boss / Big Boss / Mythical Boss — set by session orchestrator).
- Phase 5 completion flag (`phase_5_complete: true`) — Phase 6 must not render until Phase 5 is complete (or confirmed skipped).
- Weak standards data (for Big Boss: AI-identified 3 weakest standards across all subjects).

## Outputs

- `phase_6_complete: true` flag → required before Phase 7 renders.
- `boss_defeated: boolean` → determines star calculation and routing in Phase 7.
- `stars_earned: 0 | 1 | 2 | 3` → stored in student progress record.
- `phase_score_pct` → Phase 7 data collection Layer 2 (per-phase data).
- `phase_time_seconds` → Phase 7 data collection.
- Per-question data (question_id, correct, time_seconds, attempts, hints_used, bloom_level, pisa_level, damage_dealt, skill_tags) → Phase 7 data collection Layer 1.
- `standards_mastered: []` and `standards_needs_work: []` → Phase 7 Reflection + teacher dashboard.
- `capture_submitted: boolean` and `capture_rubric_score` (when capture triggered) → Phase 7 data collection.
- `remediation_flag: boolean` → raised when Light Checkpoint reaches 3rd wrong answer; consumed by Phase 7 routing algorithm.
- XP awarded → gamification economy (see `00-core/gamification-economy.md`).

## Adaptable parameters

| Parameter | Default | Override per archetype | Override per family |
|-----------|---------|------------------------|---------------------|
| Format | Standard Boss (HP combat) | Concept Intro → Light Checkpoint; Review → Full Boss | — |
| HP pool | Grade-based (see hp-damage-baseline.md) | Matematika G5–6 → 80 HP | — |
| Question count | 5 | Light Checkpoint: 5–6 chained sub-questions; Full Boss: up to 8 | — |
| MC allowed | No (G5+) | G5: up to 30% MC | — |
| Hints | Socratic tutoring (Tier 3) | Mythical Boss: ZERO hints | — |
| Re-attempt cap | Unlimited | Mythical Boss: 1 attempt only | — |
| Time budget | 8–10 min | Light Checkpoint: 5–6 min; Extended mode: 10–15 min | — |
| Stars | 0–3 | Light Checkpoint: no stars (completion only) | — |
| Scoring weight | 30% of session | — | — |
| Mid-boss checkpoint | Off | Review (Full Boss): On at ~50% HP | — |

## Subject-specific examples

**Aniq Fanlar (Matematika — Grade 6, Fractions — Standard Boss):**
- 5 questions: 2 Easy (single-step fraction operations, PISA L3, Bloom Apply), 2 Medium (multi-step word problems with method selection, PISA L4, Bloom Analyze), 1 Hard (budget/design problem with multiple constraints, PISA L5, Bloom Evaluate).
- No MC. All short answer with step capture. Common errors: forgetting to find common denominator, applying 20% as subtraction instead of multiplication.
- Sample Medium question: *"Bozorda 1 kg olma narxi 15,000 so'm. Jasur 2.4 kg olma va 1.8 kg nok sotib oldi. Nok narxi olmadan 20% qimmat. Jasur qancha pul to'ladi?"* `[Bloom: L4 | PISA: L4 | Damage: -20 HP]`

**Tabiy Fanlar (Biology — Grade 7, Cell Division — Standard Boss):**
- Scenario: a researcher's microscope images of 5 cells are shown. Student must identify the mitosis stage for each cell and explain the diagnostic feature used.
- No MC. Medium questions require "explain why" — Bloom Analyze. Hard question: *"Design an experiment to observe the effect of temperature on mitosis rate."* Bloom Create.

**Ijtimoiy Fanlar (Tarix — Grade 6, Silk Road — Standard Boss):**
- Questions require analysis of cause-effect (why did the Silk Road decline?) and source evaluation (is this primary source credible?). No MC.
- Modern professional framing: student is a *Tarixiy Tadqiqotchi* (Historical Researcher) producing a report.

**Til Fanlar (English — Grade 8, Conditionals — Light Checkpoint, Concept Intro archetype):**
- 1 integrated scenario: a student is planning a trip. 5 chained sub-questions require writing Zero, First, and Second conditionals in natural context.
- No HP combat. On 3rd wrong answer: reveal + flag raised. Completion-gated.

**Aniq Fanlar — G9 Algebra (Full Boss, Review archetype):**
- 8 questions spanning all reviewed algebraic topics. Mid-boss checkpoint after question 4.
- Hard questions require proof construction or system design. Extended response only — no answer choice of any kind.

## Verification rules

1. **Format matches archetype:** `concept_intro` → `light_checkpoint` format, `algorithm/application` → `standard_boss`, `review` → `full_boss`. Test: assert `(archetype, boss_format)` pair in session payload.
2. **HP pool is correct:** HP value must match `00-core/hp-damage-baseline.md` for the grade band and subject. Test: cross-reference session HP with hp-damage-baseline.md lookup.
3. **No MC for G5+:** Phase 6 questions for grade band G5–11 must not use multiple-choice format (except G5 up to 30%). Test: count MC items per grade band; assert 0 for G6+.
4. **Inline tags on every question:** Every question must carry `[Bloom: LX | PISA: LX | Damage: -XX HP]`. Test: regex scan on all question_text fields.
5. **40/40/20 distribution:** Question set must contain 40% Easy, 40% Medium, 20% Hard (±1 question tolerance for small sets). Test: count difficulty_tier values in question set.
6. **Socratic hints present:** Every non-Light-Checkpoint question must carry 3 `socratic_hints`. Test: assert len(socratic_hints) == 3 per question.
7. **Failure language compliance:** Phase 6 failure messages must use *"Hali emas!"* and never *"Noto'g'ri"* or *"Xato"*. Test: string scan on all feedback strings.
8. **Pronoun compliance:** All Uzbek text must use "Siz". Zero "sen" occurrences. Test: regex scan.
9. **No skipping:** Phase 6 must be unbypassable in session flow (except Mythical Boss auto-trigger). Test: session orchestrator flow graph must not include an edge that skips Phase 6.
10. **Capture rule applied:** Questions meeting capture trigger conditions (see `00-core/capture-rule.md`) must have `capture_required: true` and a populated `scoring_rubric`. Test: validate capture_required field for multi-step calculation questions.

## Integration points

**Entry:**
- Session orchestrator calls `render_phase_6(archetype, boss_tier, grade_band, subject, pisa_level, chapter_id)` after confirming `phase_5_complete: true` (or `phase_5_skipped: true`).
- For Big Boss: orchestrator passes `weak_standards[]` (3 weakest standards from prior records).
- For Mythical Boss: session orchestrator injects surprise overlay before rendering Phase 6.
- HP pool fetched from `00-core/hp-damage-baseline.md` lookup.

**Exit:**
- On boss defeated or Light Checkpoint completed: session state records `phase_6_complete: true`, `boss_defeated`, `stars_earned`, `phase_score_pct`, `standards_mastered[]`, `standards_needs_work[]`, per-question data array, `remediation_flag`.
- These signals passed to session context store.
- Phase 7 Reflection is unlocked and auto-navigated to.

**Cross-references:**
- `00-core/hp-damage-baseline.md` — authoritative HP pools and damage values.
- `00-core/capture-rule.md` — governs when calculation step capture is triggered and scored.
- `00-core/routing-algorithm.md` — consumed by Phase 7 using `boss_defeated` and `phase_score_pct` signals.
- `00-core/skill-taxonomy.md` — skill_tags on per-question data (6 axes: creativity, problem-solving, critical-thinking, memory, application, translation).
- `00-core/pisa-framework.md` — PISA level calibration for question generation.
- `00-core/pronoun-policy.md` — student-facing language rules.
- `00-core/gamification-economy.md` — XP values for boss defeat, stars, Mythical Boss 5× multiplier.
- Phase 5 Consolidation (`phase-05-consolidation.md`) — entry dependency.
- Phase 7 Reflection (`phase-07-reflection.md`) — receives all Phase 6 output signals.
- Teacher dashboard — receives `standards_mastered[]`, `standards_needs_work[]`, star counts.

## UX/animation spec

**Layout:** Boss encounter screen. Three zones: (1) Boss avatar + HP bar at top; (2) Question card in center; (3) Answer input + hint button at bottom. Light Checkpoint removes HP bar zone entirely — plain question card layout.

**Boss avatar:** Illustrated character (grade-appropriate: creature/robot for G1–6, abstract entity/AI for G7–11). HP bar: animated health bar with color gradient (green → yellow → red as HP depletes). HP loss animation: screen flash (red tint overlay, 100ms fade) + HP bar segment break animation.

**Question card entrance:** Slide up from bottom (translateY 100% → 0%, 350ms ease-out). Question text fades in with the same staggered sentence entrance as Phase 0-A.

**Difficulty indicator:** Color-coded chip in top-right of question card: green = Easy, amber = Medium, red = Hard. Bloom level label below in 10px muted text.

**Combo streak display:** Counter badge at top-left. "3 correct → 2× damage" activated: badge pulses gold (scale 1→1.15→1, 300ms), counter glows. Next damage event shows "×2" floating text over HP bar.

**Hint button:** Bottom-right of question card. First tap shows Socratic hint 1 with HP penalty notification: *"–10 HP: Boss kuchaydi!"* (Boss recovered HP). Button re-tappable for hints 2 and 3.

**Correct answer celebration:** Confetti burst (200 particles, 1.5s) + damage number floats upward over boss avatar (e.g., "–20 HP!" in red bold). Boss avatar shakes on hit (translateX ±12px, 3 cycles, 200ms). If combo active, floating text shows "–40 HP! COMBO!"

**Boss defeated screen:** Full-screen celebration. Boss avatar crumbles/dissolves animation (1.5s). Stars appear one by one from center (scale 0→1.2→1, 200ms each, 300ms stagger). XP counter increments with rolling number animation. "Davom etish" button appears after 2 seconds.

**Failure screen:** Boss avatar looms larger (scale 1→1.15, 500ms ease-in). TEFCAS message appears: *"Hali emas! Miyangiz Feedback oldi."* Socratic tutoring dialogue box slides in from bottom. Re-attempt button after tutoring sequence completes.

**Light Checkpoint layout:** No boss avatar. Clean question card only. Hint appears as an inline expansion below the question (not a separate button) — softer visual treatment matching the lower-stakes format.

**Mythical Boss appearance:** Surprise overlay — screen darkens, boss silhouette materializes with particle effects (5× scale fade-in). Warning banner: *"⚠️ A Mythical Boss has appeared!"* No hint button rendered.

**Mid-boss checkpoint (Full Boss / Review):** Triggered at ~50% HP depletion. Animated pause: boss avatar freezes, performance summary card slides in (score so far, hints used, flagged questions). Student can tap flagged question to review the hint used. "Davom etish" dismisses checkpoint and resumes boss.
