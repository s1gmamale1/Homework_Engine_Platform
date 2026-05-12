# Reflection Section — Addendum to New Flow

**Status:** Note for the new flow document owner
**Scope:** Two additions to the Reflection / Debrief / Marking section (Section 15)
**Source:** Resolves Content Quality issues #30 and #31

---

## Addition 1 — Track and report fixed mistakes during the session

### Definition

A "fixed mistake" is recorded when three conditions are met:

1. The student answered wrong at point A in the session
2. The student later answered right at point B on a question tagged with the same skill
3. The correct answer was not shown to the student between A and B

Skill matching is medium-strict: same concept tested in a different surface form. Not the same question. Not the same domain.

### Example that counts

Case-Based Preview: "Plant in dark closet vs plant by window — which grows more?" Student picks dark closet. Wrong.

Boss Arena: "Why does a plant need light to grow?" Student answers correctly.

System did not reveal the answer between A and B. Same concept, different shape. Counts as a fix.

### Example that does not count

Memory Check: "What does chlorophyll do?" Student answers wrong. System shows correct answer as feedback.

Boss Arena: same question. Student answers right.

This is recall, not repair. Does not count.

### Upstream requirements

Two things must exist for this metric to work:

1. **Skill tag on every question** across Case-Based Preview, Practice Arc, and Boss Arena. The current system has Bloom and PISA tags. A third concept/skill identifier needs to be added.
2. **Feedback-shown flag** between attempts. The system already shows feedback after wrong answers — this just needs to be made explicit as a flag Reflection can read.

If either is missing, the metric is unreliable.

---

## Addition 2 — Render Reflection as a fixed 3-beat narrative

### The 3 beats

1. **Where you started** — first significant failure in Case-Based Preview, framed as entry weak spot
2. **What you fixed** — mistakes repaired during the session (from Addition 1)
3. **Where to go next** — the existing next-step suggestion, made specific

### Example output

> You came in shaky on photosynthesis — your first Case-Based Preview decision picked the dark closet plant as the bigger grower. By Boss Arena you correctly explained why light is needed, even when the question was rephrased. Photosynthesis stuck. Cellular respiration is your next gap — try §23.

### Beat 2 fallback when no fixes happened

If the student got everything right first try, Beat 2 has no repair to report. Two fallback options:

- **Default:** replace Beat 2 with "what you got right first try" (strong points framed as confidence)
- **Alternative:** skip Beat 2, merge Beats 1 and 3 into a shorter Reflection

Recommend the default.

### Data source per beat

| Beat | Source |
|---|---|
| Where you started | First failed predict/choose action in Case-Based Preview |
| What you fixed | mistake_repair_count from Addition 1 |
| Where to go next | next-step suggestion (already in flow spec) |

The model narrates the data. It does not invent any of it.

---

## What this note does not cover

- BOST goal callback (considered, rejected)
- Pass/fail logic and retake rules (Section 16 already covers)
- Buzan anchor recap (Section 17 already covers)

---

## Summary

Two changes to Section 15 of the new flow:

1. Add tracked output **mistake_repair_count** with the medium-strict matching definition above. Requires skill tagging on every question and a feedback-shown flag between attempts.
2. Specify Reflection rendering as a fixed 3-beat narrative — started, fixed, next — with the empty-Beat-2 fallback rule.

The rest of Section 15 stays as written.
