# Sigma_Edu_3000 — Project Context & Instructions

This directory contains the **NETS (National Education Transformation System)** project, an AI-powered, gamified Learning Management System (LMS) designed for Uzbekistan's 8.8M K-11 students. The primary goal is to improve national PISA scores through structured, engaging homework sessions.

## 🚀 Project Overview

*   **Purpose:** Elevate Uzbekistan's PISA performance in Mathematics, Reading, Science, and Creative Thinking.
*   **Core Logic:** A 7-step "Learning Journey" (Memory Sprint, Story Mode, Game Breaks, Real-Life Challenge, Consolidation, Final Boss, Reflection).
*   **Key Innovation:** AI-driven difficulty adaptation based on Item Response Theory (IRT) and Socratic tutoring for remediation.
*   **Authoritative Source:** `standards/NETS-Homework-Engine-UNIFIED.md` (v2.0) is the **Single Source of Truth** for all development and content creation.

## 🏗️ Architecture & Structure

The project is divided into several key areas:

### 1. Frontend Application (`/app`)
*   **Tech Stack:** Next.js 16+, React 19, TailwindCSS 4, TypeScript 5.
*   **State Management:** React Context (`src/lib/session-context.tsx`) and custom hooks.
*   **Content Loading:** Fetches JSON data from `public/data/` via `src/lib/data-loader.ts`.
*   **Key Path:** `app/src/app/session/` contains the implementation of the 7-step journey.

### 2. Standards & Specifications (`/standards`)
*   **`NETS-Homework-Engine-UNIFIED.md`**: Master specification covering game mechanics, PISA matrices, and JSON schemas.
*   **`QUICK_REFERENCE.md`**: A condensed cheat sheet for developers and designers.
*   **`EDUCATIONAL_EXPERIENCE_DESIGN.md`**: UX and pedagogical philosophy.

### 3. Content Processing & Tooling (`/scripts`)
*   **Purpose:** Scripts for OCR, parsing textbooks, generating demo lessons, and checking compliance.
*   **Key Scripts:**
    *   `generate_demo_lessons.py`: Generates the JSON data used by the app.
    *   `check_blueprint_compliance.py`: Ensures generated content meets PISA standards.
    *   `convert_md_to_docx.py`: Utility for documentation exports.

### 4. Curriculum Data (`/textbooks`, `/app/public/data`)
*   **Source:** Raw textbooks in PDF/Markdown format (Grades 5-11).
*   **Output:** Structured JSON in `app/public/data/` (e.g., `phases.json`, `student_A_malika.json`).

## 🛠️ Building and Running

### Application (Frontend)
```bash
cd app
npm install
npm run dev    # Start development server on http://localhost:3000
npm run build  # Build for production
npm run lint   # Run ESLint checks
```

### Content Scripts
*   Requires **Python 3.10+**.
*   Install dependencies (if any) as required by individual scripts.
*   Example: `python scripts/generate_demo_lessons.py`

## 📏 Development Conventions

1.  **Strict Compliance:** All engineering and content must strictly follow the standards in `standards/NETS-Homework-Engine-UNIFIED.md`.
2.  **Type Integrity:** All data structures in the app must match the interfaces defined in `app/src/lib/types.ts`.
3.  **PISA Alignment:** Every assessment item must be tagged with its corresponding PISA domain, proficiency level, and `transition_skill`.
4.  **Cultural Relevancy:** Use Uzbek names, locations (e.g., Samarkand, Registan), and cultural contexts (e.g., Bazaars, Plov) in all narratives.
5.  **AI Tiering:** Use appropriate AI models for different tasks (Tier 1 for templates, Tier 3 for complex Socratic tutoring) to manage costs.

## 🧪 Testing & Validation
*   Refer to `stress tests/` for AI-driven quality audits of the content and logic.
*   Use `scripts/verify_demos.py` to validate generated JSON files against schemas.

---
*Last Updated: April 2026*
