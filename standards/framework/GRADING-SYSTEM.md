# NETS Grading System — Learning Curve Specification

**Version:** 1.0 | April 2026 | Replaces: XP-based reward system
**Parent:** `NETS-Homework-Engine-UNIFIED-Buzan.md` v2.0
**Layer:** 4 (grading overlay — sits on top of all mechanics)

---

## 0. Design Principle

XP measures **effort**. The Learning Curve Grade measures **learning progress**. A student who earns 500 XP by getting everything wrong but trying hard is not learning — they're practicing mistakes. The grading system must distinguish between these students.

**What replaces XP entirely:** Every mechanic now feeds into a **Learning Curve Grade** with 4 components:

| Component | Symbol | Range | What It Measures |
|---|---|---|---|
| **Level** | L | 0–100% | Current accuracy on this skill |
| **Velocity** | n | 0.0–1.0 | Rate of improvement (from `y = Kx^n`) |
| **Efficiency** | E | 0–100% | Speed + independence (time per answer, hints used) |
| **Attempts** | A | count | Total practice attempts |

---

## 1. The Learning Curve Model

### The Formula

Every skill's progress follows: `L = K × A^n`

- **L** = current level (accuracy %)
- **K** = baseline constant (derived from first session)
- **A** = total attempts on this skill
- **n** = velocity (learning rate, 0.0–1.0)

### The 4 Phases

| Phase | Level Range | Velocity | What the Student Experiences | System Response |
|---|---|---|---|---|
| **Novice** | 0–30% | Any | "I don't understand this" | Easier questions, more hints, encouraging feedback |
| **Apprentice** | 30–60% | n > 0.4 (rising) | "I'm starting to get it" | Same difficulty, let them ride the growth wave |
| **Apprentice** | 30–60% | n < 0.2 (stuck) | "I keep failing at the same thing" | Switch teaching method, flag for teacher |
| **Proficient** | 60–85% | n > 0.2 | "I can do this reliably" | Push to next PISA level |
| **Proficient** | 60–85% | n < 0.1 (plateau) | "I can't get better than this" | New instruction method, targeted remediation |
| **Mastered** | 85–100% | Any | "This is easy now" | Offer harder variant, move to next skill |

### Trajectory Labels

| Trajectory | Condition | Display | Meaning |
|---|---|---|---|
| **Fast Riser** | n ≥ 0.6 | ↗↗ | Learning faster than 80% of peers |
| **Improving** | 0.3 ≤ n < 0.6 | ↗ | Learning at expected pace |
| **Steady** | 0.1 ≤ n < 0.3 | → | Slow but moving |
| **Plateaued** | n < 0.1, 4+ attempts | ⏸ | Not improving — intervention needed |
| **Declining** | last 2 sessions < previous 2 | ↘ | Performance dropping — investigate cause |

---

## 2. Per-Mechanic Grading Rules

Each mechanic contributes data to the learning curve. Different mechanics measure different things:

### Type A: Accuracy-Based (Pure Correctness)

**Mechanics:** Memory Sprint, Tile Match, Sentence Fill, Memory Palace, Mystery Box, Reaction Chain, Adaptive Quiz, Connect Four, Memory Match Blitz, Puzzle Lock, Tic Tac Toe vs AI

**What gets recorded per session:**
```
{ skill_id, accuracy (%), attempts, time_per_answer (s), hints_used, wrong_count }
```

**Grade displayed after session:**
```
┌───────────────────────────────────────┐
│  Tile Match — Concept: Fractions      │
│                                       │
│  ████████░░  62%  (Apprentice ↗)      │
│  Velocity: n=0.48 (improving)         │
│  Speed: 14s/answer (was 22s ✓)        │
│  Sessions to Proficient: ~3           │
└───────────────────────────────────────┘
```

### Type B: Rubric-Based (Multi-Dimension)

**Mechanics:** Peer Teaching (3 axes), Notebook Capture (4 axes), Real-Life Challenge (3 axes), Why Chain (2 axes)

**What gets recorded per session:**
```
{ skill_id, dimension_scores: {completeness: %, clarity: %, accuracy: %},
  overall: %, attempts, ai_feedback_tags: [...] }
```

**Grade displayed after session:**
```
┌───────────────────────────────────────┐
│  Peer Teaching — Concept: Fractions   │
│                                       │
│  Overall: 68%  (Apprentice ↗)         │
│  ┌──────────────────────────────┐     │
│  │ Completeness: ████████░ 75%  │     │
│  │ Clarity:      ██████░░░ 60%  │     │
│  │ Accuracy:     ███████░░ 70%  │     │
│  └──────────────────────────────┘     │
│  Velocity: n=0.35 (steady improving)  │
│  Flagged: "Accuracy dropping —       │
│           review prerequisite concept"│
└───────────────────────────────────────┘
```

### Type C: Outcome-Based (Win/Loss or Efficiency)

**Mechanics:** Territory Conquest, Final Boss

**What gets recorded per session:**
```
{ skill_id, outcome (win/loss/partial), turns_used, budget_remaining (%),
  accuracy_during_game (%), attempts }
```

**Grade displayed after session:**
```
┌───────────────────────────────────────┐
│  Final Boss — Fraction Comparison     │
│                                       │
│  🏆 DEFEATED  (85% — Proficient ✓)    │
│  Attempts to defeat: 4                │
│  Session 1: 35%  Session 2: 48%      │
│  Session 3: 62%  Session 4: 85%       │
│  Curve: n=0.72 (fast riser ↗↗)       │
│  Skill upgraded: Apprentice → Proficient│
└───────────────────────────────────────┘
```

### Type D: Participation-Based (No Grade, Just Record)

**Mechanics:** Reflection Journal, Movement Breaks

**What gets recorded per session:**
```
{ skill_id, completed (bool), reflection_tags: [...], engagement_seconds }
```

**No grade displayed.** These feed the curve as "session completed" markers but don't affect accuracy.

---

## 3. Session Report Card

Replaces the XP summary screen. After every 7-phase session:

```
╔═══════════════════════════════════════════╗
║   Session Report                          ║
║   G5 Math — Chapter 4: Fractions          ║
║   April 13, 2026                          ║
╠═══════════════════════════════════════════╣
║                                           ║
║  Phase 1  Memory Sprint     5/6  ✓       ║
║  Phase 2  Story Mode        ✓✓✓  ✓       ║
║  Phase 3  Tile Match        62%  ↗       ║
║  Phase 3  Adaptive Quiz     5/7  ↗       ║
║  Phase 3  Mystery Box       2/3  ✓       ║
║  Phase 4  Real-Life Ch.     68%  →       ║
║  Phase 6  Final Boss        85%  ✓       ║
║  Phase 7  Reflection        Done  ✓       ║
║                                           ║
║  ═══ Skill Updates ═══                    ║
║                                           ║
║  📊 Compare Fractions                     ║
║     52% → 62%  (Apprentice ↗)             ║
║     ~3 sessions to Proficient             ║
║                                           ║
║  📊 Equivalent Fractions                  ║
║     71% → 73%  (Proficient →)             ║
║     Plateau risk — try different method   ║
║                                           ║
║  🆕 NEW SKILL UNLOCKED                    ║
║     Add Fractions (same denom.)           ║
║     Starting level: Novice (0%)           ║
║                                           ║
╚═══════════════════════════════════════════╝
```

### Symbol Key

| Symbol | Meaning | Level Range |
|---|---|---|
| ✓ | Proficient or above | 60%+ |
| ↗ | Improving | Any level, n ≥ 0.3 |
| → | Steady / Slow | Any level, 0.1 ≤ n < 0.3 |
| ⏸ | Plateaued | Any level, n < 0.1, 4+ attempts |
| ↘ | Declining | Last 2 sessions worse than previous 2 |
| △ | Apprentice (30-60%) | — |
| ★ | Mastered (85%+) | — |

---

## 4. Feedback Rules (During Session)

The system changes its feedback based on the student's position on the learning curve:

| Curve Position | In-Game Feedback | Difficulty Adjustment |
|---|---|---|
| **Novice, first attempt** | "These are new. Watch for the pattern." | Easiest question, large hints |
| **Novice, 2nd wrong** | "This is tricky. Here's a clue about [specific gap]." | Same difficulty, add hint |
| **Apprentice, rising (n ≥ 0.4)** | "You're getting better! Last time: 35%. Now: 52%." | Hold difficulty — let them ride |
| **Apprentice, stuck (n < 0.2)** | "You've been around this level. Let's try it differently." | Switch question format or mechanic |
| **Proficient** | "You've got this. Want to try the harder version?" | Offer next PISA level |
| **Mastered** | "You've mastered this. Moving to the next challenge." | Auto-advance to new skill |
| **Declining** | "This session feels harder. That's normal — learning isn't a straight line." | Drop to previous level, rebuild confidence |

---

## 5. Reflection Prompts (Phase 7)

The reflection prompt changes based on the student's curve trajectory:

| Curve State | Prompt | Purpose |
|---|---|---|
| **Fast riser** (n ≥ 0.6) | "You improved a lot. What changed? Did something click?" | Identify the breakthrough factor |
| **Steady improver** (0.3 ≤ n < 0.6) | "You're getting better each session. What's different now vs. last time?" | Reinforce self-comparison habit |
| **Plateaued** (n < 0.2, 4+ attempts) | "You've been at about the same level for a few sessions. What feels like the thing holding you back?" | Student self-diagnosis of plateau |
| **Declining** | "This session was harder. What was different? Tired? Rushed?" | Normalize the dip, find the cause |
| **Mastered** | "You know this very well. What would make it more interesting?" | Keep engagement high |

---

## 6. Teacher Dashboard Integration

The teacher sees aggregated learning curve data:

```
Class: G5-Math-4  |  32 students

SKILL HEALTH
┌──────────────────────────────────────────────┐
│ Skill                  │ Avg% │ ↗  →  ⏸  ↘   │
├──────────────────────────────────────────────┤
│ Compare fractions      │  62% │ 18  8   4   2│
│ Equivalent fractions   │  71% │ 12 14   5   1│
│ Add same denom.        │  45% │ 15 10   6   1│
│ Add diff. denom.       │  28% │  8 12  10   2│
└──────────────────────────────────────────────┘

⚠️  ALERTS (Plateau Risk)
• 4 students stuck on "Compare fractions" (n < 0.1, 5+ attempts)
• 2 students declining on "Add diff. denom." (dropping from 35% → 22%)

📊 INDIVIDUAL VIEW
Student: Sardor R.
┌──────────────────────────────────────────┐
│ Compare Fractions:  ████████░░ 62% ↗    │
│   n=0.48  |  8 attempts  |  ~3 to goal  │
│                                          │
│ Equivalent Fractions: █████████░ 73% →  │
│   n=0.12  |  14 attempts  |  PLATEAU    │
│   ⚠ Recommend: switch to Visual Method  │
└──────────────────────────────────────────┘
```

---

## 7. Data Model

```json
{
  "student_id": "student_12345",
  "skills": {
    "UZ-MATH-5-FRAC-03": {
      "name": "Compare fractions (same denominator)",
      "pisa_level": 2,
      "subject": "math",
      "history": [
        { "session": 1, "accuracy": 15, "time_per_answer": 22, "hints": 4, "wrong": 5, "date": "2026-04-01" },
        { "session": 2, "accuracy": 30, "time_per_answer": 18, "hints": 3, "wrong": 4, "date": "2026-04-03" },
        { "session": 3, "accuracy": 45, "time_per_answer": 15, "hints": 2, "wrong": 3, "date": "2026-04-05" },
        { "session": 4, "accuracy": 52, "time_per_answer": 14, "hints": 2, "wrong": 3, "date": "2026-04-08" },
        { "session": 5, "accuracy": 58, "time_per_answer": 12, "hints": 1, "wrong": 2, "date": "2026-04-10" }
      ],
      "curve_fit": {
        "K": 12.5,
        "n": 0.55,
        "r_squared": 0.94,
        "last_updated": "2026-04-10"
      },
      "current_grade": {
        "level": 58,
        "label": "Apprentice",
        "trajectory": "improving",
        "efficiency": 72,
        "attempts": 5,
        "estimated_to_proficient": 3,
        "estimated_to_mastered": 12
      }
    }
  }
}
```

### Curve Fitting Algorithm

On each new data point:
1. Collect all (attempt_number, accuracy) pairs for this skill
2. Fit `log(L) = log(K) + n × log(A)` using least-squares regression
3. Extract `n` (velocity) and `K` (baseline)
4. Calculate `r²` — if < 0.5, the curve is noisy (student oscillating) → flag for teacher
5. Predict attempts to 75% (Proficient threshold): `A_75 = (75/K)^(1/n)`
6. Predict attempts to 90% (Mastered threshold): `A_90 = (90/K)^(1/n)`

---

## 8. Migration from XP

**XP is not deleted** — it becomes a secondary metric. The grading system is primary.

| Old (XP) | New (Learning Curve Grade) |
|---|---|
| "+100 XP per correct match" | "Level 58% → 62% (Apprentice ↗)" |
| "+50 XP per card" | "Spaced repetition interval: 3 days → 7 days" |
| "+300 XP for perfect session" | "Skill upgraded: Apprentice → Proficient ✓" |
| "Total XP: 2,450" | "Skills mastered: 3 | In progress: 7" |
| XP leaderboard | Learning velocity leaderboard (n value, not total) |

**XP remains** for:
- Metagame rewards (Bilim Tokens, Bilim Bazasi)
- Streak bonuses
- Motivational celebrations (confetti, badges)

**XP is removed from:**
- Academic progress tracking
- Teacher dashboard priority
- Remediation routing decisions
- PISA level estimation

---

## 9. What This Replaces in Existing Specs

Every Elite Spec document currently has a "Scoring" section with XP tables. All of these are replaced by:

1. **What data this mechanic feeds** (accuracy, time, hints, rubric scores)
2. **How the grade is computed** from that data
3. **What the student sees** (the grade card format for this mechanic)
4. **What the teacher sees** (alert conditions)

---

*NETS Grading System — Learning Curve Specification v1.0*
