# NETS System Design v1 — Executive Summary

**Document status:** Draft  
**Version:** 1.0  
**Date:** 2026-04-09  
**Full document:** `standards/system-design/v1/NETS-System-Design-v1.md`

---

NETS shifts from framework to product. This document defines the multi-layer architecture, two-tier model, and persistent metagame that turn the Universal Framework into a deployable national LMS for 8.8M students. The Universal Framework v2.0 remains the constitution. Everything new layers on top.

---

## Architecture Diagram

```
Layer 0: UNIVERSAL FRAMEWORK v2.0       (the constitution — unchanged)
              ↓  inherits
Layer 1: SUBJECT FAMILY FRAMEWORKS      (5 families — NEW this sprint)
              ↓  inherits
Layer 2: SUBJECT FRAMEWORKS             (per subject × grade × language — ~110 total)
              ↓  inherits
Layer 3: TIER OVERLAY                   (Basic + Premium — cuts across all subjects)
              ↓  inherits
Layer 4: METAGAME + APP SURFACES        (Bilim Bazasi — persistent, cross-subject)
```

---

## Section 1: Benchmark

Current scores: Pedagogical rigor 9/10, Architecture clarity 7/10, Content coverage 1/10, Product readiness 3/10, Engagement design 6/10, Differentiation 5/10, Subject treatment 2/10. We have a score-9 constitution and one validated subject framework. We have no content factory and no product layer. This document adds both.

## Section 2: The 5-Layer Architecture

Layer 0 (Universal Framework v2.0) is the constitution: 7-phase session, 28 mechanics, PISA framework, mandatory tagging — unchanged. Layer 1 (Subject Family Frameworks) is the new addition: five families that cluster subjects by cognitive demand and mechanic fit, doing the heavy design work once so Layer 2 subject frameworks can be written as fast deltas. Layer 2 (Subject Frameworks) are the per-subject, per-grade, per-language content documents; 1 of ~110 complete. Layer 3 (Tier Overlay) is a thin delta across all subjects specifying what changes between Basic and Premium — not a duplicate content set. Layer 4 (Metagame) is the persistent cross-session motivation layer. Each layer inherits from the one above and cannot contradict it.

## Section 3: Subject Family Classification

Five families cover all K–11 subjects. **Aniq Fanlar** (Exact Sciences: Math, Physics, Chemistry, Informatics) emphasizes CPA progression, worked examples, Tile Match for formula assembly, and Notebook Capture for hand-written derivations. **Til Fanlari** (Languages: Uzbek, Russian, English, Native Language, Literature) emphasizes spaced repetition, cloze/Sentence Fill, listening, dictation, and Story Mode for literary texts. **Tabiat Fanlari** (Natural Sciences: Biology, Geography, G5 Combined Science) emphasizes diagram labeling, Memory Palace, Why Chain, and Story Mode for discovery narratives — G5 Science v3.0 is this family's prototype. **Ijtimoiy Fanlari** (Social Sciences: History, Law, Economy, Civics) emphasizes Story Mode for historical narrative, Timeline Tile Match, Source Comparison, and case-reasoning Boss tasks. **Tarbiya/Sanat** (Soft/Formative: Art, Music, PE, Tarbiya) is intentionally minimal-gamification: lightweight expressive tasks, Reflection Journal, no scored Boss.

## Section 4: Basic and Premium Tiers

Basic Tier delivers the complete educational mission to all 8.8M students: full 7-phase gamified sessions, Tier 1 + Tier 2 AI, complete metagame access, monthly PISA checkpoints. No student is academically disadvantaged for not paying. Premium adds depth (harder difficulty band, exam prep, beyond-textbook electives), richer tools (unlimited game access, Tier 3 Opus-grade Socratic tutoring, personalized study plans), specialized cross-subject courses (AI Literacy, Critical Thinking, Economy, Law, IT, Language enrichment), and mandatory weekly PISA lessons (async 7-day window, ~20 min, teacher-tracked). Soft upsell surfaces appear after sessions — never blocking session flow. The business model (family-paid, school-licensed, sponsored, or hybrid) is an open decision in Section 10.

## Section 5: Metagame — Bilim Bazasi

Bilim Bazasi is each student's persistent visual Knowledge Base — a Central Asian cultural complex (academy / observatory / Silk Road composite — visual metaphor TBD) that grows as they complete chapters and master skills. The sole currency is Bilim Tokens (BT), earned by completing sessions, mastering PISA transition skills, defeating Bosses, and maintaining streaks. BT buys cosmetic and lore items only: buildings, Central Asian heritage decorations, and hero unlocks (Al-Khwarizmi, Ibn Sina, Ulugh Beg, Beruniy — each with lore vignettes and related mini-missions). BT cannot purchase academic advantage of any kind. Refused mechanics include real-money loot boxes (gambling psychology, banned for minors in multiple jurisdictions), pay-to-skip difficulty, energy systems with paid skips, and FOMO events that disadvantage students with irregular access.

## Section 6: AI Tier Strategy

Tier 1 (rule-based, ~$0) handles 80% of all tasks: multiple choice, matching, numeric, exact string. Tier 2 (small LLM, cents/student/year) handles Boss evaluation, Socratic prompts, anti-cheat, and story checkpoints for both tiers. Tier 3 (Opus-grade, dollars/student/year) handles deep tutoring, study plans, and exam prep for Premium only. Cost target: $3–5/student/year for Basic. All API routes implement static fallbacks so session failure on AI outage is architecturally impossible.

## Section 7: App Surfaces

**Today** (home): streak, weekly mission, single "Start Homework" CTA, one soft Premium teaser — maximum 2 information chunks before the CTA. **Bilim Bazasi**: persistent visual base, tap-to-recap buildings, BT spend interface, hero collection. **Library**: Subject Family → Subject → Grade navigation; locked Premium chapters visible with preview text (no hard paywall wall). **Tournaments**: weekly inter-class PISA events, weekly-reset class leaderboard (relative rank only), BT ticket entry. **Teacher Dashboard**: attendance heatmaps, per-student mastery maps, anti-cheat alert log, weekly PISA completion tracker — mobile-first design for school context.

## Section 8: Existing Assets

Universal Framework v2.0 → Layer 0, unchanged. G5 Science v3.0 → Layer 2 under Tabiat Fanlari, gold standard for all future subject framework production. Platform docs 00–11 → valid; will need extension contracts for Tier overlay and Metagame data model. Demo app `app/` → session visualizer; future: tier toggle and Bilim Bazasi mock. G5 psychology research → audience contract applied at Layer 0 and inherited by all five Layer 1 families. 16 + 12 mechanics → reassigned per family mechanic emphasis tables in Section 3.

## Section 9: Roadmap

Phase 1: Write 5 Subject Family Frameworks (Layer 1) — Tabiat Fanlari first, bootstrapped from G5 Science v3.0. Phase 2: Per-family G5 subject frameworks (Layer 2) — Math, Biology, History, Literature, Geography, English, Russian, Native Language, Informatics. Phase 3: Tier overlay delta contracts (Layer 3). Phase 4: Metagame spec — Bilim Bazasi data model, BT economy (post-playtesting), tournament schema (Layer 4). Phase 5: Platform implementation per extended `platform/docs/` contracts. Phase 6: G6–11 expansion and Russian-language siblings.

## Section 10: Open Decisions

Eight items deferred: (1) Premium business model — family/school/sponsored/hybrid; (2) Informatics placement — Aniq Fanlar default, ADR if warranted; (3) Literature placement — Til Fanlari default, Humanities subfamily option; (4) Tournament regional tier — class default, school/region opt-in; (5) BT economy formulas — requires playtesting with real students; (6) G5 Science v3.0 standalone vs. family-derived reconciliation; (7) Weekly PISA enforcement — async window vs. strict deadline; (8) Bilim Bazasi visual metaphor — requires cultural consultation and student user testing.

## Section 11: SOUL Constraints

**Textbook is truth:** Layer 2 follows textbook chapter sequence; NETS does not reorder or supplement without curriculum authority approval; AI errors yield to textbook, always. **Every task earns its existence:** The mandatory `transition_skill` tag is not relaxed at any layer; harder difficulty (Premium) does not waive the justification requirement. **The 10-year-old is not a small adult:** G5 psychology constraints (WM ceiling, "Hali emas" framing, hidden difficulty, weekly-reset competition, no public wrong answers) apply at every layer for G5 content and inform all G5 family and subject frameworks. **Flow state, not anxiety:** 75–85% success target enforced at Layer 2 calibration and Layer 3 difficulty banding; silent adaptive difficulty; Metagame calibrated for normal engagement, not extraordinary performance. **Intrinsic > Extrinsic, zero pay-to-win, zero real-money loot boxes:** Basic delivers full learning mission; BT has no real-money entry point; Mystery Boxes earned by mastery only; no academic advantage is purchasable at any price — this is the design constraint that makes NETS deployable as national infrastructure without reproducing economic inequality in learning outcomes.

---

## Closing

This document is the bridge between the framework era and the platform era. The next sprint produces the 5 Subject Family Frameworks — the highest-leverage work in the pipeline. Each family framework unlocks all subject frameworks beneath it. After that, subject framework production scales linearly, in parallel, and is delegable to sub-agents. NETS is ready to become a product.

---

*Full document: `standards/system-design/v1/NETS-System-Design-v1.md`*  
*Constitution: `standards/NETS-Homework-Engine-UNIFIED.md` v2.0*
