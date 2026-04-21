-- NETS Pipeline Tables
-- Run once against the n8n Postgres database
-- Connect: host=localhost port=5432 db=n8n user=n8n password=mypro98

-- Canonical lesson after extraction. Immutable once written.
CREATE TABLE IF NOT EXISTS nets_lessons (
  lesson_id      text PRIMARY KEY,
  subject        text NOT NULL,
  grade          int NOT NULL,
  lang           text NOT NULL,
  pdf_uri        text,
  md_uri         text,
  md_hash        text,
  extracted_at   timestamptz DEFAULT now()
);

-- One row per phase per lesson.
CREATE TABLE IF NOT EXISTS nets_phase_outputs (
  task_id        uuid,
  lesson_id      text REFERENCES nets_lessons(lesson_id),
  phase_id       text NOT NULL,
  output_json    jsonb,
  schema_valid   boolean DEFAULT false,
  prompt_hash    text,
  tokens_in      int DEFAULT 0,
  tokens_out     int DEFAULT 0,
  cost_usd       numeric(10,6) DEFAULT 0,
  latency_ms     int DEFAULT 0,
  cache_hit_pct  numeric(5,2) DEFAULT 0,
  created_at     timestamptz DEFAULT now(),
  PRIMARY KEY (lesson_id, phase_id)
);

-- The batch queue — status machine drives the runner.
CREATE TABLE IF NOT EXISTS nets_task_queue (
  task_id        uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  subject        text NOT NULL,
  grade          int NOT NULL,
  lang           text NOT NULL,
  lesson_id      text NOT NULL,
  pdf_uri        text NOT NULL,
  status         text NOT NULL DEFAULT 'pending',
  attempts       int DEFAULT 0,
  last_error     text,
  created_at     timestamptz DEFAULT now(),
  updated_at     timestamptz DEFAULT now()
);

-- Append-only audit log. Every session emits one row.
CREATE TABLE IF NOT EXISTS nets_session_log (
  id             bigserial PRIMARY KEY,
  task_id        uuid,
  stage          text,
  phase_id       text,
  event          text,
  payload        jsonb,
  ts             timestamptz DEFAULT now()
);

-- Validation results (written by WF-06 async validator)
CREATE TABLE IF NOT EXISTS nets_validation_results (
  id             bigserial PRIMARY KEY,
  task_id        uuid,
  lesson_id      text,
  phase_id       text,
  check_type     text,
  passed         boolean,
  notes          text,
  checked_at     timestamptz DEFAULT now()
);

-- Seed first task: Grade 5 Math, Theme 1, Uzbek
INSERT INTO nets_task_queue (subject, grade, lang, lesson_id, pdf_uri, status)
VALUES (
  'matematika',
  5,
  'uz',
  'uz-mat-g5-theme1',
  '/home/node/books/Grade 5/Uz/Math/5-sinf_matematika_darslik_2024_UZ.pdf',
  'pending'
)
ON CONFLICT DO NOTHING;
