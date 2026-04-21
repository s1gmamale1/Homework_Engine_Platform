# NETS — Homework Engine Platform

> National Education Transformation System · AI-powered gamified LMS for Uzbekistan's 8.8M K-11 students

---

## Architecture (5-Layer)

| Layer | Document | Status |
|-------|----------|--------|
| 0 | [[standards/framework/NETS-Homework-Engine-UNIFIED-Buzan\|UNIFIED-Buzan v2.0]] — single source of truth | Done |
| 1 | [[standards/library/framework/NETS-Library-Framework\|Library Framework v0.6]] — 5 families, mechanic mapping | Done |
| 2 | [[standards/library/subject-family/\|Subject Frameworks]] — per-subject production guides | 18 / ~110 |
| 3 | [[standards/framework/NETS-Tier-Overlay-Spec\|Tier Overlay v2.0]] — Basic/Premium split | Done |
| 4 | ~~Grading System~~ — DELETED (not approved for production) | — |

Supporting:
- [[standards/framework/NETS-Homework-Engine-Universal-Blueprint-Flow-Diagram\|Blueprint Flow Diagram]]
- [[standards/framework/QUICK_REFERENCE\|Quick Reference]]

---

## Subject Families

| Family | Path | Subjects | Frameworks |
|--------|------|----------|------------|
| Aniq Fanlar | [[standards/library/subject-family/Aniq Fanlar/Aniq_Fanlar_Subject_Family_Framework\|Family Doc]] | Matematika, Algebra, Geometriya, Algebra va Analiz, Geometriya Advanced | 5 |
| Til Fanlar | [[standards/library/subject-family/Til Fanlar/Til_Fanlari_Subject_Family_Framework\|Family Doc]] | English, Ona Tili, Rus Tili | 3 |
| Tabiy Fanlar | [[standards/library/subject-family/Tabiy Fanlar/Tabiy_Fanlar_Subject_Family_Framework\|Family Doc]] | Biology, Physics, Chemistry | 3 |
| Ijtimoiy Fanlar | [[standards/library/subject-family/Ijtimoiy Fanlar/Ijtimoiy_Fanlari_Subject_Family_Framework\|Family Doc]] | Tarix (x3) | 4 |
| Other Fanlar | standards/library/subject-family/Other Fanlar/ | Tarbiya/Sanat — Art, Music, PE, etc. | 0 (stub) |

### Individual Subject Frameworks

**Aniq Fanlar:**
- [[standards/library/subject-family/Aniq Fanlar/Matematika/Matematika_Subject_Framework\|Matematika]]
- [[standards/library/subject-family/Aniq Fanlar/Algebra/Algebra_Subject_Framework\|Algebra]]
- [[standards/library/subject-family/Aniq Fanlar/Geometriya/Geometriya_Subject_Framework\|Geometriya]]
- [[standards/library/subject-family/Aniq Fanlar/Algebra_va_Analiz/Algebra_va_Analiz_Subject_Framework\|Algebra va Analiz]]
- [[standards/library/subject-family/Aniq Fanlar/Geometriya_Advanced/Geometriya_Advanced_Subject_Framework\|Geometriya Advanced]]

**Til Fanlar:**
- [[standards/library/subject-family/Til Fanlar/English/English_Subject_Framework\|English]]
- [[standards/library/subject-family/Til Fanlar/Ona_Tili/Ona_Tili_Subject_Framework\|Ona Tili]]
- [[standards/library/subject-family/Til Fanlar/Rus_Tili/Rus_Tili_Subject_Framework\|Rus Tili]]

**Tabiy Fanlar:**
- [[standards/library/subject-family/Tabiy Fanlar/Biology/Biology_Subject_Framework\|Biology]]
- [[standards/library/subject-family/Tabiy Fanlar/Physics/Physics_Subject_Framework\|Physics]]
- [[standards/library/subject-family/Tabiy Fanlar/Chemistry/Chemistry_Subject_Framework\|Chemistry]]

**Ijtimoiy Fanlar:**
- [[standards/library/subject-family/Ijtimoiy Fanlar/Tarix/Tarix_Subject_Framework\|Tarix (Unified G5-6)]]
- [[standards/library/subject-family/Ijtimoiy Fanlar/Tarix/Ozbekiston_Tarixi_Subject_Framework\|O'zbekiston Tarixi]]
- [[standards/library/subject-family/Ijtimoiy Fanlar/Tarix/Jahon_Tarixi_Subject_Framework\|Jahon Tarixi]]

---

## Game Mechanics (28 total)

| Catalog | Count | Location |
|---------|-------|----------|
| Default Pool | 16 | [[standards/system/games/Game_Mechanics_Docs/DOCUMENTATION-INDEX\|Documentation Index]] |
| Interactive | 7 | [[standards/library/catalog/NETS-Interactive-Game-Catalog\|Interactive Game Catalog]] |
| Summary | all | [[standards/library/catalog/NETS-Game-Catalog-Summary\|Game Catalog Summary]] |
| Demos | 18 | [[standards/system/games/Game_Mechanics_Demos/index\|Demo Index]] |
| Specs | 21 | standards/system/games/Game_Mechanics_Docs/ |

Key docs: [[standards/system/games/Game_Mechanics_Docs/DOCUMENTATION\|Extended Documentation]]

---

## Narrative & National Pride

- [[standards/system/narrative/STRATEGY_AND_LOGIC\|Strategy & Logic]] — 55/45 origin, 70/30 type balance
- [[standards/system/narrative/Bilarmidingiz_faktlar\|Bilarmidingiz faktlar]] — 300+ "Did You Know?" facts
- [[standards/system/narrative/Milliy_hikmatlar\|Milliy hikmatlar]] — national wisdom quotes
- [[standards/system/narrative/Jahon_hikmatlari\|Jahon hikmatlari]] — global wisdom quotes
- standards/system/narrative/quotes_database.json — 4,800+ items (needs subject-tagging)
- standards/system/narrative/task_injections.json — Phase 4 injection rules

---

## UI/UX

- [[standards/system/ui-ux/NETS-UI-UX-Design-Spec\|UI/UX Design Spec]]

---

## System Design

- [[standards/system-design/v1/NETS-System-Design-v1-Summary\|System Design v1 Summary]]

---

## Library

- [[standards/library/README\|Library Overview]]
- [[standards/library/framework/NETS-Library-Framework\|Library Framework Spec]]
- standards/library/content-templates/ — schema templates
- standards/library/games/_template/ — game content template

---

## Research

- [[research/INDEX\|Research Index]] — all research grouped by topic

---

## Agents

| Agent | Config | Role |
|-------|--------|------|
| Claude | [[agents/CLAUDE\|CLAUDE.md]] | Architecture, planning, framework |
| Gemini | [[agents/GEMINI\|GEMINI.md]] | Reviews, audits, MCP memory |
| Qwen | [[agents/QWEN\|QWEN.md]] | Framework editing, compliance |
| Sonnet | [[agents/SONNET\|SONNET.md]] | Content production (Codex) |

### Content Producer Pipeline

- [[agents/content-producer/SOUL\|SOUL]] — agent identity & constraints
- [[agents/content-producer/SKILLS\|SKILLS]] — 5-step production pipeline
- [[agents/content-producer/SCHEMA\|SCHEMA]] — output format
- [[agents/content-producer/MASTER_INSTRUCTION\|MASTER_INSTRUCTION]] — National Pride engine
- [[agents/content-producer/AGENTS\|AGENTS]] — startup & session logging
- [[agents/content-producer/TOOLS\|TOOLS]] — authorized tools
- [[agents/content-producer/HEARTBEAT\|HEARTBEAT]] — monitoring checklist

---

## References

- [[references/agent-dashboard-protocol\|Agent Dashboard Protocol]]
- [[references/notion-video-lesson-tools\|Notion Video Lesson Tools]]

---

## Visuals

- visuals/Flow_diagram.jpg
- visuals/Buzan_Framework_Analysis_Report.html
- visuals/NETS-Library-Framework-Assessment.html
- visuals/NETS-Library-Framework-Audit.html
- visuals/NETS-Library-vs-System-Design-Assessment.html
- visuals/NETS_basic_vs_premium_comparison.html

---

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/check_blueprint_compliance.py` | 135+ automated spec checks |
| `scripts/generate_demo_lessons.py` | Demo homework generation |
| `scripts/md_to_docx.py` | Markdown to Word conversion |
| `scripts/build_homework_and_students.py` | Homework + student profile builder |
| `scripts/launch_squad.sh` | Multi-agent squad launcher |
| `scripts/squad-tui.sh` | Squad terminal UI |
| `scripts/scaffold_subject_family.ps1` | Subject family scaffolder |
| `build_matematika_grade5_ch1s1_uz.py` | `python-docx` builder for Grade 5 Matematika Chapter 1 Section 1.1 homework |
| `build_matematika_grade5_ch1s1_2_uz.py` | Alternate builder variant for the same chapter workflow |

---

## Recent Outputs

- `Matematika_Grade5_Ch1S1_uz.docx` — Grade 5 Matematika, Chapter 1 Section 1.1 homework in Uzbek
- `STATUS.md` — production log with completed homework entries
- `output/Matematika_Grade5_Ch1S1.1_uz.docx` — mirrored export of the same generated session

---

#NETS #overview #home
