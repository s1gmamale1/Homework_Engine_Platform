# NETS Game Mechanics — Universal Definitions v1.0

**Date:** 2026-04-11
**Scope:** 7 of 28 mechanics — Memory Palace, Story Mode, Adaptive Quiz, Mystery Box, Memory Match Blitz, Reaction Chain, Word Ladder Climb
**Status:** Skeleton / first-pass definitions. PISA/Bloom/cost/time fields are best-guess proposals for review.

## Sources

- `NETS-Game-Mechanics-Research-Answers.md` (2026-04-08) — research-backed design answers per mechanic (primary source)
- `NETS-Homework-Engine-UNIFIED.md` v2.0 — Section 6 mechanic catalog, dual-catalog rule, PISA tagging system
- `NETS-Game-Catalog-Summary.md` — quick-reference catalog
- `Researches/qwen-grade5-psychology-findings.md` — G5 psychology baseline
- Design merge decisions from conversation 2026-04-11 (see below)

## Merge Decisions Applied

These 4 design decisions were layered onto the research doc's base answers:

1. **Adaptive Quiz round length** → pure fixed (no early termination). Predictability > measurement precision for homework.
2. **Memory Match Blitz wrong-confirmation** → 3-second correct-answer flash is mandatory. Implementation must not re-hide instantly.
3. **Reaction Chain custom visuals** → custom process-diagram visuals only for top-20 chains by usage after 6 months of production data. Everything else uses default linear visual.
4. **Word Ladder Climb rung count** → capped at 5-6 rungs max. Each rung is 2 interactions so longer ladders drag.

---

## The 15-Field Template

Every mechanic definition in this document includes these 15 fields:

1. **Summary** — one-line description
2. **Core loop** — what the student does step-by-step in one round
3. **Grade-band design variations** — how the mechanic adapts across K-11
4. **Content author input** — what the content team provides per instance
5. **Evaluation & retry rules** — correct/partial/wrong, retry behavior, failure framing
6. **PISA coverage** — levels (1-6), domains, processes this mechanic can assess
7. **Bloom's band** — primary cognitive level(s)
8. **Transition skill types** — which PISA transitions this mechanic can scaffold
9. **Grade eligibility** — K-G11 with rationale for any exclusions
10. **Subject eligibility & `framework_bans`** — which subjects, which frameworks explicitly ban it, why
11. **Anti-cheat surface** — what Tier 2 watches for
12. **Telemetry events** — what gets logged for teacher dashboard + mastery map
13. **Cost profile** — Tier 1 / Tier 2 / Tier 3 touches per round
14. **Device requirements** — minimum spec, bandwidth, special hardware
15. **Session-time allocation** — minutes per round by grade band

---

# 1. Memory Palace (Default #5)

## 1.1 Summary
Student places 3-15 concepts (grade-dependent) at distinct locations in a culturally familiar 2.5D scene, then retrieves them via free recall and temporal-order prompts. Palace persists across sessions via SM-2 spaced repetition. One palace per topic to prevent cross-topic interference.

## 1.2 Core loop
1. Student picks a palace location from a pool: Registan Square, Chorsu Bazaar, hovli (courtyard home), school layout, own classroom. Rural fallback: "your home" generic layout.
2. System presents N concepts from current lesson (N varies by grade — see 1.3).
3. For each concept, student taps a hotspot on the palace image.
4. Student selects from 2-3 pre-designed visual images representing the concept, then drags the chosen image to lock it in the hotspot.
5. Guided walkthrough: system animates a walk through all placed hotspots, reinforcing placements.
6. **Free-recall test (primary):** "Walk through your palace and tell me everything you placed." Student records spoken or typed response.
7. **Temporal-order test (secondary):** "Which concept was at hotspot 3?" 2-3 probe questions.
8. Palace saves to student's personal collection. SM-2 spaced repetition schedules revisits over following weeks.

## 1.3 Grade-band design variations

| Grade band | Age | Loci | Interaction model | Primary recall format |
|---|---|---|---|---|
| K-G2 | 5-8 | 3 | Pre-placed by system, student walks through as guided narration | Point-to-location MC |
| G3-4 | 8-10 | 5 | Tap hotspot → system offers 2 images → student picks → auto-locks | Free recall with prompts + point-to-location |
| G5-6 | 10-12 | 5-7 | Full: tap → pick from 3 images → drag to lock | Free recall primary + temporal order |
| G7-9 | 12-15 | 7-10 | Full + student can add own text/voice annotation per hotspot | Free recall + temporal order + annotation retrieval |
| G10-11 | 15-17 | 10-15 | Self-built palaces (student can submit own location layouts) | Free recall + self-explanation |

## 1.4 Content author input
- N concepts from lesson (short label + 1-sentence definition)
- 2-3 authored visual image candidates per concept
- Palace background images (isometric/2.5D scenes) from the location pool
- Hotspot coordinates per palace background
- Walkthrough narration script (text + optional voice)

## 1.5 Evaluation & retry rules
- **Placement phase:** no scoring — formative.
- **Free recall:** Tier 2 compares student's response against concept list using semantic matching. Partial credit per concept recalled. Missing concepts framed as **"Hali emas"** (not yet) — never "failed."
- **Temporal order:** binary correct/wrong per probe.
- **Retry:** student may re-walk the palace once before the recall test. No retry budget on recall itself — missing concepts flow into next session's Memory Sprint (Phase 1) as spaced-repetition items.
- **Persistence:** palace saves to student profile. Revisit schedule follows SM-2: day 1 → day 3 → day 7 → day 14 → day 30.

## 1.6 PISA coverage
- **Levels:** L1-L3 primarily (factual recall, conceptual organization). L4 when temporal-order probes assess causal chain understanding.
- **Domains:** All (Math, Reading, Science, Creative Thinking) — mechanic is content-agnostic.
- **Processes:** "Represent information spatially," "Retrieve from long-term memory," "Organize concepts into structure."

## 1.7 Bloom's band
Primary: **Remember, Understand.**
Secondary: Apply (when palace is reused for problem-solving in later sessions).

## 1.8 Transition skill types this mechanic can scaffold
- L1→L2: "Organize disparate facts into a coherent structure"
- L2→L3: "Retrieve and apply prior learning to current context"
- L3→L4: "Connect spatial/temporal relationships between concepts"

## 1.9 Grade eligibility
**K-G11.** Universal. K-G2 uses pre-placed guided walks (no independent placement). Full independent use from G3 onward.

## 1.10 Subject eligibility & `framework_bans`
Eligible: all subjects. No frameworks currently ban this mechanic.
`framework_bans: []`

## 1.11 Anti-cheat surface
- Tier 2 watches for: identical free-recall transcripts across students (copy-paste), placement time below a floor (<5s per placement = clicking through), clipboard paste into free-recall input.
- Signal level: SOFT_WARNING if anomalies detected; TEACHER_ALERT if repeated across sessions.

## 1.12 Telemetry events
- `mp_palace_selected` (location_id)
- `mp_placement_completed` (concept_id, hotspot_id, time_ms)
- `mp_free_recall_score` (concepts_recalled / total)
- `mp_temporal_probe_result` (probe_id, correct)
- `mp_palace_revisit` (palace_id, days_since_last, sm2_interval)

## 1.13 Cost profile
- **Tier 1:** placement UI, hotspot coordinate matching, SM-2 schedule calculation, image asset serving
- **Tier 2:** free-recall text evaluation (semantic comparison to concept list)
- **Tier 3:** none
- **Est. per-round cost:** <$0.001

## 1.14 Device requirements
- **Min:** mid-tier Android (2GB RAM), 1024×768 screen resolution
- **Bandwidth:** ~500KB one-time image load per palace, minimal after
- **Special hardware:** microphone optional (for spoken free recall); text input fallback always available

## 1.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 3-4 min |
| G3-4 | 4-5 min |
| G5-6 | 5-7 min |
| G7-9 | 6-8 min |
| G10-11 | 7-10 min |

---

# 2. Story Mode (Default #6 / Phase 2 driver)

## 2.1 Summary
Textbook content delivered as a linear narrative with human-authored master stories and AI-personalized variants. Segments are 30-150 seconds (grade-dependent) with mixed MC + short-answer comprehension gates between segments.

**Note:** Story Mode is also the universal Phase 2 driver of every session. When selected as a Phase 3 game, it appears as a shorter "story snippet puzzle" variant. The primary definition below is for the Phase 2 use.

## 2.2 Core loop
1. Student sees segment title + illustration.
2. Segment content plays as text. TTS toggle available as optional accommodation for struggling readers.
3. At 2-3 points within the story, student makes a **micro-choice** that changes *how* the next segment is framed — same content, different presentation (farmer's POV vs. scientist's POV, etc.). Not full branching.
4. Between segments: **comprehension gate** — 2 MC items (distractors derived from textbook misconceptions, not random) + 1 short-answer (1-2 sentences, keyword-matched + semantic fallback).
5. Gate score ≥ 70% → proceed. Gate score < 70% → remediation branch: simplified recap + retry on failed items. Max 2 gate retries.
6. After 2 failed gates: "Hali emas" framing, advance anyway but flag for teacher.
7. Story ends with 4-beat arc closure: Problem → Struggle → Discovery → Solution.
8. **Stranger Test mandatory:** a newcomer student with no prior context must be able to follow the story.

## 2.3 Grade-band design variations

| Grade band | Segment length | Checkpoints | Narrative structure | Gate format |
|---|---|---|---|---|
| K-G2 | 30-45s | 2-3 | Preoperational: single protagonist, simple cause-effect, heavy illustration | 2 MC only (typing too slow) |
| G3-4 | 45-75s | 3-4 | Concrete operational: linear with problem-solution arc | 2 MC + optional voice answer |
| G5-6 | 60-90s | 4-5 | Concrete operational, mild complexity, concrete metaphors | 2 MC + 1 short-answer |
| G7-9 | 90-120s | 5-6 | Early formal: multi-perspective, thematic, mild moral ambiguity | 2 MC + 2 short-answer |
| G10-11 | 120-150s | 6-7 | Formal: layered, abstract reasoning, hypothetical scenarios | 1 MC + 2 short-answer + 1 open essay |

## 2.4 Content author input
- **Human-authored master narrative** per chapter (4-beat arc, pedagogically aligned)
- 2-3 micro-choice branch variant texts (same story beats, different framing)
- Illustrations per segment (art assets)
- Comprehension gate item bank: MC items with misconception-based distractors + short-answer items with keyword rubric + semantic match threshold
- Remediation branch content for each checkpoint

## 2.5 Evaluation & retry rules
- **MC:** immediate feedback per item. Item pool rotates — same item not re-served in the same round.
- **Short-answer:** Tier 2 keyword matching with semantic similarity fallback. Three-tier scoring (full / partial / miss).
- **Gate threshold:** 70% to advance. Below → remediation branch → retry gate (max 2 attempts).
- **After 2 failed gate attempts:** advance anyway with "Hali emas" framing. Teacher dashboard is flagged.
- **TTS:** optional toggle. Synthesized Uzbek TTS deferred until quality benchmarks met. Human pre-recorded narration remains a future enhancement (not launch requirement).

## 2.6 PISA coverage
- **Levels:** L1-L5 (L1 basic recall, L2-3 integration, L4 inference, L5 multi-perspective evaluation in G7+).
- **Domains:** Reading (primary), subject content (secondary).
- **Processes:** "Locate information," "Interpret and integrate," "Reflect and evaluate."

## 2.7 Bloom's band
Primary: **Understand.**
Secondary: **Analyze** (at multi-perspective choice points in G7+).

## 2.8 Transition skill types
- L1→L2: "Extract key information from continuous text"
- L2→L3: "Integrate information across story segments"
- L3→L4: "Infer author/character perspective"
- L4→L5: "Evaluate implications of narrative choices" (G7+ only)

## 2.9 Grade eligibility
**K-G11.** Universal. Story Mode is the Phase 2 driver for every session in every framework.

## 2.10 Subject eligibility & `framework_bans`
Eligible: all subjects.
`framework_bans: []`

## 2.11 Anti-cheat surface
- Tier 2 watches for: checkpoint completion time below a floor (<10s per segment = skipping story), clipboard paste into short-answer input, near-identical short-answer text across students, rapid forward-button mashing.

## 2.12 Telemetry events
- `sm_segment_started` (segment_id)
- `sm_micro_choice_made` (choice_id, branch_taken)
- `sm_checkpoint_mc_result` (item_id, correct, time_ms)
- `sm_checkpoint_sa_score` (item_id, rating)
- `sm_gate_outcome` (segment_id, passed, attempts)
- `sm_remediation_triggered` (segment_id)
- `sm_stranger_test_flag` (segment_id, flagged_by_review)

## 2.13 Cost profile
- **Tier 1:** MC scoring, branch variant selection, gate threshold logic, segment sequencing
- **Tier 2:** short-answer keyword matching + semantic similarity fallback
- **Tier 3:** none (core story is pre-authored, variants are Tier 2)
- **Est. per-round cost:** <$0.005

## 2.14 Device requirements
- **Min:** low-tier Android (1.5GB RAM), 720×1280
- **Bandwidth:** ~1-2MB per story (text + illustrations)
- **Special hardware:** none (TTS optional, voice input optional)

## 2.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 3-4 min |
| G3-4 | 5-7 min |
| G5-6 | 7-10 min |
| G7-9 | 10-13 min |
| G10-11 | 13-17 min |

---

# 3. Adaptive Quiz (Default #7)

## 3.1 Summary
IRT-calibrated question bank serves items at the student's current ability estimate (theta), with **productive-failure scaffolding** on wrong answers (metacognitive prompt → partial solution → answer + explanation). Fixed question count per round — **no early termination** (merge decision).

## 3.2 Core loop
1. System picks starting item at student's current theta.
2. Student answers. **Immediate feedback:** correct/wrong.
3. **On wrong answer → Productive Failure scaffold:**
   - **Step 1:** Metacognitive prompt ("What do you already know about this topic?")
   - **Step 2:** Partial worked solution (shows first step of reasoning, not the answer)
   - **Step 3:** Full answer + explanation contrasting student's likely misconception with correct reasoning
4. System updates theta via Bayesian update after each item.
5. Next item picked at new theta ± 1 level.
6. Round ends after fixed question count. Final theta logged to student profile.

## 3.3 Grade-band design variations

| Grade band | Questions per round | Feedback timing | Scaffold depth on wrong |
|---|---|---|---|
| K-G2 | 3 | Immediate, visual | 1-step: show correct answer with illustration |
| G3-4 | 4 | Immediate | 2-step: hint → answer |
| G5-6 | 5 | Immediate | 3-step full productive failure scaffold |
| G7-9 | 7 | Immediate | Full scaffold + misconception contrast |
| G10-11 | 7 | Round-end summary + per-item immediate | Full scaffold + self-explanation prompt |

**MERGE APPLIED:** Question count is **fully fixed** per grade band. No early termination for high performers. The research doc suggested early-stop on 3 consecutive correct at ceiling, but that creates variance in session time budgeting, which contradicts the same doc's own argument that "predictability matters more than measurement precision for homework."

## 3.4 Content author input
- Item bank with IRT parameters (difficulty, discrimination) — pre-calibrated via field testing or seeded from content team estimates, then refined via live Bayesian update once ~100 student responses accumulate per item
- Metacognitive prompts per item or topic
- Partial worked solutions per item
- Misconception-to-correct-reasoning explanations per item

## 3.5 Evaluation & retry rules
- **Binary correct/wrong** per item.
- **No retry** on same item in the round (item is "spent").
- Wrong items re-enter the student's spaced-repetition queue for Memory Sprint in future sessions.
- Productive failure scaffold triggers automatically on wrong answer.

## 3.6 PISA coverage
- **Levels:** L1-L6 (full range, adaptive).
- **Domains:** Math, Science, Reading, foreign languages — depending on item bank.
- **Processes:** All processes depending on item type.

## 3.7 Bloom's band
Primary: **Apply, Analyze.**
Secondary: Remember, Understand (at lower PISA levels L1-L2).

## 3.8 Transition skill types
Adaptive Quiz is the flexible workhorse — can scaffold any PISA transition depending on item bank composition. Particularly strong for:
- L2→L3: "Apply learned procedure to unfamiliar context"
- L3→L4: "Analyze a multi-step problem and select approach"

## 3.9 Grade eligibility
**K-G11.** Universal (with scaffold depth scaling by grade).

## 3.10 Subject eligibility & `framework_bans`
Eligible: Math, Science, Reading, foreign languages, most content subjects.

**Explicit bans:**
- `framework_bans: ["science_grade5"]` — Science G5 bans Adaptive Quiz because it "feels like endless testing" to Uzbek G5 students (per existing framework override doc).

**Flagged for review:**
- Tarbiya (G5+) — no objective right answers; probably not a good fit
- Tasviriy Sanat (G5+) — creative, not quiz-able

## 3.11 Anti-cheat surface
- Tier 2 watches for: answer time below a floor (<3s = guessing without reading), pattern answering (always A, always first option), theta improvement curve too steep (suspect external help), clipboard paste into short-answer inputs.

## 3.12 Telemetry events
- `aq_item_served` (item_id, student_theta_before, item_difficulty)
- `aq_item_answered` (item_id, correct, time_ms)
- `aq_scaffold_step` (item_id, step: metacog | partial | answer)
- `aq_round_complete` (final_theta, items_correct, items_total)

## 3.13 Cost profile
- **Tier 1:** item selection, IRT Bayesian update, scoring, scaffold content selection
- **Tier 2:** short-answer item evaluation (if present); scaffold text personalization
- **Tier 3:** none (scaffolds are pre-authored, not live-generated)
- **Est. per-round cost:** <$0.003

## 3.14 Device requirements
- **Min:** low-tier Android, 720×1280
- **Bandwidth:** minimal (text + light graphics)
- **Special hardware:** none

## 3.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 3 min |
| G3-4 | 4-5 min |
| G5-6 | 5-7 min |
| G7-9 | 7-10 min |
| G10-11 | 10-13 min |

---

# 4. Mystery Box (Default #8)

## 4.1 Summary
Student picks from 2-5 boxes (grade-dependent) with **vague thematic labels** — "Something about plants..." or "From last week's chapter...". Each box contains a problem from a different prior chapter, interleaved. The vague-label design sits at the inverted-U peak of curiosity (Loewenstein 1994): not blind (anxiety), not revealed (boring).

**Not to be confused with Treasure Chest** — the metagame reward event is a separate mechanic (see Cross-Cutting Notes).

## 4.2 Core loop
1. System presents N closed boxes, each with a vague thematic label.
2. Student picks any box in any order (autonomy-preserving — Self-Determination Theory).
3. Box opens: problem from the labeled category appears.
4. **Identification step** (G3+): student identifies what problem type this is before solving (discriminative contrast).
5. Student solves the problem.
6. Feedback: correct/wrong. Correct = box "claimed." Wrong = one retry offered.
7. Round ends when all boxes resolved.
8. **Bonus connection:** 1-in-10-to-15 rounds includes a cross-subject "bonus connection" box, explicitly framed as a bonus.

## 4.3 Grade-band design variations

| Grade band | Box count | Label specificity | Identification step |
|---|---|---|---|
| K-G2 | 2 | Picture only, no text | Skipped — just solve |
| G3-4 | 3 | Short vague text ("Plants?") | Optional |
| G5-6 | 3 | Vague thematic ("Something about last week") | Required |
| G7-9 | 4 | Vague thematic | Required + brief justification |
| G10-11 | 4-5 | Abstract thematic | Required + justify + connect to prior |

## 4.4 Content author input
- Problem pool from prior chapters, tagged by category/chapter
- Vague thematic labels per category (authored to be noticeable but not revealing)
- Difficulty levels matched to student's theta
- Occasional cross-subject "bonus connection" problems (flagged)

## 4.5 Evaluation & retry rules
- **Identification step:** correct or wrong (one retry on wrong category guess). No penalty — discriminative contrast is the point.
- **Solve step:** evaluated per item type (MC, short-answer, etc.) — same rules as Adaptive Quiz items.
- **Box order:** any — student picks order freely (autonomy).

## 4.6 PISA coverage
- **Levels:** L2-L5 (requires identifying context before solving).
- **Domains:** All.
- **Processes:** "Recognize problem type," "Select appropriate strategy," "Apply prior learning."

## 4.7 Bloom's band
Primary: **Apply, Analyze** (strategy selection).
Secondary: Remember (retrieval from prior chapters).

## 4.8 Transition skill types
- L2→L3: "Recognize when to apply which tool"
- L3→L4: "Strategy selection across multiple plausible approaches"

## 4.9 Grade eligibility
**K-G11.** Identification step scales by grade; K-G2 skips it entirely.

## 4.10 Subject eligibility & `framework_bans`
Eligible: all subjects with accumulated chapter history. **First-chapter sessions cannot use Mystery Box** (no prior chapters to interleave).
`framework_bans: []`

## 4.11 Anti-cheat surface
- Tier 2 watches for: always picking same-position box (gaming the order), identification step answered before box fully opens (automation suspicion).

## 4.12 Telemetry events
- `mb_round_started` (box_count, categories_served)
- `mb_box_picked` (box_id, order_index)
- `mb_identification_result` (box_id, correct, attempt)
- `mb_solve_result` (box_id, correct, time_ms)
- `mb_bonus_connection_triggered` (box_id, cross_subject_tag)

## 4.13 Cost profile
- **Tier 1:** box generation, category pool selection, identification matching
- **Tier 2:** solve-step evaluation (inherits from item type)
- **Tier 3:** none
- **Est. per-round cost:** <$0.003

## 4.14 Device requirements
- **Min:** low-tier Android
- **Bandwidth:** minimal
- **Special hardware:** none

## 4.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 2-3 min |
| G3-4 | 3-5 min |
| G5-6 | 5-7 min |
| G7-9 | 6-9 min |
| G10-11 | 7-10 min |

---

# 5. Memory Match Blitz (Interactive #4)

## 5.1 Summary
Concentration-style grid. Student flips cards to find pairs. When a pair is found, a **confirmation question tied to that specific pair** gates whether the pair locks. Wrong confirmation → correct answer flashes for **exactly 3 seconds (mandatory)** → cards re-hide. Leverages hypercorrection effect (Butterfield & Metcalfe 2006).

## 5.2 Core loop
1. Grid displays face-down. Cards contain term-definition pairs (mixed).
2. Student flips two cards.
3. If cards don't match → both re-hide.
4. If cards match → confirmation question appears, tied to that specific concept (not a random question from the pool).
5. Student answers confirmation:
   - **Right** → pair locks, stays face-up, score increases.
   - **Wrong** → correct answer flashes for **exactly 3 seconds** (hypercorrection window — mandatory, non-negotiable), then cards re-hide.
6. Round continues until all pairs locked OR soft timer expires.
7. Final score = pairs locked + speed bonus (fluency reward).

## 5.3 Grade-band design variations

| Grade band | Grid size | Pairs | Timer | Confirmation question |
|---|---|---|---|---|
| K-G2 | 2×3 | 3 | None | Skipped — just match |
| G3-4 | 3×4 | 6 | Soft 2 min | Simple MC |
| G5-6 | 3×4 or 4×4 | 6-8 | Soft 90s | MC + brief explanation |
| G7-9 | 4×4 | 8 | Soft 90s | Short-answer about the concept |
| G10-11 | 4×5 | 10 | Soft 60s | Short-answer + connection question |

**Max grid: 4×5 (20 cards, 10 pairs).** Larger grids exceed working memory (~4 chunks per Cowan 2001) and shift the task from memory strategy to random search.

**MERGE APPLIED:** 3-second correct-answer flash on wrong confirmation is **mandatory** — not optional. Implementation must not re-hide cards instantly. The 3-second window preserves the hypercorrection benefit.

## 5.4 Content author input
- Term-definition pair pool per chapter
- Confirmation question per pair — **must be tied to that specific concept**, not generic or pool-random
- Correct-answer flash content (what the student sees during the 3s window)

## 5.5 Evaluation & retry rules
- **Match step:** no gating — student tries freely.
- **Confirmation step:** wrong answer → mandatory 3s correct-answer flash → re-hide.
- Pair can be re-attempted in the same round (retrieval practice + corrective feedback loop).
- **Soft timer:** points decrease with time, but round does NOT end on timeout. Student completes at their pace.
- Speed bonus rewards fluency without punishing slower students.

## 5.6 PISA coverage
- **Levels:** L1-L3 (recall, definition mapping, basic application).
- **Domains:** All with term-definition content.
- **Processes:** "Retrieve from long-term memory," "Map term to meaning."

## 5.7 Bloom's band
Primary: **Remember, Understand.**

## 5.8 Transition skill types
- L1→L2: "Map term to its definition in context"
- L2→L3: "Recognize term when presented in varied form"

## 5.9 Grade eligibility
**K-G11.** Grid size scales by working memory capacity.

## 5.10 Subject eligibility & `framework_bans`
Eligible: subjects with term-definition content (Science, Language subjects, Tarbiya vocabulary, Geografiya place-names, etc.). Less useful for process-heavy subjects (Math procedures, Tasviriy Sanat technique) but not banned.
`framework_bans: []`

## 5.11 Anti-cheat surface
- Tier 2 watches for: confirmation question answered faster than human read time (<1s), identical wrong-then-right patterns (memorizing card positions rather than content).

## 5.12 Telemetry events
- `mmb_round_started` (grid_size, pair_count)
- `mmb_pair_found` (pair_id, attempts_to_find)
- `mmb_confirmation_result` (pair_id, correct, time_ms)
- `mmb_hypercorrection_shown` (pair_id) — logs the 3s flash event
- `mmb_round_complete` (pairs_locked, time_s, score)

## 5.13 Cost profile
- **Tier 1:** grid generation, match detection, scoring, 3s flash rendering
- **Tier 2:** confirmation question evaluation (if short-answer)
- **Tier 3:** none
- **Est. per-round cost:** <$0.002

## 5.14 Device requirements
- **Min:** low-tier Android
- **Bandwidth:** minimal
- **Special hardware:** none

## 5.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 2-3 min |
| G3-4 | 3-5 min |
| G5-6 | 4-6 min |
| G7-9 | 5-7 min |
| G10-11 | 6-8 min |

---

# 6. Reaction Chain (Interactive #5)

## 6.1 Summary
4-10 **conceptually sequential** nodes light up as student answers correctly. 3 wrong in a row resets the streak to 0 (but lit nodes keep their partial credit). Soft 15-30s countdown per node — timeout counts as 1 wrong. Default visual is linear node chain; **top-20 chains by usage after 6 months get custom process-diagram visuals** (merge decision).

## 6.2 Core loop
1. System presents a chain of N conceptually sequential nodes linked to a topic with natural order (photosynthesis steps, water cycle, historical event chain, algorithm flow, math procedure).
2. Node 1 question appears.
3. Student answers.
   - **Correct:** node lights up, move to node 2.
   - **Wrong or timeout:** adds to 3-in-a-row counter.
4. If 3 wrong in a row → **chain "breaks" visually**, streak resets to 0, lit nodes keep their partial credit points.
5. **Recovery scaffold on break:** "Your streak was [X]. Let's rebuild it together." Next question is 1 level easier.
6. Round ends when all nodes lit OR max question count reached.

## 6.3 Grade-band design variations

| Grade band | Nodes | Timer per node | Break threshold |
|---|---|---|---|
| K-G2 | 4 | None | 2 wrong in a row |
| G3-4 | 5-6 | 30s soft | 3 wrong in a row |
| G5-6 | 6-8 | 20s soft | 3 wrong in a row |
| G7-9 | 8-10 | 15s soft | 3 wrong in a row |
| G10-11 | 10 | 15s soft | 3 wrong in a row |

**MERGE APPLIED:** Custom process-diagram visuals (photosynthesis-specific art, historical-timeline-specific art, etc.) only for the **top 20 chains by usage after 6 months of production data**. All other chains use the auto-generated default linear-node visual. Stops endless "should we build custom X?" debates and prevents over-investment on low-traffic content.

## 6.4 Content author input
- N conceptually sequential concepts in **strict order**
- Question per node, calibrated to student level
- Recovery question pool (easier than normal) for scaffold on break
- Default linear visual auto-generated; custom process diagram authored only for top-20 chains

## 6.5 Evaluation & retry rules
- **Binary correct/wrong** per node.
- **Timeout** counts as wrong (contributes to 3-in-a-row counter).
- **On break:** partial credit preserved for lit nodes, streak resets to 0, recovery scaffold activates.
- Round completes at all-nodes-lit or max question count reached.

## 6.6 PISA coverage
- **Levels:** L2-L4 (sequential reasoning, process understanding).
- **Domains:** Science (process chains), Math (multi-step procedures), History (event chains), IT (algorithms).
- **Processes:** "Sequence steps correctly," "Identify causal chain," "Apply procedural knowledge."

## 6.7 Bloom's band
Primary: **Understand, Apply.**
Secondary: Analyze (at higher node depths where cause-effect reasoning matters).

## 6.8 Transition skill types
- L2→L3: "Recall sequenced information in correct order"
- L3→L4: "Understand causal/procedural flow between steps"

## 6.9 Grade eligibility
**K-G11.** Node count and timer scale by grade.

## 6.10 Subject eligibility & `framework_bans`
Eligible: subjects with inherently sequential content (Science processes, Math procedures, History timelines, Programming/IT algorithms, Geografiya physical processes).

**NOT appropriate for:** Tarbiya (values content has no natural sequence), Tasviriy Sanat (creative content has no natural sequence), vocabulary recall (no sequence).

**Flagged bans — needs review:**
- `framework_bans: ["tarbiya_grade5", "tasviriy_sanat_grade5"]`

## 6.11 Anti-cheat surface
- Tier 2 watches for: answer time below a floor (<2s per node = pattern guessing), identical wrong-node sequences across students.

## 6.12 Telemetry events
- `rc_chain_started` (chain_id, node_count, custom_visual: bool)
- `rc_node_answered` (node_id, correct, time_ms)
- `rc_streak_broken` (nodes_lit_at_break, recovery_triggered)
- `rc_chain_complete` (nodes_lit, total, time_s)

## 6.13 Cost profile
- **Tier 1:** node rendering (linear visual auto-generated), streak tracking, scoring, recovery scaffold selection
- **Tier 2:** question evaluation (if short-answer)
- **Tier 3:** none
- **Est. per-round cost:** <$0.002

## 6.14 Device requirements
- **Min:** low-tier Android
- **Bandwidth:** minimal for linear visual; custom process diagrams add ~200-500KB per chain (top 20 only)
- **Special hardware:** none

## 6.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | 2-3 min |
| G3-4 | 3-5 min |
| G5-6 | 5-7 min |
| G7-9 | 6-9 min |
| G10-11 | 7-10 min |

---

# 7. Word Ladder Climb (Interactive #6)

## 7.1 Summary
Transform a start word into a target word one letter at a time, each intermediate step must be a real dictionary word. Each rung is a **2-phase step**: (1) answer a subject question, (2) solve the letter-change puzzle as the "reward." **Language subjects ONLY.** Ladder capped at 5-6 rungs max (merge decision).

## 7.2 Core loop
1. System presents start word and target word (e.g., COLD → WARM).
2. **Rung 1:**
   - **Phase A:** Subject question appears (grammar, vocabulary, definition).
   - Student answers. Correct → unlocks the letter-change puzzle. Wrong → hint offered (within hint budget).
   - **Phase B:** Student performs the letter change — 1 letter substitution, result must be a real dictionary word (validated against stored wordlist).
   - Correct letter change → move to rung 2. Wrong → try again (up to 2 attempts, then hint or auto-skip).
3. Repeat for 4-5 more rungs until target word reached.
4. Ladder completes at target. Skip budget: 1 skip per ladder total.

## 7.3 Grade-band design variations

| Grade band | Rungs | Word length | Skip budget | Hints |
|---|---|---|---|---|
| K-G2 | **NOT ELIGIBLE** | — | — | — |
| G3-4 | 3 | 3-4 letters | 1 skip | Unlimited hints |
| G5-6 | 4-5 | 4 letters | 1 skip | 1 hint per step |
| G7-9 | 5-6 | 4-5 letters | 1 skip | 1 hint per step |
| G10-11 | 6 | 4-5 letters | 1 skip | No hints, just skip budget |

**MERGE APPLIED:** Ladder capped at 5-6 rungs maximum. Each rung is 2 interactions (question + puzzle) so longer ladders drag — 6 rungs × 2 interactions = 12 interactions is already at the limit for a Phase 3 game.

## 7.4 Content author input
- Pre-validated word ladder database (start/target pairs with known valid letter-change paths)
- Subject question per rung
- Hint content per rung (first/last letter reveal, definition clue)
- Dictionary validation source per language (Uzbek, Russian, English)

## 7.5 Evaluation & retry rules
- **Subject question (Phase A):** correct advances; wrong offers hint (within budget); second wrong auto-reveals answer and advances.
- **Letter-change puzzle (Phase B):** 2 attempts before hint; after hint, 1 more attempt before auto-skip.
- **Skip budget:** 1 per ladder total — one escape hatch for a frustrating step.
- No streak / no hypercorrection — ladder is linear progression, not retrieval-practice loop.

## 7.6 PISA coverage
- **Levels:** L1-L3 (vocabulary recognition, morphological awareness, spelling pattern application).
- **Domains:** Reading (primary).
- **Processes:** "Recognize word form," "Apply spelling patterns," "Build vocabulary."

## 7.7 Bloom's band
Primary: **Remember, Apply.**
Secondary: Understand (word families, morphology).

## 7.8 Transition skill types
- L1→L2: "Recognize word transformations"
- L2→L3: "Apply orthographic patterns to new words"

## 7.9 Grade eligibility
**G3-G11.** NOT eligible for K-G2 (pre-reading / early reading stage).

## 7.10 Subject eligibility & `framework_bans`
**Eligible: Language subjects ONLY** — Uzbek Tili, Rus Tili, Ingliz Tili (English).

**NOT eligible for:** Science, Math, Biology, History, Tarbiya, Tasviriy Sanat, Texnologiya, Geografiya, IT, Music — essentially every non-language subject.

`framework_bans: ["science_grade5", "tarbiya_grade5", "tasviriy_sanat_grade5", "texnologiya_grade5", "geografiya_grade5"]` — and extends to all future non-language subject frameworks by default.

**Uzbek note:** Classic letter-substitution word ladders don't work well in agglutinative Turkic languages like Uzbek. Uzbek builds words via suffix stacking, not single-letter swaps (example: KITOB → KITOBLAR → KITOBLARIM = "book → books → my books"). A **Suffix Ladder variant** — add/remove one suffix per step, each step a real inflected word — is the linguistically appropriate version for Uzbek Tili and Rus Tili. Same pedagogy (morphological awareness), different implementation. **Flagged as a separate future mechanic — see Cross-Cutting Notes.**

## 7.11 Anti-cheat surface
- Tier 2 watches for: dictionary lookup on another device (answer time consistent with external lookup cadence), clipboard paste into puzzle input.

## 7.12 Telemetry events
- `wlc_ladder_started` (start_word, target_word, rung_count, language)
- `wlc_rung_question_answered` (rung, correct, hints_used)
- `wlc_rung_puzzle_solved` (rung, attempts, correct)
- `wlc_skip_used` (rung)
- `wlc_ladder_complete` (time_s, hints_total, skips_used)

## 7.13 Cost profile
- **Tier 1:** dictionary validation, letter-change matching, hint selection
- **Tier 2:** subject question evaluation (if short-answer items)
- **Tier 3:** none
- **Est. per-round cost:** <$0.002

## 7.14 Device requirements
- **Min:** low-tier Android
- **Bandwidth:** minimal (dictionary stored locally)
- **Special hardware:** none

## 7.15 Session-time allocation

| Grade band | Per round |
|---|---|
| K-G2 | — (not eligible) |
| G3-4 | 3-4 min |
| G5-6 | 4-6 min |
| G7-9 | 5-8 min |
| G10-11 | 6-9 min |

---

# Cross-Cutting Architectural Notes

## A. Mystery Box split → Treasure Chest (separate mechanic)

The original NETS-Game-Catalog-Summary.md conflated two very different things under "Mystery Box":

| Aspect | Mystery Box (this spec, #4) | Treasure Chest (separate, not defined here) |
|---|---|---|
| Purpose | Phase 3 interleaved-practice learning mechanic | Bilim Bazasi metagame reward event |
| Psychology | Discriminative contrast (Rohrer interleaving) + curiosity (Loewenstein) | Variable-ratio reward schedule (Skinner) |
| Research base | Interleaving studies | Behavioral economics |
| K-11 concern | None | Gambling-like mechanics in children's product — ethical flag |

**Recommendation:** Define **Treasure Chest** separately as part of Bilim Bazasi metagame (Layer 4) work. Do not let the two share a name, a UI, or a codebase. The confusion in the original catalog is why the split is necessary.

## B. Word Ladder → Suffix Ladder variant for Uzbek

Classic letter-substitution word ladders are an **English-specific mechanic**. They do not translate to agglutinative Turkic languages. A sibling mechanic, **Suffix Ladder**, should be designed for Uzbek Tili and Rus Tili:

- Add or remove **one suffix** per step
- Each step must be a real inflected/derived word
- Validated against a morphological analyzer (MorphUz or equivalent)
- Same pedagogy (morphological awareness), appropriate implementation

**Action:** Flagged for linguistics review and separate mechanic definition when language subject frameworks are written.

## C. The `framework_bans` pattern

Every mechanic definition in this document includes a `framework_bans` field — an explicit list of subject-grade frameworks that ban this mechanic, with rationale. This makes ban decisions **visible to designers** instead of hidden in override docs.

As more subject frameworks are written, this list grows into a cross-subject compatibility matrix.

**Existing bans captured in this v1.0 document:**

| Mechanic | Banned frameworks | Reason |
|---|---|---|
| Adaptive Quiz | Science G5 | "Feels like endless testing" — G5 psychology |
| Reaction Chain | Tarbiya G5, Tasviriy Sanat G5 (flagged) | Non-sequential content — mechanic requires natural order |
| Word Ladder Climb | All non-language subjects (by design) | Mechanic only works for language content |

## D. Fields marked as best-guess — review needed

The following fields in all 7 mechanic definitions are my first-pass proposals and need review by content/pedagogy leads before locking:

- **PISA coverage levels (L1-L6)** per mechanic
- **Bloom's band assignments**
- **Transition skill type candidates**
- **Cost profile estimates** (per-round cost in USD)
- **Session-time allocations** per grade band

---

# What's Next

1. **Review and adjust this v1.0 draft** — especially the fields in note D above.
2. **Write the remaining 21 mechanics** using this template and research-sourced decisions, if and when the scope expands beyond these 7.
3. **Resolve open items:**
   - Confirm Reaction Chain `framework_bans` for Tarbiya G5 and Tasviriy Sanat G5.
   - Define **Treasure Chest** as part of Layer 4 Bilim Bazasi metagame work.
   - Design **Suffix Ladder** variant with linguistics review when Uzbek Tili framework is written.
   - Validate PISA/Bloom assignments with pedagogy lead.
4. **Sync with the Library Framework** when it lands — content-heavy mechanics (especially Adaptive Quiz item banks and Story Mode authoring) will need re-mapping to Library Framework structures.

---

*Document path: `All analysis/Game Mechanics/NETS-Game-Mechanics-Definitions.md`*
*Primary research source: `NETS-Game-Mechanics-Research-Answers.md` (2026-04-08)*
*Constitution: `NETS-Homework-Engine-UNIFIED.md` v2.0*
*Status: v1.0 skeleton — 7 of 28 mechanics defined. Best-guess fields (see Cross-Cutting Notes D) need review.*
