# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

NETS (National Education Transformation System) — AI-powered gamified LMS for Uzbekistan's 8.8M K-11 students. This repo is the **specification and content vault**, not a codebase. It contains framework documents, content architecture, research, and an agent-driven homework production pipeline.

## Architecture — 5 Layers

**Layer 0: UNIFIED-Buzan** (`standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md`) — The engine. Pre-Session (Theme Preview + Flash Cards) → 7-phase homework engine (Memory Sprint → Story Mode → Game Breaks → Real-Life Challenge → Consolidation → Final Boss → Reflection). Single source of truth for all mechanics, timing, HP, PISA gating, Buzan cognitive science, and National Pride module.

**Layer 1: Library Framework** (`standards/library/framework/NETS-Library-Framework.md` v0.6) — Content architecture. 5 subject families, each with mechanic emphasis, boss format, and pedagogical rules.

**Layer 2: Subject Family Docs + Subject Frameworks** (`standards/library/subject-family/`) — Per-family filter/adapter docs that reference Layers 0-1, plus per-subject production guides with grade-band tables.

**Layer 3: Tier Overlay** (`standards/framework/NETS-Tier-Overlay-Spec.md` v2.0) — Basic/Premium split. Basic = full product. Premium = enrichment on top.

**Layer 4: Grading System** (`standards/framework/GRADING-SYSTEM.md`) — Learning Curve Grade (Level, Velocity, Efficiency, Attempts). Not yet approved for production.

## Repository Structure

```
standards/
  framework/               ← UNIFIED-Buzan, Tier Overlay, Grading System, Quick Reference, Blueprint
  library/
    framework/             ← Library Framework v0.6
    catalog/               ← Game Catalog (16 Default + 7 Interactive), Interactive Game Catalog
    subject-family/        ← Family docs + subject-specific frameworks
      Aniq Fanlar/         ← Pure math (5 subjects: Mat, Alg, Geo, Alg&Analiz, Geo Adv)
      Til Fanlar/          ← Languages (English/, Ona_Tili/, Rus_Tili/)
      Tabiy Fanlar/        ← Natural Sciences (Biology/, Physics/, Chemistry/)
      Ijtimoiy Fanlar/     ← Social Sciences (Tarix/)
      Other Fanlar/        ← Soft & Formative (Tarbiya, Music, Art, Informatics, etc.)
    games/_template/       ← Content item JSON schema
    content-templates/     ← Standard content schemas
  system/
    games/
      Game_Mechanics_Demos/ ← 20+ interactive HTML demos
      Game_Mechanics_Docs/  ← 21 numbered game docs + DOCUMENTATION.md master
    narrative/             ← National Pride: quotes_database.json (600), facts, wisdom quotes
    ui-ux/                 ← UI/UX Design Spec
  system-design/v1/        ← System architecture summary
research/                  ← Buzan research, curriculum, engagement hooks, proposals
agents/
  content-producer/        ← Production agent config (SOUL.md, SKILLS.md, SCHEMA.md, etc.)
  CLAUDE.md, GEMINI.md, QWEN.md, SONNET.md  ← Per-agent instructions
references/                ← Agent dashboard protocol, Notion pipeline tools
textbooks/                 ← Grade 5-11 PDFs (uz + ru)
scripts/                   ← Python utilities
memory/                    ← Shared MCP memory palace
```

## Key Documents

| Document | Path | Purpose |
|----------|------|---------|
| UNIFIED-Buzan | `standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md` | Source of truth — read this first |
| Library Framework | `standards/library/framework/NETS-Library-Framework.md` | 5 families, mechanics, Bloom's/PISA (v0.6) |
| Game Catalog | `standards/library/catalog/NETS-Game-Catalog-Summary.md` | 16 Default + 7 Interactive games |
| Tier Overlay | `standards/framework/NETS-Tier-Overlay-Spec.md` | Basic/Premium tier rules (v2.0) |
| Quick Reference | `standards/framework/QUICK_REFERENCE.md` | Fast session flow lookup |
| HOME.md | `HOME.md` | Obsidian hub — links to everything |

## Content Production Pipeline

Homework sessions (.docx) are produced by AI agents. The agent's pipeline:

1. **Pre-Flight (once per subject):** Read Family Doc (FULL) + Subject Framework (FULL) + Textbook TOC
2. **Chapter Extraction:** Read textbook chapter, extract concepts/terms/formulas
3. **Content Mapping:** Map extracted content → session phases using framework knowledge
4. **Deep Read + Write:** Read UNIFIED-Buzan phase specs (§5.1-§5.7) + Game Mechanic Docs + National Pride data → produce .docx
5. **Log:** Update STATUS.md → next chapter

The agent does NOT front-load all framework docs. It reads what it needs, when it needs it. SOUL.md has a summary + reference map; actual specs are read just-in-time before writing each phase.

Agent config: `agents/content-producer/` (SOUL.md, SKILLS.md, SCHEMA.md, AGENTS.md, TOOLS.md, HEARTBEAT.md, MASTER_INSTRUCTION.md)

**Production environments:** OpenClaw (WSL, prototyping) · PaperclipAI (production scale, CEO distributes tasks) · Codex CLI (direct runs)
**Output:** Real .docx via `python-docx` (not plain text). Saved to `Homeworks/` folder.

## Framework Rules That Cannot Be Violated

- **Session structure is immutable:** Pre-Session 0-A → 0-B → Phase 1-7. No skipping, no reordering.
- **Phase 3 game selection:** 3 games per session. ≥1 from Interactive Catalog (7 games), ≥2 from Default Pool (16 mechanics).
- **Boss HP:** G1-4: 50 | G5-8: 100 | G9-11: 150. Damage: Easy -10, Medium -20, Hard -30. Distribution: 40/40/20.
- **No MC for G6+ in Final Boss.** G5 allows up to 30% MC.
- **Textbook is source of truth.** NETS transforms textbook content into better learning — never alters facts, never adds external curriculum.
- **Every content item must carry:** `standard_ref`, `blooms_level`, `pisa_level`, `transition_skill`. Every question in homework .docx must have inline `[Bloom: LX | PISA: LX]` tags.
- **Phase 1 Memory Sprint:** Warm-up from CURRENT chapter (not prior chapters). Prior-chapter review is handled outside homework sessions.
- **Phase 4 scenarios:** Modern professional context only. No bazaar/village/shopkeeper/farmer clichés.
- **5 Subject Families are locked.** Reclassification requires formal ADR.
- **Removed games (do not reference):** Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest.
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

This repo doubles as an Obsidian vault. `HOME.md` is the central hub. Graph color groups: framework=blue, system=cyan, library=green, subject-family=yellow, research=orange, agents=red, references=purple.

## Multi-Agent Context

Multiple agents (Claude, Gemini, Qwen, Codex) work on this project. OpenClaw for agent prototyping, PaperclipAI for production scale. Shared memory via agent-recall MCP (`mcp-shared-memory.json`). Each agent has instruction files in `agents/`.

## What NOT to Do

- Do not modify framework documents unless the user explicitly directs changes.
- Do not hardcode framework rules in agent configs — always reference the source docs.
- Do not push to git without explicit user request.
- Do not modify `openclaw.json` or MCP server configs unless explicitly asked.
- Do not create files in `.claude/`, `.codex/`, `.qwen/`, `.gemini/` — these are gitignored agent runtime dirs.
- Do not add IELTS, DTM, or Premium course content to subject frameworks — textbook only.
- Do not reference removed games (Blackjack, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest).
