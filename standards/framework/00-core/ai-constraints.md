---
name: ai-constraints
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED §18 lines 3400-3433
---

# AI Constraints

## Rule

AI Refinement operates within strict boundaries. It may transform presentation; it may not alter substance.

## Permissible AI Operations (§18.1)

- **Formatting:** Restructure textbook content for digital display
- **Narrative framing:** Wrap concepts in character-driven stories with Uzbek cultural context
- **Cultural contextualization:** Add Uzbek names, locations, scenarios, currency
- **Difficulty scaffolding:** Adjust question complexity within the same concept
- **Question generation:** Create new questions that test the same concepts as textbook exercises
- **Visual generation:** Create diagrams, bar models, and visual representations of textbook concepts
- **Translation:** Convert between Uzbek and Russian while preserving meaning
- **Hint/scaffold/explain:** Provide scaffolded hints and explanations for existing content

## Prohibited AI Operations (§18.2)

AI Refinement MUST NOT:

- Alter factual claims, mathematical formulas, or scientific laws
- Modify historical dates, geographical information, or biographical facts
- Change grammar rules or vocabulary definitions
- Simplify in ways that remove essential meaning or prerequisite knowledge
- Introduce content beyond textbook scope for the given grade
- Generate questions that test concepts not covered in the textbook
- Create cultural references that are inaccurate or inappropriate
- Produce content that contradicts the national curriculum

## Tier Distinction

| Tier | Description | Review Requirement |
|------|-------------|-------------------|
| **Tier 1** | Pre-generated at authoring time. Content is fixed before student interaction. | Expert review before publish |
| **Tier 2** | Live generative — AI produces content dynamically during a student session. | Expert review of templates/prompts; outputs logged for audit |

## CS/Informatics Exception (§18.3)

Where MoEN-approved CS textbooks do not yet cover topics in the NETS CS progression (e.g., Python/JavaScript for Grades 7–9, AI/ML concepts for Grades 10–11), these topics are NETS-supplemented content. This is an explicit, acknowledged exception to the textbook-source-of-truth principle. CS-supplemented content must still comply with all tagging, PISA calibration, and review requirements. Exception reviewed annually as textbooks are updated.

## Verification

- Content audit: cross-reference every factual claim against the source textbook chapter
- Tier 2 outputs: maintain generation logs; flag anomalies for expert review

## Cross-references

- UNIFIED-Buzan §18 lines 3400–3433 (canonical source)
- CLAUDE.md project instructions: "Textbook is source of truth" rule
- Agent config `agents/content-producer/SKILLS.md` — production pipeline must respect these boundaries
