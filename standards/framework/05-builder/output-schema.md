---
name: Output Schema — Homework .md Format + Metadata JSON
status: v0.1 draft — validated against §22 only
layer: 5 (builder)
source: UNIFIED §16 (lines 3188-3364)
---

# Output Schema — Homework .md Format + Metadata JSON

Defines the exact format every homework file must conform to. Produced by Step 6 of `homework-builder.md`. Validated by Gate 1 of `verification-checklist.md`.

---

## Part A — Homework `.md` file structure

Every homework `.md` file uses this section order. No sections may be reordered or skipped (absent phases are omitted, not placeholder-commented).

```markdown
# {SUBJECT} {GRADE} — {CHAPTER TITLE} — {SECTION TITLE}
**Lesson ID:** {lesson_id}
**Mode:** {easy|hard}
**Family:** {aniq-fanlar|tabiy-fanlar|til-fanlar|ijtimoiy-fanlar}
**Language:** {uz|ru}
**Textbook:** {textbook_ref.chapter} › {textbook_ref.section} (pp. {page_range})
**Generated:** {timestamp}

---

## Phase 0-A — Preview
{panel content — per phase-0a-preview.md spec}

---

## Phase 0-B — Flash Cards
{flash card content — per phase-0b-flashcards.md spec}

---

## Phase 1 — Memory Sprint
{memory sprint items — per phase-01-memory-sprint.md spec}

---

## Phase 2 — Reading (Til Fanlar only, Hard mode only)
{story + checkpoints — per phase-02-reading.md spec}

---

## Phase 3 — Game Breaks
{game content — per phase-03-game-breaks.md spec}

---

## Phase 4 — Real-Life Challenge (Aniq/Tabiy Fanlar only, Hard mode only)
{scenario content — per phase-04-real-life.md spec}

---

## Phase 5 — Consolidation (conditional)
{consolidation content — per phase-05-consolidation.md spec}

---

## Phase 6 — Final Challenge
{boss content — per phase-06-final-challenge.md spec}

---

## Phase 7 — Reflection
{reflection prompt — per phase-07-reflection.md spec}
```

---

## Part B — Question / item format

Every question or item in every phase must conform to this inline format:

```
{prompt text}

A) {option}
B) {option}
C) {option}
D) {option}

✓ Correct: {answer}
[Bloom: L{1-6} | PISA: L{1-6} | Skill: {atomic_skill_id}]
[Damage: -{10|20|30} HP]   ← Final Challenge items only
[CAPTURE]                  ← Calculation steps in Phase 3/4/5 (Math/Science)

Hint 1: {hint text}
Hint 2: {hint text}
Hint 3: {hint text}
```

Fields that are not applicable for a given format may be omitted (e.g., options for True/False; hints for Final Boss).

### Answer formats

| Format key | When used | Correct answer value |
|------------|-----------|---------------------|
| `exact` | Single correct string or number | Exact string/number |
| `numeric_range` | Calculated numeric answer with tolerance | `{min}–{max}` |
| `multiple_choice` | MC items | Letter: `A`, `B`, `C`, or `D` |
| `matching_pairs` | Tile match, pairing exercises | Array of `[left, right]` pairs |
| `ordered_list` | Sequencing tasks | Ordered array of items |
| `open_rubric` | Productive/creative output | Rubric string (see rubric format below) |

### Rubric format (open_rubric items)

```
Rubric:
- {criterion}: {max_points} pts — {description}
- {criterion}: {max_points} pts — {description}
Total: {sum} pts
```

### Hint chain

Progressive hints, from least revealing to most revealing. Maximum 3 hints. Not available in Phase 6 (Final Challenge). Hints must not give away the answer directly — they narrow down the approach.

---

## Part C — Metadata JSON schema

Written alongside the `.md` file as `{lesson_id}-meta.json`. Source: UNIFIED §16 JSON Schema.

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
        "subject": {
          "type": "string",
          "enum": ["math", "reading", "science", "history", "biology", "chemistry",
                   "physics", "geography", "informatics", "english",
                   "uzbek_language", "russian_language"]
        },
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
        "domain": {
          "type": "string",
          "enum": ["mathematics", "reading", "science", "creative_thinking"]
        },
        "competency": {
          "type": "string",
          "description": "Specific PISA competency targeted"
        },
        "transition_skill": {
          "type": "string",
          "description": "MANDATORY. Which Level N->N+1 transition this task supports.",
          "examples": [
            "L1->L2: extract from simple charts",
            "L2->L3: sequential decision-making",
            "L3->L4: select and integrate representations"
          ]
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
          "enum": ["memory_sprint", "flashcards", "tile_match", "sentence_fill",
                   "memory_palace", "story_mode", "adaptive_quiz", "mystery_box",
                   "movement_breaks", "why_chain", "peer_teaching",
                   "real_life_challenge", "reflection_journal",
                   "final_boss", "creative_lab"]
        },
        "format": {
          "type": "string",
          "description": "Specific interaction format within the mechanic"
        },
        "ui_template_id": { "type": "string" }
      }
    },
    "content": {
      "type": "object",
      "required": ["question_text", "language", "answer"],
      "properties": {
        "question_text": {
          "type": "string",
          "description": "Question in target language (uz or ru)"
        },
        "question_text_secondary": {
          "type": "string",
          "description": "Question in secondary language if bilingual"
        },
        "language": { "type": "string", "enum": ["uz", "ru"] },
        "media": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["image", "audio", "video", "animation", "diagram"]
              },
              "url": { "type": "string", "format": "uri" },
              "alt_text": { "type": "string" }
            }
          }
        },
        "answer": {
          "type": "object",
          "properties": {
            "correct": {
              "description": "Correct answer — string, number, array, or object depending on format"
            },
            "format": {
              "type": "string",
              "enum": ["exact", "numeric_range", "multiple_choice",
                       "matching_pairs", "ordered_list", "open_rubric"]
            },
            "rubric": {
              "type": "string",
              "description": "For open_rubric format: scoring rubric text"
            },
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
          "description": "Progressive hints — max 3. Not available in Final Boss (Phase 6)."
        }
      }
    },
    "difficulty": {
      "type": "object",
      "properties": {
        "irt_theta": {
          "type": "number",
          "description": "IRT difficulty parameter (-3 to +3)"
        },
        "estimated_minutes": { "type": "number", "minimum": 0.25, "maximum": 10 },
        "cognitive_load": {
          "type": "string",
          "enum": ["low", "medium", "high"]
        }
      }
    },
    "prerequisites": {
      "type": "array",
      "items": { "type": "string" },
      "description": "curriculum_standard.primary_code values that must be mastered first",
      "example": ["UZ-MATH-4-DIV-03", "UZ-MATH-5-FRAC-01"]
    },
    "session_placement": {
      "type": "object",
      "properties": {
        "journey_step": { "type": "integer", "minimum": 0, "maximum": 7 },
        "step_name": {
          "type": "string",
          "enum": ["preview", "flashcards", "memory_sprint", "story_mode",
                   "game_breaks", "real_life_challenge", "consolidation",
                   "final_boss", "reflection"]
        }
      }
    },
    "ai_tier": {
      "type": "integer",
      "enum": [1, 2, 3],
      "description": "1 = template/open-source · 2 = mid-range (Haiku) · 3 = premium (Sonnet/Opus)"
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
        "created_by": {
          "type": "string",
          "enum": ["human_teacher", "ai_tier1", "ai_tier2", "ai_tier3"]
        },
        "reviewed_by": { "type": "string" },
        "review_status": {
          "type": "string",
          "enum": ["draft", "ai_generated", "teacher_reviewed", "approved", "deprecated"]
        },
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

## Part D — Session-level metadata (top of metadata JSON)

In addition to per-task schema above, the top-level session record wraps all tasks:

```json
{
  "lesson_id": "HW-MAT7-CH3-S2-UZ",
  "subject": "math",
  "grade": 7,
  "mode": "hard",
  "family": "aniq-fanlar",
  "language": "uz",
  "timestamp": "2026-04-21T00:00:00Z",
  "textbook_ref": { "chapter": "3", "section": "2", "page_range": "45-52" },
  "verification_log": {
    "gates_passed": 11,
    "gates_failed": 0,
    "retries": 0,
    "status": "approved"
  },
  "variant_pool": [
    { "phase": 1, "item_index": 2, "variant": { "...": "alternate item" } }
  ],
  "capture_rubrics": {
    "phase_3_adaptive_quiz": "...",
    "phase_4_real_life": "..."
  },
  "tasks": [ { "...": "per-task records per schema above" } ]
}
```

**`variant_pool`:** Alternate items for each phase, used in the remediation path when a student scores below the pass threshold (60%). At minimum, one variant per graded item.

**`capture_rubrics`:** Per-phase rubrics for evaluating step-by-step captured work. Required for Aniq Fanlar and Tabiy Fanlar in Phase 3 (Adaptive Quiz), Phase 4 (Real-Life), and Phase 5 (Consolidation).

**`verification_log`:** Written by the builder at the end of Step 5. Records gate results, retry counts, and final status. `status` must be `"approved"` before the session is shipped.
