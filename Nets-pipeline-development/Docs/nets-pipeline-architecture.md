# NETS — Autonomous Homework Generation Pipeline
## Architecture Specification

**Document meta:** Architecture Specification · v0.1 · Draft · Claude Satter / NETS
**Audience:** Engineering
**Scope:** System + Cycle + Integration Points
**Out of scope:** Framework content

System-level design for the NETS content engine — turning government textbooks into gamified, grade-calibrated, multilingual homework at the scale of an entire curriculum, without a human in the loop.

---

## Contents

1. [Architectural Principles](#-01--architectural-principles)
2. [System Topology](#-02--system-topology)
3. [The Macro Cycle — Batch Runner](#-03--the-macro-cycle--batch-runner)
4. [The Micro Cycle — Per-Lesson Pipeline](#-04--the-micro-cycle--per-lesson-pipeline)
5. [Stage 01 — PDF Extraction Session](#-05--stage-01--pdf-extraction-session)
6. [Stage 02 — Phase Sessions (Parallel)](#-06--stage-02--phase-sessions-parallel)
7. [Stage 03 — Assembly Session](#-07--stage-03--assembly-session)
8. [Session Anatomy](#-08--session-anatomy)
9. [Framework Integration Points — Summary](#-09--framework-integration-points--summary)
10. [State & Persistence](#-10--state--persistence)
11. [Kimi API Configuration](#-11--kimi-api-configuration)
12. [Tooling Stack](#-12--tooling-stack)
13. [Observability & Failure Modes](#-13--observability--failure-modes)
14. [Post-Hoc Validation (Async, Non-Blocking)](#-14--post-hoc-validation-async-non-blocking)
15. [Implementation Sequence](#-15--implementation-sequence)
16. [Research & Patterns Referenced](#-16--research--patterns-referenced)

---

## § 01 · Architectural Principles

Every decision downstream follows from these six rules. They exist to keep the system cheap, deterministic, and resumable across a full K–11 curriculum run.

1. **One canonical lesson, many sessions.** PDF extraction runs once per lesson and produces a frozen `lesson.md`. Every phase session reads from that artifact — never from the PDF directly.
2. **Sessions are independent and stateless.** Each phase session is a single Kimi API call (or a short retry loop around one). No conversation history, no chained turns. Context travels in via prompt, out via structured JSON.
3. **Cache-friendly prefix discipline.** Every prompt is assembled in the same order: *static system → static framework → dynamic lesson → dynamic state → dynamic instruction*. This lets Kimi's native context cache hit on the first two layers across every call.
4. **State is a database, not a message.** No session "passes state" to another session. Sessions read and write rows in Postgres. The pipeline is a DAG over DB rows, not a chain of API calls.
5. **Batch is resumable.** If the machine dies at grade 8, lesson 47, subject "History", phase "Story Mode" — restart picks up at that exact task, not at the top.
6. **Validation is asynchronous.** Generation runs at full speed. A separate process sweeps outputs and flags failures for review. Quality gates never block generation throughput.

---

## § 02 · System Topology

Three concentric layers. The innermost does work; the outer two coordinate.

```
┌──────────────────────────────────────────────────────────────────────┐
│  MACRO LOOP · Batch Runner                                           │
│  iterates: subject → grade (5..11) → lang → lesson_id                │
│                                                                      │
│   ┌────────────────────────────────────────────────────────────┐     │
│   │  MICRO LOOP · Per-Lesson Pipeline                          │     │
│   │                                                            │     │
│   │   ┌─────────────┐   ┌──────────────────────────────┐       │     │
│   │   │             │   │                              │       │     │
│   │   │  [01]       │──▶│  [02] PHASE SESSIONS         │──┐    │     │
│   │   │  EXTRACTOR  │   │      (parallel fan-out)      │  │    │     │
│   │   │             │   │                              │  │    │     │
│   │   └─────────────┘   └──────────────────────────────┘  │    │     │
│   │         │                                             │    │     │
│   │         ▼                                             ▼    │     │
│   │   lesson.md                                     [03] ASSEMBLY  │
│   │   (frozen)                                            │    │     │
│   │                                                       ▼    │     │
│   │                                               homework.md  │     │
│   └────────────────────────────────────────────────────────────┘     │
│                                                                      │
│   ◆ Postgres · state of record for every row                         │
│   ◆ Object storage · PDFs in, homework.md out                        │
│   ◆ Async validator · sweeps completed rows, flags issues            │
└──────────────────────────────────────────────────────────────────────┘
```

The **Macro Loop** is the "one click" — a queue worker that iterates through every combination of subject, grade, language, and lesson. The **Micro Loop** is what happens for a single lesson. Everything else — storage, logging, validation — is ambient infrastructure.

---

## § 03 · The Macro Cycle — Batch Runner

The runner is a worker loop over a task table. It's not an "AI orchestrator". It's a queue consumer with idempotency and retry semantics. This is the "1 click autonomous" surface the operator touches.

### Task shape

Before a run starts, the system enumerates every (subject, grade, language, lesson) tuple that has a source PDF, and writes one row per tuple into `task_queue` with status `pending`. From that moment the run is resumable — pull the queue and execute.

```sql
-- task_queue row
task_id        uuid         pk
subject        text         -- 'history' | 'math' | 'biology' ...
grade          int          -- 5..11
lang           text         -- 'uz' | 'ru'
lesson_id      text         -- stable reference to a PDF chapter
pdf_uri        text
status         text         -- pending | extracting | phasing | assembling | done | failed
attempts       int          -- retry counter, capped
last_error     text
created_at     timestamptz
updated_at     timestamptz
```

### Iteration order

Subject → grade (ascending) → language → lesson. This isn't arbitrary: it optimizes Kimi cache hit rate. Consecutive tasks share the same subject-specific framework prompt, so the static prefix stays cached across many calls.

### Concurrency

The runner pulls up to `N` tasks concurrently from the queue (where `N` is bounded by Kimi rate limits). Each task runs its full Micro Cycle independently. Crashes leave the row in its last `status` — the next run picks it back up from that stage.

> **Operator Interface.** A single command: `nets-run --subject history --grades 5-11 --lang uz`. It enumerates the queue, spawns the worker pool, streams progress, and is interruptible at any point without corrupting state.

---

## § 04 · The Micro Cycle — Per-Lesson Pipeline

Three stages. The first is sequential and must finish before anything else runs. The second is a parallel fan-out. The third is the final join.

```
   PDF in object storage
       │
       ▼
   [ STAGE 01 ]  Extraction Session           1 call    · sequential
       │    output: lesson.md (canonical, frozen)
       ▼
   [ STAGE 02 ]  Phase Sessions               N calls   · parallel
       │    each reads lesson.md + its framework spec
       │    each writes its output row to phase_outputs
       ▼
   [ STAGE 03 ]  Assembly Session             1 call    · sequential
            output: homework.md + queue row marked done
```

The user's framework defines how many phase sessions run in Stage 02 and which of them (if any) depend on each other. This document treats Stage 02 as a parameter: the operator supplies a list of phase definitions and the runner executes them with the concurrency model the framework allows.

### ◆ Framework Integration Point · Phase Graph

The framework author supplies a manifest that declares which phases exist and their dependency edges. The runner consumes this manifest and schedules accordingly. If all phases are independent, all run in parallel. If some depend on others, the runner honors a topological order and parallelizes within each tier.

```yaml
# phase-graph.yaml (operator-supplied)
phases:
  - id: phase_0a
    name: "Preview · 8 Panels"
    depends_on: []
    framework_ref: frameworks/unified/phase_0a.md
  - id: phase_0b
    name: "Flashcards"
    depends_on: []
    framework_ref: frameworks/unified/phase_0b.md
  # ... one block per phase. depends_on is empty = eligible for parallel wave.
```

You own this file. The system doesn't care what's in it as long as the graph is valid (no cycles, every `framework_ref` resolves).

---

## § 05 · Stage 01 — PDF Extraction Session

**Extractor** — 1 call · sequential · blocking

| Inputs | Outputs |
|---|---|
| Source PDF (or pre-OCR'd text) | Canonical `lesson.md` (frozen, hash-addressable) |
| Task metadata: subject, grade, lang, lesson_id | Row in `lessons` table with path + hash |

This session's job is narrow: read the raw textbook chapter and produce a clean, structured Markdown document with headings, body, vocabulary, examples, and any tables or numbered content preserved. **No gamification. No interpretation. No translation.** Just a faithful, structured representation of the source material.

### ◆ Framework Integration Point · Extraction Prompt

The operator supplies the Extractor's full prompt template at `frameworks/system/extraction.md`. The runner composes the final prompt as:

- **SYSTEM** — your extraction persona, output constraints, structural requirements (headings, vocabulary sections, etc.). Static. Cached.
- **CONTEXT** — runner-injected: `{{subject}}, {{grade}}, {{lang}}`. Small, dynamic.
- **INPUT** — the PDF content (pre-OCR'd text, or the raw PDF if using Kimi vision).
- **TASK** — "produce `lesson.md` matching schema X".

The runner doesn't know or care what Uzbek/Russian structural conventions you want. You encode those in the SYSTEM block.

> The extracted `lesson.md` is immutable for the rest of the pipeline. Every phase session sees the exact same bytes. This eliminates a class of subtle bugs where two sessions interpret the PDF differently.

---

## § 06 · Stage 02 — Phase Sessions (Parallel)

**Phase Worker** — N calls · parallel (honoring phase graph) · retryable

| Inputs | Outputs |
|---|---|
| `lesson.md` (from Stage 01) | Structured JSON output for this phase |
| Phase framework spec (`framework_ref`) | Row in `phase_outputs` table |
| Subject-specific framework | |
| Game mechanic docs (if referenced by the phase) | |
| Task metadata: grade, lang, subject | |

Each phase worker is the same code. Only the prompt differs, and the prompt is composed at runtime from files on disk. This means adding a new phase = adding a markdown file and one line to the phase graph, nothing else.

### Prompt composition (per phase call)

```
-- Order matters for cache efficiency. Cached layers first.

[ LAYER 1 · SYSTEM ]
  frameworks/system/phase_worker_base.md
  // invariant instructions: output JSON, follow schema, refuse to ad-lib, etc.

[ LAYER 2 · UNIFIED FRAMEWORK ]
  frameworks/unified/schema.md
  // the Buzan-unified schema reference that applies to all phases

[ LAYER 3 · SUBJECT FRAMEWORK ]
  frameworks/subjects/{{subject}}.md
  // subject-specific adaptation rules (history vs math vs biology)

[ LAYER 4 · PHASE SPEC ]
  {{framework_ref}}
  // THIS phase's rules, steps, examples, output contract

[ LAYER 5 · GAME MECHANICS ]  (only if referenced)
  frameworks/games/{{game_id}}.md

[ LAYER 6 · LESSON INPUT ]
  lesson.md  // the extracted content, verbatim

[ LAYER 7 · DYNAMIC CONTEXT ]
  { grade: 7, lang: "uz", subject: "history", lesson_id: "..." }

[ LAYER 8 · TASK ]
  "Produce the phase deliverable matching schema X. Return JSON only."
```

Layers 1–5 are fully cached on the second call onward (within cache TTL). Layers 6–8 change per call. Every phase of every lesson reuses the same Layers 1–3. The Micro Cycle's per-phase cost drops sharply after the first call in a subject.

### ◆ Framework Integration Point · Where You Plug In

You are the author of everything in `frameworks/`. The runner supplies the machinery. Specifically, you define:

- `frameworks/system/phase_worker_base.md` — worker-wide invariants (output JSON, refuse to invent, language register rules)
- `frameworks/unified/schema.md` — the Buzan-unified framework as a single reference doc
- `frameworks/subjects/{subject}.md` — one file per subject family
- `frameworks/unified/{phase_id}.md` — one file per phase (0-A, 0-B, Memory Sprint, Story Mode, Game Break, Real Life Challenge, AI Sub Boss, Reflection)
- `frameworks/games/{game_id}.md` — one per game mechanic
- `frameworks/schemas/{phase_id}.json` — the JSON schema the phase must return

The runner validates outputs against the schemas and rejects malformed returns before they touch the DB.

---

## § 07 · Stage 03 — Assembly Session

**Assembler** — 1 call · sequential · blocking

| Inputs | Outputs |
|---|---|
| All rows from `phase_outputs` for this lesson | Final `homework.md` written to object storage |
| Assembly template (`frameworks/system/assembly.md`) | Queue row transitioned to `done` |
| Task metadata | |

The Assembler doesn't "generate" content — it composes what already exists. It takes each phase's structured JSON and renders it into the final student-facing Markdown document, respecting order, section headers, and any cross-references the framework defines.

Depending on framework complexity, the Assembler is either (a) a deterministic template renderer with zero LLM calls — cheapest, fastest, most reliable — or (b) a thin LLM call for cases where final polish (transitions, wrap-up narrative) needs to feel cohesive. **Default to (a); escalate to (b) only if deterministic rendering produces visibly seam-ridden output.**

### ◆ Framework Integration Point · Assembly Template

You supply the order of phases in the final document and any static scaffolding (student greeting, section dividers, navigation). The runner fills in the dynamic content from `phase_outputs`.

---

## § 08 · Session Anatomy

Every session in this system — Extractor, any Phase Worker, Assembler — has the same internal shape. The runner code is the same; only the prompt layers differ.

```
   SESSION
   ├─ compose_prompt()
   │    └─ reads framework files from disk → builds layered prompt
   ├─ call_model()
   │    └─ Kimi K2.5 API · structured output mode · JSON schema enforced
   ├─ validate_output()
   │    └─ JSON schema check · reject + retry on fail (bounded)
   ├─ persist()
   │    └─ write row to Postgres with prompt hash + model response + cost
   └─ emit_log()
        └─ structured event: { task_id, phase_id, tokens, cost, latency, cache_hit }
```

No shared runtime state between sessions. No in-process handoff. The DB is the integration surface. This is what makes the pipeline resumable, observable, and debuggable — every session's full input and output is on disk, addressable by `task_id + phase_id`.

---

## § 09 · Framework Integration Points — Summary

Every place the operator (you) plugs in framework content. The runner owns none of this; it reads these files at session start.

| Path | Purpose | Consumed By |
|------|---------|-------------|
| `frameworks/system/extraction.md` | Extraction session prompt | Stage 01 |
| `frameworks/system/phase_worker_base.md` | Phase-worker invariants (always included) | Stage 02 |
| `frameworks/system/assembly.md` | Final document composition template | Stage 03 |
| `frameworks/unified/schema.md` | Unified framework reference | Stage 02 |
| `frameworks/unified/{phase_id}.md` | One file per phase (0-A through Reflection) | Stage 02 |
| `frameworks/subjects/{subject}.md` | Subject-specific adaptation rules | Stage 02 |
| `frameworks/games/{game_id}.md` | Game mechanic documentation | Stage 02 (phases referencing games) |
| `frameworks/schemas/{phase_id}.json` | JSON schema each phase output must match | Stage 02 (validation) |
| `phase-graph.yaml` | Phase list + dependency edges | Stage 02 (scheduler) |

> These paths are a suggestion, not a hard requirement. The runner accepts a config that maps logical roles to file paths — rename or restructure as you prefer.

---

## § 10 · State & Persistence

Postgres. You already run an instance for Paperclip. Add the following tables.

```sql
-- The canonical lesson after extraction. Immutable once written.
CREATE TABLE lessons (
  lesson_id      text PRIMARY KEY,
  subject        text,
  grade          int,
  lang           text,
  pdf_uri        text,
  md_uri         text,            -- path to lesson.md in storage
  md_hash        text,            -- content hash; identity of the frozen doc
  extracted_at   timestamptz
);

-- One row per phase per lesson. Many-to-one with lessons.
CREATE TABLE phase_outputs (
  task_id        uuid,
  lesson_id      text REFERENCES lessons(lesson_id),
  phase_id       text,            -- 'phase_0a', 'memory_sprint', etc.
  output_json    jsonb,           -- the structured phase deliverable
  schema_valid   boolean,
  prompt_hash    text,            -- for cache analysis + reproducibility
  tokens_in      int,
  tokens_out     int,
  cost_usd       numeric(10,6),
  latency_ms     int,
  cache_hit_pct  numeric(5,2),
  created_at     timestamptz,
  PRIMARY KEY (lesson_id, phase_id)
);

-- The batch queue. Status machine drives the runner.
CREATE TABLE task_queue (
  task_id        uuid PRIMARY KEY,
  subject        text, grade int, lang text, lesson_id text,
  pdf_uri        text,
  status         text,
  attempts       int DEFAULT 0,
  last_error     text,
  created_at     timestamptz, updated_at timestamptz
);

-- Append-only audit log. Every session emits one row.
CREATE TABLE session_log (
  id             bigserial PRIMARY KEY,
  task_id        uuid,
  stage          text,            -- 'extract' | 'phase' | 'assemble'
  phase_id       text,            -- null for extract/assemble
  event          text,            -- 'start' | 'success' | 'retry' | 'fail'
  payload        jsonb,
  ts             timestamptz DEFAULT now()
);
```

No coordination tables. No locks. The queue's `status` field is the source of truth for what stage a task is in; concurrent workers claim rows with `SELECT ... FOR UPDATE SKIP LOCKED`.

---

## § 11 · Kimi API Configuration

### Model

Kimi K2.5 via `api.moonshot.ai/v1`. OpenAI-compatible SDK — any OpenAI client library works with the base URL swapped. At writing, pricing is **$0.60/M input, $2.50/M output**, with automatic context caching at **$0.15/M for cached prefixes (75% discount)**. No caching configuration required; the platform handles it as long as prompt prefixes are stable.

### Request shape

```json
{
  "model": "kimi-k2-0711-preview",
  "messages": [
    { "role": "system", "content": "<Layers 1–5, concatenated>" },
    { "role": "user",   "content": "<Layers 6–8, concatenated>" }
  ],
  "response_format": { "type": "json_object" },
  "temperature": 0.3,
  "max_tokens": 8000
}
```

### Cache discipline

- System message is the **cacheable prefix**. Never inject dynamic values into it.
- User message holds everything volatile: lesson content, grade, lang, task instruction.
- Within a run, prompt-prefix hash collisions across tasks should exceed 80% — monitor this (see Observability).
- Iteration order in the Macro Loop (subject → grade → lang → lesson) is chosen specifically to maximize cache stickiness.

### Retry policy

- Transient errors (429, 5xx, timeouts) → exponential backoff, max 5 attempts.
- Schema validation failures → re-prompt once with the specific error, then fail the task.
- All retries logged to `session_log`.

---

## § 12 · Tooling Stack

| Layer | Choice | Why |
|---|---|---|
| Language / runtime | Python 3.11+ | Ecosystem for LLM, PDF, and DB work is unmatched; async-first for the parallel phase wave. |
| Model API | Kimi K2.5 (Moonshot) | Uzbek quality + pricing + automatic caching. |
| HTTP client | `openai` python SDK | Works against Moonshot's OpenAI-compatible endpoint; zero custom HTTP code. |
| Concurrency | `asyncio` + `asyncio.Semaphore` | Native to Python, bounded parallelism without task frameworks. |
| DB | Postgres 15+ (existing) | Row locks (`SKIP LOCKED`) give you a queue for free. |
| Object storage | Local filesystem → S3/R2 later | Storing `lesson.md` and `homework.md`; cheap. |
| Schema validation | `pydantic` v2 | Per-phase output models; rejects malformed JSON before DB writes. |
| PDF → text | `pdfplumber` or `pymupdf` | Fallback to Kimi vision for scanned/complex PDFs. |
| CLI | `typer` or `click` | The "one click" surface. |
| Observability | Structured logs → Postgres + a CLI dashboard | No need for LangSmith etc.; your data is in your DB. |

Total dependencies: fewer than 10. No agent framework, no orchestration engine, no workflow GUI, no Docker mandate. The system is ~600 lines of Python that you can fully read in an afternoon.

---

## § 13 · Observability & Failure Modes

### What to log per session

- `task_id`, `stage`, `phase_id`
- Tokens in / out, latency, USD cost
- **Cache hit percentage** — reported by Moonshot in the usage block; track it, target > 70%.
- Prompt prefix hash (to correlate cache behavior with prompt structure)
- Schema validation result + any validator errors
- Raw response JSON (for post-hoc audit)

### Failure modes to plan for

1. **Malformed JSON** — retry once with error shown to model; fail task on second miss.
2. **Hallucinated content** (phase invents facts not in `lesson.md`) — caught by async validator (§14), not pipeline.
3. **Language register drift** (Uzbek slides toward Russian) — caught by async validator.
4. **Rate limit** — bounded semaphore throttles outgoing calls; 429 triggers exponential backoff.
5. **Runner crash mid-batch** — `task_queue.status` row remains in its pre-crash state; next run reclaims it.
6. **PDF unreadable** (corrupted, scanned at low DPI) — task marked `failed` with reason; sidelined from batch, doesn't block others.

---

## § 14 · Post-Hoc Validation (Async, Non-Blocking)

A separate process. Runs after generation, sweeps completed rows, never blocks the pipeline. Optional but strongly recommended — it's the feedback loop that tells you whether the generator is actually producing good Uzbek and framework-compliant homework.

```
   homework.md · completed
       │
       ▼
   VALIDATOR SWEEP  (cron / queue consumer)
   ├─ language register check   (is this Uzbek? academic-appropriate?)
   ├─ framework compliance      (does each phase match schema + rubric?)
   ├─ factual grounding         (do claims trace back to lesson.md?)
   └─ age appropriateness       (grade-calibrated vocabulary + complexity)
       │
       ▼
   validation_results  →  dashboard · review queue · retraining corpus
```

Implementation: a cheaper model (Haiku 4.5 or Gemini Flash — cross-model evaluation reduces in-family blind spots) runs a rubric check per phase output. Flagged items go to a review queue for you or a teacher to examine. Passing items contribute to a clean corpus you can use later for evaluation benchmarks or fine-tuning.

> The validator is a *linter*, not a gatekeeper. Pipeline throughput is never blocked. You trade instant-quality-enforcement for simplicity, then pay back the debt with a visible review surface.

---

## § 15 · Implementation Sequence

Build order, from highest-leverage to lowest. Don't build what you don't need yet.

1. **Schema + storage** — create the four Postgres tables. Stub out `frameworks/` with empty placeholder files.
2. **Session runner** — single Python function: compose prompt, call Kimi, validate JSON, write row. Used by all three stages.
3. **Extractor** — wire the session runner to the extraction prompt. Test on one PDF.
4. **One phase worker** — implement against one real phase (pick the simplest, e.g., Flashcards). Prove the layered prompt + cache behavior works.
5. **Phase graph + scheduler** — parse `phase-graph.yaml`, topologically sort, run eligible phases in parallel via asyncio.
6. **Assembler** — start with deterministic template rendering. Only add an LLM pass if the output feels seam-ridden.
7. **Batch runner** — task queue enumerator + worker pool. This is the "one click" surface.
8. **Observability** — structured logs, cost rollup, cache-hit percentage dashboard (even a terminal-only view is fine).
9. **Post-hoc validator** — last. Build it against a batch of real outputs; you'll know what rubric to encode only after you've seen the failure modes.

Stages 1–7 should be achievable in roughly 5–8 focused days with Claude Code. Stages 8–9 are incremental and can be added without touching the core pipeline.

---

## § 16 · Research & Patterns Referenced

This architecture is deliberately conservative — it uses established patterns rather than novel ones. For reference:

- **Anthropic · *Building Effective Agents*** ([anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)) — the distinction between workflows (this system) and agents (not this system), and the Prompt Chaining / Routing / Orchestrator-Workers / Evaluator-Optimizer patterns.
- **Cloudflare Agents Reference** ([github.com/cloudflare/agents](https://github.com/cloudflare/agents)) — open-source implementations of all five Anthropic patterns using Durable Objects. Useful as a concrete reference.
- **Moonshot Kimi K2 · Context Caching** — automatic prefix caching at $0.15/M cached tokens (75% discount). Cache discipline in §11 is built around this.
- **DSPy** ([dspy.ai](https://dspy.ai)) — Stanford framework for compiling LM pipelines with optimizable prompts. Consider it as a later optimization if Uzbek quality plateaus and you have an eval metric.
- **Postgres `FOR UPDATE SKIP LOCKED`** — the pattern that makes the task queue safe under concurrent workers without a separate queue service.

What this system deliberately does *not* use: LangChain, LangGraph, CrewAI, n8n, any agent orchestrator, any RAG index. The pipeline is a sequence of typed function calls against a database. That's the feature, not a limitation.

---

> *"The path to success is measuring performance and iterating on implementations. Add complexity only when it demonstrably improves outcomes."*
> — Building Effective Agents · Anthropic

---

**NETS · Autonomous Homework Pipeline**
**Architecture Spec · v0.1 Draft**
**Claude Satter Recruiting / NETS**
