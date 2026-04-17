-- NETS Pipeline — Migration 002: validation_results
-- Source: architecture spec §14 "Post-Hoc Validation"
--
-- Holds rubric outcomes from the async validator (Haiku/Gemini).
-- Non-blocking: rows here never affect task_queue status.

BEGIN;

CREATE TABLE IF NOT EXISTS validation_results (
  id               bigserial   PRIMARY KEY,
  lesson_id        text        NOT NULL,
  phase_id         text        NOT NULL,
  validator_model  text        NOT NULL,      -- 'claude-haiku-4-5-...' | 'gemini-flash-...'
  validated_at     timestamptz NOT NULL DEFAULT now(),

  -- Overall verdict: 'pass' (all rubrics OK), 'flag' (review queue), 'fail' (clear violation)
  verdict          text        NOT NULL,
  verdict_summary  text,                       -- short human-readable one-liner

  -- Per-rubric detail. Stored as JSONB so the rubric can evolve without migrations.
  -- Expected shape:
  --   { "language_register":   {"pass": true,  "notes": "..."},
  --     "framework_compliance":{"pass": true,  "notes": "..."},
  --     "factual_grounding":   {"pass": false, "notes": "claim 'X' not in lesson"},
  --     "age_appropriate":     {"pass": true,  "notes": "..."} }
  rubric_scores    jsonb       NOT NULL,

  -- Raw model response for audit
  raw_response     jsonb,

  CONSTRAINT validation_verdict_check
    CHECK (verdict IN ('pass','flag','fail')),
  CONSTRAINT validation_phase_fk
    FOREIGN KEY (lesson_id, phase_id)
    REFERENCES phase_outputs(lesson_id, phase_id)
    ON DELETE CASCADE,
  CONSTRAINT validation_unique
    UNIQUE (lesson_id, phase_id, validator_model)
);

CREATE INDEX IF NOT EXISTS validation_verdict_idx
  ON validation_results (verdict);

CREATE INDEX IF NOT EXISTS validation_lesson_idx
  ON validation_results (lesson_id);

COMMIT;

-- End of 002_validation.sql
