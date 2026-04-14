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
| `recall_item` | Quick-fire question from previous chapters | Phase 1: Memory Sprint | Textbook |
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
|  P1  MEMORY SPRINT -------- 2 min ----- [flexible format, prior]    |
|   |    +-- MC / Speed Match / Flash Sprint / Fill-Blanks / Order     |
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
   - Phase 1: 5-8 recall_items from PREVIOUS chapters (spaced repetition algo)
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

| # | Component | What It Delivers |
|---|---|---|
| 1 | **Summary of Book Content** | A cleaner, more digestible reframing of what the textbook chapter covers. Plain language, better visual hierarchy. NOT a rewrite — a refocusing. |
| 2 | **Better Explanation** | Concepts the textbook assumes the student understands, clarified. Fills the gap between textbook language and student comprehension. |
| 3 | **Examples** | Additional worked examples beyond what the textbook provides, showing the concept in action step-by-step. |
| 4 | **Real-Life Research** | The origin story of the concept. Who discovered it? What problem did it solve? What changed in the world because of it? |
| 5 | **Personal Hook** | First-person address connecting topic to student's own life. "Remember when you saw...?" / "Maybe you've wondered why...?" |
| 6 | **Why This Matters** | Explicit statement of real-world relevance — not "it's on the exam" but genuine why-you-need-this. |
| 7 | **Industry Application** | How this concept is used in real industries, jobs, and technology. Shows career relevance. |
| 8 | **Additional Materials** | Curated external resources (videos, articles, simulators). Language does NOT matter — English, Russian, or Uzbek all permitted. Student picks the language they prefer. |

**Design Rules:**
- **No quiz, no pressure.** Exploration mode. There are no answers to give, so there are no wrong answers.
- **Student-paced.** No timer. Student scrolls/clicks at their own speed. May skip components.
- **Visual-first.** Diagrams, photos, short video clips preferred over walls of text.
- **First-person POV throughout.** "You" not "the student". Direct address, never third-person.
- **Ends with explicit transition** to Flash Cards: *"Before we start — here are the key ideas you'll need."*

**Why this exists:** Demos showed students felt dropped into homework cold. The original framework assumed the student arrives prepared. Theme Preview closes the gap between *reading the textbook* and *doing the homework* — that's where engagement was dying.

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

**Design Rules:**
- **One concept per card.** No cramming multiple ideas into a single card.
- **Swipeable / scrollable.** Student flips through at their own pace.
- **No testing here.** Reference, not assessment. No right/wrong.
- **Returnable during homework.** A "Flash Cards" button is available throughout the homework session — quick-access overlay. NOT a hint (no penalty), just a reference.
- **Ends with the "Start my Homework" button.** This is the explicit gateway into the 7-phase engine. Only after this press does the session timer start and XP accrue.

---

## 5. Phase Specifications

### 5.1 Phase 1 -- Memory Sprint (2 minutes)

**Purpose:** Activate prior knowledge. Prevent memory decay. Connect old learning to new. Deliver quick dopamine to warm the student into the session.

**UPDATED 2026-04-07:** Memory Sprint is no longer locked to "single-answer recall". The original spec was too narrow and led content creators to produce typed quiz questions only. The intent was *warm up the brain* — any fast-paced format that hits prior chapters in ≤2 min is now permitted.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | ≤2 minutes (hard cap) | ≤2 minutes |
| Item count | 5-8 items | 8-10 items |
| Source | Previous chapters in same subject (NOT current topic) | Same |
| Format | **Flexible — any approved fast format (see table below)** | Same |
| Hints allowed | No | No |
| AI Tier | Tier 1 (pre-generated pool) | Same |

**Approved Memory Sprint Formats:**

| Format | Description | Best For |
|---|---|---|
| **Quick MC / Binary** | 5-8 tap-to-answer questions from prior chapters | All subjects |
| **Speed Match** | Drag-and-drop matching: term ↔ definition, formula ↔ result | Math, Science |
| **Flash Sprint** | Rapid-fire flashcards — student swipes "Know" or "Review" | Biology, History |
| **Fill-in-Blanks Race** | Complete 5 sentences with missing keywords, timed | Language, Science |
| **Order the Steps** | Arrange process steps in correct order (drag-and-drop) | Science, Math procedures |

**Format Selection Rule:** Content creator chooses the format that best fits the subject and prior chapter content. All formats must have a Start button, instant per-item feedback, streak/combo bonuses, and a final score display. Mixing formats within a single Sprint is permitted.

**Item Selection Algorithm:**
```
1. GET all recall_items from chapters BEFORE the current chapter
2. PRIORITIZE by forgetting curve:
   - Items the student got WRONG in previous sessions -> highest priority
   - Items approaching forgetting threshold (Ebbinghaus model) -> high priority
   - Items answered correctly but not seen in 7+ days -> medium priority
3. FILTER to 5-8 items, balanced across prior chapters
4. RANDOMIZE order
```

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
4. SELECT 3 game mechanics:
   - At least 1 matching the student's CURRENT Bloom's level (reinforcement)
   - At least 1 one level ABOVE (stretch)
   - At least 1 targeting a current transition skill
   - Subject-appropriate mechanics only (see Game Mechanic Decision Table)
5. LOAD pre-generated game_items tagged to THIS topic's standard_ref
6. CONSTRAINT: No mechanic appears more than 2x in one session
7. ARRANGE interleaved with Story Mode segments
```

### 5.4 Phase 4 -- Real-Life Challenge: Transfer Application (3-5 min standard / 10 min extended)

**Purpose:** Force transfer -- apply textbook knowledge to a real-world scenario. This is the core skill PISA measures.

**UPDATED 2026-04-07 — First-Person Expert POV is mandatory.** All four AI demos used third-person scenarios ("Tomir's plant is dying", "Salimjon is in his garage"). Students were observers, not decision-makers. Every Real-Life Challenge must now put the student in the role of THE EXPERT who must solve a real case.

| Element | Requirement |
|---|---|
| **POV** | Direct address: "You are..." / "Your job is..." / "A client comes to you..." Never third-person. |
| **Role** | Student is positioned as an expert — fire safety inspector, scientist, engineer, consultant, doctor, lawyer, historian — NOT as a student answering a textbook question. |
| **Case** | Preferably a real-world case (historical incident, documented event, known engineering challenge). If not available, a realistic hypothetical that could plausibly occur. |
| **Tricky Questions** | Multiple-path questions with plausible wrong answers (distractors that look right to a novice). Forces real reasoning, not pattern matching. |
| **Explanation Required** | Student must justify their choice. AI evaluates the reasoning, not just the choice. ("What would you do AND why?") |
| **Subject Integration** | All reasoning must use concepts from the current lesson. No outside knowledge required. |

**Examples:**

> ❌ OLD (Kimyo / Combustion): *"Salimjon's garage has petrol. Should he light the stove?"*
> ✅ NEW: *"You are a fire safety inspector called to a workshop. The owner stores gasoline, uses a wood-burning stove, and keeps an asbestos fire blanket in the corner. He asks: 'Is my setup safe?' You look around and immediately spot 3 problems. What are they, and what do you tell the owner?"*

> ❌ OLD (Algebra / Linear Functions): *"A taxi charges 2000 + 1500 per km. Calculate the cost for 5 km."*
> ✅ NEW: *"You are advising a city council on taxi pricing regulation. Two companies propose different pricing models. Company A: 2000 base + 1500/km. Company B: 3000 base + 1000/km. At what distance does Company B become cheaper? A commuter claims Company B is always better — is this true? Write your recommendation."*

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 3-5 minutes | 10 minutes |
| Scenario count | 1 scenario, 2-3 sub-questions | 1 scenario, 3-5 sub-questions |
| Context | Uzbek cultural context (bazaars, travel, family, local industry) | Same |
| AI Tier | Tier 2 (AI-generated, expert-reviewed) | Same |
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

**Purpose:** Lock key concepts into long-term memory before the high-stakes boss fight.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 2-3 minutes | 5 minutes |
| Technique selection | Based on grade level and content type | Same |
| AI Tier | Tier 1 (pre-generated) | Same |

**Technique Selection by Grade:**

| Grade Band | Available Techniques |
|---|---|
| 1-2 | Chunking, Rhymes, Songs |
| 3-4 | Memory Palace intro, Acronyms, Dual coding |
| 5-7 | Full Memory Palace (Loci), Peg system, Mind maps |
| 8-9 | Spaced retrieval mastery, Exam technique mnemonics |
| 10-11 | Self-directed systems, Autonomous consolidation |

**Memory Palace Default Setting:** Registan Square (Samarkand) -- with options for student's home, school building, or local bazaar.

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

**Failure Flow:**
```
IF boss NOT defeated (HP > 0 after all questions):
  1. IDENTIFY which learning objectives the student failed on
  2. MAP failures back to specific textbook sections and standards
  3. ACTIVATE Socratic Tutoring (Tier 3 AI):
     - AI asks guiding questions, NEVER gives answers
     - Routes student back to the SPECIFIC Story Mode segment they need
  4. REGENERATE boss questions (same standards, different numbers/context)
  5. Student re-attempts boss

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

**AI Prompt Generation:**
```
IF accuracy >= 80%:
  -> "What strategy helped you succeed today?"
IF accuracy 60-79%:
  -> "What was challenging? How did you work through it?"
IF accuracy < 60%:
  -> "What would help you understand this better?"

IF hesitation detected on concept X:
  -> "Question 3 seemed tricky. What made it difficult?"

IF streak >= 5:
  -> "You had a [X]-question streak! What was your focus?"
```

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

## 6. 14 Game Mechanics Specification

### 6.1 Complete Game Mechanics Decision Table

*Source: HOMEWORK_TASK_ENGINE.md provides the most accurate Bloom's/PISA mapping. HOMEWORK_STANDARDS.md matrix was inconsistent with source docx on Final Boss and several others. This table is the unified resolution.*

| # | Name | Bloom's Level | PISA Level | Best Content Type | AI Tier | Research Citation | Expected Gain |
|---|---|---|---|---|---|---|---|
| 1 | Memory Sprint | Remember | 1 | Facts, formulas, dates | Tier 1 | Retrieval Practice (Roediger & Karpicke, 2006) | Automaticity |
| 2 | Spaced Flashcards | Remember | 1 | Vocabulary, definitions, formulas | Tier 1 | Forgetting Curve (Ebbinghaus, 1885) | +50-70% retention |
| 3 | Tile Match | Understand | 1-2 | Concept-visual pairing, term matching | Tier 1 | Dual Coding (Paivio, 1986) | +25-40% recognition |
| 4 | Sentence Fill | Understand | 2 | Grammar, cloze comprehension, formulas | Tier 1 | Cloze Testing (Taylor, 1953) | +35% vocabulary |
| 5 | Memory Palace | Remember | 1-2 | Sequential facts, processes, timelines | Tier 1 | Method of Loci (Maguire et al., 2003) | +300% retention |
| 6 | Story Mode | Understand | 2-3 | New concept introduction with narrative | Tier 2 | Narrative Retention (Willingham, 2004) | 22x better retention |
| 7 | Adaptive Quiz | Apply | 2-3 | Multi-step problems, IRT-calibrated | Tier 1 | Item Response Theory | +30% measurement accuracy |
| 8 | Mystery Box | Apply/Analyze | 3 | Interleaved problem-type identification | Tier 1 | Interleaving (Rohrer & Taylor, 2007) | +43% transfer |
| 9 | Movement Breaks | Apply | 1-2 | Kinesthetic concept reinforcement (K-4) | Tier 1 | Embodied Cognition (Barsalou, 2008) | +15-20% retention |
| 10 | Why Chain | Analyze | 3-4 | Causal reasoning, science explanation | Tier 2 | Elaborative Interrogation (Pressley et al., 1992) | +2 PISA sub-levels |
| 11 | Peer Teaching | Evaluate | 4-5 | Explaining concepts to classmates | Tier 1 | Protege Effect (Chase et al., 2009) | +25% for mentors |
| 12 | Real-Life Challenge | Evaluate | 4-5 | Uzbek-context applied problem solving | Tier 2 | Phenomenon-Based (Silander, 2015) | +1-2 PISA levels |
| 13 | Reflection Journal | Create | 3-4 | Metacognitive self-assessment | Tier 1 | Metacognition (Flavell, 1979) | +20-30% performance |
| 14 | Final Boss | Apply/Create (tiered) | 3-6 | Synthesis problem, HP system, **3-tier (Sub/Big/Mythical) — see §5.6** | Tier 3 | Productive Struggle (Stigler & Hiebert, 1999) | +2 PISA levels in 6mo |
| 15 | **Tic Tac Toe vs AI** *(NEW 2026-04-07)* | Remember/Apply | 2-3 | Recall-heavy content where strategic stakes make practice feel like a duel | Tier 1 (questions) + game-AI engine | Game-Based Learning (Gee, 2003) — combines familiar game with content recall | +20-30% engagement on recall tasks |
| 16 | **Notebook Capture** *(NEW 2026-04-07)* | Apply/Analyze/Create | 2-5 | Hand-written derivations, diagrams, sketches, geometric constructions, lab observations, essay drafts | Tier 3 (multimodal vision evaluation) | Generation Effect (Slamecka & Graf, 1978) + Embodied Cognition (Kiefer & Trumpp, 2012) — physical writing/drawing improves retention by 25-40% over typing | +25-40% retention vs. digital input |

**Key changes from previous versions:**
- Final Boss: Changed from "Level 3-4" to "Level 3-6 (tiered)" -- resolves the contradiction between HOMEWORK_STANDARDS.md (L3-4) and source docx (L5-6). Boss questions are now explicitly tiered by PISA level. **As of 2026-04-07, also split into Sub / Big / Mythical tiers (§5.6).**
- Reflection Journal: Changed from "Level 6" to "Level 3-4" -- reflection is metacognitive, not the advanced reasoning PISA L6 requires.
- Memory Palace: Listed as standalone mechanic #5 (was embedded in Mnemonic Lock in original spec).
- **Mystery Box:** Reworked 2026-04-07 from a simple interleaving question into a *case-opening event* with a performance-weighted reward pool. See §6.3 for full specification.
- **Tic Tac Toe vs AI:** New mechanic #15 added 2026-04-07. Full game rules in §6.4.

### 6.2 Detailed Game Specifications

#### Game 1: Tile Match

**Purpose:** Visual-verbal association for rapid concept recognition

```
MECHANICS:
1. Grid displays 8-12 face-down tiles (4-6 pairs)
2. Click first tile -> reveals content
3. Click second tile -> reveals content
4. IF match: tiles animate (fade out), +100 XP, timer +3 seconds bonus
5. IF no match: tiles shake (3x, 100ms), return face-down, timer -5 seconds
6. WIN: All pairs matched before timer = 0
7. LOSS: Timer reaches 0 with pairs remaining -> partial XP (50 per completed pair)

TIMER: 2:30 (visible countdown), max 3:00 with bonuses
XP: Perfect = 300 XP | Partial = 100-250 XP

DIFFICULTY BY GRADE:
  Grades 1-2: 4 pairs, 3:00 timer
  Grades 3-4: 6 pairs, 2:30 timer
  Grades 5-8: 6-8 pairs, 2:30 timer
  Grades 9-11: 8 pairs, 2:00 timer

ACCESSIBILITY:
  - Color-blind mode: Add patterns in addition to colors
  - Screen reader: Announce tile position and content
  - Motor impairment: Extended timer option (+30 seconds)
```

**Subject Examples:**

Mathematics (Fractions): Tile A: "1/2" <-> Tile B: [Visual: 1 of 2 parts shaded]
Science (Photosynthesis): Tile A: "Chloroplast" <-> Tile B: [Diagram with chloroplast highlighted]
Reading (Literary Devices): Tile A: "Metaphor" <-> Tile B: "The classroom was a zoo"

#### Game 2: Spaced Flashcards

**Purpose:** Long-term retention through spaced repetition algorithm

```
SPACING ALGORITHM (SM-2 Modified):

Initial State:
  - Card deck: 10-20 cards from previous chapters
  - Each card has: ease_factor (default 2.5), interval (days), repetitions

Player Sees Card -> Thinks of answer -> Flips card (self-paced)

Player Self-Rates:
  - "Again" (wrong)     -> interval = 0, ease_factor -= 0.2
  - "Hard" (difficult)   -> interval = interval x 1.2, ease_factor -= 0.15
  - "Good" (correct)     -> interval = interval x 2.5, ease_factor unchanged
  - "Easy" (effortless)  -> interval = interval x 3.5, ease_factor += 0.15

CARDS PER SESSION: 5-10
TIMER: 2-3 minutes
XP: 50 XP per correct recall
```

#### Game 3: Memory Sprint

See Phase 1 specification (Section 5.1). Used as both standalone game mechanic and session warm-up.

#### Game 4: Sentence Fill (Cloze Test)

```
BLANK SELECTION RULES:
  - Remove every 3rd word (Grades 2-4)
  - Remove every 4th word (Grades 5-7)
  - Remove every 5th word (Grades 8-11)
  - NEVER remove: Proper nouns, numbers, key formulas
  - ALWAYS keep first and last sentence intact

WORD BANK:
  Grades 2-4: Correct answers + 3 distractors per blank
  Grades 5-7: Correct answers + 2 distractors per blank
  Grades 8-11: No word bank (free recall)

XP: 100 XP per correct fill | First-attempt bonus: +25 XP | All correct: +100 bonus
TIMER: 2-3 minutes
```

#### Game 5: Memory Palace

```
PALACE CONSTRUCTION:
Step 1 - Select Palace (30 sec): Registan Square (default), student's home, school, local bazaar
Step 2 - Place Concepts (60 sec): 5 concepts placed at 5 locations
Step 3 - Mental Walkthrough (30 sec): Guided visualization
Step 4 - Recall Test (60 sec): "What was at the Main Gate?" -- 5 questions

XP: 50 XP per correct recall | All 5 correct: +50 bonus | Total: 300 XP max
```

#### Game 6: Story Mode

See Phase 2 specification (Section 5.2). Detailed media and cultural requirements included there.

#### Game 7: Adaptive Quiz

```
ITEM RESPONSE THEORY (IRT) IMPLEMENTATION:

Question Bank Requirements:
  - Each question pre-calibrated with:
    - difficulty (theta): -3.0 to +3.0
    - discrimination (alpha): 0.5 to 2.0
    - guessing (c): 0.1 to 0.25

Adaptation Algorithm:
  1. Start with theta = 0 (grade-level expectation)
  2. Present question with difficulty ~ current theta
  3. IF correct: theta += 0.3
     IF incorrect: theta -= 0.3
  4. Select next question with difficulty ~ new theta
  5. Repeat for 5-7 questions
  6. Final theta = student's ability estimate

PISA CEILING: Adaptive Quiz difficulty tiers map to PISA levels:
  Tier 1-2 = PISA Level 1-2
  Tier 3 = PISA Level 3
  Tier 4 = PISA Level 4
  Tier 5 = PISA Level 5

XP: Based on final theta achieved
```

#### Game 8: Mystery Box (Interleaving)

```
MECHANICS:
  1. Display 3-5 closed boxes
  2. Each box contains problem from DIFFERENT category (current + previous chapters)
  3. Click box -> box opens with animation -> problem revealed
  4. FIRST: Student identifies problem TYPE (dropdown)
  5. THEN: Student solves problem
  6. Feedback on both type identification AND solution

SCORING:
  - Correct type ID: +50 XP
  - Correct solution: +150 XP
  - Both correct: +50 bonus XP
  - Total per box: 250 XP maximum
```

#### Game 9: Movement Breaks

```
GRADES 1-4 REQUIRED | GRADES 5-6 OPTIONAL | GRADES 7+ DISABLED

Activity Types:
  1. Act It Out: "Use your arms to show acute/right/obtuse angle"
  2. Find It: "Look around your room. Find something shaped like a circle"
  3. Count With Motion: "Count by 3s. Clap on each number"

DURATION: 60-90 seconds
PLACEMENT: Between Story Mode and Game Breaks
XP: +100 XP for completion (honor system)
```

#### Game 10: Why Chain (Socratic Dialogue)

```
AI DIALOGUE PATTERN:

Level 1 (Surface):
  AI: "Why do plants need sunlight?"
  Student: "To grow."
  AI: "Good start! But WHY does sunlight help them grow?"

Level 2 (Mechanism):
  Student: "Sunlight gives them energy."
  AI: "Excellent! What do plants DO with that energy?"

Level 3 (Process):
  Student: "They make food from CO2 and water."
  AI: "Perfect! You've described photosynthesis!"

CHAIN LENGTH: 3-5 levels minimum
TIMER: 3 minutes
AI RULES: NEVER give direct answer | ALWAYS acknowledge | ALWAYS probe deeper

PISA LEVEL EXAMPLES:
  Level 2-3: Why Chain with 2-3 levels, guided prompts
  Level 3-4: Why Chain with 4 levels, less scaffolding
  Level 5-6: Why Chain with 5+ levels, open-ended, competing explanations

XP: 150 XP per level | Complete all levels: +250 bonus | Hint: -10 XP per hint
```

#### Game 11: Peer Teaching

```
SCENARIOS:
  A - Explain to Younger Student: "A Grade 3 student is learning fractions. Explain what 1/2 means."
  B - Help a Classmate: "Sardor doesn't understand common denominators. Write a message to help."
  C - Correct a Mistake: "A student said 1/2 + 1/3 = 2/5. Explain what went wrong."

SCORING:
  - Completeness (key concept covered): +100 XP
  - Clarity (language appropriate): +100 XP
  - Accuracy (mathematically/scientifically correct): +200 XP
  - Total: 400 XP

AI EVALUATION: Check for key terms, logical flow, correct facts. Flag for teacher review if inaccurate.
AVAILABILITY: Grades 5-11 only
```

#### Game 12: Reflection Journal

See Phase 7 specification (Section 5.7). Used as both standalone mechanic and session closer.

#### Game 13: Final Boss

See Phase 6 specification (Section 5.6). Full HP system, tiered PISA mapping, Socratic failure flow.

#### Game 14: Real-Life Challenge

See Phase 4 specification (Section 5.4). Full scenario structure with Uzbek cultural context.

---

### 6.3 Mystery Box — Case-Opening Specification *(NEW 2026-04-07)*

The Mystery Box is no longer a static interleaving question. It is a **case-opening event** — explicitly NOT gambling. There is no "rare drop" mechanic that withholds learning value. Every Mystery Box attempt yields XP. The mystery is *what question* appears and *what reward pool item* is earned, not whether the student learns.

**Appearance Rules:**

| Aspect | Rule |
|---|---|
| **Trigger** | Either (a) randomly during homework as a surprise event, OR (b) pre-placed by content creator at a specific milestone in the session |
| **Question Source** | If inside homework: questions from the current subject. If outside homework (random event): questions from ALL subjects passed up to current point |
| **Difficulty Range** | Easy to Extreme Hard — randomly selected. Student has no control. |
| **Question Format** | Single challenging question — MC, open reasoning, puzzle, or case scenario |
| **No Gambling** | Every attempt yields XP. No "withhold learning" mechanic. |

**Reward Logic (performance-based, not chance):**

| Performance | Reward |
|---|---|
| Correct answer | XP + random bonus from reward pool (below) |
| Partial answer | Reduced XP + smaller bonus |
| Wrong answer | Small participation XP only (no bonus item) |

**Reward Pool (drawn when student earns a bonus):**

| Reward | Description | Rarity |
|---|---|---|
| **XP Boost** | +50% XP on next homework session | 40% |
| **Extra AI Usage** | Additional advanced AI tutor uses ("Talk to your AI tutor for 5 extra questions") | 25% |
| **Avatar Frame** | Cosmetic frame for student profile picture | 15% |
| **Customization Item** | Theme, color, animation for profile or UI | 10% |
| **Coupon** | In-system currency for avatar shop, streak freeze, etc. | 7% |
| **Mythical Boss Event Ticket** | Guarantees a Mythical Boss appearance in one of the next 3 sessions | 3% |

### 6.4 Tic Tac Toe vs AI — Full Game Rules *(NEW 2026-04-07)*

A strategic game where the student plays Tic Tac Toe against the AI. Each move requires answering a subject-related question correctly.

**Game Flow:**

```
1. AI asks FIRST question (determines who starts)
   - Correct → student goes first (places X)
   - Wrong   → AI goes first (places O)

2. STUDENT'S TURN:
   a. Student selects which tile they want to place their X
   b. AI asks a subject-related question
   c. Student answers:
      - CORRECT (or ≥60% credit on open-reasoning) → X placed on chosen tile
      - WRONG  → X placed on a RANDOM tile
        (0.2% mercy chance the random tile is the one student wanted)

3. AI'S TURN:
   a. AI places its O strategically (optimal play at current difficulty)
   b. No question required — AI just moves

4. Win / Loss / Draw:
   - Student gets 3 in a row → WIN
   - AI gets 3 in a row      → LOSS
   - Board full, no winner   → DRAW (replay)
```

**Difficulty Scaling:**

| Rule | Detail |
|---|---|
| **Starting difficulty** | Calibrated to student's PISA level |
| **Adaptive decrease** | After each incorrect answer, AI decreases question difficulty by 1 tier |
| **Minimum difficulty floor** | 60% of student's current PISA level — AI will never drop below this |
| **AI play strength** | AI plays optimally. It will not deliberately let the student win — strategic mistakes are not part of the design. |

**Chances and Failure:**

| Rule | Detail |
|---|---|
| **Attempts** | 3 chances (3 games per Tic Tac Toe session) |
| **Per-game failure** | If student loses a game, they get feedback on which questions they missed, then retry |
| **All 3 failed** | Task marked FAILED. Score = 0 for this practice. Student must redo the homework session (Duolingo Mode applies — see §8). |
| **Win** | Standard XP + bonus for remaining attempts (fewer attempts used = more bonus XP) |

**Win Rate Tracking:** The system MUST accurately calculate and display the student's win rate for this game mode. Win rate feeds into the mastery map and is visible on the student's profile.

### 6.5 "Did You Know..." — Loading Screen Insights *(NEW 2026-04-07)*

Between phases, during loading screens, or between questions, the system displays short engaging insights related to the current subject/theme. Turns dead time into micro-learning without adding session length.

| Rule | Detail |
|---|---|
| **Content** | Fun facts, historical discoveries, surprising experiments, real-world connections, "behind the scenes" science/math/history |
| **Length** | 1-2 sentences max. Readable in 5 seconds. |
| **Relevance** | MUST relate to the current lesson's theme. Random off-topic facts are rejected. |
| **Tone** | Conversational, surprising, "wait really?" energy |
| **Frequency** | 1 per phase transition. Not more — it becomes noise. |
| **No quiz follow-up** | Pure curiosity injection. No questions, no scoring. |

**Example:** *"Did you know? The word 'oxygen' comes from Greek words meaning 'acid producer' — because scientists originally thought ALL acids contained oxygen. They were wrong."*

---

## 6.6 Assessment System — Pass/Fail, Celebration Tiers, Duolingo Mode *(NEW 2026-04-07)*

The original framework had no clear pass/fail threshold, no repass mechanic, and no performance-based celebration tiers. This section closes that gap.

**Score-Tier Response Matrix:**

| Score Range | Rating | Consequence | Reward |
|---|---|---|---|
| **100%** | PERFECT | Session complete | 🎉 On-screen celebration (confetti, animation, sound). Maximum XP. Temporary title: "Perfectionist". |
| **99%** | Almost Perfect | Session complete | Tease: *"So close! One more point!"* Maximum XP minus 1%. |
| **90-98%** | Excellent | Session complete | Strong praise. Full XP. Streak fire animation. |
| **80-89%** | Very Good | Session complete (first-time-80%+ bonus) | Bonus XP for hitting 80% on first attempt. Standard praise. |
| **60-79%** | Passing | Session complete. **Repass option offered.** | Standard XP. *"You passed! Want to try again for a better score?"* |
| **Below 60%** | Failed | **MUST redo.** Session enters Duolingo Mode. | No XP for failed tasks. *"Let's try again — you've got this!"* |

**Duolingo Mode (Below 60%):**

When a student scores below 60%:

1. **Immediate feedback:** *"You scored X%. You need 60% to pass. Let's work on what you missed."*
2. **Task-by-task review:** The system identifies which specific questions the student got wrong and re-presents them with additional scaffolding (hints, simplified versions).
3. **Adjusted difficulty:** Re-attempt questions are one difficulty tier lower.
4. **Repeat until 60%:** Student continues until they reach the 60% threshold. No upper limit on attempts. Teacher is auto-flagged after 3 failed sessions on the same topic.
5. **No XP penalty:** XP is only awarded once the student crosses 60%. Previous failed attempts earn 0 XP (not negative).

**Repass Option (60-79%):**

Students who pass with 60-79% are offered: *"You passed! Want to try again for a better score?"*

- If accepted: the homework restarts with regenerated questions (same standards, different numbers/scenarios).
- If declined: session completes with current score and XP.
- Maximum 2 repass attempts per homework.

---

## 6.7 Answer Checking Logic — Dual Pathway *(NEW 2026-04-07)*

Not all questions need AI evaluation. The system uses two distinct pathways depending on question type. This eliminates the previous "AI checks everything" latency and cost problem.

| Question Type | Checking Method | Reason |
|---|---|---|
| **Hardcoded** (MC, matching, Tile Match, numeric answer, formula input) | **Rule-based exact match.** No AI needed. Instant feedback (<0.1s). | Answers are fixed and verifiable without interpretation. |
| **Open Reasoning** (typed response, explanation, justification, essay, case analysis) | **AI real-time evaluation AFTER submission.** Tier 3 model scores against rubric and returns instant feedback. | Student can phrase the answer in their own words. The expected answer is a concept, not a string. AI must understand semantic equivalence. |

**AI Real-Time Check Rules:**

- Triggered ONLY when student submits a typed/open answer.
- AI receives: the question, the scoring rubric, the student's answer, the student's PISA level.
- AI returns within 3 seconds: score (0-100%), partial credit breakdown, one-sentence feedback.
- **Hard timeout: 5 seconds.** If AI fails to respond → fallback to keyword matching against expected answer concepts in the rubric.
- **Never reveals the correct answer during evaluation.** Only scores and gives feedback.
- All AI evaluations log: question_id, student_answer, ai_score, ai_feedback, latency, fallback_used (bool). For audit and pipeline tuning.

---

## 6.8 Notebook Capture — Hand-Written / Hand-Drawn Tasks *(NEW 2026-04-07)*

**Purpose:** Force the student off the screen and back into a physical notebook for tasks that genuinely benefit from hand-writing or hand-drawing. The student does the work on paper, takes a photo, uploads it, and AI vision evaluates the result.

**Why this exists:** Cognitive science (Generation Effect, Embodied Cognition, Mueller & Oppenheimer's "pen vs laptop" research) consistently shows that physical writing improves retention 25-40% over typing — especially for math derivations, diagrams, and conceptual sketches. NETS was previously screen-only. This closes that gap without abandoning the digital game loop.

### 6.8.1 When to Use Notebook Capture

| Subject | Best Use Cases |
|---|---|
| **Math** | Long-form derivations, multi-step proofs, geometric constructions, sketching graphs, working out word problems on paper |
| **Physics / Chemistry** | Free-body diagrams, circuit schematics, molecular structures, balancing equations by hand, sketching wave forms |
| **Biology** | Labelled diagrams (cell structures, anatomy, plant parts), food-web sketches, microscope drawings |
| **History / Geography** | Hand-drawn timelines, annotated maps, cause-and-effect mind maps |
| **Literature / Languages** | Essay drafts, paragraph plans, vocabulary mind-maps, calligraphy practice for Uzbek/Russian/Arabic scripts |
| **Art / Design** | Sketches, perspective practice, color studies (where the curriculum requires) |

**Frequency rule:** A Notebook Capture task should appear in approximately **1 of every 3-4 homework sessions** for Grades 5+. Lower grades (1-4) get them less often (1 in 6 sessions) because younger students need more digital scaffolding. They are NOT mandatory in every session — overuse breaks the game loop.

### 6.8.2 Where in the Session It Fits

Notebook Capture tasks can be placed in:

- **Phase 3 (Game Breaks)** — as a 5-min "deep dive" replacing one of the 3 game slots, when the topic benefits from hand-work
- **Phase 4 (Real-Life Challenge)** — when the case requires a hand-drawn diagram or sketched plan as part of the response
- **Phase 6 (Boss Fight)** — for higher grades, the boss can demand a hand-derived solution as the final question (Mythical Boss almost always requires this)

It does NOT fit in Phase 1 (too slow), Phase 2 (passive content), Phase 5 (consolidation, not production), or Phase 7 (reflection is text-based by design).

### 6.8.3 Task Flow

```
1. PROMPT: Task card displays "📓 Notebook Task" with the prompt text
   ("Sketch the free-body diagram for a block sliding down a 30° ramp,
    label all forces, and show the net force vector.")
2. INSTRUCTION: "Open your notebook. Do the work. When you're done,
   tap UPLOAD to take a photo."
3. STUDENT WORKS OFFLINE — no timer pressure beyond a soft 10-min
   suggested cap. App can be backgrounded.
4. STUDENT TAPS UPLOAD: opens camera (or photo picker as fallback)
5. STUDENT TAKES / PICKS PHOTO of their notebook page
6. PRE-UPLOAD VALIDATION (client-side, instant):
   - Image is in focus (Laplacian variance > 100)
   - Page is detected (edge detection finds rectangular bound)
   - Lighting is adequate (mean brightness 60-200 / 255)
   - If any check fails: prompt to retake with specific tip
     ("It's a bit blurry — hold steady" / "Too dark — find brighter light")
7. UPLOAD: image sent to AI Tier 3 vision model
8. AI VISION EVALUATION (within 8 seconds):
   - OCR + diagram understanding extracts the student's work
   - Compared against the rubric for the task
   - Returns: score 0-100%, partial credit breakdown, specific feedback
     ("Your free-body diagram correctly shows gravity and normal force,
      but the friction vector is pointing the wrong way. Friction opposes
      motion — re-check the direction.")
9. FEEDBACK: shown to student with the photo + AI annotations overlaid
   (small red circles around problem areas, green checks on correct parts)
10. STUDENT can either ACCEPT the score and move on, or RETRY with
    a corrected page if score < 60%.
```

### 6.8.4 AI Vision Evaluation Rules

| Rule | Detail |
|---|---|
| **Model tier** | AI Tier 3 multimodal (vision-capable). Rubric-driven, NEVER reveals the correct answer in the feedback. |
| **Latency budget** | Hard 10-second cap. If exceeded → fallback to "human review queue" + provisional XP based on participation. Teacher reviews async. |
| **Acceptable handwriting** | Must handle messy student handwriting, smudges, eraser marks, and notebook lines. Rubric evaluation is semantic, not pixel-perfect. |
| **Multi-page tasks** | Student can upload up to 3 photos for one task (e.g., a 2-page proof). Photos are stitched and evaluated as one submission. |
| **Privacy** | Photos are stored encrypted, retained for 30 days for re-evaluation/audit, then deleted. Teacher and parent can view; nobody else. |
| **No face / personal info** | If the AI vision detects faces, student names visible on the page header, or personal identifiers, those regions are blurred client-side BEFORE upload. |
| **Cheating detection** | Vision model flags suspiciously perfect work (looks printed, looks copied), identical submissions across students, or work that doesn't match the student's prior handwriting baseline. Flagged work goes to teacher review, not auto-failed. |

### 6.8.5 Scoring and XP

| Outcome | XP | Notes |
|---|---|---|
| **Correct + clear handwriting** | 100% XP | Standard reward |
| **Correct concept, messy execution** | 80-95% XP | Partial credit for clarity issues only if rubric specifies neatness |
| **Partial answer** | 40-70% XP | Pro-rated against rubric coverage |
| **Wrong** | 0-30% XP (participation) | Routes into Duolingo Mode if it's the boss question |
| **Bonus: pristine notebook** | +10% XP | Teacher-controlled toggle for handwriting/presentation grades |

### 6.8.6 Accessibility / Edge Cases

- **No camera available?** Student can upload a scanned PDF or use the device's photo library.
- **Visually impaired student?** Notebook Capture is exempt — replaced with a verbal description task (audio recording instead).
- **Motor disability?** Teacher can toggle Notebook Capture OFF for individual students; replaced with the standard digital input version of the task.
- **No notebook (forgot)?** Student can use the in-app sketch tool as a fallback (stylus or finger drawing on screen). Reduced XP (max 80%) because it bypasses the embodied cognition benefit.
- **Privacy at home / shared device?** Photos are tied to the student account, not the device. Other family members cannot access them.

### 6.8.7 Teacher Controls

Teachers can:
- Disable Notebook Capture entirely for their class (default: ON for Grades 5+)
- Adjust frequency (1-in-3 default, 1-in-6 minimum, every-session maximum)
- Toggle the "pristine notebook" bonus
- Review all submitted photos for their class via the teacher dashboard
- Override AI scores with manual scoring

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
    |     no duplicates, prerequisites valid, time estimate realistic
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
    |-- [14. Delivery API] -> Frontend renders session
    |-- [15. Analytics Collector] -> Performance data (feeds back into steps 11, 12, 13)
```

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
| Grades 1-2 | 15-20 min | 30 min | 10-15 min |
| Grades 3-4 | 20-25 min | 35-40 min | 15-20 min |
| Grades 5-8 | 20-30 min | 40-50 min | 15-20 min |
| Grades 9-11 | 25-30 min | 45-50 min | 20-25 min |

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

**END OF UNIFIED SPECIFICATION**

*This document is the single authoritative specification for the NETS Homework Engine.*
*All previous versions are superseded.*
*Engineering and content teams build exclusively from this document.*

**Version:** 2.0
**Date:** April 2, 2026
**Status:** Single Source of Truth
