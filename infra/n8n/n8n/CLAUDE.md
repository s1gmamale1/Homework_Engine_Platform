# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Scope

This directory (`infra/n8n/n8n/`) is the **self-hosted n8n deployment** that runs the NETS homework production pipeline. Broader repository context — the NETS framework, subject specs, content vault, and agent instructions — lives at the parent `Sigma_Edu_3000/` root. See `../../../CLAUDE.md` for that. This file covers only the n8n infrastructure.

## What this pipeline does

Converts textbook PDF chapters into fully assembled NETS homework sessions. One task per chapter flows through 9 sequential stages:

1. **Extraction** (Kimi `kimi-k2.5`) — PDF → structured chapter JSON
2. **Phase 0-A** Theme Preview  →  3. **Phase 0-B** Flash Cards  →  4. **Phase 1** Memory Sprint  →  5. **Phase 2** Story Mode  →  6. **Phase 3** Game Breaks  →  7. **Phase 4** Real-Life Challenge  →  8. **Phase 5** Consolidation  →  9. **Phase 6** Final Boss

Phase workers use Kimi `kimi-k2-turbo-preview`. Final output is an assembled Markdown homework file, destined for the sibling GitHub repo `https://github.com/s1gmamale1/Homeworks.git` via GitHub API push (replacing the older local-write approach into `nets-output/`).

The phase DAG is declarative — see `phase-graph.yaml`. Each phase references a framework spec (`frameworks/unified/phase_*.md`) and a JSON schema (`frameworks/schemas/phase_*.json`) baked into the image.

## Architecture

- **n8n** (`n8nio/n8n:latest`) — workflow orchestration, host port 5678
- **PostgreSQL 16-alpine** — state store (task queue, phase outputs, session log, validation results)
- **Custom Docker image** — extends n8n base and bakes textbook PDFs + framework Markdown into `/home/node/nets/` at build time. Every Code/Execute node gets direct file access with no volume plumbing.

Services are defined in `docker-compose.yml`. The custom `Dockerfile` copies `books/` and `frameworks/` into `/home/node/nets/` with `node:node` ownership.

### Postgres schema (`setup.sql`)

Five tables drive the pipeline. All `CREATE TABLE IF NOT EXISTS` (idempotent):

| Table | Role |
|-------|------|
| `nets_task_queue` | batch queue — one row per lesson, status machine drives the runner |
| `nets_lessons` | extracted lesson metadata, immutable once written |
| `nets_phase_outputs` | one row per `(lesson_id, phase_id)` — JSON output, tokens, cost, latency |
| `nets_session_log` | append-only audit log |
| `nets_validation_results` | async validator output (written by WF-06) |

Seeds one initial task on first apply: Grade 5 Math, Theme 1, Uzbek (`uz-mat-g5-theme1`).

### Workflows (`workflows/*.json`)

Seven n8n workflow exports, imported manually via the n8n UI (Settings → Import from File):

| File | Role |
|------|------|
| `wf-main.json` | orchestrator entry point |
| `wf-01-batch-runner.json` | picks next `pending` task from `nets_task_queue` |
| `wf-02-micro-loop.json` | per-task phase loop driver (walks the phase DAG) |
| `wf-03-extractor.json` | PDF → chapter JSON via Kimi `k2.5` |
| `wf-04-phase-sessions.json` | phase-by-phase content generation via Kimi `k2-turbo-preview` |
| `wf-05-assembler.json` | stitches phase outputs into a single Markdown homework; pushes to `s1gmamale1/Homeworks` |
| `wf-06-validator.json` | async quality + schema validator, writes `nets_validation_results` |

A higher-level `NETS Main Pipeline v2.json` also lives one directory up in `../` — that is the export of the integrated top-level workflow, kept at parent level for visibility.

## Common commands

```bash
# Start the stack
docker compose up -d

# Stop (preserves volumes)
docker compose down

# View n8n logs
docker compose logs -f n8n

# Apply / re-apply schema (idempotent)
docker exec -i n8n-postgres-1 psql -U n8n -d n8n < setup.sql

# Full reset (DESTRUCTIVE — drops volumes, re-applies schema)
docker compose down -v && docker compose up -d && docker exec -i n8n-postgres-1 psql -U n8n -d n8n < setup.sql

# Rebuild image after adding/updating books/ or frameworks/
docker compose build --no-cache n8n && docker compose up -d

# Tail the task queue
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c "SELECT task_id, subject, grade, lesson_id, status, attempts FROM nets_task_queue ORDER BY created_at DESC LIMIT 10;"

# Inspect last phase output for a lesson
docker exec -it n8n-postgres-1 psql -U n8n -d n8n -c "SELECT phase_id, schema_valid, tokens_in, tokens_out, cost_usd, latency_ms FROM nets_phase_outputs WHERE lesson_id='<lesson_id>' ORDER BY phase_id;"
```

Note: `docker exec ... psql -f /tmp/file.sql` fails from Git Bash on Windows due to MSYS path translation. Always pipe via stdin (`< file.sql`) or use `-c "..."` instead of `-f`.

## LAN access

n8n is exposed on `192.168.1.41:5678` for teammates on the local network. Env vars in `docker-compose.yml`:

- `N8N_HOST=192.168.1.41`
- `N8N_PROTOCOL=http`
- `N8N_SECURE_COOKIE=false` (required for plain-HTTP LAN logins — cookies are otherwise rejected on non-HTTPS origins)
- `WEBHOOK_URL=http://192.168.1.41:5678/`
- `N8N_EDITOR_BASE_URL=http://192.168.1.41:5678/`

If the host IP changes (DHCP), update all three URL env vars and restart the n8n container. Docker Desktop auto-manages the Windows firewall rule — no manual entry needed.

## Credentials

- Postgres credentials live in `.env` (gitignored). Default values used for local LAN: user=`n8n`, db=`n8n`.
- `N8N_ENCRYPTION_KEY` in `.env` must **never change after first boot** — it encrypts stored credentials inside n8n and re-keying makes every stored credential unrecoverable.
- Kimi (Moonshot) API keys are stored inside n8n's own credential store via the n8n UI, not in `.env`.
- A GitHub Personal Access Token with `repo` scope is needed for the assembler to push to `s1gmamale1/Homeworks`. Create as an HTTP Request Auth credential in n8n (Credentials → New → Header Auth, value `Bearer <PAT>`).

## Notable constraints

- **Books and frameworks are baked into the image**, not volume-mounted. Adding or updating a textbook PDF or framework doc requires `docker compose build --no-cache n8n`. Trade-off: ~355 MB image bloat, but every node gets instant file access.
- **`N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true`** is on — the n8n settings file must be `0600` inside the container. If you `docker cp` a new settings file in, `chmod 600` it immediately after.
- **`NODE_FUNCTION_ALLOW_EXTERNAL=*`** is permissive — Code nodes can `require` any npm package. Fine for local/trusted dev, but do not expose this instance to the public internet without tightening.
- **`N8N_CONCURRENCY_PRODUCTION_LIMIT=20`** caps parallel workflow executions. Raise cautiously — phase generation is LLM-bound and too much parallelism burns Kimi quota fast.
- **`NODE_FUNCTION_ALLOW_BUILTIN=fs,path,crypto,https`** — only these Node built-ins are whitelisted for Code nodes. Anything else needs to go through the external-module path.

## Utilities

`extract_pdfs.py` — standalone one-off script using `pymupdf` (fitz) to convert every `.pdf` under a local books directory to a sibling `.txt`. Not part of the pipeline; used for offline text-inspection of textbooks before feeding them to the extractor. Default books dir is hardcoded to `D:\Class A Education\Books` — edit before running.

## Documentation

Full pipeline spec with node-by-node reference, prompt templates, and per-phase token budgets lives at `../NETS-Pipeline-v2-Documentation.md` (parent `infra/` directory). Read that before editing any workflow JSON.

## Things to avoid

- Don't change `N8N_ENCRYPTION_KEY` after first boot — breaks every stored credential.
- Don't volume-mount over `/home/node/nets/books/` or `/home/node/nets/frameworks/` — the Dockerfile copies them in deliberately, mounting would hide the baked content.
- Don't edit workflow JSONs by hand — export from the n8n UI after making changes to preserve node IDs and credential references.
- Don't `git push` assembled homework from inside the n8n container — the flow is GitHub API (PUT `/repos/{owner}/{repo}/contents/{path}`) from the assembler workflow, not local git.
- Don't treat `nets-output/` as authoritative — it's a legacy local-write directory; the production destination is the `s1gmamale1/Homeworks` repo via API.
