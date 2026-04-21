---
name: content-architecture
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §2 (lines 196-332)
---

# Content Reference Architecture

## Content

### 2.1 Hierarchy

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

*Source: Original spec Section 2.1. Best-structured hierarchy across all sources.*

---

### 2.2 Learning Units (LU)

Each textbook chapter is split into Learning Units (LUs):
- Typically 1-3 LUs per chapter section
- Each LU maps to exactly one curriculum standard code
- Each LU has a prerequisite chain (e.g., fractions require whole number division)
- Each LU generates 10-15 tasks across Bloom's levels: 4 Remember, 3 Understand, 3 Apply, 2 Analyze, 1-2 Evaluate/Create
- Each task is assigned to exactly one game mechanic

*Source: HOMEWORK_TASK_ENGINE.md. Adds critical intermediate concept between Topic and Content Block.*

---

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

---

### 2.4 Dual Standard Code Format

The descriptive format `UZ-MATH-5-FRAC-01` is the PRIMARY format. The original dotted format `MAT.5.1.3.2` is supported as an alias for backward compatibility.

*Resolution: The colleagues' descriptive format is the PRIMARY format. The dotted format is supported as an alias.*

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

---

### 2.5 Mandatory Tagging Schema — Every Item

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

## Scope

This architecture applies to every content item across all subjects and grade bands. It governs how content is structured, identified, tagged, and routed to game mechanics and phases.

- §2.1 Hierarchy: the six-level tree is the canonical model for all content storage and retrieval.
- §2.2 Learning Units: defines the granularity at which the AI builder generates content sets (10-15 tasks per LU).
- §2.3 Block Types: determines which phase each block belongs to; block type is immutable once assigned.
- §2.4 Dual Code Format: both code formats must be present in every item — neither can be omitted.
- §2.5 Mandatory Tags: all eight tag groups are required for `approved` status; any missing tag locks the item in `draft`.

## Cross-references

- `core-principles.md §1.3` — the "No Busywork" rule mandates the `transition_skill` tag in §2.5; they are inseparable.
- `core-principles.md §1.2 Principle 1` — textbook-is-source-of-truth constrains `Source Layer` values in §2.3 (no purely invented content).
- `NETS-Homework-Engine-UNIFIED-Buzan.md §3` — PISA Framework defines valid values for `pisa_ref.proficiency_level` and `pisa_ref.process_category`.
- `NETS-Homework-Engine-UNIFIED-Buzan.md §4.4-§5.7` — Phase construction rules consume block types from §2.3; each phase pulls from its designated block type only.
- `standards/library/catalog/NETS-Game-Catalog-Summary.md` — valid values for the `game_mechanic` tag in §2.5.
- `agents/content-producer/SCHEMA.md` — the production agent's output template must map to §2.5 tag structure.
- `agents/content-producer/SKILLS.md` — builder pipeline step "Content Mapping" maps extracted concepts to block types per §2.3.
- All subject frameworks (standards/library/subject-family/) — inherit this architecture; subject-specific construction recipes produce content blocks of the types defined in §2.3.

## Verification

- [ ] Every deployed content item carries all eight tag groups from §2.5 (no field omitted).
- [ ] `transition_skill` is populated for every item (not null, not empty string).
- [ ] Both `primary_code` (UZ-format) and `alias_code` (dotted format) present in every `standard_ref`.
- [ ] Block type assignment matches the phase where the item appears (e.g., no `boss_question` block in Phase 3).
- [ ] Each LU generates 10-15 tasks with the correct Bloom's distribution: 4 Remember, 3 Understand, 3 Apply, 2 Analyze, 1-2 Evaluate/Create.
- [ ] Items with `review_status: "draft"` are not in the live content pool.
- [ ] `game_mechanic` value matches an entry in the Game Catalog (16 Default + 6 Interactive); removed games are never referenced.
