# Why Chain (Nima Uchun? Zanjiri)

> Default Mechanic #10 — AI-Guided Socratic Dialogue

**Players:** 1 | **Mode:** Solo + AI | **Buzan Integrated** | **Bloom's:** Analyze | **PISA:** 3-4 | **AI Tier:** Tier 2

---

## 1. Core Game Mechanics

Why Chain is an **AI-guided Socratic dialogue** that asks "why?" at increasing depth. The AI never gives direct answers — it always acknowledges the student's response and probes deeper.

**Chain structure:**

- The AI presents an initial question tied to the current lesson topic (e.g., "Nima uchun o'simliklar yorug'likka muhtoj?").
- The student types a free-text answer.
- The AI evaluates the answer for keyword presence and reasoning depth.
- If accepted: the AI acknowledges ("Yaxshi boshlanish!"), then asks the next "why?" at greater depth. The chain continues.
- If rejected: the AI gives a **hint** (not the answer) and invites the student to try again. Hints cost -10 XP.

**Chain depth by grade / PISA level:**

- **Grades 2-3 (L2-3):** 2-3 chain levels. The AI asks "why?" two to three times, each probing one layer deeper into the causal chain.
- **Grades 3-4 (L3-4):** 4 chain levels. The AI digs into multi-step reasoning, requiring the student to connect cause to mechanism to principle.
- **Grades 5-6+ (L5-6):** 5+ chain levels. The final level may present a hypothetical or paradox ("Agar Quyosh faqat infraqizil nur chiqarganida, o'simliklar yashay olarmidi?").

**AI behavioral rules (non-negotiable):**

- **NEVER give a direct answer.** The AI's role is to guide, not to tell. Even on the final chain level, the AI does not state the correct explanation — it asks the student to synthesize.
- **ALWAYS acknowledge.** Every student response receives affirmation first ("Yaxshi!", "Ajoyib!", "Zo'r!") before the next probe.
- **ALWAYS probe deeper.** The AI never accepts a surface-level answer at a deep level. If the student says "because plants need light," the AI asks "why do they need light?" — pushing past the tautology.

**Timer:** 3-minute countdown. The student can work through the chain at their own pace within this window. Timer expiration does not end the chain — the student can continue, but bonus XP for full completion is forfeited.

**Hints:** Each hint costs -10 XP. Hints point to page references, visual cues, or prior lesson content — they never state the answer directly.

---

## 2. Tier-Based Access Control

Why Chain is available to all tiers during Phase 3 sessions. Premium extends chain depth, AI sophistication, and visual polish.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 (Phase 5 — Mustahkamlash) | Same + on-demand access from Library for extra practice |
| **Chain Depth** | Standard depth per grade (2-5 levels as specified above) | +1 additional level per chain (e.g., G3-4 gets 5 levels instead of 4) |
| **AI Response Quality** | Keyword-based evaluation with canned follow-up prompts | LLM-powered dynamic response generation — unique follow-ups per student answer |
| **Hint System** | Static hints (page references, fixed cues), -10 XP each | Adaptive hints (contextual to student's prior mistakes), -10 XP each |
| **Chain Visualization** | Level dots in header (1-5), color-coded by status | Animated chain graph — each answered level draws a connecting line to the next, building a visible reasoning tree |
| **Multi-Topic Chains** | Single-topic chains only (all questions about one concept) | Cross-topic chains (e.g., chain connects photosynthesis → energy → ecosystems) |
| **XP Reward** | Standard (150 per level + 250 completion bonus) | Standard + +50 XP per level for chains completed without hints |

> **Basic Tier Guarantee:** The core Socratic experience is identical for both tiers — the AI asks "why?" at the specified depth, accepts answers, and provides hints. Premium adds dynamic AI generation, deeper chains, and visual polish. The learning outcome is the same.

---

## 3. Buzan Integration: Radiant Questioning

Why Chain implements **Tony Buzan's Radiant Thinking and Hierarchical Order** principles by structuring dialogue as an expanding chain of inquiry.

- **Color Hooks (Chain Depth Encoding):** Each chain level has a distinct color that appears in the level indicator dots: Level 1 = blue (surface), Level 2 = green (mechanism), Level 3 = gold (principle), Level 4 = purple (synthesis), Level 5 = red (paradox). As the student progresses, the colors shift from cool to warm, visually signaling increasing depth. Per Buzan, color gradients help the brain encode hierarchical information — the warmest color signals the most cognitively demanding level.
- **Radiant Branches (Question Tree):** Each "why?" branches outward from the initial concept. In Premium, the completed chain is rendered as a visual tree: the initial concept is the root, each answered question is a branch, and the final synthesis is the terminal node. Students can review their chain later as a study artifact — it represents their own reasoning path, not a teacher's explanation.
- **Imagery Through Verbal Exaggeration:** The AI's acknowledgment phrases use vivid, emotionally positive language ("MUKAMMAL!", "Ajoyib!") that creates an emotional tag on the cognitive effort. Buzan emphasizes that emotional salience strengthens memory — a student who hears "Bu juda chuqur fikrlash!" (That's very deep thinking!) at Level 5 will associate the breakthrough moment with positive affect.
- **Self-Generated Mental Maps:** Because the AI never provides answers, the student must construct their own mental model at each level. This is Buzan's Radiant Thinking operationalized: the student's own reasoning radiates outward from the central concept, building associative links that are personally meaningful rather than externally imposed.

---

## 4. Question Styles & Interaction Mechanics

Why Chain IS the interaction — the student types free-text answers, and the AI evaluates them against keyword sets and reasoning depth. The chain levels scale with PISA complexity.

| PISA Level | Question Style (AI Prompt) | Acceptance Criteria | Cognitive Target | Hint Style |
|-----------|--------------------------|-------------------|-----------------|-----------|
| **L1** | colspan="4" style="text-align:center;" | Why Chain does not operate at L1 — too shallow for Socratic dialogue. Minimum entry is L2. | N/A |
| **L2** | Direct "why" about a known fact ("Why do plants need light?") | Answer contains 1+ topic-relevant keywords from a predefined set | Property identification — connect a known fact to its cause | Page reference to the lesson text where the fact is explained |
| **L3** | Mechanism probe ("Why does light give plants energy?") | Answer identifies the process (photosynthesis, chlorophyll role) + 2+ keywords | Causal reasoning — explain how a cause produces its effect | Visual cue ("Look at the diagram on page 25 — what does the green part do?") |
| **L4** | Principle identification ("Why can ONLY plants do this?") | Answer distinguishes the unique mechanism (chloroplasts, chlorophyll in plant cells) from non-plant alternatives | Process analysis — differentiate between similar systems | Comparison prompt ("What do plant cells have that animal cells don't?") |
| **L5** | Hypothetical scenario ("What if the sun only emitted infrared light?") | Answer proposes a reasoned argument (not just a fact), 15+ characters, references prior chain levels | Evaluation — apply known principles to a novel scenario | Synthesis nudge ("Think about what chlorophyll absorbs — which wavelengths?") |
| **L6** | Paradox or open problem ("If photosynthesis is so efficient, why haven't animals evolved it?") | Answer proposes a multi-factor argument, acknowledges complexity, 20+ characters | Synthesis — construct a novel argument from first principles | Framework prompt ("Consider evolutionary constraints: energy cost, cellular complexity, timescale") |

> **Evaluation Transparency:** The AI uses keyword matching for L2-L4 levels and length + reasoning criteria for L5-L6. This is intentionally simple — the goal is to verify that the student engaged with the concept, not to grade essay quality. A student who types a thoughtful answer without the "right" keywords will be prompted to try again (with a hint), not rejected outright. The system favors inclusion over precision.

---

## 5. Victory Conditions & Scoring

### A. Chain Victory (Standard)

Complete all chain levels within the 3-minute timer:

- **+150 XP per level completed** — awarded immediately upon each accepted answer.
- **+250 XP completion bonus** — awarded when all levels are completed (regardless of timer status).
- **Perfect Chain (no hints used):** Additional +50 XP per level (Premium only).

### B. Partial Completion

Timer expires before all levels are completed:

- **XP for completed levels is retained** (150 XP x levels completed).
- **No completion bonus** — the +250 XP bonus requires all levels.
- **"Hali emas" framing:** "Hali emas — zanjir hali tugamadi!" (Not yet — the chain is not finished!) The student is encouraged to retry in the next session. The incomplete chain is saved and can be resumed from the last completed level.

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Level completed (accepted answer) | +150 | Per level, awarded immediately |
| All levels completed (chain victory) | +250 | One-time bonus for finishing the full chain |
| Premium: Perfect chain (no hints) | +50 per level | Stacks on top of per-level XP |
| Hint requested | -10 | Per hint. Cannot go below 0 XP total |
| Wrong answer (rejected) | 0 | No XP loss — student receives a hint and retries |
| Timer expires (partial) | 150 x levels done | No completion bonus. Chain saved for resume. |
| Timer expires (0 levels) | 0 | Must retry from the beginning |

### D. Maximum Possible XP

- **G2-3 (3 levels, Basic):** 3 x 150 + 250 = **700 XP**
- **G3-4 (4 levels, Basic):** 4 x 150 + 250 = **850 XP**
- **G5-6+ (5 levels, Basic):** 5 x 150 + 250 = **1,000 XP**
- **G5-6+ (5 levels, Premium, perfect):** 5 x (150 + 50) + 250 = **1,250 XP**

> **Research basis:** Elaborative Interrogation (Pressley et al., 1992) shows that asking "why?" and generating explanations improves comprehension by approximately 2 PISA sub-levels. The XP structure rewards depth (more levels = more XP) and independence (hint-free completion bonus). The 3-minute timer creates moderate pressure without making speed the primary metric — reasoning quality matters more than speed.

---

*NETS Elite Mechanic Specification — Why Chain (Nima Uchun? Zanjiri) v1.0*
