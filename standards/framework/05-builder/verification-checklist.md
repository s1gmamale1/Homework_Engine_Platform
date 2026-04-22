---
name: Verification Checklist — Homework Compliance Gate
status: v0.1 draft — validated against §22 only
layer: 5 (builder)
source: UNIFIED §10.1b (Buzan QA gates) + Architecture doc (lines 328-345)
---

# Verification Checklist — Homework Compliance Gate

Every homework must pass ALL gates before shipping. Any single failure rejects the homework and triggers a targeted rebuild (see `homework-builder.md` §Step 5 for retry logic).

| # | Gate | What it checks | Method | Pass condition | Applies to |
|---|------|---------------|--------|----------------|------------|
| 1 | Schema valid | Output `.md` conforms to `output-schema.md` structure; metadata JSON passes JSON Schema validation | Automated structural validator | 100% conformance | All |
| 2 | Tagging coverage | Every question/item carries `[Bloom: LX \| PISA: LX \| Skill: <id>]`; boss questions also carry `[Damage: -XX HP]` | Regex scan | 100% of items tagged | All |
| 3 | Pronoun compliance | Zero occurrences of `sen` (Uzbek informal) or `ты` (Russian informal) anywhere in output | `grep -ri` keyword scan | 0 hits | All |
| 4 | Context compliance | No bazaar/village/farmer/shopkeeper cliché contexts in Phase 4 scenarios or any narrative | Keyword scan + reviewer flag | 0 hits | All |
| 5 | Format rules | Phase 1 contains only MC / T-F / YNNG formats; ≥2 formats present; Phase 3 has correct game count (Easy = 2, Hard = 3) and correct Interactive/Default mix (Hard: ≥1 Interactive + ≥2 Default) | Automated format check | 100% conformance | All |
| 6 | Capture markers | Every calculation step in Phase 3 (Adaptive Quiz), Phase 4, and Phase 5 carries a capture flag | Automated marker scan | 100% of calc steps flagged | Aniq Fanlar, Tabiy Fanlar |
| 7 | Textbook fidelity | No concepts, facts, or formulas introduced that do not appear in the source chapter; no external curriculum | Embedding similarity diff vs. chapter extract + human review flag | 0 external facts; reviewer sign-off | All |
| 8 | Cognitive variety | Bloom level distribution across the full homework spans ≥3 distinct levels; minimum range L2-L5 present | Distribution count across all tagged items | ≥3 Bloom levels, L2-L5 minimum | All |
| 9 | Reproducibility | Running the same inputs through the builder 3 times produces outputs with ≥95% structural similarity (same phases, same item count, same format types) | Automated structural diff (3× regeneration) | ≥95% match across 3 runs | All |
| 10 | Language QA | Grammar correctness, subject-appropriate terminology, and formal register (Siz / Вы) throughout | External language validator (automated pass + human spot-check for Tier 3 content) | ≤2 errors per 1000 words | All |
| 11 | Teaching methodology | Genetic method present in Preview; two-layer explanation (concept + application) present in at least Panels 1-4 | Content review (automated keyword check + reviewer confirmation) | Both elements present in Preview | All |

---

**Failure handling:** Gate failure → homework status set to `rejected`. Builder identifies failing gate, isolates the component, retries rebuild up to 3×. After 3 failed retries on the same gate → status set to `DRAFT — manual review required`. Partial output is preserved with failure annotation. See `homework-builder.md` §Step 5.
