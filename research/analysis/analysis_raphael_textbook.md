# Textbook Source-of-Truth Compliance Check — v2 (Updated)
**Analyst:** Raphael (Agent TMN-7)
**Date:** 2026-04-02
**Version:** 2 (recheck after document updates)
**Criterion Evaluated:** Criterion 1 — Textbooks are the main source of truth. NETS is not changing concepts, only refining content and adapting delivery.

---

## Verdict: **PASS** (4 flags — 2 carried forward, 2 new)

The document remains fundamentally compliant. Several updates **strengthen** the source-of-truth architecture. However, two new gaps introduced by the updated Section 9 (Operations & Edge Cases) need attention.

---

## What Changed Since v1 Review

| Section | Change | Impact on Criterion |
|---|---|---|
| §1.1 Learning Pyramid | Expanded from 6 to 7 levels (now includes EVALUATE + CREATE, full Bloom's taxonomy) | Neutral — delivery structure only |
| §2.3 Story Mode | Added explicit "Preserve Core Concepts: Story MUST NOT change textbook concepts" | ✅ Strengthens compliance |
| §2.7 Final Boss | New PISA-Level Tiered Question Framework; HP for Grades 5-8 changed 100 → 80 | Neutral — game mechanics only |
| §4.2 Reading Progression | Full grade-by-grade matrix added (was placeholder); added explicit textbook philosophy note | ✅ Strengthens compliance |
| §4.3 Science Progression | Full grade-by-grade matrix added (was placeholder); added explicit textbook philosophy note | ✅ Strengthens compliance |
| §3 Games | 14-game matrix added with research citations | Neutral — delivery layer |
| **§9 (NEW)** | Real-World Operations & Edge Cases: Recovery Queue, Catch-Up Mode, Boost Mode, Low Engagement, Tech Failures, Teacher Tools, Parent Portal | ⚠️ New flags — see below |

---

## Core Architecture — Still Passing

### Section 1.2 Principle 1 (Unchanged)

> **STANDARD:** "Homework MUST NOT change core concepts from textbooks. It MUST adapt delivery method to active, gamified, AI-personalized learning."

Still present, still mandatory language. No regression.

---

### Section 5.2 Adaptation Rules (Unchanged)

| DO | DON'T |
|---|---|
| ✅ Preserve core concepts exactly as in textbook | ❌ Change mathematical formulas or scientific facts |
| ✅ Add narrative layer for engagement | ❌ Alter historical dates or geographical information |
| ✅ Convert passive examples to active problems | ❌ Modify grammar rules or vocabulary definitions |
| ✅ Embed cultural context | ❌ Remove essential prerequisite knowledge |
| ✅ Add gamification elements | ❌ Add content not aligned with textbook scope |

Still present, still the governing constraint. No regression.

---

### New Strengthening Language (Additions)

**Section 2.3 Story Mode — new rule:**
> "Preserve Core Concepts: Story MUST NOT change textbook concepts"

This closes a previously implicit gap where Story Mode's narrative wrapping could theoretically distort concepts. Now explicitly prohibited.

**Section 4.2 Reading — new philosophy note:**
> "The textbook provides the texts; NETS deepens the student's relationship WITH those texts through active comprehension, critical analysis, and creative response."

**Section 4.3 Science — new philosophy note:**
> "The textbook explains phenomena; NETS makes students THINK LIKE SCIENTISTS. Science is questioning, not memorizing."

Both add subject-level reinforcement of source-of-truth principle within their respective progression sections.

---

## Flags — Full Assessment

### Flag 1 (Carried Forward — Minor): "AI Refinement" Stage Lacks Inline Constraints

**Location:** Section 5.1

The pipeline `TEXTBOOK → AI REFINEMENT → NETS HOMEWORK` still has no definition of what "refinement" is constrained to do. The 5.2 DO/DON'T rules remain the governing constraint, but they are one section away.

**Recommendation:** Add a one-line definition in §5.1: *"AI Refinement is limited to: narrative framing, cultural contextualization, difficulty scaffolding, and gamification formatting. It MUST NOT alter factual claims, formulas, dates, or definitions."*

---

### Flag 2 (Carried Forward — Minor): CS Progression May Exceed Textbook Scope

**Location:** Sections 3 (Game 14 reference) and NETS_PROPOSAL_SUMMARY P45

The CS grade-by-grade progression (Block coding → Python/JS → AI/ML concepts) remains without documented mapping to MoEN-approved textbooks. No update was made to address this in the current revision.

**Recommendation:** Confirm the CS progression maps to existing curriculum for each grade band, or document it as an explicit exception.

---

### Flag 3 (NEW — Medium): Catch-Up Mode "Non-Critical Content" Is Undefined

**Location:** Section 9.2

The Catch-Up Mode algorithm includes:

```
IF chapter is standalone enrichment:
  priority = LOW → mark as "reviewed" (skip Final Boss)
```

And the specification states: **"Content Scope: Essential concepts only (non-critical content skipped)"**

The document does not define what makes content "non-critical" or "standalone enrichment" vs. a core chapter. If the AI content-prioritization model misclassifies a textbook chapter — or if any chapter labeled enrichment actually contains prerequisite concepts — it will be entirely skipped, including its Final Boss mastery gate.

**Risk level:** Medium. This is the one operational mode where core textbook content could be bypassed without teacher or student awareness, at scale (8.8M students).

**Recommendation:**
1. Define "non-critical / standalone enrichment" explicitly — either list these chapters by subject/grade, or define the classification criteria.
2. Add a rule: chapters labeled LOW priority must still have their textbook concepts covered in a subsequent memory sprint or consolidation, even if the chapter session is skipped.
3. Teacher must explicitly approve LOW priority classifications before Catch-Up Mode executes them.

---

### Flag 4 (NEW — Minor): Teacher Custom Assignments Have No Textbook Scope Constraint

**Location:** Section 9.6 Teacher Management Tools

> "Custom Assignments: Create assignments using NETS game engine (select games, topics, difficulty)"

There is no documented rule requiring teacher-created custom assignments to draw content from approved textbooks. A teacher could in principle build assignments on topics outside the MoEN curriculum scope.

**Risk level:** Minor. Teacher authorship carries implied professional accountability, and scale-driven content drift is unlikely. But there is no structural safeguard.

**Recommendation:** Add a constraint to §9.6: *"Custom assignment topics MUST be selected from the approved curriculum content graph. Off-curriculum topics are not permitted."*

---

## Section 9 Operations Review — General Assessment

New Section 9 (Real-World Operations) introduces delivery flexibility for edge cases. The governing principle at §9.0 is strong:

> "No operational mode defined in this section may bypass the Final Boss mastery gate. Accommodations may adjust difficulty, time, or support level, but completion of Final Boss remains required for chapter progression. This is non-negotiable."

This correctly protects the mastery gate even in compressed/offline/disengaged scenarios. The modes adjust *delivery*, not *content*:

| Mode | Content Changed? | Delivery Changed? | Verdict |
|---|---|---|---|
| Recovery Queue | No | Yes — condensed, steps skipped | ✅ Compliant |
| Catch-Up Mode (HIGH priority) | No | Yes — simplified, 50% HP | ✅ Compliant |
| Catch-Up Mode (LOW priority) | **Chapter skipped entirely** | N/A | ⚠️ Flag 3 |
| Boost Mode | No — optional supplementary | Yes — bonus XP incentive | ✅ Compliant |
| Low Engagement | No | Yes — session shortened, more games | ✅ Compliant |
| Offline Mode | No | Yes — Why Chain/Real-Life unavailable | ✅ Compliant (equity note*) |
| Teacher Custom Assignments | Unconstrained | N/A | ⚠️ Flag 4 |

*Equity note: Why Chain and Real-Life Challenge (the deepest reasoning activities) are both unavailable offline. In a country with 10,000+ rural schools, students in low-connectivity areas will systematically receive less deep textbook-concept engagement. Not a source-of-truth violation, but worth tracking as an equity metric.

---

## Full Pass/Fail Summary

| Area | v1 Result | v2 Result | Notes |
|---|---|---|---|
| Core Philosophy §1.2 Principle 1 | ✅ PASS | ✅ PASS | Unchanged, still strong |
| Adaptation Pipeline §5.1 | ⚠️ Flag | ⚠️ Flag 1 | "AI Refinement" still undefined |
| Adaptation Rules §5.2 | ✅ PASS | ✅ PASS | Unchanged |
| NETS Proposal P4–P5 | ✅ PASS | ✅ PASS | Unchanged |
| P39 Subject Overview | ✅ PASS | ✅ PASS | Unchanged |
| Mathematics (P40) | ✅ PASS | ✅ PASS | Unchanged |
| Reading (P41 + §4.2) | ✅ PASS | ✅ PASS | New explicit note strengthens it |
| Science (P42 + §4.3) | ✅ PASS | ✅ PASS | New explicit note strengthens it |
| English (P43) | ✅ PASS | ✅ PASS | Unchanged |
| History (P44) | ✅ PASS | ✅ PASS | Unchanged |
| CS (P45) | ⚠️ Flag | ⚠️ Flag 2 | No change; textbook mapping still absent |
| Story Mode §2.3 | (not flagged) | ✅ PASS | **Improved** — explicit "Preserve Core Concepts" rule added |
| Operations §9 (NEW) | — | ✅ PASS with 2 flags | Catch-Up LOW priority + Custom Assignments |

**Overall: PASS.** Core architecture is sound. Two new flags from Section 9 require attention before production rollout — Flag 3 (medium severity) most urgently.
