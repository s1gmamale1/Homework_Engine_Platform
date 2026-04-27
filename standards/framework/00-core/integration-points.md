---
name: integration-points
status: v0.1 draft — validated against §15 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §15 (lines 3143-3186)
---

# Integration Points

## Rules / Capabilities

### 15.1 Kundalik/eMaktab

```
PULL from Kundalik:
  - Class rosters (student list per class)
  - Attendance data (feeds into absence detection)
  - Timetable (homework assigned per subject schedule)

PUSH to Kundalik:
  - Homework completion status (complete / in-progress / missed)
  - Grade equivalent (1-5 scale, derived from boss performance)
  - Completion timestamp
```

### 15.2 Parent Dashboard

```
PARENT PORTAL FEATURES:
  - PISA level progression chart (over time, per subject)
  - Subject performance breakdowns
  - Homework completion rates
  - Weak standards with home support recommendations (specific, actionable)
  - AI-generated home support recommendations
  - Weekly summary (platform notification or SMS for parents without app)

PRIVACY:
  - Reflection Journal content NOT shared (teacher and parent see themes only)
  - Individual question-level data available only to teacher
```

### 15.3 Admin/National Analytics

```
AGGREGATE (anonymized):
  - Per-school average PISA levels by subject
  - Per-region standard mastery rates
  - National content gap analysis (which standards are weakest nationwide)
  - Textbook effectiveness metrics (which chapters have lowest mastery rates)
  - Creative Thinking domain progress (national aggregate)
```

## Scope

§15.1 covers the primary school-system sync (Kundalik/eMaktab is Uzbekistan's national grade book and attendance platform). §15.2 covers the parent-facing portal. §15.3 covers anonymized aggregate data for MoE/national-level reporting across 8.8M students. No individual student data is exposed at the §15.3 level.

## Cross-references

- §12.3 Edge Cases — attendance data pulled from Kundalik feeds absence detection for Catch-Up Mode
- §12.4 Edge Cases — parent notification (Boost Mode) surfaces via §15.2 Parent Dashboard
- §12.5 Edge Cases — parent notification (low engagement) surfaces via §15.2 Parent Dashboard
- §13 Anti-Cheat — escalation Flag 4 (account-level review) routes to admin layer (§15.3 admins)
- §14 Teacher Controls — deadline controls and custom assignments feed §15.1 Kundalik push

## Verification

- Kundalik PULL includes: rosters, attendance, timetable (3 data types only)
- Kundalik PUSH includes: completion status, grade equivalent (1-5), timestamp (3 fields only)
- Reflection Journal content must NOT be shared with parents or teachers — themes only
- Individual question-level data is teacher-only; not exposed to parents or national analytics
- §15.3 data is anonymized aggregate — no individual student identifiers at national level
