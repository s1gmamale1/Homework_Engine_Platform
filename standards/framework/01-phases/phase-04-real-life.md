---
name: Phase 4 — Real-Life Challenge
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.4 (lines 866-974) + §22 session
---

# Phase 4 — Real-Life Challenge

> **ACTIVE FOR: Aniq Fanlar (Math) and Tabiy Fanlar (Sciences).**
> Til Fanlar (Languages): SKIPPED — Reading (Phase 2) serves the comprehension-transfer role for Language family.
> Ijtimoiy Fanlar (History/Social Sciences): SKIPPED — narrative and causal transfer handled in Phase 0-A Preview framing and Phase 6 Final Boss.
> If skipped, route directly from Phase 3 to Phase 5 Consolidation.

---

## Purpose (WHAT)

Force transfer: the student applies textbook knowledge to a single, deep, immersive real-world scenario as THE EXPERT — not as a student answering a question. This is the primary PISA transfer assessment for the session. One deep scenario outperforms multiple shallow ones (§22 session decision).

Phase 4 is scored and contributes 30% of the session's total score.

**Scope lock:** Real-Life tests APPLICATION of what Preview taught — it MUST NOT introduce new skills, methods, or concepts. If Preview taught factoring via `p+q`/`pq`, Real-Life uses factoring. If Preview didn't teach the quadratic formula, Real-Life cannot require it. Every skill tested in Phase 4 must have been explicitly taught in Phase 0-A.

**Complexity ceiling:** Scenarios use the SAME difficulty tier as the hardest Preview example, with different numbers/context. Don't escalate — transfer, not stretch. Stretch happens in Phase 6 Final Challenge.

**Family scope:**
- **Aniq Fanlar + Tabiy Fanlar:** ACTIVE in Hard mode. Uses word→formula translation pattern taught in Preview.
- **Til Fanlar + Ijtimoiy Fanlar:** SKIPPED. Language uses Reading phase for transfer. History narrative lives in Preview.

---

## Structure (HOW)

**ONE scenario, 4–6 sub-questions:**

```
[Scenario setup — context narrative] → [Sub-question 1] → [Sub-question 2] → ... → [Sub-question N] → phase exit
```

**First-Person Expert POV — mandatory:**

Every scenario uses direct address. The student is a professional:

| Element | Rule |
|---------|------|
| POV | "You are..." / "Your job is..." / "A client asks you..." — never third-person ("Alisher is...") |
| Role | Modern, aspirational professional — project manager, engineer, analyst, consultant, researcher, lab director. Never folksy or patronizing. Reference: `00-core/context-policy.md` |
| Case | Realistic professional scenario plausible in a modern workplace, business, or research setting |
| Questions | Multiple-path with plausible distractors. Forces reasoning, not pattern matching |
| Justification | Student must explain their answer. AI evaluates reasoning, not just the selected option |
| Curriculum | All reasoning uses concepts from the current textbook chapter only. No outside knowledge required |
| **Visuals** | 1-2 SVG illustrations per scenario (scenario diagram + result visualization). Full spec: `00-core/visual-generation.md`. Example: solar farm layout diagram, drone flight path arc, hitbox wireframe. If agent cannot render SVG, emit structured JSON placeholder for downstream rendering. |

Context policy is defined in `00-core/context-policy.md`. The key prohibition: no bazaar/village/shopkeeper/farmer clichés. Modern professional context only. Uzbek settings are natural and encouraged when genuine (Yashil Makon, IT Park, Afrosiyob rail, Tashkent City development) — but never forced-folksy.

**Subject routing (from §22 session):**

| Family | Approach | Example framing |
|--------|---------|-----------------|
| Aniq Fanlar (Math) | Applied word problem with real-world constraints. Pure calculation when the scenario is computational; W5H scaffold when multiple factors are involved. Filtering examples: hitbox analysis, drone flight path, solar farm output, Yashil Makon irrigation design | "You are the lead engineer on the Yashil Makon solar farm. Your panels convert 18% of sunlight..." |
| Tabiy Fanlar (Sciences) | Narrative-process style: tell the process as a compact story, then ask questions — the "photosynthesis pattern" from §22. Student reads 3–4 sentences of process narrative, then answers applied questions | "You are the lab director at the Tashkent Botanical Institute. Your team's experiment shows chlorophyll absorbing light at 680nm..." |

**Capture rule:**
Calculation solve-steps trigger Notebook Capture. Reference: `00-core/capture-rule.md`. Capture applies to individual solve steps, not to the scenario setup or final answer confirmation. 1–3 capture points per scenario is the expected range.

**Buzan — W5H Radiant Problem Solving Scaffold:**

Before the answer area opens, a 6-branch frame appears — Who / What / Where / When / Why / How — radiating from the problem statement. Student fills at least 4 of 6 branches with brief notes (1–2 words each). The frame stays visible as a sidebar reference while answering.

| Grade band | W5H mode |
|------------|----------|
| G5–6 | Mandatory, 4 of 6 branches minimum |
| G7–8 | Default ON, toggleable off, 5 of 6 branches |
| G9+ | Available via "Tahlil" (Analyze) button, not forced |

W5H is scaffolding — NOT scored. The student's final answer is scored per the rubric.

W5H does NOT apply to pure calculation scenarios (single correct answer, no multi-factor reasoning). Apply it to: multi-factor investigations (Sciences), scenarios with competing constraints (Math with multiple variables), any scenario requiring reasoning about stakeholders or trade-offs.

**Buzan — Decision Mapping Scaffold (Method #5):**

For scenarios involving a genuine choice between two or more competing options (not single-answer expert problems), extend W5H with a Decision Map: each option radiates from the central problem with pro/con sub-branches. Student assigns weights (1–5) to branches, selects their choice, and writes a 1–2 sentence justification.

Decision Mapping applies where: Sciences (two experimental designs), Math (two fleet plans, two engineering approaches). It does NOT apply to single-answer scenarios ("spot the 3 fire safety violations"), pure calculation, or any Language/History scenario.

**National Pride — "Wise Status" injection (30% of Phase 4 tasks):**

For approximately 1 in 3 Real-Life Challenges, the expert-role framing is enhanced:

1. **Status:** Professional title in the scenario — "Bosh Muhandis," "Strategik Tahlilchi," "Laboratoriya Rahbari"
2. **Arena (55/45):** National: anchor in real Uzbek achievement ("Afrosiyob tezyurar poyezdlari 250km/s aniqlikda ishlaydi"). Global: anchor in global standard ("CERN ning Katta Adron Kollayderi...")
3. **Bridge:** Connect the textbook question to the arena. The academic core (formula, calculation, reasoning) is UNTOUCHED
4. **Closing:** "Sizning aniqligingiz Uchinchi Renessansni quradi" (national) or "Sizning natijangiz global standartlarga mos" (global)

Source templates: `system/narrative/task_injections.json`. The 70% of tasks without Wise Status use the standard first-person expert POV with no heritage framing.

---

## Cognitive load

| Axis | Range |
|------|-------|
| Bloom's taxonomy | L3 (Apply) — L5 (Evaluate) |
| PISA | L2 — L4 |
| Time budget | 15–18 min standard · ~10 min extended (focused, tighter scenario) |
| Per-question budget | ~3–4 min |
| Cognitive mode | Transfer → expert reasoning → multi-step justification |
| Score weight | 30% of session total |

---

## Inputs

- Phase 3 aggregate output: `phase_03_score`, skill axis breakdown, PISA estimate
- Current `standard_ref` and textbook chapter content
- Subject family tag (determines routing — skip or enter, and which subject approach to use)
- Grade band (determines question count, W5H mode, capture point count)
- `00-core/context-policy.md`
- `00-core/capture-rule.md`
- `system/narrative/task_injections.json` (for Wise Status injection)
- PISA minimum gate: L2+. If student is below L2 after Phase 3, replace this phase with an extra Apply-level Adaptive Quiz (routing defined in `00-core/routing-algorithm.md`)

---

## Outputs

- Per-question: correct/incorrect, partial-credit flag, reasoning quality tag, time, skill tags `[Bloom: LX | PISA: LX]`
- Phase aggregate: `phase_04_score` (% of available points), PISA process tags (`employ` / `interpret` / `formulate`)
- Capture events: list of solve-step items where Notebook Capture was triggered
- W5H branch fill rate (analytics only — not scored)
- Skip signal: `phase_04_status: "skipped"` for Language and History families

---

## Adaptable parameters

| Parameter | Default | Override per family | Override per archetype |
|-----------|---------|---------------------|------------------------|
| Scenario count | 1 | — | — |
| Sub-question count | 4–6 | Sciences: 4 (narrative-process style, fewer but deeper) | Application archetype: 5–6 |
| Capture points | 1–3 | Aniq Fanlar: up to 3 per scenario | — |
| W5H scaffold | Grade-dependent (see table above) | Math pure-calc: W5H OFF | — |
| Decision Map | Only on multi-option scenarios | — | — |
| Wise Status injection | ~30% of tasks | — | — |
| PISA minimum gate | L2+ | — | — |
| Skip condition | Language (Til Fanlar), History/Social (Ijtimoiy Fanlar) | — | — |

---

## Subject-specific examples

**Aniq Fanlar (Math — Grade 7, linear functions / comparing plans):**

> "You run a delivery startup. You are comparing two vehicle leasing plans for your fleet. Plan A: 2,000,000 so'm/month base + 1,500 so'm/km. Plan B: 3,000,000 so'm/month base + 1,000 so'm/km. Your drivers average 120 km/day. Which plan saves more money over a month? A partner says Plan B is always better — is that true? Show your analysis."

W5H scaffold: ON (multiple factors). Decision Map: ON (two competing plans). Capture: ON (cost calculation steps).

**Aniq Fanlar (Math — Grade 5, fractions with real-world constraints):**

> "You are a project coordinator for the Yashil Makon city greening initiative. Your team must plant saplings in three zones: Zone A needs 3/4 of the total seedlings, Zone B needs 1/6, and Zone C gets the rest. You have 480 seedlings in stock. Is there enough for all three zones? How many saplings go to Zone C?"

W5H: partially ON (Grade 5 mandatory, but can be simplified for pure calculation sub-questions). Capture: ON for both calculation steps.

**Tabiy Fanlar (Biology — Grade 8, photosynthesis):**

Narrative-process intro (3–4 sentences):
> "You are the lab director at the Tashkent Botanical Institute. Your team has placed two identical plants in identical conditions — except one is under a red-spectrum LED (680nm) and one is in total darkness. After 48 hours, one plant has produced measurable glucose; the other has not."

Sub-questions: identify which plant produced glucose and explain why; predict what happens if CO₂ is removed; calculate expected glucose output given light intensity data from the textbook.

W5H: ON (multi-factor investigation). Capture: ON (calculation sub-question). No Decision Map (single-answer expert problem for most sub-questions).

**Tabiy Fanlar (Chemistry — Grade 9, combustion / fire safety):**

> "You are a fire safety inspector called to a workshop. The owner stores gasoline, uses a wood-burning stove, and keeps an asbestos fire blanket in the corner. He asks: 'Is my setup safe?' You look around and immediately spot 3 problems. What are they, and what do you tell the owner?"

W5H: ON. No calculation → no Capture. No Decision Map (single-answer spot-the-violation).

---

## Verification rules

1. **Family routing gate:** If `subject_family == "til-fanlar"` or `subject_family == "ijtimoiy-fanlar"` → phase must be absent from session output. `phase_04_status: "skipped"` must be emitted. Violation: any Language or History session containing a Phase 4 block.
2. **First-person POV mandatory:** Scenario setup must contain direct address ("You are...", "Your job is...", "A client asks you..."). Third-person framing ("Alisher needs to...") is a production error. Automated check: scan `context_narrative` field for second-person direct address.
3. **Context policy compliance:** Scenario must not contain bazaar, village, shopkeeper, or farmer tropes. Reference `00-core/context-policy.md`. Automated check: banned-context keyword list in `scripts/check_blueprint_compliance.py`.
4. **Single scenario rule:** Exactly 1 scenario per Phase 4. Multiple scenarios = production error (§22 decision: single deep scenario outperforms multiple shallow).
5. **Question count bounds:** 4–6 sub-questions for standard mode. Fewer than 4 = production block. More than 6 = production warning.
6. **Bloom/PISA tags required:** Every sub-question carries `[Bloom: LX | PISA: LX]` and a `pisa_process` tag (`employ` / `interpret` / `formulate`). Missing tags = production block.
7. **Capture rule compliance:** Any sub-question involving a calculation step must carry a `notebook_capture: true` flag. Reference `00-core/capture-rule.md`. Calculation questions without capture trigger = violation.
8. **PISA minimum gate:** If student PISA level estimate entering Phase 4 is below L2, routing-algorithm must redirect to Adaptive Quiz. Phase 4 with a below-L2 student is a routing error.
9. **No external curriculum:** Every concept tested must trace to the current textbook chapter `standard_ref`. Cross-chapter injection = production block.
10. **Pronoun compliance:** All Uzbek content uses "Siz" (formal). Never "sen". Reference `00-core/pronoun-policy.md`.
11. **Wise Status tagging:** Tasks using the Wise Status recipe must reference `task_injections.json` template IDs. Academic core (formula, calculation, reasoning) must be identical between Wise Status and non-Wise Status versions of equivalent tasks.

---

## Integration points

**Entry (called by Phase 3 exit):**
- Receives: `phase_03_score`, skill axis breakdown, updated PISA estimate, family tag, grade band, `standard_ref`
- Guard 1: if `subject_family` is in skip list (`til-fanlar`, `ijtimoiy-fanlar`) → emit `phase_04_status: "skipped"` and route to Phase 5
- Guard 2: if student PISA estimate < L2 → emit `phase_04_status: "remediation_redirect"` and route to Adaptive Quiz (see `00-core/routing-algorithm.md`)
- If entered: load pre-generated scenario for current `standard_ref`

**Exit (calls Phase 5 Consolidation):**
- Emits: `phase_04_score`, per-skill axis results, `pisa_process` breakdown, capture event list
- Phase 5 Consolidation uses `phase_04_score` and `keywords_80_20` (from Phase 2 if Language; from Phase 3 game metadata if non-Language) to build the Radiant Summary branches

**Cross-references:**
- `00-core/context-policy.md` — modern professional context rules
- `00-core/capture-rule.md` — Notebook Capture mechanic
- `00-core/routing-algorithm.md` — PISA gate, 60% threshold, post-phase routing
- `00-core/pronoun-policy.md` — "Siz" / "Вы" enforcement
- `00-core/skill-taxonomy.md` — maps outputs to problem-solving, application, critical-thinking axes
- `system/narrative/task_injections.json` — Wise Status recipe templates

---

## UX/animation spec

**Scenario entry:**
- Scenario card fades in (300ms ease-in) following Phase 3 exit screen
- Context narrative displayed first as a full-width reading panel — no sub-questions visible yet
- Student taps "Ready" or waits 10 seconds (auto-advance disabled for G5–6; auto-advance optional for G9+)

**W5H scaffold display:**
- Appears as a radiant diagram sidebar (persistent on the right or bottom of the question card)
- Six branches radiate from a central "Problem" node; empty branches pulse softly to invite input
- Student taps a branch to type 1–2 words; filled branches turn solid; required branches (minimum 4) show a subtle incomplete indicator until filled
- W5H panel is collapsible for G9+ (hidden by default, tap "Tahlil" to expand)

**Decision Map display (when applicable):**
- Extends from the W5H frame — two option nodes emerge from the central problem
- Pro/con sub-branches appear as the student expands each option
- Weight slider (1–5) appears on each branch; total weight auto-balances
- Design spec: `system/ui-ux/` (Decision Map component)

**Sub-question display:**
- One sub-question at a time (passage/context remains visible above the fold)
- Answer input: MC tap-select, short-answer text, or calculation input depending on question type
- Calculation input: numeric keypad with fraction/decimal toggle; triggers Notebook Capture flow on confirmation (see `00-core/capture-rule.md`)
- On wrong answer: feedback referencing the specific textbook concept; partial credit awarded where rubric allows
- Partial-credit display: amber badge on the question card (not red); encourages persistence

**Wise Status framing:**
- Professional title shown in a subtle header above the context narrative: "Laboratoriya Rahbari sifatida..."
- Closing quote (from `task_injections.json`) appears after final sub-question confirmation, before phase exit
- Visual treatment: national arena → Uzbek color palette accent; global arena → neutral/blue accent

**Phase exit:**
- Shows Phase 4 aggregate score + PISA process breakdown (employ / interpret / formulate bars)
- 3-second auto-advance, tap to skip
- Feeds into session-level progress ribbon
