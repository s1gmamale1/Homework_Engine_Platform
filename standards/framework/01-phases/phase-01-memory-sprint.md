---
name: Phase 1 — Memory Sprint
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.1 (lines 629-694) + §22 session
---

# Phase 1 — Memory Sprint

## Purpose (WHAT)

Light warm-up that activates prior knowledge and builds readiness for the current chapter's concepts — NOT real practice (that is Phase 3). Delivers quick dopamine to energize session start while priming the schemas the student will need for Story Mode.

## Structure (HOW)

**Item count:** 5–7 items (Standard Mode). See Adaptable parameters for overrides.

**Duration:** ≤2 minutes hard cap. No extensions.

**3 approved formats — ONLY these:**

| Format | Description | Best For |
|--------|-------------|----------|
| **Multiple Choice** | 4 options, single correct answer. Student taps to select. Basic concept checks, formula recognition, terminology. | All subjects |
| **True / False** | Statement displayed, student taps True or False. Fact verification, rule checks, common misconception busters. | All subjects |
| **Yes / No / Not Given** | IELTS-lite style. Statement presented, student selects Yes, No, or Not Given based on chapter content. Tests whether the student absorbed the material. | All subjects |

**Format mixing rule:** Each sprint must use ≥2 of the 3 approved formats. A sprint of 7 all-MC items is a spec violation. A sprint mixing 3 MC + 2 T/F + 2 YNNG is valid.

**Hard format restrictions — BANNED in this phase:**
- NO manual typing. All answers are tap-to-select. No keyboard input.
- NO open-ended questions. No "explain why" or "describe how."
- NO drag-and-drop. No matching, ordering, or rearranging.
- NO fill-in-blank. No gap-fill.
- NO hints. Hints are not available at any point in Phase 1.
- Tap-only interaction: student reads → taps one option → gets instant feedback. That is the complete interaction.

**Content scope:** Current chapter recognition only. Items must target key terms, prerequisite concepts, and foundational facts from the current chapter — the concepts the student just encountered in Theme Preview (0-A) and Flash Cards (0-B). No forward leaks to content not yet covered. No items from previous chapters (spaced repetition is handled by the platform's adaptive review system outside of homework sessions).

**Notebook Capture:** Not applicable to Phase 1. All items are recognition-level (Bloom L1–L2) — no calculation, no derivation, no complex reasoning. There is nothing to capture.

**Item selection algorithm:**
```
1. GET key concepts, terms, and prerequisite facts from CURRENT chapter
2. PRIORITIZE by session relevance:
   a. Core terminology the student will encounter in Story Mode (Phase 2) → highest priority
   b. Prerequisite concepts from earlier chapters needed for current topic → high priority
   c. Key formulas, rules, or definitions introduced in this chapter → medium priority
3. FILTER to 5–7 items, balanced across the chapter's main concepts
4. APPLY Buzan Primacy Effect: most important current-topic items go FIRST
5. RANDOMIZE remaining items (after top 1–2 primacy items are locked)
```

**Buzan injection — Primacy Effect:** Phase 1 occupies the Primacy window — recall is highest at the very start of a session. The most important current-topic items are placed first because the brain is primed to encode what it sees first. The first 1–2 items must be the highest-priority concepts from the chapter.

**Not applied here:** Radiant Thinking, Peg System, Major System — these require encoding time (45–90 seconds) and do not fit the 2-minute hard cap. Memory Sprint is for rapid activation, not deep encoding.

**Scoring:**
- Correct answer: +100 XP
- Streak bonus: +10 XP × current_streak
- Speed bonus: +10 XP if answered in < 5 seconds
- Wrong answer: no penalty (this is warm-up, not assessment)
- Phase 1 score weight: 10% of total session score
- Results feed back into the spaced repetition model for platform-level adaptive review

**Adaptation rules (post-sprint routing):**
```
IF accuracy >= 80% → Student ready for new content; proceed to Phase 2 normally
IF accuracy 60–79% → Proceed but flag for teacher review dashboard
IF accuracy < 60%  → System routes to remediation BEFORE new content; Phase 2 is gated
```

**Standards reference:** Every recall item displays its standard code in the post-sprint review screen. Example: `UZ-MATH-5-NATNUM-03 — Natural sonlarni yaxlitlash`.

**Pronoun policy:** All Uzbek content uses "Siz" (formal). Never "sen". Russian: "Вы", never "ты".

## Cognitive load

- **Bloom range:** L1 (Remember) → L2 (Understand). Maximum Bloom ceiling is L3 for Algorithm archetype (see Adaptable parameters). No L4–L6 in this phase.
- **PISA range:** L1 → L2. Recognition and basic comprehension only.
- **Scoring:** Yes. +100 XP per correct, streak bonus, speed bonus. 10% of total session score.
- **Time budget:** ≤2 minutes hard cap. Typically 3 min including transitions and result screen.
- **AI Tier:** Tier 1 (pre-generated item pool).

## Inputs

- Textbook chapter content (key terms, prerequisite concepts, foundational facts for current chapter)
- Phase 0-B completion flag (Phase 1 does not render until Flash Cards gateway is passed)
- Schema activation keywords from Phase 0-A Panel 5 (used for item prioritization — items matching activated schemas are ranked higher in step 2 of item selection algorithm)
- Subject family tag (influences format distribution — see Adaptable parameters)
- Archetype tag (determines Bloom ceiling and item count override)
- Grade band (influences item difficulty calibration)

## Outputs

Per-item data, consumed by downstream phases and the platform's adaptive system:

- **Per-item results:** `{ item_id, format, correct: bool, time_ms, bloom_level, pisa_level, skill_tag }`
- **Phase aggregate:** `{ accuracy_pct, total_xp, streak_max, speed_bonus_count, phase_1_complete: true }`
- **Routing signal:** `{ readiness: "go" | "flag" | "remediate" }` based on accuracy thresholds
- **Spaced repetition feed:** incorrect items flagged for platform-level adaptive review scheduling
- **Standards log:** per-item standard code recorded for teacher dashboard

## Adaptable parameters

| Parameter | Default | Override per archetype | Override per family |
|-----------|---------|------------------------|---------------------|
| Item count | 5–7 | Light lessons: 5 | — |
| Item count | 5–7 | Review/Spiral archetype: 7 | — |
| Bloom ceiling | L2 | Concept Intro: L2 | — |
| Bloom ceiling | L2 | Algorithm archetype: L3 | — |
| Format mix | ≥2 of 3 formats | — | — |
| MC option count | 4 | — | — |
| Speed bonus threshold | < 5 seconds | — | — |
| Accuracy thresholds (routing) | 80% / 60% | — | — |

## Subject-specific examples

**Aniq Fanlar (Math/Geometry/Algebra) — Grade 7, Chapter: Linear Equations:**
- MC: *"Qaysi ifoda chiziqli tenglama?"* A) 2x + 3 = 7 ✓ B) x² = 4 C) √x = 2 D) x/y = 1
- T/F: *"2x + 3 = 7 tenglamasining yechimi x = 2."* → True ✓
- YNNG: *"Kitobda aytilishicha, barcha chiziqli tenglamalar faqat bitta yechimga ega."* → Not Given ✓

**Til Fanlar (English) — Grade 8, Chapter: Present Perfect:**
- MC: *"Which sentence uses Present Perfect correctly?"* A) I have seen that film last week B) She has just finished ✓ C) They have went D) He have eaten
- T/F: *"'Have' is used with he/she/it in Present Perfect."* → False ✓
- YNNG: *"According to the chapter, Present Perfect is used for actions with a result in the present."* → Yes ✓

**Tabiy Fanlar (Chemistry) — Grade 9, Chapter: Oxides:**
- MC: *"Oksid bu nima?"* A) Ikki elementdan iborat birikma, ulardan biri kislorod ✓ B) Faqat metallardan hosil bo'lgan birikma C) Uchta elementdan iborat modda D) Kislota bilan ishqorning reaksiya mahsuloti
- T/F: *"Barcha oksidlar suvda eriydi."* → False ✓
- YNNG: *"Darslikda aytilishicha, SO₂ kislotali oksidlarga kiradi."* → Yes ✓

**Ijtimoiy Fanlar (History) — Grade 10, Chapter: WWI Causes:**
- MC: *"Birinchi Jahon urushining bevosita sababi nima bo'ldi?"* A) Avstro-Vengriya imperiyasi kengayishi B) Arxiduke Frans Ferdinandning o'ldirilishi ✓ C) Rossiyaning Bolqonga kirib borishi D) Germaniyaning dengiz kuchlarini kengaytirishi
- T/F: *"Triple Entente tarkibiga Frantsiya, Britaniya va Italiya kirgan."* → False ✓
- YNNG: *"Kitobda Serbia hukumati suiqasd uchun to'liq javobgarlikni qabul qilgani aytilgan."* → Not Given ✓

## Verification rules

1. **Item count in bounds:** Must be 5–7 items (Standard Mode). Fewer = incomplete; more than 10 (Extended) = spec violation.
2. **Format mix enforced:** ≥2 of the 3 approved formats must be used. A single-format sprint is a spec violation.
3. **No banned formats present:** Scan for text inputs, drag targets, open-ended prompts, fill-in-blank blanks. Must return 0.
4. **MC option count:** Every MC item must have exactly 4 options. Exactly 1 must be marked correct.
5. **Current chapter scope:** All items must reference only the current chapter's content. Test: content review against chapter source — no forward-leak terms allowed.
6. **No hints:** Phase 1 must contain no hint trigger, no hint overlay, no hint XP cost mechanism. Test: check session spec for hint-related elements in Phase 1 — must return 0.
7. **Bloom ceiling respected:** All items must be tagged L1 or L2 (or up to L3 for Algorithm archetype). No L4–L6 items. Test: check `[Bloom: LX]` tag on every item.
8. **Scoring present:** Each item must have correct XP award configured (+100 base). Streak and speed bonus must be active. Test: check item payload for XP fields.
9. **Buzan Primacy applied:** First item in the sprint must correspond to the highest-priority concept in the chapter (as determined by item selection algorithm step 2a). Test: editorial review — first item should not be a low-priority fact.
10. **Post-sprint routing logic present:** Session must evaluate accuracy after Phase 1 and emit a `readiness` signal. Test: check session state for `readiness` field after phase completion.
11. **Standards code present:** Every item must carry a standard code displayed in the post-sprint review screen. Test: check item metadata for `standard_code` field.
12. **Pronoun compliance:** Scan all Uzbek text for "sen" — must return zero occurrences.

## Integration points

**Entry:**
- `render_phase_1(chapter_id, archetype, grade_band, schema_keywords)` called after Phase 0-B completion flag and "Start my Homework" gateway press.
- Session timer starts on gateway press (in Phase 0-B), not on Phase 1 render — XP accrual is already active.
- Item pool generated from current chapter content. Primacy ordering applied.

**Exit:**
- On final item completion, results screen renders (3 seconds): score, XP earned, streak, accuracy %.
- Session state records Phase 1 aggregate + per-item results.
- `readiness` signal emitted:
  - `"go"` → Phase 2 Story Mode renders immediately.
  - `"flag"` → Phase 2 renders with teacher-review flag set silently in background.
  - `"remediate"` → Remediation interstitial renders before Phase 2; student sees a targeted review prompt for weak items.
- Spaced repetition feed dispatched to platform adaptive system.

**Cross-references:**
- `00-core/pronoun-policy.md` — governs all student-facing language
- `00-core/skill-taxonomy.md` — Bloom/PISA tag definitions and level boundaries
- `00-core/gamification-economy.md` — XP values (+100 correct, streak/speed bonuses)
- `00-core/difficulty-adaptation.md` — accuracy-based routing thresholds (80% / 60%)
- `00-core/pisa-framework.md` — PISA level definitions for item tagging
- Phase 0-B (`phase-0b-flashcards.md`) — completion flag dependency; flash card overlay remains accessible in Phase 1
- Phase 2 Story Mode — receives `readiness` signal and schema keywords for narrative calibration
- Platform adaptive review system — receives spaced repetition feed for incorrect items

## UX/animation spec

**Layout:** Full-screen question card. Item number indicator top-left (*"2 / 7"*). Progress dots at bottom (one dot per item; filled = completed, active = pulsing, upcoming = empty).

**Answer buttons:** 4 large tap targets for MC (full-width stacked buttons). 2 large tap targets for T/F (side-by-side). 3 large tap targets for YNNG (stacked or side-by-side based on label length). Button height: minimum 56px. Font: 16px semibold. Color: neutral (#F0F0F0) until tapped.

**Instant feedback:** On tap, the selected button immediately changes color — correct = green (#4CAF50) with checkmark icon, incorrect = red (#F44336) with X icon. Correct answer highlighted in green if student was wrong. Feedback duration: 1 second, then auto-advance.

**Button-merge-to-line animation (between questions):** On advancing to next question, all answer buttons simultaneously animate — each button shrinks in height (56px → 2px) and fades (opacity 1 → 0) over 250ms, converging to a single horizontal line at the vertical center of the button group. The line then expands upward and downward as the next question's buttons materialize (2px → 56px, opacity 0 → 1) over 250ms. Total transition: ~500ms. New question text fades in during button expansion.

**Streak counter:** Top-right corner. Shows current streak count with a flame icon. Counter increments with a bounce animation (scale 1.0 → 1.3 → 1.0, 200ms) on each correct answer.

**Speed bonus indicator:** If answered in < 5 seconds, a "+10 ⚡" badge pops from the answer button (translateY 0 → -20px, opacity 1 → 0, 600ms) after the green feedback resolves.

**Results screen:** Appears after final item. Background: subject accent color at 10% opacity. Shows: accuracy % (large, centered), total XP earned, max streak, time taken. "Next" button advances to Phase 2 (or remediation interstitial if `readiness = "remediate"`). Auto-advances after 4 seconds if student does not tap.

**Progress dots:** Row of dots at card bottom. Active dot is subject accent color with pulsing ring animation (scale 1.0 → 1.4 → 1.0, 1s loop). Completed dots are solid subject accent color. Upcoming dots are grey (#CCCCCC).

**Timer visibility:** No visible countdown timer displayed to the student. The 2-minute hard cap enforces a session-level cutoff — if time expires, the sprint ends and results are calculated from items answered so far. A soft warning (*"Tezroq bo'ling!"*) may be shown at 30 seconds remaining, at session designer's discretion.
