---
name: Decision Enforcement — No Optional Content
status: v0.1 draft
layer: 0 (core primitive)
source: §22 session — anti-lazy-LLM principle
---

# Decision Enforcement

## The problem

LLMs take the path of least resistance. Given "optional" content, they skip it. Given "may include", they don't. Given "consider adding", they pretend to consider and move on. Every "optional" in the framework is a door for lower-quality output.

## The rule

**The word "optional" is BANNED from all component specs.**

Every conditional element must have:
- **MUST INCLUDE IF** [concrete, testable condition]
- **MUST SKIP IF** [concrete, testable condition]

No middle ground. No "consider." No "may." Binary gate: condition met → include. Condition not met → skip.

## LLM reasoning requirement

Before deciding to include or skip ANY conditional element, the agent MUST output a reasoning chain:

```
DECISION: [element name]
CONDITION: [the rule being evaluated]
EVIDENCE: [what in the content satisfies or fails the condition]
VERDICT: INCLUDE / SKIP
```

This chain is logged in the session output. Auditable. If the reasoning is missing or says "not needed" without evidence, the output fails verification.

## Scope

This rule applies to EVERY component file in the framework:
- Phase components (01-phases/): which sub-elements to include
- Family adapters (02-families/): which overrides to apply
- Mode specs (03-modes/): which scaling to use
- Builder pipeline (05-builder/): which steps to execute

If a component says "the agent may..." → rewrite as "the agent MUST IF..." with a condition.

---

## Decision gates across the framework

Every conditional element, with its enforced condition:

### Preview (Phase 0-A)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Panel 4 (Origin) | Family is Aniq Fanlar or Tabiy Fanlar (genetic method applies) | Family is Til Fanlar or Ijtimoiy Fanlar |
| Panel 5 (Personal Hook) | Mode is Hard AND lesson has no obvious personal connection | Mode is Easy OR lesson topic has self-evident relevance |
| Panel 6 (Why This Matters) | Mode is Hard | Mode is Easy AND Panel count is already ≥3 |
| Panel 7 (Industry App) | Mode is Hard AND concept has clear career application | Mode is Easy OR concept is foundational (no direct career link yet) |
| Panel 8 (Additional Materials) | Mode is Hard AND quality external resources exist for this topic | Mode is Easy OR no vetted resources available |
| Mind map / SVG visual | Concept is spatial, relational, procedural, or geometric (see `visual-generation.md` "when" table) | Concept is purely definitional or textual |
| "In plain words" block | Panel introduces a technical term, formula, or multi-step concept | Panel content is already plain language (no jargon) |

### Flash Cards (Phase 0-B)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Visual on card back | Card concept is spatial or geometric (shape, graph, diagram) | Card concept is textual (vocabulary, rule statement) |
| Memory hook | Always — EVERY card back has exactly 1 hook | Never skipped |
| Cluster grouping | Deck has ≥6 cards (enough to form meaningful clusters) | Deck has <6 cards (single cluster) |

### Memory Sprint (Phase 1)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| 7 items (not 5) | Mode is Hard | Mode is Easy |
| YNNG format | Lesson content has a common misconception to test | No clear misconception exists for this topic |

### Game Breaks (Phase 3)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| 3rd game (Interactive) | Mode is Hard | Mode is Easy (only 2 games) |
| Adaptive Quiz | Family is Aniq Fanlar or Tabiy Fanlar (calc-heavy) | Family is Til Fanlar or Ijtimoiy Fanlar |
| Notebook Capture | Question requires multi-step calculation (see `capture-rule.md`) | Question is recognition, matching, or conceptual |
| Why Chain | Lesson has ≥1 "why" question that goes 3+ levels deep | Topic is procedural with no causal depth |
| Territory Conquest | Lesson is Review archetype with conquest/expansion theme | Lesson is Concept Intro or vocabulary |

### Reading (Phase 2)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Entire phase | Family is Til Fanlar AND mode is Hard | Any other family OR mode is Easy |

### Real-Life (Phase 4)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Entire phase | Family is Aniq Fanlar or Tabiy Fanlar AND mode is Hard | Family is Til or Ijtimoiy, OR mode is Easy |
| Scenario illustration (SVG) | Scenario involves spatial/geometric/physical elements | Scenario is purely numerical |

### Consolidation (Phase 5)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Entire phase | Lesson introduces ≥2 interlocking concepts requiring method-choice synthesis | Lesson has ≤1 core concept |

### Final Challenge (Phase 6)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Entire phase | Mode is Hard | Mode is Easy |
| HP combat mechanic | Lesson is Algorithm, Application, or Review | Lesson is Concept Intro (light checkpoint instead) |
| Mid-boss checkpoint | Lesson is Review (full boss) | Lesson is anything else |

### Visuals (cross-phase)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| SVG diagram | Concept is in the "when to generate" table in `visual-generation.md` | Concept is purely textual |
| Mermaid flowchart | Concept is a process, state machine, or decision tree | Concept is static/spatial (use SVG instead) |

---

## Enforcement in the pipeline

The builder pipeline (`05-builder/homework-builder.md`) must:

1. **Before COMPOSE:** for each phase, evaluate every decision gate above
2. **Log the reasoning chain** for each INCLUDE/SKIP decision
3. **Reject output** if any conditional element lacks a logged reasoning chain
4. **Verification gate** (`05-builder/verification-checklist.md`): add "Decision reasoning complete" as a pass condition — every conditional element has a logged INCLUDE/SKIP with evidence

## How to audit existing components

Grep all component files for these banned words:
```bash
grep -rn "optional\|may include\|consider adding\|can be\|might include\|could add" standards/framework/01-phases/ standards/framework/02-families/ standards/framework/03-modes/
```

Every hit must be rewritten as MUST IF / MUST SKIP IF with a concrete condition.

## Cross-references

- Every phase component in `01-phases/`
- Every family adapter in `02-families/`
- Mode specs in `03-modes/`
- `05-builder/homework-builder.md` (COMPOSE step)
- `05-builder/verification-checklist.md` (add decision-reasoning gate)
