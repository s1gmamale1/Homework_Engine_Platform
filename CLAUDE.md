# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

NETS (National Education Transformation System) — AI-powered gamified LMS for Uzbekistan's 8.8M K-11 students. This repo is the **specification and content vault**, not a codebase. It contains framework documents, content architecture, research, and an agent-driven homework production pipeline.

## Architecture — Two Layers

**Layer 0: UNIFIED Spec** (`standards/framework/NETS-Homework-Engine-UNIFIED.md`) — The engine. Defines the session structure: Pre-Session (Theme Preview + Flash Cards) → 7-phase homework engine (Memory Sprint → Story Mode → Game Breaks → Real-Life Challenge → Consolidation → Final Boss → Reflection). This is the single source of truth for all mechanics, timing, XP, HP, PISA gating, and session modes.

**Layer 1: Library Framework** (`standards/library/framework/NETS-Library-Framework.md`) — The content architecture. Groups 29 subjects into 5 families (Aniq Fanlar, Til Fanlari, Tabiat Fanlari, Ijtimoiy Fanlari, Tarbiya/Sanat). Each family has its own mechanic emphasis, boss format, and pedagogical rules. This determines WHAT content goes inside the engine for each subject.

## Repository Structure

```
standards/
  framework/          ← UNIFIED spec, Quick Reference, Tier Overlay, Blueprint
  system/             ← Per-subsystem specs (games/, ui-ux/)
  system-design/      ← System Design v1 summary
  library/            ← Content architecture (framework, catalog, games template)
  subject-family/     ← grades/{5-11}/{uz,ru}/{family}/ — content output destination
research/             ← Buzan research, curriculum analysis, engagement hooks, proposals
agents/               ← Agent instruction files (CLAUDE.md, GEMINI.md, QWEN.md)
  content-producer/   ← Production agent config (SOUL.md, SKILLS.md, SCHEMA.md)
references/           ← Agent dashboard protocol, Notion pipeline tools
textbooks/            ← Grade 5-11 PDFs organized by grade/language/subject
scripts/              ← Python utilities (docx conversion, compliance checks, demos)
memory/               ← Shared MCP memory palace for cross-agent context
```

## Key Documents

| Document | Path | Purpose |
|----------|------|---------|
| UNIFIED Spec | `standards/framework/NETS-Homework-Engine-UNIFIED.md` | Source of truth — read this first |
| Library Framework | `standards/library/framework/NETS-Library-Framework.md` | Family rules, mechanics, Bloom's/PISA mapping |
| Game Catalog | `standards/library/catalog/NETS-Game-Catalog-Summary.md` | All 28 game mechanics described |
| Quick Reference | `standards/framework/QUICK_REFERENCE.md` | Fast lookup for session flow |
| HOME.md | `HOME.md` | Obsidian hub — links to everything |
| Research Index | `research/INDEX.md` | All research grouped by topic |

## Content Production Pipeline

Homework is produced by AI agents (Codex/MiniMax via OpenClaw, or Claude). The pipeline:

1. Agent reads framework docs (UNIFIED + Library Framework for the subject's family)
2. Agent reads textbook chapter
3. Agent produces a `.docx` homework session: Pre-Session 0-A/0-B + 7 phases
4. Agent updates `STATUS.md` in the output directory as a heartbeat
5. Output goes to `standards/subject-family/grades/{N}/{lang}/{family}/`

Agent config lives in `agents/content-producer/` — SOUL.md (framework summaries + constraints), SKILLS.md (production template), SCHEMA.md (output format).

## Framework Rules That Cannot Be Violated

- **Session structure is immutable:** Pre-Session 0-A → 0-B → Phase 1-7. No skipping, no reordering.
- **Phase 3 game selection:** 3 games per session. At least 1 from Interactive Catalog, at least 2 from Default Pool.
- **Boss HP:** G1-4: 50 | G5-8: 100 | G9-11: 150. Damage: Easy -10, Medium -20, Hard -30. Distribution: 40/40/20.
- **No MC for G6+ in Final Boss.** G5 allows up to 30% MC.
- **Textbook is source of truth.** NETS wraps textbook content in engagement — never alters facts.
- **Every content item must carry:** `standard_ref`, `blooms_level`, `pisa_level`, `transition_skill`.
- **5 Subject Families are locked.** A subject cannot move between families without a formal ADR.
- **Bloom's/PISA progression through session:** Phase 1 (L1) → Phase 6 (L3-L5).
- **All student-facing content in Uzbek (uz) or Russian (ru).** Field names stay English.

## Scripts

```bash
python scripts/check_blueprint_compliance.py   # 135 automated spec checks
python scripts/generate_demo_lessons.py        # Generate demo homework
python scripts/md_to_docx.py                   # Convert markdown to docx
python scripts/build_homework_and_students.py  # Build homework + student profiles
```

No package.json or requirements.txt at root. Scripts are standalone Python — install dependencies as needed (`pip install python-docx pymupdf`).

## Git

```bash
# Windows git has ownership mismatch — use this flag:
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" status
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" push origin master
```

Remote: `https://github.com/s1gmamale1/Homework_Engine_Platform.git` (branch: master)

## Obsidian

This repo doubles as an Obsidian vault. `HOME.md` is the central hub. Graph color groups: framework=blue, system=cyan, library=green, subject-family=yellow, research=orange, agents=red, references=purple. Team config committed in `.obsidian/` (plugins, graph, app settings).

## Multi-Agent Context

Multiple agents (Claude, Gemini, Qwen, Codex) work on this project. Shared memory is being set up via agent-recall MCP (`mcp-shared-memory.json`). Agent dashboard protocol at `references/agent-dashboard-protocol.md`. Each agent has instruction files in `agents/`.

## What NOT to Do

- Do not modify framework documents unless the user explicitly directs changes.
- Do not hardcode framework rules in agent configs — always reference the source docs.
- Do not push to git without explicit user request.
- Do not modify `openclaw.json` or MCP server configs unless explicitly asked.
- Do not create files in `.claude/`, `.codex/`, `.qwen/`, `.gemini/` — these are gitignored agent runtime dirs.
