---
name: Phase 7 — Reflection
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.7 (lines 1241-1320) + §22 session + Matrix v0.4
---

# Phase 7 — Reflection

## Purpose (WHAT)

Silent analytics engine and Duolingo-style routing layer. Phase 7 is NOT student self-reflection prose — it is the data aggregation and next-step decision system that runs invisibly at session end, with a brief student-facing end screen as its only visible output. The routing decision determines whether the student advances, remediates, or receives a regression flag.

**Redefinition note (§22 session):** Prior versions of this phase spec described Phase 7 as a student journaling step. That definition is retired. Phase 7's primary function is analytics and routing. The TEFCAS reflection prompts (from UNIFIED §5.7) are available but optional — configurable by the teacher in the teacher dashboard.

## Structure (HOW)

**Four data layers collected silently during and immediately after Phase 6:**

### Layer 1 — Per-question data

| Field | Type | Source |
|-------|------|--------|
| `question_id` | string | Generated at question creation |
| `phase_id` | enum (0a, 0b, 1, 2, 3, 4, 5, 6) | Phase context |
| `bloom_level` | L1–L6 | Tagged at generation |
| `pisa_level` | L1–L6 | Tagged at generation |
| `skill_tags` | array [creativity, problem-solving, critical-thinking, memory, application, translation] | From `00-core/skill-taxonomy.md` — 6 axes |
| `correct` | boolean | Student answer vs expected |
| `time_seconds` | int | Time spent on this question |
| `attempts` | int | Retries used |
| `hints_used` | int | 0+ |
| `difficulty` | enum (easy / medium / hard) | Tagged at generation |
| `capture_submitted` | boolean | Whether step-capture was submitted (when applicable) |
| `capture_rubric_score` | float 0–1 | Partial credit from rubric (when capture triggered) |

### Layer 2 — Per-phase data

| Field | Purpose |
|-------|---------|
| `phase_score_pct` | % correct in this phase |
| `phase_time_seconds` | Total time in phase |
| `phase_completed` | Did student finish all items |
| `phase_skill_breakdown` | { creativity: X%, problem-solving: Y%, critical-thinking: Z%, memory: A%, application: B%, translation: C% } |

### Layer 3 — Per-session data

| Field | Purpose |
|-------|---------|
| `session_id` | UUID |
| `lesson_id` | Links to `nets_lessons` |
| `overall_score_pct` | Total % correct across all graded phases |
| `passed` | boolean — `overall_score_pct ≥ 60` |
| `vs_student_avg` | Delta vs student's prior subject average |
| `route_decision` | Next-step recommendation (advance / remediate / advance+regression-flag) |
| `skill_deltas` | Skill axis changes vs last session |

### Layer 4 — Routing decision

Full algorithm specification: see `00-core/routing-algorithm.md`. Summary for reference (do NOT use as override):

```
IF overall_score_pct < 60:
    identify weakest phase(s) by phase_score_pct
    identify failed questions within those phases
    queue remediation: Preview (relevant panels) → Flash Cards → failed questions only
    mark lesson as "remediation-required"
ELIF overall_score_pct ≥ 60 AND > student_subject_avg:
    advance to next lesson
    update student_subject_avg
ELSE:  # passed but at or below average
    advance to next lesson
    flag regression signal
```

Passing threshold: **60%** overall.

**Student-facing end screen (the only visible part of Phase 7):**

The end screen renders after the routing decision is made. It contains:

1. **Score display:** Overall score % as a circular dial (animated fill on load). Stars earned (from Phase 6) displayed below the dial.
2. **Skill breakdown bar chart:** 6 horizontal bars (one per skill axis from skill-taxonomy.md), showing student's performance this session vs prior session average. Bars animate left-to-right on screen entrance (400ms stagger).
3. **Next step card:** One of three variants:
   - *Advance:* "Keyingi darsga o'tamiz — [Lesson Name]" + "Davom etish" button.
   - *Remediate:* "Bir oz ko'proq mashq kerak — [Failed concept area]" + "Takrorlash" (Review) button linking to remediation queue.
   - *Advance + regression flag:* Advance card shown to student (regression flag is teacher-only — not shown to student).

**Optional TEFCAS prompts (configurable by teacher):**

When enabled, one TEFCAS-framed prompt appears between the skill breakdown chart and the next step card. Prompt is auto-selected by accuracy:

| Accuracy | Prompt (Uzbek) | Prompt (Russian) |
|---------|---------------|-----------------|
| ≥80% | *"Bugungi eng yaxshi Trial (urinish) qaysi edi? Qaysi strategiya Success ga olib keldi?"* | *"Какая попытка сегодня была лучшей? Какая стратегия привела к успеху?"* |
| 60–79% | *"Miyangiz qanday Feedback oldi? Keyingi safar nimani Adjust qilasiz?"* | *"Какой Feedback получил ваш мозг? Что вы Adjust ируете в следующий раз?"* |
| <60% | *"Har bir Trial miyangizni kuchaytiryapti. Bitta kichik Adjust tanlang — nima qilasiz boshqacha?"* | *"Каждая попытка укрепляет ваш мозг. Выберите одно небольшое Adjust — что сделаете по-другому?"* |
| Hesitation on concept X | *"[X] savoli qiyin bo'ldi. Miyangiz qanday Feedback oldi?"* | *"Вопрос [X] был трудным. Какой Feedback получил ваш мозг?"* |
| Streak ≥5 | *"[X] ta ketma-ket to'g'ri! Supernovangiz porlayapti — qaysi strategiya ishladi?"* | *"[X] правильных подряд! Ваша Supernova светится — какая стратегия сработала?"* |

Response requirements when TEFCAS prompts are enabled: minimum 10 characters; no auto-grading (all responses accepted); teacher dashboard shows aggregate themes, not individual entries.

**BOST learning-goal closure check (always present, regardless of TEFCAS setting):**

At the end of the end screen, the student's learning goal from Phase 0-A Panel 6 is resurfaced: *"Eslatma: Bugun siz '[stored_learning_goal]' ni bilmoqchi edingiz. Bildingizmi?"* (Remember: Today you wanted to learn '[goal]'. Did you figure it out?) Three-option response: **Ha** (Yes) / **Qisman** (Partially) / **Hali emas** (Not yet). Response logged — not scored, not shown to teacher individually.

**National Pride closing line (≥60% sessions only):**

After all prompts and BOST closure check, one closing line is displayed. 55/45 national/global ratio:
- National: *"Sizning bilimingiz Uchinchi Renessansning poydevoridir."* (Your knowledge is the foundation of the Third Renaissance.)
- Global: *"Sizning aniq fikrlashingiz global standartlarga mos keladi."* (Your analytical thinking meets global standards.)

For sessions below 60% accuracy: skip pride framing. Use TEFCAS encouragement instead: *"Har bir urinish miyangizni kuchaytiryapti."*

**Telemetry layer (reference implementation QA — not student-facing):**

The following signals are logged for implementation validation and pipeline QA:

| Signal | Purpose |
|--------|---------|
| Per-question time distribution | Identify questions taking disproportionate time (content complexity or UX friction) |
| Capture failure rate | % of capture-triggered questions where student did not submit steps |
| Hint ladder usage rate | % of boss questions where 1st, 2nd, 3rd hints were used |
| Preview scroll depth | Did student read all Preview panels or skip? |
| Quit rate per phase | Phase where student most commonly exits (session abandonment signal) |
| Reproducibility diff | Generate same lesson 3× — structure ≥95% identical, content variety 30–60% |

## Cognitive load

- **Bloom range:** Not applicable (Phase 7 is silent analytics). End screen displays data; TEFCAS prompts (when enabled) are Bloom L1 metacognitive recall.
- **PISA range:** Not assessed.
- **Scoring:** None for Phase 7 itself. Aggregates scores from all prior phases.
- **Time budget:** ~1 min for end screen display. TEFCAS prompt response (when enabled): up to 2 min additional.
- **AI Tier:** Tier 1 (template-based routing and prompt selection). No live AI required.

## Inputs

- Per-question data from all graded phases (collected throughout the session, aggregated here).
- Phase aggregate data from Phases 1, 4, and 6 (primary scored phases).
- `boss_defeated` and `stars_earned` flags from Phase 6.
- `remediation_flag` from Phase 6 (Light Checkpoint 3rd-wrong-answer trigger).
- `learning_goals` string from Phase 0-A Panel 6 (for BOST closure check).
- `hesitation_points[]` and `answer_changes[]` from Phase 6 (for TEFCAS prompt selection).
- Student's prior session records (for `vs_student_avg` and `skill_deltas` calculation).
- Teacher setting: TEFCAS prompts enabled/disabled (from teacher dashboard config).
- Session mode (Standard vs Extended) — determines whether minimum response length is 10 chars or 2 sentences.

## Outputs

- `session_record` object (all 4 data layers) → written to `nets_sessions` database.
- `route_decision` → consumed by session orchestrator to render the correct next step card.
- `standards_mastered[]` and `standards_needs_work[]` → teacher dashboard (aggregate class view).
- `skill_deltas` → student progress record (drives streak and leaderboard calculations).
- `bost_goal_answered` (Yes / Partially / Not yet) → logged to session record.
- `tefcas_response_text` (when TEFCAS prompts enabled) → teacher dashboard aggregate themes only.
- `phase_7_complete: true` → session marked complete.
- Remediation queue (when `route_decision = remediate`) → queued in student's homework pipeline.

## Adaptable parameters

| Parameter | Default | Override per archetype | Override per family |
|-----------|---------|------------------------|---------------------|
| TEFCAS prompts | Off (teacher-configurable) | — | — |
| TEFCAS min response length | 10 characters | Extended mode: 2 sentences | — |
| Passing threshold | 60% | — | — |
| National Pride closing line | Enabled for ≥60% sessions | Disabled for <60% sessions | — |
| Skill chart axes | 6 (from skill-taxonomy.md) | — | — |
| BOST closure check | Always present | — | — |
| Telemetry logging | Always active | — | — |

## Subject-specific examples

**Aniq Fanlar (Matematika — Grade 6):**
- Skill breakdown: application and problem-solving axes likely strongest; creativity axis lower (expected for algorithm-heavy sessions).
- Remediation queue (if triggered): routes back to Phase 0-A Preview Panel 3 (Examples) + Phase 0-B Flash Cards for formula terms + Phase 6 failed questions regenerated with different numbers.
- Skill delta example: `{ "problem-solving": +0.12, "application": +0.08, "memory": -0.03 }` — slight memory regression flagged if formulas not being retained.

**Tabiy Fanlar (Biology — Grade 7, Cell Division):**
- Hesitation detection on mitosis-stage identification questions → TEFCAS prompt targets: *"Mitoz bo'linish savoli qiyin bo'ldi. Miyangiz qanday Feedback oldi?"*
- Skill delta: memory and critical-thinking axes primary for classification-heavy Biology sessions.
- Remediation: routes to Preview panel on stage identification + Flash Cards for stage names.

**Ijtimoiy Fanlar (Tarix — Grade 6, Silk Road):**
- Cause-effect questions typically drive critical-thinking axis. Low critical-thinking score → regression flag on that axis.
- National Pride closing line: Silk Road content defaults to national variant (heritage-rich topic).
- BOST closure: *"Bugun siz 'Ipak yo'li nima uchun muhim?' ni bilmoqchi edingiz. Bildingizmi?"*

**Til Fanlar (English — Grade 8, Conditionals — Concept Intro / Light Checkpoint):**
- No boss_defeated flag (Light Checkpoint doesn't have HP combat). `passed` determined by overall_score_pct ≥ 60%.
- `remediation_flag` may be raised if Light Checkpoint's 3rd-wrong-answer trigger fired.
- Skill axes: translation and application primary; creativity secondary (writing conditional sentences in natural context).

## Verification rules

1. **Routing is always executed:** `route_decision` must be present in every session record. Test: assert `route_decision` is not null in session payload.
2. **Passing threshold is 60%:** `passed = true` if and only if `overall_score_pct ≥ 60`. Test: assert logical consistency between `overall_score_pct` and `passed` flag.
3. **Routing logic matches threshold:** `route_decision` must match the routing algorithm in `00-core/routing-algorithm.md` for the given `overall_score_pct` and `vs_student_avg`. Test: validate routing decision against algorithm output for same inputs.
4. **All 4 data layers present:** session record must contain per-question data, per-phase data, per-session data, and route_decision. Test: assert all required fields exist and are non-null.
5. **Skill tags match taxonomy:** All `skill_tags` values must be one of the 6 axes defined in `00-core/skill-taxonomy.md`. Test: validate each skill_tag value against allowed set.
6. **BOST closure check always rendered:** End screen must always include the BOST learning-goal closure prompt. Test: assert BOST prompt render in session payload regardless of TEFCAS setting.
7. **National Pride line gated at 60%:** Pride line must not appear when `overall_score_pct < 60`. Test: assert pride line absent in low-score session payloads.
8. **Pronoun compliance:** All Uzbek text must use "Siz". Zero "sen" occurrences. Test: regex scan on all student-facing Phase 7 strings.
9. **TEFCAS prompt respects teacher config:** TEFCAS prompts must not render if teacher has disabled them. Test: assert no TEFCAS prompt render when teacher config `tefcas_enabled: false`.
10. **Phase 7 completion flag emitted:** `phase_7_complete: true` and full session record must be written before session is marked complete. Test: assert flag and record in session state.

## Integration points

**Entry:**
- Session orchestrator calls `run_phase_7(session_context)` immediately after `phase_6_complete: true` is set.
- All per-question data collected throughout the session is passed as input.
- Student's prior session records fetched from `nets_sessions` for `vs_student_avg` and `skill_deltas`.
- Teacher dashboard config fetched to determine TEFCAS prompt setting.

**Exit:**
- On student tapping "Davom etish" or "Takrorlash" on the end screen: `phase_7_complete: true` set, full session record written, `route_decision` executed.
- Advance → session orchestrator queues next lesson, student navigated to next session home screen.
- Remediate → remediation queue populated, student navigated to remediation entry point (Phase 0-A Preview of failed panels).
- Advance + regression flag → advance path executed for student; regression flag written to teacher dashboard only.

**Cross-references:**
- `00-core/routing-algorithm.md` — authoritative routing logic (Layer 4). Do not duplicate routing algorithm here.
- `00-core/skill-taxonomy.md` — authoritative 6-axis skill tag definitions.
- `00-core/pronoun-policy.md` — student-facing language rules.
- Phase 0-A (`phase-0a-preview.md`) — provides `learning_goals` string (BOST closure input) and is the entry point for remediation routing.
- Phase 6 Final Challenge (`phase-06-final-challenge.md`) — primary data source (boss data, stars, standards).
- Teacher dashboard — receives `standards_mastered[]`, `standards_needs_work[]`, aggregate TEFCAS themes, regression flags.
- `nets_sessions` database — receives full session record write.
- `system/narrative/quotes_database.json` — National Pride closing line selection (subject-tagged, 55/45 ratio).

## UX/animation spec

**Layout:** End screen is a single scrollable card (no pagination). Three stacked sections: (1) Score + Stars, (2) Skill Breakdown Chart, (3) Next Step + optional TEFCAS prompt + BOST closure.

**Score dial:** Circular progress dial, 120px diameter, centered. Fills clockwise from 0 to `overall_score_pct` on entrance (800ms ease-out). Color: green for ≥80%, amber for 60–79%, red for <60%. Percentage number counter increments simultaneously (0 → final, same 800ms). Stars appear below dial with the same entrance animation as Phase 6 boss-defeated screen (scale 0→1.2→1, 200ms each, 300ms stagger).

**Skill breakdown chart:** 6 horizontal bars labeled with skill axis names (Uzbek: Ijodkorlik, Muammoni Hal Etish, Tanqidiy Fikrlash, Xotira, Qo'llash, Tarjima). Each bar shows current session value (solid color) vs prior session average (ghost bar overlay). Bars animate left-to-right simultaneously (width 0 → final, 400ms ease-out, 60ms stagger between bars). Subject-family accent color used for filled portion.

**Next step card:** Rounded card with subject-accent left border. Advance: forward arrow icon + lesson name. Remediate: circular arrows icon + topic name in amber. Button fills on tap (subject-accent color, 200ms). No transition animation on exit — direct navigation to next screen.

**TEFCAS prompt block (when enabled):** Soft blue prompt box matching Phase 0-A BOST styling. Multiline text input (max 5 lines). Character counter at bottom right. Placeholder: *"Fikringizni yozing..."* (Write your thought...) Submitted on "Davom etish" tap.

**BOST closure check:** Three tap-chip options (Ha / Qisman / Hali emas) in a horizontal row. Selected chip turns solid (subject-accent color). One tap required before "Davom etish" activates. No transition animation — chips simply toggle state on tap.

**National Pride closing line:** Appears below BOST closure check as a full-width soft banner (light gold background for national variant, light blue for global). Text centered, italic. Fades in (opacity 0→1, 500ms) after BOST chip is tapped.

**Absent for <60% sessions:** Pride banner does not render. TEFCAS prompt (if enabled) shifts to encouragement variant automatically.

**Transition out:** "Davom etish" / "Takrorlash" tap triggers: current end screen fades out (opacity 1→0, 300ms) + brief session-complete haptic pulse (mobile only) → next screen slides in from right.
