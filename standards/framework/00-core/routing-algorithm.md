---
name: routing-algorithm
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: Matrix v0.4 lines 209-224 | §22 reference implementation session
---

# Routing Algorithm

## Mechanic

### Phase Weights

**Proposal — pending pilot calibration.** These weights are not yet in the Matrix body; they are locked in the Matrix header (v0.4) for carry-forward.

| Phase | Weight |
|-------|--------|
| Memory Sprint (Phase 1) | 10% |
| Game Breaks (Phase 3) | 30% |
| Real-Life Challenge (Phase 4) | 30% |
| Final Challenge (Phase 6) | 30% |

Phases 0-A, 0-B, 5, and 7 are ungraded. Phase 2 (Reading) applies to Language family only and replaces the Story Mode slot; its weight is not yet specified for routing purposes.

### Passing Threshold

`overall_score_pct ≥ 60` → passed.

`overall_score_pct` = weighted sum of graded phase scores using the weights above.

### Routing Logic

```
COMPUTE overall_score_pct from graded phases (weighted)

IF overall_score_pct < 60:
    weakest_phase  = argmin(phase_score_pct, graded phases)
    weakest_skill  = argmin(skill_scores, skill_taxonomy)
    remediation_queue:
        1. Re-show Preview panels relevant to the weakest skill cluster
        2. Re-serve Flash Cards for that skill cluster
        3. Re-serve failed questions only, in easier variant form
    mark lesson as "remediation-required"
    DO NOT advance to next lesson

ELIF overall_score_pct >= 60 AND overall_score_pct > student_subject_avg:
    advance to next lesson
    update student_subject_avg
    mark IMPROVEMENT

ELSE:  # passed but at or below average
    advance to next lesson
    flag regression signal in student_pisa_profile
```

### Skill Taxonomy (6 axes)

Locked in Matrix v0.4. Used by `weakest_skill = argmin(skill_scores)`:

| Skill Axis | Description |
|------------|-------------|
| memory | Retention and accurate recall |
| translation | Cross-language / cross-representation mapping |
| problem-solving | Multi-step procedural reasoning |
| critical-thinking | Evaluation, argument analysis, source assessment |
| application | Using known methods in new contexts |
| metacognition | Awareness and regulation of own thinking |

Each question carries `skill_tags` (array, one or more axes). Per-session skill scores are aggregated from `phase_skill_breakdown` data.

### Skill → Remediation Content Mapping

When remediation is queued, the engine maps the weakest skill axis to Preview panel clusters and Flash Card clusters from the current lesson's pre-generated content:

| Weakest Skill | Remediation Content Priority |
|---------------|------------------------------|
| memory | Flash Cards (0-B) — all cards for current chapter, served again |
| translation | Preview panel: "Better Explanation" + "Examples" (0-A components 2 & 3) |
| problem-solving | Preview panel: "Examples" + "Industry Application" (0-A components 3 & 7) |
| critical-thinking | Preview panel: "Real-Life Research" + "Why This Matters" (0-A components 4 & 6) |
| application | Preview panel: "Examples" + Flash Cards for formulas/methods (0-A component 3 + 0-B) |
| metacognition | Preview panel: "Personal Hook" + "Why This Matters" (0-A components 5 & 6) |

After Preview/Flash Card re-serve, failed questions are served as easier variants (see `variant-generator.md`).

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Passing threshold | 60% | Overall weighted score |
| Phase 1 weight | 10% | Memory Sprint |
| Phase 3 weight | 30% | Game Breaks |
| Phase 4 weight | 30% | Real-Life Challenge |
| Phase 6 weight | 30% | Final Challenge |
| Remediation trigger | < 60% overall | Blocks lesson advance |
| Improvement flag | ≥ 60% AND > student_subject_avg | Marks IMPROVEMENT |
| Regression flag | ≥ 60% AND ≤ student_subject_avg | Flags regression signal |

## Scope

Fires once at session end (Phase 7 analytics layer). Determines whether the student advances to the next lesson or enters remediation. Does not affect within-session difficulty adaptation (see `difficulty-adaptation.md`).

## Cross-references

- `difficulty-adaptation.md` — within-session tier changes; cross-session profile updates
- `variant-generator.md` — produces the easier variants served during remediation
- `hp-damage-baseline.md` — Phase 6 score is derived from HP combat outcome

## Verification

1. Student scores 55% overall → verify lesson marked "remediation-required", no lesson advance.
2. Student scores 65% with prior avg 60% → verify IMPROVEMENT flag set, lesson advances.
3. Student scores 65% with prior avg 70% → verify regression signal flagged, lesson still advances.
4. Confirm weakest skill correctly maps to the appropriate Preview panel cluster in remediation queue.
