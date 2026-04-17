# Memory Sprint: Prior Knowledge Activation

> Default Mechanic #1 — Rapid Recall from Prior Chapters

**Players:** 1 | **Mode:** Solo Recall | **Buzan Integrated** | **Bloom's:** Remember | **PISA:** 1 | **AI Tier:** Tier 1

---

## 1. Memory Sprint Mechanics

A **two-phase rapid recall exercise** used as the Phase 1 warm-up in every homework session. Designed to activate prior knowledge from **previous chapters** (NOT current topic), preventing decay and priming the brain for new content.

### Phase 1: Study (5 seconds)

6 items are displayed simultaneously for exactly 5 seconds. Each item shows: emoji/icon + label. The student must memorize as many as possible. Items are drawn from topics covered 2-4 weeks ago (spaced repetition timing).

### Phase 2: Recall (30 seconds)

Items disappear. 6 multiple-choice questions appear one at a time, each testing one of the 6 items shown. Student selects the correct answer from 4 options. The 30-second timer creates mild time pressure (not anxiety — most students finish in 15-20 seconds).

### Flexible Question Formats

Memory Sprint supports 5 sub-formats, selected based on subject and content type:

- **MC Recall:** Standard 4-option multiple choice ("Which process do plants use?")
- **Speed Match:** Two items flash briefly; student taps if they belong to the same category
- **Fill-Blanks:** A key term is removed from a definition; student selects the correct word
- **Order Steps:** 4 steps of a process shown scrambled; student selects the correct first step
- **Image Label:** A diagram is shown; student selects the correct label for a highlighted part

### Parameters

- Items: 6 per sprint
- Study time: 5 seconds (fixed)
- Recall time: 30 seconds (soft cap — student can finish early)
- Questions: 6 (1 per item shown)
- XP: 50 per correct answer (max 300)
- No penalty for wrong answers — the sprint is diagnostic, not evaluative
- Source pool: Spaced Flashcards "Again" items + items from 2-4 weeks ago that haven't been reviewed recently

---

## 2. Tier-Based Access Control

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Phase 1 mandatory warm-up every session | Same + optional "Pre-Sprint" (extra 3-item warm-up before the main sprint) |
| **Question Formats** | MC Recall + Fill-Blanks (standard) | All 5 formats including Speed Match, Order Steps, Image Label |
| **Item Selection** | Algorithm selects from 2-4 week old items | Same + AI prioritizes items from the student's weakest PISA domains |
| **Feedback** | Score shown at end (X/6 correct) | Per-item breakdown showing which items were missed + quick review card |
| **Timer** | Fixed 30-second recall | Adaptive timer: 30s for weak students, 20s for strong students (pressure tuning) |

> **Basic Tier Guarantee:** The core warm-up function — activating prior knowledge with 6 items — is identical for both tiers. Premium adds format variety and adaptive timing, not additional knowledge.

---

## 3. Buzan Integration: Primacy/Recency Activation

Memory Sprint leverages **two of Buzan's core memory principles** simultaneously.

- **Primacy/Recency Effect:** The 5-second study window exploits the fact that the brain remembers the first and last items in a sequence best. Items are ordered so that the student's weakest items appear first (primacy) and last (recency), with stronger items in the middle. This maximizes the chance of recall during the recall phase while still challenging the student on gaps.
- **Color Hooks:** Each item card uses the subject family's color as a background tint. Math = light blue, Science = light green, etc. The color acts as a subconscious category cue, strengthening the memory trace.
- **Multi-sensory Preview (Premium):** In Speed Match format, a brief sound plays when items appear (e.g., a "whoosh" for physics items, a "chirp" for biology). The auditory cue creates an additional encoding channel.

---

## 4. Question Styles & Interaction Mechanics

Memory Sprint questions are **always from past content** — never from the current session's topic. The complexity scales by the student's current PISA level:

| PISA Level | Study Phase Items | Recall Questions | Cognitive Target |
|-----------|------------------|-----------------|-----------------|
| **L1** | Term + large icon (emoji) | MC: "Which one was shown?" with 4 visual options | Visual recognition |
| **L2** | Term + small icon | MC: "What does [term] mean?" with 4 definition options | Definition recall |
| **L3** | Term only (no icon) | Fill-Blanks or MC with plausible distractors (same-family terms) | Concept discrimination — student must distinguish similar concepts |
| **L4** | Process step (partial description) | Order Steps: "Which step comes first?" with 4 process options | Sequential reasoning — student must remember the full process chain |
| **L5+** | Data point or quote fragment | MC: "What principle does this illustrate?" requiring synthesis | Abstract connection — linking specific data to general principle |

> **Stranger Test Compliance:** L1 items always include large icons. L2 items include small icons. A test player who doesn't speak the language can still complete L1-L2 sprints through visual matching. L3+ removes visual support — reading comprehension becomes part of the test.

---

## 5. Victory Conditions & Scoring

### A. Sprint Completion

| Score | XP | Feedback |
|-------|----|----------|
| 6/6 (Perfect) | 300 + 100 bonus = 400 | "Ajoyib! Hammasini esladingiz!" (Excellent! You remembered everything!) |
| 5/6 | 250 + 50 bonus = 300 | "Yaxshi natija!" (Good result!) |
| 4/6 | 200 | "Yaxshi boshlanish!" (Good start!) |
| 3/6 | 150 | "Hali emas — lekin yaxshi harakat!" (Not yet — but good effort!) |
| 2/6 or below | 100 | "Bu materialni qayta ko'rib chiqamiz." (We'll review this material again.) |

### B. Below 60% Threshold — Remediation Routing

If a student scores **below 60% (≤3/6)** on the Memory Sprint, the system routes them to a **targeted remediation micro-exercise** before continuing to Story Mode. The remediation is:

- A 30-second review of the 3 items they missed (items reappear with correct answers highlighted)
- 1 follow-up question per missed item (total 3 follow-ups, MC format)
- No XP penalty — the remediation is supportive, not punitive
- Flagged on the teacher dashboard: "Student struggled with prior knowledge on [topic]"

### C. No "Fail" State

Memory Sprint has no failure condition. Even a student who scores 0/6 continues to the next phase. The sprint's purpose is diagnostic — it tells the system what the student has forgotten so the Story Mode and Game Breaks can compensate. The "Hali emas" framing applies throughout: forgetting is normal, and the system responds by helping, not punishing.

---

*NETS Elite Mechanic Specification — Memory Sprint v1.0*
