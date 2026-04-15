# NETS Homework Engine — Unified Specification

**Version 2.0 — April 2, 2026**
**Status: Single Source of Truth — Supersedes All Previous Versions**
**Target: 8.8M K-11 Students, Uzbekistan**
**PISA 2022 Baseline: Math 364, Reading 336, Science 355**
**Goal: 80%+ students currently below Level 2 move to Level 2-3 within 2 years**

> This document is the authoritative specification for the NETS Homework Engine.
> It supersedes: `NETS-Homework-Engine-Specification.md` (v1.0), `HOMEWORK_STANDARDS.md` (v1.0),
> `HOMEWORK_TASK_ENGINE.md` (v1.0), and all gap analysis documents.
> Engineering and content teams build exclusively from THIS document.

---

## Table of Contents

1. [Core Principles and Philosophy](#1-core-principles-and-philosophy)
2. [Content Reference Architecture](#2-content-reference-architecture)
3. [PISA Proficiency Framework](#3-pisa-proficiency-framework)
4. [The Homework Session Engine](#4-the-homework-session-engine)
5. [Phase Specifications](#5-phase-specifications)
6. [14 Game Mechanics Specification](#6-14-game-mechanics-specification)
7. [PISA Skill Progression Framework](#7-pisa-skill-progression-framework)
8. [PISA Creative Thinking Domain](#8-pisa-creative-thinking-domain)
9. [Difficulty Adaptation Engine](#9-difficulty-adaptation-engine)
10. [Textbook-to-NETS Content Pipeline](#10-textbook-to-nets-content-pipeline)
11. [Gamification Economy](#11-gamification-economy)
12. [Edge Cases and Recovery Modes](#12-edge-cases-and-recovery-modes)
13. [Anti-Cheat System](#13-anti-cheat-system)
14. [Teacher Controls](#14-teacher-controls)
15. [Integration Points](#15-integration-points)
16. [Homework Task JSON Schema](#16-homework-task-json-schema)
17. [Grade-Level Implementation Matrix](#17-grade-level-implementation-matrix)
18. [AI Refinement Constraints](#18-ai-refinement-constraints)
19. [Bilingual Language Acquisition Framework](#19-bilingual-language-acquisition-framework)
20. [Research Citations and Evidence Base](#20-research-citations-and-evidence-base)

---

## 1. Core Principles and Philosophy

### 1.1 The NETS Learning Pyramid

*Source: HOMEWORK_STANDARDS.md Section 1.1. Retained because it maps Bloom's to PISA with the critical ENGAGE foundation layer.*

Every homework session MUST map to Bloom's Taxonomy through the NETS Learning Pyramid:

```
                    +-------------+
                    |  TRANSFER   | <-- Real-Life Challenges (PISA Level 5-6)
                   +---------------+
                  |    ANALYZE     | <-- Why Chain, Mystery Box (PISA Level 4)
                 +------------------+
                |      APPLY        | <-- Adaptive Quiz, Final Boss (PISA Level 3)
               +--------------------+
              |     UNDERSTAND       | <-- Story Mode, Tile Match (PISA Level 2)
             +------------------------+
            |       REMEMBER          | <-- Memory Sprint, Flashcards (PISA Level 1)
           +--------------------------+
           |     ENGAGE (Foundation)   | <-- Gamification, Flow State
           +---------------------------+
```

**NON-NEGOTIABLE:** Every homework session MUST include activities spanning at least 4 levels of the pyramid.

### 1.2 The 3 Sacred Principles

#### Principle 1: Textbook is Source of Truth, NETS is the Transformer

| What Textbook Does | What NETS Does |
|---|---|
| Provides core concepts | Forces REASONING with concepts |
| Presents information | Creates active engagement |
| Shows solved examples | Requires student to CONSTRUCT solutions |

**STANDARD:** Homework MUST NOT change core concepts from textbooks. It MUST adapt delivery method to active, gamified, AI-personalized learning.

*Source: Both specs agreed. Textbook analysis of Grade 5 Math (2024 RU edition) confirmed CPA progression already present in textbooks, making NETS integration natural.*

#### Principle 2: Flow State is Mandatory

Based on Csikszentmihalyi (1990), every student MUST be maintained in the flow channel:

```
Challenge Level
    |         ANXIETY (Overwhelmed - Student Quits)
    |              /
    |            /
    |          /  +===========+
    |        /    | FLOW      | <-- TARGET ZONE
    |      /      | 70-80%    |
    |    /        | Success   |
    |  /          +===========+
    |/___________________________
    |    SKILL Level    \
    |                     \
    |                       BOREDOM (Underwhelmed - Student Quits)
```

**STANDARD:** AI MUST adjust difficulty every 3-5 questions:
- Below 60% success rate --> Reduce difficulty by 1 tier
- Above 90% success rate --> Increase difficulty by 1 tier
- 70-80% success rate --> Maintain current tier

*Source: HOMEWORK_STANDARDS.md. Chosen over the original spec's "3 consecutive correct/2 consecutive wrong" rule because percentage-based thresholds are more robust against variance.*

#### Principle 3: Intrinsic Motivation > Extrinsic Rewards

All rewards MUST celebrate LEARNING PROGRESS, not compliance.

| DO (Intrinsic) | DON'T (Extrinsic) |
|---|---|
| "You mastered fractions!" | "You logged in 7 days!" |
| "Your reasoning improved!" | "You clicked 100 times!" |
| "You helped a classmate!" | "You watched an ad!" |

**STANDARD:** Zero pay-to-win mechanics. Zero real-money purchases. Every reward is earned through demonstrated learning.

*Source: HOMEWORK_STANDARDS.md Principle 3. Critical design constraint — the gamification economy (Section 11) must comply.*

### 1.3 The "No Busywork" Rule

**Every task must explicitly scaffold ONE specific PISA transition skill.** No filler questions. No repetition without purpose. If a task cannot be tagged to a transition skill, it does not enter the content pool.

*Source: HOMEWORK_TASK_ENGINE.md. This is the single most important design constraint for content creators.*

### 1.4 Buzan Cognitive Foundation

The NETS 7-phase structure is built on Tony Buzan's research into how the brain learns. Two frameworks underpin the session design:

**TEFCAS — The Learning Loop.** Every NETS session is a TEFCAS cycle: Trial (Phase 3 — student attempts problems) → Event (outcome) → Feedback (immediate per-item feedback) → Check (IRT engine recalculates proficiency) → Adjust (difficulty adapts + Phase 5 targets weak areas) → Success (Phase 6 Boss defeat). This is not a new addition — it is the *naming* of what the engine already does. The AI tutor uses TEFCAS vocabulary: failures are "Feedback," not errors. The system-wide maxim: **"There is no such thing as failure, only feedback."**

**The MIG — Why 7 Phases Exist.** Buzan's "Most Important Graph" describes recall during a session:
- **Primacy Effect** → Phase 1 (Memory Sprint) places key items first, when recall is highest
- **Recency Effect** → Phase 7 (Reflection) ensures the last mental act consolidates learning
- **Association Effect** → Phase 0-A/0-B activate prior schemas so new content anchors to existing knowledge
- **Von Restorff Effect** → Phase 3 (Game Breaks) mid-session anchor provides a memorable, outstanding moment
- **The Sag** → Game Breaks split the session into sub-sessions, resetting the Primacy/Recency curve multiple times

**BOST — The Study Technique the Engine Models.** The Buzan Organic Study Technique maps onto NETS: Browse (Phase 0-A Theme Preview) → Time/Amount (session timer) → Prime what you know (Phase 0-A "What do you already know?" prompt) → Questions/Goals (Phase 0-A "What do you want to learn?") → Overview (Phase 0-B Flash Cards) → Preview/Inview (Phase 2-3 Story + Games) → Review (Phase 5+7 Consolidation + Reflection).

**Where Buzan does NOT apply:** Buzan methods are delivery mechanisms — the HOW, never the WHAT. They never alter textbook content, curriculum standards, or PISA calibration. Sections 2 (Content Architecture), 3 (PISA Framework), 11 (Gamification Economy), 14 (Teacher Controls), and 15 (Integration Points) are unchanged by Buzan injection.

### 1.5 National Pride & Progress Module ("Milliy G'urur va Taraqqiyot")

The NETS engine embeds Uzbek national pride and global wisdom into homework sessions. This is NOT patriotic decoration — it connects learning to purpose ("Your knowledge builds something real") and positions Uzbekistan as part of the world, not separate from it.

**Two Ratios Govern All Injected Content:**

| Rule | Ratio | What It Means |
|---|---|---|
| **The Origin Balance** | **55% National / 45% Global** | Over any rolling 10-item window, ~55% of injected facts/quotes/settings reference Uzbekistan; ~45% reference global science, figures, or events. Individual sessions may deviate. |
| **The Type Balance** | **70% Facts / 30% Quotes** | Between-phase content is 70% "Bilarmidingiz?" curiosity facts and 30% "Hikmatlar" wisdom quotes. Facts trigger cognitive engagement; quotes trigger emotional reflection. |

**Where National Pride Content Appears:**

| Phase | What Gets Injected | How | Frequency |
|---|---|---|---|
| **0-A: Theme Preview** | Topic-relevant wisdom quote with 5-second skip lock | Gate quote before Panel 1. Pulled from `quotes_database.json`, subject-tagged. "Davom etish" (Continue) button disabled for 5 seconds with visible countdown. | 1 per session |
| **Transitions (between phases)** | "Bilarmidingiz?" fact or "Hikmatlar" quote | Merges into existing §6.5 "Did You Know..." loading screen insights. 70/30 type balance, 55/45 origin balance. | 1 per transition |
| **2: Story Mode** | Ambient setting tagged national or global | Narrative segments tagged `setting_origin: "national" | "global"`. Rolling 55/45 balance across sessions (not per-session — a single session about Uzbek History can be 100% national). | Per story |
| **4: Real-Life Challenge** | "Wise Status" role + heritage hook + closing | For 30% of Phase 4 tasks: student gets a professional title ("Bosh Muhandis," "Strategik Tahlilchi"), problem anchored in Uzbek or global achievement, closing connects to national/global progress. Academic core UNTOUCHED. | ~1 in 3 sessions |
| **5: Consolidation** | Heritage anchor in mnemonic link sentences | When organically relevant — e.g., Peg System link sentence: "Mirzo Ulug'bek yulduzlarni sanagan — siz ham shu aniqlikda hisoblang." Not forced. | When natural |
| **7: Reflection** | Closing line connecting learning to contribution | After TEFCAS prompts and BOST goal recall: "Sizning bilimingiz Uchinchi Renessansning poydevoridir" (national) or "Sizning aniq fikrlashingiz global standartlarga mos keladi" (global). | 1 per session (≥60% accuracy only) |

**Where National Pride Content Does NOT Appear:**

| Phase | Why Not |
|---|---|
| **0-B: Flash Cards** | Pure reference. No emotional framing. |
| **1: Memory Sprint** | 2-minute high-speed recall. Adding role framing wastes precious seconds. |
| **3: Game Breaks** | Game mechanics own the engagement. Pride framing adds cognitive overhead to games designed for flow. |
| **6: Final Boss** | Pure PISA assessment gate. No framing, no injection, no heritage hooks. The Boss tests demonstrated competence — adding pride content would dilute assessment validity. |

**"Wise Status" Recipe (Phase 4 only, 30% of tasks):**

1. **Assign Status:** Professional title, not praise. "Siz Bosh Muhandissiz" (You are the Chief Engineer), not "Siz juda aqllisiz" (You are very smart).
2. **Set the Arena:** National (55%): anchor in a real Uzbek achievement (Afrosiyob, IT-Park, Ulug'bek Observatory). Global (45%): anchor in a global standard (CERN, NASA, WHO).
3. **Bridge:** Connect the textbook question to the arena. The academic core (formula, calculation, reasoning) is UNTOUCHED.
4. **Closing:** "Sizning aniqligingiz Uchinchi Renessansni quradi" (national) or "Sizning natijangiz global standartlarga mos" (global).

**Additional Rules from National Pride Proposal:**

| Rule | Implementation |
|---|---|
| **5-second skip lock on Phase 0-A quote** | The gate quote in Phase 0-A has a 5-second countdown timer. The "Davom etish" (Continue) button is disabled until the timer expires. This ensures students read the mindset-setting quote before proceeding. |
| **20% all-task injection** | Every 5th homework task across Phases 1, 2, 4, 5, and 7 gets national pride framing — professional title + heritage/global context anchor. This applies to Memory Sprint (brief role intro before recall), Phase 4 (full Wise Status recipe), and Phase 5 (heritage mnemonic anchor). Phase 0-A/0-B, Phase 3 (Game Breaks), and Phase 6 Boss are excluded. |
| **Phase 6 "certification" framing** | Final Boss is reframed as a "professional certification." On Boss entry: *"Bu — sizning professional sertifikatingiz. Global standartga mos keling."* On Boss defeat: *"Sertifikatsiya muvaffaqiyatli! Siz [Role] sifatida tasdiqlandingiz."* The HP/Boss game mechanics remain unchanged — only the narrative framing changes. |
| **Dark mode (#0a0a0a) as default** | The platform defaults to dark mode (#0a0a0a background) for all National Pride injection screens (gate quote, between-phase facts/quotes, milestone breaks). In-session phases use the existing theme. Students can override in settings. |

**Data Source:** `quotes_database.json` (4,800+ items, structured with type/author/text/category/origin/id). Requires subject-tagging before deployment (current `category: "General"` is insufficient for relevant matching).

---

## 2. Content Reference Architecture

### 2.1 Hierarchy

*Source: Original spec Section 2.1. Best-structured hierarchy across all sources.*

Every piece of content in NETS follows this strict hierarchy:

```
TEXTBOOK (physical book, specific edition)
  +-- CHAPTER (bob)
        +-- TOPIC (mavzu)
              +-- LEARNING OBJECTIVE (o'quv maqsadi)
                    +-- CONTENT BLOCK (kontent bloki)
                          +-- ASSESSMENT ITEM (baholash elementi)
```

**Example:**

```
Matematika 5-sinf (2024 nashr)
  +-- 3-bob: Oddiy kasrlar (Common Fractions)
        +-- Mavzu 3.4: Teng kasrlar (Equivalent fractions)
              +-- LO-3.4.1: Explain why 2/4 = 1/2 using visual models
                    +-- Block: CPA Stage 2 -- Pictorial bar model
                          +-- Item: Tile Match pair (visual x equation)
```

### 2.2 Learning Units (LU)

*Source: HOMEWORK_TASK_ENGINE.md. Adds critical intermediate concept between Topic and Content Block.*

Each textbook chapter is split into Learning Units (LUs):
- Typically 1-3 LUs per chapter section
- Each LU maps to exactly one curriculum standard code
- Each LU has a prerequisite chain (e.g., fractions require whole number division)
- Each LU generates 10-15 tasks across Bloom's levels: 4 Remember, 3 Understand, 3 Apply, 2 Analyze, 1-2 Evaluate/Create
- Each task is assigned to exactly one game mechanic

### 2.3 Content Block Types

Each Learning Objective is delivered through multiple content blocks. Every block has a fixed type:

| Block Type | Purpose | Used In Phase | Source Layer |
|---|---|---|---|
| `recall_item` | Quick-fire warm-up question from current chapter's key concepts | Phase 1: Memory Sprint | Textbook |
| `narrative_segment` | Textbook content rewritten as story/documentary | Phase 2: Story Mode | Textbook + NETS |
| `checkpoint_question` | Comprehension gate between narrative segments | Phase 2: Story Mode | PISA-calibrated |
| `game_item` | Practice item for a specific game mechanic | Phase 3: Game Breaks | Textbook + PISA |
| `transfer_scenario` | Cross-subject real-world problem | Phase 4: Real-Life Challenge | PISA-calibrated |
| `mnemonic_exercise` | Memory Palace, acronym, flashcard consolidation | Phase 5: Mnemonic Lock | NETS |
| `boss_question` | PISA-calibrated assessment question | Phase 6: Final Boss | PISA-calibrated |
| `reflection_prompt` | Metacognitive self-review prompt | Phase 7: Battle Replay | NETS |

**Source Layer Key:**
- **Textbook** = content derived directly from textbook material
- **NETS** = NETS-designed delivery wrapper (does not alter concepts)
- **PISA-calibrated** = difficulty and skill targeting governed by PISA framework
- **Textbook + PISA** = textbook content with PISA-level difficulty calibration
- **Textbook + NETS** = textbook content with NETS narrative/engagement layer

### 2.4 Dual Standard Code Format

*Resolution: The colleagues' descriptive format `UZ-MATH-5-FRAC-01` is the PRIMARY format. The original dotted format `MAT.5.1.3.2` is supported as an alias for backward compatibility.*

**Primary Format (descriptive):**
```
UZ-{SUBJECT}-{GRADE}-{TOPIC}-{SEQ}
```

| Code | Meaning |
|---|---|
| `UZ-MATH-5-FRAC-01` | Uzbekistan, Mathematics, Grade 5, Fractions, Objective 01 |
| `UZ-SCI-7-PHOTO-03` | Uzbekistan, Science, Grade 7, Photosynthesis, Objective 03 |
| `UZ-READ-5-NARR-02` | Uzbekistan, Reading, Grade 5, Narrative text, Objective 02 |
| `UZ-HIST-9-SILK-01` | Uzbekistan, History, Grade 9, Silk Road, Objective 01 |
| `UZ-INF-8-PROG-02` | Uzbekistan, Informatics, Grade 8, Programming, Objective 02 |

**Alias Format (backward-compatible, dotted):**
```
{SUBJECT}.{GRADE}.{CHAPTER}.{TOPIC}.{LEARNING_OBJECTIVE}
```

| Code | Equivalent Primary |
|---|---|
| `MAT.5.3.4.1` | `UZ-MATH-5-FRAC-01` (Chapter 3, Topic 4, LO 1) |
| `SCI.7.4.2.1` | `UZ-SCI-7-PHOTO-01` |

**Implementation:** The system stores both formats. Every API response and content tag includes both. Alias lookup table maintained per textbook edition.

### 2.5 Mandatory Tagging Schema -- Every Item

Every single content block and assessment item in the system MUST carry these tags before it enters the live pool:

```json
{
  "textbook_ref": {
    "textbook_id": "mat-5-2024-uz",
    "grade": 5,
    "subject": "math",
    "language": "uz",
    "chapter": "Oddiy kasrlar",
    "section": "Teng kasrlar",
    "page_range": "52-58",
    "textbook_isbn": "978-9943-XXXX",
    "textbook_year": 2024
  },
  "standard_ref": {
    "primary_code": "UZ-MATH-5-FRAC-01",
    "alias_code": "MAT.5.3.4.1",
    "standard_description": "Kasrlarning teng ekanligini isbotlash",
    "curriculum_year": 2024
  },
  "pisa_ref": {
    "domain": "mathematics",
    "proficiency_level": 2,
    "content_category": "quantity",
    "process_category": "employ",
    "context": "personal",
    "transition_skill": "L1->L2: interpret simple visual representations"
  },
  "blooms_level": "understand",
  "language": "uz",
  "ai_tier": 1,
  "review_status": "approved",
  "game_mechanic": "tile_match",
  "prerequisites": ["UZ-MATH-4-DIV-03", "UZ-MATH-5-FRAC-01"]
}
```

**Critical addition:** The `transition_skill` field is MANDATORY. Every task must explicitly declare which PISA level transition it scaffolds (e.g., "L1->L2: extract from simple charts", "L2->L3: sequential decision-making"). This field was absent from all previous specs.

*Source: transition_skill concept from HOMEWORK_TASK_ENGINE.md; tagging schema structure from original spec Section 2.3.*

**No tag, no deployment.** Content missing any required tag is held in `draft` status and flagged for completion.

---

## 3. PISA Proficiency Framework

### 3.0 Official PISA Level Definitions

*Source: Gap analysis (Leonardo) identified that previous specs referenced PISA levels without defining them. These are official OECD competency descriptors that content creators MUST reference when designing questions.*

#### Mathematics

| Level | Score Range | What Students Can Do | Uzbekistan Status |
|---|---|---|---|
| Below 1 | <258 | Read single values from labeled charts; basic whole-number arithmetic | ~15% of students |
| 1 | 258-357 | Answer questions in familiar contexts with all information present; single-step procedures | ~40% of students |
| 2 | 358-419 | Recognize situations needing simple strategies; extract info from tables/charts; basic ratios; literal interpretation of results | ~25% of students (TARGET MINIMUM) |
| 3 | 420-481 | Execute multi-step procedures; interpret representations from multiple sources; select simple problem-solving strategies; communicate reasoning | ~12% of students |
| 4 | 482-544 | Work with explicit models for complex situations; select and integrate representations; construct explanations | ~5% of students |
| 5 | 545-606 | Develop models for complex situations; systematic problem-solving; reflect on results in real-world context | ~2% of students |
| 6 | >607 | Conceptualize, generalize, use advanced math reasoning; link multiple information sources; creative flexible thinking | <1% of students |

#### Reading

| Level | Core Competency | Task Type |
|---|---|---|
| 1 | Locate single explicit information in short text | Access and Retrieve |
| 2 | Identify main idea; compare info across simple sources; basic inference | Access and Retrieve + |
| 3 | Integrate several pieces of information; compare/contrast/categorize with competing info | Integrate and Interpret |
| 4 | Interpret nuance; draw inferences from multiple sources; evaluate relevance | Integrate and Interpret + |
| 5 | Evaluate credibility of sources; handle contradictory information; hypothesize about implicit features | Reflect and Evaluate |
| 6 | Critically evaluate multiple complex texts; synthesize across diverse sources; construct novel interpretations with evidence | Reflect and Evaluate + |

#### Science

| Level | Core Competency | Scientific Process |
|---|---|---|
| 1 | Recognize basic scientific facts; identify simple causal relationships | Identify |
| 2 | Explain familiar scientific phenomena; identify variables in simple investigation | Explain |
| 3 | Interpret data/evidence; identify question in simple experimental design | Interpret |
| 4 | Use more abstract scientific content; reflect on actions using scientific evidence | Use Evidence |
| 5 | Apply scientific knowledge to novel/complex situations; evaluate competing explanations | Evaluate |
| 6 | Consistently identify, explain, and apply scientific knowledge in complex life situations; link different information sources and explanations | Evaluate and Create |

*Source: HOMEWORK_TASK_ENGINE.md + OECD PISA 2022 Framework. These definitions MUST be referenced by content creators when claiming a PISA level for any task.*

### 3.1 PISA Level Definitions Applied to NETS

| PISA Level | NETS Bloom's Mapping | Primary Game Mechanics | Transition Skills (L->L+1) |
|---|---|---|---|
| Below Level 1 | Remember | Flashcards, Memory Sprint | Basic recall accuracy |
| Level 1 | Remember-Understand | Tile Match, Sentence Fill, Memory Palace | L1->L2: multi-step reasoning; extract from charts/tables; basic ratio |
| Level 2 | Understand-Apply | Quizzes, Mystery Box, Story Mode | L2->L3: sequential decisions; integrate multiple sources; communicate reasoning |
| Level 3 | Apply-Analyse | Real-Life Challenge, Why Chain, Final Boss (Easy) | L3->L4: explicit models; select/integrate representations; construct explanations |
| Level 4 | Analyse-Evaluate | Why Chain (deep), Final Boss (Medium), Peer Teaching | L4->L5: develop models; compare strategies; reflect on results |
| Level 5-6 | Evaluate-Create | Final Boss (Hard), Real-Life Extended, Creative Lab | L5->L6: conceptualize; generalize; advanced reasoning under novel conditions |

### 3.2 PISA Level as Progression Gate

The student's current PISA level (tracked per subject) determines:

- **Which Bloom's levels they primarily receive** -- A student at PISA Level 1 gets mostly Remember/Understand items.
- **Final Boss difficulty tier** -- Easy=L3, Medium=L4, Hard=L5-6 (see Section 5.6)
- **Game mechanic availability** -- Higher PISA levels unlock harder mechanics
- **Homework completion threshold** -- Final Boss requires demonstrating competence AT the student's target PISA level

### 3.3 PISA Level Tracking Per Student

```json
{
  "student_id": "420d17a7-...",
  "subjects": {
    "mathematics": {
      "current_level": 1.7,
      "target_level": 2.0,
      "last_assessed": "2026-04-01",
      "trajectory": "on_track",
      "domain_breakdown": {
        "quantity": 1.8,
        "space_and_shape": 1.5,
        "change_and_relationships": 1.9,
        "uncertainty_and_data": 1.4
      },
      "transition_skills_mastered": [
        "L1->L2: single-step procedures",
        "L1->L2: extract from labeled charts"
      ],
      "transition_skills_in_progress": [
        "L1->L2: basic ratio understanding",
        "L1->L2: interpret simple visual representations"
      ]
    },
    "reading": {
      "current_level": 1.4,
      "target_level": 2.0,
      "last_assessed": "2026-04-01",
      "trajectory": "at_risk",
      "domain_breakdown": {
        "access_and_retrieve": 1.6,
        "integrate_and_interpret": 1.3,
        "reflect_and_evaluate": 1.1
      }
    },
    "science": {
      "current_level": 1.5,
      "target_level": 2.0,
      "last_assessed": "2026-04-01",
      "trajectory": "on_track",
      "domain_breakdown": {
        "identify": 1.8,
        "explain": 1.5,
        "interpret": 1.3,
        "use_evidence": 1.0
      }
    }
  }
}
```

The continuous PISA scale (e.g., 1.7) is calculated from the student's performance across all assessment items, weighted by recency and item difficulty (IRT). This allows fine-grained tracking without waiting for full PISA-simulation tests.

---

## 4. The Homework Session Engine

### 4.1 Session Duration

*Updated 2026-04-07 per IMPROVEMENTS_TO_THE_CURRENT_FRAMEWORKS.md. Pre-Homework Sessions (Theme Preview + Flash Cards) added to the front of every session, and the 7-phase engine richer (story arcs, expert-POV transfer, dual-pathway checking) — durations increased accordingly.*

| Mode | Duration | Use Case | Default? |
|---|---|---|---|
| **Standard (Homework)** | 30-45 minutes | Daily home use | YES |
| **Extended (In-Class)** | 45-60 minutes | In-class session, teacher-directed | No -- teacher override |
| **Recovery (Condensed)** | 15-20 minutes | Missed homework catch-up | Auto-triggered |

**Pre-Homework overhead** (Theme Preview §4.4 + Flash Cards §4.5): 3-5 additional minutes, student-paced, optional but recommended. The 7-phase Homework Engine begins only after the student presses **"Start my Homework"**.

### 4.2 Session Structure Overview

```
+--------------------------------------------------------------------+
|  HOMEWORK SESSION: [Subject] -- [Chapter] -- [Topic]                |
|  Standard: [UZ-MATH-5-FRAC-01]  |  PISA Target: L2  |  Bloom's: Mix |
+--------------------------------------------------------------------+
|                                                                      |
|  PRE-HOMEWORK (student-paced, optional but recommended)              |
|                                                                      |
|  0-A  THEME PREVIEW ------- 2-3 min --- [hook + context + why]      |
|   |    +-- 8 components, no quiz, no scoring, exploration mode       |
|   |                                                                  |
|  0-B  FLASH CARDS --------- 1-2 min --- [formulas/concepts/rules]   |
|   |    +-- swipeable, returnable during homework                     |
|   |    +-- ends with [ START MY HOMEWORK ] button                    |
|   |                                                                  |
|  ===================================================================  |
|  HOMEWORK ENGINE (7 phases, begins after "Start my Homework")        |
|                                                                      |
|  P1  MEMORY SPRINT -------- 2 min ----- [tap-only, current chapter] |
|   |    +-- MC / True-False / Yes-No-Not Given (3 formats ONLY)       |
|   |                                                                  |
|  P2  STORY MODE ----------- 5-7 min --- [Problem->Struggle->         |
|   |                                       Discovery->Solution arc]   |
|   |    +-- IELTS-style comprehension checkpoints                     |
|   |                                                                  |
|  P3  GAME BREAKS ---------- 6-9 min --- [interleaved practice]      |
|   |    +-- Tile Match / Sentence Fill / Why Chain / Mystery Box /    |
|   |        Tic Tac Toe vs AI                                         |
|   |                                                                  |
|  P4  REAL-LIFE CHALLENGE -- 3-5 min --- [first-person expert POV]   |
|   |                                                                  |
|  P5  CONSOLIDATION -------- 2-3 min --- [mnemonic lock before boss] |
|   |                                                                  |
|  P6  FINAL BOSS ----------- 5-10 min -- [3-tier: Sub / Big / Myth]  |
|   |    +-- FAIL -> Socratic tutoring -> regenerated boss             |
|   |                                                                  |
|  P7  REFLECTION ----------- 2-3 min --- [metacognition + review]    |
|                                                                      |
|  SESSION COMPLETE -- XP awarded, stars calculated                    |
|  Score < 60% -> Duolingo Mode (must redo until passing)              |
+--------------------------------------------------------------------+
```

**Extended Mode (45-60 min):** Story Mode expands to 10 min, Game Breaks to 10 min, Real-Life to 10 min, Final Boss to 10-15 min.

**"Did You Know..." insights** play between phase transitions throughout the session (1 per transition, theme-relevant, 1-2 sentences). See §6.5.

### 4.3 Session Initialization

When a student opens a homework assignment, the engine performs:

```
1. LOAD student_pisa_profile for the subject
2. LOAD homework_assignment (chapter, topic, learning objectives)
3. VERIFY textbook_ref exists for all content blocks
4. CALCULATE difficulty_band based on:
   - Student's current PISA level in this subject
   - Student's domain breakdown (e.g., weak in "quantity" -> harder quantity items)
   - Grade target PISA level
   - Teacher overrides (if any)
5. SELECT content blocks from the pre-generated pool:
   - Pre-Homework: theme_preview_components (§4.4) + flash_cards (§4.5)
   - Phase 1: 5-8 recall_items from CURRENT chapter (warm-up activation)
   - Phase 2: narrative_segments for THIS topic
   - Phase 3: game_items matching the topic's learning objectives
   - Phase 4: 1 transfer_scenario contextualized to Uzbek culture
   - Phase 5: mnemonic_exercise for this chapter's key concepts
   - Phase 6: boss_questions at the student's TARGET PISA level
   - Phase 7: reflection_prompt
6. VERIFY transition_skill coverage:
   - At least 2 different transition skills must be targeted in the session
   - At least 1 must match student's "in_progress" transition skills
7. BUILD session_plan (ordered sequence of all blocks)
8. PRESENT Theme Preview (§4.4), then Flash Cards (§4.5)
9. WAIT for student to press "Start my Homework"
10. START session timer (Phase 1 begins)
```

**Important:** Sessions 0-A and 0-B are pre-homework. The session timer does NOT start until the student presses "Start my Homework". Theme Preview and Flash Cards are student-paced and do not affect XP or assessment scoring.

### 4.4 Theme Preview (Session 0-A)

**Position:** First thing the student sees when opening a homework assignment.
**Purpose:** Hook the student, connect the topic to their world, explain why this matters, equip the mental model before any practice begins. Bridges the gap between textbook reading and gamified homework.
**Duration:** 2-3 minutes (student-paced, no timer pressure)
**Scoring:** None. Pure exploration. No quiz, no XP, no penalties.
**AI Tier:** Tier 2 (content generation), Tier 1 (delivery)

**The 8 Required Components:**

| # | Component | What It Delivers | Min Depth |
|---|---|---|---|
| 1 | **Summary of Book Content** | A cleaner, more digestible reframing of what the textbook chapter covers. Plain language, better visual hierarchy. NOT a rewrite — a refocusing. | **8-10 sentences** |
| 2 | **Better Explanation** | Concepts the textbook assumes the student understands, clarified. Fills the gap between textbook language and student comprehension. | **8-10 sentences** |
| 3 | **Examples** | Additional worked examples beyond what the textbook provides, showing the concept in action step-by-step. | **8-10 sentences** |
| 4 | **Real-Life Research** | The origin story of the concept. Who discovered it? What problem did it solve? What changed in the world because of it? | **8-10 sentences** |
| 5 | **Personal Hook** | First-person address connecting topic to student's own life. "Remember when you saw...?" / "Maybe you've wondered why...?" | **8-10 sentences** |
| 6 | **Why This Matters** | Explicit statement of real-world relevance — not "it's on the exam" but genuine why-you-need-this. | **5-10 sentences** |
| 7 | **Industry Application** | How this concept is used in real industries, jobs, and technology. Shows career relevance. | **5-10 sentences** |
| 8 | **Additional Materials** | Curated external resources (videos, articles, simulators). Language does NOT matter — English, Russian, or Uzbek all permitted. Student picks the language they prefer. | **5-10 sentences** |

**Design Rules:**
- **No quiz, no pressure.** Exploration mode. There are no answers to give, so there are no wrong answers.
- **Student-paced.** No timer. Student scrolls/clicks at their own speed. May skip components.
- **Visual-first, but substantive.** Diagrams, photos, and short video clips complement text — but each panel MUST meet its minimum sentence count (see table above). Depth of explanation is required; do not sacrifice substance for brevity. A panel with 2 sentences and a diagram is incomplete.
- **First-person POV throughout.** "You" not "the student". Direct address, never third-person.
- **Pronoun policy — "Siz" (formal) only.** All student-facing content in Uzbek uses "Siz" (formal/respectful second person). Never use "sen" (informal). This applies universally: narratives, questions, prompts, closings, professional framing. In Uzbek educational and cultural context, "Siz" is the appropriate form for teacher-to-student communication. For Russian content: use "Вы" (formal), not "ты". English has no equivalent distinction — use "you" naturally.
- **Ends with explicit transition** to Flash Cards: *"Before we start — here are the key ideas you'll need."*

**Why this exists:** Demos showed students felt dropped into homework cold. The original framework assumed the student arrives prepared. Theme Preview closes the gap between *reading the textbook* and *doing the homework* — that's where engagement was dying.

**National Pride Injection — Gate Quote with 5-Second Lock:** Before Panel 1, a topic-relevant wisdom quote is displayed from `quotes_database.json` (subject-tagged, 55/45 national/global). The "Davom etish" (Continue) button is disabled for 5 seconds with a visible countdown, ensuring the student reads the quote. After 5 seconds, the button activates. Example for Math: *"Tartib va mantiq — ilmning poydevoridir." — Muhammad al-Xorazmiy.* Example for Science: *"Ilm — o'rganish bilan, amal — qilish bilan." — Abu Ali ibn Sino.* Skipped in Recovery Sessions and Boss-retry sessions.

**Buzan Injection — BOST Pre-reading + Schema Priming:**
- **Panel 1 (Summary)** renders as a **Structural Scan** for G5+: heading tree, bold-term chips, diagram thumbnails — not flowing paragraphs. This trains Buzan's scanning/skimming before deep reading. G3-4 keeps paragraph layout.
- **Panel 5 (Personal Hook)** adds a prompt: *"Bu mavzu haqida nimalarni bilasiz?"* (What do you already know?). Student taps 2-3 keywords or types freely. This is the BOST "Prime" step — activating existing schemas so Phase 2 content anchors to what's already in memory. Tier 1, no scoring.
- **Panel 6 (Why This Matters)** adds: *"Bugun [Mavzu] haqida nimani bilmoqchisiz?"* (What do you want to learn about [Topic] today?). Stored and resurfaced in Phase 7 Reflection. This is the BOST "Questions/Goals" step.
- **Not applied here:** Radiant Thinking, Peg System, Memory Palace — these are consolidation tools (Phase 5), not pre-reading tools. Applying them before the student has encountered content would be premature.

### 4.5 Flash Cards (Session 0-B)

**Position:** Between Theme Preview (§4.4) and the 7-phase Homework Engine.
**Purpose:** Surface every formula, concept, rule, and definition the student will need during the homework. Last reference moment before the challenge begins. Doubles as an in-session reference deck.
**Duration:** 1-2 minutes initial pass (student-paced); accessible throughout homework on demand.
**Scoring:** None. Pure reference.
**AI Tier:** Tier 1 (pre-generated cards from textbook + standards).

**Card Pool — what it must contain:**

| Category | Description |
|---|---|
| **All Key Formulas** | Every formula, equation, or rule the student will encounter in the homework. One per card. |
| **All Key Concepts** | Definitions, terminology, classifications. Example: "What is an oxide?" / "What does valence mean?" |
| **All Key Rules** | Conditions, exceptions, boundaries. Example: "Combustion requires 3 things: fuel, oxygen, heat. If any one is missing, fire stops." |

**Card Pool — what it must NOT contain:**

Flash cards are a **REFERENCE DECK**, not a practice set. If an item asks the student to DO something, it does not belong here.

- NO practice problems or exercises
- NO worked examples (those belong in Phase 0-A Panel 3)
- NO mini-quizzes or checkpoint-style questions
- NO "try this" or "solve this" prompts
- NO scenario-based content
- NO hints or strategies (those belong in Story Mode)

Each card = one formula, one concept, one rule, or one term. Nothing else.

**Design Rules:**
- **One concept per card.** No cramming multiple ideas into a single card. *(Buzan: "One Word Per Branch" applied to cards — max one chunk of 3-5 words per card face.)*
- **Swipeable / scrollable.** Student flips through at their own pace.
- **No testing here.** Reference, not assessment. No right/wrong.
- **Returnable during homework.** A "Flash Cards" button is available throughout the homework session — quick-access overlay. NOT a hint (no penalty), just a reference.
- **Ends with the "Start my Homework" button.** This is the explicit gateway into the 7-phase engine. Only after this press does the session timer start and XP accrue.

---

## 5. Phase Specifications

### 5.1 Phase 1 -- Memory Sprint (2 minutes)

**Purpose:** Warm up the student's brain for the CURRENT chapter's homework. Activate relevant schemas, preview key terminology, and build readiness for the concepts about to be learned. Deliver quick dopamine to energize the session start.

**UPDATED 2026-04-15:** Memory Sprint now targets the CURRENT chapter, not prior chapters. The student has already seen the Theme Preview (0-A) and Flash Cards (0-B) — Memory Sprint is the first active engagement with the current topic's key terms, concepts, and prerequisite connections. Prior-chapter spaced repetition is handled by the platform's adaptive review system outside of homework sessions.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | ≤2 minutes (hard cap) | ≤2 minutes |
| Item count | 5-8 items | 8-10 items |
| Source | **Current chapter** — key terms, prerequisite concepts, foundational facts needed for this session | Same |
| Format | **Tap-only — 3 approved formats ONLY (MC, T/F, YNNG — see table below). NO typing, NO drag-and-drop.** | Same |
| Hints allowed | No | No |
| AI Tier | Tier 1 (pre-generated pool) | Same |

**Approved Memory Sprint Formats (3 ONLY):**

| Format | Description | Best For |
|---|---|---|
| **Multiple Choice** | 4 options, single correct answer. Tap to select. Basic concept checks, formula recognition, terminology. | All subjects |
| **True / False** | Statement displayed, student taps True or False. Fact verification, rule checks, common misconception busters. | All subjects |
| **Yes / No / Not Given** | IELTS-lite warm-up style. Statement presented, student selects Yes, No, or Not Given based on chapter content. Lighter than full IELTS — tests whether the student read/absorbed the material. | All subjects |

**Hard format restrictions:**
- **NO manual typing.** All answers are tap-to-select. No keyboard input.
- **NO open-ended questions.** No "explain why" or "describe how."
- **NO drag-and-drop.** No matching, no ordering, no rearranging.
- **Tap-only interaction.** Student reads → taps one option → gets instant feedback. That's it.

**Content scope:** Items must be basic warm-up questions — simple concept checks, formula recall, terminology recognition, translation between representations. This is a warm-up, not an assessment. Questions should not overwhelm — they should activate prior knowledge and build confidence.

**Format Selection Rule:** Content creator chooses from the 3 approved formats above. All items must have a Start button, instant per-item feedback, streak/combo bonuses, and a final score display. Mixing formats within a single Sprint is permitted (e.g., 3 MC + 2 T/F + 2 YNNG).

**Item Selection Algorithm:**
```
1. GET key concepts, terms, and prerequisite facts from the CURRENT chapter
2. PRIORITIZE by session relevance:
   - Core terminology the student will encounter in Story Mode (Phase 2) -> highest priority
   - Prerequisite concepts from earlier chapters needed to understand current topic -> high priority
   - Key formulas, rules, or definitions introduced in this chapter -> medium priority
3. FILTER to 5-8 items, balanced across the chapter's main concepts
4. RANDOMIZE order
```

**Buzan Injection — Primacy Effect:** Phase 1 is the Primacy window — recall is highest at the start of a session. This is why the most important current-topic items go here — the brain is primed to encode what it sees first. The Link Chain format adds Buzan's Link System mnemonic to the format options.

**Not applied here:** Radiant Thinking, Peg System, Major System — these require encoding time (45-90s) and don't fit the 2-minute hard cap. Memory Sprint is for rapid activation, not deep encoding.

**Scoring:**
- Correct: +100 XP per question
- Streak bonus: +10 XP x current_streak
- Speed bonus: +10 XP if answered in <5 seconds
- No penalty for wrong answers (this is warm-up, not assessment)
- Results feed back into the spaced repetition model

**Adaptation Rules:**
```
IF accuracy >= 80% -> Student ready for new content
IF accuracy 60-79% -> Proceed but flag for teacher review
IF accuracy < 60%  -> System routes to remediation BEFORE new content
```

**Standards Reference:** Every recall item displays its standard code in the review screen: `UZ-MATH-5-NATNUM-03 -- Natural sonlarni yaxlitlash`

*Source: Both specs aligned. XP values from HOMEWORK_STANDARDS.md (100 XP per correct) used over original spec (10 XP) because they better support the gamification economy.*

### 5.2 Phase 2 -- Story Mode: Concept Delivery (5-7 min standard / 10 min extended)

**Purpose:** Deliver new textbook content in an engaging narrative format. Build conceptual understanding before practice.

**UPDATED 2026-04-07 — Story Arc Mandatory.** All four AI demos produced textbook paragraphs with checkpoint questions and called it "narrative". The original spec used the word *narrative* but never defined what makes something a story vs. exposition. Story Mode now requires a complete story arc.

**Required Story Arc Structure (every Story Mode segment):**

| Beat | Requirement |
|---|---|
| **Problem** | Opens with a genuine problem or mystery that the content will solve. NOT "Today we'll learn about..." but "In 1774, a priest named Priestley heated a red powder and something impossible happened..." |
| **Struggle** | The character/scientist tries familiar approaches and they fail. The student feels the tension. |
| **Discovery** | The new concept is introduced as the missing tool that breaks the deadlock. This is where the textbook content lands. |
| **Solution** | The character applies the concept and the situation resolves. The student doesn't end a segment hanging — they get the answer, but they EARNED it by following the logic. |

**CRITICAL — Blueprint vs Output:** The four beats above (Problem → Struggle → Discovery → Solution) are a **CONSTRUCTION BLUEPRINT** — they guide how the content creator builds each story segment. The student-facing output must be a **normal, flowing story**. Do NOT insert beat labels ("Muammo:", "Kurash:", "Kashfiyot:", "Yechim:") into the text. Do NOT divide the story into labeled sections. The student reads a cohesive narrative where the beats are invisible scaffolding. If you can see the structure labels in the output, you did it wrong.

**Real-World Examples Preferred:** If the concept has a real historical discovery, real-world event, or documented case study — use that as the spine. Invented scenarios are a fallback, not the default.

**IELTS-Style Comprehension on Checkpoints:** Story Mode checkpoints test comprehension, not fact recall. Approved checkpoint question types:
- Main idea identification
- Inference ("What can we conclude from...?")
- Compare information across segments
- Identify the author's/character's purpose
- Vocabulary in context

> ✅ "Why did Priestley's experiment change chemistry?" (comprehension)
> ❌ "What is the formula of oxygen?" (fact recall — belongs in Memory Sprint)

This builds Reading PISA levels alongside subject content.

**Stranger Test (Quality Gate):** Before deployment, every Story Mode segment must pass the Stranger Test:

> *If a person who has never seen this textbook content can follow the segment and answer the checkpoint question using only the narrative logic (not prior knowledge), it passes. If it requires the reader to already know the content, it fails.*

Segments that fail the Stranger Test are returned to the content pipeline for rewrite.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 5-7 minutes | ~10 minutes |
| Segment count | 3 segments x 90 seconds | 3-5 segments x 2-3 minutes |
| Checkpoint frequency | 1-2 per segment (MUST answer to proceed) | Same |
| Source | Textbook chapter/topic -- refined into learning script | Same |
| CPA staging (Maths) | Concrete -> Pictorial -> Abstract | Same |
| AI Tier | Tier 1 (pre-generated) for content; Tier 2 for dynamic adaptation | Same |

**Content Structure Per Segment:**

```json
{
  "textbook_ref": { "chapter": "Oddiy kasrlar", "section": "Teng kasrlar", "page_range": "52-58" },
  "standard_ref": "UZ-MATH-5-FRAC-04",
  "narrative_text": "...",
  "media": [
    { "type": "image", "url": "...", "alt": "Bar model showing 2/4 = 1/2" },
    { "type": "video_clip", "url": "...", "duration": 45 }
  ],
  "cpa_stage": "pictorial",
  "checkpoint": {
    "question": "Rasmga qarang. 2/4 va 1/2 nima uchun teng?",
    "correct_answer": "Chunki ikkalasi ham yarimni bildiradi",
    "blooms_level": "understand",
    "pisa_level": 2,
    "transition_skill": "L1->L2: interpret simple visual representations",
    "explanation_on_wrong": "Bar modelga qarang -- har ikkala kasrda ham yarimga teng qism bo'yalgan..."
  }
}
```

**Rules:**
- Student CANNOT skip ahead without answering the checkpoint correctly
- On wrong checkpoint answer: show explanation referencing the textbook section, then re-ask
- Maximum 2 retries per checkpoint. After 2 failures: simplified version of the question
- Story mode tracks time-per-segment to detect disengagement (<30 seconds = flagged as skimming)

**Buzan Injection — 80/20 Keyword Tagging (Method #22):**

Every narrative segment must have its `keywords_80_20` extracted (the ~20% of words carrying ~80% of meaning). These keywords feed Phase 5 Radiant Summary branches, Flash Card fronts, and Memory Sprint items. This is a content pipeline requirement, not a student-facing feature.

*CUT — Focus Guide, Forward Momentum Rule, Semantic Chunking, and Typography optimization (Methods #16, #17, #18, #19, #20, #21, #23) are moved to a standalone "Future: Reading Fluency Module" (see end of this document). Reason: G5 students' bottleneck is COMPREHENSION, not speed. Rayner et al. (2016) found speed reading training does not improve comprehension — it teaches skimming. Pushing G5 students (Lexile 830-1010L) to read faster would actively harm understanding. Regression is a legitimate comprehension strategy, not a bad habit, at this developmental stage. These methods may be appropriate for G9+ once reading fluency is established.*

**Grade-Level Narrative Framework:**

*Source: HOMEWORK_STANDARDS.md Section 2.3. Uzbek cultural narratives.*

| Grade | Semester Narrative | Cultural Elements |
|---|---|---|
| 3 | "The Young Explorer of Samarkand" | Registan, Silk Road, traditional crafts |
| 4 | "The Silk Road Expedition" | Caravans, trade, cultural exchange |
| 5 | "The Cotton Harvest Challenge" | Agriculture, family work, rural life |
| 6 | "Building the Registan" | Architecture, mathematics in design |
| 7 | "The Amir Temur Campaign" | History, strategy, leadership |
| 8 | "Modern Tashkent" | Urban life, technology, progress |
| 9-11 | Subject-specific narratives | Professional applications |

**Subject-Specific Adaptations:**

| Subject | Story Mode Approach | Source Layer |
|---|---|---|
| Mathematics | CPA staging: manipulate objects -> draw models -> write equations | Textbook (confirmed CPA in Grade 5 Math 2024) |
| Science | Present phenomenon -> predict -> reveal results -> explain | National standards |
| Literature | Read excerpt -> contextualize author/period -> discuss themes | Textbook |
| English/Russian | Immersive content in target language with L1 support available | Textbook + PISA |
| History | Narrative with primary source excerpts -> cause/effect framing | Textbook |

**National Pride Injection — Ambient Setting Tag:** Each `narrative_segment` is tagged `setting_origin: "national" | "global"`. Rolling 55/45 balance across sessions (not per-session — a single session on Uzbek History can be 100% national). Don't force global settings on inherently Uzbek topics or national settings on inherently global ones. The balance is a yearly guideline, not a per-session mandate.

### 5.3 Phase 3 -- Game Breaks: Active Practice (6-9 min standard / 10 min extended)

**Purpose:** Apply newly learned concepts through targeted game mechanics. Each game activates a specific cognitive skill.

**UPDATED 2026-04-07:** Tic Tac Toe vs AI added as a new mechanic — see §6.4 for the full game rules. It is selectable as one of the 3 game slots in Phase 3, particularly well-suited for recall-heavy content where strategic stakes (the tic-tac-toe board) make practice feel like a duel rather than a quiz.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 6-9 minutes total | 10 minutes |
| Games per session | 3 games x 2-3 min each | 3-4 games x 2-3 min |
| Placement | Interleaved between Story Mode segments | Same |
| Game selection | Based on subject, Bloom's target, and student PISA level | Same |
| AI Tier | Tier 1 (pre-generated items) | Same |

**Game Selection Algorithm:**
```
1. GET current topic's learning objectives
2. GET student's PISA level and weakest domain areas
3. GET student's in-progress transition skills
4. SELECT 3 game mechanics from TWO POOLS:
   - Default Pool: the 16 mechanics in §6 (Tile Match, Sentence Fill, Memory Sprint,
     Spaced Flashcards, Story Mode, Adaptive Quiz, Mystery Box, Movement Breaks,
     Why Chain, Peer Teaching, Real-Life Challenge, Reflection Journal, Memory Palace,
     Final Boss, Tic Tac Toe vs AI, Notebook Capture)
   - Interactive Catalog Pool: the 12 knowledge-gated games defined in
     standards/NETS-Interactive-Game-Catalog.md (see §6.9)
   DUAL-CATALOG RULE (NEW 2026-04-07):
   - At LEAST 1 of the 3 selected games MUST come from the Interactive Catalog Pool
   - At LEAST 2 of the 3 selected games MUST come from the Default Pool
   - At least 1 selection must match the student's CURRENT Bloom's level (reinforcement)
   - At least 1 selection must be one level ABOVE (stretch)
   - At least 1 must target a current transition skill
   - Subject-appropriate mechanics only (see Game Mechanic Decision Table §6.1
     and the Subject-to-Game Compatibility Matrix in NETS-Interactive-Game-Catalog.md)
5. LOAD pre-generated game_items tagged to THIS topic's standard_ref
6. CONSTRAINT: No mechanic appears more than 2x in one session
6b. BUZAN — Cortical Diversity Constraint (SOFT RECOMMENDATION, not a hard gate):
   - Tag each selected game's cortical modality:
     Verbal/Logical (Sentence Fill, Why Chain, Adaptive Quiz, Codebreaker)
     Visual/Spatial (Tile Match, Memory Palace, Radiant Summary, Puzzle Lock, Memory Sprint)
     Kinesthetic/Motor (Notebook Capture, Movement Breaks)
     Strategic/Decision (Tic Tac Toe, Connect Four, Mystery Box)
     Productive/Generative (Peer Teaching, Reflection Journal)
   - RECOMMENDATION: At least 2 of the 3 selected games SHOULD come from DIFFERENT modalities
   - This ensures left+right brain synergy per session (Buzan's Cortical Skills principle)
   - ENFORCEMENT: This is a soft recommendation, not a production block. Sessions that naturally hit 2+ modalities (Story Mode = verbal/visual, Game Breaks = logical/spatial, Memory Palace = spatial/visual) comply automatically. A compliance check script (`scripts/check_cortical_diversity.py`) flags single-modality sessions for review but does NOT block production. Content creators should use judgment — purely mathematical chapters (e.g., algebra) may not naturally span modalities without artificial injection.
6c. BUZAN — Von Restorff Anchor:
   - The MIDDLE game (Game Break 2 of 3) is tagged as the "Von Restorff Anchor"
   - This game instance preferentially selects content items tagged "outstanding: true"
     (surprising facts, humorous framing, unusual visuals)
   - Rationale: the Sag (mid-session recall dip) is countered by an outstanding moment
7. ARRANGE interleaved with Story Mode segments
```

**Buzan also enhances individual game mechanics** — see §6.2 for per-game Buzan injections (Tile Match gets Dual Coding, Why Chain gets radiant visualization, Sentence Fill gets 80/20 keywords, etc.).

### 5.4 Phase 4 -- Real-Life Challenge: Transfer Application (3-5 min standard / 10 min extended)

**Purpose:** Force transfer -- apply textbook knowledge to a real-world scenario. This is the core skill PISA measures.

**UPDATED 2026-04-07 — First-Person Expert POV is mandatory.** All four AI demos used third-person scenarios ("Tomir's plant is dying", "Salimjon is in his garage"). Students were observers, not decision-makers. Every Real-Life Challenge must now put the student in the role of THE EXPERT who must solve a real case.

| Element | Requirement |
|---|---|
| **POV** | Direct address: "You are..." / "Your job is..." / "A client comes to you..." Never third-person. |
| **Role** | Student is positioned as a professional — project manager, analyst, engineer, consultant, business owner, researcher — NOT as a student answering a textbook question. Roles must feel modern and aspirational, not folksy or patronizing. |
| **Case** | A realistic professional scenario that could plausibly occur in a modern workplace, business, or research setting. Avoid cliché bazaar/village/folksy scenarios — students should feel like they're solving real problems, not acting in a school play. |
| **Tricky Questions** | Multiple-path questions with plausible wrong answers (distractors that look right to a novice). Forces real reasoning, not pattern matching. |
| **Explanation Required** | Student must justify their choice. AI evaluates the reasoning, not just the choice. ("What would you do AND why?") |
| **Subject Integration** | All reasoning must use concepts from the current lesson. No outside knowledge required. |

**Examples:**

> ❌ OLD (Kimyo / Combustion): *"Salimjon's garage has petrol. Should he light the stove?"*
> ✅ NEW: *"You are a fire safety inspector called to a workshop. The owner stores gasoline, uses a wood-burning stove, and keeps an asbestos fire blanket in the corner. He asks: 'Is my setup safe?' You look around and immediately spot 3 problems. What are they, and what do you tell the owner?"*

> ❌ OLD (Algebra / Linear Functions): *"A taxi charges 2000 + 1500 per km. Calculate the cost for 5 km."*
> ✅ NEW: *"You run a delivery startup. You're comparing two vehicle leasing plans for your fleet. Plan A: 2,000,000 so'm/month base + 1,500 so'm/km. Plan B: 3,000,000 so'm/month base + 1,000 so'm/km. Your drivers average 120 km/day. Which plan saves more money over a month? A partner says Plan B is always better — is that true? Show your analysis."*

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 3-5 minutes | 10 minutes |
| Scenario count | 1 scenario, 2-3 sub-questions | 1 scenario, 3-5 sub-questions |
| Context | Modern professional context — business, tech, infrastructure, research. Uzbek setting when natural, but never forced-folksy. | Same |
| AI Tier | Tier 2 (AI-generated, expert-reviewed) | Same |

**Buzan Injection — W5H Radiant Problem Solving Scaffold:**

Before the answer area opens, a 6-branch frame appears: **Who / What / Where / When / Why / How** radiating from the problem statement. The student fills at least 4 of 6 branches with brief notes (1-2 words each), forcing structured decomposition before writing. The frame stays visible as a sidebar reference while answering.

- **G5-6:** Mandatory, 4 of 6 branches minimum
- **G7-8:** Default ON, toggleable off, 5 of 6 branches
- **G9+:** Available via "Tahlil" (Analyze) button, not forced

The W5H frame itself is NOT scored — it's scaffolding. The student's final answer (which benefits from the structured thinking) is scored per the existing rubric.

*Where this does NOT apply:* Math-only Real-Life Challenges where the scenario is purely computational (e.g., "calculate the cost"). W5H works for scenarios requiring reasoning about multiple factors — Science investigations, History cause-effect, Geography resource decisions. It adds unnecessary friction to pure calculation tasks.

| Subject | W5H Scaffold Useful? | Why |
|---|---|---|
| Science | YES | Multi-factor investigations (fire safety, ecosystem analysis) |
| History | YES | Cause-effect reasoning (why did X happen?) |
| Geography | YES | Resource/location decisions with trade-offs |
| Math | SOMETIMES | Only for word problems with multiple factors, not pure calculation |
| Tarbiya | YES | Moral dilemmas have multiple stakeholders (Who matters here) |
| Tasviriy Sanat | NO | Creative challenges don't decompose into W5H |
| Language | NO | Text comprehension doesn't need spatial decomposition |

**Buzan Injection — Decision Mapping Scaffold (Method #5):**

For Real-Life Challenges that involve choosing between competing options (not single-answer problems), the W5H frame is extended with a **Decision Map**: two options radiate from the central problem, each with pro/con sub-branches. Student completes missing branches, assigns weights (1-5), selects their choice, and writes a 1-2 sentence justification.

Decision Mapping is a PROBLEM-SOLVING scaffold — it belongs here in Phase 4, not in the Boss (Phase 6). The Boss is an assessment gate that tests demonstrated competence. Adding scaffolding to assessment would inflate scores artificially.

- **Where it works:** Geography (two locations for a park — weigh cost vs access), Science (two experimental designs — weigh accuracy vs feasibility), History (two leadership strategies — weigh short vs long term), Tarbiya (moral dilemmas with competing values)
- **Where it does NOT work:** Math (has correct answers, not trade-offs), Language (grammar/comprehension doesn't involve decision trade-offs), Tasviriy Sanat (creative, not analytical)
- **Not every RLC needs it.** Only scenarios with genuine trade-offs between 2+ options. Single-answer expert scenarios (e.g., "spot the 3 fire safety problems") use W5H alone.

**National Pride Injection — "Wise Status" (30% of Phase 4 tasks):**

For approximately 1 in 3 Real-Life Challenges, the existing expert-role framing (§5.4) is enhanced with the "Wise Status" recipe:

1. **Status:** Professional title — "Bosh Muhandis," "Strategik Tahlilchi," "Laboratoriya Rahbari" — not generic praise.
2. **Arena (55/45):** National: anchor in real Uzbek achievement ("Afrosiyob tezyurar poyezdlari 250km/s aniqlikda ishlaydi"). Global: anchor in global standard ("CERN ning Katta Adron Kollayderi fizika chegaralarini kengaytirmoqda").
3. **Bridge:** Connect the textbook question to the arena. Academic core (formula, calculation, reasoning) is UNTOUCHED.
4. **Closing:** "Sizning aniqligingiz Uchinchi Renessansni quradi" (national) or "Sizning natijangiz global standartlarga mos" (global).

Source templates: `task_injections.json`. The 70% of Phase 4 tasks that don't get Wise Status play exactly as the existing spec defines — first-person expert POV, no heritage framing.

| Minimum PISA level | Level 2+ (below L2: replaced with extra Apply-level Adaptive Quiz) | Same |

**Scenario Structure:**

```json
{
  "title": "Toshkent bozorida mevalar",
  "context_narrative": "Toshkent bozorida Alisher onasiga yordam bermoqda. Ular 3/4 kg olma, 1/2 kg nok va 2/3 kg uzum sotib olishdi.",
  "textbook_refs": [
    { "standard": "UZ-MATH-5-FRAC-06", "connection": "operations with fractions" }
  ],
  "sub_questions": [
    {
      "question": "Jami necha kilogramm meva sotib olishdi?",
      "pisa_level": 3,
      "blooms": "apply",
      "pisa_process": "employ",
      "transition_skill": "L2->L3: multi-step procedure with unlike denominators",
      "correct_answer": "23/12 = 1 11/12 kg",
      "scoring_rubric": "Full marks: correct LCD + addition. Partial: correct method, arithmetic error."
    },
    {
      "question": "Agar sumkaga 2 kg sig'sa, bir sumka yetadimi? Nima uchun?",
      "pisa_level": 4,
      "blooms": "evaluate",
      "pisa_process": "interpret",
      "transition_skill": "L3->L4: interpret result in real-world context",
      "correct_answer": "Ha, yetadi. 1 11/12 < 2.",
      "scoring_rubric": "Full marks: correct comparison + reasoning. Partial: correct answer without explanation."
    }
  ]
}
```

*Source: Structure from original spec; Bazaar scenario from HOMEWORK_TASK_ENGINE.md Task 4. Cultural context confirmed by textbook analysis (Uzbek sum currency, bazaar settings, character names like Alisher, Malika, Sardor found in actual Grade 5 textbook).*

### 5.5 Phase 5 -- Consolidation / Mnemonic Lock (2-3 min standard / 5 min extended)

**Purpose.** Consolidation is the memory-science process of moving freshly-learned concepts out of fragile short-term memory into durable long-term storage. Without it, a large share of what a student encountered in Phases 2-4 decays within 24 hours (Ebbinghaus forgetting curve). Phase 5 is the engine's anti-forgetting insurance: it re-encodes the lesson's key concepts through a second channel (visual / spatial / associative) so the memory trace is stored in multiple brain pathways, not just the verbal one used in Phase 2 Story Mode.

**What Phase 5 does.** Takes the lesson's `keywords_80_20` (the ~20% of words carrying ~80% of meaning, already extracted during the Phase 2 pipeline) and locks them into long-term memory using the Buzan mnemonic technique that best fits the CONTENT STRUCTURE — not a random pick. Hierarchical content → Radiant Summary. Sequential content → Link System. Spatial content → Memory Palace. Discrete facts → Peg System. Numeric content → Major System (G7+).

**What Phase 5 is NOT.** Not assessment (that's Phase 6). Not new teaching (that's Phase 2). Not a game break (that's Phase 3). Not a transfer task (that's Phase 4). It is a low-stakes, formative, structure-imposing rehearsal.

**Agenda (student-facing flow):**

1. **Entry card** (3-5 sec): short framing — *"Endi bilganlaringizni mustahkamlaymiz."* (Now we lock in what you've learned.)
2. **Technique intro** (5-10 sec): brief explainer of the selected mnemonic technique with a worked example from the default palace (Registan Square) or grade-appropriate scene.
3. **Exercise 1** (45-75 sec): one mnemonic exercise — drag-and-drop placement, chain ordering, peg association, or mind-map branch assembly.
4. **Exercise 2** (45-75 sec): second exercise, same technique with different items OR recall test out of original order.
5. **Transition** (3-5 sec): closing line connecting to Phase 6 — *"Yaxshi! Endi Boss uchun tayyormiz."* (Good! Now we're ready for the Boss.)

**Parameters:**

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 2-3 minutes | 5 minutes |
| Number of exercises | 2 | 3 |
| Technique selection | Driven by content structure (table below) | Same |
| AI Tier | Tier 1 (pre-generated; no live-AI needed) | Same |
| Gate | **Formative — no pass/fail.** Student advances to Phase 6 after attempting both exercises. | Same |
| Score shown to student | **None.** Qualitative feedback only. | Same |
| Failure language | *"Yana bir marta"* (Once more) + reveal-then-retry option. **Never** *"Hali emas!"* — that phrase is reserved for Phase 6 boss gravity. | Same |
| Hint tax | None | None |

**Technique Selection by Grade (Buzan-Enhanced):**

| Grade Band | Available Techniques |
|---|---|
| 1-2 | Chunking, Rhymes, Songs |
| 3-4 | Memory Palace intro, Acronyms, Dual coding |
| 5-7 | Full Memory Palace (Loci), **Peg System**, **Radiant Summary**, **Link System** |
| 7-9 | All G5-7 + **Major System (phonetic digit code)**, Spaced retrieval mastery |
| 10-11 | All G7-9 + Self-directed systems, Autonomous consolidation |

**Content Structure → Technique Mapping (Phase 5 is Buzan's home phase).** The technique is selected based on the CONTENT STRUCTURE of the lesson, not randomly:

| Content Structure | Best Technique | How It Works | Example |
|---|---|---|---|
| **Hierarchical** (categories, classifications) | **Radiant Summary** | Partially completed mind map — student drags keywords onto correct branches. Follows Buzan's 7 Laws: central image, organic branches, one keyword per branch, 3+ colors. G5: max 4 branches (WM ceiling). | Kingdom Animalia: center=animal icon, branches=Invertebrates/Vertebrates, sub-branches=phyla |
| **Sequential** (processes, timelines) | **Link System** | 5 items with a vivid story chain. SMASHIN' SCOPE imagery (movement, humor, exaggeration). Recall tested out of order. | Water cycle: Bug'lanish → Kondensatsiya → Yog'ingarchilik → Oqim → Shimilish with vivid chain story |
| **Spatial** (locations, map features) | **Memory Palace** | 2.5D isometric scene, 5 hotspots, student places concepts at locations. Already fully defined — see §6 Game 5. | Silk Road cities placed at Registan Square hotspots |
| **Discrete facts** (5 key terms, dates) | **Peg System** | Number-Shape pegs (1=Candle, 2=Swan, 3=Heart, 4=Sailboat, 5=Hook — culturally adapted for Uzbekistan). Student associates each concept with a peg image, then recalls both directions. | History: 5 Silk Road facts pegged to 5 number-shapes |
| **Numbers** (dates, constants) | **Major System** (G7+ only) | Phonetic digit code: 1=T, 2=N, 3=M, 4=R... Digits convert to consonants, then to a memorable word. Example: 1441 → T-R-R-T → "Toshbaqa" (Turtle). | Navoi birth year 1441 → Turtle reading a Navoi book |

**Subject-Technique Fit:**

| Subject | Best Techniques | Rarely Useful |
|---|---|---|
| Science (Tabiy Fanlar: Biology, Physics, Chemistry, Geography, Astronomy) | Radiant Summary (classification), Link System (processes), Memory Palace (anatomy) | Major System (few numbers) |
| Math (Aniq Fanlar) | Peg System (formula names), Radiant Summary (formula families) | Link System (math isn't sequential narrative), Memory Palace (abstract) |
| History (Ijtimoiy Fanlar) | Link System (timelines), Major System (dates), Memory Palace (locations) | Radiant Summary (history is temporal, not hierarchical) |
| Geography (Tabiy Fanlar) | Memory Palace (locations on map), Radiant Summary (biome categories) | Major System, Link System |
| Tarbiya / Sanat | Radiant Summary (virtue categories) | Major System (no numbers), Memory Palace (abstract values don't map to locations well) |
| Tasviriy Sanat | Radiant Summary (art elements, color theory) | Most other mnemonics (creative subjects need making, not memorizing) |
| Language (Til Fanlari) | Peg System (vocabulary sets), Link System (grammar rule chains) | Major System, Radiant Summary |

**Interaction Model.** Every Phase 5 exercise is active, never passive reading:

- **Drag-and-drop placement** (Memory Palace, Radiant Summary)
- **Chain assembly** (Link System — student orders items, then recalls reversed)
- **Peg-to-concept pairing** (Peg System — both directions tested)
- **Word-digit conversion** (Major System — student reconstructs word from digits)

Passive viewing ("read this mnemonic") is banned. Student MUST produce the recall at least once per exercise.

**Completion Criteria.** Phase 5 is complete when the student has attempted both (Standard) or all three (Extended) exercises **once**. Correctness is not required — attempt is sufficient. The student can opt to redo any exercise using the *"Yana bir marta"* button; unlimited retries are allowed within the phase's time budget. Extension beyond time budget is not allowed (Phase 6 must still fit in session window).

**Failure / Retry Language (soft, not TEFCAS-boss).** When a student's placement is wrong:

| Situation | Student-facing message (uz) | Student-facing message (ru) |
|---|---|---|
| First attempt wrong | *"Yaqin edi — yana bir marta urinib ko'ring."* | *"Почти — попробуйте ещё раз."* |
| Second attempt wrong | *"Javobni ko'rsataymi?"* (Show the answer?) + reveal-then-retry | *"Показать ответ?"* |
| After reveal | *"Yaxshi. Keyingi mashqqa o'tamiz."* | *"Хорошо. Переходим к следующему."* |

**Never** use *"Hali emas!"*, *"Noto'g'ri"*, *"Xato"*, or any Phase-6 boss-tier language in Phase 5. Phase 5 is rehearsal, not judgment.

**SMASHIN' SCOPE Quality Gate (content-side, not student-facing).** Every mnemonic exercise authored for Phase 5 must score 6+/12 on the SMASHIN' SCOPE checklist — **S**ynaesthesia, **M**ovement, **A**ssociation, **S**ubstitution (concrete for abstract), **H**umor, **I**magination, **N**umber, **S**ymbolism, **C**olor, **O**rder, **P**ositive, **E**xaggeration. Content scoring below 6 is returned for enrichment. This is a content-pipeline QA gate — students never see the score. *(Threshold is PROVISIONAL pending pilot calibration.)*

**Buzan Review-Interval Theory.** Phase 5 is the first Buzan review touchpoint (~10 minutes after initial learning in Phase 2). Without this touchpoint, the Ebbinghaus forgetting curve begins dropping retention sharply within 20 minutes. Concepts taught verbally in Phase 2 reappear in Phase 5 through a different encoding channel (visual / spatial / associative) — this is **Dual Coding** in action. The second channel provides a backup retrieval route, dramatically improving durability.

**Nationalism Narrative Integration (Phase 5-specific rules, inherits §1.5):**

- **Default Memory Palace:** Registan Square, Samarkand. Optional student-selectable alternatives: home, school building, local bazaar, Ichan Qal'a (Khiva), Amir Temur Square (Tashkent).
- **Peg System culturally-adapted shapes:** 1=Sham (Candle), 2=Oqqush (Swan), 3=Yurak (Heart), 4=Kema (Sailboat), 5=Ilgak (Hook) — Uzbek-rooted imagery, not generic Western pegs.
- **Link System heritage-anchored sentences:** when organically relevant, the 5-item chain may include a heritage figure as a character (e.g., *"Mirzo Ulug'bek yulduzlarni sanadi..."* to open an astronomy chain). Not forced; only when the content genuinely fits.
- **20% all-task injection compliance:** per §1.5, every 5th Phase 5 task carries an explicit heritage anchor (Wise Status-lite — professional-role framing of the mnemonic scene: *"Siz Bosh Astronom Ulug'bekning shogirdisiz — yulduzlarni pegga bog'lang."*). Phases 0-A/0-B, 3, and 6 are excluded from this rotation; Phase 5 is included.
- **55/45 content balance** applies at the rolling-10 level across Phase 5 mnemonic scenes: 55% Uzbek heritage contexts (Registan, Ulugh Beg, Silk Road, Zarafshan), 45% global (generic homes, world landmarks, global science figures).

**Game Mechanic Compatibility:**

| Mechanic | Use in Phase 5 | Notes |
|---|---|---|
| Memory Palace (§6.14) | **Primary** | Spatial content. Fully specified elsewhere. |
| Peg System exercise | **Primary** | Discrete-fact content. |
| Link System chain | **Primary** | Sequential content. |
| Radiant Summary drag-fill | **Primary** | Hierarchical content. |
| Major System digit-word | **Primary (G7+)** | Numeric content. |
| Memory Match Blitz (§6.18) | **Secondary delivery vehicle** | Allowed as a game-flavored skin for Peg System exercises when 5 discrete facts need pairing practice. Counts as one Phase 5 exercise. |
| Reaction Chain (§6.19) | **Secondary delivery vehicle** | Allowed as a game-flavored skin for Link System exercises when the sequence has 5+ steps. Counts as one Phase 5 exercise. |
| Tile Match, Sentence Fill, Tic Tac Toe, Connect Four, Mystery Box, Puzzle Lock, Word Ladder, Creative Lab | **Banned in Phase 5** | These are Phase 3 Game Break mechanics. Using them here would conflict with consolidation intent. |
| Adaptive Quiz, Story Mode, Real-Life Challenge | **Banned in Phase 5** | Assessment (6), teaching (2), and transfer (4) mechanics — wrong phase. |

**Tagging Requirements (Mandatory for Deployment).** Every Phase 5 mnemonic exercise MUST carry:

- `game_mechanic: "mnemonic_exercise"`
- `buzan_technique: "memory_palace" | "peg_system" | "link_system" | "radiant_summary" | "major_system"`
- `content_structure: "hierarchical" | "sequential" | "spatial" | "discrete" | "numeric"`
- `smashin_scope_score: <integer 0-12>` (must be ≥6 for deployment)
- `heritage_anchor: <boolean>` (true if this is a 20%-injection task)
- `textbook_ref`, `standard_ref`, `pisa_ref`, `blooms_level`, `language`, `ai_tier`, `review_status`, `prerequisites` (all universal §2.5 fields)

**Edge Cases:**

- **Recovery Mode (§12.1):** when student is >7 days behind, Phase 5 collapses to *"Quick flashcard review only (1 min)"* — a single pass through the most critical `keywords_80_20` items as flashcards. Full mnemonic exercises are skipped; consolidation is done at a minimum-viable level to preserve session completion.
- **Mythical Boss / Big Boss sessions (§5.6):** Phase 5 is unchanged. These special Phase 6 variants do not alter Phase 5 structure.
- **Offline Mode (§12.6):** Phase 5 is fully offline-compatible — all mnemonic exercises are Tier 1 pre-generated content, no live AI required.
- **Extended Mode:** 3 exercises instead of 2; the third exercise is always a recall-test variant (items out of original order, or reverse-direction Peg recall).

### 5.6 Phase 6 -- Final Boss: Assessment Gate (5-10 min standard / 10-15 min extended)

**Purpose:** PISA-calibrated assessment that gates homework completion. The student MUST demonstrate competence at their target PISA level to pass.

**UPDATED 2026-04-07 — 3-Tier AI Boss System.** The Final Boss is no longer a single type. There are now three distinct AI Boss tiers, each serving a different pedagogical purpose. The remaining boss specification (HP system, damage tiers, failure flow, mastery stars) below applies to all three tiers unless explicitly overridden.

| Boss Tier | Trigger | Scope | Difficulty | Reward | Purpose |
|---|---|---|---|---|---|
| **Sub Boss** | End of every homework session (default) | Current lesson's content only | Calibrated to student's PISA level | Standard XP + stars | Assess mastery of current topic |
| **Big Boss** | Weekly (once per week per student, replaces that week's final Sub Boss) | ALL subjects passed up to current point, focusing on weakest 3 standards | One tier above student's current PISA level | **2× XP** + weekly badge + streak freeze if >80% | Spaced cross-subject retrieval, weak-point remediation |
| **Mythical Boss** | Random appearance, **<5% chance** per session — student cannot predict, force, or farm it | ALL subjects passed up to current point | PISA Level 5-6 regardless of student level — designed to overwhelm | **5× XP** + exclusive title + avatar frame + Hall of Fame entry | Elite challenge, aspiration driver, identifies top performers |

**Sub Boss** (the default — every homework session): Operates as documented in the rest of this section. HP, damage, hints, Socratic tutoring on failure all apply.

**Big Boss** (weekly):
- Auto-assigned once per week per student. Replaces that week's final Sub Boss.
- Cross-subject scope: AI identifies the student's 3 weakest standards across ALL subjects and builds the question set around them.
- Difficulty: one tier above the student's current PISA level in each subject (e.g., Math 1.7 → questions target PISA L2-3).
- Format: same as Sub Boss — open reasoning, no MC for Grade 5+, Socratic hints available (cost HP as usual).
- Reward: 2× XP, weekly leaderboard badge, streak freeze token if score > 80%.
- Failure: weak standards persist into next week's Big Boss until mastered.

**Mythical Boss** (random elite event):
- Trigger: <5% random chance per homework session. Student cannot predict, force, or farm. Appears as a surprise: *"⚠️ A Mythical Boss has appeared!"*
- Scope: ALL subjects passed up to the current point. Questions can span Math, Science, Biology, History — any completed content.
- Question type — one of two formats:
  1. **Real-World Case Scenario:** extremely complex problem requiring multi-subject reasoning. Example: *"A city's water supply is contaminated. Using chemistry (filtration), math (flow rate), and biology (bacterial growth), design a solution."*
  2. **Advanced Mathematical Challenge:** requires high-level equations, multi-step derivations, or cross-disciplinary math.
- Difficulty: PISA L5-6 regardless of student's current level. Designed to overwhelm. Most students will fail — that's by design.
- Hints: **ZERO**. No Socratic tutoring. **One attempt only**.
- Reward (if passed):
  - **5× normal session XP**
  - Exclusive title displayed on profile ("Mythical Slayer", "The Chosen One", etc.)
  - Permanent exclusive avatar frame (visually distinct)
  - Entry into "Mythical Hall of Fame" (opt-in, class-visible)
- If failed: NO penalty. Small participation XP. *"The Mythical Boss retreats... for now."*
- Psychological role: aspiration, social buzz, legend status. The rarity makes it legendary.

---

**The remainder of §5.6 (HP system, damage tiers, question schema, failure flow, mastery stars) applies to all three boss tiers below.**


| Parameter | Grades 1-4 | Grades 5-8 | Grades 9-11 |
|---|---|---|---|
| Boss HP | 50 HP | 100 HP | 150 HP |
| Question Types | Multiple choice + short answer | Short answer + open reasoning (no MC for 5+) | Open reasoning + extended response only |
| Hint Tax | -5 HP (boss regains) | -10 HP | -15 HP |
| Combo Bonus | 3 correct -> 2x next damage | Same | Same |
| Skippable | **NO. Zero exceptions.** | Same | Same |
| AI Tier | Tier 3 (premium -- Socratic tutoring on failure) | Same | Same |

**PISA-Tiered Damage System:**

*Resolution: Leonardo's gap analysis identified that Final Boss was inconsistently mapped to PISA Level 3-4 in one spec and Level 5-6 in another. The unified solution: Final Boss is tiered by difficulty, with each tier explicitly mapped to a PISA level.*

| Difficulty Tier | Damage | PISA Level | Bloom's Level | Example |
|---|---|---|---|---|
| Easy | -10 HP | Level 3 | Apply | "Calculate the total area of a combined shape" |
| Medium | -20 HP | Level 4 | Analyze | "Explain why method A gives a different result than method B" |
| Hard | -30 HP | Level 5-6 | Evaluate/Create | "Design a budget for a class trip to Samarkand using all constraints" |

**Question Distribution:**
```
Boss question set = {
  40% Easy (at or below student's CURRENT PISA level -- should get most right),
  40% Medium (at student's TARGET PISA level -- the real test),
  20% Hard (one level ABOVE target -- challenge bonus, not required to win)
}
```

**Every Boss Question MUST Include:**

```json
{
  "question_text": "Bozorda 1 kg olma narxi 15,000 so'm. Jasur 2.4 kg olma va 1.8 kg nok sotib oldi. Nok narxi olmadan 20% qimmat. Jasur qancha pul to'ladi?",
  "standard_ref": "UZ-MATH-5-FRAC-06",
  "textbook_ref": { "chapter": "Oddiy kasrlar", "section": "Kasrlar ustida amallar", "page": "83" },
  "pisa_level": 3,
  "pisa_domain": "mathematics",
  "pisa_content": "quantity",
  "pisa_process": "employ",
  "pisa_context": "personal",
  "transition_skill": "L2->L3: multi-step procedure with strategy selection",
  "blooms_level": "apply",
  "difficulty_tier": "medium",
  "correct_answer": "68,400 so'm",
  "scoring_rubric": {
    "full_marks": "Correct final answer with clear working",
    "partial_marks": "Correct method, arithmetic error -> 50% credit",
    "no_marks": "Random answer or no working shown"
  },
  "solution_steps": [
    "1. Olma narxi: 2.4 x 15,000 = 36,000 so'm",
    "2. Nok narxi per kg: 15,000 x 1.20 = 18,000 so'm",
    "3. Nok umumiy: 1.8 x 18,000 = 32,400 so'm",
    "4. Jami: 36,000 + 32,400 = 68,400 so'm"
  ],
  "socratic_hints": [
    "Avval 1 kg nok narxini toping. Olmadan 20% qimmat degani nima?",
    "Endi har bir mevaning umumiy narxini alohida hisoblang.",
    "Oxirgi qadam -- ikkala narxni qo'shing."
  ],
  "common_errors": [
    { "error": "54,000", "misconception": "Forgot to add 20% to pear price", "remediation_hint": "20% qimmat degani asosiy narxga 20% qo'shish kerak" }
  ]
}
```

**Buzan Injection — TEFCAS Failure Language (Method #10, #11):**

*All failure responses in Phase 6 use "Hali emas!" (Not yet!) — never "Wrong" or "Noto'g'ri."* The Socratic tutoring walks the student through TEFCAS: "Let's **Check** where the gap is → How would you **Adjust** your approach? → Now try again for **Success**."

*CUT — Decision Map was originally proposed here but moved to Phase 4 (Real-Life Challenge). Reason: the Boss is an assessment gate that tests demonstrated competence. Decision Mapping is a problem-solving scaffold. Adding scaffolding to assessment inflates scores. It belongs in Phase 4 where the student practices expert-role reasoning.*

**Failure Flow:**
```
IF boss NOT defeated (HP > 0 after all questions):
  1. IDENTIFY which learning objectives the student failed on
  2. MAP failures back to specific textbook sections and standards
  3. ACTIVATE Socratic Tutoring (Tier 3 AI) — TEFCAS framed:
     - "Hali emas! Miyangiz Feedback oldi." (Not yet! Your brain received Feedback.)
     - CHECK: "Keling, tekshiramiz — qayerda tushunmovchilik bor?" (Let's check — where's the gap?)
     - ADJUST: "Buni boshqacha yondashsangiz nima o'zgaradi?" (What changes if you approach this differently?)
     - AI asks guiding questions, NEVER gives answers
     - Routes student back to the SPECIFIC Story Mode segment they need
  4. REGENERATE boss questions (same standards, different numbers/context)
  5. Student re-attempts boss → SUCCESS

IF boss defeated:
  -> Proceed to Phase 7
  -> Calculate Mastery Stars
```

**Mastery Star Calculation:**

| Stars | Criteria | Unlocks |
|---|---|---|
| 1 Star | Boss defeated (any number of attempts) | Chapter complete |
| 2 Stars | Boss defeated in <=2 attempts, >50% HP remaining | Bonus avatar item |
| 3 Stars | Boss defeated on FIRST attempt with no hints used, >80% HP | Special badge progress |

### 5.7 Phase 7 -- Battle Replay: Reflection (2-3 minutes)

**Purpose:** Build metacognitive awareness. Students who reflect on their thinking improve 20-30% on subsequent assessments.

| Parameter | Value |
|---|---|
| Duration | 2-3 minutes |
| AI Tier | Tier 1 (template-based) |
| Privacy | Student-only (teacher sees summary themes only) |

**AI Prompt Generation (TEFCAS-framed):**
```
IF accuracy >= 80%:
  -> "Bugungi eng yaxshi Trial (urinish) qaysi edi? Qaysi strategiya Success ga olib keldi?"
     (What was your best Trial today? What strategy led to Success?)
IF accuracy 60-79%:
  -> "Miyangiz qanday Feedback oldi? Keyingi safar nimani Adjust qilasiz?"
     (What Feedback did your brain receive? What will you Adjust next time?)
IF accuracy < 60%:
  -> "Har bir Trial miyangizni kuchaytiryapti. Bitta kichik Adjust tanlang — nima qilasiz boshqacha?"
     (Every Trial strengthens your brain. Pick one small Adjust — what will you do differently?)

IF hesitation detected on concept X:
  -> "[X] savoli qiyin bo'ldi. Miyangiz qanday Feedback oldi?"
     ([X] question was hard. What Feedback did your brain get?)

IF streak >= 5:
  -> "[X] ta ketma-ket to'g'ri! Supernovangiz porlayapti — qaysi strategiya ishladi?"
     ([X] correct in a row! Your Supernova is glowing — what strategy worked?)
```

**Buzan Injection — Recency Effect + BOST Goal Recall:**

Phase 7 exploits the Recency Effect — the last thing in a session sticks. TEFCAS vocabulary makes the reflection feel like a deliberate learning step, not a chore.

At the end of every Phase 7, regardless of performance, resurface the BOST learning goal from Phase 0-A: *"Eslatma: Bugun siz '[stored_learning_goal]' ni bilmoqchi edingiz. Bildingizmi?"* (Remember: Today you wanted to learn '[goal]'. Did you figure it out?). Student responds: Yes / Partially / Not yet.

*Where TEFCAS language is unnecessary in Phase 7:* The performance summary data (total questions, correct, hints) stays as-is. TEFCAS framing applies only to the reflection PROMPTS, not to the raw statistics.

**National Pride Injection — Closing Line (≥60% accuracy sessions only):** After TEFCAS prompts and BOST goal recall, one closing line connects today's learning to contribution. 55/45 national/global: *"Sizning bilimingiz Uchinchi Renessansning poydevoridir"* (national) or *"Sizning aniq fikrlashingiz global standartlarga mos keladi"* (global). For sessions below 60% accuracy, skip pride framing — use TEFCAS encouragement instead ("Har bir urinish miyangizni kuchaytiryapti").

**Structure:**

```json
{
  "performance_summary": {
    "total_questions": 8,
    "correct": 6,
    "incorrect": 2,
    "hints_used": 1,
    "time_spent": "12:34",
    "hardest_question": { "standard": "UZ-MATH-5-FRAC-04", "blooms": "analyze" },
    "hesitation_points": ["question_3", "question_7"],
    "answer_changes": ["question_5"]
  },
  "reflection_prompts": [
    "Qaysi savol eng qiyin bo'ldi? Nima uchun?",
    "Keyingi safar nimani boshqacha qilgan bo'lar edingiz?",
    "Bugungi darsdan eng muhim narsa nima edi?"
  ],
  "student_writes": "...",
  "standards_mastered": ["UZ-MATH-5-FRAC-01", "UZ-MATH-5-FRAC-04"],
  "standards_needs_work": ["UZ-MATH-5-FRAC-06"]
}
```

**Response Requirements:**
- Minimum 10 characters (2 sentences for Extended Mode)
- No auto-grade (all valid responses accepted)
- Teacher dashboard shows aggregate themes, not individual entries

---

# NETS Game Mechanics — Functional Documentation
## Why Chain · Peer Teaching · Reflection Journal · Puzzle Lock

Version: 1.0 | April 2026 | For: NETS Content & Engineering Teams

---

# 1. WHY CHAIN

## What It Is
A recursive Socratic conversation. The AI asks one "Why?" question. The student answers. The AI acknowledges and asks "Why?" again — drilling one layer deeper each time — until the student reaches the mechanism, principle, or root cause behind a concept. The chain only ends at the target depth or when the 3-minute timer expires.

## How It Is Played

### Step-by-step flow
1. AI presents Level 1 question (surface observable fact)
2. Student types answer in free text
3. AI reads response, acknowledges it, asks the next deeper "Why?"
4. Student answers again
5. Repeat for 3–5 levels
6. At final level: AI confirms the student has reached the core concept and names it
7. Grade awarded based on levels completed and reasoning quality

### Chain structure

| Level | Target | AI Behaviour |
|---|---|---|
| 1 — Surface | Observable fact | Asks why the observation exists |
| 2 — Mechanism | How it actually works | Asks what enables that mechanism |
| 3 — Process | The step-by-step of the mechanism | Asks why those steps work |
| 4 — Principle | Underlying law or rule | Asks what would happen if the principle changed |
| 5+ — Synthesis | Competing explanations, edge cases | Accepts multiple valid answers |

### AI rules (hard constraints)
- NEVER give the direct answer — only probe, acknowledge, redirect
- ALWAYS acknowledge before probing: "Yaxshi boshlanish!" / "Ajoyib!" before the next Why
- ALWAYS reference specific textbook pages if the student is stuck: "Sahifa 7ga qarang"
- When student answer is wrong: do not say "wrong" — ask a redirecting question instead
- When student answer is partially right: build on the correct part, probe the gap

### Parameters
- Timer: 3 minutes
- Minimum chain depth: 3 levels (configurable per topic)
- Grade: Type B (Rubric-Based) — Chain depth (% of levels reached) + Reasoning quality (% of levels with substantive answers). See GRADING-SYSTEM.md.
- AI Tier: 2 (live generative — most expensive Phase 3 mechanic)
- Input: free text (typed), minimum 3 characters per response

### PISA scaling

| PISA Level | Chain depth | Scaffolding style |
|---|---|---|
| L2–3 | 2–3 levels | Guided — AI suggests which direction to think |
| L3–4 | 4 levels | Moderate — AI waits longer before nudging |
| L5–6 | 5+ levels | Open — competing explanations accepted, no single right answer |

## Subject Implementations

### Natural Sciences — Photosynthesis
- L1: "Why do plants need sunlight?"
- L2: "Why does light give them energy specifically?"
- L3: "What do plants do with that energy — step by step?"
- L4: "Why can plants make food from CO₂ and water but animals can't?"
- L5+: "What would happen to life on Earth if the sun emitted only infrared light?"

### Natural Sciences — Ecosystems
- L1: "Why do ecosystems need both predators and prey?"
- L2: "What happens to plant populations if all wolves disappear?"
- L3: "Why does removing one species cause a cascade across the whole ecosystem?"
- L4: "What is the underlying principle that keeps ecosystems in balance?"

### Social Sciences / History — Silk Road
- L1: "Why did traders use the Silk Road instead of sea routes?"
- L2: "Why did cities like Samarkand grow specifically along the route?"
- L3: "Why did cultural exchange happen alongside trade — why didn't merchants just trade and leave?"
- L4: "What is the underlying principle that causes trade routes to produce cultural change?"

### Social Sciences / History — Cause of World War I
- L1: "Why did Franz Ferdinand's assassination start a world war?"
- L2: "Why did one assassination trigger so many countries to fight?"
- L3: "Why did the alliance system make the war spread rather than stay contained?"
- L4: "What structural conditions made WWI inevitable regardless of the assassination?"

### Exact Sciences — Gravity (Physics, G7+)
- L1: "Why do objects fall to the ground?"
- L2: "Why does mass cause attraction — what is gravity actually doing?"
- L3: "Why does the Moon not fall to Earth even though gravity pulls it?"
- L4: "Why does the same force that keeps the Moon in orbit also cause tides?"

### Reading / Literature
- L1: "Why did the main character lie to his father?"
- L2: "Why did he feel he had no other choice?"
- L3: "Why did the author make him feel trapped — what does this tell us about the theme?"
- L4: "Why do stories need characters who make bad choices?"

## Subject Restrictions

| Subject Family | Status | Depth cap |
|---|---|---|
| Natural Sciences | Primary mechanic | 5 levels |
| Social Sciences / History | Primary mechanic — intro chapters excluded | 3 levels |
| Reading / Literature | Secondary mechanic | 4 levels |
| Exact Sciences | Secondary, G6+ only | 2 levels G5, 3 levels G6+ |
| Language Sciences | Rarely used | 2 levels max |
| Arts / Tarbiya | Not recommended | — |

**History restriction:** Do not use Why Chain in introductory/Chapter 1 lessons. Students lack the prior knowledge base to sustain causal reasoning. Reserve for middle and later chapters of any unit.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 or 3 (Stretch or Transition Skill slot)**

```
Game Break 1 — Reinforcement (at current level)
    ↓
→ WHY CHAIN — Stretch (one level above current) ←
    ↓
Game Break 3 — Transition skill target
```

**Why this position:**
- Why Chain targets Bloom's Analyze — requires the student to have first encountered the content in Story Mode
- Should never be the first Game Break (student hasn't absorbed content yet)
- Works best as the "stretch" mechanic — after reinforcement builds confidence, the chain pushes deeper
- Not suitable as the final game before the Boss — the open-ended nature doesn't give the tight recall consolidation the Boss requires

---

# 3. PEER TEACHING

## What It Is
The student becomes the teacher. They are given a scenario involving a fictional younger student or confused classmate and must explain, help, or correct — in writing. The AI evaluates whether the explanation is complete, clear, and factually correct.

It is the only mechanic in the catalog where the student produces knowledge for someone else rather than retrieving it for themselves.

## How It Is Played

### Step-by-step flow
1. Scenario card appears with fictional student name and situation
2. Student reads the scenario and selects scenario type (A / B / C) — or AI pre-selects
3. Large text area opens for the student's explanation
4. Student writes their explanation (no word limit, no minimum displayed)
5. "Yuborish" (Submit) button
6. AI evaluates against rubric in real time (Tier 1 or Tier 2 depending on subject)
7. Score breakdown shown: Completeness / Clarity / Accuracy
8. If inaccurate: flagged for teacher review (not auto-failed)
9. Grade awarded based on rubric dimensions

### Three scenario types

| Type | Demand | Best for |
|---|---|---|
| **A — Explain from scratch** | Build understanding in someone with zero prior knowledge | Bloom's Understand |
| **B — Help someone stuck** | Diagnose confusion and re-explain with a different approach | Bloom's Apply |
| **C — Correct a wrong answer** | Identify the exact error and explain the correct path | Bloom's Evaluate |

### Scoring rubric

Grade: Type B (Rubric-Based) — Three dimensions tracked as percentages: Completeness (%), Clarity (%), Accuracy (%). Composite accuracy feeds the learning curve.

| Criterion | What AI checks |
|---|---|
| Completeness | All key concepts present — no critical gaps |
| Clarity | Language appropriate for the fictional audience |
| Accuracy | Factually correct against textbook content |

### AI evaluation behaviour
- Tier 1: keyword matching + logical flow check (Exact Sciences, straightforward topics)
- Tier 2: semantic evaluation (History, Literature, open-ended explanations)
- Flags for teacher review if factually inaccurate — does NOT auto-fail
- Never reveals the "correct" explanation to the student before they submit

### Availability
- Grades 5–11 only (below G5: developmental readiness insufficient for formulating explanations)
- All subject families (no subject restriction)

## Subject Implementations

### Exact Sciences
- A: "Explain to a Grade 4 student what a negative number means using a real example from daily life"
- A: "Explain why we can't divide by zero — use a story or example, not a definition"
- B: "Sardor keeps getting the wrong answer when multiplying fractions. Walk him through the correct method step by step"
- B: "Malika calculated speed as distance × time and got 240 km/h. She doesn't understand why this is wrong. Help her"
- C: "A student said 1/2 + 1/3 = 2/5. Explain exactly what error they made and what the correct answer is"
- C: "A student wrote: speed = distance + time. What is wrong and why?"

### Natural Sciences
- A: "Explain photosynthesis to a Grade 4 student without using the word 'photosynthesis'"
- A: "Explain why we have seasons — your classmate thinks it's because Earth gets closer to the Sun in summer"
- B: "Rustam drew his food chain as: Wolf → Rabbit → Grass. His teacher marked it wrong. He's confused. Help him"
- B: "Feruza thinks veins always carry deoxygenated blood. She found a website that says the same thing. Help her understand the full picture"
- C: "A student said 'arteries always carry oxygenated blood.' The teacher marked it wrong. Explain why"
- C: "A student said 'deserts are always hot.' Give three specific pieces of evidence that prove this wrong"

### Language Sciences
- A: "Explain the difference between past simple and past perfect to a student who has never heard of verb tenses"
- A: "Explain what a syllable is — use 5 words from today's lesson as examples"
- B: "Dilnoza keeps putting adjectives after nouns in English (e.g. 'a car red'). She can't understand why this is wrong. Help her"
- C: "A student wrote: 'Yesterday I go to school and buyed some food.' Identify and explain every error"

### Social Sciences / History
- A: "Explain to a Grade 4 student what a primary source is — give two examples from Uzbek history"
- B: "Temur thinks the Mongol invasion was purely destructive. He can't understand how the Timurid Renaissance happened so soon after. Help him"
- C: "A student answered: 'The Silk Road was only an economic phenomenon — it was just about trade.' The teacher gave 2/5. Explain what the answer is missing"

### Arts / Tarbiya
- A: "Explain what respect means in practice — give 3 specific examples, not a dictionary definition"
- C: "A student said 'being cooperative means always agreeing with the team.' Explain what is incomplete about this"

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 or 3 (Evaluate/Create slot)**

```
Game Break 1 — Reinforcement (Apply)
    ↓
Story Segment 2
    ↓
→ PEER TEACHING — Stretch (Evaluate) ←
    ↓
Story Segment 3 → Real-Life Challenge
```

**Why this position:**
- Peer Teaching requires the student to have absorbed content (cannot explain what they haven't encountered)
- Should come after at least one Story Segment and one reinforcement Game Break
- Naturally feeds into the Real-Life Challenge (Phase 4) — both require applying knowledge to an external context
- Not suitable as the final mechanic before the Boss — the open production format doesn't give tight consolidation

**Not recommended:**
- As the first Game Break (student hasn't encountered content yet)
- In Recovery Sessions (cognitive overhead too high for struggling students)
- For students below PISA L2 (scaffolding insufficient — use Adaptive Quiz instead)

---

# 4. REFLECTION JOURNAL

## What It Is
The metacognitive closure mechanic. After the Boss Fight and Remediation, the student is shown a prompt that asks them to look back at what happened in the session — what they understood, what confused them, and what they would do differently. They write a short response. No grading. No wrong answers.

It completes the TEFCAS loop: Trial → Event → Feedback → Check → Adjust → **Success** — the Reflection Journal is the conscious "Adjust" step, making the brain's natural error-correction process explicit.

## How It Is Played

### Step-by-step flow
1. Reflection prompt appears (AI-generated based on performance pattern)
2. Student reads the prompt
3. Text area opens — minimum 10 characters required (2 sentences in Extended Mode)
4. Student writes response — no time limit, no AI evaluation of content
5. "Tugatdim" (Finish) button
6. Response stored privately — student-only. Teacher sees themes only, not individual text.
7. Session closure screen

### Prompt types (AI selects based on performance)

| Performance pattern | Prompt type | Example |
|---|---|---|
| Strong session (2–3 stars) | Depth probe | "You understood today's topic well. What is the one thing that would help you explain it to a younger student?" |
| Weak session (0–1 star) | Growth frame | "You found today's topic difficult. Name one specific thing that confused you. What question would you ask the teacher?" |
| Inconsistent (good game breaks, poor boss) | Gap identification | "You did well on the practice games but struggled on the Boss. What was different about the Boss questions?" |
| First time on topic | Curiosity hook | "You just learned about [topic] for the first time. What surprised you most? What do you still want to know?" |
| Returning after failure | Re-engagement | "Last time you struggled with [standard]. Today you tried again. What felt different this time?" |

### Parameters
- No timer — student-paced
- No minimum quality threshold — any 10+ character response accepted
- No AI evaluation of content
- Privacy: content visible to student only. Teacher dashboard shows aggregate themes (e.g. "12 students mentioned confusion about denominators") — never individual entries
- Grade: Type D (Participation-Based) — No accuracy grade. Recorded as 'completed' or 'skipped.' No penalty for skipping.
- AI Tier: 1 for prompt generation (pre-pattern matching, not generative)

## Subject Implementations

### Exact Sciences
- After strong session: "Today you worked with fractions. Write one real situation from your life where you would need to add fractions"
- After weak session: "Which step in today's problem confused you the most? Draw it out in your mind and describe where you got lost"
- After inconsistent session: "You got the practice problems right but struggled on the Boss. What was different about the Boss question?"

### Natural Sciences
- After strong session: "You understood photosynthesis today. Describe it as if you were explaining it to a plant"
- After weak session: "Which part of the cell cycle confused you? What would help it make more sense?"
- Curiosity hook: "You just learned about the human immune system. What is one thing about it that surprised you?"

### Language Sciences
- After strong session: "You learned 8 new vocabulary words today. Which one will you actually use this week, and where?"
- After weak session: "Which grammar rule from today still feels unclear? Write it out in your own words — even if you're not sure it's right"

### Social Sciences / History
- After strong session: "Today you studied [historical event]. What would you have done differently if you were the decision-maker at the time?"
- After weak session: "What is one question about today's topic that the textbook didn't answer for you?"
- Curiosity hook: "You just learned about the Silk Road. What one thing about it do you want to know more about?"

### Arts / Tarbiya
- After any session: "What is one thing you did today that you feel proud of — inside or outside of your homework?"
- Character prompt: "You studied [character value] today. Describe one moment this week when you saw that value in real life — or when you wished you had shown it"

## Where It Fits in the Homework

**Position: Phase 8 — After Remediation, before Session Closure**

```
Phase 6 — Boss Fight
    ↓
Phase 7 — AI Analysis (server-side, invisible)
    ↓
Phase 8a — Remediation (targeted micro-exercises)
    ↓
→ REFLECTION JOURNAL ←
    ↓
Session Closure
```

**Why this position:**
- Must come after all assessment is complete — the student needs to know how they performed before they can reflect on it
- Must come before the reward sequence — the emotional closure of writing grounds the dopamine hit of the reward chest
- Cannot be moved earlier — reflecting before the Boss Fight creates test anxiety (student is thinking about what they got wrong, not fighting the Boss)

**Skippable:** Yes — Type D (Participation-Based). If the student taps "Skip" the session closes normally. Recorded as 'skipped' rather than 'completed.'

---

# 5. PUZZLE LOCK (SLIDING TILE)

## What It Is
A classic sliding tile puzzle (15-puzzle / 8-puzzle) where the ability to move tiles is gated by knowledge questions. Correct answer → student chooses which tile to slide. Wrong answer → a random adjacent tile slides automatically, potentially making the puzzle harder. The student must reach the solved state (tiles in correct order) before the timer expires.

## How It Is Played

### Step-by-step flow
1. Scrambled tile grid appears (3×3 = 8 tiles + 1 empty, or 4×4 = 15 tiles + 1 empty)
2. Student taps a tile adjacent to the empty space to attempt a move
3. Question modal appears immediately
4. Student answers the question
5. **Correct answer:** chosen tile slides into the empty space (student's intended move)
6. **Wrong answer:** a random valid adjacent tile slides instead (not necessarily the student's choice)
7. Repeat until solved or timer expires
8. Solved = all tiles in correct order → celebration
9. Time expired without solving = partial credit based on progress

### Tile content options
The tiles can contain:
- **Numbers** (default — solve the classic 1-2-3...8 order)
- **Vocabulary words** (arrange in alphabetical or grammatical order)
- **Historical events** (arrange in chronological order)
- **Equation steps** (arrange in logical solution order)
- **Sentence fragments** (arrange into a grammatically correct sentence)
- **Classification categories** (arrange organisms from simple to complex)

### Parameters
- Grid sizes: 3×3 (G1–6), 4×4 (G7+)
- Timer: 3 minutes (3×3), 5 minutes (4×4)
- Grade: Type A (Accuracy-Based) + Efficiency — Correct answers / total attempts = accuracy level. Fewer wrong answers = higher efficiency score.
- Questions: one per attempted move (not per wrong answer)
- AI Tier: 1 (pre-generated questions, rule-based evaluation)

### Wrong answer penalty psychology
The random tile slide creates a "punishment" that is strategic, not punitive — the puzzle becomes harder, but the student can still win. This is the same psychology as the Minefield Navigator: consequences are real but not catastrophic. The student is motivated to answer correctly to maintain control of their strategy.

## Subject Implementations

### Exact Sciences
- **Number tiles:** Arrange steps of long division in correct order
- **Equation tiles:** Arrange steps of solving 2x + 5 = 13 in sequence
- **Formula tiles:** Arrange: "Speed = Distance ÷ Time" — tiles show Speed / = / Distance / ÷ / Time scrambled
- Questions asked: arithmetic, formula recall, unit conversion

### Natural Sciences
- **Classification tiles:** Arrange taxonomy levels from broadest to narrowest: Kingdom → Phylum → Class → Order → Family → Genus → Species
- **Process tiles:** Arrange the stages of mitosis in order: Interphase → Prophase → Metaphase → Anaphase → Telophase
- **Food chain tiles:** Arrange organisms from producer to apex predator
- Questions asked: organism identification, process step functions, habitat facts

### Language Sciences
- **Sentence tiles:** Arrange scrambled words into correct grammatical order
- **Alphabet tiles:** Arrange vocabulary words in alphabetical order
- **Story tiles:** Arrange 8 sentence fragments to reconstruct a paragraph in logical order
- Questions asked: vocabulary definitions, grammar rules, spelling

### Social Sciences / History
- **Timeline tiles:** Arrange historical events in chronological order (dates on each tile)
- **Cause-effect tiles:** Arrange events from root cause to final consequence
- **Map tiles:** Arrange regions of Central Asia (image puzzle — tiles form a map)
- Questions asked: dates, key figures, event significance

### Arts / Tarbiya
- **Sequence tiles:** Arrange steps of a creative process (sketch → draft → refine → final)
- **Value tiles:** Arrange character values from most personal to most social
- Questions asked: vocabulary, creative concepts, reflection questions

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement slot)**

```
Story Segment 1 → Checkpoint 1
    ↓
Movement Break
    ↓
→ PUZZLE LOCK — Game Break 1 (Reinforcement) ←
```

**Also suitable:**
- Game Break 2 (Apply/Analyze) when using content-ordered tiles (timeline, classification sequence)
- Phase 5 Consolidation alternative to Memory Palace when the lesson involves a sequential process

**Why this position:**
- Puzzle Lock is a medium-overhead mechanic — visual/spatial, immediately engaging, lower cognitive demand than Why Chain
- Excellent as the first Game Break because it re-engages spatial reasoning after the narrative focus of Story Mode
- The "arrange in order" tile formats reinforce the structural understanding introduced in Story Mode without requiring the student to generate new knowledge

**Not recommended:**
- As the only Game Break in a session (needs to be complemented by a more evaluative mechanic)
- For abstract, non-sequential content that doesn't lend itself to ordering (use Tile Match instead)

---

# 6. TILE MATCH

## What It Is
A card-flipping memory-and-knowledge mechanic. The board contains face-down paired cards. The student flips two cards to attempt a match — but only gets to keep the match if they answer a subject question correctly. Wrong answer and the matched pair flips back.

## How It Is Played

### Step-by-step flow
1. 4×4 grid of face-down cards (8 pairs) appears
2. Student taps first card — it flips to reveal content
3. Student taps second card — it flips
4. If the two cards are a pair: question modal appears
5. **Correct answer:** both cards lock face-up (matched)
6. **Wrong answer:** both cards flip back face-down (pair lost)
7. If the two cards are not a pair: both flip back automatically (no question)
8. Repeat until all 8 pairs are matched
9. XP awarded based on total attempts needed

### Parameters
- Grid: 4×4 (8 pairs), all subjects
- XP: ≤8 attempts = 300 XP | ≤12 = 200 XP | 13+ = 100 XP
- Tile content: term/definition pairs, concept/example pairs, word/translation pairs
- No timer (concentration mechanic — student-paced)
- AI Tier: 1 (pre-generated questions)

### Wrong answer psychology
Unlike Puzzle Lock where wrong answers cause random moves, Tile Match wrong answers cause the pair to disappear from view again — requiring the student to relocate it spatially. This is a double penalty: knowledge penalty AND memory penalty.

## Subject Implementations

### Exact Sciences
- Pairs: formula ↔ name (e.g. "E = mc²" ↔ "Mass-Energiya tenglamasi")
- Pairs: number ↔ square root (e.g. "64" ↔ "8")

### Natural Sciences
- Pairs: organism ↔ classification (e.g. "Ko'rshapalak" ↔ "Sutemizuvchi")
- Pairs: organ ↔ function (e.g. "O'pka" ↔ "Nafas olish")

### Language Sciences
- Pairs: word ↔ translation or synonym
- Pairs: verb ↔ past tense form

### Social Sciences / History
- Pairs: event ↔ year (e.g. "O'zbekiston mustaqilligi" ↔ "1991")
- Pairs: figure ↔ achievement

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement)**

```
Story Segment 1 → Checkpoint 1
    ↓
Movement Break
    ↓
→ TILE MATCH — Game Break 1 (Reinforcement) ←
```

**Why this position:**
- Medium spatial + knowledge demand — ideal warm-up game break
- Reinforces vocabulary and paired concepts introduced in Story Mode
- Self-paced nature suits post-Movement Break state (students settle back in)

**Not recommended:**
- As a timed mechanic (defeats the concentration purpose)
- For abstract/procedural content that doesn't pair naturally

---

# 8. SPACED FLASHCARDS

## What It Is
A digital implementation of the spaced repetition method. The student is shown a card front (question/term), thinks privately, reveals the back (answer), then rates their confidence on a 4-point scale. Cards rated "Again" return to the queue; cards rated "Easy" exit the session. The mechanic simulates the Leitner box system without physical cards.

## How It Is Played

### Step-by-step flow
1. Card front shown: question or term
2. Student thinks (no timer — deliberate recall is the goal)
3. "Show Answer" button tapped → card flips to reveal back
4. Student self-assesses and taps one of four rating buttons:
   - **Again (Qayta):** did not recall — card returns to queue end (0 XP)
   - **Hard (Qiyin):** recalled with difficulty (+20 XP)
   - **Good (Yaxshi):** recalled correctly (+50 XP)
   - **Easy (Oson):** recalled instantly (+80 XP)
5. Next card loads from queue
6. Session ends when no "Again" cards remain
7. Session summary shown: Easy/Good/Again counts + total XP

### Parameters
- Cards per session: 8 (expandable)
- No time limit — student-paced throughout
- "Again" cards recycle to end of queue (not discarded)
- XP: 0 / 20 / 50 / 80 per card depending on rating
- AI Tier: 0 (no AI — pure self-assessment)
- Privacy: ratings stored for teacher analytics; content is not evaluated

### Spaced repetition logic
"Again" cards always re-appear before session end. "Hard" and "Good" cards exit the current session but return in future sessions at shorter intervals. "Easy" cards return at longer intervals. This mirrors the Leitner system and Ebbinghaus forgetting curve.

## Subject Implementations

### All subjects
The mechanic is subject-agnostic. Card fronts and backs are populated from the lesson's vocabulary and concept list:
- **Exact Sciences:** formula ↔ name, term ↔ definition
- **Natural Sciences:** organism ↔ classification, process ↔ steps
- **Language Sciences:** word ↔ translation, irregular verb ↔ past tense
- **History:** event ↔ date, figure ↔ role
- **Arts/Tarbiya:** value ↔ behavioural example

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

```
Session opens
    ↓
→ SPACED FLASHCARDS — Memory Hook ←
    ↓
Story Segment 1
```

**Why this position:**
- Activates prior knowledge before new content is introduced
- Sets retrieval context — Ebbinghaus shows recall before re-exposure strengthens retention
- Low-stakes (no wrong answer, just self-rating) — appropriate for session opening

**Also suitable:**
- Phase 5 Consolidation — reviewing lesson vocabulary after all content is covered
- Recovery sessions — low cognitive overhead, no time pressure

---

# 9. MEMORY SPRINT

## What It Is
A two-phase rapid-fire memory mechanic. Phase 1 (Study): 6 items are displayed simultaneously for exactly 5 seconds. Phase 2 (Recall): items are hidden and the student answers 6 questions about them under a 30-second timer. The faster the student answers, the more of the timer remains. The mechanic exploits the Primacy/Recency recall curve by forcing active retrieval immediately after study.

## How It Is Played

### Step-by-step flow
**Phase 1 — Study (5 seconds):**
1. 6 items appear in a 3×2 grid — each item has an emoji + label
2. A visible countdown runs from 5 to 0
3. At 0, all items disappear simultaneously

**Phase 2 — Recall (30 seconds):**
4. Question 1 of 6 appears — 4-option multiple choice
5. Student answers
6. Immediate feedback (correct/wrong) + next question loads
7. Timer keeps counting — questions can be answered at any speed
8. Session ends when all 6 questions answered or timer hits 0
9. XP awarded per correct answer

### Parameters
- Study duration: 5 seconds (fixed — not adjustable)
- Recall timer: 30 seconds
- Items: 6 per round
- XP: +50 per correct answer (300 XP max)
- AI Tier: 1 (pre-generated item/question sets)
- No partial credit — correct or wrong only

### Cognitive design
The 5-second study window is short enough to require genuine attention (students cannot read slowly — they must scan and encode visually). The immediate recall phase exploits the working memory window before items decay. This is distinct from Spaced Flashcards (which tests long-term memory) — Memory Sprint tests working memory and initial encoding.

## Subject Implementations

### Exact Sciences
- Items: formulas, geometric shapes, number sequences
- Questions: "Which formula appeared?", "What was the value shown?"

### Natural Sciences
- Items: organisms, organs, ecosystem elements
- Questions: "Which organism was NOT shown?", "What was the 3rd item?"

### Language Sciences
- Items: vocabulary words in target language
- Questions: translation recall, spelling recall

### History
- Items: key figures, dates, places
- Questions: "Which year was shown?", "Which figure appeared?"

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

```
Session opens
    ↓
→ MEMORY SPRINT — Memory Hook ←
    ↓
Story Segment 1
```

**Why this position:**
- Pre-loads relevant items into working memory before Story Mode introduces them formally
- Creates a "familiar" feeling when items reappear in Story Mode (recognition advantage)
- 35-second total duration — minimal time cost at session start

**Not recommended:**
- As a Game Break (too short and cognitively light for mid-session use)
- G1–2 (reading speed and working memory capacity insufficient for 5-second study window)

---

# 10. SENTENCE FILL (CLOZE TEST)

## What It Is
A structured gap-fill mechanic. The student is shown a sentence with one or more words missing (replaced by a blank). They select the correct word from 4 options. Unlike free-text input, the multiple-choice format ensures accessibility across grade levels and enables AI Tier 1 evaluation. The mechanic targets Bloom's Understand — testing whether the student can use context to identify the correct concept.

## How It Is Played

### Step-by-step flow
1. Sentence with blank(s) appears on screen
2. Subject tag shown (e.g. "🌿 Tabiiy Fanlar")
3. Optional hint shown below sentence
4. Student selects one of 4 options
5. **Correct:** blank fills with the word in green; +50 XP
6. **Wrong:** blank fills with student's wrong choice in red; correct answer highlighted green
7. Next sentence loads after 1.2 seconds
8. 6 sentences per session; session summary at end

### Parameters
- Questions per session: 6
- Options per question: 4
- XP: +50 per correct answer; +100 bonus if zero wrong answers
- Timer: none (student-paced)
- AI Tier: 1 (pre-generated sentences with controlled vocabulary)
- Subjects: all families

### Difficulty scaling

| Level | Blank type | Example |
|---|---|---|
| L1–2 | Single content word | "O'simliklar _____ yordamida oziq tayyorlaydi" |
| L3–4 | Technical term | "Atom tarkibida _____ va elektronlar bor" |
| L5+ | Multi-blank or clause | "_____ jarayonida CO₂ _____ ga aylanadi" |

## Subject Implementations

### Exact Sciences
- "Uchburchak barcha burchaklari yig'indisi _____ teng." → 180°
- "Tezlik = _____ ÷ Vaqt" → Masofa

### Natural Sciences
- "O'simliklar _____ va suv yordamida oziq-ovqat tayyorlaydi." → yorug'lik
- "Inson qoni _____ orqali tanaga kislorod yetkazadi." → gemoglobin

### Language Sciences
- Fill-in-the-blank grammar: "Yesterday I _____ to school." → went
- Vocabulary: "The opposite of 'hot' is _____." → cold

### History
- "Ipak Yo'li _____ dan Yevropagacha cho'zilgan." → Xitoy

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 or 2 (Reinforce/Apply)**

**Why this position:**
- Tests Bloom's Understand — verifies comprehension of Story Mode content
- Low UI friction (tap to answer) — suitable for both Game Break 1 and 2
- Works well as a "cooldown" game break between more complex mechanics

**Not recommended:**
- As the only mechanic in a session (pair with higher-order mechanic)
- For open-ended creative or evaluative content (use Peer Teaching instead)

---

# 11. TIC TAC TOE

## What It Is
Classic 3×3 Tic Tac Toe with knowledge gating. The student plays X, the AI plays O. Before each X placement, the student must answer a subject question. Correct answer → X placed on chosen cell. Wrong answer → AI immediately places O on a random empty cell (player's intended X does not appear). The student must get 3 X's in a row before the AI does.

## How It Is Played

### Step-by-step flow
1. Empty 3×3 board appears
2. Student taps any empty cell
3. Question modal appears
4. **Correct answer:** X placed on chosen cell
5. **Wrong answer:** AI places O on a random cell (not the student's chosen cell)
6. Check for win/loss/draw after each move
7. AI does NOT answer questions — AI moves happen automatically after wrong answers only
8. Game ends on 3-in-a-row for either player, or board full (draw)
9. Score tracked across multiple games in session

### Parameters
- Board: 3×3 standard
- Win condition: 3 in a row (horizontal, vertical, diagonal)
- XP: Win = 200 XP | Draw = 100 XP | Loss = 50 XP; +30 XP per correct answer regardless of outcome
- AI strategy: random empty cell (not minimax — keeps game winnable)
- Questions: 1 per student move attempt
- AI Tier: 1

### Game psychology
The AI randomness means the student can win even after wrong answers — the game is never unwinnable. Wrong answers increase risk (AI gets free moves) without guaranteeing loss. This maintains engagement without frustration.

## Subject Implementations

### All subjects
Questions are drawn from the current lesson's concept pool. The game board is thematically neutral — the knowledge gate is the only subject-specific element.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply)**

**Why this position:**
- Familiar format requires zero explanation — cognitive load is minimal
- Strategic element (cell placement) adds a layer above pure Q&A
- Short game duration (3–9 moves) fits the 2–3 minute Game Break window

**Not recommended:**
- As the first Game Break (needs student to be settled — the competitive element can create anxiety early in session)
- Recovery sessions (competitive framing not appropriate)

---

# 12. CONNECT FOUR

## What It Is
Classic 7×6 Connect Four with knowledge gating. The student plays yellow discs, the AI plays red. The student selects a column and must answer a question before their disc drops. Correct answer → yellow disc drops into chosen column. Wrong answer → AI drops a red disc into a random column. First to connect 4 in a row (horizontal, vertical, or diagonal) wins.

## How It Is Played

### Step-by-step flow
1. 7×6 empty grid appears with column arrow buttons at top
2. Student taps a column arrow
3. Question modal appears
4. **Correct answer:** yellow disc drops into chosen column (bottom-most empty row)
5. **Wrong answer:** AI drops red disc into a random valid column
6. After correct student move: AI automatically plays one move
7. Win check after every disc placement
8. Game ends on 4-in-a-row or board full (draw)

### Parameters
- Grid: 7 columns × 6 rows (standard)
- Win condition: 4 consecutive discs in any direction
- XP: Win = 200 XP | Draw = 80 XP | Loss = 50 XP; +30 XP per correct answer
- AI: random valid column (not strategic — keeps game learnable)
- Questions: 1 per student move attempt
- AI Tier: 1

### Depth vs Tic Tac Toe
Connect Four has 4,531,985,219,092 possible game states vs Tic Tac Toe's 255,168. The longer game duration (average 36 moves) makes it more suitable for a full Game Break slot. The vertical/diagonal win conditions add genuine strategic thinking beyond simple Q&A.

## Subject Implementations

### All subjects
Questions drawn from lesson concept pool. The board itself is thematically neutral.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply/Analyze)**

**Why this position:**
- Longer game = more questions answered per session
- Spatial strategy element engages different cognitive resources than pure recall
- Higher replay motivation than Tic Tac Toe (more varied outcomes)

**Not recommended:**
- Game Break 1 (too complex for a first Game Break — student needs to be warmed up)
- G1–3 (Connect Four strategy requires abstract spatial planning)

---


# 14. MEMORY PALACE

## What It Is
A digital implementation of the Method of Loci (memory palace technique). A virtual room is divided into 6 named zones (e.g. Entrance, Window, Wall, Desk, Chair, Bookshelf). Each zone is assigned a knowledge item (emoji + label). The student studies the zone-item assignments, then the items are hidden and the student must tap the correct zone for each item presented.

## How It Is Played

### Step-by-step flow
**Phase 1 — Study (10 seconds):**
1. Room grid appears with all 6 items visible in their zones
2. Countdown timer from 10 to 0
3. At 0, items disappear

**Phase 2 — Recall:**
4. One item is presented at a time (emoji + name): "Where was this?"
5. Student taps the zone they believe the item was placed in
6. **Correct:** zone highlights green
7. **Wrong:** chosen zone highlights red; correct zone highlights green
8. Next item presented until all 6 recalled
9. XP awarded per correct recall

### Parameters
- Zones: 6 (named locations in a room)
- Study duration: 10 seconds
- Recall: untimed (self-paced)
- XP: +50 per correct zone; bonus for perfect recall
- AI Tier: 0 (no AI evaluation — correct answer is deterministic zone matching)

### Pedagogical basis
The Method of Loci exploits the brain's strong spatial memory by anchoring abstract content to familiar physical locations. Research (Bower, 1970; Yates, 1966) shows 2–3× better recall for loci-encoded material vs rote memorisation. In this mechanic, the "palace" is always the same room — familiarity with the palace grows over repeated sessions.

## Subject Implementations

### All subjects
The zone-item assignments are generated from the lesson's key concept list:
- **Natural Sciences:** photosynthesis steps → room zones
- **History:** Silk Road cities → room zones
- **Exact Sciences:** formula components → room zones
- **Language Sciences:** vocabulary clusters → room zones

## Where It Fits in the Homework

**Primary position: Phase 5 — Mustahkamlash (Consolidation)**

**Also suitable:**
- As alternative to Codebreaker in consolidation slot (when content is list-based rather than vocabulary-based)

**Why this position:**
- Consolidation requires organising disparate items into a coherent structure — exactly what the palace provides
- Students have seen all items in Story Mode and Game Breaks; the palace re-organises them spatially
- The 10-second study window forces rapid scanning — mimics how expert memorisers encode

**Not recommended:**
- Phase 1 (student hasn't encountered items yet — nothing to anchor to zones)
- For procedural/sequential content (Puzzle Lock is better for ordered sequences)

---

# 15. STORY MODE

## What It Is
The narrative backbone of each homework session. Story Mode presents lesson content as a story with a protagonist, setting, and plot — not as a textbook explanation. Content is delivered in 3 segments of ~90 seconds each. Between segments, a Checkpoint question verifies comprehension before the story continues. The student is a passive reader/listener during segments and an active responder at checkpoints.

## How It Is Played

### Step-by-step flow
1. Scene card appears: icon + chapter label + narrative text (90 seconds reading time estimate)
2. "Davom etish" (Continue) button advances to next segment or checkpoint
3. At each checkpoint: question modal appears (no "Continue" button — question must be answered)
4. **Correct answer:** +80 XP, story continues
5. **Wrong answer:** 0 XP, story still continues (checkpoints are not blockers — they are measurement points)
6. After Segment 3: session summary + total XP
7. Story complete → transition to Game Breaks

### Segment structure

| Segment | Content | Bloom's level |
|---|---|---|
| 1 — Introduction | Hook + context + key concept introduced | Remember |
| Checkpoint 1 | Surface recall question | Remember/Understand |
| 2 — Mechanism | How/why the concept works | Understand |
| Checkpoint 2 | Comprehension question | Understand |
| 3 — Application | Real-world examples + connection to prior knowledge | Apply |
| Checkpoint 3 | Application question | Apply |

### Parameters
- Segments: 3 (expandable to 4 for complex topics)
- Checkpoints: 3 (one after each segment)
- XP: +80 per checkpoint correct answer (240 XP max from Story Mode)
- Checkpoints are non-blocking — wrong answer does not replay the segment
- AI Tier: 1 for checkpoints; Tier 2 for AI-generated narrative personalisation (future)
- Language: Uzbek (primary), Russian/English support planned

## Subject Implementations

### Natural Sciences — Photosynthesis
- S1: "Every morning the sun rises and plants wake up. For them, sunlight is not just light — it is energy..."
- CP1: "What energy source does photosynthesis use?"
- S2: "The leaf takes 3 things: light, water, CO₂. These combine to make sugar and oxygen..."
- CP2: "What does photosynthesis produce?"
- S3: "The green pigment chlorophyll captures light energy. Without leaves there is no photosynthesis..."
- CP3: "Which pigment plays the key role in photosynthesis?"

### History — Silk Road
- S1: "Centuries ago, camel caravans crossed the desert between China and Europe..."
- S2: "Cities like Samarkand grew not just because of trade, but because of what traveled alongside goods..."
- S3: "The Silk Road was not just an economic route — it was a channel for ideas, religions, and languages..."

## Where It Fits in the Homework

**Position: Phase 2 — Hikoya (the only mechanic in this phase)**

```
Phase 1 — Memory Hook (Spaced Flashcards / Memory Sprint)
    ↓
→ STORY MODE — Phase 2 (all 3 segments + checkpoints) ←
    ↓
Phase 3 — Game Breaks
```

**Mandatory phase:** Story Mode cannot be skipped. All subsequent game mechanics assume the student has been exposed to the content through Story Mode. Without Story Mode, Why Chain and Peer Teaching have no knowledge base to operate on.

---

# 16. ADAPTIVE QUIZ

## What It Is
A 10-question multiple-choice quiz where difficulty adjusts in real time based on student performance. Starting at Level 1 (L1), each correct answer raises difficulty by 1 level after 2 consecutive correct answers; each wrong answer drops difficulty by 1 level. The quiz ends after 10 questions. Final PISA level estimate and XP are based on the highest sustained difficulty level reached.

## How It Is Played

### Step-by-step flow
1. Question 1 appears at difficulty Level 1
2. Student selects one of 4 options
3. Immediate feedback shown (correct/wrong)
4. Difficulty adjusts for next question (up after 2 consecutive correct, down after any wrong)
5. Streak counter resets on any wrong answer
6. Repeat for 10 questions
7. Session summary: correct count, final level, XP earned

### Difficulty levels

| Level | PISA Equivalent | Question type |
|---|---|---|
| L1 | Below L2 | Direct recall, simple arithmetic |
| L2 | L2–L3 | Single-step reasoning, basic application |
| L3 | L3–L4 | Multi-step, concept connection |
| L4 | L4–L5 | Analysis, cause-effect reasoning |
| L5 | L5–L6 | Synthesis, evaluation, edge cases |

### Scoring
- XP per question: Level × 30 (L1 = 30 XP, L5 = 150 XP)
- Bonus: 3+ consecutive correct at L4–L5 = streak multiplier ×2
- Total XP range: 300 (all L1 correct) to ~1,200 (all L5 correct)

### Parameters
- Questions: 10 fixed
- Difficulty range: L1–L5 (5 levels)
- Escalation: +1 level after 2 consecutive correct
- De-escalation: −1 level after any wrong
- AI Tier: 1 (pre-banked question pool per level per subject)

## Subject Implementations

### All subjects
Each subject has a question bank organised by the 5 difficulty levels. Questions at L1 test vocabulary and surface recall; questions at L5 test analysis and synthesis.

## Where It Fits in the Homework

**Primary position: Phase 6 — Boss Fight**

```
Phase 5 — Consolidation
    ↓
→ ADAPTIVE QUIZ — Boss Fight ←
    ↓
Phase 7 — AI Analysis
    ↓
Phase 8 — Remediation
```

**Why the Boss position:**
- The Boss Fight must assess the full range of student ability — fixed-difficulty quizzes miss both very weak and very strong students
- Adaptive difficulty ensures every student is challenged appropriately
- The 10-question structure provides sufficient data for the post-session AI analysis
- Rising difficulty creates emotional arc: students feel the quiz "getting harder" as they succeed

**Not recommended:**
- As a Game Break (Boss position is its design purpose — using it earlier undermines the Boss Fight significance)
- Without the full question bank populated per subject (thin bank = repeated questions within session)

---

# 17. MYSTERY BOX

## What It Is
A surprise-reward mechanic built around knowledge gating. A 3×3 grid of 9 mystery boxes is presented — each concealing a different reward (large XP, medium XP, small XP, penalty, or empty). The student selects a box, answers a question, and if correct the box opens to reveal its contents. Wrong answer triggers a small XP penalty but the box still opens (revealing the prize regardless — the question is the gate, not the reveal).

## How It Is Played

### Step-by-step flow
1. 3×3 grid of identical mystery boxes (contents unknown)
2. Student taps any box
3. Question modal appears
4. **Correct answer:** box opens to reveal prize; full XP awarded
5. **Wrong answer:** −30 XP penalty; box opens anyway (student still sees what was inside)
6. Repeat until all 9 boxes opened
7. Session summary: big prizes / medium prizes / penalty count / total XP

### Prize distribution (fixed per session, randomised placement)
| Prize type | Count | XP value |
|---|---|---|
| Large prize (🏆) | 1 | +300 XP |
| Medium prize (⭐) | 3 | +150 XP each |
| Small prize (💫) | 3 | +80 XP each |
| Penalty (💀) | 1 | −30 XP |
| Empty (📭) | 1 | 0 XP |

### Parameters
- Grid: 3×3 (9 boxes)
- Prize placement: randomised each session
- Wrong answer cost: −30 XP (does not affect box reveal)
- AI Tier: 1
- All subjects

### Psychological design
The box-opening reveal creates genuine anticipation — students do not know which box has the large prize. This variable reward schedule (Skinner, 1938) is among the most powerful engagement drivers in game design. The knowledge gate ensures XP is earned, not just discovered. The penalty box creates mild risk-aversion without catastrophic consequences.

## Subject Implementations

Questions are drawn from the lesson concept pool — identical format to other Game Break mechanics. The Mystery Box shell is subject-agnostic; only the questions change per lesson.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement)**

**Why this position:**
- High novelty and engagement — ideal for the first Game Break where motivation is most critical
- Low cognitive overhead (standard MCQ) allows focus on the surprise element
- Short per-box interaction (tap + answer + reveal) maintains pace

**Also suitable:**
- As a bonus mechanic after completing other Game Breaks (reward feel)

**Not recommended:**
- As the only mechanic in a session (no depth beyond surprise; needs a higher-order mechanic alongside it)
- Boss Fight position (lacks the assessment rigor required there)

---

# 18. MEMORY MATCH BLITZ

## What It Is
An accelerated variant of Tile Match with a critical addition: all cards are briefly revealed at the start of the game. Before the timer begins, all 16 cards are shown face-up for exactly 3 seconds — then hidden simultaneously. The student then has 60 seconds to find all 8 pairs from memory alone. No question gating — pure speed and spatial memory.

## How It Is Played

### Step-by-step flow
1. Empty 4×4 board displayed
2. "Boshlash" (Start) tapped
3. **Peek phase:** all 16 cards flip face-up simultaneously — 3 second countdown
4. At 0: all cards flip back face-down — timer starts at 60 seconds
5. Student taps two cards to flip them
6. **Match:** both cards lock face-up (+40 XP)
7. **No match:** both flip back face-down after 0.7 seconds
8. Game ends when all 8 pairs matched OR timer reaches 0
9. Final XP: matched pairs × 40, minus wrong flips × 5

### Parameters
- Grid: 4×4 (8 pairs)
- Peek duration: 3 seconds (fixed)
- Game timer: 60 seconds
- XP: +40 per matched pair; −5 per wrong flip attempt; speed bonus if all 8 matched with >20 seconds remaining
- No question gating (pure memory — no knowledge questions)
- AI Tier: 0

### Difference from Tile Match

| Feature | Tile Match | Memory Match Blitz |
|---|---|---|
| Knowledge gate | ✅ Question per match | ❌ No questions |
| Preview | ❌ No preview | ✅ 3-second preview |
| Timer | ❌ Untimed | ✅ 60 seconds |
| Bloom's level | Remember + Apply | Remember (pure) |
| Phase placement | Game Break 1 | Memory Hook (Phase 1) |

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

**Why this position:**
- The 3-second preview pre-loads visual items into working memory before lesson content arrives
- No question gate = no knowledge required = appropriate before content is taught
- 60-second duration fits the Memory Hook time budget

**Not recommended:**
- As a Game Break (no knowledge gate = no content reinforcement)
- G1–2 (3-second encoding window too fast for early readers)

---

# 19. REACTION CHAIN

## What It Is
A rapid categorisation mechanic. Items (emoji + name) appear one at a time and the student must tap the correct category bucket to sort them. The faster and more accurately they sort, the longer their "chain" grows. Correct sorts extend the chain and increase the XP multiplier; any wrong sort breaks the chain and resets the multiplier to ×1. The session runs for 90 seconds.

## How It Is Played

### Step-by-step flow
1. 4 category buckets displayed (e.g. Living / Non-living / Natural / Man-made)
2. Timer starts: 90 seconds
3. Item appears in centre: emoji + name + hint question
4. Student taps the correct bucket
5. **Correct:** item counted in bucket; chain length +1; chain display updates
6. **Wrong:** chain resets to 0; chain display clears
7. Next item appears immediately (no delay)
8. Session ends when timer reaches 0
9. Final XP: correct × 30, with chain multiplier (×2 at chain ≥3)

### Chain mechanics

| Chain length | XP multiplier |
|---|---|
| 1–2 | ×1 (30 XP per item) |
| 3–5 | ×2 (60 XP per item) |
| 6–9 | ×2 + combo banner |
| 10+ | ×3 (90 XP per item) |

### Parameters
- Timer: 90 seconds
- Categories: 4 (subject-specific per lesson)
- XP: base 30 per correct, multiplied by chain
- No question modal — answer IS the bucket tap (instant feedback)
- AI Tier: 0 (rule-based categorisation, no generative AI)

## Subject Implementations

### Natural Sciences
- Categories: Tirik (Living) / Jonsiz (Non-living) / Tabiiy (Natural) / Insoniy (Man-made)
- Items: animals, minerals, rivers, machines

### Exact Sciences
- Categories: Kasrlar / Butun sonlar / Geometrik shakllar / Algebraik ifodalar
- Items: mathematical expressions sorted by type

### Language Sciences
- Categories: Noun / Verb / Adjective / Adverb
- Items: words to be classified by part of speech

### History
- Categories: Qadimgi davr / O'rta asrlar / Yangi davr / Zamonaviy davr
- Items: historical events sorted by period

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply)**

**Why this position:**
- Bloom's Apply — student must know categories well enough to sort instantly
- The 90-second duration and rapid-fire pace suit the mid-session energy peak
- Chain mechanic creates natural excitement arc in the middle of the session

**Not recommended:**
- Phase 1 (student hasn't learned the categories yet)
- For nuanced content where categorisation is ambiguous (use Sentence Fill instead)

---

# 20. WORD LADDER CLIMB

## What It Is
A word transformation puzzle where the student changes one letter at a time to transform a start word into a target word — each intermediate step must be a valid word. Before each letter change is accepted, the student must answer a subject question. Correct answer → change applied, rung added to the ladder. Wrong answer → change rejected, student tries again. The visual ladder grows upward as the student climbs toward the target.

## How It Is Played

### Step-by-step flow
1. Start word shown at bottom of ladder; target word shown at top
2. Student taps a letter in the current word to select it
3. Student taps a replacement letter from the on-screen alphabet
4. "Qo'llash" (Apply) button confirms the change
5. If the proposed word is not on the valid path: rejected immediately (no question asked)
6. If the proposed word is valid: question modal appears
7. **Correct answer:** new word appears as the next rung on the ladder (+60 XP)
8. **Wrong answer:** change rejected, student must re-attempt (+0 XP, wrong counter +1)
9. Repeat until target word reached
10. Bonus +100 XP for zero wrong answers

### Ladder display
- Each completed rung shows the word with the changed letter underlined/highlighted
- Target rung shown in blue throughout (constant visual goal)
- Current word shown in amber (active position)
- Completed rungs shown in green

### Parameters
- Word length: 3–4 letters (expandable to 5 for G7+)
- Ladder depth: 3–5 steps depending on puzzle
- XP: +60 per valid step + 100 bonus for clean run
- No timer (strategic puzzle — student-paced)
- AI Tier: 1 (pre-constructed valid paths)
- Subject: Language Sciences primary; all subjects for abbreviation-based variants

## Subject Implementations

### Language Sciences (Primary)
- CAT → COT → COG → DOG (English vocabulary)
- HOT → HOD → COD (3-step)
- COLD → CORD → WORD → WARD → WARM (5-step)

### All subjects (Abbreviation variant)
- ATOM → ATOP → STOP → STEP (science abbreviations as waypoints)
- Questions at each step test the meaning of the word/abbreviation being changed to

## Where It Fits in the Homework

**Primary position: Phase 5 — Mustahkamlash (Consolidation)**

**Why this position:**
- Requires deliberate letter-level attention — deepens vocabulary encoding after surface exposure
- Strategic puzzle nature suits the consolidation phase (student has time to think, not racing)
- The visual ladder provides clear progress metaphor aligned with the session's "climb" narrative

**Also suitable:**
- Language Sciences sessions as a Phase 3 Game Break (vocabulary focus)

**Not recommended:**
- Phase 1 (vocabulary hasn't been taught yet)
- Non-language subjects as primary (letter manipulation has weak connection to most content areas)
- Recovery sessions (puzzle complexity too high for struggling students)


---


## 7. PISA Skill Progression Framework

### 7.1 Mathematics Progression

*Source: HOMEWORK_STANDARDS.md Section 4.1, confirmed against textbook analysis.*

| Grade | PISA Target Level | Key Competencies | Primary NETS Games | Transition Skills |
|---|---|---|---|---|
| 1-2 | Below 1 - 1 | Basic recall, simple single-step operations | Memory Sprint, Tile Match, Movement Breaks | Basic number sense, single-step procedures |
| 3 | Level 1 | Single-step problems, familiar contexts | Memory Sprint, Tile Match, Flashcards | L0->L1: answer questions with all info present |
| 4 | Level 1-2 | Single-step to basic multi-step | Story Mode, Adaptive Quiz, Sentence Fill | L1->L2: extract from simple charts; basic ratios |
| 5 | Level 2 | Multi-step problems, basic reasoning | Why Chain, Final Boss, Mystery Box | L1->L2: interpret simple representations |
| 6 | Level 2-3 | Applied mathematics, beginning modeling | Real-Life Challenge, Adaptive Quiz | L2->L3: sequential decisions; communicate reasoning |
| 7 | Level 3 | Complex reasoning, justification | Why Chain (4+ levels), Final Boss Medium | L2->L3: integrate multiple info sources |
| 8 | Level 3-4 | Abstract thinking, proof concepts | Final Boss, Mystery Box, Peer Teaching | L3->L4: explicit models; integrate representations |
| 9 | Level 4 | Advanced modeling, evaluation | Real-Life Challenge, Peer Teaching | L3->L4: construct explanations with evidence |
| 10 | Level 4-5 | Complex problem solving, strategy comparison | All games at mastery level | L4->L5: develop models; compare strategies |
| 11 | Level 5-6 | PISA readiness, creative mathematical thinking | Final Boss Hard, Real-Life Extended, Creative Lab | L5->L6: conceptualize; generalize; advanced reasoning |

**PISA Skill Focus -- Mathematics:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Mathematical Reasoning | Construct logical arguments | Why Chain, Final Boss | PISA-calibrated |
| Problem Solving | Apply math to novel situations | Real-Life Challenge, Mystery Box | PISA-calibrated |
| Mathematical Modeling | Translate real world -> math | Real-Life Challenge | PISA-calibrated |
| Communication | Explain mathematical thinking | Reflection Journal, Why Chain, Peer Teaching | PISA-calibrated |

### 7.2 Reading Progression

*Source: Leonardo's gap analysis template + PISA 2022 Reading framework. Fills the critical placeholder stubs from HOMEWORK_STANDARDS.md Sections 4.2.*

| Grade | PISA Target Level | Key Skill Focus | Primary NETS Games | Transition Skills |
|---|---|---|---|---|
| 1-2 | Level 1 | Retrieval: locate single explicit information in short text | Memory Sprint (vocab recall), Sentence Fill, Tile Match | Basic word recognition, literal comprehension |
| 3-4 | Level 1-2 | Inference: identify main idea; make straightforward inferences | Story Mode, Why Chain (2-level), Sentence Fill | L1->L2: compare info across simple sources; basic inference |
| 5-6 | Level 2-3 | Interpretation: integrate info from multiple parts of text; generate inferences | Why Chain (3-level), Mystery Box, Adaptive Quiz | L2->L3: integrate several pieces of info; compare/contrast |
| 7-8 | Level 3-4 | Evaluation: reflect on content and form; evaluate relevance | Real-Life Challenge, Why Chain (4-level), Final Boss Medium | L3->L4: interpret nuance; draw inferences from multiple sources |
| 9-11 | Level 4-6 | Critical Analysis: evaluate competing claims; assess reliability; synthesize across sources | Real-Life Challenge (extended), Final Boss Hard, Peer Teaching, Creative Lab | L4->L5: evaluate credibility; handle contradiction |

**PISA Skill Focus -- Reading:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Access and Retrieve | Find explicit information in text | Memory Sprint, Sentence Fill | Textbook |
| Integrate and Interpret | Draw conclusions, make inferences, understand author's intent | Why Chain, Mystery Box, Real-Life Challenge | PISA-calibrated |
| Reflect and Evaluate | Judge text quality/credibility, evaluate arguments | Final Boss, Reflection Journal, Peer Teaching | PISA-calibrated |

### 7.3 Science Progression

*Source: Leonardo's gap analysis template + PISA 2022 Science framework. Fills the critical placeholder stubs from HOMEWORK_STANDARDS.md Sections 4.3.*

| Grade | PISA Target Level | Key Skill Focus | Primary NETS Games | Transition Skills |
|---|---|---|---|---|
| 1-2 | Level 1 | Scientific Knowledge: recall basic scientific facts; identify simple cause-effect | Memory Sprint, Flashcards, Movement Breaks | Basic observation, naming phenomena |
| 3-4 | Level 1-2 | Scientific Explanation: describe simple cause-effect relationships | Story Mode, Tile Match, Why Chain (2-level) | L1->L2: explain familiar phenomena; identify variables |
| 5-6 | Level 2-3 | Evidence Evaluation: use evidence to support claims; interpret data from simple tables | Mystery Box, Adaptive Quiz, Why Chain (3-level) | L2->L3: interpret data/evidence; identify experimental questions |
| 7-8 | Level 3-4 | Experimental Design: identify variables, propose tests, evaluate methods | Real-Life Challenge, Why Chain (4-level), Final Boss Medium | L3->L4: use abstract scientific content; reflect using evidence |
| 9-11 | Level 4-6 | Advanced Modeling: construct scientific models; evaluate competing hypotheses | Real-Life Challenge (extended), Final Boss Hard, Peer Teaching, Creative Lab | L4->L5: apply knowledge to novel/complex situations; evaluate competing explanations |

**PISA Skill Focus -- Science:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Scientific Explanation | Explain phenomena using evidence | Why Chain, Story Mode | Textbook + PISA |
| Evaluation and Design | Evaluate experiments, design investigations | Real-Life Challenge, Final Boss | PISA-calibrated |
| Data Interpretation | Analyze graphs, tables, evidence | Tile Match, Adaptive Quiz | PISA-calibrated |
| Scientific Reasoning | Construct causal chains | Why Chain (3+ levels) | PISA-calibrated |

---

### 7.4 History Progression

*Source: Research proposal P44 (History Philosophy), gap analysis (Michelangelo assessment p.283-290) identified History as having zero game adaptation specs despite being referenced in §15 (Parent Portal). This section fills that BLOCKER gap.*

> **History Philosophy:** The textbook presents events; NETS forces ANALYSIS of causation and significance. History is not a PISA-assessed domain, but it develops competencies that transfer to two PISA domains: **Reading** (source evaluation, textual inference, evidence-based argumentation) and **Creative Thinking** (multiple perspectives, evaluating competing claims, generating explanations). History uses **dual-domain PISA mapping** — it does not have its own PISA levels.

> **Note on Catch-Up Mode:** History chapters are classified as NON-enrichment. Prerequisite chains exist (e.g., understanding historical sources in §1 is prerequisite for evaluating sources in later chapters). History chapters MUST NOT be skipped as "standalone enrichment" in Catch-Up Mode.

| Grade | PISA Reading Target | PISA Creative Thinking Target | Key Competencies | Primary NETS Games | Transition Skills |
|---|---|---|---|---|---|
| 5 | Level 1-2 | Generating diverse ideas | Define history; identify and classify source types; recall key terms and examples | Memory Sprint, Tile Match, Flashcards, Sentence Fill, Mystery Box | L1→L2: locate explicit info; classify by attributes |
| 6 | Level 2 | Generating + evaluating ideas | Interpret what sources reveal; compare source types; explain significance of evidence | Why Chain (3-level), Mystery Box, Adaptive Quiz, Story Mode | L1→L2: make straightforward inferences; compare across simple sources |
| 7 | Level 2-3 | Evaluating + improving ideas | Analyze causation; distinguish fact from interpretation; construct simple arguments | Why Chain (4-level), Real-Life Challenge, Final Boss | L2→L3: integrate info; compare/contrast with competing sources |
| 8 | Level 3 | Full creative problem-solving | Evaluate reliability of sources; analyze multiple perspectives on events; construct evidence-based arguments | Real-Life Challenge, Why Chain (4-5 level), Final Boss, Peer Teaching | L2→L3: evaluate relevance; handle partial/conflicting info |
| 9 | Level 3-4 | Full creative problem-solving | Synthesize across multiple sources; evaluate competing historical claims; construct original interpretations | Real-Life Challenge, Final Boss (Hard tier), Peer Teaching | L3→L4: interpret nuance; draw inferences from multiple sources |
| 10-11 | Level 4-5 | Full creative problem-solving | Advanced historiographical analysis; evaluate primary vs. secondary sources; construct complex arguments with evidence | Final Boss (Hard tier), Real-Life Extended, Creative Lab, Peer Teaching | L4→L5: evaluate credibility; handle contradictory information |

**PISA Skill Focus — History:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Source Evaluation | Classify, compare, and evaluate reliability of historical sources | Tile Match (artifact-concept pairing), Mystery Box (source classification), Final Boss (evaluate limitations) | PISA Reading: Access and Retrieve + Reflect and Evaluate |
| Causation Analysis | Identify causes, consequences, and chains of historical events | Why Chain (causal chains), Story Mode (cause/effect framing) | PISA Reading: Integrate and Interpret |
| Perspective-Taking | Understand multiple viewpoints on historical events | Real-Life Challenge (compare past to present), Creative Lab (alternative explanations) | PISA Creative Thinking: Generating diverse ideas |
| Argumentation | Construct evidence-based historical arguments | Final Boss (argumentation with evidence), Peer Teaching (explain with evidence) | PISA Reading: Reflect and Evaluate |

**Game Adaptation for History:**

| Game Mechanic | History Adaptation | Example (Grade 5, §1) |
|---|---|---|
| Tile Match | Match artifacts to their names, functions, or time periods | [Stone tool image] ↔ "Mehnat quroli" |
| Flashcards | Historical terms, dates, source type definitions | Front: "Arxiv" → Back: "Eski hujjatlar saqlanadigan joy" |
| Sentence Fill | Fill blanks in historical definitions and descriptions | "Tarixiy manba — bu inson qo'li bilan yaratilgan barcha _____ va yozib qoldirilgan _____" |
| Mystery Box | Classify objects/descriptions as moddiy manba / yozma manba / boshqa | "Qadimgi tanga" → Student identifies: "Moddiy manba" |
| Why Chain | Trace causal chains in historical events (NOT for introductory lessons — requires prior knowledge) | "Nima uchun Ipak yo'li Samarqand orqali o'tgan?" → "Geografik joylashuvi..." → "Nima uchun..." |
| Story Mode | Narrative with primary source excerpts → cause/effect framing (per §5.2 line 569) | "Sardor bobosi bilan muzeyga boradi..." |
| Real-Life Challenge | Connect historical concepts to student's mahalla, family, or modern Uzbekistan | "Mahallangiz tarixini o'rganish uchun qanday manbalardan foydalanasiz?" |
| Final Boss | Argumentation with evidence; evaluate what sources can and cannot tell us | "Arxeologlar faqat moddiy manbalar topdi. Nimalarni bilib bo'ladi, nimalarni bilib bo'lmaydi?" |
| Adaptive Quiz | Short-answer questions on source types, terminology, classification (replaces IRT for non-numerical History content) | "Avesto — bu qanday manba turi? Javobingizni tushuntiring." |
| Memory Palace | Place historical concepts at Uzbek architectural landmarks | Walk through Registan: each madrasah holds a concept |
| Reflection Journal | "Tarixni o'rganish haqida fikringiz qanday o'zgardi?" | Metacognitive, not PISA-assessed |

**AI Considerations for History:**
- History questions often have MULTIPLE VALID ANSWERS (unlike math). AI evaluation must accept reasoned alternatives, not just exact matches.
- AI MUST check generated content against textbook-stated historical facts (Section 18.2 Prohibition #2: "Modify historical dates, geographical information, or biographical facts").
- For Why Chain in History: requires deeper prior knowledge than introductory lessons provide. Reserve for chapters where students have sufficient context for causal reasoning.
- For Socratic tutoring on boss failure: AI references specific textbook pages and uses cause/effect framing, not just factual correction.

---

## 8. PISA Creative Thinking Domain

*Source: Gap analysis (Leonardo) identified that PISA 2022 assessed Creative Thinking for the first time. Uzbekistan scored 14/60 (OECD average: 33/60). No previous spec addressed this. This section is entirely new.*

### 8.1 Why Creative Thinking Matters

PISA Creative Thinking assesses four competencies:
1. **Generating diverse ideas** -- producing multiple different solutions
2. **Generating creative ideas** -- producing original, non-obvious solutions
3. **Evaluating and improving ideas** -- refining and selecting best approaches
4. **Expressing ideas** -- written, visual, scientific, and social problem-solving

### 8.2 Creative Thinking Through Existing Mechanics

Rather than adding a 15th mechanic immediately, existing mechanics are expanded with Creative Thinking variants:

| Mechanic | Standard Mode | Creative Thinking Expansion |
|---|---|---|
| Real-Life Challenge | 1 correct solution path | "Generate 3 DIFFERENT solutions. Which is best? Why?" |
| Final Boss (Hard tier) | Evaluate/Create questions | Include open-ended design/creation questions: "Design a water system for your school using these constraints" |
| Reflection Journal | "What strategy helped?" | "What would you do differently? Design an alternative approach" |
| Why Chain | Linear causal chain | "Branch Chain": at Level 3+, student must identify 2+ different causal paths |
| Peer Teaching | Explain correct method | "Explain the concept using a completely different analogy than the textbook" |

### 8.3 Creative Lab (Optional Mechanic)

For students at PISA Level 3+ who have demonstrated readiness:

```
CREATIVE LAB:
  Duration: 5-8 minutes (replaces one Game Break in Extended Mode)
  Format: Open-ended challenge with multiple valid solutions

  TYPES:
  1. "Design Challenge": Design a solution to a real problem using concepts from this chapter
  2. "What If?": Change one variable in a scenario and predict consequences
  3. "Mashup": Combine concepts from 2 different chapters to solve a novel problem
  4. "Improve It": Given a flawed solution, find 3 ways to improve it

  SCORING:
  - Diversity of ideas (multiple distinct approaches): +100 XP per unique approach
  - Originality (solution not in standard answer bank): +200 XP
  - Feasibility (solution actually works): +100 XP
  - Communication (explanation is clear): +100 XP
  - Max: 500 XP

  AI TIER: Tier 2 (AI evaluates creativity and feasibility)
  AVAILABILITY: Grades 5-11, PISA Level 3+ only
  SESSION PLACEMENT: Replaces one Game Break OR offered as bonus after Session Complete
```

### 8.4 Creative Thinking Progression

| Grade Band | Creative Thinking Focus | NETS Implementation |
|---|---|---|
| 1-4 | Divergent play, multiple representations | Movement Breaks with creative element; Tile Match with "make your own pair" |
| 5-6 | Generate multiple solutions | Real-Life Challenge: "Find 2 different ways to solve this" |
| 7-8 | Evaluate and improve ideas | Why Chain branches; Peer Teaching with alternative explanations |
| 9-11 | Full creative problem-solving | Creative Lab; Final Boss Hard tier with design questions |

---

## 9. Difficulty Adaptation Engine

### 9.1 Real-Time Adjustment (Within Session)

*Source: Both specs combined. Percentage thresholds from HOMEWORK_STANDARDS.md, consecutive-item rules from original spec as secondary triggers.*

```
ADAPTATION RULES (checked every 3-5 questions):

PRIMARY (percentage-based):
  IF success_rate < 60%:
    -> difficulty_tier -= 1
    -> Provide scaffolding (hints enabled, simpler representations)
    -> DO NOT drop below the student's established floor

  IF success_rate > 90%:
    -> difficulty_tier += 1
    -> Reduce hint availability
    -> Introduce next Bloom's level items

  IF success_rate 70-80%:
    -> Maintain current tier (FLOW ZONE)

SECONDARY (event-based):
  IF student gets 3 consecutive correct at current level:
    -> Increase difficulty by 0.5 PISA sub-level

  IF student gets 2 consecutive wrong:
    -> Decrease difficulty by 0.5 PISA sub-level
    -> Provide scaffolded version of the question

EMERGENCY:
  IF accuracy in a game break < 40%:
    -> Flag the specific standard
    -> Insert additional Story Mode micro-segment for that standard
    -> The micro-segment references the exact textbook page

ALWAYS:
  -> Maintain 60-80% success rate target (Csikszentmihalyi flow channel)
  -> Track per-standard accuracy, not just overall
  -> Track per-transition-skill accuracy
```

### 9.2 Difficulty Tiers

| Tier | Description | Success Rate Target | PISA Level Range |
|---|---|---|---|
| Tier 1 | Foundational (recall) | 80-90% | Below 1 - 1 |
| Tier 2 | Basic application | 70-80% | 1-2 |
| Tier 3 | Multi-step reasoning | 70-80% | 2-3 |
| Tier 4 | Complex analysis | 60-70% | 3-4 |
| Tier 5 | Advanced evaluation/creation | 60-70% | 5-6 |

### 9.3 Cross-Session Adaptation

```
AFTER EACH SESSION:
  1. UPDATE student_pisa_profile with new performance data
  2. UPDATE spaced_repetition_model (which items need review, when)
  3. UPDATE standard_mastery_map:
     - Each standard has a mastery score: 0.0 (never seen) to 1.0 (fully mastered)
     - Mastery decays over time (Ebbinghaus curve)
     - Standards below 0.6 mastery are flagged for Memory Sprint inclusion
  4. UPDATE transition_skill_tracker:
     - Mark transition skills as mastered (>80% accuracy across 3+ sessions)
     - Identify new transition skills to target
  5. RECALCULATE domain_breakdown (quantity, space, etc.)
  6. CHECK trajectory:
     - If 3 consecutive sessions show declining performance -> activate Boost Mode
     - If student exceeds grade target PISA level -> offer enrichment content
```

---

## 10. Textbook-to-NETS Content Pipeline

### 10.1 Pipeline Overview

*Source: Original spec Section 8 for the conceptual pipeline, HOMEWORK_TASK_ENGINE.md Section E for the detailed engineering pipeline. Combined.*

```
TEXTBOOK (physical book)
    |
    v
Phase 1: INGESTION (offline, one-time per textbook)
    |-- [1. OCR Engine] -> Raw text + bounding boxes
    |     (Tesseract for Uzbek/Russian + GPT-4o Vision for diagrams/formulas)
    |-- [2. Structure Parser] -> Structured document (JSON tree)
    |     (Detect: Chapter, Section, Example, Exercise, Definition, Diagram)
    |-- [3. Content Splitter] -> Learning Units (LUs)
    |     (1 LU = one teachable concept, typically 2-3 per textbook section)
    |-- [4. Standard Tagger] -> Tagged LUs
    |     (Map each LU to UZ-SUBJ-GRADE-TOPIC-SEQ + prerequisites)
    |     (HUMAN TEACHER REVIEW REQUIRED -- batch approval UI)
    |
    v
Phase 2: TASK GENERATION (offline, batch process)
    |-- [5. Bloom's Distributor] -> Task specifications per LU
    |     (4 Remember, 3 Understand, 3 Apply, 2 Analyze, 1-2 Evaluate/Create)
    |     (Each spec includes target PISA level + transition skill)
    |-- [6. Task Generator] -> Raw tasks (3 modes):
    |     Mode A: Template Fill (80% of tasks, Tier 1) -- ~$0.0001/task
    |     Mode B: AI Augmented (15% of tasks, Tier 2) -- ~$0.001/task
    |     Mode C: AI Creative (5% of tasks, Tier 3) -- ~$0.01/task
    |-- [7. Game Mechanic Router] -> Mechanic-assigned tasks
    |     (Bloom's + content type -> best mechanic from Decision Table)
    |-- [8. Common Error Annotator] -> Enriched tasks
    |     (2-3 likely wrong answers per task, each tagged with misconception)
    |
    v
Phase 3: QUALITY ASSURANCE (semi-automated)
    |-- [9. Automated QA] -> Validated tasks
    |     Checks: answer correctness, language grade-appropriateness,
    |     Bloom's tag matches cognitive demand, PISA level consistent,
    |     no duplicates, prerequisites valid, time estimate realistic,
    |     Buzan QA gates (see below)
    |     (Reject rate target: <10%)
    |-- [10. Teacher Review Queue] -> Approved tasks
    |     (Batch review UI, minimum 1 teacher per LU)
    |     (Tier 3 tasks ALWAYS human-reviewed)
    |     (Target: 50 tasks/hour per reviewer)
    |-- [11. IRT Calibration] -> Calibrated tasks
    |     (Initial estimate from AI; after 30+ student attempts: recalibrate)
    |
    v
Phase 4: SESSION ASSEMBLY & DEPLOYMENT (real-time)
    |-- [12. Student Profile Check] -> PISA level, prerequisites, spaced repetition schedule
    |-- [13. Session Assembler] -> 7-Step Session (20-30 min, 15-25 tasks)
    |     Buzan: Schema Activation Check — verify every P2 concept has a
    |     prerequisite activated in P1 or P0-B. Auto-inject if missing.
    |-- [14. Delivery API] -> Frontend renders session
    |-- [15. Analytics Collector] -> Performance data (feeds back into steps 11, 12, 13)
```

### 10.1b Buzan Quality Gates (added to Automated QA, Step 9)

Four additional checks added to the pipeline. All are additive — they supplement existing QA, never replace it.

| Gate | Applies To | Rule | On Fail |
|---|---|---|---|
| **80/20 Keywords** | Every `narrative_segment` | Must have `keywords_80_20` array (3-8 tagged keywords carrying ~80% of meaning). Fed to Radiant Summary, Flash Cards, Sentence Fill, Memory Sprint. | Block → stays DRAFT |
| **Dual Coding** | Every `game_item`, `mnemonic_exercise`, `boss_question` | Must declare 2+ encoding channels: VRB (verbal), VIS (visual), SPA (spatial), AUD (auditory), KIN (kinesthetic) | Block → stays DRAFT |
| **SMASHIN' SCOPE** | Every `mnemonic_exercise` (Memory Palace, Peg System, Radiant Summary, Link Chain) | Must score 6+/12: Synaesthesia, Movement, Association, Substitution, Humor, Imagination, Number, Symbolism, Color, Order, Positive, Exaggeration. **Provisional threshold — subject to empirical calibration after pilot data.** | Return for enrichment |
| **Schema Activation** | Session plan (Step 13) | Every new concept in P2 must have ≥1 prerequisite activated in P1 or P0-B | Auto-fix (inject prerequisite into Sprint) |

*Where these gates do NOT apply:* 80/20 Keywords don't apply to game items or boss questions (only narrative segments). SMASHIN' SCOPE doesn't apply to non-mnemonic content (quizzes, checkpoints, boss questions). Dual Coding doesn't apply to Movement Breaks (physical activity, not knowledge encoding).

### 10.2 Minimum Content Requirements Per Topic

Before a topic can be assigned as homework, it must have:

| Content Type | Minimum Count | Purpose |
|---|---|---|
| `recall_item` | 10 | Memory Sprint pool (rotated across sessions) |
| `narrative_segment` | 3-5 | Story Mode delivery |
| `checkpoint_question` | 1 per segment | Story Mode gates |
| `tile_match_pair` | 8 pairs | Game Break option |
| `flashcard` | 10 cards | Game Break + Mnemonic Lock |
| `sentence_fill` | 8 items | Game Break option |
| `quiz_item` | 12 items (4 easy, 4 medium, 4 hard) | Game Break -- adaptive |
| `mystery_box_item` | 6 items (mixed topics) | Game Break option |
| `why_chain_sequence` | 3 sequences | Game Break option |
| `real_life_scenario` | 3 scenarios | Phase 4 (rotated) |
| `mnemonic_exercise` | 2 exercises | Phase 5 (selected by technique) |
| `boss_question` | 15 questions (5 easy, 5 medium, 5 hard) | Phase 6 (regeneration pool) |
| `reflection_prompt` | 3 prompts | Phase 7 (rotated) |

**Total minimum per topic: ~85 content items**, all tagged, all reviewed, all traceable to the textbook.

### 10.3 Pipeline Cost Estimate

| Phase | Cost Driver | Estimate |
|---|---|---|
| OCR + Parsing | GPT-4o Vision, ~200 pages | ~$5 |
| Task Generation | 500 tasks avg per textbook | ~$5 (80% Tier 1 + 15% Tier 2 + 5% Tier 3) |
| QA Automated | LLM validation pass | ~$1 |
| Teacher Review | 10 hrs at local rate | ~$50 |
| **Total per textbook** | | **~$61** |
| **Total for Grade 5 (10 subjects x 2 languages)** | | **~$1,220** |
| **Total for Grades 5-8 (pilot scope)** | | **~$4,880** |

### 10.4 Confirmed Textbook Inventory (from NETS.zip)

| Grade | Language | Subjects Available | Key Gaps |
|---|---|---|---|
| 5 | Russian | Science, Informatics, History, Fine Arts, Ethics, Technology | Math (separate PDF), Language textbooks |
| 5 | Uzbek | Biology, Geography, Informatics, Music, Science, Ethics, Technology | Math, Language textbooks |
| 6 | Russian | Science, Botany, Ethics, Informatics, History, Literature, Music, Technology | Math, Language |
| 7 | Russian | Algebra, Biology, Geography, Geometry, Informatics, Literature, Physics, Chemistry | Language |
| 7 | Uzbek | Algebra, Biology, Physics, Geography, Geometry, Informatics, Chemistry | Language |
| 8 | Russian | Algebra, Biology, Ethics | Very incomplete |

*Source: Textbook analysis. Grade 5 Math (2024 RU) provided separately -- deep analysis confirmed CPA progression, 13 chapters across 2 parts, ~65 Learning Units, estimated 600-900 tasks.*

---

## 11. Gamification Economy

### 11.1 XP Award Matrix

*Source: HOMEWORK_STANDARDS.md Section 6.1 XP values (scaled appropriately for the gamification economy).*

| Action | Base XP | Notes |
|---|---|---|
| Memory Sprint (per correct) | 100 | +10 streak bonus per consecutive correct |
| Story Mode completion | 150 | Per session |
| Tile Match (perfect) | 300 | Partial: 100-250 |
| Why Chain (per level) | 150 | Grades 1-4: 100, Grades 9-11: 200 |
| Sentence Fill (per correct) | 100 | First-attempt bonus: +25 |
| Mystery Box (per box) | 250 max | 50 type ID + 150 solution + 50 bonus |
| Real-Life Challenge | 400 | Grades 1-4: 300, Grades 9-11: 500 |
| Memory Palace (all correct) | 300 | 50 per concept recalled |
| Final Boss (3 stars) | 1000 | 2 stars: 700, 1 star: 500 |
| Reflection Journal | 100 | Completion only |
| Peer Teaching | 400 | Completeness + Clarity + Accuracy |
| Creative Lab | 500 max | Diversity + Originality + Feasibility + Communication |

### 11.2 Streak Multipliers

| Streak Length | XP Multiplier | Visual Indicator |
|---|---|---|
| Daily (1 day) | +20% | 1 flame |
| 7 days | +50% | 7 flames |
| 14 days | +75% | Special frame |
| 30+ days | +100% | Special frame + title |

### 11.3 Mastery Stars

See Phase 6 (Section 5.6) for star criteria.

### 11.4 Badge System

| Badge | Requirement | Display |
|---|---|---|
| Mentor | Help 10 peers via Peer Teaching | Profile + avatar frame |
| Streak Master | 30-day streak | Profile + loading screen |
| PISA Champion | Reach PISA Level 3+ in any subject | Profile + special title |
| Boss Slayer | Defeat 50 bosses | Profile + avatar accessory |
| Speed Learner | Complete chapter in <10 min | Profile |
| Rising Star | Most improved (weekly) | Weekly rotating badge |
| Bazaar Helper | Complete 10 Real-Life Challenges | Profile |
| Creative Mind | Complete 5 Creative Lab challenges | Profile |

### 11.5 Leaderboard Specification

*Source: Gap analysis (Donatello) identified missing spec. Rules from source docx.*

- **Scope:** Class-level ONLY (no school-wide to prevent unhealthy competition)
- **Reset:** Weekly (every Monday)
- **Categories:** XP, Streak, Chapters Mastered, Most Improved
- **Top 3:** Recognition with rotating spotlight
- **Anti-competition:** No public shaming. Celebrate improvement, not just ranking. Parents can opt-in.
- **Student always sees:** Own position and progress, regardless of leaderboard opt-in

### 11.6 Avatar Customization

- Cultural-themed cosmetic items (Uzbek traditional clothing, Silk Road outfits, Registan-themed items)
- Unlocked via achievements, NEVER purchases
- Non-competitive (no "rare" items that create social pressure)
- Display in: leaderboards, reflection journal, peer teaching, profile

**Principle 3 compliance:** All gamification rewards celebrate learning progress. Zero pay-to-win. Zero real-money purchases.

---

## 12. Edge Cases and Recovery Modes

*Source: Original spec Sections 9.1-9.4. Entirely absent from HOMEWORK_STANDARDS.md -- gap analysis (Donatello) rated this as critical missing. These are daily realities for 8.8M students.*

### 12.1 Missed Homework (Within Grace Period)

```
Grace period: 3 days (teacher-configurable, range 1-7 days)

RECOVERY SESSION (condensed, 15-20 min):
  - Phase 1: EXTENDED Memory Sprint (3 min, 10 questions -- more decay to recover)
  - Phase 2: Condensed Story Mode (key segments only, ~3 min)
  - Phase 3: 1 game break only (2-3 min)
  - Phase 4: SKIPPED (time constraint)
  - Phase 5: Quick flashcard review only (1 min)
  - Phase 6: Full Final Boss (NO shortcuts -- assessment integrity maintained)
  - Phase 7: Shortened reflection (1 prompt)
```

### 12.2 Multiple Missed Sessions

```
IF missed_count > 1:
  1. SORT missed sessions by DEPENDENCY (prerequisites first)
  2. ASSIGN recovery sessions in dependency order
  3. Each recovery session is condensed (see 12.1)
  4. Maximum 2 recovery sessions per day (prevent burnout)
  5. Teacher dashboard shows recovery queue and estimated completion date
```

### 12.3 Extended Absence -- Catch-Up Mode

```
IF absence > 7 days:
  ACTIVATE Catch-Up Mode:
  - AI identifies ESSENTIAL concepts only (prerequisite chain analysis)
  - Non-essential topics deferred until caught up
  - Final Boss: reduced HP (50% of normal), hints allowed without penalty
  - EXIT condition: student completes sessions to within 1 of class position
  - Teacher notified with specific in-class support recommendations
  - Maximum 2 catch-up sessions per day
```

### 12.4 Boost Mode (Falling Behind)

```
IF student_pisa_level < class_average - 0.5 for 3+ consecutive sessions:
  ACTIVATE Boost Mode:
  - Additional optional practice sessions (incentivized with bonus XP + special avatar items)
  - Targeted to specific weak standards and transition skills
  - AI generates personalized improvement plan
  - Parent notified with home support recommendations
  - Teacher receives specific intervention recommendations
  - Auto-deactivate when student reaches class average
```

### 12.5 Low Engagement Intervention

```
IF completion_rate < 50% for 2 consecutive weeks:
  RESPONSE SEQUENCE:
  1. Reduce session length to minimum (15 min)
  2. Increase game-to-content ratio (more Game Breaks, shorter Story Mode)
  3. Re-engage with Quest Arc narrative hooks
  4. Parent notification with specific suggestions
  5. Teacher dashboard flag with engagement data
```

### 12.6 Force Majeure / Technical Failures

```
OFFLINE MODE:
  - Pre-cache current chapter + next chapter content
  - Session auto-save: resume from last checkpoint on reconnection
  - Device-agnostic: session state syncs across devices

TEACHER OVERRIDE:
  - "Excused" marking: manual override for technical issues
  - Removes homework from recovery queue
  - Does not affect PISA tracking or mastery calculations
```

---

## 13. Anti-Cheat System

*Source: Original spec Section 9.5 (more detailed than HOMEWORK_STANDARDS.md's Final-Boss-only anti-cheat).*

```
SYSTEM-WIDE INTEGRITY CHECKS:

1. Question Regeneration: Boss questions regenerated on every attempt
   (same standard + PISA level, different numbers/context)

2. Response Time Analysis: Answers faster than reading speed -> flagged
   (calibrated per student's established reading pace)

3. Session Pattern Analysis: Unusual completion patterns -> flagged
   (e.g., perfect scores on hard questions but failures on easy ones)

4. Socratic Verification: After boss defeat, 1 follow-up question
   to verify understanding (not scored, but flagged if failed)

5. Device Monitoring: Same account on multiple devices -> session locked

6. Copy-Paste Detection: Paste events in text fields -> flagged

7. Radiant Signature Analysis (Buzan) — PENDING EMPIRICAL VALIDATION:
   Concept: Open-text responses checked for "radiant" vs "linear" patterns
   to detect AI-generated or copy-pasted answers.
   STATUS: NOT DEPLOYED. Requires validation before shipping:
   - Collect 500+ real G5-6 student responses across subjects
   - Label them human vs AI-generated
   - Train classifier and measure precision/recall
   - SHIP GATE: precision must be >= 90%. If not, feature does not ship.
   - RISK: Students explaining sequential processes (water cycle, timelines)
     naturally produce linear text — not because they're cheating.
     False positive rate for systematic thinkers may be unacceptable.
   - If validation passes, scope is: Phase 4 + Peer Teaching open-text only
   - NOT applied to: MC, drag-and-drop, closed-format, Math, Language grammar

ESCALATION:
  - Flag 1: Soft warning to student ("Make sure you're solving these yourself!")
  - Flag 2: Parent notification
  - Flag 3: Teacher notification with evidence log
  - Flag 4: Account-level review (admin)
```

---

## 14. Teacher Controls

Teachers can configure per class or per student:

| Control | Default | Range |
|---|---|---|
| Session mode | Standard (20-30 min) | Standard / Extended (40-50 min) |
| Grace period for missed homework | 3 days | 1-7 days |
| Final Boss HP modifier | 100% | 50%-150% |
| Hint availability | Enabled (with XP cost) | Enabled / Disabled |
| Phase 4 (Real-Life Challenge) | Required | Required / Optional |
| Minimum reflection length | 10 characters | 10 chars - 5 sentences |
| Difficulty floor | Student's PISA level - 1 | Configurable |
| Game mechanic selection | Automatic | Auto / Manual selection |
| Recovery sessions per day | 2 max | 1-3 |
| Mandatory vs optional homework | Mandatory | Mandatory / Optional |
| Creative Lab availability | Auto (Level 3+) | Enabled / Disabled |

**Teacher Dashboard Features:**

| Feature | Description |
|---|---|
| Heat Map | Per-student, per-chapter, per-standard mastery visualization |
| Deadline Controls | Set, extend, or waive homework deadlines |
| Custom Assignments | Create assignments using NETS game engine (tagged to standards) |
| Custom Boss Questions | Create boss questions tagged to standards |
| Difficulty Override | Override AI difficulty for specific students |
| Excused Marking | Remove homework from recovery queue |
| Class Insights | Which textbook sections need classroom reinforcement (class-wide weak standards) |
| Engagement Alerts | Students with declining completion or performance |

---

## 15. Integration Points

### 15.1 Kundalik/eMaktab

```
PULL from Kundalik:
  - Class rosters (student list per class)
  - Attendance data (feeds into absence detection)
  - Timetable (homework assigned per subject schedule)

PUSH to Kundalik:
  - Homework completion status (complete / in-progress / missed)
  - Grade equivalent (1-5 scale, derived from boss performance)
  - Completion timestamp
```

### 15.2 Parent Dashboard

```
PARENT PORTAL FEATURES:
  - PISA level progression chart (over time, per subject)
  - Subject performance breakdowns
  - Homework completion rates
  - Weak standards with home support recommendations (specific, actionable)
  - AI-generated home support recommendations
  - Weekly summary (platform notification or SMS for parents without app)

PRIVACY:
  - Reflection Journal content NOT shared (teacher and parent see themes only)
  - Individual question-level data available only to teacher
```

### 15.3 Admin/National Analytics

```
AGGREGATE (anonymized):
  - Per-school average PISA levels by subject
  - Per-region standard mastery rates
  - National content gap analysis (which standards are weakest nationwide)
  - Textbook effectiveness metrics (which chapters have lowest mastery rates)
  - Creative Thinking domain progress (national aggregate)
```

---

## 16. Homework Task JSON Schema

*Source: HOMEWORK_TASK_ENGINE.md Section D. The most comprehensive schema across all sources. Extended with transition_skill field.*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "NETS Homework Task Standard",
  "type": "object",
  "required": ["task_id", "textbook_ref", "curriculum_standard", "pisa_level", "blooms_level", "game_mechanic", "content"],
  "properties": {
    "task_id": {
      "type": "string",
      "pattern": "^HW-[A-Z]+-[0-9]+-[A-Z]+-[0-9]{3}$",
      "description": "Unique task ID. Format: HW-{SUBJECT}{GRADE}-{TOPIC}-{SEQ}",
      "example": "HW-MATH5-FRAC-001"
    },
    "textbook_ref": {
      "type": "object",
      "required": ["grade", "subject", "language", "chapter", "section", "page_range"],
      "properties": {
        "grade": { "type": "integer", "minimum": 1, "maximum": 11 },
        "subject": { "type": "string", "enum": ["math", "reading", "science", "history", "biology", "chemistry", "physics", "geography", "informatics", "english", "uzbek_language", "russian_language"] },
        "language": { "type": "string", "enum": ["uz", "ru"] },
        "chapter": { "type": "string" },
        "section": { "type": "string" },
        "page_range": { "type": "string", "pattern": "^[0-9]+-[0-9]+$" },
        "textbook_isbn": { "type": "string" },
        "textbook_year": { "type": "integer" }
      }
    },
    "curriculum_standard": {
      "type": "object",
      "required": ["primary_code", "alias_code"],
      "properties": {
        "primary_code": {
          "type": "string",
          "pattern": "^UZ-[A-Z]+-[0-9]+-[A-Z]+-[0-9]{2}$",
          "description": "Primary format: UZ-SUBJECT-GRADE-TOPIC-SEQ",
          "example": "UZ-MATH-5-FRAC-01"
        },
        "alias_code": {
          "type": "string",
          "pattern": "^[A-Z]{3}\\.[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$",
          "description": "Backward-compatible dotted format",
          "example": "MAT.5.3.4.1"
        }
      }
    },
    "pisa_level": {
      "type": "object",
      "required": ["target", "domain", "competency", "transition_skill"],
      "properties": {
        "target": { "type": "integer", "minimum": 1, "maximum": 6 },
        "domain": { "type": "string", "enum": ["mathematics", "reading", "science", "creative_thinking"] },
        "competency": { "type": "string", "description": "Specific PISA competency targeted" },
        "transition_skill": {
          "type": "string",
          "description": "MANDATORY. Which Level N->N+1 transition this task supports.",
          "examples": ["L1->L2: extract from simple charts", "L2->L3: sequential decision-making", "L3->L4: select and integrate representations"]
        }
      }
    },
    "blooms_level": {
      "type": "string",
      "enum": ["remember", "understand", "apply", "analyze", "evaluate", "create"]
    },
    "game_mechanic": {
      "type": "object",
      "required": ["mechanic", "format"],
      "properties": {
        "mechanic": {
          "type": "string",
          "enum": ["memory_sprint", "flashcards", "tile_match", "sentence_fill", "memory_palace", "story_mode", "adaptive_quiz", "mystery_box", "movement_breaks", "why_chain", "peer_teaching", "real_life_challenge", "reflection_journal", "final_boss", "creative_lab"]
        },
        "format": { "type": "string", "description": "Specific interaction format" },
        "ui_template_id": { "type": "string" }
      }
    },
    "content": {
      "type": "object",
      "required": ["question_text", "language", "answer"],
      "properties": {
        "question_text": { "type": "string", "description": "Question in target language (uz or ru)" },
        "question_text_secondary": { "type": "string", "description": "Question in secondary language if bilingual" },
        "language": { "type": "string", "enum": ["uz", "ru"] },
        "media": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": { "type": "string", "enum": ["image", "audio", "video", "animation", "diagram"] },
              "url": { "type": "string", "format": "uri" },
              "alt_text": { "type": "string" }
            }
          }
        },
        "answer": {
          "type": "object",
          "properties": {
            "correct": { "description": "Correct answer (string, number, array, or object)" },
            "format": { "type": "string", "enum": ["exact", "numeric_range", "multiple_choice", "matching_pairs", "ordered_list", "open_rubric"] },
            "rubric": { "type": "string", "description": "For open-ended: scoring rubric" },
            "common_errors": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "error": { "type": "string" },
                  "misconception": { "type": "string" },
                  "remediation_hint": { "type": "string" }
                }
              }
            }
          }
        },
        "hint_chain": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Progressive hints (not available in Final Boss)"
        }
      }
    },
    "difficulty": {
      "type": "object",
      "properties": {
        "irt_theta": { "type": "number", "description": "IRT difficulty parameter (-3 to +3)" },
        "estimated_minutes": { "type": "number", "minimum": 0.25, "maximum": 10 },
        "cognitive_load": { "type": "string", "enum": ["low", "medium", "high"] }
      }
    },
    "prerequisites": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of curriculum_standard primary codes that must be mastered first",
      "example": ["UZ-MATH-4-DIV-03", "UZ-MATH-5-FRAC-01"]
    },
    "session_placement": {
      "type": "object",
      "properties": {
        "journey_step": { "type": "integer", "minimum": 1, "maximum": 7 },
        "step_name": { "type": "string", "enum": ["memory_sprint", "story_mode", "game_breaks", "real_life_challenge", "consolidation", "final_boss", "reflection"] }
      }
    },
    "ai_tier": {
      "type": "integer",
      "enum": [1, 2, 3],
      "description": "1=template/open-source, 2=mid-range (Haiku), 3=premium (Sonnet/Opus)"
    },
    "xp_reward": {
      "type": "object",
      "properties": {
        "base": { "type": "integer" },
        "streak_bonus": { "type": "integer" },
        "speed_bonus": { "type": "integer" },
        "combo_multiplier": { "type": "number" }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {
        "created_at": { "type": "string", "format": "date-time" },
        "created_by": { "type": "string", "enum": ["human_teacher", "ai_tier1", "ai_tier2", "ai_tier3"] },
        "reviewed_by": { "type": "string" },
        "review_status": { "type": "string", "enum": ["draft", "ai_generated", "teacher_reviewed", "approved", "deprecated"] },
        "usage_count": { "type": "integer" },
        "avg_accuracy": { "type": "number" },
        "avg_time_seconds": { "type": "number" },
        "version": { "type": "integer" }
      }
    }
  }
}
```

---

## 17. Grade-Level Implementation Matrix

### 17.1 Game Availability by Grade

| Game | Grades 1-2 | Grades 3-4 | Grades 5-6 | Grades 7-8 | Grades 9-11 |
|---|---|---|---|---|---|
| Memory Sprint | Simplified (4 Qs) | Standard | Standard | Standard | Standard |
| Story Mode | Heavy visuals | Balanced | Balanced | Text-heavy | Text-heavy |
| Tile Match | 4 pairs | 6 pairs | 6-8 pairs | 8 pairs | 8 pairs |
| Sentence Fill | Word bank (full) | Word bank (full) | Word bank (partial) | No word bank | No word bank |
| Memory Palace | Not available | Intro (3 items) | Full (5 items) | Full | Full |
| Flashcards | Simple | Standard | Standard | Standard | Self-directed |
| Adaptive Quiz | Simplified | Standard | Standard | IRT-calibrated | IRT-calibrated |
| Mystery Box | Not available | 3 boxes | 3-5 boxes | 5 boxes | 5 boxes |
| Movement Breaks | REQUIRED | REQUIRED | Optional | Disabled | Disabled |
| Why Chain | 2 levels | 3 levels | 3-4 levels | 4-5 levels | 5+ levels |
| Peer Teaching | Not available | Not available | Available | Available | Available |
| Real-Life Challenge | Simplified | Standard | Standard | Extended | Extended |
| Final Boss | 50 HP, MC | 50 HP, MC | 100 HP, mixed | 100 HP, open | 150 HP, open |
| Reflection Journal | 1 prompt, verbal | 1 prompt | 2 prompts | 2 prompts | 3 prompts |
| Creative Lab | Not available | Not available | Available (L3+) | Available (L3+) | Available (L3+) |

### 17.2 Session Duration by Grade

| Grade Band | Standard Mode | Extended Mode | Recovery Mode |
|---|---|---|---|
| Grades 1-2 | 15-20 min (+ 3-5 min optional pre-session) | 30 min | 10-15 min |
| Grades 3-4 | 20-25 min (+ 3-5 min optional pre-session) | 35-40 min | 15-20 min |
| Grades 5-8 | 20-30 min (+ 3-5 min optional pre-session) | 40-50 min | 15-20 min |
| Grades 9-11 | 25-30 min (+ 3-5 min optional pre-session) | 45-50 min | 20-25 min |

**Note:** Pre-session overhead (Theme Preview §4.4 + Flash Cards §4.5) is student-paced, optional but recommended, and does not count toward XP or assessment scoring.

---

## 18. AI Refinement Constraints

*Source: Gap analysis (Raphael) Flag 1 -- "AI Refinement" stage lacks inline constraints. This section defines the explicit boundaries of what AI can and cannot do.*

### 18.1 Permissible AI Operations

AI Refinement IS limited to:
- **Formatting:** Restructuring textbook content for digital display
- **Narrative framing:** Wrapping concepts in character-driven stories with Uzbek cultural context
- **Cultural contextualization:** Adding Uzbek names, locations, scenarios, currency
- **Difficulty scaffolding:** Adjusting question complexity within the same concept
- **Question generation:** Creating new questions that test the same concepts as textbook exercises
- **Visual generation:** Creating diagrams, bar models, and visual representations of textbook concepts
- **Translation:** Converting between Uzbek and Russian while preserving meaning

### 18.2 Prohibited AI Operations

AI Refinement MUST NOT:
- Alter factual claims, mathematical formulas, or scientific laws
- Modify historical dates, geographical information, or biographical facts
- Change grammar rules or vocabulary definitions
- Simplify in ways that remove essential meaning or prerequisite knowledge
- Introduce content beyond textbook scope for the given grade
- Generate questions that test concepts not covered in the textbook
- Create cultural references that are inaccurate or inappropriate
- Produce content that contradicts the national curriculum

### 18.3 CS Curriculum Exception

*Source: Gap analysis (Raphael) Flag 2.*

**Exception -- Computer Science:** Where MoEN-approved CS textbooks do not yet cover topics in the NETS CS progression (e.g., Python/JavaScript for Grades 7-9, AI/ML concepts for Grades 10-11), these topics are NETS-supplemented content. This exception to the textbook-source-of-truth principle is explicitly acknowledged and should be reviewed annually as textbooks are updated. CS-supplemented content must still comply with all other tagging, PISA calibration, and review requirements.

---

## 19. Bilingual Language Acquisition Framework

*Source: Gap analysis (Donatello) identified this as a major missing element from HOMEWORK_STANDARDS.md. The research paper specified a complete CEFR/IELTS progression.*

### 19.1 Language Progression by Grade

| Grade | English Target (CEFR) | Russian/Uzbek L2 Target | Primary NETS Games |
|---|---|---|---|
| 1-2 | Pre-A1 | N/A (L1 focus) | Flashcards (vocab), Movement Breaks (TPR), Tile Match (word-image) |
| 3-4 | A1 | Pre-A1 (if applicable) | Sentence Fill (grammar), Story Mode (comprehension), Flashcards |
| 5-6 | A1-A2 | A1 | Sentence Fill, Why Chain (simple discourse), Story Mode (immersive) |
| 7-8 | A2-B1 | A1-A2 | All mechanics in target language, Why Chain (discourse analysis) |
| 9-11 | B1-B2 | A2-B1 | Full immersion mode, Peer Teaching in L2, Real-Life in L2 |

### 19.2 Language Learning Methodology

- **Krashen's Input Hypothesis (i+1):** Content delivered at one level above student's current comprehension, with L1 support available on demand
- **Content-Based Instruction:** Language learned through subject matter, not isolated grammar drills
- **Game mechanic mapping:** Sentence Fill for vocabulary/grammar, Story Mode for reading comprehension, Why Chain for discourse analysis, Peer Teaching for productive fluency

### 19.3 Implementation

- All content exists in both `uz` and `ru` languages
- Student's preferred language is primary; toggle available for bilingual students
- English/Russian L2 content follows CEFR progression
- L1 support (hover translation, vocabulary glossary) always available, costs no XP

---

## 20. Research Citations and Evidence Base

| # | Mechanic/Principle | Citation | Key Finding |
|---|---|---|---|
| 1 | Method of Loci | Maguire, E.A., et al. (2003). "Routes to remembering." Nature Neuroscience. | 300% retention improvement |
| 2 | Dual Coding | Paivio, A. (1986). "Mental Representations." | Visual + verbal = better memory |
| 3 | Forgetting Curve | Ebbinghaus, H. (1885). "Memory: A Contribution to Experimental Psychology." | Exponential decay without review |
| 4 | Retrieval Practice | Roediger, H.L. & Karpicke, J.D. (2006). "Test-enhanced learning." Psychological Science. | Active recall > re-reading (3x) |
| 5 | Interleaving | Rohrer, D. & Taylor, K. (2007). "The effects of overlearning and distributed practice." | 43% better transfer |
| 6 | Elaborative Interrogation | Pressley, M., et al. (1992). "Metacognition in early reading." | "Why?" questions deepen understanding |
| 7 | Flow Theory | Csikszentmihalyi, M. (1990). "Flow: The Psychology of Optimal Experience." | Challenge-skill balance = optimal learning |
| 8 | Self-Determination Theory | Deci, E.L. & Ryan, R.M. (2000). "The psychology of self-determination." | Autonomy, competence, relatedness |
| 9 | Narrative Retention | Willingham, D.T. (2004). "Ask the Cognitive Scientist." | 22x better retention with story |
| 10 | Cloze Testing | Taylor, W.L. (1953). "Cloze procedure: A new tool for measuring readability." | Reliable comprehension measure |
| 11 | Phenomenon-Based Learning | Silander, T. (2015). "Phenomenal Learning from Finland." | Cross-subject transfer skills, +1-2 PISA levels |
| 12 | Metacognition | Flavell, J.H. (1979). "Metacognition and cognitive monitoring." | Reflection improves performance 20-30% |
| 13 | Protege Effect | Chase, C.C., et al. (2009). "The protege effect." | Teaching deepens learning +25% |
| 14 | Embodied Cognition | Barsalou, L.W. (2008). "Grounded cognition." | Movement enhances learning +15-20% |
| 15 | Productive Struggle | Stigler, J. & Hiebert, J. (1999). "The Teaching Gap." | Struggle leads to deeper learning, +2 PISA sub-levels |
| 16 | Singapore CPA | Leong, Y.H., et al. (2015). "Concrete-Pictorial-Abstract approach." | Structured progression for mathematical understanding |
| 17 | Item Response Theory | Lord, F.M. (1980). "Applications of Item Response Theory." | Adaptive testing precision |
| 18 | PISA 2022 Framework | OECD (2023). "PISA 2022 Results Volume I." | International assessment standards |
| 19 | Creative Thinking | OECD (2024). "PISA 2022 Results Volume III: Creative Minds, Creative Schools." | Creative thinking assessment framework |

**PISA Data Sources:**
- OECD PISA 2022 Results Volume I -- What Students Can Do
- NCES PISA 2022 Mathematics Proficiency Level Descriptions
- NCES PISA 2022 Reading Proficiency Level Descriptions
- NCES PISA 2022 Science Proficiency Level Descriptions
- ACER Teacher's Guide to PISA Mathematics
- PISA 2022 Mathematics Framework

---

## Appendix A: Session Completion and Data Flow

### A.1 Completion Requirements

A homework session is COMPLETE only when ALL phases are finished:
- Phase 1: Memory Sprint completed (all questions attempted)
- Phase 2: All Story Mode segments viewed, all checkpoints passed
- Phase 3: All assigned game breaks completed
- Phase 4: Real-Life Challenge submitted (or skipped for below-L2 students)
- Phase 5: Consolidation exercise completed
- Phase 6: Final Boss DEFEATED (HP reduced to 0)
- Phase 7: Reflection written (minimum length met)

**There is no partial completion.** A student either finishes the full session or it remains in-progress.

### A.2 Data Pushed After Session

```json
{
  "student_id": "...",
  "homework_id": "...",
  "subject": "mathematics",
  "chapter": "Oddiy kasrlar",
  "standards_covered": ["UZ-MATH-5-FRAC-01", "UZ-MATH-5-FRAC-04", "UZ-MATH-5-FRAC-06"],

  "pisa_performance": {
    "items_by_level": { "L1": "3/3", "L2": "4/5", "L3": "1/2" },
    "estimated_level_change": "+0.1",
    "new_estimated_level": 1.8,
    "transition_skills_demonstrated": ["L1->L2: interpret visual representations"]
  },

  "blooms_performance": {
    "remember": "100%",
    "understand": "90%",
    "apply": "80%",
    "analyze": "50%"
  },

  "weak_standards": ["UZ-MATH-5-FRAC-06"],
  "boss_attempts": 1,
  "boss_difficulty_tiers": { "easy": "3/3", "medium": "2/3", "hard": "0/1" },
  "mastery_stars": 3,
  "xp_earned": 2450,
  "time_spent": "24:17",

  "grade_equivalent": 4,

  "flags": [],

  "parent_summary": "Jasur bugungi matematika uy vazifasini muvaffaqiyatli tugatdi. Kasrlar mavzusida 3 yulduz oldi. Tahlil qilish ko'nikmalarida qo'shimcha mashq foydali bo'ladi."
}
```

### A.3 System Architecture Summary

```
TEXTBOOK (source of truth)
    |
NATIONAL STANDARD (every item tagged: UZ-MATH-5-FRAC-01)
    |
PISA LEVEL (every item calibrated: Level 2, transition L1->L2)
    |
CONTENT POOL (AI-generated, expert-reviewed, IRT-calibrated)
    |
HOMEWORK ENGINE (7-phase session, 20-30 min)
    |
STUDENT PERFORMANCE (per-standard, per-PISA-level, per-transition-skill)
    |
ADAPTIVE RESPONSE (difficulty adjustment, recovery, boost)
    |
TEACHER/PARENT VISIBILITY (dashboards, recommendations)
    |
NATIONAL ANALYTICS (aggregate PISA trajectory for 8.8M students)
```

**Every question a student sees can be traced back to:**
1. A specific textbook page (source)
2. A specific national curriculum standard code (reference)
3. A specific PISA proficiency level and transition skill (assessment)
4. A specific Bloom's taxonomy level
5. A specific game mechanic with research backing

**Nothing is arbitrary. Nothing is disconnected. Everything is referenced.**

---

## Appendix B: Source Reconciliation Log

Where source documents conflicted, this log records which version was chosen and why.

| Topic | Original Spec | HOMEWORK_STANDARDS.md | TASK_ENGINE.md | Unified Decision | Rationale |
|---|---|---|---|---|---|
| Session duration | 50 min default | 20-30 min default | 20-30 min | **20-30 min** (50 min as Extended) | More practical for homework; 50 min kept as teacher-override |
| Standard code format | MAT.5.1.3.2 (dotted) | Not specified | UZ-MATH-5-FRAC-01 (descriptive) | **Dual format** (descriptive primary, dotted alias) | Descriptive is more readable; dotted kept for backward compat |
| Final Boss PISA level | Not tiered (mixed L1-above) | Level 3-4 | Level 3-5 | **Level 3-6 (tiered)** | Leonardo's analysis: must be tiered to cover full PISA range |
| Reflection Journal PISA | Not specified | Level 6 | Level 3-4 | **Level 3-4** | Reflection is metacognitive, not PISA L6 advanced reasoning |
| XP per Memory Sprint correct | 10 XP | 100 XP | 100 XP | **100 XP** | Supports gamification economy; 10 XP too low for engagement |
| Flow threshold (difficulty adjustment) | 3 consecutive correct/2 wrong | <60%/>90%/70-80% | Not specified | **Both** (percentage primary, consecutive secondary) | Percentage more robust; consecutive catches edge cases |
| Game count | 12 + Memory Palace embedded | 14 (Memory Palace standalone) | 14 | **14** (Memory Palace standalone) | Memory Palace is distinct enough for standalone mechanic status |
| Reading/Science progression | Complete (Math only) | Placeholder stubs | Defined by level | **Complete matrices** (filled from gap analysis templates) | Critical gap -- 2 of 3 PISA domains cannot be stubs |
| Creative Thinking | Not addressed | Not addressed | Not addressed | **New Section 8** | PISA 2022 assessed it; Uzbekistan scored 14/60; cannot ignore |
| Edge cases/recovery | Full (Sections 9.1-9.4) | Missing | Not addressed | **Full (from original spec)** | Daily reality for 8.8M students; cannot omit |
| AI Refinement constraints | Not addressed | DO/DON'T rules only | Not addressed | **Explicit Section 18** | Raphael's flag: must define what AI can/cannot do inline |
| CS exception | Not addressed | Not addressed | Not addressed | **Documented in Section 18.3** | Raphael's flag: CS may exceed textbook scope |
| Leaderboard/Avatar | Not specified | Mentioned in passing | Not addressed | **Full spec (Section 11.5-11.6)** | Donatello's gap: core gamification needs dedicated spec |
| Bilingual framework | Not specified | Not specified | Not addressed | **New Section 19** | Donatello's gap: language learning is core subject |

---

---

## Future: Reading Fluency Module (Buzan Speed Reading — Deferred)

**Status:** NOT part of the Core Injection. Deferred to a standalone module for G9+ or once empirical validation confirms benefit for younger learners.

**Why deferred:** G5 students read at Lexile 830-1010L and struggle with multi-clause sentences, idioms, and inference. Their bottleneck is COMPREHENSION, not speed. Rayner et al. (2016, *Psychological Science in the Public Interest*) found that speed reading training does not improve comprehension — it teaches skimming. Buzan's speed reading techniques were designed for adult readers who regress out of habit. G5-6 students who re-read are building understanding, not wasting time. Applying these methods prematurely would harm learning outcomes.

**Methods captured here for future implementation:**

| Method | What It Does | Why Deferred | When It May Apply |
|---|---|---|---|
| **#16 Focus Guide (Fixation Training)** | Highlight bar moves across text in 3-5 word chunks, 5-10% faster than reading speed | Pushes past sub-vocalization — but G5 students NEED sub-vocalization to comprehend complex text | G9+ when reading fluency is established and the bottleneck shifts from comprehension to speed |
| **#21 Sub-vocalization Elimination** | Pacer moves faster than inner-voice speed (~150 WPM) to break the habit of "hearing" every word | Sub-vocalization is a comprehension AID at G5-6, not a speed limiter | G9+ or advanced readers identified by reading speed data |
| **#23 Meta-Guiding** | Visual guide maintains steady reading rhythm, reduces eye strain | Merged with Focus Guide — same deferral reason | Same as Focus Guide |
| **#18 Forward Momentum Rule** | Previous Story Mode segment fades after advancing; back-navigation requires deliberate button press | Regression is a LEGITIMATE comprehension strategy. For process-heavy subjects (Texnologiya, Science), re-reading is often NECESSARY. Buzan was optimizing for adults, not developing readers. | G9+ only, where reading habits are established and regression is genuinely habitual rather than strategic |
| **#17 Saccade Optimization** | Column width 50-75 chars (66 ideal) to optimize eye-jump distance | Good typography practice but belongs in a general UI/UX spec, not Buzan injection | **ADOPTED** — typography rules from Buzan research adopted as UI defaults in `standards/system/ui-ux/` |
| **#19 Peripheral Vision Training** | Line height 1.5x, sans-serif font to support peripheral word recognition | Same as saccade optimization — good typography, not a Buzan-specific injection | **ADOPTED** — same as #17, part of UI defaults |
| **#20 Semantic Chunking** | Wider gaps between 3-5 word groups in Story Mode text for G5-6 | Potentially useful but needs A/B testing — no evidence that visual chunking helps comprehension for Uzbek-language text specifically | After A/B test confirms benefit for Uzbek readers |

**Validation path:** If this module is revisited, the team should:
1. Run a controlled A/B test with 200+ G9-11 students (Focus Guide ON vs OFF)
2. Measure: reading speed (WPM), comprehension accuracy (checkpoint scores), and student preference
3. Only ship if comprehension is maintained or improved, not just speed increased
4. For G5-8: do NOT ship without separate validation showing no comprehension harm

---

**END OF UNIFIED SPECIFICATION**

*This document is the single authoritative specification for the NETS Homework Engine.*
*All previous versions are superseded.*
*Engineering and content teams build exclusively from this document.*

**Version:** 2.0 (Buzan-Injected)
**Date:** April 2, 2026
**Buzan Injection Date:** April 2026
**Status:** Single Source of Truth
