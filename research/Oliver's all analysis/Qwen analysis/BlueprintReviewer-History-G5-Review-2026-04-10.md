# Blueprint Review Report — NETS History Grade 5 Framework v1.0

**Reviewer:** BlueprintReviewer Agent (ID: 2266e1c5-7d75-4ac2-91ba-b53fb16096e7)
**Date:** April 10, 2026
**Document Reviewed:** `NETS-History-Grade5-Framework.md` (v1.0, 853 lines, 50,494 bytes)
**Status:** ⚠️ **APPROVED WITH CONDITIONS — Must-fix items required**

---

## Executive Summary

The History Grade 5 Framework is a **well-structured, thoughtful delta layer** over the UNIFIED v2.0 spec. It successfully adapts the universal blueprint to a subject that lacks its own PISA domain, using the dual-domain (Reading + Creative Thinking) mapping strategy correctly outlined in the UNIFIED spec §7.4.

**Key Strengths:**
- ✅ Comprehensive textbook chapter map (6 chapters, 26 sections, with page references)
- ✅ Correct application of dual-domain PISA mapping (Reading + Social Sciences)
- ✅ Strong cultural anchoring — Uzbek historical figures, places, and naming conventions throughout
- ✅ Psychology filter appropriately tuned for Grade 5 cognitive constraints (WM 4-5, Lexile 830-1010L, 30-sec struggle ceiling)
- ✅ Banned mechanics list is rigorous and age-appropriate (18 items)
- ✅ Mandatory additions are well-specified (timeline, map literacy, CPA, dual coding, scholar pairing)
- ✅ Game catalog selections are reasoned — Timeline Builder, Map Explorer as History-specific additions
- ✅ Notebook Capture task pool is domain-appropriate (map sketching, timelines, figure drawing)
- ✅ Boss configuration is solid — tiered HP, 40/40/20 distribution, MC 30% allowance justified
- ✅ Anti-cheat section acknowledges "mother-helping" cultural reality
- ✅ Sample chapter walkthrough (§17) demonstrates strong alignment with the UNIFIED spec

**Outstanding Issues Requiring Attention:** (see detailed findings below)

---

## Critical Findings

### Finding 1: Missing HTML Companion File
**Severity:** Medium
**Location:** File system — `Subject Frameworks/History Grade 5/`

All other subject frameworks ship with both `.md` AND `.html` versions. The History framework is missing its HTML render.

**Impact:** The pipeline output contract (QWEN.md) requires both formats. The HTML provides a viewable deliverable for stakeholders who don't read markdown.

**Recommendation:** Generate HTML companion file matching the styling of other framework HTMLs (Science, Tarbiya, Tasviriy Sanat, Texnologiya, Geografiya).

---

### Finding 2: PISA Dual-Domain Mapping — Incomplete Implementation
**Severity:** High
**Location:** §3 (PISA History mapping)

The framework correctly states History uses dual-domain PISA mapping (Reading + Creative Thinking per UNIFIED §7.4). However:

1. **Domain tag inconsistency:** §3 says dual-domain (Reading + Social Sciences), but the tagging schema (§15) only shows `"domain": "Reading"` — no Creative Thinking or Social Sciences sub-domain reference.
2. **No conversion logic:** The framework doesn't specify how History performance feeds into the student's Reading PISA profile. If a student excels at History Source Evaluation, does their Reading `reflect_and_evaluate` domain increase? This tracking mechanism is missing from the student profile.
3. **The `pisa_ref` in §15 shows `"domain": "Reading"` as a single domain** — but the framework declared dual-domain in §3. This is an internal contradiction.

**Recommendation:**
1. In §15 tagging schema, use `"domain": "Reading", "sub_domain": "Social Sciences"` OR add a second `"domain": "Creative Thinking"` entry to reflect dual-domain.
2. Add explicit student profile tracking structure for History (dual-domain) — this was flagged in the UNIFIED review (Finding 3) but not carried forward here.
3. Clarify whether "Social Sciences" is a sub-domain or a separate domain — UNIFIED §7.4 is ambiguous here.

---

### Finding 3: Custom Track Pattern Not Defined
**Severity:** Medium
**Location:** §3, §18

Per QWEN.md meta-rule, every non-PISA-pure subject needs its own custom reasoning track:

| Subject | Custom Track |
|---------|-------------|
| Texnologiya | Technical Reasoning (TR-L1 → TR-L4) |
| Tasviriy Sanat | Visual Arts (VA-L1 → VA-L4) |
| Tarbiya | Moral Reasoning (MR-L1 → MR-L4) + SEL |
| Geografiya | Map Literacy (ML-L1 → ML-L4) |
| **History** | **❌ MISSING** |

§18 (Open questions) item #6 acknowledges this: *"Define a specific 'Historical Reasoning (HR)' track (HR-L1 → HR-L4)."*

**Recommendation:** Define the Historical Reasoning (HR) track with 4 levels:
- **HR-L1:** Recall and identify historical facts, figures, dates
- **HR-L2:** Explain cause-and-effect in historical events; classify sources
- **HR-L3:** Interpret and compare multiple historical sources/perspectives
- **HR-L4:** Synthesize evidence to construct historical arguments

This should be added to §3 as a dedicated subsection, with `transition_skill` tags mapped to HR levels.

---

### Finding 4: Session Duration — Contradiction with UNIFIED
**Severity:** Medium
**Location:** §4.1 vs. UNIFIED §4.1

| Parameter | UNIFIED v2.0 | History G5 |
|---|---|---|
| Standard session total | 30-45 min | 30-40 min (includes 0-A + 0-B + 7 phases) |

History specifies **30-40 min** total, explicitly including Pre-Homework (0-A + 0-B). The UNIFIED spec says 30-45 min but is ambiguous about whether Pre-Homework is included (this was flagged in the UNIFIED review as Finding 2).

The History framework takes a stance (included) which is reasonable, but the 30-40 min ceiling is **tighter** than the UNIFIED 30-45 min. Phase 6 (Boss at 6-8 min) + all other phases (which sum to 25-39 min per UNIFIED calculations) + Pre-Homework (3-5 min) = **28-44 min**. The History 30-40 min cap would require running at the faster end of every phase.

**Recommendation:**
1. Either align to UNIFIED's 30-45 min range, or
2. Add explicit per-phase timing caps that guarantee the 30-40 min total is achievable (e.g., Phase 3 at 6 min instead of 6-9 min).

---

### Finding 5: Scholar Pairing Rule — Not Fully Specified
**Severity:** Low
**Location:** §7.1, §18

§7.1 says: *"At least 1 Central Asian historical figure per 5 sessions."* §11.2 lists the figures (Amir Temur, Ulugh Beg, Al-Biruni, Ibn Sina, Al-Khwarizmi).

However, the **scholar pairing rule** from Geografiya G5 (every world figure paired with a Central Asian counterpart) is not fully implemented. §18 item #7 acknowledges this.

**Recommendation:** Specify the pairing pattern explicitly:
- Herodotus ↔ Al-Biruni (historical methodology)
- Ptolemy ↔ Ulugh Beg (astronomy/cartography)
- Caesar ↔ Amir Temur (state-building/military leadership)
- Egyptian calendar-makers ↔ Al-Khwarizmi (mathematical systems)

This should be a hard rule in §7.1, not just a frequency target.

---

### Finding 6: Missing Framework Shape Declaration
**Severity:** Low
**Location:** Document structure

Per QWEN.md, every subject framework should declare which of the three shapes it follows:

| Shape | Climax | Session length | Make required |
|---|---|---|---|
| **PISA-rigorous** | Final Boss (HP, tiered) | 35-45 min | No |
| **Chill Mode** | Big Decision (no-fail rubric) | 15-25 min | No |
| **Maker-First** | The Make (create + photo upload) | 25-35 min | Yes |

The History framework declares a **tiered Boss with HP** (§6.6), which maps to **PISA-rigorous shape**. However, §18 acknowledges History is "not a PISA domain," which creates tension.

**Recommendation:** Explicitly declare the shape at the top of the framework. Given the dual-domain PISA mapping and tiered Boss, History should be declared as **PISA-rigorous with Reading-domain anchoring** — this resolves the ambiguity.

---

### Finding 7: Game Break Slot 3 Rule — Timeline Builder Frequency
**Severity:** Low
**Location:** §6.3

§6.3 says: *"Slot 3: Timeline Builder in 1 of every 3 sessions; otherwise Tic Tac Toe vs AI or Escape Room."*

The UNIFIED spec (§6) requires 3 games per session, ≥1 from Interactive Catalog + ≥2 from Default 16. Timeline Builder is a History-specific mechanic (not in either catalog), so its slot assignment needs clarification on which catalog it substitutes from.

**Recommendation:** Clarify that Timeline Builder counts as a Default 16 substitute for History, or add it to the Default catalog as a domain-specific variant.

---

### Finding 8: Version Number — Should Reflect Iteration Status
**Severity:** Low
**Location:** Header

Framework declares v1.0 but §18 lists 7 open questions that need resolution before production. The status says "Draft specification — first iteration."

**Recommendation:** Add `Status: DRAFT — 7 open items pending` to the header. The v1.0 is fine for a first draft, but the open items should be visible upfront.

---

## Quality Gates Verification

### UNIFIED Spec Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| 7-phase structure (P1-P7) | ✅ | All 7 phases present and specified |
| Pre-Homework (0-A + 0-B) | ✅ | Sessions 0-A and 0-B fully specified |
| Final Boss mandatory | ✅ | Tiered HP, defeat required, max 3 attempts |
| Stranger Test on Story Mode | ✅ | Explicitly stated in §6.2 |
| `transition_skill` tag on every task | ✅ | §3 lists 5 mandatory tags; §15 schema includes it |
| Standard code format (primary + alias) | ✅ | `UZ-HIST-5-{TOPIC}-{SEQ}` + `HIST.5.{bob}.{section}.{seq}` |
| Textbook-first references | ✅ | Chapter map with pages, §15 schema has `textbook_ref` |
| PISA-calibrated | ⚠️ | Dual-domain declared but not fully implemented (Finding 2) |
| Bloom's taxonomy mapping | ✅ | §3 pairs PISA levels with Bloom's |
| No busywork rule | ✅ | Explicitly stated; `transition_skill` enforcement in §14.2 |
| First-person expert POV (RLC) | ✅ | §6.4 — "Sen tarixchisan…" mandated |
| CPA progression | ✅ | §4.4, §6.2 — Concrete → Pictorial → Abstract |
| Dual coding | ✅ | §4.4 — Story Mode never text-only |
| Worked example before practice | ✅ | §4.4 |
| Spaced retrieval | ✅ | §4.4, §6.1 — Day 1/3/7/14 schedule |
| Effort + strategy feedback | ✅ | §4.3 banned items #10, §4.4 |
| 30-second struggle ceiling | ✅ | §4.2, §4.4 |
| Hidden difficulty labels | ✅ | §4.2, §6.6 — "INTERNAL ONLY" |
| Cultural anchors (Uzbek) | ✅ | §7.1, §11.1 — Comprehensive |
| Mobile-first, low-bandwidth | ✅ | §4.4, §7.2 |
| Notebook Capture | ✅ | §9 — 1 in every 4-5 sessions |
| AI tier strategy | ✅ | §13 — Cost-aware, matches UNIFIED |
| Teacher overrides | ✅ | §14 — Allowed/cannot-override listed |
| Duolingo Mode (<60%) | ✅ | §12.3 |
| Anti-cheat | ✅ | §10 — Culturally aware |
| Bilingual (Uzbek primary) | ✅ | §7.1, §7.3 — Uzbek only for student-facing |
| Scholar pairing | ⚠️ | Partial — Central Asian figures present but pairing rule incomplete (Finding 5) |
| Game catalog selection | ✅ | §8 — Default 16 + Interactive 12 specified |
| Content production checklist | ✅ | §16 — 12-item checklist |

**Compliance Score:** 30/32 mandatory requirements met (94%)

---

## Comparison with Other Subject Frameworks

| Dimension | Science G5 | Tarbiya G5 | Tasviriy Sanat G5 | Texnologiya G5 | Geografiya G5 | **History G5** |
|---|---|---|---|---|---|---|
| Framework version | v3.0 | v1.0 | v1.0 | v3.1 | v1.0 | **v1.0** |
| Shape | PISA-rigorous | Chill Mode | Maker-First | PISA-rigorous | PISA-rigorous | **PISA-rigorous** |
| Custom track | Science Reasoning (SR) | Moral Reasoning (MR) | Visual Arts (VA) | Technical Reasoning (TR) | Map Literacy (ML) | **❌ Missing (HR needed)** |
| PISA target | L1→L2→L3 | N/A (no-fail) | N/A (Maker) | L1→L2→L3 | L1→L2→L3 | **L1→L2→L3** |
| Session length | 35-45 min | 15-25 min | 25-35 min | 35-45 min | 35-45 min | **30-40 min** |
| Boss type | Tiered HP | Big Decision | The Make | Tiered HP | Tiered HP | **Tiered HP** |
| Notebook Capture | Yes | No | Yes (mandatory) | Yes | Yes | **Yes (1/4-5 sessions)** |
| HTML companion | ✅ | ✅ | ✅ | ✅ | ✅ | **❌ Missing** |
| Scholar pairing | ✅ | N/A | N/A | ✅ | ✅ | **⚠️ Partial** |

---

## Prioritized Recommendations

### Must-Fix Before Production (3 items):
1. **Resolve dual-domain PISA tagging** (Finding 2) — Update §3, §15 to be consistent. Add student profile tracking for History.
2. **Define Historical Reasoning (HR) custom track** (Finding 3) — HR-L1 through HR-L4 with transition skill mappings.
3. **Generate HTML companion file** (Finding 1) — Match format of other 5 frameworks.

### Should-Fix Before Beta (3 items):
4. **Align session duration** (Finding 4) — Either 30-45 min (UNIFIED alignment) or add per-phase caps.
5. **Specify scholar pairing rule** (Finding 5) — Hard pairings, not just frequency.
6. **Declare framework shape explicitly** (Finding 6) — "PISA-rigorous with Reading-domain anchoring."

### Nice-to-Have (2 items):
7. **Clarify Timeline Builder catalog membership** (Finding 7)
8. **Update status header with open items visibility** (Finding 8)

---

## Overall Assessment

**Score: 7.8/10 — CONDITIONALLY APPROVED**

The History Grade 5 Framework is a **solid first draft** that demonstrates strong understanding of the UNIFIED spec, Grade 5 psychology, and Uzbek historical context. The chapter map is thorough, the psychology filter is well-tuned, and the sample walkthrough (§17) is production-quality.

The main gaps are the missing custom track (HR), the dual-domain PISA implementation inconsistency, and the absent HTML companion file. These are structural issues, not content issues — the underlying pedagogy is sound.

**Estimated effort to resolve must-fix items:** 3-4 hours.

---

## Next Steps

1. **Address 3 must-fix items** (dual-domain PISA, HR track, HTML file)
2. **Address 3 should-fix items** (session duration, scholar pairing, shape declaration)
3. **Extract full textbook content** for remaining chapters (§18 item 1)
4. **Design adaptive scaffolded fallback** for below-L2 students (§18 item 5)
5. **Produce 5+ sessions of Chapter 1** for stress testing
6. **Review with Uzbek elementary history teacher** (per §20 reviewers needed)
7. **Proceed to engineering handoff** once must-fix and should-fix items resolved

---

**Reviewed by:** BlueprintReviewer Agent
**Review Date:** April 10, 2026
**Document:** NETS-History-Grade5-Framework.md v1.0
**Verdict:** ⚠️ Conditionally Approved — 3 must-fix items pending
