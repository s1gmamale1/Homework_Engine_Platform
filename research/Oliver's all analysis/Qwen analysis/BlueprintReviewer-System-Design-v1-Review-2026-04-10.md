# Blueprint Review Report — NETS System Design v1

**Reviewer:** BlueprintReviewer Agent (ID: 2266e1c5-7d75-4ac2-91ba-b53fb16096e7)
**Date:** April 10, 2026
**Document Reviewed:** `NETS-System-Design-v1.md` (458 lines)
**Status:** ✅ **APPROVED WITH RECOMMENDATIONS**

---

## Executive Summary

The NETS System Design v1 is the **bridge document** between the framework era and the platform era. It introduces a 5-layer architecture, 5 Subject Family classifications, a 2-tier product overlay (Basic/Premium), and a persistent metagame (Bilim Bazasi). It is well-structured, philosophically consistent with the UNIFIED v2.0 constitution, and provides a clear implementation roadmap.

**Key Strengths:**
- ✅ Clean layered architecture with strict inheritance (nothing contradicts a higher layer)
- ✅ Subject Family classification solves the content production bottleneck elegantly
- ✅ Honest current-state benchmark (Section 1) — score-9 constitution with score-1 coverage
- ✅ Tier overlay designed as a thin delta, not duplicate frameworks
- ✅ Metagame (Bilim Bazasi) is ethically constrained — zero pay-to-win, zero real-money cosmetics
- ✅ Game-design patterns adopted AND refused with clear reasoning
- ✅ SOUL constraints restated and explicitly honored throughout
- ✅ 8 open questions identified and deferred properly — no unilateral assumptions
- ✅ Existing assets fold in cleanly (Section 8) — nothing deprecated
- ✅ Implementation roadmap sequenced by dependency, not calendar

**Outstanding Issues Requiring Attention:** (see detailed findings below)

---

## Critical Findings

### Finding 1: Subject Family Membership — History Placement
**Severity:** Medium
**Location:** Section 3.4 (Ijtimoiy Fanlari)

History is placed in Ijtimoiy Fanlari (Social Sciences) — which is the correct classification. The family description matches my History G5 framework review findings well: Story Mode as primary mechanic, Memory Palace for chronology, case reasoning for Boss format, Why Chain for causal chains.

**However**, the Ijtimoiy Fanlari section states "No multiple-choice for Grade 6+" for Boss format, which aligns with the UNIFIED spec. But my History G5 framework review flagged that G5 should allow up to 30% MC at Boss (due to working memory constraints at age 10-11). The System Design v1 doesn't explicitly call out the G5 MC exception at the family level.

**Recommendation:** Add a note to Section 3.4 that G5 Bosses may use up to 30% MC per ADR-005 (the same exception that applies to Aniq Fanlar). This ensures family-level rules don't accidentally block the G5-specific override.

---

### Finding 2: Tabiat Fanlari — G5 Science v3.0 as Prototype
**Severity:** Low
**Location:** Section 3.3, Section 10 (Question 6)

Section 3.3 correctly identifies `NETS-Science-Grade5-Merged-Framework.md` v3.0 as the Tabiat Fanlari prototype. Open Question 6 asks whether to derive the family framework from v3.0 (faster) or re-derive v3.0 downward from the family framework (cleaner).

**Assessment:** The recommendation in Question 6 is sound — derive the Tabiat Fanlari family framework from v3.0, then note deltas in a v3.1 resolution log. This is pragmatically the right approach since v3.0 is already validated.

**No action required** — this is flagged as a founder decision and the document's recommendation is reasonable.

---

### Finding 3: Metagame — BT Economy Not Calibrated
**Severity:** Medium
**Location:** Section 5.2, Section 10 (Question 5)

The Bilim Token economy formulas are deliberately not fixed ("must be calibrated through playtesting"). This is the right instinct but creates a gap: without ballpark numbers, the platform team cannot implement the economy, and the metagame cannot be tested.

**Recommendation:** Provide provisional ballpark numbers for Phase 4 playtesting, even if explicitly labeled as "pre-playtest estimates":
- Session completion: 10-15 BT
- Skill mastery: 25-50 BT
- Boss defeat: 30-60 BT
- Streak milestone (7 days): 50 BT
- Weekly PISA lesson: 40 BT
- Room unlock: 100-200 BT
- Hero unlock: 200-400 BT

These don't need to be final — they give the platform team something to implement for initial testing.

---

### Finding 4: Ijtimoiy Fanlari — Missing Custom Track Pattern
**Severity:** Medium
**Location:** Section 3.4

The Ijtimoiy Fanlari family section lists cognitive demands and mechanic emphasis but doesn't define the **custom reasoning track** pattern. Per the meta-rule in QWEN.md, every non-PISA-pure subject family needs a custom reasoning track:

| Subject Family | Custom Track |
|---|---|
| Aniq Fanlar | Formal Reasoning (FR) |
| Til Fanlari | Language Acquisition (LA) |
| Tabiat Fanlari | Scientific Reasoning (SR) |
| **Ijtimoiy Fanlari** | **❌ Not defined** |
| Tarbiya/Sanat | Expressive Formation (EF) |

**Recommendation:** Define Historical Reasoning (HR) or Social Reasoning (SoR) as the custom track for Ijtimoiy Fanlari:
- **HR-L1:** Recall and identify historical facts, figures, dates
- **HR-L2:** Explain cause-and-effect; classify sources
- **HR-L3:** Interpret and compare multiple sources/perspectives
- **HR-L4:** Synthesize evidence to construct historical arguments

This aligns with my History G5 framework review (Finding 3 in that report).

---

### Finding 5: Tarbiya/Sanat Family — Under-specified
**Severity:** Low
**Location:** Section 3.5

Section 3.5 (Tarbiya/Sanat) is intentionally minimal: "Lightweight, low-stakes creative tasks. No Boss in the standard sense." This is correct per the Chill Mode and Maker-First shapes. However, it's the thinnest family description by a significant margin.

**Concern:** When Tarbiya G5 (Chill Mode) and Tasviriy Sanat G5 (Maker-First) are complete frameworks, the family description should reference their specific mechanic emphases more precisely. Currently it just says "Expressive output" and "Reflection Journal" — which undersells what those frameworks actually do.

**Recommendation:** Expand Section 3.5 after the Tarbiya G5 and Tasviriy Sanat G5 frameworks are used as prototypes. The family description should be derived upward from validated subject frameworks, not written from scratch.

---

### Finding 6: Layer 3 (Tier Overlay) — "Premium adds depth, not gating" Needs Sharper Definition
**Severity:** Medium
**Location:** Section 4

The principle "Basic delivers full learning; Premium adds depth, not gating" is philosophically sound. But the actual differentiation is:

| Dimension | Basic | Premium |
|---|---|---|
| Difficulty band | Standard | Harder |
| AI tier | T1+T2 | +T3 |
| Games | 1-2 interactive per 3-5 sessions | Unlimited |
| PISA lessons | Standard monthly | Weekly |

The concern is that **"harder difficulty band" for Premium** could create a perception problem: if Premium students are consistently working at higher PISA levels, does this create a two-track system where Premium students accelerate faster academically?

**Recommendation:** Clarify that "harder difficulty band" means Premium students get more L4-L5 stretch tasks within their **current** PISA level, not that they skip to higher levels faster. The PISA progression curve should be the same for both tiers — Premium students just get richer practice at each step.

---

### Finding 7: AI Tier Strategy — Ollama Reference
**Severity:** Low
**Location:** Section 6

Section 6 mentions: "The current local implementation uses Ollama with a quantized Qwen model." This is implementation-specific detail that may become outdated quickly.

**Recommendation:** Move the Ollama reference to a footnote or implementation note rather than the main body. The architectural principle is "small, cost-effective LLM for Tier 2" — the specific tool (Ollama, Qwen, etc.) is an implementation detail.

---

### Finding 8: App Surfaces — Missing "What Happens When Student Has No Internet?"
**Severity:** Medium
**Location:** Section 7

Section 7 describes 5 app surfaces (Today, Bilim Bazasi, Library, Tournaments, Teacher Dashboard). But the document acknowledges rural electricity outages and shared family smartphones in Section 5.5. There's no offline-first strategy described.

**Given that 89-93% mobile penetration is the target (per QWEN.md), 7-11% of students may have intermittent access.** The homework engine needs an offline mode: download a session, complete it offline, sync results when connected.

**Recommendation:** Add a Section 7.6 or note describing the offline-first strategy:
- Session content downloadable in advance
- Local answer storage with sync-on-connect
- Streak protection for offline days
- Anti-cheat considerations for offline mode (reduced monitoring, but not zero)

---

## Consistency Analysis

### UNIFIED v2.0 Constitution Compliance

| UNIFIED Rule | System Design v1 Compliance |
|---|---|
| 7-phase session structure | ✅ Inherited at Layer 0, locked |
| Textbook-first principle | ✅ Explicitly restated in Section 11 (Principle 1) |
| `transition_skill` tag mandatory | ✅ Restated in Section 11 (Principle 2) |
| No MC for Grade 6+ | ✅ Mentioned in family sections |
| 60% pass floor | ✅ Inherited at Layer 0 |
| 5 unbreakable principles | ✅ Restated and honored in Section 11 |
| PISA calibration | ✅ Referenced in all family sections |
| AI tier cost model ($3-5/student/year) | ✅ Section 6 matches UNIFIED |
| Dual-catalog game selection | ✅ Section 8 confirms inheritance |
| Hidden difficulty | ✅ Section 11 (Principle 3) |

### Internal Consistency

| Dimension | Consistency Check |
|---|---|
| Layer hierarchy strictness | ✅ "Nothing in lower layer may contradict higher layer" — enforced |
| Family membership stability | ✅ Locked, requires formal decision log |
| Mechanic bans | ✅ Cannot be re-enabled at subject level without ADR |
| Tier differentiation | ✅ "Basic delivers full learning" — no academic gating |
| Metagame ethics | ✅ No real-money entry point, zero pay-to-win |
| Open questions | ✅ 8 identified, none resolved unilaterally |

---

## Cross-Reference with Previous Reviews

### Validated by History G5 Framework Review

My History G5 framework review (BlueprintReviewer-History-G5-Review-2026-04-10) found:
- **Missing custom HR track** → Confirmed here (Finding 4)
- **Framework shape not declared** → Resolved: History is Ijtimoiy Fanlari → PISA-rigorous shape
- **Scholar pairing incomplete** → System Design v1 doesn't address this at family level — still a subject-layer issue

### Gaps in System Design v1 that affect subject frameworks

1. **G5 MC exception at family level** — History G5 framework allows 30% MC at Boss, but Ijtimoiy Fanlari says "No MC for Grade 6+" without G5 exception
2. **Offline strategy** — Affects all subject frameworks' content delivery assumptions
3. **BT economy calibration** — Affects how subject frameworks' reward systems integrate with metagame

---

## Prioritized Recommendations

### Must-Add Before Platform Implementation (3 items):
1. **Define custom reasoning track for Ijtimoiy Fanlari** (Finding 4) — HR-L1 → HR-L4
2. **Clarify G5 MC exception at family level** (Finding 1) — Add to Section 3.4
3. **Add offline-first strategy** (Finding 8) — Critical for 7-11% of students with intermittent access

### Should-Add Before Family Framework Production (3 items):
4. **Provide provisional BT economy numbers** (Finding 3) — Even as "pre-playtest estimates"
5. **Clarify Premium difficulty differentiation** (Finding 6) — Same PISA progression curve, richer practice
6. **Move Ollama reference to footnote** (Finding 7) — Keep architecture document tool-agnostic

### Nice-to-Have (2 items):
7. **Expand Tarbiya/Sanat after prototype frameworks used** (Finding 5)
8. **Resolve Open Question 6** (G5 Science v3.0 → family framework direction) — Founder decision

---

## Overall Assessment

**Score: 8.5/10 — APPROVED WITH RECOMMENDATIONS**

The NETS System Design v1 is a **strong architectural document** that successfully bridges the framework era and platform era. The 5-layer hierarchy is clean, the Subject Family classification is the highest-leverage decision in the pipeline, and the metagame design is ethically sound.

The 8 open questions are properly identified and deferred — this is a sign of architectural maturity, not incompleteness. The document doesn't pretend to know what it doesn't know.

**Main gaps:** Missing custom reasoning track for Ijtimoiy Fanlari, no offline strategy, and BT economy needs provisional numbers for implementation. These are additive, not contradictory.

**Estimated effort to address must-add items:** 2-3 hours of document revision.

---

## Next Steps

1. **Address 3 must-add items** (Ijtimoiy custom track, G5 MC exception, offline strategy)
2. **Address 3 should-add items** (BT numbers, Premium clarity, Ollama footnote)
3. **Begin Phase 1 of roadmap:** Write the 5 Subject Family Frameworks (Tabiat Fanlari first)
4. **Resolve Open Question 6** — Founder decision on G5 Science v3.0 → family framework direction
5. **Resolve Open Question 5** — BT economy provisional numbers for playtesting
6. **Proceed to platform implementation** once family frameworks are complete

---

**Reviewed by:** BlueprintReviewer Agent
**Review Date:** April 10, 2026
**Document:** NETS-System-Design-v1.md
**Verdict:** ✅ Approved with Recommendations — 3 must-add items pending
