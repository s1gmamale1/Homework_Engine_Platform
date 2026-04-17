-- NETS Autonomous Homework Pipeline — Initial schema
-- Source: architecture spec §10 "State & Persistence"
--
-- Run against a Postgres 15+ instance. Idempotent (uses IF NOT EXISTS).
--
-- Usage:
--   psql "$DATABASE_URL" -f 001_init.sql

BEGIN;

-- =====================================================================
-- lessons
-- The canonical lesson after extraction. Immutable once written.
-- =====================================================================
CREATE TABLE IF NOT EXISTS lessons (
  lesson_id      text        PRIMARY KEY,
  subject        text        NOT NULL,
  grade          int         NOT NULL,
  lang           text        NOT NULL,
  pdf_uri        text        NOT NULL,
  md_uri         text,                       -- path to lesson.md in object storage
  md_hash        text,                       -- content hash; identity of the frozen doc
  extracted_at   timestamptz
);

CREATE INDEX IF NOT EXISTS lessons_subject_grade_lang_idx
  ON lessons (subject, grade, lang);

-- =====================================================================
-- phase_outputs
-- One row per phase per lesson. Many-to-one with lessons.
-- =====================================================================
CREATE TABLE IF NOT EXISTS phase_outputs (
  task_id        uuid,
  lesson_id      text        NOT NULL REFERENCES lessons(lesson_id),
  phase_id       text        NOT NULL,      -- 'phase_0a', 'phase_0b', 'phase_1' ... 'phase_7'
  output_json    jsonb       NOT NULL,      -- the structured phase deliverable (matches frameworks/schemas/{phase_id}.json)
  schema_valid   boolean     NOT NULL DEFAULT false,
  prompt_hash    text,                      -- SHA256 of assembled prompt; for cache analysis + reproducibility
  tokens_in      int,
  tokens_out     int,
  cost_usd       numeric(10,6),
  latency_ms     int,
  cache_hit_pct  numeric(5,2),
  created_at     timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (lesson_id, phase_id)
);

CREATE INDEX IF NOT EXISTS phase_outputs_task_idx
  ON phase_outputs (task_id);

-- =====================================================================
-- task_queue
-- The batch queue. Status machine drives the runner.
-- Workers claim rows with SELECT ... FOR UPDATE SKIP LOCKED.
-- =====================================================================
CREATE TABLE IF NOT EXISTS task_queue (
  task_id        uuid        PRIMARY KEY,
  subject        text        NOT NULL,
  grade          int         NOT NULL,
  lang           text        NOT NULL,
  lesson_id      text        NOT NULL,
  pdf_uri        text        NOT NULL,
  status         text        NOT NULL DEFAULT 'pending',  -- pending | extracting | phasing | assembling | done | failed
  attempts       int         NOT NULL DEFAULT 0,
  last_error     text,
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT task_queue_status_check
    CHECK (status IN ('pending','extracting','phasing','assembling','done','failed'))
);

CREATE INDEX IF NOT EXISTS task_queue_status_idx
  ON task_queue (status);

CREATE INDEX IF NOT EXISTS task_queue_subject_grade_lang_idx
  ON task_queue (subject, grade, lang);

-- Keep updated_at current on every UPDATE
CREATE OR REPLACE FUNCTION touch_updated_at() RETURNS trigger AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS task_queue_touch_updated_at ON task_queue;
CREATE TRIGGER task_queue_touch_updated_at
  BEFORE UPDATE ON task_queue
  FOR EACH ROW EXECUTE FUNCTION touch_updated_at();

-- =====================================================================
-- session_log
-- Append-only audit log. Every session emits one row per event.
-- =====================================================================
CREATE TABLE IF NOT EXISTS session_log (
  id             bigserial   PRIMARY KEY,
  task_id        uuid,
  stage          text        NOT NULL,       -- 'extract' | 'phase' | 'assemble'
  phase_id       text,                       -- null for extract/assemble
  event          text        NOT NULL,       -- 'start' | 'success' | 'retry' | 'fail'
  payload        jsonb,
  ts             timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT session_log_stage_check
    CHECK (stage IN ('extract','phase','assemble')),
  CONSTRAINT session_log_event_check
    CHECK (event IN ('start','success','retry','fail'))
);

CREATE INDEX IF NOT EXISTS session_log_task_idx
  ON session_log (task_id);

CREATE INDEX IF NOT EXISTS session_log_ts_idx
  ON session_log (ts);

COMMIT;

-- End of 001_init.sql
