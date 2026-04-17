"""Stage wrappers — one per §04 stage. Each wraps `run_session` with
stage-specific input prep + persistence.

  extract.py   Stage 01 — PDF → lesson.md + lessons row
  phase.py     Stage 02 — lesson.md → phase JSON + phase_outputs row
  assemble.py  Stage 03 — phase_outputs rows → homework.md
"""
