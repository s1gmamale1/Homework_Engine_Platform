# TOOLS — Available Capabilities

This document lists every tool you have access to and how to use each one. Do not attempt to use tools not listed here. If a task requires a tool you don't have, log it in `_log.md` and skip that step.

---

## 1. File System — Read

**Purpose:** Read framework documents, textbook chapters, and existing output files.

**When to use:**
- Pre-flight: reading all framework documents
- Production: reading textbook chapter content
- Resume: checking what output already exists

**Paths you are authorized to read:**
- `standards/` — all framework, library, system, and subject-family docs
- `textbooks/` — source material
- `research/` — background context (only when assignment requires it)
- `agents/content-producer/` — your own config files

**Paths you must NEVER read:**
- `.env`, `.env.*` — secrets
- `.claude/`, `.codex/`, `.qwen/`, `.gemini/` — other agents' private state
- `node_modules/`, `.venv/` — runtime dependencies

---

## 2. File System — Write

**Purpose:** Write homework .md files and production logs.

**When to use:**
- Production: writing .md homework session files
- Throughout: writing/updating STATUS.md progress log

**Paths you are authorized to write:**
- Your assignment's specific `output_path` (e.g., `output/Grade5_Math_uz/`)
- STATUS.md in the output directory (your heartbeat)

**Rules:**
- Never overwrite existing files unless assignment explicitly requests regeneration
- One .md per chapter: `{Subject}_Grade{N}_Ch{N}_{lang}.md`
- STATUS.md updated after every .md file creation

---

## 3. Notion API (When Available)

**Purpose:** Upload validated content items to the NETS Notion workspace.

**When to use:** After Phase 4, if the assignment includes a `notion_upload: true` flag.

**Configuration:**
- Notion MCP or API credentials are provided via environment/tool config
- Target database ID is specified in the assignment

**Upload rules:**
- Only upload items that passed ALL validation checks
- Each JSON item becomes one Notion database entry
- Preserve all field values exactly as they appear in the JSON
- Log upload success/failure per item in `_log.md`

**If Notion is unavailable:** Skip upload, note in `_log.md`, output JSON files are the primary deliverable regardless.

---

## 4. Directory Listing

**Purpose:** Check what files exist in a directory before writing or reading.

**When to use:**
- Pre-flight: verify framework docs exist at expected paths
- Resume: check what output files already exist
- Discovery: list available game specs under `standards/system/games/`

---

## 5. Search / Grep

**Purpose:** Find specific content within framework documents.

**When to use:**
- Looking up a specific family's mechanic emphasis table
- Finding a game's description in the catalog
- Locating grade-band overrides in the Library Framework
- Checking for subject-specific rules

**Prefer targeted reads over broad searches.** If you know the file, read the file. Search is for when you know WHAT you're looking for but not WHERE it is.

---

## Tools You Do NOT Have

- **No web access.** All information comes from the repo.
- **No database access.** Output is JSON files (and optionally Notion via API).
- **No code execution.** You do not run Python scripts or validators. You self-validate using the checklist in SKILLS.md.
- **No communication with other agents.** You work independently. If you encounter a blocker, log it and move on.
