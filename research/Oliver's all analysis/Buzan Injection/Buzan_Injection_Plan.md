# Buzan 34-Method Injection Plan for NETS Homework Engine

## Context

We have 6 Buzan research briefs (Mind Map Book, Mind Maps for Kids, Scientific Research, Speed Reading, Use Your Head, Use Your Memory) containing 34 distinct methods. These must ALL be injected into the NETS homework engine as delivery mechanisms — never changing the textbook content itself.

**Sacred Rule:** Content is sacred. Buzan = the HOW, never the WHAT.

Currently, zero Buzan methods are integrated into the active NETS specs. Memory Palace exists independently but not as a Buzan-attributed technique. Phase 5 lists "Peg system, Mind maps" for G5-7 but neither is defined.

---

## 5 Injection Layers

All 34 methods are categorized into one of five layers:

### Layer A — Phase-Bound Injections (methods that live inside specific phases)
### Layer B — Cross-Cutting Injections (design principles enforced across all phases)
### Layer C — UI/UX Layer Injections (change how content is displayed, not what)
### Layer D — AI Tutor Language Injections (change how the AI speaks to students)
### Layer E — Content Pipeline Injections (quality gates for content authors)

---

## Complete Method-to-Layer-to-Phase Mapping

| # | Method | Layer | Phase(s) | What Changes |
|---|---|---|---|---|
| 1 | Radiant Thinking | A+C | P5, P0-A | New "Radiant Summary" game mechanic in P5 (fills undefined "Mind maps" slot). Drag-and-drop keywords onto partially completed radiant map. P0-A Panel 1 optionally renders topic as radiant thumbnail. |
| 2 | 7 Laws of Mind Mapping | B+E | All radiant UI | Design principle DP-1: any radiant UI must comply with 7 laws (central image, organic branches, hierarchy, one keyword/branch, emphasis, association, 3+ colors). Pipeline QA checklist for mnemonic exercises. |
| 3 | Group Mind Mapping | A | P3 (future) | Post-MVP: async collaborative map building. MVP fallback: student builds map, AI simulates classmate's map for merge exercise. |
| 4 | Radiant Problem Solving | A | P4 | Pre-solution W5H frame (Who/What/Where/When/Why/How) radiating from problem statement. Student fills 4+ branches before writing answer. |
| 5 | Decision Mapping | A | P6 | New Boss question format: two competing options radiate from central problem with weighted pros/cons. For Big Boss / Mythical Boss decision-type questions. |
| 6 | Simplified Laws (Kids) | C | All G5-6 UI | Landscape orientation, thick organic branches, Icon-First (image before text), max 4-5 main branches (WM ceiling). |
| 7 | Supernova Effect | A | P5 | "Supernova Sprint" micro-game: 30-sec timed association burst from one keyword. Each valid association = radiating spark + XP. |
| 8 | Secret Symbols | A+Meta | P5, Bilim Bazasi | Students create/save personal symbol stickers for concepts. Symbols persist in Bilim Bazasi and reappear when concept resurfaces. |
| 9 | Color-Coded Zones | C | All phases | Each subject family gets a distinct color. Each BOI branch uses a unique color. Extends to Bilim Bazasi, loading screens, all in-session radiant elements. |
| 10 | "Hali emas" / TEFCAS reframe | D | All failure states | ALL failure responses across ALL phases use "Hali emas!" (Not yet!) + TEFCAS framing. Never "Wrong" or "Incorrect." |
| 11 | TEFCAS full loop | B+D | All phases | DP-2: Map TEFCAS onto session flow (T=P3 attempts, E=outcome, F=feedback, C=IRT check, A=difficulty adjust, S=Boss defeat). AI tutor uses TEFCAS vocabulary. |
| 12 | Dual Coding Theory | B+E | All phases | DP-5: Every content block must engage 2+ encoding channels (verbal+visual, verbal+spatial, visual+kinesthetic). Pipeline QA checks this. |
| 13 | Schema Theory | B | Session Assembly | DP-6: Session Assembler verifies every new concept in P2 has a prerequisite activated in P1 or P0-B of the same session. |
| 14 | Von Restorff Effect | B | P3 (anchor) | DP-4: One game per session tagged as "Von Restorff anchor" — deliberately unusual, funny, or visually striking. Mid-session game (Sag position) gets highest novelty score. |
| 15 | Anti-Cheat Radiant Signature | A | P4, P6 | New anti-cheat Check #7: analyze open-text responses for "radiant signature" (idiosyncratic associations, non-linear logic). Too-linear responses flagged as potential AI/copy-paste. |
| 16 | Fixation Training | A | P2 | "Focus Guide" — text highlights in 3-5 word chunks sequentially. Speed adapts to student's reading pace. Trains eye to fixate on chunks, not words. |
| 17 | Saccade Optimization | C | P2 | Column width 50-75 chars (66 ideal). Optimizes saccade distance. |
| 18 | Regression Elimination | A | P2 | Forward Momentum Rule (G5-6): previous Story Mode segment fades after swipe. Back-navigation requires deliberate button press (friction). |
| 19 | Peripheral Vision Training | C | P2 | Merged with #17: column width + line height (1.5x) + sans-serif font (Arimo) optimize peripheral vision utilization. |
| 20 | Chunking | A+C | P2, P0-B | Story Mode text rendered in semantic clusters (3-5 words, wider spacing between chunks). Flash Cards: max one chunk per card face. |
| 21 | Sub-vocalization Elimination | A | P2 | Merged into Focus Guide (#16): pacer moves 5-10% faster than student's established reading speed, pushing beyond inner-voice speed. |
| 22 | 80/20 Rule | E | Content Pipeline | Every `narrative_segment` must extract and tag `keywords_80_20` array — the 20% of words carrying 80% of conceptual value. Used by Focus Guide, Radiant Summary, Flash Cards, Memory Sprint. |
| 23 | Meta-Guiding | A | P2 | Merged into Focus Guide (#16): the visual pacer IS the meta-guide that maintains rhythm and reduces eye strain. |
| 24 | Pre-reading (Scan/Skim) | A | P0-A | Panel 1 redesigned as "Structural Scan": heading tree, bold-term highlights, diagram thumbnail grid. Trains scanning before deep reading. |
| 25 | Cortical Skills Synergy | B | P3 selection | DP-3: Game selection algorithm must pick 2+ games engaging DIFFERENT cortical modalities (verbal/logical, visual/spatial, kinesthetic/procedural, social). |
| 26 | Primacy & Recency | B | P1, P7 | DP-4: Formalize that P1 exploits Primacy, P7 exploits Recency. Already true — make explicit in docs. |
| 27 | BOST full sequence | A | All phases | Alignment table mapping BOST steps to NETS phases. Two small additions: "What do you already know?" prompt in P0-A Panel 5, "What do you want to learn?" prompt in P0-A Panel 6. |
| 28 | Link System | A | P1, P5 | New Memory Sprint format #6: "Link Chain" — 5 sequential items with vivid story chain, recall tested out of order. Also available as P5 technique for sequential content. |
| 29 | Peg System | A | P5, P3 | New game mechanic spec (fills undefined "Peg system" slot). Number-Shape pegs (1=Candle, 2=Swan, etc., culturally adapted). Association + recall phases. Integrates with Tic Tac Toe vs AI. |
| 30 | Major System | A | P5 (G7+) | Phonetic digit code for number-heavy subjects (History dates, Chemistry constants). AI generates memorable word from target number. G7+ only. |
| 31 | SEM-cubed | A+Meta | Bilim Bazasi | Memory Matrix data model underneath Bilim Bazasi: concepts indexed by subject x encoding type. Powers knowledge tree visualization and informs session assembler about encoding coverage. |
| 32 | SMASHIN' SCOPE | E | Pipeline QA | Every `mnemonic_exercise` must score 6+/12 on SMASHIN' SCOPE (Synaesthesia, Movement, Association, Sexuality→Humor, Humor, Imagination, Number, Symbolism, Color, Order, Positive, Exaggeration). Below 6 = returned for enrichment. |
| 33 | The MIG | B | P1, P3, P7 | Merged with #26: formalize that the 7-phase structure IS the MIG in action. Von Restorff anchor in P3 breaks the Sag. |
| 34 | Buzan Review Intervals | A+B | P1, spaced rep | Four mandatory touchpoints override SM-2 when SM-2 would schedule later: ~10min (same session P5), ~24h (next day P1), ~1 week, ~1 month. Rule: `min(SM-2 schedule, Buzan mandatory)` — whichever is SOONER wins. |

---

## Overlap Reconciliation

| Existing Feature | Buzan Method | Action |
|---|---|---|
| Memory Palace (fully defined) | Method of Loci (part of #28-31 family) | ENHANCE: Add SMASHIN' SCOPE gate to Memory Palace content |
| "Hali emas" in Memory Palace only | #10 "Hali emas" | EXTEND: Apply to ALL failure states across ALL phases |
| IRT engine = Check/Adjust | #11 TEFCAS | FORMALIZE: Name it TEFCAS in docs; extend to AI tutor language |
| Dual Coding in Memory Palace research | #12 Dual Coding | ENFORCE: System-wide mandatory design principle |
| Phase 5 lists "Peg system" (undefined) | #29 Peg System | FILL GAP: Write full game mechanic spec |
| Phase 5 lists "Mind maps" (undefined) | #1 Radiant Thinking | FILL GAP: Write "Radiant Summary" game mechanic spec |
| SM-2 Modified spaced repetition | #34 Buzan Review Intervals | AUGMENT: Add 4 mandatory touchpoints as floor constraints |
| 7-phase structure | #26 Primacy/Recency, #33 MIG | FORMALIZE: Document that the structure IS the MIG |

---

## Deliverables List

### New Game Mechanic Specs (full documents like the Memory Palace spec)
1. `NETS-Radiant-Summary-Specification.md` — Methods 1, 2, 7
2. `NETS-Peg-System-Specification.md` — Method 29

### Spec Amendments (sections added to existing docs)
3. UNIFIED spec: BOST alignment table + TEFCAS alignment section (Methods 11, 27)
4. UNIFIED spec Phase 1: Link Chain format + Buzan Review Intervals floor (Methods 28, 34)
5. UNIFIED spec Phase 2: Focus Guide feature (Methods 16, 21, 23) + Forward Momentum Rule (Method 18)
6. UNIFIED spec Phase 3: Cortical Diversity Constraint + Von Restorff Anchor (Methods 25, 14)
7. UNIFIED spec Phase 4: W5H Radiant Analysis scaffold (Method 4)
8. UNIFIED spec Phase 5: Major System for G7+ (Method 30), Link System technique (Method 28)
9. UNIFIED spec Phase 6: Decision Map question type + TEFCAS Socratic language (Methods 5, 11)
10. UNIFIED spec Phase 7: TEFCAS-framed reflection prompts (Method 11)
11. UNIFIED spec Phase 0-A: Structural Scan for Panel 1 + BOST prompts for Panels 5/6 (Methods 24, 27)
12. UNIFIED spec Section 9: Buzan Review Intervals as SM-2 floor constraints (Method 34)
13. UNIFIED spec Section 10: 80/20 keyword extraction + Dual Coding check + SMASHIN' SCOPE gate + Schema Activation check (Methods 22, 12, 32, 13)
14. UNIFIED spec Section 13: Anti-cheat Check #7 Radiant Signature (Method 15)

### UI/UX Spec Amendments
15. `NETS-UI-UX-Design-Spec.md`: Radiant UI Standard (7 Laws) (Method 2)
16. `NETS-UI-UX-Design-Spec.md`: G5-6 Simplified Radiant Rules (Method 6)
17. `NETS-UI-UX-Design-Spec.md`: Subject Color System (Method 9)
18. `NETS-UI-UX-Design-Spec.md`: Reading Optimization (column width, line height, font) (Methods 17, 19)
19. `NETS-UI-UX-Design-Spec.md`: Focus Guide visual spec (Methods 16, 21, 23)
20. `NETS-UI-UX-Design-Spec.md`: Semantic Chunking rendering rule (Method 20)
21. `NETS-UI-UX-Design-Spec.md`: Radiant Journey Map sidebar (Method 1)

### AI Tutor Language
22. AI Prompt Template Library: "Hali emas" failure responses for all phases (Method 10)
23. AI Prompt Template Library: TEFCAS Socratic prompts for P6 and P7 (Method 11)
24. AI Language Style Guide: Buzan-Inspired Tutor Voice (30+ template phrases) (Methods 7, 10, 11)

### Lower Priority / Future Roadmap
25. `NETS-Group-Map-Game-Brief.md` — Method 3 (post-MVP, multiplayer dependency)
26. Secret Symbols feature spec + Bilim Bazasi amendment (Method 8)
27. SEM-cubed Memory Matrix data model (Method 31)

---

## Implementation Sequence

**Sprint 1 — Foundation (Cross-cutting + Docs):** Deliverables 3, 15-18, 22-24, 13
**Sprint 2 — Core Mechanics:** Deliverables 1, 2, 4, 5, 12
**Sprint 3 — Phase Amendments:** Deliverables 6-11, 14, 19-21
**Sprint 4 — Polish & Future:** Deliverables 25-27

---

## Cost Impact

All methods are Tier 1 (algorithmic/template) except:
- Tier 2 (small LLM calls): Methods 4, 7 (G7+ open input), 15, 30 — minimal marginal cost
- Tier 3 (expensive): Methods 3, 8, 31 — Premium-only or infrequent

**$3-5/student/year target preserved.** No Tier 3 required for Basic users.

---

## Critical Files to Modify

- `All analysis/Universal Specs/NETS-Homework-Engine-UNIFIED.md` — Main constitution, receives bulk of amendments
- `All analysis/Universal Specs/NETS-UI-UX-Design-Spec.docx` — UI/UX layer injections
- `All analysis/Game Mechanics - All Definitions/` — New mechanic specs go here
- `All analysis/Buzan Injection/` — Source briefs (read-only reference)
- `All analysis/NETS-System-Design-v1.md` — Bilim Bazasi/metagame amendments

## Verification

After implementation:
1. Every one of the 34 methods should be traceable to at least one deliverable
2. No deliverable changes any textbook content
3. All new game mechanics follow the existing spec template (see Memory Palace spec as model)
4. All pipeline QA gates are additive (new checks, not replacing existing ones)
5. Generate the combined Buzan Injection spec as both .md and .html
