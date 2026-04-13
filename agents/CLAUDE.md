# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

NETS (National Education Transformation System) — AI-powered gamified LMS for Uzbekistan's 8.8M K-11 students. This repo contains the specification documents and a demo Next.js app that visualizes a homework session.

## Repository Structure

- `standards/` — Authoritative specs. `NETS-Homework-Engine-UNIFIED.md` (2,072 lines, 20 sections) is the single source of truth for all engineering.
- `app/` — Next.js 16 demo app (the homework session visualizer)
- `demo/` — Homework design documents + 3 student profile JSONs (Malika/Bobur/Jasur)
- `research/` — Original proposal, analysis reports, assessments
- `stress tests/` — Agent stress test results for AI-R&R document
- `textbooks/` — Grade 5-11 textbook PDFs (Uzbek + Russian)
- `scripts/` — Python utilities (docx conversion)

## App Development

### Commands

```bash
cd app
npm run dev          # Start dev server (http://localhost:3000)
npm run build        # Production build
npm run lint         # ESLint
```

### Tech Stack

Next.js 16.2.2 (App Router) + React 19 + TypeScript 5 (strict) + Tailwind CSS 4. Path alias `@/*` → `./src/*`.

**IMPORTANT:** Next.js 16 has breaking changes from training data. Read `app/AGENTS.md` and check `node_modules/next/dist/docs/` before writing code.

### Architecture

**Landing page** (`app/src/app/page.tsx`) → Select student profile → **Session page** (`app/src/app/session/page.tsx`) → 8 phases in strict order → Session complete.

**Session state** is managed via React Context + useReducer in `lib/session-context.tsx`. The reducer handles: SET_STUDENT, ADD_XP, CORRECT_ANSWER, WRONG_ANSWER, COMPLETE_PHASE, NEXT_PHASE, BOSS_DAMAGE, BOSS_HINT_PENALTY, SET_STARS, ADD_WEAK_AREA, SESSION_COMPLETE, RESET.

**8 phases** execute in order defined by `PHASE_ORDER` in `lib/types.ts`:
1. speed_match → 2. flashcard_sprint → 3. story_mode → 4. apply (tile_match + sentence_fill + mystery_box) → 5. analyze → 6. memory_palace → 7. boss_fight → 8. remediation

Each phase is a component in `components/phases/`. All use `"use client"` and access state via `useSession()`.

**Answer evaluation** uses hardcoded correct answers with fuzzy matching (`lib/fuzzy-match.ts`). The fuzzy matcher handles typos (Levenshtein), word reordering, Uzbek apostrophe variants, partial answers, and multi-point answers. AI (Ollama) is used as a secondary evaluator for boss fights, not the primary check.

### Ollama Integration

The app calls a local Ollama instance for AI features (boss evaluation, Socratic tutoring, anti-cheat analysis).

```
Endpoint: http://192.168.1.15:11434/api/chat  (native Ollama, NOT /v1/chat/completions)
Model:    huihui_ai/qwen3.5-abliterated:9b-Claude
Timeout:  60 seconds (model needs ~15-20s for inference)
```

`lib/ollama.ts` handles the connection. The model wraps JSON in markdown code blocks — the helper strips those. All API routes (`app/api/*`) extract JSON via regex fallback when the model returns malformed responses.

**Fallback:** If Ollama is unreachable, all API routes fall back to static responses or local evaluation so the app still works.

### API Routes

All in `app/src/app/api/`:
- `evaluate-boss/` — Scores open-ended boss answers via Ollama + rubric
- `evaluate-checkpoint/` — Scores story mode checkpoints
- `socratic-tutor/` — Generates guiding questions (never reveals answers)
- `anti-cheat/` — Compares answers against student's behavioral baseline
- `generate-report/` — Teacher/parent session reports

### Student Data

Three profiles loaded from `demo/` JSONs. The `lib/students.ts` loader accepts full names ("Malika Karimova"), first names ("Malika"), or keys ("malika"). Each profile contains: PISA levels, mastery map, transition skills, behavioral baseline (for anti-cheat), session history, engagement data (streak, XP, badges).

### Anti-Cheat System

Rule-based flags (SPEED_ANOMALY, LENGTH_ANOMALY, PASTE_DETECTED) + AI-based flags (VOCAB_JUMP, STRUCTURE_ANOMALY). Verdict ladder: 0 flags = CLEAN, 1 = MONITOR, 2 = SOFT_WARNING, 3+ = TEACHER_ALERT. New students (Jasur) get calibration mode with halved flag sensitivity.

### Content Data

`app/data/phases.json` contains all homework content (questions, answers, rubrics) extracted from the design docs. `lib/placeholder-data.ts` has hardcoded fallback content. Content is structured by phase matching the `PhaseData` type in `lib/types.ts`.

## Key Constraints

- All UI text is in **Uzbek**. Use existing text patterns in components as reference.
- **Textbook is source of truth** — NETS wraps textbook content in engagement, never alters facts.
- Every task must have: `standard_ref`, `blooms_level`, `pisa_level`, `transition_skill`.
- Boss HP: 50 (Grades 1-4), 100 (Grades 5-8), 150 (Grades 9-11).
- Boss format: No multiple choice for Grade 5+ (open reasoning only).
- The 7-phase sequence is immutable. Phases always run in order.
