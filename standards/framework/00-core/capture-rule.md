---
name: capture-rule
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: §22 session decision (not in UNIFIED — new policy)
---

# Notebook Capture Rule

## Rule

Any question that requires the student to **perform a calculation** (solve, derive, compute) requires **Notebook Capture**. Questions that do not require calculation do not require capture.

## Scope

Applies across ALL phases where calculation questions appear:

- **Phase 3 Adaptive Quiz** — primary capture-bearing location for Aniq Fanlar
- **Phase 4 Real-Life Challenge** — solve steps within professional scenarios
- **Phase 6 Final Boss** — solve steps in challenge questions

## Capture vs. No-Capture Decision

| Question type | Capture required? |
|---------------|:-----------------:|
| Solve / derive / compute | YES |
| Recognition / matching | NO |
| Conceptual / definitional | NO |
| Socratic / interpretive | NO |
| Evaluation / judgment | NO |

## Capture UX

1. Student solves the problem on paper
2. Student photographs their written work
3. AI vision evaluates the photograph against the rubric

## General Capture Rubric

Pass if **3 of 4** criteria are present:

1. Original equation written out
2. Intermediate steps shown
3. Final answer matches expected result
4. Handwriting legible

## Failure Mode

If handwriting is unreadable after **2 re-capture attempts**, fall back to a multiple-choice version of the same problem. The problem is not skipped; only the capture mechanic is bypassed.

## Aniq Fanlar Phase 3 Note

For Aniq Fanlar (math/exact sciences), the **Adaptive Quiz is mandatory** and is the primary capture-bearing game in Phase 3. Other Phase 3 games in that family (e.g., Why Chain, Memory Match) run **capture-free** because they are non-calculation by design.

## Cross-references

- `context-policy.md` — Phase 4 scenarios that are purely computational do not use the W5H scaffold (UNIFIED §5.4); capture still applies to their solve steps
- Subject frameworks for Aniq Fanlar — detail which Phase 3 game slots are Adaptive Quiz vs. non-calculation games
- Agent config `agents/content-producer/SCHEMA.md` — output template must flag capture-required questions
