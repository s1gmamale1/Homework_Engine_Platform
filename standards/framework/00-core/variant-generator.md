---
name: variant-generator
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: §22 reference implementation session (Kvadrat Tenglama, Grade 8 Algebra)
---

# Variant Generator

## Mechanic

When a student fails a question, the remediation flow does not re-serve the identical question. Instead, the engine generates an easier variant that preserves all cognitive tags but reduces numeric complexity.

### Generation Rules

All four constraints must hold simultaneously:

| Constraint | Rule |
|------------|------|
| Bloom level | Keep identical (e.g., if original is Apply, variant is Apply) |
| PISA level | Keep identical (e.g., PISA L3 stays PISA L3) |
| Skill tag(s) | Keep all identical skill_tags from original question |
| Numeric scaling | Scale numeric coefficients to 0.3–0.6 of original values, targeting clean integer or simple fraction results |

The variant tests the same skill at the same cognitive level — only the arithmetic burden is reduced.

### Numeric Scaling Examples (from §22 reference session)

| Original | Variant | Scaling note |
|----------|---------|--------------|
| `x² = 20` | `x² = 16` | Irrational result → clean integer (4²) |
| `x² + 60x – 43200 = 0` | `x² + 10x – 600 = 0` | Large coefficients → scaled ~0.15–0.17× for clean integer roots |

The scaling target is a result the student can verify mentally, removing arithmetic as a confound so the conceptual skill is isolated.

### Attempt Limit

```
attempt_1: serve original question
  IF failed:
    attempt_2: serve variant (scaled coefficients)
    IF failed:
      attempt_3: serve variant (same or further scaled)
      IF failed:
        MAX ATTEMPTS REACHED
        -> Reveal full solution with step-by-step worked example
        -> Activate Socratic Tutoring (TEFCAS framing — "Hali emas!")
        -> Route back to specific Story Mode / Preview segment for the standard
```

Maximum 2 variant attempts (3 total attempts including original) before solution reveal.

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Bloom level preservation | Identical | Never lower Bloom level |
| PISA level preservation | Identical | Never lower PISA level |
| Skill tag preservation | Identical | All original tags must carry over |
| Coefficient scaling range | 0.3–0.6× | Targeting clean integer or simple fraction result |
| Max variant attempts | 2 | After attempt 3, reveal solution |
| Solution reveal trigger | 3 total failed attempts | Includes original attempt |

## Scope

Fires during remediation flow (post-session routing) and within-session emergency steps. Does not fire during the first-pass session — variants are only served after an initial failure on the original question.

## Cross-references

- `routing-algorithm.md` — triggers variant generator for failed questions in the remediation queue
- `difficulty-adaptation.md` — when difficulty tier steps down, the next item served may itself be a variant; check overlap to avoid double-scaling
- `hp-damage-baseline.md` — variant questions in Phase 6 remediation carry the same damage tier as the original (damage is tied to Bloom/PISA level, not numeric complexity)

## Verification

1. Generate a variant of `x² + 60x – 43200 = 0`. Confirm Bloom = Apply, PISA = original level, skill_tags unchanged, roots are clean integers.
2. Serve original → fail → variant → fail → variant → fail. Confirm solution is revealed on 4th display, not a 4th attempt question.
3. Confirm no variant is generated for ungraded phases (0-A, 0-B, 7).
