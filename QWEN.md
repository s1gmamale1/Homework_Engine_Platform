# QWEN.md — Sigma_Edu_3000 Project Context

## Project Overview

**NETS (National Education Transformation System)** — An AI-powered, gamified Learning Management System (LMS) for Uzbekistan's 8.8M K-11 students. The project aims to raise PISA scores from the 2022 baseline (Math 364, Reading 336, Science 355 — 80%+ students below Level 2) toward top-30 globally by 2030.

**Core Philosophy:** Textbook is the source of truth; NETS wraps textbook content in active, gamified, AI-personalized learning without altering facts. Every homework session follows a 7-phase engine designed to maintain flow state (70-80% success rate) and scaffold PISA level transitions.

**Production:** Web app at https://class-a-education.netlify.app/ | API at https://edu.jakhongir.dev/

**Project Type:** Content Engineering & Specification Hub (not the main implementation repo)

---

## Repository Structure

```
Sigma_Edu_3000/
├── standards/                          # Authoritative specifications
│   ├── framework/                      # Core specs (UNIFIED, Blueprint, Quick Reference)
│   │   ├── NETS-Homework-Engine-UNIFIED.md        # THE spec (v2.0, 2600+ lines, 20 sections)
│   │   ├── NETS-Homework-Engine-Universal-Blueprint-Flow-Diagram.md
│   │   └── QUICK_REFERENCE.md                      # Developer cheat sheet
│   ├── library/                        # Library Framework & Catalog specs
│   ├── subject-family/                 # 5 Subject Family Frameworks
│   ├── system/                         # Subsystem specs (session, games, boss, etc.)
│   └── system-design/                  # System architecture & design docs
│       └── v1/NETS-System-Design-v1-Summary.md     # 5-layer architecture
│
├── research/                           # Proposals, analysis, assessments
│   ├── proposal/                       # Original NETS proposal + summaries
│   ├── analysis/                       # 4-agent quality audit
│   ├── assessments/                    # 6-agent deep assessments
│   └── INDEX.md                        # Research index
│
├── scripts/                            # Python automation utilities
│   ├── generate_demo_lessons.py        # Main demo lesson generator (Blueprint-compliant)
│   ├── check_blueprint_compliance.py   # Automated spec compliance checker (135 checks)
│   ├── build_homework_and_students.py  # Homework builder
│   ├── squad-tui.sh                    # Multi-agent squad launcher (tmux)
│   └── [PDF extraction, TOC parsing, docx conversion tools]
│
├── textbooks/                          # Grade 5-11 textbooks (266 PDFs, Uzbek + Russian)
│   ├── download_textbooks.py           # Notion API download script
│   └── grade_5/ through grade_11/      # Uzbek & Russian textbook PDFs
│
├── visuals/                            # HTML visual specs + screenshots
│   ├── NETS-Homework-Engine-UNIFIED-Visual.html
│   └── screenshot-tool/                # 44+ screenshots by role
│
├── agents/                             # Agent-specific context files
│   ├── CLAUDE.md, GEMINI.md, QWEN.md, SONNET.md
│   └── content-producer/               # Content producer agent config
│
├── memory/                             # Hive Mind Store (SQLite + Obsidian)
├── references/                         # Agent dashboard protocol, Notion tools
├── TMN/                                # (To be determined)
├── Good Demos/                         # Demo lesson examples
└── screenshots/                        # Additional screenshots
```

---

## The Source-of-Truth Document

### `standards/framework/NETS-Homework-Engine-UNIFIED.md` — THE WHAT (2600+ lines, 20 sections)

This is the **single authoritative specification**. Engineering and content teams build exclusively from it. It supersedes all previous versions.

| Section | Topic |
|---------|-------|
| 1 | Core Principles (3 Sacred Principles, Learning Pyramid, No Busywork Rule) |
| 2 | Content Reference Architecture (Hierarchy, Block Types, Dual Standard Codes, Tagging) |
| 3 | PISA Proficiency Framework (OECD level definitions, tracking per student) |
| 4 | Homework Session Engine (20-30 min / 40-50 min / 15-20 min modes) |
| 5 | Phase Specifications (All 7 phases with JSON schemas, scoring, adaptation) |
| 6 | 14 Game Mechanics (Complete specs with subject examples) |
| 7 | PISA Skill Progression (Grade 1-11 matrices for Math, Reading, Science) |
| 8 | Creative Thinking Domain (PISA Creative Thinking, Creative Lab mechanic) |
| 9 | Difficulty Adaptation Engine (IRT-based adjustment, flow state algorithm) |
| 10 | Content Pipeline (Textbook → AI Refinement → Review → Deploy) |
| 11 | Gamification Economy (XP, streaks, stars, badges, leaderboards) |
| 12 | Edge Cases & Recovery (Recovery Queue, Catch-Up Mode, Boost Mode) |
| 13 | Anti-Cheat System (Question regeneration, response patterns, Socratic verification) |
| 14 | Teacher Controls (Dashboard, heat maps, overrides, Kundalik integration) |
| 15 | Integration Points (Parent portal, Kundalik/eMaktab, analytics) |
| 16 | JSON Schema (Full homework task JSON schema) |
| 17 | Grade-Level Matrix (Game availability by grade band) |
| 18 | AI Refinement Constraints (Permissible/prohibited operations) |
| 19 | Bilingual Framework (CEFR/IELTS progression, Krashen's i+1) |
| 20 | Research Citations (19 peer-reviewed citations + PISA data sources) |

### Supporting Documents

- **`HOME.md`** — High-level navigation hub with subsystem status tracker
- **`standards/framework/QUICK_REFERENCE.md`** — Developer cheat sheet (7-phase journey, 14 games, Boss rules)
- **`standards/system-design/v1/NETS-System-Design-v1-Summary.md`** — 5-layer architecture (Framework → Subject Families → Subjects → Tier Overlay → Metagame)

---

## The 7-Phase Homework Session

Every homework session follows this immutable sequence (~25 minutes standard):

| Phase | Name | Duration | Purpose |
|-------|------|----------|---------|
| 1 | Memory Sprint | 2 min | Recall from prior chapters (spaced repetition) |
| 2 | Story Mode | 5-7 min | Deliver new content as narrative with checkpoint gates |
| 3 | Game Breaks | 6-9 min | Interleaved practice (Tile Match, Sentence Fill, Mystery Box, Why Chain) |
| 4 | Real-Life Challenge | 3-5 min | Uzbek-context transfer scenarios (PISA 3+) |
| 5 | Consolidation | 2-3 min | Memory Palace + mnemonic lock before boss |
| 6 | Final Boss | 5-10 min | PISA-calibrated assessment gate (open reasoning, no MC for Grade 5+) |
| 7 | Reflection + Remediation | 3-5 min | AI analysis, targeted micro-exercises, metacognition |

---

## Key Constraints

| Rule | Detail |
|------|--------|
| **3 Sacred Principles** | 1. Textbook = truth, NETS = transformer. 2. Flow state mandatory (70-80% success). 3. Intrinsic > extrinsic rewards |
| **No Busywork** | Every task must scaffold one specific PISA transition skill |
| **Zero Pay-to-Win** | No real-money purchases. Rewards celebrate learning, not compliance |
| **7-Phase Immutable** | Phases always run in order — cannot skip or reorder |
| **No MC for Grade 5+** | Boss fights use open reasoning only |
| **Boss HP** | 50 (Grades 1-4), 80 (Grades 5-8), 150 (Grades 9-11) |
| **Language** | All UI text in **Uzbek** |
| **Mandatory Tags** | Every item: `standard_ref`, `blooms_level`, `pisa_level`, `transition_skill`, `textbook_ref` |

---

## PISA Proficiency Framework

Students tracked on continuous PISA scale per subject (e.g., Math 1.7). Target: move 80%+ from below Level 2 to Level 2-3 within 2 years.

| PISA Level | NETS Bloom's Mapping |
|------------|---------------------|
| Below 1 | Remember |
| Level 1 | Remember-Understand |
| Level 2 | Understand-Apply |
| Level 3 | Apply-Analyze |
| Level 4 | Analyze-Evaluate |
| Level 5-6 | Evaluate-Create |

**Flow state rule:** AI adjusts difficulty every 3-5 questions — <60% success → reduce difficulty, >90% → increase, 70-80% → maintain.

---

## 5-Layer System Architecture

```
Layer 0: UNIVERSAL FRAMEWORK v2.0       (the constitution — unchanged)
              ↓  inherits
Layer 1: SUBJECT FAMILY FRAMEWORKS      (5 families — Tabiat, Aniq, Til, Ijtimoiy, Tarbiya/Sanat)
              ↓  inherits
Layer 2: SUBJECT FRAMEWORKS             (per subject × grade × language — ~110 total)
              ↓  inherits
Layer 3: TIER OVERLAY                   (Basic + Premium — cuts across all subjects)
              ↓  inherits
Layer 4: METAGAME + APP SURFACES        (Bilim Bazasi — persistent, cross-subject)
```

**5 Subject Families:**
1. **Tabiat Fanlari** (Natural Sciences) — Biology, Geography, G5 Combined Science
2. **Aniq Fanlar** (Exact Sciences) — Math, Physics, Chemistry, Informatics
3. **Til Fanlari** (Languages) — Uzbek, Russian, English, Native Language, Literature
4. **Ijtimoiy Fanlari** (Social Sciences) — History, Law, Economy, Civics
5. **Tarbiya/Sanat** (Soft/Formative) — Art, Music, PE, Tarbiya

---

## 14 Game Mechanics

| # | Name | Best For | Research Basis |
|---|------|----------|----------------|
| 1 | Tile Match | Vocabulary, formulas | Dual Coding |
| 2 | Spaced Flashcards | Memorization | Ebbinghaus |
| 3 | Memory Sprint | Recall priming | Retrieval Practice |
| 4 | Mystery Box | Problem ID | Interleaving |
| 5 | Adaptive Quiz | Assessment | Item Response Theory |
| 6 | Why Chain | Science reasoning | Elaborative Interrogation |
| 7 | Sentence Fill | Comprehension | Cloze Testing |
| 8 | Real-Life Challenge | Transfer | Phenomenon-Based |
| 9 | Story Mode | Engagement | Narrative Retention |
| 10 | Reflection Journal | Metacognition | Flavell (1979) |
| 11 | Peer Teaching | Consolidation | Protégé Effect |
| 12 | Movement Breaks | Kinaesthetic (G1-4) | Embodied Cognition |
| 13 | Final Boss | Mastery | Productive Struggle |
| 14 | Memory Palace | Long-term retention | Method of Loci |

---

## Scripts & Automation

### Key Commands

```bash
# Generate Blueprint-compliant demo lessons
python scripts/generate_demo_lessons.py

# Run 135-check compliance test
python scripts/check_blueprint_compliance.py

# Build homework + student data
python scripts/build_homework_and_students.py

# Launch multi-agent squad (tmux-based)
bash scripts/squad-tui.sh
```

### Python Dependencies
- `python-docx` — DOCX generation
- `PyMuPDF` (fitz) — PDF extraction
- `pandoc` — Document conversion (MD ↔ DOCX)

---

## Test Credentials

See `.env.txt` for full list:
- **Super Admin:** `admin` / `admin123`
- **School Admin:** `school_admin1` / `school123`, `school_admin2` / `school123`
- **Teacher:** `teacher1`–`teacher5` / `teacher123`
- **Student:** `student1`–`student24` / `student123`

---

## MCP (Model Context Protocol) Setup

The project uses MCP for cross-agent memory synchronization:

- **`mcp-shared-memory.json`** — Configures `agent-recall-mcp` server with Obsidian vault integration
- **`mcp-config.json`** — Configures `obsidian-memory-mcp` server
- **`memory/`** — Local SQLite and Obsidian-based memory files (Hive Mind Store)

Agents sync by calling `session_start()` and `recall(query="...")` to retrieve shared context.

---

## Development Notes

- **All content in Uzbek** — use existing patterns as reference for Uzbek terminology
- **Python 3** required for scripts
- **Obsidian** is used as the team knowledge vault (see `OBSIDIAN_SETUP.md`)
- **Multi-agent workflow** — Claude, Gemini, Sonnet, Qwen, and Codex collaborate via MCP
- **Textbook PDFs** are the source material — 266 PDFs across Grades 5-11 in Uzbek and Russian
- **Cultural grounding** — All narratives and challenges must use Uzbekistan context (Samarkand, Registan, Plov, Milliylik)

---

## Related Memories

- NETS Library Framework completed (v0.3) — 5 Subject Family Classifications, Universal 4-Level System, 5 Path System, 16 Cross-Subject Courses, Library Catalog Hierarchy (~125K items), Buzan Cognitive Science Integration (TEFCAS, MIG memory effects, Memory Palace, Mind Mapping, Speed Reading)
- Research wave 4 (Buzan) completed — 6 files integrated with 16+ empirical metrics
