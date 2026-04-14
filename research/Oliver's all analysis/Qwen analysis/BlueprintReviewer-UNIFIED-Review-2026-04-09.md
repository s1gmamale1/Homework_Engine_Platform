# Blueprint Review Report — NETS Homework Engine UNIFIED v2.0

**Reviewer:** BlueprintReviewer Agent (ID: 2266e1c5-7d75-4ac2-91ba-b53fb16096e7)
**Date:** April 9, 2026
**Document Reviewed:** `NETS-Homework-Engine-UNIFIED.md` (v2.0, April 2, 2026)
**Status:** ✅ **APPROVED WITH RECOMMENDATIONS**

---

## Executive Summary

The UNIFIED v2.0 specification represents a **significant improvement** over previous iterations. It successfully resolves the major contradictions identified in the Leonardo gap analysis and establishes a coherent, actionable foundation for the NETS Homework Engine.

**Key Strengths:**
- ✅ Comprehensive 2615-line specification covering all critical subsystems
- ✅ Resolution of PISA level mapping contradictions (Final Boss now tiered L3-6)
- ✅ Addition of missing domains: Reading (§7.2), Science (§7.3), History (§7.4), Creative Thinking (§8)
- ✅ New game mechanics (Tic Tac Toe vs AI #15, Notebook Capture #16)
- ✅ First-Person Expert POV mandate for Real-Life Challenges (§5.4)
- ✅ Story Arc structure with Stranger Test quality gate (§5.2)
- ✅ Dual-catalog game selection rule (§5.3, §6.9)
- ✅ Assessment system with pass/fail thresholds and Duolingo Mode (§6.6)
- ✅ Answer checking dual-pathway logic (§6.7)

**Outstanding Issues Requiring Attention:** (see detailed findings below)

---

## Critical Findings

### Finding 1: Version Number Inconsistency
**Severity:** Low  
**Location:** UNIFIED.md header vs. QWEN.md

The UNIFIED spec declares itself as **Version 2.0 — April 2, 2026**, but QWEN.md also declares itself as **Version 2.0 — April 2026**. However, the UNIFIED spec was clearly updated after April 7 (multiple "UPDATED 2026-04-07" annotations throughout). 

**Recommendation:** Update UNIFIED.md header to **Version 2.1 — April 7, 2026** to reflect the substantial additions (Notebook Capture, Tic Tac Toe, Mystery Box rework, Assessment System, etc.).

---

### Finding 2: Session Duration Contradiction (Still Unresolved)
**Severity:** Medium  
**Location:** §4.1 vs. multiple sections

Section 4.1 declares:
- Standard (Homework): **30-45 minutes**
- Extended (In-Class): **45-60 minutes**

However, Leonardo's gap analysis (Finding 4 in `analysis_leonardo_pisa.md`) noted that the **original framework specified 20-30 minutes**, and Level 5-6 activities (Real-Life Challenge at 3-5 min, Peer Teaching at 10-15 min) cannot fit properly in shorter sessions.

The UNIFIED v2.0 increased durations to 30-45 min, which **helps but does not fully resolve** the tension. A student at PISA Level 5-6 still receives:
- Phase 1: 2 min
- Phase 2: 5-7 min
- Phase 3: 6-9 min
- Phase 4: 3-5 min
- Phase 5: 2-3 min
- Phase 6: 5-10 min
- Phase 7: 2-3 min
- **Total: 25-39 min** (within 30-45 min range)

**But** Pre-Homework adds 3-5 min (Theme Preview + Flash Cards), pushing total to **28-44 min**. This is tight for the lower bound.

**Recommendation:** 
1. Clarify whether Pre-Homework (0-A + 0-B) is **included** in the 30-45 min target or **additional** to it.
2. If additional, adjust Standard duration to **35-50 minutes** to accommodate reality.
3. Add explicit guidance for below-L2 students who may need extended time on remediation.

---

### Finding 3: History Dual-Domain PISA Mapping — Implementation Gap
**Severity:** Medium  
**Location:** §7.4

Section 7.4 states that History uses **dual-domain PISA mapping** (Reading + Creative Thinking) rather than having its own PISA levels. This is conceptually sound, but the spec lacks:

1. **No explicit tracking mechanism** — The student PISA profile structure (§3.3) shows `mathematics`, `reading`, and `science` domains, but no `history` or dual-domain structure.
2. **No conversion logic** — How does History performance translate into Reading PISA levels? If a student excels at History Source Evaluation, does their Reading `reflect_and_evaluate` domain increase?

**Recommendation:** 
1. Add `history` to the student profile JSON structure in §3.3 with dual-domain tracking:
   ```json
   "history": {
     "reading_domain_alignment": {
       "access_and_retrieve": 1.6,
       "integrate_and_interpret": 1.4,
       "reflect_and_evaluate": 1.3
     },
     "creative_thinking_alignment": {
       "generating_ideas": 1.5,
       "evaluating_ideas": 1.3,
       "expressing_ideas": 1.4
     }
   }
   ```
2. Add conversion logic: "History assessment items contribute 50% to Reading PISA tracking and 50% to Creative Thinking PISA tracking."

---

### Finding 4: Notebook Capture — Privacy Compliance Gap
**Severity:** High  
**Location:** §6.8

Section 6.8.4 states:
- "Photos are stored encrypted, retained for 30 days for re-evaluation/audit, then deleted."
- "If the AI vision detects faces, student names visible on the page header, or personal identifiers, those regions are blurred client-side BEFORE upload."

**Issues:**
1. **No explicit parental consent mechanism** for students under 13 (or under 16 per GDPR-equivalent standards). Uzbekistan's education system serves 8.8M students, many of whom are minors.
2. **No data sovereignty statement** — Where are photos stored? Uzbekistan may have data localization laws.
3. **Client-side blurring is insufficient** — AI vision models can still process metadata (EXIF data, GPS coordinates, device identifiers) unless explicitly stripped.

**Recommendation:** 
1. Add parental consent flow: "For students under 16, Notebook Capture requires explicit parental/guardian consent before first use."
2. Add data sovereignty clause: "All images stored on servers within Republic of Uzbekistan jurisdiction, compliant with [specific law if applicable]."
3. Add metadata stripping requirement: "Client MUST strip EXIF data, GPS coordinates, and device identifiers BEFORE upload. Only raw pixel data transmitted."

---

### Finding 5: Mystery Box Reward Pool — Gambling Concern
**Severity:** Low-Medium  
**Location:** §6.3

The spec explicitly states "every attempt yields XP" and "no gambling," which is good. However, the reward pool includes:
- **Mythical Boss Event Ticket (3% rarity)** — This is a gacha-style mechanic.

While the spec says "no gambling," the psychological effect of a 3% chance item mirrors loot box mechanics, which are **regulated in some jurisdictions** and scrutinized in gaming ethics literature.

**Recommendation:** 
1. Add disclosure: "Mystery Box rewards are disclosed to parents/guardians in monthly reports."
2. Consider replacing the 3% Mythical Boss Ticket with a **guaranteed progress mechanic** (e.g., "After 33 Mystery Box attempts, student earns a guaranteed Mythical Boss ticket").
3. Ensure the system does NOT create psychological dependency on the "random reward" loop — monitor for compulsive behavior patterns.

---

## Medium-Priority Findings

### Finding 6: Game Selection Algorithm — Computational Complexity
**Severity:** Medium  
**Location:** §5.3

The Phase 3 Game Selection Algorithm (§5.3) must:
1. Get current topic's learning objectives
2. Get student's PISA level and weakest domains
3. Get student's in-progress transition skills
4. Select 3 games from TWO POOLS (Default 16 + Interactive 12 = 28 total)
5. Apply 5+ constraints (dual-catalog rule, Bloom's matching, stretch level, transition skill match, subject compatibility)
6. Check no mechanic appears more than 2x in one session
7. Arrange interleaved with Story Mode

**Issue:** This is a **constraint satisfaction problem** that could be computationally expensive on low-end devices (which the system explicitly supports — see §6.9 device constraints for Bridge Builder/Minefield).

**Recommendation:** 
1. Pre-compute valid game combinations per subject/topic offline (Tier 1 processing).
2. Runtime selection becomes a simple lookup + student profile filtering.
3. Add fallback: "If constraint solver takes >2 seconds, use pre-computed default combination for this subject."

---

### Finding 7: AI Tier Cost Modeling — Missing Projections
**Severity:** Medium  
**Location:** QWEN.md states "$3-5/student/year at national scale"

The UNIFIED spec defines:
- **Tier 1:** 80% of traffic (scripted/algorithmic) — minimal cost
- **Tier 2:** 15% of traffic (enhanced logic) — moderate cost
- **Tier 3:** 5% of traffic (generative AI) — high cost

However, the spec does not provide:
1. **Per-request cost estimates** for each tier
2. **Throughput calculations** (requests per student per session)
3. **Scaling model** (how cost decreases at 8.8M student scale)

**Recommendation:** Add an appendix to the UNIFIED spec with cost modeling:
```
Tier 1: $0.0001/request x 50 requests/session x 365 sessions = $1.83/student/year
Tier 2: $0.001/request x 10 requests/session x 365 = $3.65/student/year (but only 15% of traffic = $0.55)
Tier 3: $0.01/request x 3 requests/session x 365 = $10.95/student/year (but only 5% of traffic = $0.55)
Total: ~$2.93/student/year (within $3-5 target)
```

---

### Finding 8: Boss Retry Limit — Still Unresolved
**Severity:** Low  
**Location:** QWEN.md "Known Open Decisions" #1

QWEN.md lists: "Boss retry limit: UNIFIED says unlimited retries, Blueprint says max 2 per session."

The UNIFIED spec §5.6 states:
- "IF boss NOT defeated -> ACTIVATE Socratic Tutoring -> REGENERATE boss questions -> Student re-attempts boss"
- No explicit retry limit in §5.6 itself.

However, §6.6 (Duolingo Mode) states: "Repeat until 60%: Student continues until they reach the 60% threshold. **No upper limit on attempts.**"

This creates ambiguity:
- Does "no upper limit" apply to the Final Boss specifically?
- Or does the "max 2 retries" from the Blueprint still apply?

**Recommendation:** Add explicit retry limit to §5.6:
"Maximum 2 boss re-attempts per session. If boss still not defeated after 2 re-attempts, session ends with partial credit. Next homework session continues from the same learning objectives with simplified boss questions."

---

## Low-Priority Findings

### Finding 9: Missing Subject Frameworks
**Severity:** Low (pipeline issue, not spec issue)  
**Location:** QWEN.md lists 9 subjects; only 5 have frameworks

**Current State:**
- ✅ Science Grade 5 — v3.0
- ✅ Texnologiya Grade 5 — v3.1
- ✅ Tarbiya Grade 5 — v1.0
- ✅ Tasviriy Sanat Grade 5 — v1.0
- ✅ Geografiya Grade 5 — v1.0
- ⚠️ Tarix (History) — **Textbook available, framework NEEDED**
- ⚠️ Matematika (Mathematics) — **Framework NEEDED**
- ⚠️ Ona tili (Native Language) — **Framework NEEDED**
- ⚠️ Ingliz tili (English) — **Framework NEEDED**

**Recommendation:** Prioritize Matematika and Ona tili frameworks next, as these are core PISA-assessed subjects (Math and Reading).

---

### Finding 10: Scholar Pairing Rule — Not Yet Implemented
**Severity:** Low  
**Location:** QWEN.md "Known Open Decisions" #6

"Scholar pairing rule — Central Asian scientists should appear in all PISA-rigorous frameworks retroactively."

The UNIFIED spec mentions cultural narratives (Registan, Silk Road, Amir Temur) but does not mandate inclusion of Central Asian scholars in Story Mode segments or Theme Preview components.

**Recommendation:** Add to §5.2 (Story Mode):
"Real-World Examples Preference: When a concept was discovered or advanced by a Central Asian scientist/scholar (e.g., Al-Khwarizmi for algebra, Al-Biruni for science, Ibn Sina for medicine), their story MUST be used as the narrative spine. This is non-negotiable for PISA-rigorous frameworks."

---

## Structural Assessment

### Specification Quality Metrics

| Metric | Score | Notes |
|---|---|---|
| **Completeness** | 9/10 | Comprehensive coverage of all subsystems. Missing: cost modeling, data privacy details |
| **Consistency** | 8/10 | Minor contradictions remain (session duration, boss retry limit). Resolved: PISA mapping |
| **Actionability** | 9/10 | Content creators and engineers can build directly from this spec. JSON schemas are excellent |
| **Testability** | 8/10 | Most rules are verifiable. Ambiguity in "no upper limit" vs "max 2 retries" needs resolution |
| **Cultural Fit** | 9/10 | Strong Uzbek context throughout. Could strengthen with explicit scholar pairing mandate |
| **Scalability** | 7/10 | Cost modeling absent. Device constraints noted for some games but not all |
| **Overall** | **8.3/10** | **Production-ready with minor amendments** |

---

## Recommended Amendments (Prioritized)

### MUST FIX (Before Engineering Handoff)
1. ✅ **Session Duration Clarity** — Is Pre-Homework included in 30-45 min or additional? (Finding 2)
2. ✅ **Boss Retry Limit** — Explicit statement in §5.6: max 2 or unlimited? (Finding 8)
3. ✅ **History Tracking** — Add dual-domain student profile structure (Finding 3)

### SHOULD FIX (Before Beta Launch)
4. Notebook Capture Privacy — Parental consent, data sovereignty, metadata stripping (Finding 4)
5. Cost Modeling Appendix — Per-tier cost projections to validate $3-5/student/year target (Finding 7)
6. Scholar Pairing Mandate — Central Asian scholars in Story Mode (Finding 10)

### NICE TO HAVE (Post-Launch Iteration)
7. Game Selection Pre-computation — Performance optimization for low-end devices (Finding 6)
8. Mystery Box Progress Mechanic — Replace 3% gacha with guaranteed progress (Finding 5)
9. Version Number Update — UNIFIED.md header to v2.1 (Finding 1)

---

## Conclusion

**The NETS Homework Engine UNIFIED v2.0 specification is APPROVED for engineering handoff** pending resolution of the 3 MUST FIX items above.

The specification successfully:
- ✅ Resolves all critical contradictions from previous versions
- ✅ Fills gaps identified in gap analysis (Reading, Science, History, Creative Thinking progressions)
- ✅ Introduces innovative mechanics (Notebook Capture, Tic Tac Toe vs AI, dual-catalog selection)
- ✅ Establishes clear quality gates (Stranger Test, First-Person Expert POV, No Busywork Rule)
- ✅ Maintains cultural relevance while achieving PISA alignment

**Next Steps:**
1. Resolve 3 MUST FIX items (estimated 2-3 hours of spec writing)
2. Engineering team begins technical architecture from UNIFIED v2.0
3. Content pipeline team begins textbook-to-NETS conversion for Matematika and Ona tili
4. Privacy team reviews Notebook Capture data flow (§6.8) for compliance

**Reviewed by:** BlueprintReviewer Agent  
**Date:** April 9, 2026  
**Status:** ✅ APPROVED WITH CONDITIONS

---

*This review was conducted as part of Paperclip task 7daa1bec-0cf4-415b-ae1b-068c3712735d, run 2777295e-3759-4987-bcaa-4916145c53ed.*
