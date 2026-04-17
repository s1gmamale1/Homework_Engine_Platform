### 5.1 Phase 1 -- Memory Sprint (2 minutes)


**Purpose:** Warm up the student's brain for the CURRENT chapter's homework. Activate relevant schemas, preview key terminology, and build readiness for the concepts about to be learned. Deliver quick dopamine to energize the session start.

**UPDATED 2026-04-15:** Memory Sprint now targets the CURRENT chapter, not prior chapters. The student has already seen the Theme Preview (0-A) and Flash Cards (0-B) — Memory Sprint is the first active engagement with the current topic's key terms, concepts, and prerequisite connections. Prior-chapter spaced repetition is handled by the platform's adaptive review system outside of homework sessions.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | ≤2 minutes (hard cap) | ≤2 minutes |
| Item count | 5-8 items | 8-10 items |
| Source | **Current chapter** — key terms, prerequisite concepts, foundational facts needed for this session | Same |
| Format | **Tap-only — 3 approved formats ONLY (MC, T/F, YNNG — see table below). NO typing, NO drag-and-drop.** | Same |
| Hints allowed | No | No |
| AI Tier | Tier 1 (pre-generated pool) | Same |

**Approved Memory Sprint Formats (3 ONLY):**

| Format | Description | Best For |
|---|---|---|
| **Multiple Choice** | 4 options, single correct answer. Tap to select. Basic concept checks, formula recognition, terminology. | All subjects |
| **True / False** | Statement displayed, student taps True or False. Fact verification, rule checks, common misconception busters. | All subjects |
| **Yes / No / Not Given** | IELTS-lite warm-up style. Statement presented, student selects Yes, No, or Not Given based on chapter content. Lighter than full IELTS — tests whether the student read/absorbed the material. | All subjects |

**Hard format restrictions:**
- **NO manual typing.** All answers are tap-to-select. No keyboard input.
- **NO open-ended questions.** No "explain why" or "describe how."
- **NO drag-and-drop.** No matching, no ordering, no rearranging.
- **Tap-only interaction.** Student reads → taps one option → gets instant feedback. That's it.

**Content scope:** Items must be basic warm-up questions — simple concept checks, formula recall, terminology recognition, translation between representations. This is a warm-up, not an assessment. Questions should not overwhelm — they should activate prior knowledge and build confidence.

**Format Selection Rule:** Content creator chooses from the 3 approved formats above. All items must have a Start button, instant per-item feedback, streak/combo bonuses, and a final score display. Mixing formats within a single Sprint is permitted (e.g., 3 MC + 2 T/F + 2 YNNG).

**Item Selection Algorithm:**
```
1. GET key concepts, terms, and prerequisite facts from the CURRENT chapter
2. PRIORITIZE by session relevance:
   - Core terminology the student will encounter in Story Mode (Phase 2) -> highest priority
   - Prerequisite concepts from earlier chapters needed to understand current topic -> high priority
   - Key formulas, rules, or definitions introduced in this chapter -> medium priority
3. FILTER to 5-8 items, balanced across the chapter's main concepts
4. RANDOMIZE order
```

**Buzan Injection — Primacy Effect:** Phase 1 is the Primacy window — recall is highest at the start of a session. This is why the most important current-topic items go here — the brain is primed to encode what it sees first. The Link Chain format adds Buzan's Link System mnemonic to the format options.

**Not applied here:** Radiant Thinking, Peg System, Major System — these require encoding time (45-90s) and don't fit the 2-minute hard cap. Memory Sprint is for rapid activation, not deep encoding.

**Scoring:**
- Correct: +100 XP per question
- Streak bonus: +10 XP x current_streak
- Speed bonus: +10 XP if answered in <5 seconds
- No penalty for wrong answers (this is warm-up, not assessment)
- Results feed back into the spaced repetition model

**Adaptation Rules:**
```
IF accuracy >= 80% -> Student ready for new content
IF accuracy 60-79% -> Proceed but flag for teacher review
IF accuracy < 60%  -> System routes to remediation BEFORE new content
```

**Standards Reference:** Every recall item displays its standard code in the review screen: `UZ-MATH-5-NATNUM-03 -- Natural sonlarni yaxlitlash`

*Source: Both specs aligned. XP values from HOMEWORK_STANDARDS.md (100 XP per correct) used over original spec (10 XP) because they better support the gamification economy.*