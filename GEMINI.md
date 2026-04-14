# GEMINI — Project Instruction & Context Manual

**Sigma_Edu_3000 — National Education Transformation System (NETS)**
*AI-powered, gamified LMS for Uzbekistan's 8.8M K-11 students.*

---

## 🚀 Project Overview

**Sigma_Edu_3000** is the **Master Specification Hub** for the NETS project. It serves as the single source of truth for the pedagogy, game mechanics, and content architecture of a nation-wide Learning Management System aimed at improving Uzbekistan's PISA scores in Math, Reading, Science, and Creative Thinking.

### 🧠 Core Architecture: The 7-Step Learning Journey
Every homework session is structured around a "Phase Model" mapped to Bloom's Taxonomy and PISA proficiency levels:
1.  **Memory Sprint (L1):** Rapid recall/mnemonics.
2.  **Story Mode (L2):** Narrative context and concept discovery.
3.  **Game Breaks (L2-L3):** Interactive mechanics (14 unique games).
4.  **Real-Life Challenge (L4-L5):** Application of concepts toSamarkand/Uzbekistan-based scenarios.
5.  **Consolidation (L2-L3):** Review and connection.
6.  **Final Boss (L3-L6):** Tiered difficulty adaptive challenge.
7.  **Reflection (Metacognition):** Student self-evaluation.

---

## 📂 Directory Overview

| Directory | Purpose |
|-----------|---------|
| **`standards/`** | **The Single Source of Truth.** Contains the Unified Specification, Game Catalog, and PISA matrices. |
| **`scripts/`** | **Automation Layer.** Python scripts for generating demo JSONs, checking compliance, and document conversion. |
| **`research/`** | **Evidence Base.** Includes the original proposal, 6-agent quality audits, and PISA 2022 benchmarks. |
| **`textbooks/`** | **Source Material.** 266 PDFs (Grades 5-11) used as the basis for all generated content. |
| **`memory/`** | **Hive Mind Store.** Local SQLite and Obsidian-based memory files for agent synchronization. |
| **`agents/`** | **Identity Layer.** Instructions and history for Gemini, Claude, and Qwen. |

---

## 🛠️ Key Files

- **`standards/framework/NETS-Homework-Engine-UNIFIED.md`**: The master 2600-line spec. All engineering MUST follow this.
- **`HOME.md`**: High-level navigation and subsystem status tracker.
- **`scripts/generate_demo_lessons.py`**: The main content generation logic for transforming textbooks into NETS sessions.
- **`mcp-shared-memory.json`**: Configuration for the `agent-recall-mcp` shared memory hub.
- **`README.md`**: Project overview, team roles, and test credentials.

---

## 🤖 Usage Guidelines for Agents

### 1. The "Hive Mind" Sync
Before starting any task, sync with the project memory:
```bash
@mcp agent-recall recall(query="SIGMA_EDU_3000 project context")
```
### 2. PISA Alignment
Every content item created must include:
- `pisa_level` (1-6)
- `transition_skill` (The specific skill being scaffolded from L to L+1)

### 3. Cultural Relevancy
All narrative and "Real-Life Challenges" must be grounded in **Uzbekistan's culture** (Samarkand, Registan, Plov, Milliylik).

### 4. Code vs. Content
This repository is primarily for **Content Engineering and Specification**. Implementation of the "Engine" (Next.js/Python) happens in a separate repository, but the **Data Schemas** and **Content Logic** live here in `scripts/`.

---

#NETS #Gemini #InstructionalContext
