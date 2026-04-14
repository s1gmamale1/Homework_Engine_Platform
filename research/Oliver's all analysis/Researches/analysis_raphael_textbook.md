# Textbook Source-of-Truth Compliance Check
**Analyst:** Raphael (Agent TMN-7)
**Date:** 2026-04-02
**Criterion Evaluated:** Criterion 1 — Textbooks are the main source of truth. NETS is not changing concepts, only refining content and adapting delivery.

---

## Verdict: **PASS** (with minor flags for review)

The core architecture of HOMEWORK_STANDARDS.md is fundamentally sound on this criterion. The textbook-as-source-of-truth principle is explicitly stated, structurally enforced, and consistently reflected across subject philosophies. There are two minor areas worth monitoring.

---

## Evidence Summary

### Section 1 (Core Philosophy) — HOMEWORK_STANDARDS.md

**Section 1.2, Principle 1: "Textbook is Source of Truth, NETS is the Transformer"**

| What Textbook Does | What NETS Does |
|---|---|
| Provides core concepts | Forces REASONING with concepts |
| Presents information | Creates active engagement |
| Shows solved examples | Requires student to CONSTRUCT solutions |

> **STANDARD:** "Homework MUST NOT change core concepts from textbooks. It MUST adapt delivery method to active, gamified, AI-personalized learning."

Assessment: Clear, unambiguous language. The principle is defined as a mandatory standard, not a guideline.

---

### Section 5 (Textbook-to-NETS Content Adaptation) — HOMEWORK_STANDARDS.md

**Section 5.1 — The Adaptation Pipeline**

```
TEXTBOOK (Source) → AI REFINEMENT (Transform) → NETS HOMEWORK (Deliver)
```

**Section 5.2 — Explicit DO/DON'T Rules**

| DO | DON'T |
|---|---|
| ✅ Preserve core concepts exactly as in textbook | ❌ Change mathematical formulas or scientific facts |
| ✅ Add narrative layer for engagement | ❌ Alter historical dates or geographical information |
| ✅ Convert passive examples to active problems | ❌ Modify grammar rules or vocabulary definitions |
| ✅ Embed cultural context (Uzbek names, scenarios) | ❌ Remove essential prerequisite knowledge |
| ✅ Add gamification elements | ❌ Add content not aligned with textbook scope |

Assessment: The DON'T list is concrete and subject-specific, not vague. Each prohibition protects a factual domain (formulas, dates, grammar). This is robust non-destructive adaptation framing.

---

### P4–P5 (What NETS Is and Isn't) — NETS_PROPOSAL_SUMMARY.md

- **"Textbooks remain — source of truth."**
- **"NETS transforms HOW students engage with textbook content."**
- NETS is characterized as a "replacement architecture for content delivery, assessment, iteration" — NOT a replacement for content itself.

Assessment: Consistent with HOMEWORK_STANDARDS.md. The distinction between replacing *delivery* (allowed) and replacing *content* (not allowed) is clearly drawn.

---

### P39–P45 (Subject Philosophies) — NETS_PROPOSAL_SUMMARY.md

Each subject maintains a strict two-role split:

| Subject | Textbook's Role | NETS's Role |
|---|---|---|
| **Mathematics** | Teaches the concept | Forces student to REASON with it |
| **Reading** | Provides the texts | Deepens student's relationship WITH those texts |
| **Science** | Explains phenomena | Makes students THINK LIKE SCIENTISTS |
| **English** | Provides grammar and vocabulary | Builds ACTUAL FLUENCY through immersion |
| **History** | Presents events | Forces ANALYSIS of causation and significance |
| **Computer Science** | Introduces concepts | Gives HANDS-ON logical challenges |

P39 states the overarching principle:
> "Each subject in the curriculum has a core purpose... NETS's methods serve that purpose, not override it."

Assessment: Every subject philosophy is structured as *textbook provides content → NETS deepens engagement*. The architecture is non-destructive across all six subjects reviewed.

---

## Red Flags

### Flag 1 (Minor): "AI Refinement" Stage Lacks Constraints (Section 5.1)

**What:** The pipeline shows `TEXTBOOK → AI REFINEMENT → NETS HOMEWORK`. The label "AI Refinement" implies transformation, but Section 5.1 provides no definition of what refinement is allowed to do — it relies entirely on Section 5.2's DO/DON'T rules downstream.

**Risk:** If the AI refinement layer is implemented without explicit constraints bound to 5.2, there is an implementation risk that content could be silently altered (e.g., paraphrasing that distorts a scientific explanation, or simplifying a historical account in ways that change its meaning).

**Recommendation:** Add a definition of "AI Refinement" in Section 5.1 that explicitly limits the operation to: formatting, narrative framing, cultural contextualization, and difficulty scaffolding — with a prohibition on altering factual claims, formulas, or dates.

---

### Flag 2 (Minor): CS Progression May Exceed Textbook Scope (P45)

**What:** The Computer Science philosophy describes a grade-by-grade programming progression:

| Grade | Focus |
|---|---|
| 1–3 | Block-based coding, algorithmic puzzles |
| 4–6 | Basic programming concepts, debugging |
| 7–9 | Python/JavaScript basics, simple projects |
| 10–11 | AI/ML concepts, data structures |

This is a self-contained NETS curriculum, not clearly derived from textbook content.

**Risk:** The 5.2 DON'T rule states: "Add content not aligned with textbook scope." If Uzbekistan's existing CS textbooks for Grades 7–11 do not yet cover Python/JavaScript or AI/ML, this progression may introduce out-of-scope content, contradicting the source-of-truth principle.

**Recommendation:** Confirm that the CS progression maps to existing MoEN-approved textbook chapters for each grade band. If textbooks are absent or insufficient, document this explicitly as a NETS-supplemented subject and note it as an exception to Criterion 1 rather than a silent violation.

---

## Summary

| Area | Result | Notes |
|---|---|---|
| Core Philosophy (Section 1) | ✅ PASS | Explicit, mandatory standard language |
| Adaptation Pipeline (Section 5.1) | ⚠️ PASS with flag | "AI Refinement" step lacks inline constraints |
| Adaptation Rules (Section 5.2) | ✅ PASS | Concrete DO/DON'T list per domain |
| P4–P5 (What NETS Is/Isn't) | ✅ PASS | Consistent with standards doc |
| P39 Subject Overview | ✅ PASS | "Methods serve purpose, not override it" |
| Mathematics (P40) | ✅ PASS | Reasoning on textbook concepts |
| Reading (P41) | ✅ PASS | Texts sourced from textbook |
| Science (P42) | ✅ PASS | Phenomena from textbook, NETS adds inquiry |
| English (P43) | ✅ PASS | Grammar/vocab from textbook, NETS builds fluency |
| History (P44) | ✅ PASS | Events from textbook, NETS adds analysis |
| CS (P45) | ⚠️ PASS with flag | Progression may exceed textbook scope for upper grades |

**Overall: PASS.** The document architecture is fundamentally compliant with the textbook source-of-truth criterion. Two implementation-level flags should be addressed before production rollout to prevent silent violations at the AI layer (Flag 1) and the CS curriculum layer (Flag 2).
