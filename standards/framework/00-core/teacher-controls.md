---
name: teacher-controls
status: v0.1 draft — validated against §14 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §14 (lines 3110-3141)
---

# Teacher Controls

## Rules / Capabilities

Teachers can configure per class or per student:

| Control | Default | Range |
|---|---|---|
| Session mode | Standard (20-30 min) | Standard / Extended (40-50 min) |
| Grace period for missed homework | 3 days | 1-7 days |
| Final Boss HP modifier | 100% | 50%-150% |
| Hint availability | Enabled (with XP cost) | Enabled / Disabled |
| Phase 4 (Real-Life Challenge) | Required | Required / Optional |
| Minimum reflection length | 10 characters | 10 chars - 5 sentences |
| Difficulty floor | Student's PISA level - 1 | Configurable |
| Game mechanic selection | Automatic | Auto / Manual selection |
| Recovery sessions per day | 2 max | 1-3 |
| Mandatory vs optional homework | Mandatory | Mandatory / Optional |
| Creative Lab availability | Auto (Level 3+) | Enabled / Disabled |

### Teacher Dashboard Features

| Feature | Description |
|---|---|
| Heat Map | Per-student, per-chapter, per-standard mastery visualization |
| Deadline Controls | Set, extend, or waive homework deadlines |
| Custom Assignments | Create assignments using NETS game engine (tagged to standards) |
| Custom Boss Questions | Create boss questions tagged to standards |
| Difficulty Override | Override AI difficulty for specific students |
| Excused Marking | Remove homework from recovery queue |
| Class Insights | Which textbook sections need classroom reinforcement (class-wide weak standards) |
| Engagement Alerts | Students with declining completion or performance |

## Scope

All controls apply at the class level by default; any control can be narrowed to a specific student. Controls modify runtime behavior only — they do not alter the underlying phase structure or PISA gating rules. Final Boss HP modifier stacks multiplicatively with grade-band base HP (see UNIFIED §4.6).

## Cross-references

- §12.1 Edge Cases — grace period default (3 days) is set here; range 1-7 days
- §12.2 Edge Cases — recovery sessions per day cap (default 2, range 1-3)
- §12.6 Edge Cases — Excused Marking removes homework from recovery queue
- §13 Anti-Cheat — teacher notification at Flag 3 of escalation sequence
- §15.1 Kundalik/eMaktab — deadline controls feed assignment sync

## Verification

- Default grace period = 3 days; must match §12.1
- Final Boss HP modifier range = 50%-150% (not a flat HP override)
- Recovery sessions per day default = 2; configurable range = 1-3
- Difficulty floor default = Student's PISA level - 1
- Creative Lab default = Auto (Level 3+), not always-on or always-off
