# Master Cross-Criteria Gap Analysis & Synthesis (v2)

**Analyst:** Michelangelo (Agent 71ccba21)
**Date:** April 2, 2026
**Task:** TMN-8 — Cross-Criteria Gap Analysis and Synthesis (Re-review after updates)
**Sources:** `HOMEWORK_STANDARDS.md` (v1.0, 2063 lines — updated April 2, 2026), `NETS_PROPOSAL_SUMMARY.md`, `EDUCATIONAL_EXPERIENCE_DESIGN.md`, `QUICK_REFERENCE.md`, sibling analyses (`analysis_leonardo_pisa.md`, `analysis_donatello_research.md`, `analysis_raphael_textbook.md`)

---

## Executive Summary

HOMEWORK_STANDARDS.md has been **substantially improved** since the first review. Multiple critical gaps identified in v1 have been addressed. The document is now closer to production-ready, though several issues remain.

### What Changed Since v1

| Previously Identified Gap | Status | Details |
|---------------------------|--------|---------|
| Reading PISA progression matrix (was placeholder stub) | **FIXED** | Full grade 1–11 matrix with competencies and game mappings (Section 4.2) |
| Science PISA progression matrix (was placeholder stub) | **FIXED** | Full grade 1–11 matrix with competencies and game mappings (Section 4.3) |
| Real-world operations entirely missing | **FIXED** | New Section 9 with 7 subsections: Recovery Queue, Catch-Up, Boost, Low Engagement, Technical Failures, Teacher Tools, Parent Portal |
| Final Boss PISA level mapping contradicted docx | **FIXED** | Final Boss now shows "Apply → Create" spanning PISA Level 3–6 with tiered question framework (Section 2.7) |
| Teacher Dashboard missing | **FIXED** | Section 9.6 with heat maps, deadline controls, custom assignments, Kundalik integration |
| Parent Portal missing | **FIXED** | Section 9.7 with PISA progression charts, AI recommendations, SMS summary, localization |
| Leaderboard specification missing | **NOT FIXED** | Still no dedicated section |
| Avatar Customization missing | **NOT FIXED** | Still no dedicated section |
| Bilingual Language Framework missing | **NOT FIXED** | Still absent |
| PISA Level definitions missing | **NOT FIXED** | No official OECD competency descriptors embedded |
| Creative Thinking domain not addressed | **PARTIALLY FIXED** | Acknowledged as "Known Limitation" (line 1455) with Phase 2 recommendation, but no mechanics added |
| AI Refinement stage lacks inline constraints | **NOT FIXED** | Section 5.1 still shows pipeline without defining permissible AI operations |
| PISA-level-tagged example questions | **NOT FIXED** | Game specs still lack per-PISA-level examples |

---

## Per-Criterion Verdicts (Updated)

| Criterion | Description | Previous Verdict | Updated Verdict | Change |
|-----------|-------------|-----------------|-----------------|--------|
| **1. Textbook Source-of-Truth** | NETS adapts delivery, not content | PASS | **PASS** | No change — was already strong |
| **2. Research Paper Coverage** | All research elements present | PARTIAL (78/100) | **PARTIAL (89/100)** | +11 — operations, progressions added |
| **3. PISA Criteria Alignment** | Standards map to PISA levels | PARTIAL | **PARTIAL (improved)** | Progressions complete, Final Boss fixed, but Level 5-6 + Creative Thinking remain thin |

---

## Criterion 1: Textbook Source-of-Truth — PASS

No regressions. The two minor flags from v1 remain:

1. **AI Refinement stage** (Section 5.1): Pipeline still shows `TEXTBOOK → AI REFINEMENT → NETS HOMEWORK` without defining permissible AI operations inline. The DO/DON'T rules in 5.2 are downstream — implementers may not cross-reference them. Low risk but worth a one-line constraint definition.

2. **CS curriculum scope** (implicit): The CS progression (Python/JS for Grades 7–9, AI/ML for Grades 10–11) may exceed MoEN-approved textbook scope. Should be documented as an explicit exception or confirmed as textbook-aligned.

---

## Criterion 2: Research Paper Coverage — PARTIAL (89/100)

### Improvements

| Category | Previous Score | Updated Score | Notes |
|----------|---------------|---------------|-------|
| Edge Cases & Real-World Operations | 15% | **90%** | Comprehensive Section 9 with mode precedence, state transitions, worked examples |
| Grade-by-Grade Detail | 50% | **85%** | Reading and Science progressions now complete (Grades 1–11) |
| Gamification Economy | 70% | **75%** | Slight improvement — badge system expanded but leaderboard/avatar still missing |

### Remaining Gaps (Criterion 2)

**MAJOR:**

1. **Bilingual Language Acquisition Framework** — The research paper's CEFR/IELTS progression (Pre-A1 to C1), Krashen's Input Hypothesis, and content-based instruction methodology remain absent. This is a core subject area. Score impact: -4 points.

2. **Leaderboard Specification** — Research paper specifies class-level only, weekly reset, anti-competition measures, opt-in for parents. HOMEWORK_STANDARDS.md mentions leaderboards in passing (Principle 3 and badges) but has no dedicated section. Score impact: -2 points.

3. **Avatar Customization Specification** — Research paper describes cultural-themed cosmetic items (Uzbek clothing, Silk Road outfits). Only mentioned in badge context. No specification section. Score impact: -2 points.

**MINOR:**

4. **Estonia ProgeTiger / Computational Thinking Track** — Not specified as a game or standard. Score impact: -1 point.

5. **Canada BC Six Meta-Competencies** — Only PISA skills tracked, not the full meta-competency set. Score impact: -1 point.

6. **Anti-Unhealthy Competition Measures** — Principle 3 addresses intrinsic > extrinsic motivation, but the specific anti-competition safeguards (no public shaming, opt-in leaderboards, celebrating improvement) from the research paper are not codified. Score impact: -1 point.

---

## Criterion 3: PISA Criteria Alignment — PARTIAL (improved)

### Improvements

1. **Reading & Science progression matrices now complete** — Full grade 1–11 tables with PISA level targets, competencies, and game mappings. These are well-structured and include subject-specific game adaptations.

2. **Final Boss PISA mapping resolved** — Now correctly shows "Varies (Apply → Create)" at PISA Level 3–6 in the Game Mechanics Matrix (Section 3.1, line 937). Section 2.7 has a detailed tiered question framework with PISA ceilings by grade band.

3. **Learning Pyramid updated** — Now shows CREATE at the top with Final Boss (Hard tier) and properly places EVALUATE with Real-Life Challenges and Peer Teaching.

4. **Tiered damage-to-PISA mapping** — Section 2.7 now specifies PISA ceiling by grade band per tier (Easy/Medium/Hard), with a design note explaining that PISA level is decoupled from HP damage (damage reflects relative difficulty to the student, PISA level is tracked for analytics).

### Remaining Gaps (Criterion 3)

**HIGH:**

1. **PISA Creative Thinking still not covered by any mechanic.** The document now acknowledges this as a "Known Limitation" (line 1455) and recommends a "Creative Lab" mechanic for Phase 2. This is honest but doesn't fix the gap. Uzbekistan scored 14/60 (OECD avg: 33/60). No homework activity develops creative thinking skills. Score impact: significant for PISA readiness.

2. **PISA Levels 5–6 remain thin.** The document now correctly maps Final Boss Hard tier to Level 5–6 for Grades 9–11, and Real-Life Challenge targets Level 5–6. But these are still only 2 mechanics, and Level 5–6 work is confined to ~8–15 minutes of a 20–30 minute session. The Known Limitation note (line 1455) acknowledges this. For top-30 PISA ambitions, more Level 5–6 time is needed.

3. **No PISA level definitions embedded.** PISA levels are referenced throughout but never defined. Content creators must still guess what "Level 4" means when writing questions. The OECD provides precise competency descriptors — these should be included as a reference section.

**MODERATE:**

4. **Game mechanic specs lack PISA-level-tagged example questions.** Each game provides subject examples but doesn't tag them to specific PISA levels. Content teams need exemplars at Level 2, Level 3–4, and Level 5–6 for each mechanic.

5. **Adaptive Quiz PISA ceiling unclear.** Mapped to Level 3 in Section 3.1, but the IRT algorithm (Section 11.5) can escalate without bound. The spec doesn't indicate what PISA levels the hardest questions reach.

---

## Top 10 Highest-Priority Gaps (Updated)

| Rank | Gap | Criterion | Severity | Status vs. v1 |
|------|-----|-----------|----------|---------------|
| **1** | **Bilingual Language Acquisition Framework missing** — CEFR/IELTS progression, Krashen's Input Hypothesis, grade-level targets absent | C2 | **High** | Unchanged |
| **2** | **PISA Creative Thinking domain not covered** — acknowledged as limitation but no mechanic added | C3 | **High** | Acknowledged, not fixed |
| **3** | **PISA Levels 5–6 still thin** — only Final Boss Hard + Real-Life Challenge | C3 | **High** | Improved (Final Boss now tiered) but still structurally limited |
| **4** | **No PISA level definitions embedded** — content creators lack reference for what each level means | C3 | **Moderate** | Unchanged |
| **5** | **Leaderboard specification missing** — class-only, weekly reset, anti-competition rules not codified | C2 | **Moderate** | Unchanged |
| **6** | **Avatar Customization specification missing** — cultural-themed cosmetics system unspecified | C2 | **Moderate** | Unchanged |
| **7** | **AI Refinement stage lacks inline constraints** — Section 5.1 doesn't define permissible operations | C1 | **Moderate** | Unchanged |
| **8** | **Game specs lack PISA-level-tagged example questions** — content teams need per-level exemplars | C3 | **Low-Moderate** | Unchanged |
| **9** | **Anti-unhealthy competition measures not codified** — research paper safeguards not in standards | C2 | **Low** | Unchanged |
| **10** | **Adaptive Quiz PISA ceiling unspecified** — IRT algorithm has no stated PISA cap | C3 | **Low** | Unchanged |

---

## Specific Actionable Edit Suggestions for HOMEWORK_STANDARDS.md

### 1. Add Bilingual Language Acquisition Framework — HIGH

Add a new Section 4.4 (or standalone section) specifying:

| Grade | CEFR Target | Key Skills | NETS Games |
|-------|-------------|-----------|------------|
| 1–2 | Pre-A1 | Letter recognition, basic greetings | Flashcards, Tile Match (bilingual pairs), Movement Breaks |
| 3–4 | A1 | Simple phrases, reading short texts | Sentence Fill (word bank), Story Mode (bilingual segments) |
| 5–6 | A1–A2 | Short paragraphs, basic writing | Why Chain (2–3 levels), Sentence Fill (partial bank) |
| 7–8 | A2–B1 | Complex texts, structured writing | Why Chain (4+ levels), Real-Life Challenge (English context) |
| 9–11 | B1–B2 | Academic texts, essays, debates | Final Boss (English), Peer Teaching (English), Real-Life Challenge |

Reference Krashen's Input Hypothesis (i+1) and content-based instruction methodology.

### 2. Add Section 4.0: PISA Proficiency Level Definitions — HIGH

Insert before Section 4.1 with official OECD competency descriptors for Mathematics, Reading, and Science at each level (1–6). This gives content teams a reference when designing questions and verifying PISA level tags.

### 3. Add Leaderboard Specification to Section 6 — MODERATE

Add Section 6.4:

| Parameter | Specification |
|-----------|---------------|
| **Scope** | Class-level ONLY (no school-wide) |
| **Reset Cycle** | Weekly (every Monday at 00:00 local time) |
| **Categories** | XP Total, Streak Length, Chapters Mastered |
| **Display** | Top 3 highlighted, all students see own rank |
| **Parent Access** | Opt-in only |
| **Anti-Competition** | No public shaming, celebrate improvement (weekly "Most Improved" spotlight), anonymize below-median positions |

### 4. Add Avatar Customization Specification to Section 6 — MODERATE

Add Section 6.5:

| Parameter | Specification |
|-----------|---------------|
| **Theme** | Cultural — Uzbek traditional clothing, Silk Road outfits, historical figures |
| **Unlock Method** | Achievement-based only (no purchases) |
| **Sources** | Boss victories (2★+), badge milestones, streak rewards, Boost Mode incentives |
| **Display** | Leaderboard, reflection journal header, peer teaching profile |
| **Non-Competitive** | No "rare" items creating social pressure; all items obtainable through effort |

### 5. Add AI Refinement Constraints to Section 5.1 — MODERATE

After the pipeline diagram, add:

> **"AI Refinement" is limited to:** formatting, narrative framing, cultural contextualization, difficulty scaffolding, and question generation from textbook concepts. **AI Refinement MUST NOT:** alter factual claims, modify formulas or dates, change scientific explanations, simplify in ways that remove essential meaning, or introduce content beyond textbook scope. These constraints codify the DO/DON'T rules in Section 5.2 at the pipeline level.

### 6. Add PISA-Level-Tagged Example Questions to Game Specs — LOW-MODERATE

For each game mechanic in Sections 10/11, add at least one example at Level 2, Level 3–4, and Level 5–6. Example for Why Chain:

| PISA Level | Example |
|------------|---------|
| Level 2 | "Why do plants need water?" (single causal step) |
| Level 3–4 | "Why does the rate of photosynthesis change at different temperatures?" (multi-step, variable analysis) |
| Level 5–6 | "Design an experiment to test whether light intensity or CO₂ concentration has a greater effect on photosynthesis rate. Justify your variable controls." (experimental design, evaluation) |

### 7. Specify Adaptive Quiz PISA Ceiling — LOW

In Section 11.5, add to the IRT implementation:

> **PISA Level Mapping:** θ ranges map to PISA levels as follows: θ < 0 → Level 1–2, θ 0–0.5 → Level 3, θ 0.5–1.0 → Level 4, θ 1.0–1.5 → Level 5, θ > 1.5 → Level 6. Question banks MUST contain calibrated items at all PISA levels to support the full θ range.

### 8. Document CS Curriculum Exception — LOW

In Section 5.2 or 5.3, add a note:

> **Exception — Computer Science:** Where MoEN-approved CS textbooks do not yet cover topics in the NETS CS progression (e.g., Python/JavaScript for Grades 7–9, AI/ML for Grades 10–11), these topics are NETS-supplemented content. This exception to Principle 1 is explicitly acknowledged and should be reviewed annually as textbooks are updated.

---

## New Strengths in Updated Document

The following additions are well-executed and should be preserved:

1. **Section 9 Real-World Operations** — Comprehensive and well-structured. The mode precedence system (Section 9.0) with priority hierarchy, interaction rules, and state transition diagram is excellent engineering. The dual-threshold Boost Mode trigger (Section 9.3) prevents false positives. The class-level exception is smart.

2. **Reading & Science progression matrices** — Complete, grade 1–11, with subject-specific game adaptations. The note about starting at Grade 1 (unlike Mathematics at Grade 3) shows attention to detail.

3. **Final Boss tiered question framework** — The decoupling of PISA level from HP damage is a strong design decision. The note explaining that damage reflects relative challenge to the student while PISA level is tracked for analytics is clear and well-reasoned.

4. **Teacher override policy** (Section 9.6) — Clear bounds with hard limits (cannot override Final Boss gate, anti-cheat, or 40-minute welfare cap). All overrides logged for accountability.

5. **Offline mode specification** (Section 9.5) — Pre-caching 7 sessions with 3x question pools, local theta-based adaptation, and reconnection sync protocol is production-grade.

6. **Low Engagement graduated response** (Section 9.4) — Three severity tiers with escalating interventions is more nuanced than the binary trigger in the research paper.

7. **Known Limitation acknowledgment** (line 1455) — Honestly stating that Level 5–6 coverage is thin and recommending Creative Lab for Phase 2 is better than silently ignoring the gap.

---

## Production Readiness Verdict (Updated)

### **CONDITIONALLY PRODUCTION READY**

The document has moved from "NOT YET PRODUCTION READY" to **conditionally production ready**. The critical blockers from v1 (missing progressions, missing operations) have been resolved.

| Blocker Type | v1 Count | v2 Count | Must Fix Before Production? |
|-------------|----------|----------|---------------------------|
| Critical gaps | 3 | **0** | N/A — all resolved |
| High gaps | 4 | **3** (bilingual, Creative Thinking, PISA definitions) | **Bilingual: Yes. Creative Thinking: Acceptable as Phase 2. PISA definitions: Recommended.** |
| Moderate gaps | 3 | **3** (leaderboard, avatar, AI constraints) | Recommended but not blocking |
| Low gaps | 2 | **3** (examples, quiz ceiling, CS exception) | Nice-to-have |

**Recommended path to full production readiness:**
1. **Must-fix:** Add bilingual language acquisition framework (core subject with no specification)
2. **Should-fix:** Add PISA level definitions (content teams need this reference)
3. **Should-fix:** Add leaderboard and avatar specs (gamification elements promised in the platform)
4. **Acceptable deferral:** Creative Thinking as Phase 2 (honestly acknowledged)
5. **Acceptable deferral:** PISA-level-tagged examples (can be added incrementally)

---

## Cross-Criterion Interaction Analysis

1. **Bilingual gap** spans C2 (missing from research paper coverage) and C3 (no PISA-aligned English/language progression). Fixing it improves both criteria.

2. **Known Limitation note** (line 1455) bridges C3 gap honestly — it acknowledges Level 5–6 thinness and Creative Thinking absence rather than claiming "Production Ready" without qualification. However, the document header (line 8) still says "Status: Production Ready" — consider changing to "Status: Production Ready (Phase 1)" to match the Known Limitation.

3. **Section 9 operations** create positive C1 interactions — the Recovery Queue and Catch-Up Mode specs explicitly preserve the Final Boss mastery gate (Section 9.0 governing principle), which protects the textbook source-of-truth by ensuring simplified modes don't skip assessment.

---

*Cross-criteria synthesis v2 complete. Re-reviewed against updated HOMEWORK_STANDARDS.md (2063 lines, updated April 2, 2026).*
*Michelangelo — Agent 71ccba21 | TMN-8 | April 2, 2026*
