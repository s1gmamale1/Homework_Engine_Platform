# PISA Criteria Alignment Analysis

**Analyst:** Leonardo (Agent c434f08b)
**Date:** April 2, 2026 (Revision 3 — V3 Unified Spec review)
**Task:** TMN-5 — Criterion 3: PISA Criteria Alignment
**Source Document:** `standards/NETS-Homework-Engine-UNIFIED.md` (Version 2.0, April 2, 2026)
**Previous Sources:** `HOMEWORK_STANDARDS.md` (v1.0), `NETS_PROPOSAL_SUMMARY.md`, `__NATIONAL EDUCATION__.docx`

---

## Revision History

| Date | Version | Document Reviewed | Score |
|------|---------|-------------------|-------|
| April 1, 2026 | v1 | HOMEWORK_STANDARDS.md (original) | PARTIAL |
| April 2, 2026 | v2 | HOMEWORK_STANDARDS.md (updated) | PARTIAL-STRONG |
| April 2, 2026 | v3 | standards/NETS-Homework-Engine-UNIFIED.md | **STRONG — approaching YES** |

---

## Executive Summary (v3)

1. **All seven gaps from v1/v2 have been addressed.** The Unified Spec (V3) systematically resolves every issue identified in previous analyses, citing this gap analysis as the source for several new sections.

2. **Official PISA proficiency level definitions are now embedded** (Section 3.0) with full Math, Reading, and Science tables including score ranges, competency descriptors, and Uzbekistan student distribution. Content teams now have authoritative reference definitions.

3. **PISA Creative Thinking has a dedicated section** (Section 8) with four sub-sections covering: why it matters, creative expansions to existing mechanics, a fully specified "Creative Lab" optional mechanic, and a grade-band progression table.

4. **The Final Boss PISA-tiered framework is now definitive.** Section 5.6 provides explicit Easy=Level 3/Medium=Level 4/Hard=Level 5-6 mapping with example questions, a question distribution formula (40% Easy, 40% Medium, 20% Hard), and a complete JSON schema for PISA-tagged boss questions including rubrics, solution steps, and Socratic hints.

5. **New structural improvements beyond gap fixes:** mandatory PISA tagging schema for every content item (Section 2.5), continuous PISA level tracking per student with domain breakdowns (Section 3.3), transition skill tracking (L→L+1), difficulty tiers explicitly mapped to PISA level ranges (Section 9.2), and a Grades 5-8 Boss HP restored to 100 HP (matching source docx).

---

## Gap Resolution: Complete Status

| # | Gap (from v1) | v1 | v2 | v3 Status | How V3 Addresses It |
|---|---------------|----|----|-----------|---------------------|
| 1 | Reading & Science progression matrices missing | CRITICAL | FIXED | **FIXED** | Section 7.2 (Reading) and 7.3 (Science) with full grade-band tables, NETS games, and transition skills |
| 2 | Final Boss Bloom's-to-PISA mapping inconsistency | HIGH | FIXED | **ENHANCED** | Section 5.6 provides definitive tiered system with PISA level per tier, damage values, example questions, JSON schema with `pisa_level` field, and distribution formula |
| 3 | No PISA Creative Thinking coverage | HIGH | DEFERRED | **FIXED** | Entirely new Section 8 with four sub-sections: CT competencies, expansions to 5 existing mechanics, Creative Lab spec, and grade-band progression |
| 4 | Level 5-6 activities don't fit session time | MODERATE | PARTIAL | **FIXED** | Extended mode sessions (40-60 min) introduced in Section 4.1; Real-Life Challenge extended to 10 min; Final Boss extended to 10-15 min |
| 5 | No PISA level definitions embedded | MODERATE | OPEN | **FIXED** | Section 3.0 provides official OECD definitions for Math (with score ranges + Uzbekistan distribution), Reading, and Science. Source note mandates content creators reference these. |
| 6 | No PISA-level-tagged exemplar questions | LOW-MOD | OPEN | **FIXED** | Section 5.6 includes a complete JSON exemplar (Grade 5 Math, market problem) with pisa_level, pisa_domain, pisa_content, pisa_process, pisa_context, transition_skill, blooms_level, difficulty_tier, rubric, solution steps, and common errors |
| 7 | Adaptive Quiz PISA ceiling unclear | LOW | OPEN | **FIXED** | Section 9.2 maps difficulty tiers to PISA level ranges (Tier 1=Below 1-1, Tier 2=1-2, Tier 3=2-3, Tier 4=3-4, Tier 5=5-6). Section 3.1 maps PISA levels to Bloom's and game mechanics. |

---

## PISA Level Coverage (v3)

| PISA Level | v1 | v2 | v3 | Mechanics in V3 |
|------------|----|----|----|----|
| **Below 1** | — | — | **Explicit** | Flashcards, Memory Sprint (new: explicitly included as a level) |
| **Level 1** | Adequate | Adequate | **Strong** | Tile Match, Sentence Fill, Memory Palace, Movement Breaks |
| **Level 2** | Adequate | Adequate | **Strong** | Story Mode, Adaptive Quiz, Sentence Fill, Mystery Box |
| **Level 3** | Partial | Good | **Strong** | Final Boss Easy, Real-Life Challenge, Why Chain, Adaptive Quiz |
| **Level 4** | Partial | Good | **Strong** | Final Boss Medium, Why Chain (deep), Peer Teaching |
| **Level 5-6** | Very Weak | Partial | **Good** | Final Boss Hard, Real-Life Extended, Creative Lab, Peer Teaching |

**Level 5-6 assessment:** Improved from "Very Weak" to "Good" but not yet "Strong" because:
- Creative Lab is optional and restricted to PISA Level 3+ students (Grades 5-11)
- Final Boss Hard questions are only 20% of the encounter
- Real-Life Extended requires the longer session mode
- The bulk of Level 5-6 content relies on AI generation quality (Tier 2-3)

This is an acceptable design trade-off: 80%+ of Uzbek students are currently below Level 2, so Level 5-6 should be aspirational, not the primary focus of Phase 1.

---

## New Strengths in V3

### 1. Mandatory PISA Tagging Schema (Section 2.5)
Every content item requires a `pisa_ref` object with domain, proficiency_level, content_category, process_category, context, and transition_skill. The `transition_skill` field is a significant addition — it forces content creators to declare *which specific PISA level transition* each task scaffolds (e.g., "L1→L2: extract from simple charts"). This was absent from all previous specs.

### 2. Continuous PISA Level Tracking (Section 3.3)
Full JSON schema for per-student PISA tracking with:
- Continuous scale (e.g., 1.7) instead of integer levels
- Domain breakdowns (quantity, space, etc. for Math; access, integrate, reflect for Reading)
- Transition skills mastered vs. in-progress
- Trajectory assessment (on_track, at_risk)
- IRT-weighted recency-based calculation

### 3. PISA Level as Progression Gate (Section 3.2)
Student's PISA level now determines: which Bloom's levels they receive, Final Boss difficulty tier, game mechanic availability, and homework completion threshold. This creates a tighter feedback loop than the previous "one-size-fits-all" approach.

### 4. Difficulty Tiers Mapped to PISA (Section 9.2)
Each of the 5 difficulty tiers now has an explicit PISA level range:
- Tier 1 (Foundational): Below 1 - Level 1
- Tier 2 (Basic application): Level 1-2
- Tier 3 (Multi-step reasoning): Level 2-3
- Tier 4 (Complex analysis): Level 3-4
- Tier 5 (Advanced evaluation/creation): Level 5-6

### 5. Reflection Journal Corrected to Level 3-4 (Section 6.1)
Previous versions mapped Reflection Journal to "Create / Level 6". V3 correctly re-maps it to "Create / Level 3-4" with the note: "reflection is metacognitive, not the advanced reasoning PISA L6 requires." This is a more honest and accurate mapping.

### 6. Source Attribution Throughout
V3 cites which previous document each section came from and explicitly references this gap analysis (Leonardo) as the source for Sections 3.0, 7.2, 7.3, and 8. This creates a clear audit trail.

---

## Remaining Items (Minor)

### 1. Level 5-6 Depth (LOW)
Level 5-6 is "Good" but not "Strong." This is acceptable for Phase 1 given that 80%+ of students are below Level 2. However, for the top 2-3% of students, the system should eventually provide richer Level 5-6 content beyond Final Boss Hard and Creative Lab.

**Recommendation for Phase 2:** Develop a standalone "PISA Readiness Challenge" mode for Grades 9-11 students at Level 4+, with 20-30 minute sessions exclusively featuring Level 5-6 problems.

### 2. Reading Progression Uses Grade Bands Instead of Individual Grades (LOW)
Math progression (Section 7.1) maps individual grades (Grade 3, Grade 4, etc.). Reading (7.2) and Science (7.3) use grade bands (Grades 1-2, 3-4, 5-6, 7-8, 9-11). This is less granular but arguably appropriate given that reading/science skill development is less linear than math.

### 3. Creative Lab AI Evaluation Quality (LOW — Operational Risk)
Creative Lab scoring requires AI to evaluate "creativity" and "feasibility" of open-ended student responses (Tier 2 AI). This is inherently harder than evaluating structured answers. V3 acknowledges this by making Creative Lab optional and gated to Level 3+ students, which is a sensible risk mitigation.

---

## Overall Score (v3)

**Does `standards/NETS-Homework-Engine-UNIFIED.md` satisfy Criterion 3 (PISA Criteria Alignment)?**

### **STRONG — YES with minor caveats**

| Criterion | v1 | v2 | v3 |
|-----------|----|----|-----|
| All 3 PISA domains have grade-level progressions | No | Yes | **Yes** (enhanced with transition skills) |
| Game mechanics mapped to PISA levels | Partial | Yes | **Yes** (with Bloom's, AI tier, and content type) |
| PISA Levels 1-4 adequately covered | Partial | Yes | **Yes** (strong across all levels) |
| PISA Levels 5-6 adequately covered | No | Partial | **Good** (acceptable for Phase 1 demographics) |
| PISA Creative Thinking addressed | No | No | **Yes** (dedicated Section 8 with 4 sub-sections) |
| PISA level definitions embedded | No | No | **Yes** (Section 3.0 with official OECD descriptors) |
| Content team guidance (exemplars) | No | No | **Yes** (JSON exemplar with full PISA tagging) |
| PISA tracking per student | No | No | **Yes** (continuous scale with domain breakdowns) |
| Mandatory PISA tagging on all content | No | No | **Yes** (Section 2.5 with transition_skill field) |

**The Unified Spec (V3) satisfies Criterion 3.** It provides comprehensive PISA alignment across all three core domains plus Creative Thinking, with embedded level definitions, mandatory content tagging, per-student tracking, and a clear progression framework from Below Level 1 through Level 6. The remaining Level 5-6 depth limitation is an appropriate Phase 1 trade-off given Uzbekistan's current student distribution.

---

*Analysis complete. V3 represents a substantial improvement over previous versions and is ready for engineering and content teams to build against.*
