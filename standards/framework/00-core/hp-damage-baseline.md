---
name: hp-damage-baseline
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §5.6 lines 1099-1240 | Matrix v0.4 Final Challenge table (lines 113-128)
---

# HP and Damage Baseline

## Mechanic

### HP Pools by Grade Band

| Grade Band | Boss HP |
|------------|---------|
| Grades 1–4 | 50 HP |
| Grades 5–8 | 100 HP |
| Grades 9–11 | 150 HP |

**Subject-specific override:**

| Subject | Grade Band | HP Override |
|---------|------------|-------------|
| Matematika | Grades 5–6 | 80 HP |

No other subject-specific HP overrides are defined. All other subjects inherit the grade-band defaults above.

### Damage Tiers

| Difficulty | Damage | PISA Level | Bloom's Level |
|------------|--------|------------|---------------|
| Easy | –10 HP | Level 3 | Apply |
| Medium | –20 HP | Level 4 | Analyze |
| Hard | –30 HP | Level 5–6 | Evaluate / Create |

### Question Distribution

```
Boss question set = {
  40% Easy   (at or below student's CURRENT PISA level — should get most right),
  40% Medium (at student's TARGET PISA level — the real test),
  20% Hard   (one level ABOVE target — challenge bonus, not required to win)
}
```

### Hint Tax

| Grade Band | Hint Cost |
|------------|-----------|
| Grades 1–4 | –5 HP (boss regains) |
| Grades 5–8 | –10 HP |
| Grades 9–11 | –15 HP |

### Combo Bonus

3 consecutive correct answers → 2× damage on the next question. Applies to all grade bands.

### Final Challenge Adaptive Format (by Lesson Archetype)

Source: Matrix v0.4 Final Challenge spec.

| Lesson Archetype | Format | HP Mechanic | Purpose |
|------------------|--------|-------------|---------|
| Concept Intro | Light checkpoint — one integrated problem, no combat framing | None | Closure, "you got it" |
| Algorithm | Standard boss — 3–5 questions, HP bar, tiered damage | Yes (grade-based HP) | Skill verification |
| Application | Standard boss — applied scenario with HP | Yes | Method-choice validation |
| Review | Full boss — max HP, all damage tiers, longest fight | Yes (+ checkpoint mid-boss) | Summative assessment |

Concept Intro checkpoints skip the HP mechanic entirely — completion, not combat.

### Boss Tiers (Sub / Big / Mythical)

All three boss types inherit this HP and damage table unless explicitly overridden:

| Boss Type | Trigger | Difficulty | Reward |
|-----------|---------|------------|--------|
| Sub Boss | End of every homework session (default) | Calibrated to student's PISA level | Standard XP + stars |
| Big Boss | Weekly (replaces that week's Sub Boss) | One tier above student's PISA level | 2× XP + weekly badge + streak freeze if > 80% |
| Mythical Boss | < 5% random chance per session | PISA L5–6 regardless of student level | 5× XP + exclusive title + avatar frame + Hall of Fame |

**Mythical Boss exceptions:** Zero hints. One attempt only. No HP penalty on failure.

### Failure Flow

```
IF boss NOT defeated (HP > 0 after all questions):
  1. IDENTIFY which learning objectives the student failed on
  2. MAP failures back to specific textbook sections and standards
  3. ACTIVATE Socratic Tutoring (Tier 3 AI) — TEFCAS framed:
     - "Hali emas!" (Not yet! — NEVER "Wrong" or "Noto'g'ri")
     - CHECK: "Keling, tekshiramiz — qayerda tushunmovchilik bor?"
     - ADJUST: "Buni boshqacha yondashsangiz nima o'zgaradi?"
     - AI asks guiding questions, NEVER gives answers directly
     - Routes student back to the SPECIFIC Story Mode / Preview segment
  4. REGENERATE boss questions (same standards, different numbers/context)
  5. Student re-attempts boss -> SUCCESS required to proceed

IF boss defeated:
  -> Proceed to Phase 7
  -> Calculate Mastery Stars
```

### Mastery Star Calculation

| Stars | Criteria | Unlocks |
|-------|----------|---------|
| 1 Star | Boss defeated (any number of attempts) | Chapter complete |
| 2 Stars | Boss defeated in ≤ 2 attempts, > 50% HP remaining | Bonus avatar item |
| 3 Stars | Boss defeated on FIRST attempt, no hints used, > 80% HP remaining | Special badge progress |

### Format Constraint: No Multiple Choice for Grade 5+

| Grade Band | Allowed Question Types |
|------------|----------------------|
| Grades 1–4 | Multiple choice + short answer |
| Grades 5–8 | Short answer + open reasoning (no MC) |
| Grades 9–11 | Open reasoning + extended response only |

Grade 5 exception: up to 30% MC allowed in Final Boss only (see CLAUDE.md framework rules).

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| G1–4 HP | 50 HP | Default |
| G5–8 HP | 100 HP | Default |
| G9–11 HP | 150 HP | Default |
| Matematika G5–6 HP | 80 HP | Subject override |
| Easy damage | –10 HP | PISA L3 / Bloom Apply |
| Medium damage | –20 HP | PISA L4 / Bloom Analyze |
| Hard damage | –30 HP | PISA L5–6 / Bloom Evaluate/Create |
| Easy distribution | 40% | At/below current PISA |
| Medium distribution | 40% | At target PISA |
| Hard distribution | 20% | Above target PISA |
| Hint tax G1–4 | –5 HP | Boss regains |
| Hint tax G5–8 | –10 HP | Boss regains |
| Hint tax G9–11 | –15 HP | Boss regains |
| Combo threshold | 3 consecutive correct | Next hit = 2× damage |
| Mythical Boss trigger | < 5% random | Per session |
| Mythical Boss hints | 0 | No hints, no Socratic |
| Mythical Boss attempts | 1 | One attempt only |
| Skippable | Never | Zero exceptions |

## Scope

Applies to Phase 6 (Final Challenge) in all sessions where the lesson archetype is Algorithm, Application, or Review. Concept Intro archetype activates light checkpoint format with no HP mechanic.

## Cross-references

- `difficulty-adaptation.md` — initial difficulty tier drives the 40/40/20 question set composition
- `routing-algorithm.md` — Phase 6 score (derived from HP outcome) contributes 30% to overall_score_pct
- `variant-generator.md` — regenerated boss questions on failure follow variant generation rules (same Bloom/PISA, different numbers)

## Verification

1. Grade 6 Matematika session: confirm HP initializes to 80, not 100.
2. Grade 8 session: serve 5 questions (2 easy, 2 medium, 1 hard). Confirm max possible damage = 20+20+40+40+30 = 150 (with combo on question 5 if earned).
3. Concept Intro lesson: confirm Phase 6 renders light checkpoint, HP bar absent.
4. Student uses hint in Grade 9: confirm boss HP increases by 15 (hint tax).
5. Boss defeated first attempt, no hints, 85% HP remaining: confirm 3 stars awarded.
