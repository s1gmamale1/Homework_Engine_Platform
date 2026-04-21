# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

NETS (National Education Transformation System) — AI-powered gamified LMS for Uzbekistan's 8.8M K-11 students. This repo is the **specification and content vault**, not a codebase. It contains framework documents, content architecture, research, and an agent-driven homework production pipeline.

## Architecture — 5 Layers

**Layer 0: UNIFIED-Buzan** (`standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md`) — The engine. Pre-Session (Theme Preview + Flash Cards) → 7-phase homework engine (Memory Sprint → Story Mode → Game Breaks → Real-Life Challenge → Consolidation → Final Boss → Reflection). Single source of truth for all mechanics, timing, HP, PISA gating, Buzan cognitive science, and National Pride module. **Defines WHAT each phase must contain.**

**Layer 1: Library Framework** (`standards/library/framework/NETS-Library-Framework.md`) — Content architecture. 5 subject families, each with mechanic emphasis, boss format, and pedagogical rules.

**⚠ Architecture updated (2026-04-21):** UNIFIED-Buzan is now FROZEN. The framework has been decomposed into a component architecture at `standards/framework/`. See `NETS-Framework-Architecture.md` for the full map.

**Layer 0: Core Primitives** (`standards/framework/00-core/`, 19 files) — Shared rules: pronouns, PISA/Bloom, skill taxonomy, capture rule, routing algorithm, HP baselines, context policy, decision enforcement, national narrative, visual generation, etc.

**Layer 1: Phase Components** (`standards/framework/01-phases/`, 9 files) — Each homework phase as a standalone spec: Preview, Flash Cards, Sprint, Reading, Game Breaks, Real-Life, Consolidation, Final Challenge, Reflection.

**Layer 2: Family Adapters** (`standards/framework/02-families/`, 5 files) — Pipeline blueprints per subject family (Aniq Fanlar, Tabiy Fanlar, Til Fanlar, Ijtimoiy Fanlar) + subject-english.md override. Defines Easy/Hard pipelines, game picks, teaching methodology per family.

**Layer 2b: Construction Recipes** (`standards/library/subject-family/`) — Per-subject production guides with grade-band tables and construction recipes. Delta layers on top of family adapters.

**Layer 3: Modes** (`standards/framework/03-modes/`, 2 files) — Easy (5 components, ~35 min) and Hard (6-8 components, ~70-90 min). Binary mode selection per lesson. English is always Hard.

**Layer 4: Difficulty** (`standards/framework/04-difficulty/`, 3 files) — Phase weights, item tier distribution, per-family difficulty calibration.

**Layer 5: Builder** (`standards/framework/05-builder/`, 3 files) — 6-step pipeline (classify → load → extract → compose → verify → ship) + verification checklist + output schema.

**Tier Overlay** (`standards/framework/NETS-Tier-Overlay-Spec.md` v2.0) — Basic/Premium split. Basic = full product. Premium = enrichment on top.

**Grading System** (`standards/framework/GRADING-SYSTEM.md`) — Learning Curve Grade (Level, Velocity, Efficiency, Attempts). Not yet approved for production.

## Repository Structure

```
standards/
  framework/               ← UNIFIED-Buzan, Tier Overlay, Grading System, Quick Reference, Blueprint
  library/
    framework/             ← Library Framework
    catalog/               ← Game Catalog (16 Default + 6 Interactive), Interactive Game Catalog
    subject-family/        ← Family docs + subject-specific frameworks
      Aniq Fanlar/         ← Pure math (5 subjects: Mat, Alg, Geo, Alg&Analiz, Geo Adv)
      Til Fanlar/          ← Languages (English/, Ona_Tili/, Rus_Tili/)
      Tabiy Fanlar/        ← Natural Sciences (Biology/, Physics/, Chemistry/)
      Ijtimoiy Fanlar/     ← Social Sciences (Tarix/, Jahon_Tarixi/, Ozbekiston_Tarixi/)
    games/_template/       ← Content item JSON schema
  system/
    games/
      Game_Mechanics_Demos/ ← 19 interactive HTML demos
      Game_Mechanics_Docs/  ← 19 numbered game docs + DOCUMENTATION.md master
    narrative/             ← National Pride: quotes_database.json, facts, wisdom quotes, task_injections
    ui-ux/                 ← UI/UX Design Spec
  system-design/v1/        ← System architecture summary
research/                  ← Buzan research, curriculum, engagement hooks, proposals
agents/
  content-producer/        ← Production agent config (SOUL.md, SKILLS.md, SCHEMA.md, TOOLS.md, AGENTS.md, HEARTBEAT.md, MASTER_INSTRUCTION.md)
  CLAUDE.md, GEMINI.md, QWEN.md, SONNET.md  ← Per-agent instructions (agents/CLAUDE.md is STALE — ignore it)
references/                ← Agent dashboard protocol, Notion pipeline tools
textbooks/                 ← Grade 5-11 PDFs (uz + ru)
scripts/                   ← Python/shell utilities (19 files)
memory/                    ← Shared MCP memory palace
Homeworks/                 ← Output: .md homework sessions + STATUS.md
Good Demos/                ← Reference homework outputs (Grade7, GPT/Qwen)
output/                    ← HTML visualizations
HOME.md                    ← Obsidian vault hub
```

## Key Documents

| Document | Path | Purpose |
|----------|------|---------|
| UNIFIED-Buzan | `standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md` | Source of truth — WHAT rules |
| Library Framework | `standards/library/framework/NETS-Library-Framework.md` | 5 families, mechanics, Bloom's/PISA |
| Game Catalog | `standards/library/catalog/NETS-Game-Catalog-Summary.md` | 16 Default + 6 Interactive games |
| Interactive Game Catalog | `standards/library/catalog/NETS-Interactive-Game-Catalog.md` | Detailed interactive game specs |
| Tier Overlay | `standards/framework/NETS-Tier-Overlay-Spec.md` | Basic/Premium tier rules (v2.0) |
| Quick Reference | `standards/framework/QUICK_REFERENCE.md` | Fast session flow lookup |
| HOME.md | `HOME.md` | Obsidian hub — links to everything |

## Content Production Pipeline

Homework sessions are produced by AI agents using the component architecture. The pipeline reads component files (not the frozen UNIFIED monolith) to compose homework.

**Pipeline (6 steps — see `05-builder/homework-builder.md`):**
1. **CLASSIFY:** Subject → family tag (from textbook path). Content → Easy/Hard mode. Grade → difficulty band.
2. **LOAD:** Core primitives (00-core/) + active phase components (01-phases/ per mode) + family adapter (02-families/) + difficulty calibration (04-difficulty/).
3. **EXTRACT:** Textbook PDF → structured chapter JSON (concepts, terms, formulas). Identify 5-7 atomic skills.
4. **COMPOSE:** Per active phase, generate content following phase component spec + family teaching methodology + decision enforcement gates.
5. **VERIFY:** 11-gate checklist (`05-builder/verification-checklist.md`). All gates must pass.
6. **SHIP:** Write homework .md + metadata JSON → push to `s1gmamale1/Homeworks` repo.

**n8n pipeline (production):** `infra/n8n/` — self-hosted n8n + Postgres. See `infra/n8n/n8n/CLAUDE.md`.
**Agent config:** `agents/content-producer/` (7 files: SOUL, SKILLS, SCHEMA, TOOLS, AGENTS, HEARTBEAT, MASTER_INSTRUCTION). Note: these reference the old monolith and need updating to point at component files.
**Output:** Markdown (.md) files → `s1gmamale1/Homeworks` repo via GitHub API.

## Framework Rules That Cannot Be Violated

- **Two modes:** Easy (5 components, ~35 min) or Hard (6-8 components, ~70-90 min). English is always Hard. Pipeline decides mode, not the LLM.
- **v1 active games only:** Tile Match, Memory Match, Sentence Fill, Adaptive Quiz, Notebook Capture. All others frozen for v2.
- **Decision enforcement:** No "optional" content. Every conditional element has MUST IF / MUST SKIP IF gates. LLM must log reasoning for every include/skip decision. See `00-core/decision-enforcement.md`.
- **Boss HP:** G1-4: 50 | G5-8: 100 | G9-11: 150. Damage: Easy -10, Medium -20, Hard -30. Distribution: 40/40/20. (Matematika G5-6 override: 80 HP)
- **No MC for G6+ in Final Boss.** G5 allows up to 30% MC.
- **Textbook is source of truth.** NETS transforms textbook content into better learning — never alters facts, never adds external curriculum.
- **Every question must carry inline tags:** `[Bloom: LX | PISA: LX]`. Boss questions also carry `[Damage: -XX HP]`.
- **Phase 1 Memory Sprint:** 3 formats ONLY — Multiple Choice, True/False, Yes/No/Not Given. Must mix ≥2 formats. BANNED: fill-in-blank, gap-fill, drag-and-drop, typing, open-ended. Tap-only. Current chapter only.
- **Phase 2 Story Mode:** ONE continuous flowing story. Arc beats (Problem→Struggle→Discovery→Solution) are invisible INGREDIENTS baked into the narrative — NOT segments, NOT labels, NOT output sections. Checkpoints come after the story.
- **Pronoun policy:** All Uzbek content uses "Siz" (formal). Never "sen". Russian: "Вы", never "ты".
- **Phase 4 scenarios:** Modern professional context only. No bazaar/village/shopkeeper/farmer clichés.
- **5 Subject Families are locked.** Reclassification requires formal ADR.
- **Removed games (NEVER reference):** Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker.
- **Subject frameworks are delta layers.** They only specify what's DIFFERENT from UNIFIED. Don't restate HP values, damage tables, or stars criteria — inherit them.
- **No IELTS/DTM/Premium content in subject frameworks.** Those are separate courses, not textbook homework.
- **Universal production rules (all families):** Bidirectional thinking, Error Analysis/Detection primary (every 2 sessions), Answer Completeness.

## Scripts

```bash
python scripts/check_blueprint_compliance.py   # 135 automated spec checks
python scripts/generate_demo_lessons.py        # Generate demo homework
python scripts/md_to_docx.py                   # Convert markdown to docx
python scripts/build_homework_and_students.py  # Build homework + student profiles
```

No package.json or requirements.txt at root. Scripts are standalone Python — install dependencies as needed (`pip install python-docx pymupdf markdown`).

## Git

```bash
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" status
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" push origin Cheeks
```

Remote: `https://github.com/s1gmamale1/Homework_Engine_Platform.git`
Branches: `Cheeks` (development) · `master` (stable)

## Obsidian

This repo doubles as an Obsidian vault. `HOME.md` is the central hub. `OBSIDIAN_SETUP.md` has team onboarding. Graph color groups: framework=blue, system=cyan, library=green, subject-family=yellow, research=orange, agents=red, references=purple.

## Multi-Agent Context

Multiple agents (Claude, Gemini, Qwen, Codex) work on this project. OpenClaw for agent prototyping, PaperclipAI for production scale. Shared memory via agent-recall MCP (`mcp-shared-memory.json`). Each agent has instruction files in `agents/`. **Note:** `agents/CLAUDE.md` is stale (references a non-existent Next.js app) — ignore it; this root CLAUDE.md is authoritative.

## Compact Instructions

During context compaction, preserve:
- Framework architecture (UNIFIED = WHAT, Subject Framework = HOW, Agent = BUILD)
- All 17 framework file paths and their current state
- Phase structure details (Pre-Session 0-A/0-B + Phase 1-7 rules and construction recipes)
- Game catalog constraints (16 Default + 6 Interactive, removed games list)
- Production agent output status tables and quality assessments
- Any tables comparing before/after or listing what was fixed
- File modification history and sync status (PaperclipAI, OpenClaw)
- Team branch assignments (Cheeks, MYPRO, Sam/Toriq, Oliver)
- Specific line numbers and exact quotes from framework docs when referenced
- Delta layer pattern: what each subject framework overrides vs inherits
Do not summarize away technical constraints, construction recipes, or rejection criteria.

## What NOT to Do

- Do not modify framework documents unless the user explicitly directs changes.
- Do not hardcode framework rules in agent configs — always reference the source docs.
- Do not push to git without explicit user request.
- Do not modify `openclaw.json` or MCP server configs unless explicitly asked.
- Do not create files in `.claude/`, `.codex/`, `.qwen/`, `.gemini/` — these are gitignored agent runtime dirs.
- Do not add IELTS, DTM, or Premium course content to subject frameworks — textbook only.
- Do not reference removed games (Blackjack, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker).
