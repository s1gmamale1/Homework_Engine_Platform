---
name: item-tier-distribution
status: v0.1 draft — validated against §22 only
layer: 4 (difficulty)
source: UNIFIED §5.6 lines 1099-1240 + 00-core/hp-damage-baseline.md
---

# Item Tier Distribution

HP values and damage numbers live in `00-core/hp-damage-baseline.md`. This file documents only the **distribution ratios** and **Bloom target mappings** per tier, and how they shift by grade band.

---

## Standard Distribution (All Grade Bands, Sub Boss)

Applies to every Final Challenge / Boss encounter unless a boss-tier override applies (see Big Boss and Mythical Boss in `00-core/hp-damage-baseline.md`).

| Tier | Share | PISA Calibration | Bloom's Level |
|------|:-----:|------------------|---------------|
| Easy | 40% | At or below student's CURRENT PISA level | L2–L3 (Understand / Apply) |
| Medium | 40% | At student's TARGET PISA level | L3–L4 (Apply / Analyze) |
| Hard | 20% | One level ABOVE target — challenge bonus | L4–L6 (Analyze / Evaluate / Create) |

> The Easy tier is designed so students should get most right. The Medium tier is the real test. The Hard tier is a challenge bonus — students are not required to clear it to defeat the boss.

---

## Bloom Target by Tier and Grade Band

Bloom targets tighten as grade band rises. The tier proportions (40/40/20) remain constant; the absolute Bloom level shifts.

| Tier | G1–4 | G5–8 | G9–11 |
|------|------|------|-------|
| Easy | L1–L2 (Remember / Understand) | L2–L3 (Understand / Apply) | L3 (Apply) |
| Medium | L2–L3 (Understand / Apply) | L3–L4 (Apply / Analyze) | L4–L5 (Analyze / Evaluate) |
| Hard | L3–L4 (Apply / Analyze) | L4–L6 (Analyze / Evaluate / Create) | L5–L6 (Evaluate / Create) |

---

## Question Format Constraints by Grade Band

| Grade Band | Easy tier | Medium tier | Hard tier |
|------------|-----------|-------------|-----------|
| G1–4 | MC or short answer | MC or short answer | MC or short answer |
| G5–8 | Short answer (no MC) | Short answer + open reasoning | Open reasoning |
| G9–11 | Open reasoning | Open reasoning | Extended response |

Grade 5 exception: up to 30% MC in Final Challenge Easy-tier questions only.  
Full format constraint table: `00-core/hp-damage-baseline.md § Format Constraint`.

---

## Sample Question Count by Boss HP

These are reference counts for the most common HP pools. Actual question count is not fixed by spec — agents select items to fill the 40/40/20 ratio. Counts below illustrate a minimal viable set.

| HP Pool | Total Qs (min viable) | Easy (40%) | Medium (40%) | Hard (20%) |
|---------|-----------------------|:----------:|:------------:|:----------:|
| 50 HP | 5 | 2 | 2 | 1 |
| 80 HP (Mat G5-6) | 5 | 2 | 2 | 1 |
| 100 HP | 5–7 | 2–3 | 2–3 | 1 |
| 150 HP | 7–10 | 3–4 | 3–4 | 1–2 |

> A student who answers all questions correctly without hints reaches 0 HP and defeats the boss. Combo bonus (3 consecutive correct → 2× next damage) can accelerate defeat.

---

## Lesson Archetype Overrides

Distribution stays 40/40/20 across archetypes, but the boss format changes:

| Archetype | Final Challenge Format | HP Mechanic |
|-----------|----------------------|:-----------:|
| Concept Intro | Light checkpoint — one integrated problem | None |
| Algorithm | Standard boss — 3–5 questions, HP combat | Yes |
| Application | Standard boss — applied scenario | Yes |
| Review | Full boss — max HP, all damage tiers | Yes |

Concept Intro checkpoints skip HP combat entirely. No tier distribution applies to light checkpoints.

---

## Cross-references

- `00-core/hp-damage-baseline.md` — HP pools, damage values, hint tax, combo bonus, mastery star thresholds
- `04-difficulty/per-family-difficulty.md` — HP overrides by family and grade band
- `04-difficulty/phase-weights.md` — How Boss phase score contributes to overall session score
