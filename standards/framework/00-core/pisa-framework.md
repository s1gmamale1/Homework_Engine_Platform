---
name: PISA Proficiency Framework
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §3 (lines 334-452) + §7 (lines 2532-2650) + §8 (lines 2653-2713)
---

# PISA Proficiency Framework

## Rule / Definition

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

---

### 3.1 PISA→Bloom's Mapping

| PISA Level | NETS Bloom's Mapping | Primary Game Mechanics | Transition Skills (L->L+1) |
|---|---|---|---|
| Below Level 1 | Remember | Flashcards, Memory Sprint | Basic recall accuracy |
| Level 1 | Remember-Understand | Tile Match, Sentence Fill, Memory Palace | L1->L2: multi-step reasoning; extract from charts/tables; basic ratio |
| Level 2 | Understand-Apply | Quizzes, Mystery Box, Story Mode | L2->L3: sequential decisions; integrate multiple sources; communicate reasoning |
| Level 3 | Apply-Analyse | Real-Life Challenge, Why Chain, Final Boss (Easy) | L3->L4: explicit models; select/integrate representations; construct explanations |
| Level 4 | Analyse-Evaluate | Why Chain (deep), Final Boss (Medium), Peer Teaching | L4->L5: develop models; compare strategies; reflect on results |
| Level 5-6 | Evaluate-Create | Final Boss (Hard), Real-Life Extended, Creative Lab | L5->L6: conceptualize; generalize; advanced reasoning under novel conditions |

---

### 3.2 PISA Level as Progression Gate

The student's current PISA level (tracked per subject) determines:

- **Which Bloom's levels they primarily receive** — A student at PISA Level 1 gets mostly Remember/Understand items.
- **Final Boss difficulty tier** — Easy=L3, Medium=L4, Hard=L5-6 (see Section 5.6)
- **Game mechanic availability** — Higher PISA levels unlock harder mechanics
- **Homework completion threshold** — Final Boss requires demonstrating competence AT the student's target PISA level

---

### 3.3 Per-Student PISA Tracking (with Domain Breakdown)

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

### 7.1 Mathematics Progression by Grade

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

**PISA Skill Focus — Mathematics:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Mathematical Reasoning | Construct logical arguments | Why Chain, Final Boss | PISA-calibrated |
| Problem Solving | Apply math to novel situations | Real-Life Challenge, Mystery Box | PISA-calibrated |
| Mathematical Modeling | Translate real world -> math | Real-Life Challenge | PISA-calibrated |
| Communication | Explain mathematical thinking | Reflection Journal, Why Chain, Peer Teaching | PISA-calibrated |

---

### 7.2 Reading Progression by Grade

*Source: Leonardo's gap analysis template + PISA 2022 Reading framework.*

| Grade | PISA Target Level | Key Skill Focus | Primary NETS Games | Transition Skills |
|---|---|---|---|---|
| 1-2 | Level 1 | Retrieval: locate single explicit information in short text | Memory Sprint (vocab recall), Sentence Fill, Tile Match | Basic word recognition, literal comprehension |
| 3-4 | Level 1-2 | Inference: identify main idea; make straightforward inferences | Story Mode, Why Chain (2-level), Sentence Fill | L1->L2: compare info across simple sources; basic inference |
| 5-6 | Level 2-3 | Interpretation: integrate info from multiple parts of text; generate inferences | Why Chain (3-level), Mystery Box, Adaptive Quiz | L2->L3: integrate several pieces of info; compare/contrast |
| 7-8 | Level 3-4 | Evaluation: reflect on content and form; evaluate relevance | Real-Life Challenge, Why Chain (4-level), Final Boss Medium | L3->L4: interpret nuance; draw inferences from multiple sources |
| 9-11 | Level 4-6 | Critical Analysis: evaluate competing claims; assess reliability; synthesize across sources | Real-Life Challenge (extended), Final Boss Hard, Peer Teaching, Creative Lab | L4->L5: evaluate credibility; handle contradiction |

**PISA Skill Focus — Reading:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Access and Retrieve | Find explicit information in text | Memory Sprint, Sentence Fill | Textbook |
| Integrate and Interpret | Draw conclusions, make inferences, understand author's intent | Why Chain, Mystery Box, Real-Life Challenge | PISA-calibrated |
| Reflect and Evaluate | Judge text quality/credibility, evaluate arguments | Final Boss, Reflection Journal, Peer Teaching | PISA-calibrated |

---

### 7.3 Science Progression by Grade

*Source: Leonardo's gap analysis template + PISA 2022 Science framework.*

| Grade | PISA Target Level | Key Skill Focus | Primary NETS Games | Transition Skills |
|---|---|---|---|---|
| 1-2 | Level 1 | Scientific Knowledge: recall basic scientific facts; identify simple cause-effect | Memory Sprint, Flashcards, Movement Breaks | Basic observation, naming phenomena |
| 3-4 | Level 1-2 | Scientific Explanation: describe simple cause-effect relationships | Story Mode, Tile Match, Why Chain (2-level) | L1->L2: explain familiar phenomena; identify variables |
| 5-6 | Level 2-3 | Evidence Evaluation: use evidence to support claims; interpret data from simple tables | Mystery Box, Adaptive Quiz, Why Chain (3-level) | L2->L3: interpret data/evidence; identify experimental questions |
| 7-8 | Level 3-4 | Experimental Design: identify variables, propose tests, evaluate methods | Real-Life Challenge, Why Chain (4-level), Final Boss Medium | L3->L4: use abstract scientific content; reflect using evidence |
| 9-11 | Level 4-6 | Advanced Modeling: construct scientific models; evaluate competing hypotheses | Real-Life Challenge (extended), Final Boss Hard, Peer Teaching, Creative Lab | L4->L5: apply knowledge to novel/complex situations; evaluate competing explanations |

**PISA Skill Focus — Science:**

| Skill | Description | NETS Games | Assessment Layer |
|---|---|---|---|
| Scientific Explanation | Explain phenomena using evidence | Why Chain, Story Mode | Textbook + PISA |
| Evaluation and Design | Evaluate experiments, design investigations | Real-Life Challenge, Final Boss | PISA-calibrated |
| Data Interpretation | Analyze graphs, tables, evidence | Tile Match, Adaptive Quiz | PISA-calibrated |
| Scientific Reasoning | Construct causal chains | Why Chain (3+ levels) | PISA-calibrated |

---

### 7.4 History Progression by Grade

*Source: Research proposal P44 (History Philosophy), gap analysis (Michelangelo assessment p.283-290).*

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

---

### 8.1 PISA Creative Thinking Domain — 4 Modes

*Source: Gap analysis (Leonardo) identified that PISA 2022 assessed Creative Thinking for the first time. Uzbekistan scored 14/60 (OECD average: 33/60).*

PISA Creative Thinking assesses four competencies:
1. **Generating diverse ideas** — producing multiple different solutions
2. **Generating creative ideas** — producing original, non-obvious solutions
3. **Evaluating and improving ideas** — refining and selecting best approaches
4. **Expressing ideas** — written, visual, scientific, and social problem-solving

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

### 8.4 Creative Thinking Progression by Grade Band

| Grade Band | Creative Thinking Focus | NETS Implementation |
|---|---|---|
| 1-4 | Divergent play, multiple representations | Movement Breaks with creative element; Tile Match with "make your own pair" |
| 5-6 | Generate multiple solutions | Real-Life Challenge: "Find 2 different ways to solve this" |
| 7-8 | Evaluate and improve ideas | Why Chain branches; Peer Teaching with alternative explanations |
| 9-11 | Full creative problem-solving | Creative Lab; Final Boss Hard tier with design questions |

---

## Scope

This file applies to every question in every phase of every session. Any item tagged `[PISA: LX]` must map to a competency descriptor in this document. The progressions in §7 govern which PISA level to target when designing content for a given grade.

## Cross-references

- `01-phases/phase-01-memory-sprint.md` — PISA gate for format selection
- `01-phases/phase-05-consolidation.md` — PISA gate for Final Boss difficulty
- `01-phases/phase-06-final-boss.md` — PISA level determines Easy/Medium/Hard tier
- `02-families/aniq-fanlar.md` — Mathematics domain breakdown usage
- `02-families/tabiy-fanlar.md` — Science domain breakdown usage
- `02-families/til-fanlar.md` — Reading domain breakdown usage
- `02-families/ijtimoiy-fanlar.md` — History dual-domain mapping
- `00-core/skill-taxonomy.md` — Maps PISA competencies to 6 skill axes

## Verification

- Every question in the session must carry `[PISA: LX]` inline tag.
- The PISA level claimed must match a descriptor row in §3.0 tables above.
- Grade-level PISA targets (§7.1–7.4) must align with the grade band of the session being built.
- Creative Lab (§8.3) may only appear for PISA Level 3+ students, Grades 5-11.
- History sessions must use dual-domain mapping (Reading + Creative Thinking) — no standalone History PISA level.
