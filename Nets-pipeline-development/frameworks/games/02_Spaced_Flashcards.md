# Spaced Flashcards: Ebbinghaus Edition

> Default Mechanic #2 — SM-2 Spaced Repetition Vocabulary & Formula Retention

**Players:** 1 | **Mode:** Solo Recall | **Buzan Integrated** | **Bloom's:** Remember | **PISA:** 1 | **AI Tier:** Tier 1

---

## 1. Spaced Flashcard Mechanics

A swipeable flashcard deck powered by a **modified SM-2 spaced repetition algorithm** (SuperMemo-2, adapted for K-11 education). Each card has an **ease factor** and a **review interval** that dynamically adjust based on the student's self-rated recall performance.

- **Card display:** One card at a time. Front shows term/formula/image. Student flips to reveal back (definition/answer).
- **Self-rating:** After revealing, student rates their recall: **"Yana" (Again)**, **"Qiyin" (Hard)**, **"Yaxshi" (Good)**, **"Oson" (Easy)**.
- **SM-2 algorithm response:**
  - **Again:** Interval resets to 1 day. Ease factor decreases by 0.2. Card reappears in the next session within 10 minutes.
  - **Hard:** Interval x 1.2. Ease factor decreases by 0.15.
  - **Good:** Interval x 2.5 (or ease factor x previous interval for first repetitions). Ease factor unchanged.
  - **Easy:** Interval x 3.5. Ease factor increases by 0.15. Card may skip multiple sessions.
- **Session load:** 5-10 cards per session, 2-3 minutes total.
- **XP:** 50 XP per card rated "Good" or better. 0 XP for "Again" — but the card schedules more frequently so the student can earn it next time.

**Card types:**

- **Vocabulary:** Term → Definition (with example sentence)
- **Formulas:** Formula name → Formula expression (with one worked example)
- **Diagrams:** Diagram with labeled parts → Student must name all parts before revealing
- **Dates/Events:** Date → Event description (or vice versa)
- **Translation:** Word in Uzbek → Word in target language (or vice versa)

### Feeds the Memory Sprint Pipeline

Cards rated **"Again" 3+ times in a row** are automatically added to the **Memory Sprint question pool** for the next session. This creates a closed learning loop:

**Spaced Flashcards** (identify weak items) → **Memory Sprint** (rapid-fire recall on weak items) → **Session Game Breaks** (reinforcement) → **Boss** (summative test)

This loop ensures that items the student struggles with get progressively more exposure across different interaction formats — the exact mechanism that drives the +50-70% retention gain.

---

## 2. Tier-Based Access Control

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Phase 0-B mandatory flashcards (5-10 cards) | Same + on-demand Library access to all past cards |
| **Card Content** | Standard text + emoji | Enhanced: custom illustrations, audio pronunciation (for language cards) |
| **Review Modes** | Standard flip-and-rate only | + "Speed Drill" mode (timed rapid recall, no flip), + "Audio-Only" mode (hear term, recall definition aloud) |
| **Streak Display** | Simple count of consecutive "Good/Easy" ratings | Visual streak bar + milestone celebrations (7-day, 30-day, 100-card) |
| **Due Card Preview** | Not shown — cards appear automatically | Dashboard shows "X cards due tomorrow" so Premium students can plan |
| **SM-2 Tuning** | Standard interval multipliers | Adaptive tuning: algorithm learns individual student's forgetting curve more precisely |

> **Basic Tier Guarantee:** The SM-2 algorithm works identically for both tiers. The core spaced repetition mechanism — the educational engine — is not degraded for Basic students. Premium adds review modes and cosmetic enhancements, not algorithmic advantage.

---

## 3. Buzan Integration: Radiant Encoding

Spaced Flashcards implement **Tony Buzan's memory encoding** principles within the SM-2 framework.

- **Color Hooks per Subject:** Each subject family has a distinct card border color. Math = blue, Science = green, History = gold, Languages = purple, Art = pink. Over time, the color itself becomes a retrieval cue — the student's brain associates "blue border" with "mathematical formula."
- **Imagery & Exaggeration:** Premium flashcards include exaggerated illustrations (e.g., "Photosynthesis" shown as a plant wearing sunglasses and eating a sun like a pizza slice). Per Buzan: bizarre imagery is 3-7x more memorable than literal text. Basic flashcards use emoji-only (simpler but still visual).
- **Associative Chains:** When a student rates a card "Easy" three times in a row, the system draws an invisible "thread" to the next card in the same concept family. After 5+ Easy ratings, the card "graduates" and a branch-complete animation shows it connecting to the student's Knowledge Web (see Tile Match Buzan integration).
- **Multi-sensory hooks (Premium):** Audio pronunciation for language cards. Tapping the card plays the word spoken by a native speaker. The combination of visual + auditory encoding creates dual-channel memory traces.

---

## 4. Question Styles & Interaction Mechanics

Spaced Flashcards are **self-rated** — there is no external question. However, the card content itself scales by PISA level:

| PISA Level | Front of Card | Back of Card | Cognitive Target |
|-----------|--------------|-------------|-----------------|
| **L1** | Term + large icon (e.g., "Triangle" with visual triangle) | Simple definition: "3 sides, 3 angles" | Direct visual recognition |
| **L2** | Term alone (e.g., "Chloroplast") | Definition + diagram showing location in cell | Property identification with visual anchor |
| **L3** | Process name (e.g., "Photosynthesis") | Multi-step description: "CO2 + H2O → Glucose + O2 (with sunlight)" | Process recall — student must remember all steps |
| **L4** | Principle name (e.g., "Natural Selection") | Full definition + one real-world example case | Conceptual understanding with application |
| **L5+** | Abstract framework name (e.g., "Social Contract Theory") | Definition + competing interpretations + one critique | Synthesis — student must understand nuance, not just recall |

> **Stranger Test Compliance:** L1 and L2 cards always include visual elements (icons, diagrams) so a test player who cannot read the target language can still make progress through visual association. L3+ cards may be text-only (reading comprehension is now the test).

---

## 5. Victory Conditions & Scoring

### A. Session Completion (Standard)

Complete all cards in the current batch (5-10 cards). No time limit — student-paced.

- **Perfect Session:** All cards rated "Easy." +200 XP bonus.
- **Strong Session:** 80%+ cards rated "Good" or "Easy." +100 XP bonus.
- **Standard Session:** Any mix. Standard XP (50 per "Good/Easy" card).
- **Struggling Session:** 50%+ cards rated "Again." No XP earned. Cards re-schedule aggressively (next session within 10 min). Flagged for teacher dashboard ("student struggling with X concept").

### B. Long-Term Scoring (Across Sessions)

| Milestone | XP | Condition |
|-----------|----|-----------|
| Card graduated | +100 | Card rated "Easy" 3 consecutive times and moves to long-term review (30+ day interval) |
| Concept family mastered | +250 | All cards in one concept family (e.g., all 8 fraction cards) graduated |
| 7-day streak | +150 | Completed flashcard review every day for 7 days |
| 30-day streak | +500 | Completed flashcard review every day for 30 days |
| 100 cards graduated | +1000 | Cumulative milestone |
| "Again" → "Easy" turnaround | +75 | Card that was "Again" 3+ times is now rated "Easy" (demonstrates learning growth) |

### C. "Hali Emas" (Not Yet) Framing

There is no "fail" state in Spaced Flashcards. The entire mechanic is built on the principle that forgetting is normal — the SM-2 algorithm exists precisely because humans forget. A student who rates everything "Again" is not failing; they are correctly identifying what needs more work. The system responds by scheduling those cards more frequently, not by penalizing the student.

---

*NETS Elite Mechanic Specification — Spaced Flashcards v1.0*
