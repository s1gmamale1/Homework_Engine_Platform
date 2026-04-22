# Adaptive Quiz — IRT-Calibrated Dynamic Difficulty Assessment

**Default Mechanic #7**
**Bloom's Level:** Apply
**PISA Level:** 2-3
**AI Tier:** Tier 1 ($0)
**Research Basis:** Item Response Theory (IRT), Expected Gain: +30% measurement accuracy
**Session Phase:** Phase 3 (Game Breaks)

---

## 1. Core Game Mechanics

Adaptive Quiz uses **Item Response Theory (IRT)** to calibrate questions that adjust difficulty after each answer: correct = harder, wrong = easier. Creates a unique question path per student — finding the exact boundary of ability. Provides **~30% more measurement accuracy** than fixed-difficulty assessments.

### IRT Parameters

- **Difficulty (theta, θ):** -3.0 (easiest) to +3.0 (hardest). θ = 0 = grade-level proficiency
- **Discrimination (alpha, α):** 0.5 to 2.0. Higher α = better distinguishes students who know vs. don't know
- **Guessing parameter (c):** 0.1 to 0.25 for MC. Free-response = 0.05

### Adaptive Algorithm (5-7 questions per round)

**Q1 — Seed (θ = 0):** Starts at grade level with high-discrimination question (α ≥ 1.2).

**Q2+ — Difficulty Adjustment:** Correct → θ += 0.3 (harder). Incorrect → θ -= 0.3 (easier). Capped at ±3.0. System prefers questions with higher α at target θ.

**Termination:** Ends at 7 questions, or early convergence (5 questions if standard error < 0.3 for 3 consecutive), or ceiling/floor hit (θ = ±3.0 for 2 consecutive).

### PISA Tier Mapping

| Estimated Theta | PISA Level | Interpretation |
|---|---|---|
| θ ≤ -1.5 | Below L1 | Below grade level — needs foundational support |
| -1.5 < θ ≤ -0.5 | L1 | Basic recall — simple, direct tasks |
| -0.5 < θ ≤ 0.5 | L2 | Grade-level — routine application tasks |
| 0.5 < θ ≤ 1.5 | L3 | Above grade level — multi-step reasoning |
| 1.5 < θ ≤ 2.5 | L4 | Advanced — complex analysis in unfamiliar contexts |
| θ > 2.5 | L5-L6 | Elite — abstract synthesis and evaluation |

### Grade Scaling
- **G1-4:** 5 questions. All MC with visuals. Step = 0.2 (gentler). Min θ = -2.0.
- **G5-7:** 5-7 questions. MC + short-answer. Step = 0.3. Full θ range.
- **G8-11:** 7 questions. MC + short-answer + open-response (AI-evaluated). θ > 1.5 may require multi-step reasoning with written justification.

---

## 2. Tier-Based Access Control

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | During assigned sessions | Same + unlimited on-demand practice from Library |
| **Questions per Round** | 5-7 (adaptive termination) | Same + "Extended Round": 10-12 questions |
| **Feedback per Question** | Correct/wrong + correct answer | Same + micro-explanation with concept link |
| **Theta Visualization** | Simple bar showing current θ | Full θ trajectory graph + trend across past rounds |
| **Subject Heatmap** | Not available | Per-topic θ estimates — "Algebra: θ=+0.8, Geometry: θ=-0.3" |
| **PISA Projection** | Not available | "At this rate, you'll reach PISA L4 in ~6 weeks" |
| **Question Format Mix** | MC dominant, occasional short-answer | Same + open-response (G8+) with partial credit scoring |
| **Retake Cooldown** | 1 round per session | 2 rounds per session |

> **Basic Tier Guarantee:** All students receive the full IRT-adaptive experience — same algorithm, same question pool, same theta estimation. Premium adds detailed analytics, richer feedback, and extended rounds. The core measurement and learning benefit is identical.

---

## 3. Buzan Integration: Color-Coded Confidence

- **Color Gradient for Difficulty:** θ ≤ -1.0 = calming blue. -1.0 to 0.0 = green. 0.0 to +1.0 = amber (productive struggle). θ > +1.0 = deep orange-red. The student *sees* their proficiency shift with each answer.
- **Radiant Knowledge Map:** After each round, a mini mind map shows tested concept branches. Correct = solid green nodes. Missed = pulsing amber nodes.
- **Imagery for Wrong Answers:** Incorrect answers display the correct answer alongside a memorable visual metaphor. Vivid imagery attached to correction creates stronger encoding.
- **Positive Framing of Difficulty Increase:** When θ increases: "Siz kuchliroq savolga tayyorsiz!" — Difficulty increase framed as achievement.
- **Memory Anchor for Repeated Misses:** Missing the same concept type across 3+ rounds triggers a "Memory Anchor" card — one vivid image + one-sentence explanation — as pre-warmup.

---

## 4. Question Styles & Interaction Mechanics

| PISA Level | Question Format | Cognitive Target | Example Style | Time Limit |
|------------|----------------|-----------------|--------------|------------|
| **L1** | MC, 3 options, heavy visuals | Direct recall | "Which organ for photosynthesis?" with images | 30s |
| **L2** | MC, 4 options, some visuals | Comprehension | "If plant kept in darkness, what happens to glucose?" | 45s |
| **L3** | MC or short-answer | Application | "Crops grow faster after thunderstorm. Which nutrient?" | 60s |
| **L4** | Short-answer or multi-step MC | Analysis | "Two plants: one gets fertilizer, 3x larger. Which factor? Justify." | 90s |
| **L5** | Open-response (AI rubric) | Evaluation | "Evaluate: 'plants breathe same way animals do.'" | 120s |
| **L6** | Open-response, multi-paragraph | Creation | "Design a greenhouse for -40°C maximizing photosynthesis." | 180s |

> **Interaction Mechanics:** Progress bar shows question number (e.g., "3/7"). Current theta visible as color-coded dot on difficulty ladder. Feedback: green glow + "To'g'ri!" / red shake + correct answer. No "go back" — forward-only.

---

## 5. Victory Conditions & Scoring

### A. Grade Computation

This mechanic is the **primary PISA level estimator**. Feeds both Type A (Accuracy) and direct PISA data:

| What Gets Recorded | Source | Curve Impact |
|---|---|---|
| Theta estimate (θ) | Weighted average of correct answer difficulties | **Primary** — directly maps to PISA Level |
| Answer accuracy (%) | Correct / total questions | Secondary — validates theta reliability |
| Question discrimination | Alpha values of questions answered | Tertiary — high-α correct = stronger signal |
| Attempts (cumulative) | Total adaptive rounds | Feeds velocity: is θ trending up, stable, or declining? |

### B. Session Report Card

```
Adaptive Quiz — [Topic]
θ = +0.42 → PISA L2 (Grade Level ✓)
Accuracy: 5/7 correct (71%)
Velocity: n=0.55 (improving)
~4 rounds to PISA L3
```

### C. Proficiency Grades

- **Above Grade Level (θ > +0.5):** "Zo'r! Siz sinf darajasidan yuqorisiz!" — Rising arrow. PISA tier upgraded if consistent across 3+ rounds. Grade: Proficient ✓ or Mastered ★
- **At Grade Level (-0.5 ≤ θ ≤ +0.5):** "Yaxshi! Siz kutayotgan darajadasiz." — Theta at grade-level line. Confirmed at current PISA tier
- **Below Grade Level (θ < -0.5):** "Hali emas — lekin siz o'sib boryapsiz." — Upward arrow. No PISA downgrade from single round (requires 3 consecutive below threshold)

### D. No Failure State

Adaptive Quiz **cannot be failed** — every round produces valid measurement data. Even θ = -3.0 is useful information (student needs foundational support). "Hali emas" framing applies only when θ drops below current PISA tier threshold.

### E. Long-Term Tracking

- **Theta trajectory:** Plotted across all rounds. Upward = positive velocity. Flat = plateau. Downward = investigation needed
- **PISA level consistency:** Must demonstrate same PISA level across 3 consecutive rounds before "confirmed"
- **Subject heatmaps (Premium):** Per-topic θ estimates — "Algebra: θ=+0.8, Geometry: θ=-0.3"
- **PISA projection (Premium):** Predictive model estimates when student reaches next PISA level

---

*NETS Elite Mechanic Specification — Adaptive Quiz v1.0*
