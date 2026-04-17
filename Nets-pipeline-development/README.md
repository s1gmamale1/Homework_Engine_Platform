# NETS Autonomous Homework Pipeline

This tool takes a government textbook PDF and turns it into a gamified homework file. You point it at a PDF, run one command, and a few minutes later you have a ready-to-use lesson written in the textbook's own language (Uzbek or Russian) with flashcards, a story, games, a mission, a summary, a quiz, and a reflection.

No manual editing. No agent frameworks. No RAG. It's about 2,000 lines of Python talking to a Postgres queue and the Kimi K2 language model.

---

## What it does, end to end

You give it this:

- A PDF of one textbook chapter (say, Biology Grade 5, Section 1 in Uzbek)
- A small entry in a YAML file saying "this PDF is biology, grade 5, Uzbek, call it `biology_G5_uz_sec01`"

You run `nets-run seed` once, then `nets-run run`, and you get back:

- `storage/lessons/biology_G5_uz_sec01.md` — the cleaned-up chapter content (the "lesson")
- `storage/homeworks/biology_G5_uz_sec01.md` — the gamified homework, ~280 lines of Uzbek, ready to ship

Everything else — the prompts, the database rows, the logs — is handled automatically.

One lesson costs roughly **$0.12** in API calls and takes **about 2 minutes** to produce.

---

## The three things you need to know

### 1. Setup (one time)

You need Python 3.11+, Docker (for Postgres), and a Moonshot API key.

```bash
# 1. Create a Python virtual environment and install the pipeline
cd Nets-pipeline-development
python -m venv venv
source venv/Scripts/activate       # Windows
# source venv/bin/activate          # Mac/Linux
pip install -r requirements.txt
pip install -e .

# 2. Start Postgres in Docker (uses port 5433 to avoid conflicts)
docker run -d --name nets-pg \
  -e POSTGRES_USER=nets \
  -e POSTGRES_PASSWORD=nets_dev_pw \
  -e POSTGRES_DB=nets_pipeline \
  -p 5433:5432 \
  postgres:15

# 3. Apply the database schema
docker exec -i nets-pg psql -U nets -d nets_pipeline -f - < migrations/001_init.sql
docker exec -i nets-pg psql -U nets -d nets_pipeline -f - < migrations/002_validation.sql

# 4. Create your .env file
cp .env.example .env
# then edit .env — you need DATABASE_URL and MOONSHOT_API_KEY at minimum
```

A working `.env` looks like this:

```
DATABASE_URL=postgresql://nets:nets_dev_pw@localhost:5433/nets_pipeline
MOONSHOT_API_KEY=sk-...your-key-here...
STORAGE_PATH=./storage
MAX_CONCURRENT_TASKS=4
LOG_LEVEL=INFO
```

### 2. Commands you'll actually run

```bash
# Load a list of PDFs into the queue
nets-run seed --manifest pilot_manifest.yaml

# Process everything in the queue
nets-run run

# Check what's in the queue
nets-run status

# See how much you've spent and how the cache is performing
nets-run metrics

# If a task failed, see why
nets-run metrics --failures
```

That's the core loop. Seed, run, check.

### 3. How to add more textbooks

Edit `pilot_manifest.yaml` and list each chapter as its own task:

```yaml
tasks:
  - subject: biology
    grade: 5
    lang: uz
    lesson_id: biology_G5_uz_sec01
    pdf_uri: ../textbooks/biology/5/uz/biology_G5_uz_sec01.pdf

  - subject: biology
    grade: 5
    lang: uz
    lesson_id: biology_G5_uz_sec02
    pdf_uri: ../textbooks/biology/5/uz/biology_G5_uz_sec02.pdf
```

The important rule: **one task = one chapter**, not one task = whole textbook. The language model has a token budget per call, so a 60-page book won't fit in one extraction. Split your PDFs by chapter first.

---

## How the pipeline works under the hood

There are three stages. You never run them directly — `nets-run run` walks through all three for each task.

### Stage 1 — Extract

The pipeline reads the PDF, pulls out the text (using `pdfplumber` with `pymupdf` as backup), and asks Kimi to produce a clean Markdown version of the chapter. The result goes into `storage/lessons/<lesson_id>.md`.

Once a lesson is extracted, its SHA256 hash gets saved in the `lessons` table. Future runs see the hash and skip this stage — the cleaned lesson is frozen. This is important: every phase worker reads the same lesson.md, so reruns are deterministic.

### Stage 2 — Phases (9 parallel calls)

The lesson.md goes through 9 phases, each producing a different slice of the homework:

| Phase | What it produces |
|-------|------------------|
| **0-A** | Topic preview — 8 panels that introduce the lesson with an Uzbek cultural hook |
| **0-B** | Flashcards — quick vocabulary prep |
| **1** | Memory Sprint — rapid-fire quiz questions |
| **2** | Story Mode — a narrative that teaches the concept through a character |
| **3** | Game Breaks — 3 mini-games picked from a catalog of 17 |
| **4** | Mission — an applied real-world task |
| **5** | Radiant Summary — a mind-map style recap |
| **6** | Checkpoint — a mastery quiz |
| **7** | Reflection — closing questions that consolidate learning |

Phases 0-A through 6 run **in parallel** (one wave of 8 calls). Phase 7 runs after, because it needs outputs from phases 1, 3, 4, and 6 to reflect on them. The dependency list lives in `phase-graph.yaml`.

Each phase call reuses the same big system prompt (the subject framework + phase spec + game docs), which is ~30,000 tokens. Kimi's prompt cache means we pay full price for those tokens **once** and then ~25% price on every call afterward. In practice we see **99% cache hit rate** across a lesson's 9 phases.

### Stage 3 — Assemble

No language model call here. Pure Python. It reads all 9 phase JSON outputs from the `phase_outputs` table and formats them into one Markdown file using fixed templates. Output lands at `storage/homeworks/<lesson_id>.md`.

### The database

Five Postgres tables:

- **`lessons`** — one row per chapter. Holds the md_uri and md_hash so Stage 1 can skip itself on reruns.
- **`phase_outputs`** — one row per (lesson, phase). Holds the raw JSON Kimi returned plus token counts and cost.
- **`task_queue`** — the work list. Each row is one chapter waiting to be processed, or in-flight, or done, or failed.
- **`session_log`** — every Kimi call's start/retry/success/fail events with payloads. Your audit trail.
- **`validation_results`** — optional post-hoc quality checks from a second language model (Claude Haiku). Runs on demand via `nets-run validate`, doesn't gate the pipeline.

### How workers claim tasks safely

Multiple `nets-run run` workers can run at the same time. They grab tasks using Postgres's `SELECT ... FOR UPDATE SKIP LOCKED`, then atomically mark the row as `extracting` in the same transaction. Two workers can never claim the same task. If a worker crashes mid-task, the row sits there for 10 minutes and then gets reclaimed.

---

## File and folder layout

```
Nets-pipeline-development/
├── README.md                    ← this file
├── .env                         ← your secrets, not in git
├── .env.example                 ← template
├── pyproject.toml               ← Python package config
├── requirements.txt             ← runtime dependencies
├── requirements-dev.txt         ← linting / testing tools
├── phase-graph.yaml             ← which phases depend on which
├── pilot_manifest.yaml          ← list of textbooks to seed
│
├── Docs/
│   └── nets-pipeline-architecture.md   ← the full 16-section design spec
│
├── frameworks/                  ← the "rulebook" the model reads
│   ├── system/                  ← one prompt file per stage
│   │   ├── extraction.md        ← Stage 1 instructions
│   │   ├── phase_worker_base.md ← shared invariants for all 9 phases
│   │   ├── assembly.md          ← Stage 3 template
│   │   └── validator.md         ← rubric for the post-hoc validator
│   ├── unified/                 ← the 9 phase specs + unified Buzan schema
│   │   ├── schema.md
│   │   ├── phase_0a.md … phase_7.md
│   ├── subjects/                ← one file per subject (14 populated)
│   │   ├── biology.md, chemistry.md, matematika.md, …
│   ├── games/                   ← 17 game mechanic docs (01 through 21, with gaps)
│   └── schemas/                 ← JSON Schemas that enforce output shape
│       ├── lesson.json
│       └── phase_0a.json … phase_7.json
│
├── migrations/
│   ├── 001_init.sql             ← the 4 core tables
│   └── 002_validation.sql       ← validation_results table
│
├── src/
│   ├── nets_pipeline/           ← main package
│   │   ├── cli.py               ← the `nets-run` entry point
│   │   ├── config.py            ← reads .env
│   │   ├── db.py                ← Postgres connection pool
│   │   ├── kimi_client.py       ← Moonshot API wrapper
│   │   ├── pdf_reader.py        ← PDF → text
│   │   ├── prompt.py            ← layered prompt composition
│   │   ├── session.py           ← the compose → call → validate → log loop
│   │   ├── validator.py         ← JSON Schema enforcement
│   │   ├── phase_graph.py       ← loads phase-graph.yaml, computes waves
│   │   ├── scheduler.py         ← runs phases in waves with asyncio.gather
│   │   ├── balance.py           ← National Pride 55/45 tracker
│   │   ├── stages/
│   │   │   ├── extract.py       ← Stage 1
│   │   │   ├── phase.py         ← Stage 2 (one phase)
│   │   │   └── assemble.py      ← Stage 3 (deterministic rendering)
│   │   ├── storage.py           ← writes lesson.md and homework.md
│   │   ├── seed.py              ← populates task_queue
│   │   ├── batch.py             ← worker pool
│   │   ├── runner.py            ← the per-task micro cycle
│   │   ├── dashboard.py         ← metrics queries
│   │   └── logging_setup.py     ← structlog JSON output
│   └── nets_validator/          ← optional post-hoc quality checker
│       ├── client.py            ← wraps Anthropic / Gemini
│       ├── rubric.py            ← loads validator.md
│       ├── sweep.py             ← runs validation on unvalidated rows
│       └── review.py            ← queries the validation_results table
│
└── storage/
    ├── lessons/                 ← cleaned markdown chapters (frozen)
    └── homeworks/               ← final gamified output
```

---

## Costs and performance

Numbers from the Biology G5 Section 1 pilot (5-page PDF):

| Stage | Token input | Token output | Cache hit | Cost |
|-------|-------------|--------------|-----------|------|
| Extract | ~4,000 | ~3,500 | 0% | $0.012 |
| Phase 0-A | 70,312 | 1,435 | 99.4% | $0.014 |
| Phase 0-B | 69,529 | 404 | 99.4% | $0.012 |
| Phase 1 | 71,807 | 599 | 99.1% | $0.013 |
| Phase 2 | 72,615 | 733 | 99.1% | $0.013 |
| Phase 3 | 70,145 | 895 | 99.3% | $0.013 |
| Phase 4 | 74,456 | 737 | 99.0% | $0.013 |
| Phase 5 | 77,071 | 876 | 99.0% | $0.014 |
| Phase 6 | 74,739 | 924 | 99.0% | $0.014 |
| Phase 7 | 73,817 | 422 | 98.8% | $0.013 |
| **Total** | | | | **~$0.13** |

End-to-end time: ~2 minutes for one chapter. Most phases ran in 15-35 seconds.

Kimi pricing (reflected in the code): $0.60 per million input tokens, $2.50 per million output, $0.15 per million cached. The whole reason phases are cheap is the 99% cache hit rate on the static framework content.

---

## Known gaps

Be aware before scaling:

**Phase 3 game selection is not automated.** The framework spec describes a two-pool game selection algorithm with Bloom's taxonomy targeting. The code doesn't implement it. `phase-graph.yaml` has an empty `games_used: []` for phase 3. In the pilot, Kimi improvised game content from the phase_3.md text alone and happened to produce schema-valid JSON, but there's no guarantee of quality or consistency. Before seeding a full textbook you should either (a) pre-populate `games_used` in the YAML for each subject, or (b) build a proper game selector.

**Stale references in some framework files.** `phase_worker_base.md` mentions `quotes_database.json` and `task_injections.json`, and `phase_3.md` mentions `NETS-Interactive-Game-Catalog.md`. None of these files exist in the repo. Kimi ignores them silently. If you care about curated quotes for Phase 0-A and consistent task templates for Phase 4, you'll want to either create these files or edit the specs to drop the references.

**Gemini validator and S3 storage are stubs.** `nets_validator/client.py` has a `_GeminiValidator` class that raises `NotImplementedError`. `storage.py` only supports local filesystem. Both are fine for now — Claude Haiku works as the validator, and local storage is fast enough for the pilot.

**Only 14 of 32 subjects have frameworks.** The current 14 cover Math family, Science family, Language family (partial), and History family. Missing: Astronomy, Geography, Literature, Law, Economics, and the 9 Tarbiya/Sanat (ethics/arts) subjects. To add a subject, drop a new `frameworks/subjects/<name>.md` file following the existing pattern.

---

## Troubleshooting

**`psycopg cannot use the 'ProactorEventLoop'` (Windows)**
The CLI sets `WindowsSelectorEventLoopPolicy` automatically. If you're calling the pipeline from your own script, do the same before `asyncio.run`.

**`password authentication failed for user 'nets'`**
Your `.env` `DATABASE_URL` doesn't match how Docker was started. Recreate the container with the credentials you want, or update `.env`.

**`port 5432 is already in use`**
You have a native Postgres running. Either stop it, or start Docker on a different port (`-p 5433:5432`) and update `DATABASE_URL` to match.

**`MOONSHOT_API_KEY is not set`**
The `run` command needs it. `seed`, `status`, and `metrics` don't — they work without a key.

**Phase fails with "Schema validation failed twice"**
Kimi produced JSON that doesn't match the phase schema. Check `session_log.payload->'errors'` for the specific mismatches. The fix is usually in the phase spec or the schema — the task instruction already embeds the schema verbatim so Kimi should see it.

**Extraction returns truncated JSON**
The chapter is too long for Kimi's output budget. Split the PDF into smaller sections (one `§` per file is the norm). The extractor uses `max_tokens=16000`, which fits roughly 8-10 pages of dense Uzbek text.

**"Framework not found" when running**
You're trying to run a subject without a framework file. Check `frameworks/subjects/` — if your subject isn't listed, you need to add one.

---

## What this pipeline deliberately doesn't use

No LangChain. No LangGraph. No CrewAI. No n8n. No agent frameworks. No vector databases. No RAG. No retrievers. No embeddings.

It's a Postgres queue, an API client, and some prompt templating. When something breaks, you read `session_log` and see exactly what happened. That simplicity is the feature.

---

## Where to read more

- **`Docs/nets-pipeline-architecture.md`** — the full 16-section design spec. Every decision traces back to a numbered section.
- **`frameworks/unified/phase_*.md`** — what each phase is supposed to produce, in the operator's own words.
- **`frameworks/subjects/*.md`** — per-subject teaching rules.
- **`src/nets_pipeline/session.py`** — the 200-line core loop. If you only read one file, read this.
