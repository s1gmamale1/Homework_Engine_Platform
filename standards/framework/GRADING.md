# Grading by Section — How Each Phase Is Scored, With Examples

**Version:** 1.0  |  **Date:** 2026-04-27
**Companion to:** `AMR-GRADING-SYSTEM.md` v1.1 (the spec)
**Audience:** Teachers, content producers, agent builders, parents who want a concrete walkthrough

This document walks through every section of a NETS homework session in order and answers three questions for each:

1. **Is it graded?** — yes / no / partially
2. **How?** — the method (closed accuracy, 2-axis rubric, engagement-only, etc.)
3. **What does it look like?** — a worked example with a real student response, the AI's scoring, and the report-card line

For the formal rules (formulas, axis definitions, 3-pass median, escalation chains, mastery promotion windows), read `AMR-GRADING-SYSTEM.md`. This document is the "in practice" companion.

---

## How the 2-axis rubric works (read this before the open phases)

Sections 4, 5b, and 6 are graded with **the same 2-axis rubric**. The rubric is the engine; the only thing that varies between phases is what "the answer" looks like. Once you understand the rubric, every open-phase example below follows the same logic.

### The two axes

**Axis 1 — Concept Identification.** Did the student show they recognized which rule applies, before applying it?

**Axis 2 — Process Integrity.** Did the student show a valid logical chain that actually arrives at the answer?

Each axis is scored on a 4-level scale:

| Level | Label | Concept (Axis 1) | Process (Axis 2) |
|---|---|---|---|
| 4 | Mastered | Names the rule precisely AND links it to the problem's conditions ("…chunki ∠C = 90°") | ≥ 3 ordered steps, valid, justified, no gaps, clear final answer with units |
| 3 | Proficient | Names the rule precisely; trigger justification not stated | ≥ 3 ordered, valid steps; final answer present; justification implicit |
| 2 | Apprentice | Vague gesture ("geometriya qoidasi") without a specific name | 2 steps OR a missing intermediate step (gap) |
| 1 | Novice | No rule named at all | 0–1 steps, OR self-contradictory work |

### What the AI checks under the hood

The grader doesn't just "vibe-check" — it runs sub-criteria. These are the levers it actually uses to land on a level:

**Axis 1 sub-criteria:**
- A1.1 — Naming presence (did the student write the rule's name at all?)
- A1.2 — Naming timing (named *before* applying, not retroactively as a label?)
- A1.3 — Naming specificity ("Pifagor teoremasi", not "geometriya qoidasi")
- A1.4 — Trigger justification (linked the problem's conditions to the rule's preconditions?)

**Axis 2 sub-criteria:**
- A2.1 — Step count
- A2.2 — Step ordering (each step uses what the previous produced)
- A2.3 — Step validity (no math errors)
- A2.4 — Gap absence (no hidden jumps)
- A2.5 — Justification per step ("kvadrat ildiz olib", "qo'yib")
- A2.6 — No internal contradictions
- A2.7 — Final closure (clear answer with units)

### The score formula

```
axis_avg     = (axis_1_median + axis_2_median) / 2
item_score % = axis_avg × 25
```

Each rubric level is worth 25 percentage points. Lowest possible item score: 25%. Highest: 100%.

### Score grid — every possible median pair

| Axis 1 → / Axis 2 ↓ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 25 (Novice) | 38 (Apprentice) | 50 (Apprentice) | 63 (Proficient) |
| **2** | 38 (Apprentice) | 50 (Apprentice) | 63 (Proficient) | 75 (Proficient) |
| **3** | 50 (Apprentice) | 63 (Proficient) | 75 (Proficient) | 88 (Mastered) |
| **4** | 63 (Proficient) | 75 (Proficient) | 88 (Mastered) | 100 (Mastered) |

Note the symmetry: a (4, 1) student — perfect concept naming but no work shown — and a (1, 4) student — flawless work without naming the rule — both end at 63%. The rubric weights both axes equally because **knowing what to apply** and **applying it correctly** are both required for genuine understanding.

### Why two axes (not three)

An earlier draft included an Axis 3 — Self-Verification. It was rejected because:
- "Restating the answer" was indistinguishable from "doing nothing."
- "Estimates first" encoded one specific verification technique, penalizing students who verified another way.
- Self-verification is a metacognitive habit most G5–G7 students don't have yet — measuring its absence isn't fair.
- It produced the highest cross-pass disagreement (most subjective axis).

Self-Verification is permanently out. **Do not re-introduce it.**

### How the 3 passes + median + escalation work

Every open response is graded **three times in parallel** by the same Tier-2 LLM with identical input. Variance comes from LLM stochasticity, not from sending different prompts.

**Per-pass call:**
- Provider: Kimi (Moonshot) or Anthropic (Claude) — auto-detected from env
- Model: cheapest tier first (e.g. `moonshot-v1-8k`, `claude-haiku-4-5`)
- Temperature: 0.7
- Both axes scored in **one prompt per pass** (3 LLM calls per item, not 6)

**Aggregation:**
```
axis_1_median = median(passA.axis1, passB.axis1, passC.axis1)
axis_2_median = median(passA.axis2, passB.axis2, passC.axis2)
spread        = max(passes) − min(passes)   ∈ {0, 1, 2, 3}
confidence    = max(0, 100 − a1_spread × 20 − a2_spread × 20)
```

**What the spread means:**

| Spread | Meaning | Grade ships? | Teacher flag? | Counts toward mastery? |
|---|---|---|---|---|
| 0 | All 3 passes identical | ✅ confident | ❌ none | ✅ yes |
| 1 | One pass off by one (normal LLM noise) | ✅ confident | ❌ none | ✅ yes |
| 2 | Significant disagreement | ✅ provisional | ⚠️ medium | ✅ yes (provisional) |
| 3 | Maximum disagreement | ✅ provisional + low-confidence tag | 🚨 high priority | ⏸ paused until teacher reviews |

**Cost-aware escalation.** If `confidence < 80%`, escalate to the next-tier model and re-run 3 passes. Repeat until confidence clears 80% or the chain is exhausted.

```
Kimi:      moonshot-v1-8k → moonshot-v1-32k → moonshot-v1-128k → kimi-k2-0711-preview
Anthropic: claude-haiku-4-5 → claude-sonnet-4-6 → claude-opus-4-6 → claude-opus-4-7
```

If even the strongest tier doesn't clear 80%, the strongest tier's grade ships (the student is never blocked) and the item is flagged for high-priority teacher review.

### Worked walkthrough — same student response, all 3 passes traced

**Prompt (G8 Real-Life):**
> "Sevara is laying a 12 m × 5 m garden bed and wants a diagonal walking path corner-to-corner. How long is the path? Show your reasoning."

**Student response:**
> "Bu to'g'ri to'rtburchak, demak diagonal Pifagor teoremasi bilan topiladi (chunki uchburchak to'g'ri burchakli). d² = 12² + 5² = 144 + 25 = 169. d = √169 = 13 m."

**Pass 1 (kimi moonshot-v1-8k, T=0.7):**

| Axis | Level | Sub-criteria the AI fired |
|---|---|---|
| A1 | 4 | A1.1 ✓ ("Pifagor teoremasi"), A1.2 ✓ (named before applying), A1.3 ✓ (specific), A1.4 ✓ ("chunki uchburchak to'g'ri burchakli") |
| A2 | 4 | A2.1 = 3 steps, A2.2 ✓ ordered, A2.3 ✓ valid, A2.4 ✓ no gaps, A2.5 ✓ implicit but clean, A2.7 ✓ ("13 m") |

**Pass 2 (same model, same input):**

| Axis | Level | Notes |
|---|---|---|
| A1 | 4 | Same calls as Pass 1 |
| A2 | 3 | This pass flagged A2.5 as missing — student didn't write "kvadrat ildiz olib" explicitly, only the symbol |

**Pass 3 (same model, same input):**

| Axis | Level |
|---|---|
| A1 | 4 |
| A2 | 4 |

**Aggregation:**
- `axis_1_median = median(4, 4, 4) = 4`
- `axis_2_median = median(4, 3, 4) = 4`
- `axis_1_spread = 0`, `axis_2_spread = 1`
- `confidence = 100 − 0×20 − 1×20 = 80%` ✓ ships at first tier
- `item_score = ((4 + 4) / 2) × 25 = 100%` — Mastered

**What lands on the report card:**
```
Real-Life item       100%  (A1=4 · A2=4)  Mastered ★
                     Confidence 80% · 1 pass disagreed by one level on Axis 2 (normal LLM noise)
```

### What changes axis-by-axis as student responses get weaker

Hold the prompt constant, vary the response, watch each axis move:

| Student response | A1 | A2 | Score | Why |
|---|---|---|---|---|
| Names rule + cites trigger + 3 valid steps with units | **4** | **4** | 100% | Both axes hit Mastered |
| Names rule + 3 valid steps, no trigger justification | **3** | **4** | 88% | A1.4 missing — rule named but not justified by problem conditions |
| Names rule, 2 steps with a gap (square root elided) | **3** | **2** | 63% | Process axis takes the hit; concept axis fine |
| "12² + 5² = 169. 13." | **1** | **2** | 38% | No rule named; steps present but compressed/incomplete |
| "13" | **1** | **1** | 25% | Result-only — no concept, no process; floor of the rubric |

Notice: **the right numerical answer alone earns 25%.** That's the AMR's whole reason for existing — *reasoning over results.* A student who plugs the answer in without showing why bottoms out the rubric, regardless of correctness.

### How to read the per-phase examples below

For Phase 4, 5b, and 6, every worked example uses the same machinery:

1. Student writes a response.
2. The same prompt goes to the grader 3× in parallel.
3. Per-axis median is taken (not per-pass average — the median is robust to one-off outliers).
4. `((a1 + a2) / 2) × 25` is the item score.
5. Phase score = mean of all items in that phase.

The phase-specific examples below show how the **content** of "the right answer" changes (a Real-Life problem vs. a Boss problem vs. a Consolidation comparison), but the rubric never changes.

---

## At-a-glance table

| # | Section | Graded? | Method | Feeds session score? |
|---|---|---|---|---|
| 0-A | Theme Preview | ❌ | Engagement only | No |
| 0-B | Flash Cards | ❌ | Exposure only | No |
| 1 | Memory Sprint | ✅ | Closed accuracy | Yes |
| 2 | Story Mode | ✅ light | Pass/fail per checkpoint | Yes |
| 3 | Game Breaks | ✅ | Closed accuracy per game, mean across games | Yes |
| 4 | Real-Life Challenge | ✅ | 2-axis rubric × 3-pass median | Yes |
| 5 | Consolidation | ✅ conditional | Reminders ungraded; 2–3 open items rubric-graded | Yes (if present) |
| 6 | Final Boss | ✅ | 2-axis rubric per item; HP overlay separate | Yes |
| 7 | Reflection | ❌ | Participation only | No |

---

## Section 0-A — Theme Preview (Pre-Session)

**Graded?** No.
**Method:** Engagement signals only — `time_on_phase`, `scroll_depth`, `clicked_through`.
**Why not graded:** This section is the hook. It exists to spark curiosity ("you'll learn how circle-secants make hidden angles visible"). Grading it would replace curiosity with anxiety.

**What gets recorded:**
```json
{ "phase": "0-A", "time_on_phase_s": 47, "scroll_depth": 0.92, "completed": true }
```

**What the student sees:**
> No score. A small "✓ Theme previewed" tick at the top of the dashboard, nothing more.

**What the teacher sees:**
> Aggregate engagement only — "28 of 32 students previewed the theme. Median dwell: 45s." Used for content-quality QA, not student grading.

---

## Section 0-B — Flash Cards (Pre-Session)

**Graded?** No.
**Method:** Exposure only — `cards_seen`, `cards_flipped`, `cards_kept_open ≥ 3s`.
**Why not graded:** Flashcards are pre-loading vocabulary into working memory. Testing recognition before the lesson would punish students for not yet knowing things they're about to learn.

**What gets recorded:**
```json
{ "phase": "0-B", "cards_seen": 10, "cards_flipped": 8, "deep_views": 6 }
```

**Example:**
- Card front: "Aylananing kesuvchisi"
- Card back: "Aylanani ikki nuqtada kesib o'tuvchi to'g'ri chiziq"

The student flips 8 of 10 cards, dwells on 6 for ≥ 3 seconds. **No score is computed.** A "✓ Flash cards seen" tick appears.

**Edge case — fast-clicker abuse.** If a student opens and closes 10 cards in under 5 seconds total, the section logs `engagement_quality: "low"` but still doesn't grade. The teacher dashboard surfaces low-engagement patterns; the grade is unaffected.

---

## Section 1 — Memory Sprint

**Graded?** Yes — closed accuracy.
**Method:** `accuracy = correct / attempted`. Skips count as wrong. Hints allowed (recorded as metadata, not penalized).
**Why graded this way:** Memory Sprint is recall practice on the lesson's named entities — closed by design, with one right answer per item.

**Recorded shape:**
```json
{ "phase": "1", "skill_id": "UZ-MATH-8-AYL-kesuvchi", "correct": 5, "attempted": 6, "accuracy": 83.3, "hints_used": 1 }
```

### Worked example

**Item 1.** "Aylanani ikki nuqtada kesib o'tuvchi to'g'ri chiziq qanday ataladi?"
- Student answer: **kesuvchi** ✓ (correct, no hint)

**Item 2.** "Urinma chiziq aylanani nechta nuqtada kesib o'tadi?"
- Student answer: **bitta** ✓ (correct, used hint)

**Item 3.** "Aylanaga ichki chizilgan burchak nima?"
- Student answer: **markaziy burchak** ✗ (wrong)

**Item 4.** "Pifagor teoremasi qaysi uchburchakda qo'llaniladi?"
- Student skipped. ✗ (counts as wrong)

**Item 5–6.** Both correct. ✓ ✓

**Phase score:** `4 / 6 = 66.7%` — Proficient band.

**Report card line:**
```
Phase 1  Memory Sprint   4/6 (67%)  Proficient ↗
```

**Why this is fair:** Hints don't hide a wrong answer (they help the student think); skipping doesn't gain a "neutral" outcome that students could exploit to dodge weak topics.

---

## Section 2 — Story Mode

**Graded?** Yes — light. Pass/fail per checkpoint, first-try accuracy.
**Method:** Each Story checkpoint asks one closed comprehension question. Score = `passed_checkpoints / total_checkpoints`.
**Why "light":** Story is primarily a narrative carrier; the questions are sanity checks that the student is following, not high-stakes assessment.

**Recorded shape:**
```json
{ "phase": "2", "checkpoints_total": 4, "checkpoints_passed": 3, "first_try_passes": 3, "accuracy": 75.0 }
```

### Worked example

**Story:** Sevara is mapping a circular pond in her grandfather's garden. She walks along a straight path that crosses the pond's edge twice — that's a **kesuvchi** (secant). The path's two intersection points define a chord she can measure with a string.

**Checkpoint 1 (after p.1).** "What kind of line did Sevara walk along?"
- Options: tangent / **secant** / chord
- Student picks **secant.** ✓

**Checkpoint 2 (after p.2).** "How many points does her path share with the pond's circle?"
- Student answers **2.** ✓

**Checkpoint 3 (after p.3).** "If Sevara had walked tangent to the pond, how many points would the path touch?"
- Student answers **2.** ✗ (wrong; it's 1)

**Checkpoint 4 (after p.4).** "Which segment is the chord?"
- Student picks correct segment. ✓

**Phase score:** `3 / 4 = 75%` — Proficient band.

**Report card line:**
```
Phase 2  Story Mode      3/4 (75%)  Proficient
```

**What's NOT graded in Story Mode:** Reading speed, voice-narration usage, animation interaction. Those are engagement signals.

---

## Section 3 — Game Breaks

**Graded?** Yes.
**Method:** Each game has its own closed accuracy (`correct / attempted`). The phase score is the **mean** across the 3 games played.
**Why graded:** Game Breaks are the lesson's main retrieval practice — that's where the actual learning is being tested under low-stakes conditions.

### What's NOT used

- **No Bloom or PISA multipliers.** A Bloom L4 question is worth one point, same as Bloom L2. Difficulty enters via adaptive routing (which questions you face), not score weight.
- **No game-type weight.** Adaptive Quiz games and Sentence Fill games count equally.

### Worked example

A G8 session with three Game Break games:

**Game A — Adaptive Quiz** (5 items)
| Item | Student | Correct? |
|---|---|---|
| Q1: "Ichki burchak teoremasini ifodalang." | "(yoy_1 + yoy_2) / 2" | ✓ |
| Q2: "Tashqi nuqtadan chiqqan ikki kesuvchi orasidagi burchak…" | (Wrong formula) | ✗ |
| Q3: "Aylanaga urinma chiziq…" | "1 nuqtada tegadi" | ✓ |
| Q4: Multi-step computation | "55°" | ✓ |
| Q5: "Ichki yoki tashqi burchak?" | "ichki" | ✓ |

**Game A score:** `4/5 = 80%`

**Game B — Sentence Fill** (5 items)
- 4 correct, 1 wrong → `4/5 = 80%`

**Game C — Mystery Box** (3 items)
- 2 correct, 1 wrong → `2/3 = 67%`

**Phase 3 score (mean of games):** `(80 + 80 + 67) / 3 = 75.7%` — Proficient band.

**Report card line:**
```
Phase 3  Game Breaks     76% (Adaptive 80 · Fill 80 · Mystery 67)  Proficient ↗
```

**Edge case — game abandoned mid-play.** If a student starts Game C and quits after 1 of 3 items:
- Played item is graded. Unplayed items are excluded.
- Game C score = `correct / attempted_items_only`, not `correct / total_designed`.
- Default for "mid-game abandonment" is open question — see `AMR-GRADING-SYSTEM.md` §12.

---

## Section 4 — Real-Life Challenge

**Graded?** Yes — 2-axis rubric × 3-pass median.
**Method:** The student writes an open response. Sent to a Tier-2 LLM grader **three times in parallel**. Each pass returns Axis 1 (Concept Identification) and Axis 2 (Process Integrity) on a 4-level scale. Per-axis median is taken; `item_score = ((a1 + a2) / 2) × 25`.
**Why this method:** Real-Life problems require the student to identify which rule applies and walk through the reasoning. There's no single right surface form, so closed scoring doesn't work — but reasoning quality is judgeable against anchored exemplars.

### Worked example

**Prompt:**
> Sevara is laying a 12 m × 5 m rectangular garden bed and wants to run a diagonal walking path corner-to-corner. How long is the path? Show your reasoning.

**Student response:**
> "Bu to'g'ri to'rtburchak, demak diagonal Pifagor teoremasi bilan topiladi (chunki uchburchak to'g'ri burchakli). d² = 12² + 5² = 144 + 25 = 169. d = √169 = 13 m."

### Pass 1 (Kimi moonshot-v1-8k, T=0.7)
```json
{
  "axis_1_concept": 4,
  "axis_1_reason": "Names Pifagor teoremasi explicitly, ties it to the right-angle condition.",
  "axis_2_process": 4,
  "axis_2_reason": "Three steps: setup → substitute → solve. No gaps, final answer with units."
}
```

### Pass 2 (Kimi moonshot-v1-8k, T=0.7)
```json
{ "axis_1_concept": 4, "axis_2_process": 3, "axis_2_reason": "Steps clear but justification implicit (no 'kvadrat ildiz olib' label)." }
```

### Pass 3 (Kimi moonshot-v1-8k, T=0.7)
```json
{ "axis_1_concept": 4, "axis_2_process": 4 }
```

### Aggregation
- `axis_1_median = median(4, 4, 4) = 4`
- `axis_2_median = median(4, 3, 4) = 4`
- `axis_1_spread = 0`, `axis_2_spread = 1`
- `confidence = 100 − 0×20 − 1×20 = 80%` ✓ ships
- `item_score = ((4 + 4) / 2) × 25 = 100%` — Mastered band

**Report card line:**
```
Phase 4  Real-Life      100% (A1=4 · A2=4)  Mastered ★
                        Confidence 80% · 1 pass disagreed by one level (normal)
```

### Counter-example — same problem, weaker response

**Student response:**
> "12² + 5² = 169. 13."

### Pass 1
```json
{ "axis_1_concept": 1, "axis_1_reason": "No rule named at all.",
  "axis_2_process": 2, "axis_2_reason": "Two steps shown but the square-root step is elided." }
```

### Pass 2
```json
{ "axis_1_concept": 1, "axis_2_process": 2 }
```

### Pass 3
```json
{ "axis_1_concept": 2, "axis_1_reason": "Implies a rule via formula structure but never names it.",
  "axis_2_process": 2 }
```

- Median: A1 = 1, A2 = 2 → `((1 + 2) / 2) × 25 = 37.5%` — Apprentice band, low end.

**Report card line:**
```
Phase 4  Real-Life      38% (A1=1 · A2=2)  Apprentice
                        Tip: name the rule before applying it.
```

The student got the right number. They didn't show the **reasoning that earns the grade** — and the AMR explicitly says: *reasoning over results.*

### When the 3 passes disagree badly

If `confidence < 80%`, the runtime escalates to the next-tier model (e.g. `moonshot-v1-32k`) and re-runs 3 passes. If the strongest tier still doesn't clear 80%, the strongest tier's grade is used and the item is **flagged for teacher review** at the corresponding severity (medium for spread=2, high for spread=3). The student is never blocked while waiting.

---

## Section 5 — Consolidation

**Graded?** Conditionally.
**Method:** Phase 5 has two sub-parts:
- **5a — Reminders / micro-recap.** Ungraded. Pure exposure (notes the student rereads).
- **5b — 2–3 open consolidation questions.** Each rubric-graded with the **same 2-axis rubric × 3-pass median** as Phase 4.

**Why conditional:** If the lesson covers a single concept, Phase 5 is **skipped entirely** (the engine sets `consolidation: { skipped: true }` in the homework data). A single-concept lesson doesn't need consolidation across topics.

**When skipped:** Phase 5 contributes nothing to the session average. Mean is taken over phases 1, 2, 3, 4, 6 only.

### Worked example — multi-concept lesson (NOT skipped)

The lesson covered both **inscribed angle** and **secant–secant external angle**. Phase 5b asks the student to compare them:

**Question 5b.1.** "An inscribed angle and an external secant–secant angle both intercept the same arc pair. Which is bigger and why?"

**Student response:**
> "Ichki burchak yarim yoyga teng (yoy_1 / 2). Tashqi burchak (yoy_1 − yoy_2) / 2 — ya'ni ikkala yoyning farqining yarmi. Tashqi burchak kichikroq, chunki ayrim yoy chegirib olinadi."

- 3-pass median: A1 = 4, A2 = 3
- Item score: `((4 + 3) / 2) × 25 = 87.5%` — Mastered band

**Question 5b.2.** A second comparison item, scored 75%.

**Phase 5 score (mean of 5b items):** `(87.5 + 75) / 2 = 81.25%` — Proficient band.

**Report card line:**
```
Phase 5  Consolidation   81% (item1=88 · item2=75)  Proficient ↗
```

### Worked example — single-concept lesson (SKIPPED)

The lesson covered only the inscribed angle theorem. The homework producer marks `consolidation: { skipped: true }`.

**Student experience:** Phase 5 doesn't appear in the UI. The session jumps from Phase 4 to Phase 6.

**Report card:** Phase 5 line is omitted. Session average computed over remaining phases.

---

## Section 6 — Final Boss

**Graded?** Yes.
**Method:** Pure 2-axis rubric grading per item (same as Phase 4). **No multiple-choice items at any grade.** Phase score = mean across items. The Boss HP overlay is **separate** from the academic score.
**Why no MC:** Final Boss is the session's apex challenge. MCQ allows guessing to land hits, which would inflate the gamification narrative without reflecting actual mastery. Open responses force the student to demonstrate reasoning.

### Item count distribution (40 / 40 / 20)

| Total items | Easy | Medium | Hard | Max HP damage if all pass |
|---|---|---|---|---|
| 5 | 2 | 2 | 1 | 90 |
| 6 | 2 | 3 | 1 | 110 |
| 7 | 3 | 3 | 1 | 120 |

For G7–G9, Boss HP = 100. With 5 items the Boss survives even on a perfect session — that's intentional (they need 6+ items, or a hit on a Hard item, to defeat). For G9–G11, HP = 150 makes Boss harder to defeat.

### Worked example — G8 Boss, 6 items, HP = 100

**Item B1** (Easy). Student response → A1=4, A2=3 → item_score=88% ≥ 60% → **−10 HP** (Easy full damage). HP: 90.

**Item B2** (Easy). A1=2, A2=3 → 63% ≥ 60% → **−10 HP**. HP: 80.

**Item B3** (Medium). A1=3, A2=4 → 88% ≥ 60% → **−20 HP**. HP: 60.

**Item B4** (Medium). A1=2, A2=2 → 50% < 60% → **0 damage**. HP: 60.

**Item B5** (Medium). A1=4, A2=4 → 100% ≥ 60% → **−20 HP**. HP: 40.

**Item B6** (Hard). A1=3, A2=4 → 88% ≥ 60% → **−30 HP**. HP: **10**. Boss survives.

**Phase 6 score (academic):** `mean(88, 63, 88, 50, 100, 88) = 79.5%` — Proficient band.

**Boss outcome:** `not_defeated` (HP 10 remaining). Student gets the academic credit, but the gamification narrative shows "Boss survived — try again next session."

**Report card line:**
```
Phase 6  Final Boss     80% (6 items)  Proficient
                        Boss: Survived (10 HP left). Hard item earned the biggest hit.
```

### Counter-example — same Boss, but the Hard item missed

If item B6 (Hard) had scored 50%:
- Damage on B6: 0 → HP stays at 40.
- Phase score: `mean(88, 63, 88, 50, 100, 50) = 73.2%` — still Proficient.
- Boss outcome: `not_defeated`, HP=40. Larger gap to closing the narrative.

A student can score 88% on Phase 6 and still survive the Boss (if a Hard miss landed there); or score 73% and defeat it (if they'd have hit ≥ 60% on the Hard one). **Academic score and Boss outcome are separate signals**, recorded independently.

---

## Section 7 — Reflection

**Graded?** No.
**Method:** Participation only — `completed: true | false`, plus extracted tags (e.g. `["learned-something", "felt-stuck-on-X"]`) for teacher dashboards.
**Why not graded:** Reflection asks the student to be honest about what they didn't understand. Grading honesty would replace truthful self-report with strategic self-report.

**Recorded shape:**
```json
{ "phase": "7", "completed": true, "duration_s": 73,
  "tags_extracted": ["confused-about-tashqi-burchak", "liked-the-garden-story"] }
```

**Report card line:**
```
Phase 7  Reflection      ✓ Completed (73s)
                         "I'm still mixing up internal vs external angles."
```

**What the teacher sees:** Aggregate confusion clusters per cohort — "8 of 32 students flagged confusion on tashqi-burchak." Drives next-session content decisions, not student grades.

---

## How the session score is computed

```
session_score = mean of all SCORED phase scores
              = mean(phase_1, phase_2, phase_3, phase_4, phase_5_if_present, phase_6)
```

**Excluded from the mean:** 0-A, 0-B, 5 (if `skipped: true`), 7. Those contribute engagement signals only.

### Worked example — full session, Phase 5 present

| Phase | Score | Included? |
|---|---|---|
| 0-A | n/a | No |
| 0-B | n/a | No |
| 1 | 67% | ✓ |
| 2 | 75% | ✓ |
| 3 | 76% | ✓ |
| 4 | 100% | ✓ |
| 5 | 81% | ✓ |
| 6 | 80% | ✓ |
| 7 | n/a | No |

**Session score:** `(67 + 75 + 76 + 100 + 81 + 80) / 6 = 79.8%` — Proficient band.

**Uzbek 10-point label:** **8 — Juda yaxshi.**

---

## Mastery promotion — the rolling window

A skill graduates from one band to the next only after **sustained** performance. One great session doesn't promote; one bad session doesn't demote.

| Transition | Rule |
|---|---|
| Novice → Apprentice | 2 consecutive sessions ≥ 40% on the skill |
| Apprentice → Proficient | **3 consecutive sessions ≥ 70%** |
| Proficient → Mastered | **3 consecutive sessions ≥ 85%** AND learning velocity n ≥ 0.1 |
| Demotion (any band) | 2 consecutive sessions below current band's floor |

### Worked example

A student's 5 most recent sessions on `UZ-MATH-8-AYL-kesuvchi`:
| Session | Skill score | Band-floor check |
|---|---|---|
| S1 | 62% | (Apprentice → Proficient floor: 70%) — does NOT count |
| S2 | 73% | counts toward streak (1) |
| S3 | 76% | counts toward streak (2) |
| S4 | 71% | counts toward streak (3) → **promote to Proficient** |
| S5 | 65% | (now in Proficient — does S5 demote?) |

Demotion rule: 2 consecutive sessions below current floor. S5 alone is below 70% but only one session — student stays Proficient until/unless a second sub-70% session lands. This is the anti-noise property.

---

## Reference: phase aggregation cheat-sheet

```
PHASE 1 (Memory Sprint)
  score = correct / attempted

PHASE 2 (Story Mode)
  score = checkpoints_passed / checkpoints_total

PHASE 3 (Game Breaks)
  score = mean(game_1_acc, game_2_acc, game_3_acc)
  where each game_acc = correct / attempted

PHASE 4 (Real-Life Challenge)
  rubric: 2-axis × 4-level × 3-pass median
  score = ((a1_median + a2_median) / 2) × 25

PHASE 5 (Consolidation)
  score = mean(item_1, item_2, ...) using same 2-axis rubric
  IF skipped → excluded from session mean

PHASE 6 (Final Boss)
  score = mean(item_1, item_2, ...) using same 2-axis rubric
  HP overlay: separate signal (item ≥ 60% = full damage by difficulty)

SESSION
  score = mean of all SCORED phase scores
```

---

## What's deliberately NOT graded — recap

| Section | Why not |
|---|---|
| 0-A Theme Preview | Curiosity hook — grading kills curiosity |
| 0-B Flash Cards | Pre-loading vocabulary — testing recognition before learning is unfair |
| 5a Reminders (within Phase 5) | Pure recap exposure |
| 5 entirely (when single-concept lesson) | Producer flag `consolidation: { skipped: true }` |
| 7 Reflection | Metacognition — grading kills honesty |

These are policy, not implementation laziness. **Do not grade them.**

---

*GRADING-BY-SECTION v1.0 — companion to `AMR-GRADING-SYSTEM.md`. The spec defines the rules; this document shows what they look like in a real session.*
