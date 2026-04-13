# AI/ML Implementation Feasibility Assessment

## NETS Homework Engine Standards v1.0 — Production Readiness Review

**Assessor:** Donatello (General Assistant)
**Date:** 2026-04-02
**Source Document:** `HOMEWORK_STANDARDS.md` (v1.0, April 1 2026, 2,060 lines)
**Scope:** All AI and machine-learning specifications — IRT adaptation, flow-state algorithm, AI content generation, anti-cheat AI, and scale feasibility for 8.8 million K-11 students in Uzbekistan.

---

## 1. Executive Summary

**Verdict: NEEDS MAJOR SPECIFICATION WORK before an engineering team can build this.**

The document contains strong pedagogical vision grounded in real research. However, every AI/ML subsystem has critical specification gaps that would force an engineering team to make unguided design decisions with significant impact on learning outcomes and operational cost. The problems fall into three categories:

1. **Algorithms specified but technically incorrect.** The IRT implementation (§11.5) is not IRT — it is a fixed-step heuristic that discards the discrimination and guessing parameters it requires each question to carry. An engineering team building this as written would produce ability estimates that are measurably worse than a correct implementation.

2. **AI capabilities assumed but never scoped.** Why Chain (§11.6), Real-Life Challenge (§11.8), Story Mode (§11.9), anti-cheat Socratic verification (§2.7), and question regeneration all require live large-language-model inference for 8.8M daily users. The document specifies none of: model requirements, latency SLAs, cost per student, fallback behavior under load, content-safety filtering for children aged 6-17, or an offline alternative for the features marked as online-only.

3. **Scale arithmetic not performed.** Back-of-envelope calculations (Section 5 below) put LLM inference demand at ~70-90 million calls per school day. At current price points this alone would cost on the order of $1-5M USD per month — before infrastructure, storage, bandwidth, or the question-bank calibration pipeline that does not yet exist.

None of these problems are unfixable. But shipping the spec as "Production Ready" without resolving them risks building a system that either (a) does not actually personalize learning, (b) cannot run at Uzbekistan-scale cost constraints, or (c) both.

---

## 2. Critical Specification Gaps

These are items an engineering team **cannot build** from the current document alone.

### 2.1 IRT Implementation Is Not IRT (§11.5, lines 1649-1686)

**What the spec says:** Each question is pre-calibrated with difficulty (θ), discrimination (α), and guessing (c). After each response, student ability θ is updated by a fixed ±0.3 step.

**Why this is a problem:**

The defining feature of Item Response Theory is that the *information* each item provides about ability depends on the item's parameters *and* the student's current ability estimate. The fixed ±0.3 step ignores this entirely:

| IRT Property | Real IRT (2PL/3PL) | Spec's Algorithm |
|---|---|---|
| Uses discrimination (α) | Yes — high-α items produce larger ability updates | No — every item moves θ by exactly 0.3 |
| Uses guessing (c) | Yes — correct answers on high-c items are discounted | No — correct = +0.3 regardless of guessing probability |
| Update magnitude adapts | Yes — updates shrink as estimate converges | No — always ±0.3 |
| Standard error estimated | Yes — stops when SE is below threshold | No — runs for fixed 5-7 questions |
| Final ability precision | SE typically < 0.3 with 15-20 items | SE effectively ≥ 0.9 with 5-7 items at fixed step |

**Consequence at scale:** With 8.8M students, crude ability estimates mean millions of students receive questions that are too easy or too hard. This directly undermines the flow-state design (§1.2, Principle 2) that the entire system is built around. The spec requires every question to carry α and c parameters, then builds an algorithm that never uses them.

**Contradiction — guessing parameter (c: 0.1-0.25):** This range assumes multiple-choice questions with 4-10 options. But Memory Sprint (§2.2, line 196) mandates "Pure recall — NO multiple choice for Grades 3+." The Adaptive Quiz spec (§11.5) does not declare its item format. If free-response, c ≈ 0.0 and should not be in the item model. If MCQ, it conflicts with the Memory Sprint philosophy. This needs explicit clarification per game type.

**What the spec must add:**
- Choose an estimation method: MLE, EAP (expected a posteriori), or MAP (maximum a posteriori). EAP with a standard normal prior is the industry standard for short adaptive tests.
- Define a stopping rule: either fixed-length with SE reporting, or variable-length with a target SE threshold (e.g., SE < 0.35).
- Specify the question-bank calibration pipeline (see §2.2 below).
- State the item format for Adaptive Quiz (MCQ vs. free-response) and set c accordingly.

### 2.2 No Item Calibration Pipeline (§11.5, implied)

**What the spec says:** Each question must have pre-calibrated θ, α, and c parameters.

**What it does not say:** How those parameters are obtained.

IRT calibration is a major psychometric undertaking:

| Dimension | Scale |
|---|---|
| Grades | K-11 (12 grade levels) |
| Subjects | Math, Reading, Science (minimum 3) |
| Chapters per subject per year | ~30 (estimated from textbook structure) |
| Questions per chapter (3× pool for offline caching, §9.5) | 60-100+ |
| **Total items to calibrate** | **~65,000-110,000** |

Each item calibration requires:
- **Pilot testing:** 500-1,000 student responses per item for stable 2PL/3PL parameter estimates.
- **Psychometric software:** IRTPRO, flexMIRT, Mplus, or open-source (mirt in R, pyirt in Python).
- **Expert review:** Subject-matter experts must verify each item before and after calibration.
- **Equating:** Items across years/editions must be linked to a common scale.
- **Maintenance:** Parameters drift as curricula change; annual re-calibration is standard.

**Estimated cost of initial calibration:** Even if pilot testing is done at scale within the NETS platform itself (field-testing items alongside operational items), the psychometric analysis, expert review, and equating for 65,000-110,000 items is a multi-year, multi-million-dollar project requiring a dedicated psychometrics team. The document does not mention this at all.

### 2.3 Why Chain Requires Undefined AI Capabilities (§11.6, lines 1690-1728)

**What the spec says:**
- Real-time Socratic dialogue: AI must parse student free-text responses, acknowledge partial correctness, and probe deeper.
- "NEVER give direct answer. ALWAYS acknowledge partial correctness. ALWAYS probe one level deeper. Use student's words in follow-up questions." (lines 1723-1727)
- 3-5 levels of depth, 3-minute timer.

**What it does not say:**
- **Model:** What LLM or NLU system? On-device? Cloud-hosted? What size? What language support (Uzbek Latin, Uzbek Cyrillic, Russian)?
- **Latency SLA:** Students will not wait >2-3 seconds for a response mid-dialogue. At 8.8M users, this requires either massive GPU capacity or significant optimization.
- **Safety:** Students aged 6-17 are typing free text to an AI. What content filtering is applied? What happens if a student types harmful content? COPPA-equivalent protections for Uzbekistan?
- **Quality assurance:** How do you verify the AI's Socratic responses are pedagogically sound across 3 subjects × 12 grades? One bad response in science could teach incorrect causal reasoning.
- **Uzbek language support:** Socratic dialogue in Uzbek (Latin or Cyrillic) requires models trained or fine-tuned on Uzbek. Current commercial LLMs have limited Uzbek capability. What's the plan?
- **Offline:** §9.5 (line 1347) confirms Why Chain is NOT available offline. For students without reliable internet — potentially millions in rural Uzbekistan — this means losing access to a game that the spec credits with "+2 PISA sub-level increase in reasoning ability." No fallback or offline approximation is provided.

### 2.4 Story Mode "AI-Generated Video" Undefined (§11.9, lines 1804-1837)

**What the spec says:**
- "AI-generated video OR illustrated panels" (§2.3, line 257)
- Video spec: 30 fps, 720p minimum, 16:9 aspect (line 1829)
- 3 segments × 90 seconds each = 4.5 minutes of narrative video per chapter

**Scale calculation:**
- 12 grades × 3 subjects × ~30 chapters = ~1,080 unique Story Mode videos per year
- Total: ~4,860 minutes (81 hours) of culturally-specific AI-generated educational video per year
- Characters must use Uzbek names, real Uzbek locations, and local cultural references (lines 1833-1837)

**Feasibility assessment:**
- AI video generation in 2026 can produce short clips but struggles with: narrative coherence across 4.5 minutes, consistent character design, culturally specific settings (Registan Square, Bukhara bazaars), and educational accuracy.
- The "OR illustrated panels" alternative is more realistic but still requires ~1,080 illustrated panel sets per year with consistent art style.
- **Recommendation:** Treat "AI-generated video" as a Phase 2+ aspiration. For Phase 1, commission illustrated panels (either artist-drawn or AI-assisted with human review). Specify a content production pipeline with quality review checkpoints.

### 2.5 Real-Life Challenge Dynamic AI Generation (§11.8, lines 1768-1800)

**What the spec says:**
- Present authentic, multi-step real-world scenarios.
- §9.5 (line 1347): "Real-Life Challenge (requires dynamic AI generation)" — not available offline.

**What is unclear:**
- "Dynamic AI generation" — does this mean each student gets a unique scenario, or that scenarios are generated ahead of time from a template library?
- If per-student generation: ~8.8M unique scenarios per day = massive LLM throughput.
- If template-based with variable parameters (e.g., distance = random(200, 400) km): much more feasible, could be pre-generated and cached for offline use.
- The spec should clarify which approach is intended and design accordingly.

### 2.6 Anti-Cheat AI Unspecified (§2.7, lines 811-818)

**What the spec says:**
1. **Question Regeneration:** "Every boss attempt generates NEW questions on same concepts."
2. **Response Pattern Analysis:** "AI detects answers faster than reading speed."
3. **Device Fingerprinting:** "Flag if same account on multiple devices simultaneously."
4. **Socratic Verification:** "After victory, brief follow-up tests understanding."

**Gaps per method:**

**Question Regeneration:**
- Requires either: (a) a very large pre-generated question bank per concept, or (b) real-time LLM generation of new questions.
- If LLM-generated: how are psychometric properties (difficulty, discrimination) maintained? An LLM cannot guarantee that a generated question has the same difficulty as the one it replaced.
- If pre-generated: the question bank must be 3-5× larger than a single-attempt bank. Combined with the IRT calibration gap (§2.2), this multiplies the already-massive calibration challenge.

**Response Pattern Analysis:**
- "Answers faster than reading speed" — requires: (a) grade-level reading speed baselines (words per minute), (b) question complexity measurement, (c) minimum plausible response time calculation.
- No model architecture specified: statistical rule (time < threshold → flag) vs. ML classifier vs. sequence-based anomaly detection.
- **Critical: no acceptable false positive rate defined.** For a system serving children, a false cheating accusation is a serious adverse event. Industry standard for high-stakes assessments: <1% false positive rate. This must be specified and validated.
- What training data? You need labeled examples of cheating vs. legitimate fast responding. For a new platform, this data doesn't exist yet.

**Device Fingerprinting:**
- §9.7 (line 1451) cites Uzbekistan's Law on Personal Data (ZRU-547, 2019). Device fingerprinting collects hardware identifiers, browser characteristics, and potentially biometric-adjacent data.
- In Uzbek schools, devices are commonly shared. A single tablet may serve 20+ students per day. Fingerprinting a shared device conflates the device with the student.
- The spec actually describes multi-session detection (same account, multiple devices simultaneously), which is a different and simpler problem than device fingerprinting. Clarify the intent.
- A legal review against ZRU-547 is needed before implementing any device fingerprinting.

**Socratic Verification:**
- Requires the same LLM capabilities as Why Chain (§2.3 above). Same unresolved questions about model, latency, language support, and safety.

---

## 3. Feasibility Concerns

These are things that are specified but may not work at scale or as described.

### 3.1 Flow State Algorithm Is Under-Specified (§7.1, lines 1119-1131)

The algorithm is 8 lines of pseudocode. For 8.8M students, it needs answers to:

| Question | Current Spec | What's Needed |
|---|---|---|
| Window size | "Every 3-5 questions" | Fixed window or rolling? What triggers re-evaluation? |
| Success rate scope | Not defined | Per game? Per session? Per subject? |
| Boundary behavior | Not defined | What happens at Tier 1 (floor) or Tier 5 (ceiling)? |
| Cold start | Not defined | New student with no history — which tier? How many questions before adaptation kicks in? |
| Cross-game transfer | Not defined | Does performance in Tile Match affect Adaptive Quiz difficulty? |

### 3.2 Overlapping Tier Success Rate Targets (§7.2, lines 1133-1142)

| Tier | Target Success Rate |
|---|---|
| Tier 1 | 80-90% |
| **Tier 2** | **70-80%** |
| **Tier 3** | **70-80%** |
| **Tier 4** | **60-70%** |
| **Tier 5** | **60-70%** |

Tiers 2/3 share the same target, as do Tiers 4/5. The flow algorithm uses <60% and >90% as transition triggers, which means a student can only move *out* of the overlapping range by hitting extreme performance. The targets are descriptive, not operative — but an engineering team reading this table will reasonably ask: "What distinguishes Tier 2 from Tier 3 at implementation time?" The spec needs either distinct targets or an explicit note that tier transitions are driven solely by the <60%/>90% triggers, not by target success rates.

### 3.3 Non-Question Game Adaptation (§7.1)

The algorithm says "every 3-5 questions," but several games do not have discrete questions:

| Game | Interaction Unit | Questions? |
|---|---|---|
| Tile Match | Pair matches (4-6 pairs) | No — matches, not questions |
| Movement Breaks | Self-reported completion | No |
| Memory Palace | Location-concept recall (5 items) | Loosely |
| Story Mode | Comprehension checks (1-2 per segment) | Yes, but only 2-4 total |
| Flashcards | Self-rated recall | Not scored by system |

The flow-state algorithm should define how "success rate" is calculated for each game type, or specify that adaptation only applies to question-based games.

### 3.4 Offline Coverage Gap (§9.5, lines 1340-1349)

Features NOT available offline:
- **Why Chain** (Socratic dialogue — LLM-dependent)
- **Real-Life Challenge** (dynamic AI generation)
- **Peer Teaching** (requires network for matching)
- **Leaderboard updates**

Features available offline (from pre-cached pools):
- Memory Sprint, Flashcards, Tile Match, Sentence Fill, Story Mode, Mystery Box, Adaptive Quiz, Final Boss

**Concern:** Why Chain is credited with "+2 PISA sub-level increase in reasoning ability" (§3.1, line 930) — the single largest claimed learning gain in the entire document. Making it unavailable offline means students with unreliable internet lose access to the most impactful game. In Uzbekistan, internet penetration is ~78% (ITU 2024), but home broadband access in rural areas is significantly lower. The spec should:
1. Estimate what percentage of the 8.8M students will have reliable home internet.
2. Design an offline fallback for Why Chain (e.g., pre-generated branching dialogue trees for common topics, updated when connectivity is available).
3. Analyze whether the 7-Step Learning Journey (§2.1) can still meet its pedagogical goals when Why Chain is unavailable.

### 3.5 Uzbek Language AI Readiness

Multiple features require natural-language AI in Uzbek:
- Why Chain (Socratic dialogue)
- Socratic Verification (anti-cheat)
- Real-Life Challenge (dynamic generation)
- Sentence Fill word-bank generation
- AI-generated reflection prompts
- AI-generated parent recommendations (§9.7)

Current state of Uzbek language in commercial LLMs (2026): limited training data, lower accuracy than English/Russian, limited availability of fine-tuning datasets. The spec should:
1. Define minimum language quality requirements per feature.
2. Specify whether Russian is an acceptable fallback and under what conditions.
3. Plan for model fine-tuning or distillation to achieve acceptable Uzbek quality.

---

## 4. Recommendations

### 4.1 Immediate (Before Engineering Begins)

| # | Recommendation | Priority | Addresses |
|---|---|---|---|
| R1 | **Replace the fixed-step IRT algorithm** with EAP estimation using the 2PL model. Drop the guessing parameter (c) for free-response items; keep it only for MCQ items. Define a stopping rule (fixed-length with SE reporting). | Critical | §2.1 |
| R2 | **Design and fund the item calibration pipeline.** Define: pilot test sample sizes, calibration software, expert review workflow, equating methodology, and re-calibration schedule. Budget for a psychometrics team (2-4 specialists, ongoing). | Critical | §2.2 |
| R3 | **Specify the LLM requirements** for Why Chain, Socratic Verification, and Real-Life Challenge. Include: model size/type, hosting (cloud vs. on-premise), latency SLA (<2s response), content safety filters, Uzbek language quality benchmarks, and cost-per-inference estimate. | Critical | §2.3, §2.5, §2.6 |
| R4 | **Define the anti-cheat false positive rate** target (recommend ≤1%). Specify the response-time model: grade-level reading speed baselines, minimum plausible response times, escalation workflow for flagged students. Require human review before any cheating penalty. | Critical | §2.6 |
| R5 | **Clarify "AI-generated video" scope.** For Phase 1, specify illustrated panels with human art direction. Move AI video to Phase 2 roadmap. Define the content production pipeline. | High | §2.4 |

### 4.2 Before Scale Launch

| # | Recommendation | Priority | Addresses |
|---|---|---|---|
| R6 | **Expand the flow-state algorithm** to a full specification: define window size, per-game success metrics, boundary behavior, cold-start policy, and cross-game transfer rules. Resolve the Tier 2/3 and Tier 4/5 overlap. | High | §3.1, §3.2, §3.3 |
| R7 | **Design offline Why Chain fallback.** Pre-generated branching dialogue trees for high-priority topics, cached locally. Update when online. This is essential for equitable access. | High | §3.4 |
| R8 | **Conduct internet access survey** for target student population. Size the offline-vs-online feature split based on actual data, not assumptions. | High | §3.4 |
| R9 | **Clarify Real-Life Challenge generation mode.** If template-based with variable parameters: can be pre-generated and cached (offline-capable). If per-student LLM generation: must remain online-only and cost is significant. | Medium | §2.5 |
| R10 | **Legal review of device fingerprinting** against ZRU-547. Likely finding: multi-session detection (same account, concurrent logins) is permissible; full device fingerprinting is not. Adjust spec accordingly. | Medium | §2.6 |

### 4.3 Phase 2+

| # | Recommendation | Priority |
|---|---|---|
| R11 | AI-generated video for Story Mode (post-technology maturation). |  Low (future) |
| R12 | Dedicated PISA Level 5-6 mechanic ("Creative Lab") as noted in known limitations (line 1455). | Medium (future) |
| R13 | Advanced anti-cheat: behavioral biometrics (typing cadence, interaction patterns) with privacy-preserving design. | Low (future) |

---

## 5. Infrastructure Estimate (Rough Order of Magnitude)

### 5.1 Daily Load Model

**Assumptions:**
- 8.8M students, each completing 1 session per school day (~200 school days/year)
- Peak homework window: 4 hours (14:00-18:00 local time)
- Peak concurrency: ~40% of daily users = 3.5M concurrent
- Average session: 25 minutes, 7 steps

**Per-session interaction count:**

| Step | Interactions | AI Type |
|---|---|---|
| Memory Sprint | 5-8 evaluations | Rule-based (answer matching) |
| Story Mode | 2-4 comprehension checks | Rule-based + media delivery |
| Game Breaks (3 games) | 15-20 evaluations | Mixed (rule-based + LLM for Why Chain) |
| Real-Life Challenge | 3-4 evaluations | LLM (if dynamic generation) |
| Consolidation | 1 | Rule-based |
| Final Boss | 5-7 evaluations | Rule-based + LLM (question regeneration) |
| Reflection Journal | 1 AI prompt generation | LLM (light) |
| Anti-cheat (continuous) | ~5-10 pattern checks | ML model |
| **Total per session** | **~40-55 interactions** | |

### 5.2 Daily Inference Volume

| Category | Calculation | Daily Volume |
|---|---|---|
| Rule-based evaluations | 8.8M × ~30 per session | ~264M/day |
| LLM calls (Why Chain) | 8.8M × ~4 turns (if selected) × ~33% selection rate | ~11.6M/day |
| LLM calls (Real-Life Challenge) | 8.8M × ~2 calls × ~100% (Step 4 mandatory) | ~17.6M/day |
| LLM calls (question regen, Final Boss) | 8.8M × ~2 calls (retries) × ~30% retry rate | ~5.3M/day |
| LLM calls (Socratic verification) | 8.8M × ~1 call × ~10% trigger rate | ~0.9M/day |
| LLM calls (reflection prompts) | 8.8M × 1 | ~8.8M/day |
| ML inference (anti-cheat) | 8.8M × ~5 checks | ~44M/day |
| **Total LLM calls** | | **~44M/day** |
| **Total rule-based** | | **~264M/day** |
| **Total ML (anti-cheat)** | | **~44M/day** |

*Note: If Real-Life Challenge uses templates instead of per-student LLM generation, LLM total drops to ~27M/day.*

### 5.3 Peak Throughput Requirements

| Metric | Calculation | Requirement |
|---|---|---|
| Peak LLM calls/hour | 44M / 4-hour window × ~60% peak factor | ~6.6M/hour |
| Peak LLM calls/second | 6.6M / 3600 | **~1,830/sec** |
| GPU instances needed (at ~500ms/inference, 1 concurrent per GPU) | 1,830 × 0.5 | **~915 GPU instances** |
| With batching/optimization (4× efficiency) | 915 / 4 | **~230 GPU instances** |

### 5.4 Storage Estimate

| Data Category | Per Student/Year | Total (8.8M students) |
|---|---|---|
| Session logs (responses, timestamps, scores) | ~5 MB | ~44 TB |
| Theta/ability history | ~500 KB | ~4.4 TB |
| Flashcard state (SM-2 parameters) | ~100 KB | ~880 GB |
| Reflection journal entries | ~200 KB | ~1.8 TB |
| Media cache (7-session pre-cache) | ~100-500 MB device-side | N/A (device) |
| Question bank (with IRT parameters) | — | ~5-20 GB (central) |
| Video/illustration assets | — | ~100-500 GB (CDN) |
| **Total central storage** | | **~50-70 TB/year** |

### 5.5 Cost Estimate (Order of Magnitude)

| Component | Monthly Estimate (USD) |
|---|---|
| LLM inference (44M calls/day × $0.001-0.003/call) | $1.3M - $4.0M |
| GPU compute (230 instances × $2/hr × 8hr/day × 22 days) | ~$80K |
| Storage (50-70 TB, cloud) | ~$5-10K |
| CDN / bandwidth (8.8M users, media delivery) | ~$50-100K |
| Anti-cheat ML inference | ~$20-50K |
| **Total infrastructure (monthly)** | **$1.5M - $4.3M** |
| **Annual** | **$18M - $52M** |

*These are rough order-of-magnitude estimates. Actual costs depend heavily on: LLM model choice (commercial API vs. self-hosted open-source), optimization level, actual feature usage patterns, and negotiated pricing. Self-hosted open-source models (e.g., fine-tuned Llama or Mistral variants) could reduce LLM costs by 5-10× but require dedicated ML engineering and GPU procurement.*

**Key cost lever:** If Why Chain and Real-Life Challenge use pre-generated content with light runtime adaptation instead of per-student LLM generation, monthly LLM costs could drop to $200K-$600K — a 5-8× reduction. This is the single most impactful architectural decision for cost feasibility.

---

## 6. Summary of Findings

| Area | Verdict | Primary Issue |
|---|---|---|
| IRT / Adaptive Quiz (§11.5) | **Not implementable as written** | Algorithm ignores its own parameters; no calibration pipeline |
| Flow State Algorithm (§7.1) | **Needs significant expansion** | Under-specified for production; overlapping tier targets; no non-question-game adaptation |
| Why Chain / Socratic AI (§11.6) | **Needs full AI specification** | No model, latency, safety, language, or cost spec; offline gap is equity concern |
| Story Mode video (§11.9) | **Not feasible at scale for Phase 1** | AI video generation not mature enough; illustrated panels more realistic |
| Real-Life Challenge (§11.8) | **Needs architecture decision** | Template-based vs. per-student generation — 5-8× cost difference |
| Anti-Cheat AI (§2.7) | **Needs specification and legal review** | No false-positive rate; no model; device fingerprinting vs. ZRU-547 |
| Scale / Infrastructure | **Feasible but expensive** | $18-52M/year at full scale; major cost lever is LLM architecture choice |

**Bottom line:** The pedagogical design is ambitious and well-researched. The AI/ML implementation specifications are not yet at a level where an engineering team can build confidently. The three highest-priority actions are: (1) fix the IRT algorithm, (2) scope and fund the item calibration pipeline, and (3) make the LLM architecture decision (per-student generation vs. template + adaptation) because it has a $15-40M/year cost implication.

---

*Assessment produced by analyzing all 2,060 lines of HOMEWORK_STANDARDS.md against standard psychometric practice (IRT: de Ayala 2009, van der Linden & Hambleton 1997), OECD PISA technical standards, and current AI/ML infrastructure benchmarks.*
