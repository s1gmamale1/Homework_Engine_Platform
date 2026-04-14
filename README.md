# Sigma_Edu_3000 — NETS Homework Engine Platform

**National Education Transformation System** — AI-powered, gamified LMS for Uzbekistan's 8.8M K-11 students.

**Status:** Framework Complete (UNIFIED-Buzan v2.0) | Content Production Pipeline Active
**Branch:** `Cheeks` (development) · `master` (stable)

---

## Project Structure

```
Sigma_Edu_3000/
├── HOME.md                              # Obsidian vault hub — links to everything
├── CLAUDE.md                            # Claude Code project guidance
├── OBSIDIAN_SETUP.md                    # Team onboarding for Obsidian
│
├── standards/
│   ├── framework/                       # THE LAW — authoritative specs
│   │   ├── NETS-Homework-Engine-UNIFIED-Buzan.md   # Source of truth (v2.0, 3,651 lines)
│   │   ├── NETS-Tier-Overlay-Spec.md               # Basic/Premium tier rules (v2.0)
│   │   ├── GRADING-SYSTEM.md                        # Learning Curve Grade spec (v1.0)
│   │   ├── QUICK_REFERENCE.md                       # Fast session flow lookup
│   │   └── NETS-Homework-Engine-Universal-Blueprint-Flow-Diagram.md
│   │
│   ├── library/                         # Content architecture
│   │   ├── framework/
│   │   │   └── NETS-Library-Framework.md            # 5 families, mechanics, Bloom's/PISA (v0.5)
│   │   ├── catalog/
│   │   │   ├── NETS-Game-Catalog-Summary.md         # 16 Default + 8 Interactive games
│   │   │   └── NETS-Interactive-Game-Catalog.md     # Interactive pool detail (v1.1)
│   │   ├── subject-family/              # Subject family frameworks
│   │   │   ├── Aniq Fanlar/             # Exact Sciences (Math, Physics, Chemistry...)
│   │   │   ├── Til Fanlar/              # Languages (Uzbek, Russian, English...)
│   │   │   ├── Tabiy Fanlar/            # Natural Sciences (Biology, Geography...)
│   │   │   ├── Ijtimoiy Fanlar/         # Social Sciences (History, Law, Economy...)
│   │   │   └── Other Fanlar/            # Soft & Formative (Art, Music, PE...)
│   │   ├── games/_template/             # Content item JSON schema
│   │   └── content-templates/           # Standard content schemas
│   │
│   ├── system/                          # Subsystem specs
│   │   ├── games/
│   │   │   ├── Game_Mechanics_Demos/    # 20+ interactive HTML demos
│   │   │   └── Game_Mechanics_Docs/     # 21 numbered game docs (01-21)
│   │   │       ├── DOCUMENTATION.md     # Master game documentation (1,320 lines)
│   │   │       └── DOCUMENTATION-INDEX.md
│   │   ├── narrative/                   # National Pride module
│   │   │   ├── quotes_database.json     # 600 quotes (national + global)
│   │   │   ├── task_injections.json     # 20% task injection rules
│   │   │   ├── Bilarmidingiz_faktlar.md # 300 "Did You Know" facts
│   │   │   ├── Milliy_hikmatlar.md      # National wisdom quotes
│   │   │   ├── Jahon_hikmatlari.md      # World wisdom quotes
│   │   │   └── STRATEGY_AND_LOGIC.md    # 55/45, 70/30, 20% rules
│   │   └── ui-ux/
│   │       └── NETS-UI-UX-Design-Spec.md # Visual design + National Pride UI
│   │
│   └── system-design/v1/               # System architecture summary
│
├── agents/                              # AI agent configurations
│   ├── CLAUDE.md                        # Claude Code instructions
│   ├── GEMINI.md                        # Gemini instructions
│   ├── QWEN.md                          # Qwen instructions
│   ├── SONNET.md                        # Sonnet instructions
│   └── content-producer/                # Homework production agent
│       ├── SOUL.md                      # Framework summaries + constraints
│       ├── SKILLS.md                    # 7-phase docx production template
│       ├── SCHEMA.md                    # Output format spec
│       ├── MASTER_INSTRUCTION.md        # v6.0 AI system prompt
│       ├── AGENTS.md                    # Startup sequence + logging
│       ├── TOOLS.md                     # Environment + available tools
│       └── HEARTBEAT.md                 # Monitoring checklist
│
├── research/                            # Background research
│   ├── INDEX.md                         # Hub — all research by topic
│   ├── Buzan_*.md (×6)                  # Memory/learning theory
│   ├── DTM_*.md, Olympiad_*.md, etc.    # Uzbekistan curriculum context
│   ├── hooks/                           # Neuroscience & attention research
│   └── proposal/                        # Original NETS proposal
│
├── references/                          # Integration references
│   ├── agent-dashboard-protocol.md
│   └── notion-video-lesson-tools.md
│
├── textbooks/                           # Grade 5-11 PDFs (uz + ru)
│   └── grade_5/ through grade_11/
│
├── scripts/                             # Python utilities
│   ├── check_blueprint_compliance.py    # 135 automated spec checks
│   ├── generate_demo_lessons.py
│   ├── md_to_docx.py
│   └── build_homework_and_students.py
│
├── visuals/                             # HTML reports and visualizations
├── memory/                              # Shared MCP memory palace
└── .obsidian/                           # Obsidian vault config (team-shared)
```

---

## Architecture

**Layer 0: UNIFIED-Buzan** — The engine. Pre-Session (Theme Preview + Flash Cards) → 7-phase homework engine → Session complete. Single source of truth for all mechanics.

**Layer 1: Library Framework** — The content architecture. 5 subject families, each with mechanic emphasis, boss format, and pedagogical rules.

**Layer 2: Subject Family Frameworks** — Per-family rules that guide subject-specific content production.

**Layer 3: Tier Overlay** — Basic/Premium split. Basic = full product. Premium = enrichment on top.

**Layer 4: Grading System** — Learning Curve Grade (Level, Velocity, Efficiency, Attempts) replaces XP as the progress measure.

---

## Key Specs

| Document | Purpose |
|----------|---------|
| `NETS-Homework-Engine-UNIFIED-Buzan.md` | Source of truth — read this first |
| `NETS-Library-Framework.md` | 5 families, 29 subjects, mechanic mapping |
| `NETS-Tier-Overlay-Spec.md` | Basic vs Premium rules |
| `GRADING-SYSTEM.md` | Learning Curve Grade spec |
| `NETS-Game-Catalog-Summary.md` | All game mechanics (16 Default + 8 Interactive) |
| `DOCUMENTATION.md` | Detailed specs for 21 game mechanics |

---

## Content Production

Homework sessions are produced by AI agents (Codex via OpenClaw, or Claude). Pipeline:

1. Agent reads framework docs (UNIFIED-Buzan + Library Framework for the subject's family)
2. Agent reads textbook chapter (PDFs in `textbooks/`)
3. Agent produces a `.docx` homework session: Pre-Session 0-A/0-B + 7 phases
4. Agent updates `STATUS.md` as heartbeat
5. Output goes to `standards/library/subject-family/{family}/`

Agent config: `agents/content-producer/` (SOUL.md, SKILLS.md, SCHEMA.md)

---

## Multi-Agent Setup

| Agent | Role | Platform |
|-------|------|----------|
| Claude (Opus) | Architecture, planning, framework design | Claude Code CLI |
| Qwen | Framework editing, spec compliance | Qwen CLI |
| Gemini | Reviews, audits, MCP memory setup | Gemini CLI |
| Codex | Content production (homework generation) | OpenClaw / PaperclipAI |

Shared memory: `mcp-shared-memory.json` (agent-recall MCP). Agent dashboard: `references/agent-dashboard-protocol.md`.

---

## The Problem

Uzbekistan PISA 2022: Math 364 (-108 vs OECD), Reading 336 (-140), Science 355 (-130), Creative Thinking 14/60. Over 80% below Level 2. Goal: top-30 PISA by 2030.

---

## Quick Start

| Audience | Start Here |
|----------|-----------|
| **Engineer** | `standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md` |
| **Content creator** | `agents/content-producer/SOUL.md` + `SKILLS.md` |
| **New team member** | `HOME.md` → this README → `OBSIDIAN_SETUP.md` |
| **Reviewer** | `standards/library/framework/NETS-Library-Framework.md` |

---

## Git

```bash
# Windows ownership workaround:
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" status
git -c safe.directory="C:/Users/DaddysHere/Documents/Sigma_Edu_3000" push origin Cheeks
```

Remote: `https://github.com/s1gmamale1/Homework_Engine_Platform.git`
Branches: `Cheeks` (dev) · `master` (stable)

---

**Last Updated:** April 14, 2026
