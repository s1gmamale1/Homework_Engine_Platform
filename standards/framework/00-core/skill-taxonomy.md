---
name: Skill Taxonomy (6 Axes)
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: Derived from §22 reference implementation (Grade 8 Algebra, Kvadrat Tenglama)
---

# Skill Taxonomy — 6 Axes

## Rule / Definition

Every question in a NETS session is tagged with one or more skill axes. These six axes drive per-question tagging, per-student profiling, and downstream analytics. They are not Bloom's levels and not PISA levels — they are a finer-grained, action-oriented taxonomy derived from the §22 reference session.

---

### Axis 1: Memory

**Definition:** The ability to recognize patterns, recall vocabulary, and retrieve formulas from long-term memory without contextual transformation.

**What it measures:** Pure retrieval accuracy. Whether the student can surface a fact, term, or formula on demand.

**Example questions that tag this axis:**
- "In the equation 2x² − 5x + 3 = 0, identify the values of a, b, and c."
- "What is the standard form of a quadratic equation?"
- "True or False: x² + 4 = 0 has real solutions."

**PISA competency mapping:** PISA Math L1 (answer questions in familiar contexts; single-step procedures); PISA Reading L1 (locate single explicit information).

---

### Axis 2: Translation

**Definition:** The ability to convert a real-world problem statement or verbal description into a formal mathematical (or domain-equivalent) representation.

**What it measures:** The bridging step between natural language and symbolic/procedural form. Students must identify which variables, constraints, and relationships are present.

**Example questions that tag this axis:**
- "A rectangle has area 96 m². Its width is 4 m less than its height. Write an equation to represent this situation." → x(x + 4) = 96
- "A train travels 120 km. It takes 1 hour longer at 40 km/h than at 60 km/h. Set up the equation."

**PISA competency mapping:** PISA Math L2 (recognize situations needing simple strategies; extract info from tables/charts); PISA Math L3 (communicate reasoning; select problem-solving strategies).

---

### Axis 3: Problem-Solving

**Definition:** The ability to apply a known procedure or algorithm to compute a correct answer once the problem has been set up.

**What it measures:** Procedural fluency and execution accuracy. The student knows the method; this axis tests whether they can carry it through to a correct result.

**Example questions that tag this axis:**
- "Factor x² + 5x + 6 using the p + q / p × q method."
- "Solve 2x² − 5x + 3 = 0 by completing the square."
- "Use the quadratic formula to find the roots of x² − 4x + 1 = 0."

**PISA competency mapping:** PISA Math L2–L3 (execute multi-step procedures; apply standard algorithms).

---

### Axis 4: Critical Thinking

**Definition:** The ability to judge the validity of answers, filter out mathematically or contextually impossible results, and explain the reasoning behind a rejection or selection.

**What it measures:** Evaluative reasoning beyond computation. Students must apply domain constraints (e.g., physical reality, logical consistency) to assess whether a calculated answer is actually acceptable.

**Example questions that tag this axis:**
- "You found x = 8 and x = −12 as solutions. The variable x represents a length. Which solution is valid? Why is the other rejected?"
- "A student solved a quadratic and got two positive roots. The problem asks for a time value. Are both roots necessarily valid?"
- "Error detection: A classmate wrote x² + 5x + 6 = (x + 2)(x + 4). Is this correct? Identify the mistake."

**PISA competency mapping:** PISA Math L3–L4 (reflect on results in context; evaluate reasonableness); PISA Reading L4 (evaluate relevance).

---

### Axis 5: Application

**Definition:** The ability to take a concept learned in one context and deploy it effectively in a new, unfamiliar, real-world scenario.

**What it measures:** Transfer of learning. The student is not following a template — they must recognize that the quadratic (or domain concept) applies, set it up, solve it, and interpret the result in the new context.

**Example questions that tag this axis:**
- "A solar farm's rectangular panels have a combined area of 500 m². The length exceeds the width by 5 m. Find the panel dimensions."
- "A ball is launched from a rooftop. Its height (m) after t seconds is h = −5t² + 20t + 15. When does it hit the ground?"
- "A company's profit P (in millions) satisfies P = −2x² + 8x − 3, where x is price in USD. Find the price that maximizes profit."

**PISA competency mapping:** PISA Math L3–L4 (work with explicit models for complex situations; apply to real-world contexts); PISA Math L5 (develop models; systematic problem-solving).

---

### Axis 6: Metacognition

**Definition:** The ability to reason about the method itself — evaluating whether the chosen approach was appropriate, identifying alternative strategies, and reflecting on the conditions under which a technique applies.

**What it measures:** Awareness of one's own thinking process. Students step back from the problem to assess the method, not just execute it.

**Example questions that tag this axis:**
- "You just solved a quadratic to find a rectangle's dimensions. Could this problem have been solved without setting up a quadratic? Explain why or why not."
- "You used the quadratic formula. When would factoring be a faster method? When would completing the square be preferred?"
- "Reflection: What was the hardest part of this session? What strategy would you use differently next time?"
- "A classmate skipped writing the equation and guessed x = 8. They got the right answer. Is their method valid? What are the risks?"

**PISA competency mapping:** PISA Math L5–L6 (reflect on results; conceptualize and generalize); PISA Creative Thinking: Evaluating and improving ideas.

---

## Summary Table

| Axis | Action Verb | Bloom's Tier | PISA Range | Phase Emphasis |
|---|---|---|---|---|
| Memory | Recall, Identify, Recognize | Remember | L0–L1 | Phase 1 (Memory Sprint), Phase 0-B (Flash Cards) |
| Translation | Convert, Set up, Model | Understand–Apply | L2–L3 | Phase 2 (Story Mode), Phase 4 (Real-Life Challenge) |
| Problem-Solving | Compute, Solve, Execute | Apply | L2–L3 | Phase 3 (Game Breaks), Phase 6 (Final Boss Easy/Medium) |
| Critical Thinking | Judge, Filter, Reject, Explain | Analyse–Evaluate | L3–L4 | Phase 6 (Final Boss Medium/Hard), Phase 2 Checkpoints |
| Application | Transfer, Deploy, Use in context | Apply–Analyse | L3–L5 | Phase 4 (Real-Life Challenge), Phase 6 (Final Boss Hard) |
| Metacognition | Reflect, Evaluate method, Compare strategies | Evaluate–Create | L5–L6 | Phase 7 (Reflection), Phase 8 Creative Lab |

---

## Scope

These six axes apply universally across all subject families and all grade bands. Subject framework delta layers may emphasize certain axes (e.g., Til Fanlar emphasizes Translation and Critical Thinking; Aniq Fanlar emphasizes Problem-Solving and Metacognition), but no subject may remove axes or redefine them.

Every question in a session must carry at minimum one skill axis tag in addition to its Bloom's and PISA tags:
`[Bloom: LX | PISA: LX | Skill: Memory]`

## Cross-references

- `00-core/pisa-framework.md` — PISA competencies that each axis maps to
- `01-phases/phase-01-memory-sprint.md` — Memory axis dominates; Critical Thinking excluded
- `01-phases/phase-02-story-mode.md` — Translation axis primary at checkpoints
- `01-phases/phase-04-real-life-challenge.md` — Application axis primary
- `01-phases/phase-06-final-boss.md` — Critical Thinking and Metacognition required at Hard tier
- `01-phases/phase-07-reflection.md` — Metacognition axis primary
- `05-builder/question-schema.md` — Inline tag format: `[Skill: AxisName]`

## Verification

- Every question must carry at least one `[Skill: X]` tag from the six axes above.
- Phase 1 (Memory Sprint) must not tag Critical Thinking or Metacognition (format restrictions apply).
- Phase 7 (Reflection) must tag Metacognition.
- Final Boss Hard tier must include at least one Critical Thinking and one Metacognition question.
- No new axes may be introduced without an ADR and update to this file.
