---
name: anti-cheat
status: v0.1 draft — validated against §13 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §13 (lines 3064-3108)
---

# Anti-Cheat System

## Rules / Capabilities

```
SYSTEM-WIDE INTEGRITY CHECKS:

1. Question Regeneration: Boss questions regenerated on every attempt
   (same standard + PISA level, different numbers/context)

2. Response Time Analysis: Answers faster than reading speed -> flagged
   (calibrated per student's established reading pace)

3. Session Pattern Analysis: Unusual completion patterns -> flagged
   (e.g., perfect scores on hard questions but failures on easy ones)

4. Socratic Verification: After boss defeat, 1 follow-up question
   to verify understanding (not scored, but flagged if failed)

5. Device Monitoring: Same account on multiple devices -> session locked

6. Copy-Paste Detection: Paste events in text fields -> flagged

7. Radiant Signature Analysis (Buzan) — PENDING EMPIRICAL VALIDATION:
   Concept: Open-text responses checked for "radiant" vs "linear" patterns
   to detect AI-generated or copy-pasted answers.
   STATUS: NOT DEPLOYED. Requires validation before shipping:
   - Collect 500+ real G5-6 student responses across subjects
   - Label them human vs AI-generated
   - Train classifier and measure precision/recall
   - SHIP GATE: precision must be >= 90%. If not, feature does not ship.
   - RISK: Students explaining sequential processes (water cycle, timelines)
     naturally produce linear text — not because they're cheating.
     False positive rate for systematic thinkers may be unacceptable.
   - If validation passes, scope is: Phase 4 + Peer Teaching open-text only
   - NOT applied to: MC, drag-and-drop, closed-format, Math, Language grammar

ESCALATION:
  - Flag 1: Soft warning to student ("Make sure you're solving these yourself!")
  - Flag 2: Parent notification
  - Flag 3: Teacher notification with evidence log
  - Flag 4: Account-level review (admin)
```

## Scope

Checks 1-6 are system-wide and apply to all phases, all grades, all subjects. Check 7 (Radiant Signature Analysis) is NOT deployed — it must not be referenced as an active feature until the ship gate (precision >= 90%) is cleared. Escalation flags are cumulative within a session or rolling window (implementation detail TBD).

## Cross-references

- §4.6 Phase 6 Final Boss — question regeneration on every attempt (Check 1)
- §14 Teacher Controls — teacher notification is Flag 3 in escalation sequence
- §15.2 Parent Dashboard — parent notification is Flag 2 in escalation sequence
- §15.3 Admin/National Analytics — Flag 4 (account-level review) routes to admin

## Verification

- Boss questions must regenerate on every attempt with same standard + PISA level
- Response time thresholds are per-student (not global fixed values)
- Radiant Signature Analysis status = NOT DEPLOYED; ship gate = precision >= 90%
- Escalation sequence is ordered: student → parent → teacher → admin
- Socratic Verification follow-up is not scored, only used for flagging
