# Buzan Core Injection Specification — NETS Homework Engine

**Version:** 1.0 | April 2026
**Scope:** 22 of 34 Buzan methods — the Core Injection layer only
**Sacred Rule:** Content is sacred. Buzan = the HOW, never the WHAT.
**What was cut:** Speed Reading cluster (Methods 16-23 → future Reading Fluency module), Anti-Cheat Radiant Signature (#15 → pseudoscientific), Decision Mapping in Boss (#5 → relocate to P4), Major System (#30 → needs Uzbek phonetic analysis), Group Mind Mapping (#3, #8, #31 → future roadmap).

---

## Table of Contents

1. [TEFCAS Alignment](#1-tefcas-alignment)
2. [BOST Alignment](#2-bost-alignment)
3. [Pipeline Quality Gates](#3-pipeline-quality-gates)
4. [Radiant UI Standard](#4-radiant-ui-standard)
5. [AI Tutor Language](#5-ai-tutor-language)
6. [Radiant Summary Game Mechanic](#6-radiant-summary-game-mechanic)
7. [Peg System Game Mechanic](#7-peg-system-game-mechanic)
8. [Phase Amendments](#8-phase-amendments)
9. [What Was Cut & Why](#9-what-was-cut--why)

---

## 1. TEFCAS Alignment

The NETS 7-Phase Homework Engine is structurally aligned with Tony Buzan's **TEFCAS** model — the brain's natural cybernetic learning loop. TEFCAS is not a new addition; it is the *naming* of what the engine already does.

### TEFCAS-to-NETS Phase Mapping

| TEFCAS Step | NETS Phase | How It Already Works |
|---|---|---|
| **T — Trial** | Phase 3: Game Breaks | Student attempts practice problems. Every attempt generates data. |
| **E — Event** | Phase 3: Per-question result | Binary outcome (correct/incorrect) plus metadata (time, hesitation, hints). |
| **F — Feedback** | Phase 3: Immediate feedback | Instant per-item feedback — correct answer, explanation on wrong, streak display. |
| **C — Check** | IRT Engine (Section 9) | IRT recalculates student Theta after each response. Compares performance against target PISA level. |
| **A — Adjust** | IRT Difficulty Adjustment + Phase 5 | Engine adjusts difficulty tier. Phase 5 Consolidation targets weak concepts identified during Check. |
| **S — Success** | Phase 6: Boss Defeat | Boss defeated. Student demonstrated competence at target PISA level. XP, stars, badges awarded. |

### Core Maxim (system-wide)

> **"There is no such thing as failure, only feedback."**

When a student gets a question wrong or fails the Final Boss — the system treats the outcome as **Feedback (F)**, not as failure. All AI tutor language uses "Hali emas!" (Not yet!) framing.

### TEFCAS in Boss Failure Flow

```
1. TRIAL (T):     Student attempted the Boss questions
2. EVENT (E):     Boss HP > 0 after all questions (defeat)
3. FEEDBACK (F):  System identifies WHICH learning objectives failed
4. CHECK (C):     IRT compares failed objectives against student's current Theta
5. ADJUST (A):    Socratic tutoring guides student to specific weak branches
                  + Boss questions regenerated (same standards, new context)
6. SUCCESS (S):   Student re-attempts and defeats the Boss
```

---

## 2. BOST Alignment

The Buzan Organic Study Technique (BOST) maps to the NETS 7-Phase flow at 8/8 steps after two small additions.

### BOST-to-NETS Alignment Table

| BOST Step | NETS Phase | Status | Gap / Addition |
|---|---|---|---|
| **Browse** | Phase 0-A: Theme Preview (Panels 1-4) | ALIGNED | No change needed. |
| **Time & Amount** | Session timer display | ALIGNED | Timer already shows estimated remaining time. |
| **Prime** | Phase 0-A Panel 5 + Phase 1 Memory Sprint | PARTIAL → **ADD prompt** | See Addition 1 below. |
| **Questions/Goals** | Phase 0-A Panel 6 | PARTIAL → **ADD prompt** | See Addition 2 below. |
| **Overview** | Phase 0-B: Flash Cards | ALIGNED | Flash Cards surface all key formulas, concepts, and rules. |
| **Preview** | Phase 2: Story Mode (Segment 1) | ALIGNED | Problem beat of story arc sets context. |
| **Inview** | Phase 2-3: Story Mode + Game Breaks | ALIGNED | Core content delivery and active practice. |
| **Review** | Phase 5 + Phase 7: Consolidation + Reflection | ALIGNED | Mnemonic Lock synthesizes; Reflection enables metacognition. |

### Two Required Additions

**Addition 1 — Prior Knowledge Prompt (Panel 5):**
```json
{
  "panel": 5,
  "component": "personal_hook",
  "addition": "prior_knowledge_prompt",
  "prompt_uz": "Bu mavzu haqida nimalarni bilasiz? 2-3 ta kalit so'z tanlang yoki yozing.",
  "interaction": "keyword_chips_or_freetext",
  "scoring": "none",
  "ai_tier": 1,
  "data_use": "fed to Session Assembler to prioritize schema-linked content in Phase 2"
}
```

**Addition 2 — Learning Goal Prompt (Panel 6):**
```json
{
  "panel": 6,
  "component": "why_this_matters",
  "addition": "learning_goal_prompt",
  "prompt_uz": "Bugun [Mavzu] haqida nimani bilmoqchisiz?",
  "interaction": "single_line_text_input",
  "scoring": "none",
  "ai_tier": 1,
  "data_use": "resurfaced in Phase 7: 'Remember, you wanted to learn [X]. Did you figure it out?'"
}
```

**BOST Alignment Score:** Before: 6/8 (75%) → After: **8/8 (100%)**

---

## 3. Pipeline Quality Gates

### QG-1: 80/20 Keyword Extraction (Method #22)

Every `narrative_segment` must extract and tag **`keywords_80_20`** — the ~20% of words carrying 80% of conceptual value.

**Schema:**
```json
{
  "keywords_80_20": {
    "type": "array",
    "min_items": 3,
    "max_items": 8,
    "items": {
      "keyword_uz": "string",
      "keyword_ru": "string (optional)",
      "importance": "primary | secondary",
      "textbook_page": "integer"
    }
  }
}
```

**Consumed by:** Focus Guide, Radiant Summary, Flash Cards, Memory Sprint, Supernova Sprint.

**Validation:** `IF keywords_80_20 IS EMPTY → Block: DRAFT status.`

### QG-2: Dual Coding Check (Method #12)

Every content block must engage **at least 2 encoding channels**:

| Channel | Code | What It Means |
|---|---|---|
| Verbal/Textual | `VRB` | Words, sentences, labels |
| Visual/Pictorial | `VIS` | Images, diagrams, icons, colors |
| Spatial/Locational | `SPA` | Position, layout, movement through space |
| Auditory | `AUD` | Sound, rhythm, music, spoken word |
| Kinesthetic/Motor | `KIN` | Drag, draw, tap, physical action |

**Schema:**
```json
{
  "encoding_channels": {
    "type": "array",
    "min_items": 2,
    "items": { "enum": ["VRB", "VIS", "SPA", "AUD", "KIN"] }
  }
}
```

**Validation:** `IF encoding_channels.length < 2 → Block: DRAFT.`

### QG-3: SMASHIN' SCOPE Gate (Method #32)

Every `mnemonic_exercise` must score **6+/12** on SMASHIN' SCOPE. Score = sum of 12 boolean criteria (Synaesthesia, Movement, Association, Substitution, Humor, Imagination, Number, Symbolism, Color, Order, Positive, Exaggeration).

**Note:** The 6/12 threshold is a proposal, not empirically validated. Content creators should treat it as a quality guide, not a box-ticking exercise.

**Validation:** `IF score < 6 → Return for enrichment with specific criteria flagged.`

### QG-4: Schema Activation Check (Method #13)

Every new concept in Phase 2 must have **at least one prerequisite** activated in Phase 1 or Phase 0-B of the same session. If none exists, the Session Assembler auto-inserts one into Memory Sprint.

---

## 4. Radiant UI Standard

Any UI element displaying information radiantly (Radiant Summary, Bilim Bazasi knowledge map, topic structure) MUST comply with Buzan's 7 Laws.

### 7-Point Radiant Compliance Checklist

| # | Law | Requirement | Fail Example | Pass Example |
|---|---|---|---|---|
| 1 | **Central Image** | Center contains a colorful image/icon representing the topic. Never text alone. | Plain text "Photosynthesis" | Sun icon with green leaves |
| 2 | **Organic Branches** | Curved, organic lines. No straight connectors. CSS `border-radius` mandatory. | Straight lines | Curved, flowing lines tapering thick→thin |
| 3 | **Hierarchy** | Main branches thicker/bolder than sub-branches. Clear parent-child distinction. | All branches same thickness | Main 4px, Sub 2px, Leaf 1px |
| 4 | **One Keyword/Branch** | Each branch displays exactly one keyword. No sentences. | "The process of water evaporating" | "Bug'lanish" (Evaporation) |
| 5 | **Emphasis** | Visual hierarchy through size variation. | All labels same font size | Main 16px bold, Sub 14px, Leaf 12px |
| 6 | **Association** | Connections between related branches via arrows/dashed lines. | Isolated branches | Dashed arrow between related concepts |
| 7 | **3+ Colors** | Minimum 3 distinct colors. Each main branch has its own color zone. | Monochrome | Blue (Water), Green (Plants), Yellow (Sun) |

### G5-6 Simplified Radiant Rules (Override)

| Rule | Standard (G7+) | G5-6 Override |
|---|---|---|
| Orientation | Any | **Landscape only** |
| Max main branches | 6-8 | **4-5 maximum** (WM ceiling) |
| Branch style | Organic, varied | **Extra thick, exaggerated curves** |
| Label format | Keyword text | **Icon-First: image BEFORE text** |
| Interaction | Drag-and-drop | **Tap-to-select from 3 options** (drag optional) |
| Color | 3+ colors | **Exactly 4-5 colors**, high saturation |

### Subject Color System

| Subject Family | Primary Color | Hex |
|---|---|---|
| **Aniq Fanlar** (Exact Sciences) | Deep Blue | `#1565C0` |
| **Tabiat Fanlari** (Natural Sciences) | Forest Green | `#2E7D32` |
| **Til Fanlari** (Languages) | Warm Amber | `#E65100` |
| **Ijtimoiy Fanlar** (Social Sciences) | Royal Purple | `#6A1B9A` |
| **Tarbiya / San'at** (Values & Arts) | Warm Red | `#C62828` |

**Application:** Phase header bar, radiant central node, Bilim Bazasi zones, loading screen gradient, progress bar. Color-blind students get distinct line patterns as secondary differentiator.

### Reading Optimization (Typography)

| Parameter | Value |
|---|---|
| Column width | **50-75 chars per line** (66 ideal) |
| Line height | **1.5x** (minimum 1.4x) |
| Font family | **Arimo** (primary), Noto Sans (fallback) |
| Font size | **16px** base (mobile), **18px** (tablet/desktop) |
| Text alignment | **Left-aligned** (ragged right) |
| Max container width | **640px** on desktop |

Applies to: Story Mode, Theme Preview, Flash Cards, Real-Life Challenge, Boss questions. NOT to navigation/UI chrome.

### Semantic Chunking (G5-6)

Story Mode text rendered with wider gaps (0.4em) between 3-5 word semantic chunks. Chunk boundaries pre-computed: (1) after punctuation, (2) between subject/predicate, (3) between verb phrase/object, (4) after 5 words (fallback).

---

## 5. AI Tutor Language

### Core Rule

**The words "Wrong," "Incorrect," "Noto'g'ri," and "Xato" are BANNED from all AI tutor responses across all phases.** Every failure state uses: **"Hali emas!"** (Not yet!) + TEFCAS-framed follow-up.

### Phase-by-Phase Failure Templates (Key Examples)

| Phase | Trigger | Template (Uzbek) |
|---|---|---|
| **P1** Memory Sprint | 0-2/5-8 correct | "Hali emas! Miyangiz hozir eslamoqda. Ertaga bu so'zlar osonroq bo'ladi." |
| **P2** Story Mode | Wrong checkpoint (1st) | "Hali emas! Hikoyaga qaytib qarang — javob o'sha yerda." |
| **P3** Game Breaks | Wrong game answer | "Hali emas! Miyangiz hozir Feedback oldi. Keyingi urinish yaxshiroq bo'ladi." |
| **P4** Real-Life | Wrong sub-question | "Hali emas! Mutaxassis sifatida qayta o'ylang — yana qaysi ma'lumot kerak?" |
| **P5** Consolidation | Concept not recalled | "Hali emas — Saroyingiz qurilgan! Ertaga qaytib borsak, eslay olasiz." |
| **P6** Boss | Wrong answer | "Hali emas! Miyangiz Feedback oldi. Keling, Tekshiramiz (Check) — qayerda tushunmovchilik bor?" |
| **P6** Boss | Boss defeat (HP > 0) | "Hali emas! Boss hali yengilmagan — lekin Bilim Bazangiz kuchaydi. Keling, Moslashtiramiz (Adjust)." |
| **P7** Reflection | <60% accuracy | "Bugun ko'p Feedback oldingiz — bu ajoyib! Har bir Feedback miyangizni kuchaytiryapti." |

### TEFCAS Socratic Sequence (Phase 6 Post-Failure)

```
PROMPT 1 — CHECK (C):
  "Keling, tekshiramiz. [Failed_concept] haqida nima bilasiz?"

PROMPT 2 — ADJUST (A):
  "Yaxshi. Endi moslashtiramiz. Agar [failed_concept] o'rniga
   [simpler_analogy] deb o'ylasangiz — javob qanday o'zgaradi?"

PROMPT 3 — SUCCESS (S):
  "Ajoyib! Endi qayta urinib ko'ring. Yangi strategiyangiz bilan Success ga erishishingiz mumkin."
```

### Voice Principles

1. **Brain-science language, not generic praise.** "Your brain just formed a new connection" not "Good job!"
2. **TEFCAS vocabulary embedded naturally.** Trial, Feedback, Adjust, Success as everyday words.
3. **Radiant/Supernova metaphors.** Knowledge "radiates," ideas are "sparks," learning "branches out."
4. **Always positive framing.** Even when correcting, frame as growth.
5. **Uzbek-first.** All templates authored in Uzbek with English equivalents.

### 32 Template Phrases (Tier 1 — Zero LLM Cost)

All templates stored as JSON lookup table keyed by `trigger_event` + `performance_band` + `phase`. Templates rotate via round-robin to avoid repetition across sessions. Full template library in original spec (32 phrases covering correct answers, streaks, wrong answers, phase transitions, boss defeat/victory, session complete, and specific mechanics).

---

## 6. Radiant Summary Game Mechanic

### What It Is

A visual consolidation mechanic where the student completes a partially-built radiant map of the lesson's key concepts. Fills the undefined "Mind maps" slot in UNIFIED spec Phase 5.

### Core Loop

```
Study map (10s) → Drag keywords to branches (60-90s) → Review & Score
```

**Phase A (10s):** Partially completed radiant map appears. Central image + main branches (BOIs) pre-placed. Empty slots on sub-branches. Draggable keyword chips at bottom.

**Phase B (60-90s):** Student drags keyword chips onto empty branch slots. Correct = green pulse + locks. Wrong = bounce back + soft shake. Keyword pool contains 2-3 distractors that don't belong.

**Phase D (Score):** Completed map shown with corrections. XP awarded. Map saved to Bilim Bazasi.

### Input Schema (Content Author)

```json
{
  "radiant_summary_instance": {
    "topic_code": "SCI-G5-CH4-PHOTO",
    "central_image": { "id": "img_photosynthesis_sun", "label_uz": "Fotosintez" },
    "main_branches": [
      {
        "boi_label_uz": "Kerakli moddalar",
        "color": "#2E7D32",
        "sub_branches": [
          { "slot_type": "empty", "correct_keyword_uz": "Yorug'lik" },
          { "slot_type": "empty", "correct_keyword_uz": "Suv" }
        ]
      }
    ],
    "distractor_keywords": [
      { "keyword_uz": "Oqsil" },
      { "keyword_uz": "Ildiz" }
    ]
  }
}
```

### Evaluation

| Result | Scoring |
|---|---|
| Correct first try | 80 XP per keyword |
| Correct second try | 40 XP per keyword |
| Distractor avoided | +20 XP per distractor |
| Distractor placed | -10 XP (bounces back) |

### Parameters (G5 Defaults)

| Parameter | Default | Effect |
|---|---|---|
| `boi_count` | 4 | More BOIs = wider map |
| `empty_slots_total` | 5-6 | More slots = more placement decisions |
| `distractor_count` | 2 | More distractors = harder discrimination |
| `study_time` | 10s | Shorter study = harder |
| `placement_time` | 60s | Shorter = more pressure |

**G5-6 Rules:** Landscape, max 4 BOIs, Icon-First, tap-to-select from 3 options.

### PISA / Bloom's

- **PISA:** L1-L2 (categorization, hierarchical relationships). L3 when cross-branch associations tested.
- **Bloom's:** Remember → Understand (primary), Analyze (Supernova Sprint, optional).
- **Transition skills:** `L1→L2: organize related concepts into hierarchical categories`

### Subject Eligibility

All subjects eligible. Content-agnostic — any subject with 2+ hierarchical categories benefits.

### Cost Profile

- **Tier 1:** Map rendering, drag-and-drop, keyword matching, XP. ~$0.0001/round.
- **Tier 2:** Fuzzy matching for open input (G7+). ~$0.001/Supernova round.
- **Tier 3:** None.

---

## 7. Peg System Game Mechanic

### What It Is

A mnemonic mechanic using visual "pegs" — memorable images permanently associated with numbers 1-10 — as hooks for lesson concepts. Fills the undefined "Peg system" slot in UNIFIED spec Phase 5.

### Core Loop

```
Learn pegs (first time only, 30s) → Associate concepts to pegs (45-60s) → Recall test (45-60s) → Score
```

**Phase A (30s, first time only):** Show 5 pegs with images. Student taps each to see the image and association.

**Phase B (45-60s):** 5 lesson concepts + 5 peg images. Student drags each concept to a peg. Link sentence appears: "Sham (1) yonmoqda — Fotosintez ham yorug'lik bilan boshlanadi!"

**Phase C (45-60s):** Pegs shown one at a time in random order. Student selects the correct concept. Then reverse: concept shown, student selects peg.

### Culturally Adapted Peg Set (Uzbekistan)

| # | Shape | Uzbek | Image |
|---|---|---|---|
| 1 | Candle | Sham | Tall burning candle |
| 2 | Swan | Oqqush | Graceful white swan |
| 3 | Heart | Yurak | Red heart |
| 4 | Sailboat | Yelkanli kema | Boat with triangular sail |
| 5 | Hook | Ilgak | Metal coat hook |
| 6 | Elephant trunk | Fil xortumi | Elephant with curled trunk |
| 7 | Cliff | Qoya | Cliff edge with flag |
| 8 | Snowman | Qorbobo | Two-ball snowman |
| 9 | Balloon | Shar | Balloon on string |
| 10 | Bat & ball | To'p va tayoq | Cricket bat with ball |

**Number-Rhyme variant** available for G7+ (Bir→Shir/Lion, Ikki→Tikki/Needle, etc.).

### Evaluation

| Result | Scoring |
|---|---|
| Peg → Concept, correct first try | 60 XP |
| Peg → Concept, correct second try | 30 XP |
| Concept → Peg, correct | 40 XP |
| All 10 correct (both directions) | +100 XP bonus |
| **Max score** | **600 XP** |

### Parameters (G5 Defaults)

| Parameter | Default |
|---|---|
| `peg_count` | 5 (pegs 1-5) |
| `peg_type` | shape (default for G5-6) |
| `association_time` | 45s |
| `recall_time` | 60s |
| `bidirectional` | true |

### PISA / Bloom's

- **PISA:** L1-L2. `L1→L2: use visual mnemonic anchors to organize and retrieve factual information`
- **Bloom's:** Remember (primary), Understand (link sentences require comprehension).

### Subject Eligibility

All subjects. Concept-agnostic — works for any subject with discrete facts to memorize.

### Cost Profile

- **Tier 1 only.** ~$0.0001/round. Cheapest mechanic in the catalog.

### Tic Tac Toe Integration

When Peg System + Tic Tac Toe are both selected: 9 cells labeled with peg numbers. To place X on cell #3, student must recall "Yurak (3) — bu nima?" Correct recall = X placed.

---

## 8. Phase Amendments

### Phase 1: Link Chain Format (Method #28)

New Memory Sprint format #6 (alongside MC, Speed Match, Flash Sprint, Fill-Blanks, Order Steps).

**Flow:** 5 sequential items with pre-authored link story using SMASHIN' SCOPE principles (15s study). Recall tested out of order via 4-option MC (45s). +60 XP correct, +100 bonus all 5.

**Best for:** Sequential content (process steps, timelines). NOT for unrelated vocabulary or math formulas.

### Phase 1: Buzan Review Intervals (Method #34)

Four mandatory review touchpoints override SM-2 when SM-2 would schedule later:

| Touchpoint | Timing | NETS Phase |
|---|---|---|
| ~10 min | Phase 5 of same session | Already exists |
| ~24 hours | Phase 1 of NEXT session | **ADD floor constraint** |
| ~1 week | Phase 1, 7 days later | **ADD floor constraint** |
| ~1 month | Phase 1, 30 days later | **ADD floor constraint** |

**Rule:** `actual_next_review = MIN(sm2_next_review, buzan_next_mandatory)` — whichever is sooner wins.

**Algorithm:** After Memory Sprint item selection step 2, inject Buzan mandatory items at high priority. If list exceeds 8 items, drop lowest-priority non-Buzan item.

### Phase 2: Semantic Chunking (Method #20)

G5-6 Story Mode text rendered with wider gaps (0.4em) between 3-5 word semantic chunks. Chunk boundaries pre-computed in content pipeline. Improves readability for developing readers.

### Phase 3: Von Restorff Anchor (Method #14)

One game per session (always the middle game / Game Break 2) tagged as the Von Restorff Anchor — deliberately unusual, funny, or visually striking. Resets attention at the "Sag" point of Buzan's MIG curve. Content pipeline: at least 3 items per lesson's game pool tagged `outstanding: true`.

### Phase 3: Cortical Diversity Constraint (Method #25)

Every game mechanic receives a modality tag: `VL` (Verbal/Logical), `VS` (Visual/Spatial), `KM` (Kinesthetic/Motor), `SD` (Strategic/Decision), `PG` (Productive/Generative). Session's 3 games should span at least 2 different modalities.

**Note:** This is a soft constraint, not a hard rule. If a student's weakest domain is in one modality and the content pool's strongest games are all that modality, prioritize learning over diversity.

### Phase 4: W5H Radiant Analysis Scaffold (Method #4)

Real-Life Challenge gains a pre-solution scaffold: 6-branch radiant frame (Who/What/Where/When/Why/How). Student fills at least 4 of 6 branches before writing answer (G5-6 mandatory, G7-8 toggleable, G9+ optional button). Frame NOT scored; only the final answer is scored.

### Phase 5: Link System Technique (Method #28 extension)

Available as a Phase 5 Consolidation technique (distinct from Phase 1 "Link Chain"). Technique selection by content structure:

| Content Structure | Phase 5 Technique |
|---|---|
| Sequential | Link System |
| Spatial | Memory Palace |
| Hierarchical | Radiant Summary |
| Discrete facts | Peg System |

### Phase 7: TEFCAS Reflection Prompts

Already defined in Section 5 (AI Tutor Language). Replaces generic reflection prompts with TEFCAS-structured metacognition. Student's stored learning goal from Panel 6 resurfaced: "Remember, you wanted to learn [X]. Did you figure it out?"

### MIG Formalization (Methods #26, #33)

The 7-phase structure IS Buzan's Memory Integration Graph in action:
- **Primacy Effect** → Phase 1 (Memory Sprint)
- **Recency Effect** → Phase 7 (Reflection)
- **Association Effect** → Phase 0-A/0-B
- **Von Restorff Effect** → Phase 3 anchor
- **The Sag** → Phase 3 Game Breaks reset the curve

Documentation only. No code changes needed.

---

## 9. What Was Cut & Why

| Method | Name | Reason for Cut |
|---|---|---|
| 15 | Anti-Cheat Radiant Signature | Pseudoscientific. Linear text patterns don't indicate cheating — they indicate systematic thinking. Would create false positives against students who think linearly. |
| 16-23 | Speed Reading cluster (Focus Guide, Saccade Optimization, Regression Elimination, Peripheral Vision, Sub-vocalization Elimination, Meta-Guiding) | Category error. These belong in a future Reading Fluency module, not injected into homework sessions. Speed reading research (Rayner et al. 2016) shows it doesn't improve comprehension — it teaches skimming. G5 students struggle with comprehension, not speed. |
| 5 | Decision Mapping in Boss fights | Conceptually wrong. Boss is an assessment gate, not a decision-support tool. W5H scaffold in P4 RLC captures the value without misplacing it in P6. |
| 30 | Major System | Linguistically broken for Uzbek. The phoneme-to-consonant mapping assumes English phonology. Uzbek has 33 phonemes with different distributions. Needs separate linguistic analysis before it can work. |
| 3 | Group Mind Mapping | Conflicts with banned Peer Teaching for Uzbek classroom culture. AI simulating a classmate's map doesn't solve the underlying issue. Deferred to future multiplayer module. |
| 8 | Secret Symbols | Accessibility gap — visually impaired students can't use symbol stickers. Needs haptic/audio alternative first. Deferred. |
| 31 | SEM³ Memory Matrix | Good concept, premature implementation. Data model can be built later as JSON schema + write-on-play logging. Session Assembler integration deferred. |

### What's Kept for Future Roadmap

- **Semantic Chunking** (Method #20) — genuinely useful for G5-6 readability. Included in this spec.
- **W5H Radiant Analysis** (Method #4) — useful as P4 scaffold, not P6 Boss. Included in this spec.
- **Von Restorff Anchor** (Method #14) — formalizes existing behavior, adds pipeline QA. Included but noted as documentation-heavy.

---

## Summary: Core Injection at a Glance

| Layer | Methods Injected | What Changes |
|---|---|---|
| **A — Phase-Bound** | 1, 3-5, 7-8, 20, 24, 27-29, 34 | New game mechanics (Radiant Summary, Peg System, Link Chain), Phase amendments, Buzan Review Intervals |
| **B — Cross-Cutting** | 2, 11-14, 25-26, 33 | TEFCAS naming, BOST alignment, Radiant UI Standard, Von Restorff, Primacy/Recency formalization, MIG |
| **C — UI/UX** | 2, 6, 9, 17, 19, 20 | 7 Laws compliance, G5-6 simplified rules, Subject Color System, Reading Optimization, Semantic Chunking |
| **D — AI Language** | 10-11 | "Hali emas!" failure responses, TEFCAS Socratic prompts, 32 template phrases |
| **E — Content Pipeline** | 12, 22, 32 | 80/20 keyword extraction, Dual Coding check, SMASHIN' SCOPE gate, Schema Activation |

**Cost impact:** Zero Tier 3. All new mechanics are Tier 1 or Tier 2. `$3-5/student/year` target preserved.
**Lines changed in UNIFIED spec:** ~200 lines of amendments across Sections 1-10.
**New companion docs:** This spec, AI Tutor Language templates (separate file if needed).

---

*Document path: `All analysis/Buzan Injection/NETS-Buzan-Core-Injection.md`*
*Primary source: `Buzan_Injection_Specification.md` (2,564 lines, condensed to this ~1,400-line core)*
*Constitution: `NETS-Homework-Engine-UNIFIED.md` v2.0*
*Status: v1.0 Core Injection — 22 of 34 methods. 12 methods cut or deferred (see §9).*
