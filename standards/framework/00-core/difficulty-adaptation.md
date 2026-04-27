---
name: difficulty-adaptation
status: v0.1 draft — validated against §9 (lines 2715-2788)
layer: 0 (core primitive)
source: UNIFIED-Buzan §9 lines 2715-2788
---

# Difficulty Adaptation Engine

## Mechanic

### Real-Time Adjustment (Within Session)

Checked every 3–5 questions.

```
PRIMARY (percentage-based):
  IF success_rate < 60%:
    -> difficulty_tier -= 1
    -> Provide scaffolding (hints enabled, simpler representations)
    -> DO NOT drop below the student's established floor

  IF success_rate > 90%:
    -> difficulty_tier += 1
    -> Reduce hint availability
    -> Introduce next Bloom's level items

  IF success_rate 70–80%:
    -> Maintain current tier (FLOW ZONE)

SECONDARY (event-based, fires after primary check):
  IF student gets 3 consecutive correct at current level:
    -> Increase difficulty by 0.5 PISA sub-level

  IF student gets 2 consecutive wrong:
    -> Decrease difficulty by 0.5 PISA sub-level
    -> Provide scaffolded version of the question

EMERGENCY:
  IF accuracy in a game break < 40%:
    -> Flag the specific standard
    -> Insert additional Story Mode micro-segment for that standard
    -> The micro-segment references the exact textbook page

ALWAYS:
  -> Maintain 60–80% success rate target (Csikszentmihalyi flow channel)
  -> Track per-standard accuracy, not just overall
  -> Track per-transition-skill accuracy
```

### Difficulty Tiers

| Tier | Description | Success Rate Target | PISA Level Range |
|------|-------------|--------------------|--------------------|
| Tier 1 | Foundational (recall) | 80–90% | Below 1 – 1 |
| Tier 2 | Basic application | 70–80% | 1–2 |
| Tier 3 | Multi-step reasoning | 70–80% | 2–3 |
| Tier 4 | Complex analysis | 60–70% | 3–4 |
| Tier 5 | Advanced evaluation/creation | 60–70% | 5–6 |

**How PISA level drives initial difficulty tier:** At session load, `student_pisa_profile` is read for the subject. The engine maps the student's current PISA level to the corresponding Tier row above. That Tier is the entry point for the session. Domain-specific weakness (e.g., weak in "quantity") shifts initial item selection within the tier; it does not change the tier itself.

### Cross-Session Adaptation

```
AFTER EACH SESSION:
  1. UPDATE student_pisa_profile with new performance data
  2. UPDATE spaced_repetition_model (which items need review, when)
  3. UPDATE standard_mastery_map:
     - Each standard has a mastery score: 0.0 (never seen) to 1.0 (fully mastered)
     - Mastery decays over time (Ebbinghaus curve)
     - Standards below 0.6 mastery are flagged for Memory Sprint inclusion
  4. UPDATE transition_skill_tracker:
     - Mark transition skills as mastered (>80% accuracy across 3+ sessions)
     - Identify new transition skills to target
  5. RECALCULATE domain_breakdown (quantity, space, etc.)
  6. CHECK trajectory:
     - If 3 consecutive sessions show declining performance -> activate Boost Mode
     - If student exceeds grade target PISA level -> offer enrichment content
```

**Boost Mode trigger:** `student_pisa_level < class_average – 0.5` for 3+ consecutive sessions. Activates additional optional practice sessions incentivized with bonus XP and special avatar items, targeted to specific weak standards and transition skills.

**Catch-Up Mode trigger:** Absence > 7 days. AI identifies essential concepts only via prerequisite chain analysis. Final Boss reduced to 50% HP; hints allowed without HP penalty. Maximum 2 catch-up sessions per day.

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Check interval | Every 3–5 questions | Within session |
| Flow zone | 70–80% success rate | Maintain current tier |
| Step-down threshold | < 60% success rate | Decrease tier by 1 |
| Step-up threshold | > 90% success rate | Increase tier by 1 |
| Consecutive correct trigger | 3 in a row | +0.5 PISA sub-level |
| Consecutive wrong trigger | 2 in a row | –0.5 PISA sub-level |
| Emergency accuracy floor | < 40% in a game break | Flag standard + inject micro-segment |
| Mastery decay threshold | < 0.6 mastery score | Flag for Memory Sprint inclusion |
| Transition skill mastery | > 80% accuracy, 3+ sessions | Mark as mastered |
| Boost Mode trigger | < class_avg – 0.5 PISA for 3 sessions | Activate Boost Mode |
| Catch-Up Mode trigger | Absence > 7 days | Activate Catch-Up Mode |

## Scope

Fires in all graded phases (Phase 1, 3, 4, 6) whenever the engine evaluates the next item to serve. Cross-session adaptation runs at session close (Phase 7 analytics layer).

## Cross-references

- `hp-damage-baseline.md` — difficulty tier maps to Easy/Medium/Hard damage values in Phase 6
- `routing-algorithm.md` — overall_score_pct drives advance vs. remediation; this file drives within-session item selection
- `variant-generator.md` — when difficulty steps down, variant generator produces the simpler item

## Verification

1. Simulate a student session with 5 correct then 5 wrong. Confirm tier decreases after wrong streak.
2. Confirm tier never drops below student's established floor.
3. After 3+ sessions of declining performance, confirm Boost Mode flag is set in `student_pisa_profile`.
4. Confirm emergency micro-segment fires exactly once per flagged standard per session.
