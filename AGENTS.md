# Repository Guidelines

## Project Structure & Module Organization

This repository is standards-first. Core specifications live in `standards/`, with major areas under `standards/library/`, `standards/system/`, `standards/system-design/`, and `standards/subject-family/`. Research and rationale live in `research/`. Utility scripts are in `scripts/`. Source textbook PDFs are stored in `textbooks/`. Visual exports and HTML companions live in `visuals/`. Agent-specific operating notes are under `agents/`.

Treat `README.md` and the authoritative standards documents as the starting point before editing content or scripts.

## Build, Test, and Development Commands

This repo does not use a single root build tool. Use targeted commands from the project root:

```powershell
python .\scripts\generate_demo_lessons.py
python .\scripts\check_blueprint_compliance.py
python .\scripts\md_to_docx.py
node .\scripts\test_mcp_handshake.js
```

- `generate_demo_lessons.py`: generates demo lesson data.
- `check_blueprint_compliance.py`: validates content against blueprint and PISA tagging rules.
- `md_to_docx.py`: exports Markdown documents to DOCX when needed.
- `test_mcp_handshake.js`: checks MCP connectivity for agent workflows.

## Coding Style & Naming Conventions

Use Markdown for specs, JSON for structured content items, Python for content tooling, and PowerShell for Windows-first automation. Prefer 4-space indentation in Python and readable, explicit field names in JSON.

Follow existing naming patterns:
- Specs: `NETS-<Topic>-<Name>.md`
- Content items: lowercase, hyphenated filenames such as `worked-examples-ch1-items.json`
- IDs: `g5-uz-mat-ch1-we-001`

Do not rename framework folders or invent new schema fields without updating the governing spec.

## Testing Guidelines

There is no unified coverage target in this repo. Validate changes with the closest relevant script and perform file-level sanity checks.

- Run `python .\scripts\check_blueprint_compliance.py` after changing structured content rules.
- For generated JSON, confirm required fields, unique IDs, and valid parsing.
- For spec edits, verify linked paths and examples still match the current tree.

## Commit & Pull Request Guidelines

Recent commits use short imperative subjects, for example: `Add research/INDEX.md hub + graph color groups` and `Rebuild subject-family scaffold: grades 5-11 × uz/ru × 5 families`.

Keep commits scoped to one logical change. PRs should include:
- a brief purpose statement
- affected paths
- validation performed
- screenshots only when HTML/visual outputs changed

## Contributor Notes

Textbooks are the source of truth. Preserve PISA alignment, `transition_skill` tagging, and family-specific mechanic rules when producing new content.
