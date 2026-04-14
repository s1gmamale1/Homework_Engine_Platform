# PISA Criteria Alignment Analysis

**Analyst:** Leonardo (Agent c434f08b)
**Date:** April 2, 2026
**Task:** TMN-5 — Criterion 3: PISA Criteria Alignment
**Sources:** `HOMEWORK_STANDARDS.md`, `NETS_PROPOSAL_SUMMARY.md`, `__NATIONAL EDUCATION__.docx`

---

## Executive Summary

1. **HOMEWORK_STANDARDS.md provides strong PISA mapping for Mathematics** (Section 4.1), with grade-by-grade progression from Level 1 to Level 5-6 and corresponding NETS game assignments — but **Reading and Science progression matrices are placeholders** (Sections 4.2 and 4.3 contain only `[Similar progression matrix for reading/science skills]`).

2. **The 14 Game Mechanics Matrix (Section 3.1) maps each game to a single PISA level**, but the mapping is inconsistent with the source docx. Most critically, Final Boss is tagged as "Level 3-4" in HOMEWORK_STANDARDS.md but described as targeting "Level 5-6" (Create) in the docx's Bloom's-to-PISA table.

3. **PISA Levels 5 and 6 are severely underrepresented.** Only 2 of 14 game mechanics explicitly target these levels (Real-Life Challenge at Level 5-6, Reflection Journal at Level 6). Given that Uzbekistan's goal is top-30 PISA by 2030, the standards must develop more robust Level 5-6 pathways.

4. **PISA Creative Thinking — a fourth assessed domain since 2022 — is not addressed at all.** Uzbekistan scored 14/60 vs. OECD average of 33/60. No game mechanic or framework section targets this competency explicitly.

5. **The standards lack explicit PISA competency definitions per level.** PISA defines specific skills at each proficiency level (e.g., Math Level 3 = "employ basic strategies; interpret and use proportional reasoning"). These definitions are absent, making it impossible to verify whether activities truly reach the claimed level.

---

## Gap Table: PISA Level Coverage Across 14 Game Mechanics

| PISA Level | Expected Coverage | Actual Coverage in HOMEWORK_STANDARDS.md | Gap |
|------------|-------------------|------------------------------------------|-----|
| **Level 1** (Remember/basic recall) | Multiple mechanics for foundational skills | **Adequate.** Spaced Flashcards, Memory Sprint, Movement Breaks, Memory Palace all target Level 1. | None |
| **Level 2** (Understand/single-step) | Mechanics for comprehension and recognition | **Adequate.** Tile Match, Sentence Fill, Story Mode all target Level 2. | None |
| **Level 3** (Apply/multi-step) | Mechanics requiring application to structured problems | **Partial.** Adaptive Quiz (Level 3) and Final Boss (Level 3-4) cover this. | Minor — Final Boss is split across 3-4, diluting Level 3 specificity |
| **Level 4** (Analyze/complex reasoning) | Mechanics requiring analysis, justification, evaluation of methods | **Partial.** Mystery Box (Level 4) and Why Chain (Level 4-5) address analysis. | Moderate — only 2 mechanics, and Why Chain spans two levels without grade-specific calibration to Level 4 |
| **Level 5** (Evaluate/advanced modeling) | Mechanics requiring evaluation, strategic thinking, synthesis across domains | **Weak.** Only Real-Life Challenge (Level 5-6) and Peer Teaching (Level 5) explicitly target this. | Significant — Peer Teaching is optional (Grades 5-11 only) and session time is long (10-15 min), making it impractical in the standard 20-30 min homework flow |
| **Level 6** (Create/advanced reasoning under novel conditions) | Mechanics requiring creative problem-solving, novel strategy construction, rigorous argumentation | **Very Weak.** Only Reflection Journal is tagged Level 6, but reflection is metacognitive, not a PISA-assessed reasoning task. | **Critical** — No game mechanic genuinely produces Level 6 PISA performance. Reflection Journal develops self-regulation, not the advanced mathematical modeling, scientific argumentation, or interpretive analysis PISA Level 6 requires. |

---

## Detailed Gap Analysis

### Gap 1: Reading & Science Progression Matrices Are Missing (CRITICAL)

**Location:** HOMEWORK_STANDARDS.md, Sections 4.2 and 4.3

**Finding:** Both sections contain only placeholder text: `[Similar progression matrix for reading/science skills]`. This means:
- There is no grade-by-grade PISA level target for Reading or Science
- There is no specification of which NETS games should be used at each grade for these subjects
- Content teams have no standard to build against for 2 of the 3 core PISA domains

**Impact:** Without these matrices, Reading and Science homework cannot be systematically calibrated to PISA levels. The Mathematics matrix (Section 4.1) is well-structured and should serve as the template.

**Recommendation:** Complete Sections 4.2 and 4.3 using the same format as 4.1. For Reading, map: Retrieval (L1-2) → Inference (L2-3) → Interpretation (L3-4) → Evaluation (L4-5) → Critical Analysis (L5-6). For Science, map: Scientific Knowledge (L1-2) → Scientific Explanation (L2-3) → Evidence Evaluation (L3-4) → Experimental Design (L4-5) → Advanced Modeling (L5-6).

---

### Gap 2: Bloom's-to-PISA Mapping Inconsistency for Final Boss (HIGH)

**Location:** HOMEWORK_STANDARDS.md Section 3.1 vs. `__NATIONAL EDUCATION__.docx` Section 5.2

**Finding:** The Game Mechanics Matrix maps Final Boss to:
- **HOMEWORK_STANDARDS.md:** Bloom's "Apply-Analyze" → PISA Level 3-4
- **Docx Bloom's table:** Bloom's "Create" → PISA Level 5-6

The docx example for "Create" level is: *"Design a budget for class trip to Samarkand"* — this is a Final Boss question. Yet the standards demote it to Level 3-4.

**Impact:** If Final Boss is truly Level 3-4, the system has almost no mechanism to push students to Level 5-6. If it's Level 5-6, the Game Mechanics Matrix is wrong.

**Recommendation:** Reconcile the mapping. Final Boss should be a **tiered mechanic**: Easy questions at Level 3, Medium at Level 4, Hard at Level 5-6. Update the matrix to show "Level 3-6" and specify that the difficulty tier determines the PISA level targeted. The boss HP damage system already supports this (Easy -10 HP, Medium -20 HP, Hard -30 HP) — tie each damage tier to a specific PISA level.

---

### Gap 3: No PISA Creative Thinking Coverage (HIGH)

**Location:** Absent from all sections

**Finding:** PISA 2022 assessed Creative Thinking for the first time. Uzbekistan scored 14/60 (OECD avg: 33/60). The docx mentions this score in Section 2.1, but neither the docx nor HOMEWORK_STANDARDS.md includes any game mechanic, framework section, or progression matrix for Creative Thinking.

**PISA Creative Thinking assesses:**
- Generating diverse ideas
- Generating creative ideas
- Evaluating and improving ideas
- Written expression, visual expression, scientific problem-solving, social problem-solving

**Impact:** Students will continue to score poorly on Creative Thinking assessments because no homework activity explicitly develops these skills.

**Recommendation:** Add a 15th game mechanic (e.g., "Creative Lab" or "Idea Generator") targeting Creative Thinking, or expand existing mechanics:
- **Real-Life Challenge:** Add a "generate 3 different solutions" requirement
- **Final Boss Hard tier:** Include open-ended design/creation questions
- **Reflection Journal:** Add a "What would you do differently? Design an alternative approach" prompt
- Create a Section 4.4: Creative Thinking Progression Matrix

---

### Gap 4: Level 5-6 Activities Don't Fit Within 20-30 Minute Sessions (MODERATE)

**Location:** HOMEWORK_STANDARDS.md Section 2.1 (session duration) vs. Level 5-6 mechanics

**Finding:** The standard homework session is 20-30 minutes. But the only mechanics targeting PISA Level 5-6 are:
- **Real-Life Challenge:** 3-5 minutes (adequate but shallow for Level 5-6 reasoning)
- **Peer Teaching:** 10-15 minutes (half the entire session, and only unlocked by advanced students)

PISA Level 5-6 questions require sustained multi-step reasoning, synthesis, and argumentation. 3-5 minutes is insufficient for genuine Level 5-6 work.

**Recommendation:**
- Extend Real-Life Challenge to 5-8 minutes for Grades 9-11 when targeting Level 5-6
- Ensure Final Boss Hard-tier questions are genuinely Level 5-6 (not just harder Level 3-4)
- Consider an optional "Extended Challenge" mode (15-20 min standalone session) for students who have reached Level 4+ proficiency

---

### Gap 5: No PISA Level Definitions Embedded in Standards (MODERATE)

**Location:** Missing from all sections

**Finding:** The standards reference PISA levels (1-6) throughout but never define what each level means. The PISA framework defines precise competency thresholds:

| Level | Mathematics Example |
|-------|-------------------|
| 1 | Answer questions involving familiar contexts where all relevant information is present and the questions are clearly defined |
| 2 | Interpret and recognise situations in contexts that require no more than direct inference |
| 3 | Execute clearly described procedures, including those that require sequential decisions; select and apply simple problem-solving strategies |
| 4 | Work effectively with explicit models for complex concrete situations; select and integrate different representations |
| 5 | Develop and work with models for complex situations; select, compare, and evaluate appropriate problem-solving strategies |
| 6 | Conceptualise, generalise, and utilise information based on modelling of complex problem situations; apply insight and understanding |

Without these definitions, content creators must guess what "Level 4" means when designing questions.

**Recommendation:** Add a Section 4.0: "PISA Proficiency Level Definitions" with official OECD competency descriptors for Mathematics, Reading, and Science. Each game mechanic specification should reference these definitions when claiming a PISA level.

---

### Gap 6: Game Mechanics Lack Per-Level Question Templates (LOW-MODERATE)

**Location:** Section 3 game specifications

**Finding:** Each game mechanic provides subject-specific examples, but these examples are not tagged to specific PISA levels. For instance, the Why Chain examples (photosynthesis, Silk Road, fractions) don't indicate whether they represent Level 3, 4, or 5 performance. Content teams need PISA-level-tagged exemplar questions for each game mechanic.

**Recommendation:** For each game mechanic, provide at least one example question at Level 2, Level 3-4, and Level 5-6. This gives content teams concrete targets.

---

### Gap 7: Adaptive Quiz PISA Ceiling Is Unclear (LOW)

**Location:** HOMEWORK_STANDARDS.md Section 3.1

**Finding:** Adaptive Quiz is mapped to "Apply" (Bloom's) and "Level 3" (PISA). But the adaptive algorithm should be able to escalate to Level 4-5 for high-performing students. The current specification doesn't indicate a PISA ceiling — the quiz simply gets "harder" without specifying what PISA levels the hardest questions reach.

**Recommendation:** Specify that Adaptive Quiz difficulty tiers map to PISA levels: Tier 1-2 = Level 1-2, Tier 3 = Level 3, Tier 4 = Level 4, Tier 5 = Level 5. This ensures the adaptive algorithm has PISA-calibrated content at every difficulty tier.

---

## Overall Score

**Does HOMEWORK_STANDARDS.md satisfy Criterion 3 (PISA Criteria Alignment)?**

### **PARTIAL — with critical gaps**

**Evidence for strengths:**
- Mathematics PISA progression (Section 4.1) is well-structured with grade-by-grade level targets
- 14 game mechanics are each mapped to at least one PISA level
- The Bloom's Taxonomy pyramid (Section 1.1) explicitly links Bloom's levels to PISA levels
- Subject-specific PISA skill tables (Section 1.3) map competencies to NETS games for Math, Reading, and Science
- Research citations supporting PISA-level gains are provided for each mechanic

**Evidence for gaps:**
- **2 of 3 core PISA domain progression matrices are missing** (Reading, Science)
- **PISA Levels 5-6 are critically underserved** — only 1 genuine mechanic (Real-Life Challenge)
- **PISA Creative Thinking is completely absent** despite being a scored domain
- **Bloom's-to-PISA mapping contradicts the source docx** for the most important mechanic (Final Boss)
- **No PISA level definitions are included** for content team reference
- **No PISA-level-tagged example questions** within game mechanic specs

**Recommended priority to reach "Yes":**
1. **[CRITICAL]** Complete Reading and Science progression matrices (Sections 4.2, 4.3)
2. **[HIGH]** Reconcile Final Boss PISA level mapping — make it Level 3-6 tiered
3. **[HIGH]** Add Creative Thinking coverage (mechanic or expanded existing mechanics)
4. **[MODERATE]** Embed official PISA level definitions (new Section 4.0)
5. **[MODERATE]** Strengthen Level 5-6 pathways with longer time allocations and more mechanics
6. **[LOW]** Add PISA-level-tagged exemplar questions to each game mechanic spec

---

*Analysis complete. Reviewed against PISA 2022 framework and OECD proficiency level descriptors.*
