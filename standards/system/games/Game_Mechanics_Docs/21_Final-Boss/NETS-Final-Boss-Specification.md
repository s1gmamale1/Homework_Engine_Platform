# NETS Final Boss — Game Mechanic Specification

**v1.1 — 2026-04-12** | Layer 0 Mechanic #14 | Phase 6: Assessment Gate | Constitution: UNIFIED v2.0

---

## The 3 Boss Types

| Boss | Trigger | Scope | Difficulty | Hints | Attempts | Reward |
|------|---------|-------|------------|-------|----------|--------|
| **Sub Boss** | Every homework session | Current lesson only | Calibrated to PISA level | Yes (costs HP) | Basic: **2 max** / Premium: unlimited | 500-1000 XP + stars |
| **Big Boss** | Weekly | Cross-subject, weakest 3 standards | One PISA tier harder | Yes (costs HP) | **1 default** (extendable via bonuses, TBD) | 2x XP + badge + streak freeze if >80% |
| **Mythical Boss** | Random event / easter egg / bonus credits (Basic) / Mystery Box (Premium) | All completed subjects | PISA L5-6 regardless | **ZERO** | **ONE** | 5x XP + title + frame + Hall of Fame |

### Mythical Boss Access

| Tier | Access |
|------|--------|
| Basic | Random events / easter eggs + **purchasable with bonus credits** |
| Premium | Random events / easter eggs + **Mystery Box drops**. Weekly limit (TBD). |

> **Spec divergence note:** UNIFIED v2.0 defines Mythical as "<5% random, cannot be farmed." This spec adds bonus credit purchase (Basic) and Mystery Box triggers (Premium). Requires ADR update to Layer 0.

---

## Tier Overlay (Basic vs Premium)

| Dimension | Basic | Premium |
|-----------|-------|---------|
| **Content source** | Textbook-level only (national curriculum) | Textbook + extra materials (L2-L4 extended content) |
| **Difficulty** | Standard — calibrated to student's PISA within textbook scope | AI adjusts harder than textbook with supplementary materials |
| **Sub Boss attempts** | **2 max.** Both fail → homework marked FAILED → Duolingo Mode activates | **Unlimited.** Questions regenerate each attempt |
| **Big Boss attempts** | **1 default** (extendable via bonuses, TBD) | Same |
| **Mythical Boss** | Random/easter egg + **bonus credits** | Random/easter egg + **Mystery Box drops** (weekly limit) |
| **AI evaluation** | Tier 1 (rule-based) + Tier 2 (LLM for open reasoning) | Tier 1 + Tier 2 + **Tier 3 (deep Socratic tutoring on failure)** |
| **Socratic tutoring** | Tier 2 — guided hints from stored arrays + basic LLM | Tier 3 — personalized AI tutoring, references specific textbook pages, cause/effect framing |
| **Question format** | Same as Premium (no MC for G6+ applies to both) | Same (Layer 0 locked) |
| **Boss HP** | Same (50/100/150 by grade) | Same |
| **Duolingo Mode** | Active (always) | Active (always) |

### Basic Tier: Sub Boss Failure Flow

```
Attempt 1: Student faces boss. If HP > 0 after all questions → FAIL.
  → Socratic tutoring (Tier 2). Questions regenerated.
Attempt 2: Student re-attempts with fresh questions. If HP > 0 → FAIL.
  → Homework marked FAILED.
  → Duolingo Mode activates: task-by-task review, adjusted difficulty, repeat until 60%.
  → Teacher auto-flagged after 3 failed sessions on same topic.
  → No further boss attempts for this session.
```

### Premium Tier: Sub Boss Failure Flow

```
Attempt N: Student faces boss. If HP > 0 → FAIL.
  → Socratic tutoring (Tier 3 — deep, personalized, textbook-referenced).
  → Questions regenerated (same standards, different numbers/context).
  → Student re-attempts. Unlimited until boss defeated.
  → Duolingo Mode still activates if overall session < 60%.
```

---

## HP & Damage

| Grade Band | HP | Hint Cost | Question Format |
|-----------|-----|-----------|-----------------|
| Grades 1-4 | 50 | +5 HP to boss | MC + short answer |
| Grade 5 | 100 | +10 HP | Mixed (30% MC allowed, ADR-005) |
| Grades 6-8 | 100 | +10 HP | Open reasoning only, no MC |
| Grades 9-11 | 150 | +15 HP | Extended response, proofs, essays |

| Difficulty | Damage | PISA | Bloom's |
|-----------|--------|------|---------|
| Easy | -10 HP | L3 | Apply |
| Medium | -20 HP | L4 | Analyze |
| Hard | -30 HP | L5-6 | Evaluate/Create |

### Question Distribution by Tier

| Tier | Easy | Medium | Hard | Source |
|------|------|--------|------|--------|
| **Basic** | 45% | 40% | 15% | Textbook content only (L1) |
| **Premium** | 35% | 40% | 25% | Textbook + extended materials (L1-L2+) |

```
Combo: 3 consecutive correct = next answer deals 2x damage
Hint/wrong answer resets combo to 0
Min pool: 15 boss questions per topic (5 easy / 5 medium / 5 hard)
Premium pool: 20+ (additional questions from extended materials)
```

---

## Answer Evaluation (Dual Pathway)

| Type | Method | Latency | Fallback |
|------|--------|---------|----------|
| Hardcoded (MC, numeric) | Rule-based exact match | <0.1s | N/A |
| Open reasoning (typed) | Tier 2 LLM vs rubric | <3s (5s timeout) | Keyword matching |

| Evaluation Feature | Basic | Premium |
|-------------------|-------|---------|
| Rule-based scoring (Tier 1) | Yes | Yes |
| LLM evaluation (Tier 2) | Yes (open reasoning) | Yes |
| Deep Socratic tutoring (Tier 3) | No — stored hint arrays + Tier 2 | Yes — personalized, textbook-referenced |
| Partial credit | Yes (both tiers) | Yes |
| AI feedback sentence | Generic | Personalized to student's error pattern |

```
Partial credit: 90-100% = full damage | 50-89% = half damage | <50% = 0 damage
AI never reveals correct answer. Only scores + one-sentence feedback.
```

---

## Hints (Sub & Big Boss only)

```
3 progressive hints per question: vague → specific → directed
Each hint: boss REGAINS HP (-5/-10/-15 by grade band)
Socratic method: guide to discover, never reveal answer

Basic: Hints from stored socratic_hints arrays (pre-written per question)
Premium: Hints from Tier 3 AI — dynamically generated based on student's specific error

Mythical Boss: ZERO hints for both tiers. No scaffolding. Raw challenge.
```

---

## Failure & Scoring

### Sub Boss Failure

| Tier | Attempt 1 Fail | Attempt 2 Fail | Beyond |
|------|---------------|---------------|--------|
| **Basic** | Socratic tutoring (Tier 2) → regenerate → retry | **Homework FAILED** → Duolingo Mode | No more attempts this session |
| **Premium** | Socratic tutoring (Tier 3) → regenerate → retry | Socratic → regenerate → retry | Unlimited until defeated |

### Big Boss Failure

```
1 attempt default (both tiers).
Fail → Weak standards persist into next week's Big Boss.
Extendable via bonuses (mechanism TBD).
```

### Mythical Boss Failure

```
"The Mythical Boss retreats... for now."
Small participation XP. No penalty. No re-attempt.
Basic: Proceeds to normal Sub Boss.
Basic: Can trigger another via bonus credits.
Premium: Can encounter another via Mystery Box (within weekly limit).
```

### Mastery Stars

| Stars | Criteria | XP (Sub / Big / Mythical) |
|-------|---------|--------------------------|
| 1 Star | Boss defeated (any attempts) | 500 / 1000 / — |
| 2 Stars | ≤2 attempts, >50% HP remaining | 700 / 1400 / — |
| 3 Stars | First attempt, no hints, >80% HP | 1000 / 2000 / — |
| Mythical | Defeated = flat reward | — / — / 5000 + title + frame |

### Duolingo Mode (Always Active, Both Tiers)

```
Triggers when: session score < 60% OR Basic Sub Boss fails both attempts
1. Immediate feedback: "You scored X%. Let's work on what you missed."
2. Task-by-task review with scaffolding
3. Adjusted difficulty: one tier lower
4. Repeat until 60%
5. Teacher flagged after 3 failed sessions on same topic
6. No XP until crossing 60%
```

---

## Subject Family Variations

| Family | Boss Format | AI Tier | Basic vs Premium |
|--------|------------|---------|-----------------|
| **Aniq Fanlar** (Math, Physics, Chem) | Open derivation/numeric. Partial credit. | Tier 1 + Tier 2 | Basic: textbook problems. Premium: extended (Kirchhoff, limits, etc.) |
| **Til Fanlari** (Languages) | Writing production. G5: guided. G6+: free. G9+: extended. | Tier 2 | Basic: curriculum writing tasks. Premium: IELTS/CEFR-level prompts. |
| **Tabiat Fanlari** (Bio, Geo) | "Describe/explain why" + Notebook Capture. | Tier 2 | Basic: textbook processes. Premium: experimental design, modeling. |
| **Ijtimoiy Fanlari** (History, Law) | Case reasoning + source excerpts. | Tier 2 | Basic: single-source analysis. Premium: multi-source, historiography. |
| **Tarbiya/Sanat** (Art, PE) | Optional formative prompt. **No scoring.** | None | Same both tiers (no competitive pressure). |

---

## Anti-Cheat

```
1. Question Regeneration — fresh questions every attempt
2. Response Time Analysis — faster than reading pace = flag
3. Session Pattern Analysis — perfect Hard + fail Easy = flag
4. Socratic Verification — 1 follow-up after defeat (not scored, flagged if failed)
5. Copy-Paste Detection — paste events flagged
6. Radiance Score — AI checks authentic vs copied patterns (0.0-1.0)
Escalation: Flag 1 soft warn → Flag 2 parent → Flag 3 teacher → Flag 4 admin
```

---

## Buzan Cognitive Science Integration

### TEFCAS Cycle

The Final Boss is the **ultimate Trial** in TEFCAS:

| Stage | Boss Moment |
|-------|-------------|
| **Trial** | Student faces question and attempts answer |
| **Event** | HP bar changes, damage animation plays |
| **Feedback** | Socratic hint (never reveals answer); IRT adjusts difficulty estimate |
| **Check** | IRT compares theta (proficiency) vs item difficulty |
| **Adjust** | Next question adapts to maintain flow zone (70-80% success) |
| **Success** | Boss defeated → XP, stars, celebration |

On failure: *"Hali emas! Miyangiz hozir Feedback oldi. Bilim Bazasiga qarang — qaysi tarmoqqa yangi 'Adjust' chizig'i kerak?"*

### MIG (Memory Graph)

| Effect | Boss Implementation |
|--------|---------------------|
| **Primacy** | Phase 5 locks concepts BEFORE boss — primacy reset at phase boundary |
| **Recency** | Boss is Phase 6 (near session end) — highest recall. Phase 7 captures insights. |
| **Association** | Boss questions link to Story Mode narratives from Phase 2. |
| **Von Restorff** | Boss defeat/failure = most emotionally unique moment. Dramatic animations = deep encoding. |
| **The Sag** | 7-phase structure resets curves multiple times. No sag by Phase 6. |

### Memory Systems

| System | Application |
|--------|------------|
| **Link System** | Boss questions follow causal chains from earlier phases |
| **Memory Palace** | Phase 5 places concepts in Registan Square. Boss tests retrieval from those loci. |
| **SMASHIN' SCOPE** | Failure animations: Synaesthesia (impact sound), Movement (HP shake), Exaggeration (screen flash) |

### BOST Review Intervals (Post-Boss)

| Interval | NETS Mapping |
|----------|-------------|
| 10 min | Phase 5 + Phase 7 within same session |
| 24 hours | Next day's Phase 1 Memory Sprint includes boss-related recall |
| 1 week | Big Boss targets that week's Sub Boss failures |
| 1 month | Champion's Arena / spaced repetition |

### Mind Mapping

```
Pre-Boss (Phase 5): Radiant Summary — review Mind Map of session concepts
Post-Boss (Phase 7): Reflect on strong/weak branches. AI highlights gaps.
Big Boss: Cross-subject Mind Map — weakest 3 standards as branches.
```

---

## Edge Cases

```
Catch-Up Mode (>7 days absent): Boss HP reduced 50%, hints free (both tiers)
Recovery Session: Boss unchanged — full assessment integrity
AI down: Fallback to Tier 1 keyword matching. Session never terminates.
Mythical + Recovery: Mythical suppressed (both tiers)
Teacher HP modifier: 50%-150% range. Custom boss questions allowed.
Basic 2-attempt limit + Catch-Up: Still 2 attempts, but HP at 50% makes it easier.
```

---

## Locked Constraints (Layer 0)

3-tier boss system | HP 50/100/150 | No MC for G6+ | Non-skippable | Mandatory `transition_skill` tag | 60% pass floor | Hidden difficulty labels | No pay-to-win (Basic gets full educational mission) | Textbook traceability | Phase 6 always | Duolingo Mode always active
