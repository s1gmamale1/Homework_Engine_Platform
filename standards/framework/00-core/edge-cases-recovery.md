---
name: edge-cases-recovery
status: v0.1 draft — validated against §12 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §12 (lines 2982-3060)
---

# Edge Cases & Recovery

## Rules / Capabilities

### 12.1 Missed Homework (Within Grace Period)

```
Grace period: 3 days (teacher-configurable, range 1-7 days)

RECOVERY SESSION (condensed, 15-20 min):
  - Phase 1: EXTENDED Memory Sprint (3 min, 10 questions -- more decay to recover)
  - Phase 2: Condensed Story Mode (key segments only, ~3 min)
  - Phase 3: 1 game break only (2-3 min)
  - Phase 4: SKIPPED (time constraint)
  - Phase 5: Quick flashcard review only (1 min)
  - Phase 6: Full Final Boss (NO shortcuts -- assessment integrity maintained)
  - Phase 7: Shortened reflection (1 prompt)
```

### 12.2 Multiple Missed Sessions

```
IF missed_count > 1:
  1. SORT missed sessions by DEPENDENCY (prerequisites first)
  2. ASSIGN recovery sessions in dependency order
  3. Each recovery session is condensed (see 12.1)
  4. Maximum 2 recovery sessions per day (prevent burnout)
  5. Teacher dashboard shows recovery queue and estimated completion date
```

### 12.3 Extended Absence — Catch-Up Mode

```
IF absence > 7 days:
  ACTIVATE Catch-Up Mode:
  - AI identifies ESSENTIAL concepts only (prerequisite chain analysis)
  - Non-essential topics deferred until caught up
  - Final Boss: reduced HP (50% of normal), hints allowed without penalty
  - EXIT condition: student completes sessions to within 1 of class position
  - Teacher notified with specific in-class support recommendations
  - Maximum 2 catch-up sessions per day
```

### 12.4 Boost Mode (Falling Behind)

```
IF student_pisa_level < class_average - 0.5 for 3+ consecutive sessions:
  ACTIVATE Boost Mode:
  - Additional optional practice sessions (incentivized with bonus XP + special avatar items)
  - Targeted to specific weak standards and transition skills
  - AI generates personalized improvement plan
  - Parent notified with home support recommendations
  - Teacher receives specific intervention recommendations
  - Auto-deactivate when student reaches class average
```

### 12.5 Low Engagement Intervention

```
IF completion_rate < 50% for 2 consecutive weeks:
  RESPONSE SEQUENCE:
  1. Reduce session length to minimum (15 min)
  2. Increase game-to-content ratio (more Game Breaks, shorter Story Mode)
  3. Re-engage with Quest Arc narrative hooks
  4. Parent notification with specific suggestions
  5. Teacher dashboard flag with engagement data
```

### 12.6 Force Majeure / Technical Failures

```
OFFLINE MODE:
  - Pre-cache current chapter + next chapter content
  - Session auto-save: resume from last checkpoint on reconnection
  - Device-agnostic: session state syncs across devices

TEACHER OVERRIDE:
  - "Excused" marking: manual override for technical issues
  - Removes homework from recovery queue
  - Does not affect PISA tracking or mastery calculations
```

## Scope

Applies to all students across all grades and subjects. Recovery session structure (§12.1) overrides standard session structure only when the recovery flag is active. Boost Mode and Catch-Up Mode can be active simultaneously.

## Cross-references

- §14 Teacher Controls — grace period configuration, recovery sessions per day limit, excused marking
- §15.1 Kundalik/eMaktab — completion status push (missed/in-progress)
- §15.2 Parent Dashboard — parent notification triggers (§12.4, §12.5)
- §4.6 Phase 6 Final Boss — assessment integrity rule applies even in recovery sessions

## Verification

- Grace period default = 3 days; confirm teacher-configurable range is 1-7 days
- Recovery session Phase 4 must be SKIPPED (not shortened)
- Catch-Up Mode Final Boss HP = 50% of normal (not a flat value)
- Boost Mode auto-deactivates when student_pisa_level reaches class_average
- Max recovery sessions per day: 2 (§12.2 and §12.3 both enforce this cap)
