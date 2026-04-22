# NETS Homework Pipeline — v2 Documentation

## Table of Contents
1. [System Overview](#1-system-overview)
2. [Architecture](#2-architecture)
3. [Requirements](#3-requirements)
4. [Setup Guide](#4-setup-guide)
5. [Running the Workflow](#5-running-the-workflow)
6. [File Structure](#6-file-structure)
7. [Database Reference](#7-database-reference)
8. [Useful Docker Commands](#8-useful-docker-commands)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. System Overview

NETS Pipeline v2 is an n8n workflow that takes a textbook chapter and generates a complete gamified homework session for NETS (National Education Transformation System). The user selects a subject, grade, language, chapter, and lesson number through a form. The pipeline reads the pre-split chapter text, sends it to Kimi AI for extraction, then generates all 9 homework phases **one by one** in a sequential loop.

**Output:** A single Markdown file containing the full homework session — all 9 phases assembled in order.

### Homework Phases Generated

| Phase | Name | Description |
|---|---|---|
| 0-A | Theme Preview | Introduction panels, gate quote, learning goal |
| 0-B | Flash Cards | Key term cards front/back |
| 1 | Memory Sprint | Quick recall questions |
| 2 | Story Mode | Narrative with embedded checkpoints |
| 3 | Game Breaks | 3 interactive games (Tile Match, Puzzle Lock, Tic-Tac-Toe AI) |
| 4 | Real-Life Challenge | Scenario-based application questions |
| 5 | Consolidation | Mnemonic/memory technique exercise |
| 6 | Final Boss | Boss battle — HP-based questions (Easy/Medium/Hard) |
| 7 | Reflection | TEFCAS reflection prompts + BOST goal recall |

---

## 2. Architecture

### 2.1 Workflow Flow

```
┌─────────────────────────────────────────────────────────────────┐
│  ENTRY POINT A — Form                                           │
│  Form Trigger → Build Task From Form → Set Task                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌─────────────────────────────────────────────────────────────────┐
│  ENTRY POINT B — Queue                                          │
│  Manual Trigger → Pull One Task → Has Task? ──No──► (stop)     │
│                                      │Yes                       │
│                                   Set Task                      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                       Mark Extracting
                               │
                     Extract Chapter Text
                               │
                    Build Extraction Prompt
                               │
                          Kimi Extract          [kimi-k2.5 | 6,000 tokens]
                               │
                      Parse & Save Lesson ──► {lesson_id}_lesson.json
                               │
                       Save Lesson to DB
                               │
                      Check Done Phases
                               │
                       Build Phase List  (emits 9 items)
                               │
                    ┌─ Loop Phases ◄────────────────────┐
                    │  (one phase at a time)             │
                    │                                    │
              Compose Phase Prompt                       │
                    │                                    │
               Kimi Phase        [kimi-k2-turbo-preview] │
                    │                                    │
            Parse Phase Output                          │
                    │                                    │
            Save Phase to DB ───────────────────────────┘
                    │
            (all 9 done)
                    │
            Load All Phases
                    │
           Assemble Homework ──► {lesson_id}_homework.md
                    │
               Mark Done
                    │
               Log Done
```

### 2.2 Node Reference

| Node | Type | What It Does |
|---|---|---|
| Form Trigger | Form | Collects Subject, Grade, Language, Qism, Chapter, Lesson, Theme from user |
| Build Task From Form | Code | Maps form inputs to a chapter file path. Generates `task_id` and `lesson_id`. Validates chapter and lesson > 0 |
| Manual Trigger | Manual | Starts the queue-pull path |
| Pull One Task | Postgres | SELECTs the oldest `pending` task from `nets_task_queue` |
| Has Task? | IF | Stops execution if queue is empty |
| Set Task | Code | Normalizes task fields into a standard object passed to all downstream nodes |
| Mark Extracting | Postgres | UPSERT — sets task status to `extracting` |
| Extract Chapter Text | Code | Reads the `.txt` lesson file from disk. Cleans text (removes markers, timestamps, duplicate lines) |
| Build Extraction Prompt | Code | Builds the Kimi API payload for lesson extraction using `kimi-k2.5` |
| Kimi Extract | HTTP | POST to Moonshot API — extracts structured lesson JSON from chapter text |
| Parse & Save Lesson | Code | Parses Kimi response, writes `{lesson_id}_lesson.json` to `/home/node/nets/nets-output/` |
| Save Lesson to DB | Postgres | Inserts/updates lesson record in `nets_lessons` |
| Check Done Phases | Postgres | Queries `nets_phase_outputs` to find already-completed phases (resume support) |
| Build Phase List | Code | Emits 9 phase items. Skips phases already in DB. Falls back to all 9 if nothing to skip |
| Loop Phases | Split In Batches | Processes one phase at a time. Routes to `Compose Phase Prompt` while iterating, routes to `Load All Phases` when done |
| Compose Phase Prompt | Code | Reads framework files from disk. Builds the full layered Kimi prompt for the current phase |
| Kimi Phase | HTTP | POST to Moonshot API — generates phase content JSON |
| Parse Phase Output | Code | Strips markdown fences from Kimi response. Parses JSON. Throws named error if invalid |
| Save Phase to DB | Postgres | UPSERT phase output into `nets_phase_outputs` |
| Load All Phases | Postgres | Loads all 9 phases ordered by phase sequence |
| Assemble Homework | Code | Combines all phases into a single Markdown document |
| Mark Done | Postgres | Sets task status to `done` |
| Log Done | Postgres | Inserts success entry into `nets_session_log` |

### 2.3 Kimi API Usage

| Node | Model | Max Tokens | Purpose |
|---|---|---|---|
| Kimi Extract | `kimi-k2.5` | 6,000 | Lesson extraction from chapter text |
| Kimi Phase | `kimi-k2-turbo-preview` | See table below | Per-phase homework content |

**Per-phase token limits (Compose Phase Prompt):**

| Phase | Max Tokens |
|---|---|
| phase_0a | 8,000 |
| phase_0b | 2,000 |
| phase_1 | 3,000 |
| phase_2 | 5,000 |
| phase_3 | 5,000 |
| phase_4 | 3,000 |
| phase_5 | 3,000 |
| phase_6 | 5,000 |
| phase_7 | 3,000 |

> **Note:** If you see `invalid JSON` errors for a phase, its max_tokens is too low. Increase it in the `Compose Phase Prompt` node.

### 2.4 Subject Framework Mapping

`Compose Phase Prompt` loads the correct subject framework file dynamically:

| Form Subject | Framework File Loaded |
|---|---|
| Matematika | `subjects/matematika.md` |
| Tarix | `subjects/tarix.md` |
| Geografiya | `subjects/tarix.md` (closest match) |
| Ona_tili / Adabiyot | `subjects/ona_tili.md` |
| Ingliz_tili | `subjects/english.md` |
| Rus_tili | `subjects/rus_tili.md` |
| Tabiiy_fanlar / Biologiya | `subjects/biology.md` |
| Kimyo | `subjects/chemistry.md` |
| Fizika | `subjects/physics.md` |
| Algebra | `subjects/algebra.md` |
| Geometriya | `subjects/geometriya.md` |
| Informatika / Texnologiya | `subjects/matematika.md` (closest match) |

### 2.5 Output Files

All output files go to `/home/node/nets/nets-output/` inside Docker (= `D:\n8n\nets-output\` on Windows):

| File | Description |
|---|---|
| `{lesson_id}_lesson.json` | Structured lesson data extracted from the chapter |
| `{lesson_id}_homework.md` | Final assembled homework — all 9 phases |

---

## 3. Requirements

### 3.1 Software

| Software | Version | Notes |
|---|---|---|
| Docker Desktop | Latest | Must be running before anything else |
| n8n | Latest (self-hosted) | Runs inside Docker as `n8n-n8n-1` |
| PostgreSQL | 16-alpine | Runs inside Docker as `n8n-postgres-1` |
| Python | 3.8+ | For pre-processing scripts on Windows host |
| PyMuPDF | Latest | `pip install pymupdf` — PDF to text extraction |

### 3.2 API Keys

| Service | Where Used |
|---|---|
| Moonshot (Kimi) API | Hardcoded in `Build Extraction Prompt` and `Compose Phase Prompt` nodes |

### 3.3 n8n Credentials

| Credential Name | Type | Connection Details |
|---|---|---|
| NETS Postgres | PostgreSQL | Host: `postgres`, Port: `5432`, DB: from env, User: from env |

---

## 4. Setup Guide

### 4.1 Docker Setup (First Time Only)

**Step 1 — Create project folder and docker-compose.yml**

Create `D:\n8n\` and place this `docker-compose.yml` inside:

```yaml
volumes:
  n8n_data:
  postgres_data:

services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 5s
      timeout: 5s
      retries: 10

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=${POSTGRES_DB}
      - DB_POSTGRESDB_USER=${POSTGRES_USER}
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - TZ=${GENERIC_TIMEZONE}
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
      - N8N_RUNNERS_ENABLED=true
      - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
      - NODE_FUNCTION_ALLOW_BUILTIN=fs,path,crypto,https
      - NODE_FUNCTION_ALLOW_EXTERNAL=*
    volumes:
      - n8n_data:/home/node/.n8n
      - D:/n8n:/home/node/nets
      - "D:/Class A Education/Books:/home/node/books"
    depends_on:
      postgres:
        condition: service_healthy
```

Create a `.env` file in the same folder:

```env
POSTGRES_USER=n8n
POSTGRES_PASSWORD=your_password_here
POSTGRES_DB=n8n
GENERIC_TIMEZONE=Asia/Tashkent
N8N_ENCRYPTION_KEY=your_encryption_key_here
```

**Step 2 — Start containers**

```bash
cd D:\n8n
docker compose up -d
```

**Step 3 — Verify containers are running**

```bash
docker ps
```

Both `n8n-n8n-1` and `n8n-postgres-1` should show status `Up`.

---

### 4.2 Database Setup (First Time Only)

```bash
docker exec -it n8n-postgres-1 psql -U n8n -d n8n
```

Run the following SQL:

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS nets_task_queue (
    task_id     UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject     TEXT NOT NULL,
    grade       INT  NOT NULL,
    lang        TEXT NOT NULL,
    lesson_id   TEXT NOT NULL,
    pdf_uri     TEXT,
    status      TEXT NOT NULL DEFAULT 'pending',
    created_at  TIMESTAMPTZ DEFAULT now(),
    updated_at  TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS nets_lessons (
    lesson_id    TEXT PRIMARY KEY,
    subject      TEXT,
    grade        INT,
    lang         TEXT,
    pdf_uri      TEXT,
    md_uri       TEXT,
    extracted_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS nets_phase_outputs (
    id           SERIAL PRIMARY KEY,
    task_id      UUID,
    lesson_id    TEXT NOT NULL,
    phase_id     TEXT NOT NULL,
    output_json  JSONB,
    schema_valid BOOLEAN DEFAULT false,
    tokens_in    INT DEFAULT 0,
    tokens_out   INT DEFAULT 0,
    cost_usd     NUMERIC(10,6) DEFAULT 0,
    latency_ms   INT DEFAULT 0,
    created_at   TIMESTAMPTZ DEFAULT now(),
    UNIQUE (lesson_id, phase_id)
);

CREATE TABLE IF NOT EXISTS nets_session_log (
    id         SERIAL PRIMARY KEY,
    task_id    UUID,
    stage      TEXT,
    event      TEXT,
    payload    JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);
```

Exit: `\q`

---

### 4.3 Prepare Textbook Files (First Time Per Grade/Language)

The workflow reads chapter text files from this folder structure on Windows:

```
D:\n8n\books\grade_5\uz\
  tarix\
    chapter_01\
      lesson_01.txt
      lesson_02.txt
    chapter_02\
      lesson_01.txt
  matematika\
    1-qism\
      chapter_01\
        lesson_01.txt
```

**Step 1 — Extract PDFs to .txt**

```bash
pip install pymupdf
python extract_pdfs.py
```

Creates a `.txt` sidecar next to each PDF in `D:\n8n\books\grade_5\uz\`.

**Step 2 — Split into chapter/lesson folders**

```bash
python split_math_chapters.py
python split_other_subjects.py
```

Reads flat `.txt` files and writes the chapter/lesson folder structure.

**Step 3 — Verify inside Docker**

```bash
docker exec n8n-n8n-1 sh -c "ls /home/node/nets/books/grade_5/uz/tarix/chapter_01/"
```

Should list `lesson_01.txt`, `lesson_02.txt`, etc.

---

### 4.4 Framework Files

Place framework files in `D:\n8n\frameworks\` (auto-mounted into Docker):

```
D:\n8n\frameworks\
  system\
    phase_worker_base.md
    extraction.md
  unified\
    schema.md
    phase_0a.md  phase_0b.md  phase_1.md  ...  phase_7.md
  subjects\
    matematika.md  tarix.md  ona_tili.md  english.md  rus_tili.md
    biology.md  chemistry.md  physics.md  algebra.md  geometriya.md
    jahon_tarixi.md  ozbekiston_tarixi.md
  schemas\
    lesson.json
    phase_0a.json  phase_0b.json  ...  phase_7.json
  games\
    03_Tile_Match.md  13_Tic_Tac_Toe_AI.md  18_Puzzle_Lock.md  (+ others)
```

> If a file is missing, the workflow silently skips it — no crash, just less context for Kimi.

---

### 4.5 Import Workflow into n8n

1. Open `http://localhost:5678`
2. Go to **Workflows → Import from File**
3. Select `NETS Main Pipeline v2.json`
4. Go to **Settings → Credentials** — verify `NETS Postgres` connects successfully
5. **Activate** the workflow (green toggle, top-right)

---

## 5. Running the Workflow

### 5.1 Before Every Session

Check Docker is running:

```bash
docker ps
```

If containers are not running:

```bash
cd D:\n8n
docker compose up -d
```

Verify the workflow is **active** in n8n (`http://localhost:5678`).

---

### 5.2 Generating Homework (Form)

1. Open the **Form Trigger** node in n8n
2. Copy the **Production URL**
3. Open it in your browser
4. Fill in the form:

| Field | Description | Example |
|---|---|---|
| Subject | Dropdown — select subject | `Tarix` |
| Grade | Dropdown — select grade | `5` |
| Language | `uz` or `ru` | `uz` |
| Qism | Book part — `none`, `1-qism`, `2-qism` | `none` |
| Chapter | Chapter number (must be ≥ 1) | `1` |
| Lesson | Lesson number within chapter (must be ≥ 1) | `1` |
| Theme | Optional — lesson topic hint | `Qadimgi Misr` |

5. Submit — watch **Executions** tab in n8n for progress

---

### 5.3 Generating from Queue (Manual Trigger)

If tasks exist in the queue with `status = pending`:

1. Click **Manual Trigger** node
2. Click **Test workflow**

The workflow picks the oldest pending task and processes it.

---

### 5.4 Finding the Output

```
D:\n8n\nets-output\{lesson_id}_homework.md
```

Example: `tarix_g5_uz_ch01_l01_homework.md`

---

## 6. File Structure

| Path (Windows) | Path (Docker) | Contents |
|---|---|---|
| `D:\n8n\books\` | `/home/node/nets/books/` | Chapter `.txt` files |
| `D:\n8n\frameworks\` | `/home/node/nets/frameworks/` | Framework `.md` and `.json` files |
| `D:\n8n\nets-output\` | `/home/node/nets/nets-output/` | Generated lesson JSON and homework Markdown |

---

## 7. Database Reference

### Tables

| Table | Key | Description |
|---|---|---|
| `nets_task_queue` | `task_id` UUID | One row per submitted task. Tracks processing status |
| `nets_lessons` | `lesson_id` TEXT | One row per extracted lesson |
| `nets_phase_outputs` | `(lesson_id, phase_id)` | One row per phase per lesson. ON CONFLICT DO UPDATE |
| `nets_session_log` | `id` SERIAL | Audit log — one row per completed session |

### Task Status Values

| Status | Meaning |
|---|---|
| `pending` | Queued, not yet started |
| `extracting` | Text extraction and phase generation in progress |
| `done` | All 9 phases generated, homework assembled |

### lesson_id Format

```
{subject_folder}_g{grade}_{lang}_ch{chapter}_l{lesson}
```

Example: `tarix_g5_uz_ch01_l02`

---

## 8. Useful Docker Commands

### Container Management

```bash
# Start all containers
docker compose up -d

# Stop all containers
docker compose down

# Restart Postgres only
docker stop n8n-postgres-1 && docker start n8n-postgres-1

# Restart n8n only
docker restart n8n-n8n-1

# Check running containers
docker ps

# Watch n8n logs live
docker logs -f n8n-n8n-1
```

### Database — Inspection

```bash
# See all lesson IDs and their phase counts
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "SELECT lesson_id, COUNT(*) FROM nets_phase_outputs GROUP BY lesson_id;"

# See all tasks and their status
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "SELECT lesson_id, subject, grade, status FROM nets_task_queue ORDER BY created_at DESC;"

# See phase details for a specific lesson
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "SELECT phase_id, tokens_out, cost_usd, latency_ms FROM nets_phase_outputs WHERE lesson_id = 'PASTE_LESSON_ID';"

# Check total API cost per lesson
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "SELECT lesson_id, ROUND(SUM(cost_usd)::numeric,4) AS cost_usd FROM nets_phase_outputs GROUP BY lesson_id ORDER BY cost_usd DESC;"
```

### Database — Maintenance

```bash
# Delete all phases for a lesson (to regenerate it)
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "DELETE FROM nets_phase_outputs WHERE lesson_id = 'PASTE_LESSON_ID';"

# Reset a stuck task back to pending
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c \
  "UPDATE nets_task_queue SET status='pending' WHERE lesson_id = 'PASTE_LESSON_ID';"

# Delete a lesson completely (all tables)
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c "
  DELETE FROM nets_phase_outputs WHERE lesson_id = 'PASTE_LESSON_ID';
  DELETE FROM nets_lessons      WHERE lesson_id = 'PASTE_LESSON_ID';
  DELETE FROM nets_task_queue   WHERE lesson_id = 'PASTE_LESSON_ID';"

# Clear session log
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c "TRUNCATE nets_session_log;"
```

### File System

```bash
# List available books inside Docker
docker exec n8n-n8n-1 sh -c "find /home/node/nets/books -type d | sort"

# Check a specific chapter folder
docker exec n8n-n8n-1 sh -c "ls /home/node/nets/books/grade_5/uz/tarix/chapter_01/"

# List generated homework files
docker exec n8n-n8n-1 sh -c "ls /home/node/nets/nets-output/"

# List all framework files
docker exec n8n-n8n-1 sh -c "find /home/node/nets/frameworks -type f | sort"
```

---

## 9. Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `Chapter file not found` | `.txt` file doesn't exist at the expected path in Docker | Run `extract_pdfs.py` then `split_other_subjects.py`. Verify with `docker exec n8n-n8n-1 sh -c "ls /home/node/nets/books/grade_5/uz/{subject}/chapter_01/"` |
| `Phase phase_X invalid JSON` | Kimi response truncated — max_tokens too low | Increase max_tokens for that phase in `Compose Phase Prompt` node |
| `Lesson number must be 1 or greater` | Lesson form field was 0, empty, or negative | Enter a valid lesson number ≥ 1 |
| `No task_id in input` | Task data not passed correctly through node chain | Check `Set Task` node — it should receive task_id from either path |
| Postgres connection error | Postgres container not running | `docker start n8n-postgres-1` then re-test credential in n8n |
| Workflow stuck on `extracting` | Previous run crashed mid-execution | Reset: `UPDATE nets_task_queue SET status='pending' WHERE lesson_id = 'ID';` |
| `Module 'https' is disallowed` | `NODE_FUNCTION_ALLOW_BUILTIN` missing `https` | Add `https` to `NODE_FUNCTION_ALLOW_BUILTIN` in docker-compose.yml and restart |
