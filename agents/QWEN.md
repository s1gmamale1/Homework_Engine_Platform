# QWEN.md — Sigma_Edu_3000 Project Context

## Project Overview

**NETS (National Education Transformation System)** — An AI-powered, gamified Learning Management System (LMS) for Uzbekistan's 8.8M K-11 students. The project aims to raise PISA scores from the 2022 baseline (Math 364, Reading 336, Science 355 — 80%+ students below Level 2) toward top-30 globally by 2030.

**Core Philosophy:** Textbook is the source of truth; NETS wraps textbook content in active, gamified, AI-personalized learning without altering facts. Every homework session follows a 7-phase engine designed to maintain flow state (70-80% success rate) and scaffold PISA level transitions.

**Production:** Web app at https://class-a-education.netlify.app/ | API at https://edu.jakhongir.dev/

---

## Repository Structure

```
Sigma_Edu_3000/
├── standards/                          # Authoritative specifications
│   ├── NETS-Homework-Engine-UNIFIED.md # THE spec (v2.0, 20 sections) — single source of truth
│   ├── NETS-Homework-Engine-Blueprint.docx  # HOW the engine runs (session lifecycle)
│   ├── EDUCATIONAL_EXPERIENCE_DESIGN.md     # Learning philosophy + UX design
│   ├── QUICK_REFERENCE.md              # Developer cheat sheet
│   └── AI-Roles-and-Responsibilities.md
│
├── app/                                # Next.js 16 demo app (homework session visualizer)
│   ├── src/app/                        # Next.js App Router pages
│   ├── src/components/                 # Phase components (phases/*.tsx)
│   ├── src/lib/                        # Core logic (session, students, Ollama, fuzzy-match)
│   └── data/                           # Homework content (phases.json)
│
├── demo/                               # Demo homework lessons (DOCX)
│   ├── NETS_Demo_Kimyo_7_Kislorod.docx
│   ├── NETS_Demo_Algebra_7_Chiziqli_Funksiya.docx
│   ├── NETS_Demo_Biologiya_7_Nafas_Olish.docx
│   ├── student_A_malika.json / student_B_bobur.json / student_C_jasur.json
│   └── Good Demos/ | Acceptable but not Good enough Demos/ | Bad Demos/
│
├── textbooks/                          # Grade 5-11 textbooks (266 PDFs, Uzbek + Russian)
│   ├── grade_5/ through grade_11/
│   └── download_textbooks.py           # Notion API download script
│
├── scripts/                            # Python utilities
│   ├── generate_demo_lessons.py        # Main demo lesson generator (Blueprint-compliant)
│   ├── check_blueprint_compliance.py   # Automated spec compliance checker (135 checks)
│   └── [PDF extraction, TOC parsing, docx conversion tools]
│
├── research/                           # Proposals, analysis, assessments
│   ├── proposal/                       # Original NETS proposal + summaries
│   ├── analysis/                       # 4-agent quality audit
│   └── assessments/                    # 6-agent deep assessments
│
├── visuals/                            # HTML visual specs + screenshots
│   ├── NETS-Homework-Engine-UNIFIED-Visual.html
│   └── screenshot-tool/                # 44+ screenshots by role
│
├── stress tests/                       # Agent stress test results for AI-R&R document
├── archive/                            # Full project archive
│
├── CLAUDE.md                           # Claude Code guidance
├── README.md                           # Project overview
└── .env.txt                            # Test credentials (Super Admin, School Admin, Teacher, Student x24)
```

---

## The Two Source-of-Truth Documents

### 1. `standards/NETS-Homework-Engine-UNIFIED.md` — THE WHAT
- 2,100+ lines, 20 sections
- Content Reference Architecture, PISA Framework, 7-Phase Specs, 14 Game Mechanics
- Difficulty Adaptation Engine, Content Pipeline, Gamification Economy, Anti-Cheat, Teacher Controls
- JSON Schema, Grade-Level Matrix, AI Refinement Constraints, Bilingual Framework, Research Citations

### 2. `standards/NETS-Homework-Engine-Blueprint.docx` — THE HOW
- Universal Session Engine — step-by-step session lifecycle
- Sections 0-8: Pre-Session → 7 Phases → Post-Session
- Hook Model (Nir Eyal), Octalysis (Yu-kai Chou), Duolingo mechanics
- AI Tiers: Tier 1 (algorithmic), Tier 2 (generative), Tier 3 (Socratic tutoring)

**Both documents together = the complete engine. Neither is sufficient alone.**

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

## The Demo App (Next.js 16)

### Tech Stack
- **Next.js 16.2.2** (App Router) + **React 19** + **TypeScript 5** (strict)
- **Tailwind CSS 4** | Path alias: `@/*` → `./src/*`
- **Ollama** integration: `http://192.168.1.15:11434/api/chat` (model: `huihui_ai/qwen3.5-abliterated:9b-Claude`)

### Architecture
- **Landing page** → Select student profile (Malika/Bobur/Jasur) → **Session page** → 8 phases in strict order
- **State management:** React Context + useReducer in `lib/session-context.tsx`
- **Answer evaluation:** Hardcoded correct answers with fuzzy matching (`lib/fuzzy-match.ts`) — handles typos (Levenshtein), word reordering, Uzbek apostrophe variants
- **AI fallback:** If Ollama is unreachable, all API routes fall back to static responses

### Commands
```bash
cd app
npm run dev          # Dev server (http://localhost:3000)
npm run build        # Production build
npm run lint         # ESLint
```

### Key Files
| File | Purpose |
|------|---------|
| `src/lib/session-context.tsx` | Session state reducer (SET_STUDENT, ADD_XP, CORRECT_ANSWER, BOSS_DAMAGE, etc.) |
| `src/lib/types.ts` | TypeScript types (PhaseData, PhaseType, StudentProfile) |
| `src/lib/fuzzy-match.ts` | Answer evaluator with fuzzy matching |
| `src/lib/ollama.ts` | Ollama API client with JSON parsing |
| `src/lib/students.ts` | Student profile loader (names, keys, or JSON) |
| `src/lib/content.ts` | Homework content loader |
| `src/app/api/evaluate-boss/` | Boss answer scoring via Ollama + rubric |
| `src/app/api/socratic-tutor/` | Guiding question generator |
| `src/app/api/anti-cheat/` | Behavioral baseline comparison |
| `data/phases.json` | All homework content (questions, answers, rubrics) |

---

## Generating Demo Lessons

The Python script `scripts/generate_demo_lessons.py` generates Blueprint-compliant DOCX lessons:

```bash
cd C:\Users\DaddysHere\Documents\Sigma_Edu_3000
python scripts/generate_demo_lessons.py       # Generate 3 demo lessons
python scripts/check_blueprint_compliance.py  # Run 135-check compliance test
```

**Compliance checklist (135 checks):** Phase presence, content tagging (standard_ref, blooms_level, pisa_level, transition_skill), game mechanics, CPA staging, flow state adaptation, mandatory tag schema, immutable constraints.

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

## Test Credentials

See `.env.txt` for full list:
- **Super Admin:** `admin` / `admin123`
- **School Admin:** `school_admin1` / `school123`, `school_admin2` / `school123`
- **Teacher:** `teacher1`–`teacher5` / `teacher123`
- **Student:** `student1`–`student24` / `student123`

---

## Student Demo Profiles

Three profiles in `demo/` JSON files:
- **Malika Karimova** — On-track, PISA Math 1.7, Reading 1.4, Science 1.5, streak 12
- **Bobur Aliyev** — At-risk, needs intervention in certain domains
- **Jasur Rakhimov** — New student, calibration mode (halved anti-cheat sensitivity)

Each contains: PISA levels, mastery map with Ebbinghaus decay, transition skills, behavioral baseline (for anti-cheat), session history.

---

## Development Notes

- **Next.js 16 has breaking changes** — always read `app/AGENTS.md` and check `node_modules/next/dist/docs/` before writing code
- **Ollama model:** Native endpoint (NOT `/v1/chat/completions`), 60s timeout, model wraps JSON in markdown code blocks
- **All content in Uzbek** — use existing component text patterns as reference for Uzbek terminology
- **Python 3** required for scripts; `python-docx` and `PyMuPDF` (fitz) are dependencies for docx/PDF operations

## Qwen Added Memories
- NETS Library Framework completed (v0.1) — standards/system-design/v1/NETS-Library-Framework.md (1,300+ lines) + interactive HTML visual. Contains: (1) 5 Subject Family Classifications with 29 subjects mapped, (2) Universal 4-Level System (L1 textbook → L2 Lyceum Delta → L3 exam prep → L4 Olympiad expert), (3) 5 Path System (STD, DTM, OLY, CERT, PISA) with DTM specialty mapping for 7 university directions, (4) 16 Cross-Subject Courses with full specs including 1M Coders/IT Park syllabi integration, (5) Library Catalog Hierarchy tree with content addressing schema and ~125K item projection, (6) Placement Suggestions with triggers and surfaces. All 9 research gaps resolved via Gemini's 3 research waves. Next research needs: DTM question samples, PISA item samples, G8-11 audit, teacher dashboard UX research.
- NETS Library Framework updated to v0.3 with Part 7: Buzan Cognitive Science Integration. New content: TEFCAS model (Trial-Event-Feedback-Check-Adjust-Success) as core difficulty adaptation engine logic; "Hali emas" failure framing for G5; MIG memory effects (Primacy/Recency/Association/Von Restorff/Sag) mapped to all 7 phases; Memory systems (Link System, Peg System Number-Shape/Rhyme, Major System phonetic code, Memory Palace with Registan Square as default Loci, SMASHIN' SCOPE 12-quality mnemonic gate, SEM3 Master Memory Matrix); BOST Organic Study Technique mapped to Phase 0-A/0-B; Mind Mapping 7 Laws with G5-G6 WM-respecting adaptations (one word per branch, icon-first, landscape orientation, minimum 3 colors, 4-5 chunk ceiling); Speed reading integration (eye tracking fixations/saccades/regressions, chunking 3-5 words, sub-vocalization ~150 WPM limit, UI/UX rules: 50-75 char column width, 1.5x line height, Arimo font); Radiant Navigation UI architecture replacing linear sidebar; Anti-cheat Radiance Score detecting linear vs radiant response patterns; BOST review intervals (10m/24h/1w/1mo) aligned with spaced repetition; Meta-learning badges (Cortical Synergist, Mind Map Master, Radiant Thinker); TEFCAS achievements (Try-All, Pivot Master, Radiant Streak, Merz's Retention). Quantifiable metrics: 16+ empirical values from Merz Study (10-15% retention gain), Farrand et al. (10% recall improvement), Buzan speed reading metrics. Research wave 4 (Buzan) completed — 6 files integrated.
