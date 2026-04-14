# Sigma_Edu_3000 — NETS Project

**National Education Transformation System** — AI-powered, gamified LMS for Uzbekistan's 8.8M K-11 students.

**Status:** Unified Specification Complete (v2.0) | Ready for Engineering
**Production:** https://class-a-education.netlify.app/ | API: https://edu.jakhongir.dev/

---

## Project Structure

```
Sigma_Edu_3000/
├── README.md                           # This file
├── .env.txt                            # Test credentials (all user roles)
│
├── standards/                          # Authoritative specifications
│   ├── NETS-Homework-Engine-UNIFIED-Buzan.md # THE spec (v2.0, 2072 lines, 20 sections)
│   │                                   #   Single source of truth — supersedes ALL previous
│   ├── EDUCATIONAL_EXPERIENCE_DESIGN.md # Learning philosophy + UX design
│   └── QUICK_REFERENCE.md             # Developer cheat sheet
│
├── research/
│   ├── proposal/                       # Original NETS proposal + summaries
│   │   ├── __NATIONAL EDUCATION__.docx # Source docx (32 pages)
│   │   ├── NETS_PROPOSAL_SUMMARY.md    # Paragraph-by-paragraph index (76 entries)
│   │   ├── RESEARCH_SUMMARY.md         # Executive research summary
│   │   └── Class-A-Education-Platform-Phase-1-Implementation.pptx
│   │
│   ├── analysis/                       # 4-agent quality audit (pre-unification)
│   │   ├── analysis_raphael_textbook.md      # C1: Textbook compliance → PASS
│   │   ├── analysis_donatello_research.md    # C2: Research coverage → 78/100
│   │   ├── analysis_leonardo_pisa.md         # C3: PISA alignment → PARTIAL
│   │   └── analysis_michelangelo_synthesis.md # Cross-criteria synthesis
│   │
│   └── assessments/                    # 6-agent deep assessments
│       ├── assessment_donatello_ai_feasibility.md
│       ├── assessment_leonardo_consistency.md
│       ├── assessment_michelangelo_content.md
│       ├── assessment_raphael_operations.md
│       ├── assessment_splinter_synthesis.md
│       └── assessment_gojo_benchmark.md
│
├── visuals/                            # HTML visualization + screenshots
│   ├── NETS-Homework-Engine-UNIFIED-Visual.html  # Full visual spec (open in browser)
│   └── screenshot-tool/                # Puppeteer screenshot capture tool
│       ├── screenshots/                # 44+ screenshots by role
│       ├── VISUAL_DOCUMENTATION.md
│       └── HOMEWORK_ANALYSIS.md
│
├── textbooks/                          # Downloaded textbooks (266 PDFs, Grades 5-11)
│   ├── download_textbooks.py           # Notion API download script
│   └── grade_5/ through grade_11/      # Uzbek & Russian textbook PDFs
│
└── archive/
    └── Sigma_Edu.zip                   # Full project archive
```

---

## The Spec: NETS-Homework-Engine-UNIFIED-Buzan.md

**This is the single authoritative document.** Engineering and content teams build exclusively from it. It supersedes all previous versions.

### 20 Sections:

| # | Section | What It Covers |
|---|---------|---------------|
| 1 | Core Principles | 3 Sacred Principles, Learning Pyramid, No Busywork Rule |
| 2 | Content Reference Architecture | Hierarchy, Learning Units, Block Types, Dual Standard Codes, Tagging Schema |
| 3 | PISA Proficiency Framework | Official OECD level definitions (Math/Reading/Science), PISA tracking per student |
| 4 | Homework Session Engine | Session modes (20-30 min / 40-50 min / 15-20 min), initialization algorithm |
| 5 | Phase Specifications | All 7 phases with full specs, JSON schemas, scoring, adaptation rules |
| 6 | 14 Game Mechanics | Complete specs for all 14 games with subject examples |
| 7 | PISA Skill Progression | Grade 1-11 matrices for Math, Reading, Science |
| 8 | Creative Thinking Domain | PISA Creative Thinking coverage (Uzbekistan: 14/60), Creative Lab mechanic |
| 9 | Difficulty Adaptation Engine | Real-time IRT-based adjustment, flow state algorithm |
| 10 | Content Pipeline | Textbook → AI Refinement → Review → Deploy pipeline |
| 11 | Gamification Economy | XP, streaks, stars, badges, leaderboards, avatar customization |
| 12 | Edge Cases & Recovery | Recovery Queue, Catch-Up Mode, Boost Mode, Low Engagement |
| 13 | Anti-Cheat System | Question regeneration, response patterns, Socratic verification |
| 14 | Teacher Controls | Dashboard, heat maps, overrides, Kundalik integration |
| 15 | Integration Points | Parent portal, Kundalik/eMaktab, analytics push |
| 16 | JSON Schema | Full homework task JSON schema with all required fields |
| 17 | Grade-Level Matrix | Game availability by grade band |
| 18 | AI Refinement Constraints | Permissible/prohibited AI operations, CS exception |
| 19 | Bilingual Framework | CEFR/IELTS progression, Krashen's i+1, content-based instruction |
| 20 | Research Citations | 19 peer-reviewed citations + PISA data sources |

Plus: Appendix A (session completion/data flow), Appendix B (source reconciliation log).

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| PISA level decoupled from HP damage | Damage is relative to student; PISA tracked for analytics |
| Final Boss spans Level 3-6 (tiered) | Resolves docx contradiction; covers full PISA range |
| Grades 5-8 Boss HP = 80 (not 100) | Fixes broken HP math (max damage 90 vs 100 HP) |
| `transition_skill` field mandatory | Every task must declare which L→L+1 transition it scaffolds |
| Dual standard code format | Descriptive primary (`UZ-MATH-5-FRAC-01`), dotted alias (`MAT.5.3.4.1`) |
| 20-30 min default, 50 min extended | Homework vs in-class modes |

---

## The Problem

Uzbekistan PISA 2022: Math 364 (-108 vs OECD), Reading 336 (-140), Science 355 (-130), Creative Thinking 14/60. Over 80% below Level 2. Goal: top-30 PISA by 2030.

## Quick Start

| Audience | Start Here |
|----------|-----------|
| **Engineer** | `standards/NETS-Homework-Engine-UNIFIED-Buzan.md` (the only spec you need) |
| **Designer** | `visuals/NETS-Homework-Engine-UNIFIED-Visual.html` (open in browser) |
| **New team member** | `research/proposal/RESEARCH_SUMMARY.md` → this README |
| **Content creator** | Unified spec Section 10 (pipeline) + Section 2 (tagging schema) |
| **Stakeholder** | `research/analysis/analysis_michelangelo_synthesis.md` |

## Test Credentials

See `.env.txt`. Roles: Super Admin, School Admin (x2), Teacher (x5), Student (x24).

---

**Last Updated:** April 2, 2026
