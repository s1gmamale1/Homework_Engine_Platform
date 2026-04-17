"""Object storage for lesson.md + homework.md artifacts.

Starts local-filesystem only (§12 "Object storage: Local filesystem → S3/R2 later").
S3/R2 backend to be added when needed — keep the interface narrow.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from .config import Settings


class Storage:
    """Minimal artifact store. Writes markdown files keyed by lesson_id."""

    def __init__(self, settings: Settings) -> None:
        if settings.storage_backend != "local":
            raise NotImplementedError(
                f"Storage backend '{settings.storage_backend}' not yet implemented. "
                "Only 'local' is supported; S3/R2 comes later per §12."
            )
        self.root: Path = settings.storage_path

        # Fail fast if the storage root is unusable, rather than on first write.
        try:
            (self.root / "lessons").mkdir(parents=True, exist_ok=True)
            (self.root / "homeworks").mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise RuntimeError(
                f"Storage root '{self.root}' is not writable: {e}. "
                f"Check STORAGE_PATH in .env."
            ) from e

        probe = self.root / ".write_probe"
        try:
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
        except OSError as e:
            raise RuntimeError(
                f"Storage root '{self.root}' exists but is not writable: {e}"
            ) from e

    # ──────────────────────────────────────────────────────────────
    # Lessons (Stage 01 output)
    # ──────────────────────────────────────────────────────────────
    def write_lesson(self, lesson_id: str, body_md: str) -> tuple[Path, str]:
        """Write lesson.md and return (path, content_hash).

        content_hash is used for the `md_hash` column in the `lessons` table
        (§10), which gives the frozen doc a stable identity.
        """
        path = self.root / "lessons" / f"{lesson_id}.md"
        path.write_text(body_md, encoding="utf-8")
        content_hash = hashlib.sha256(body_md.encode("utf-8")).hexdigest()
        return path, content_hash

    def read_lesson(self, lesson_id: str) -> str:
        path = self.root / "lessons" / f"{lesson_id}.md"
        return path.read_text(encoding="utf-8")

    # ──────────────────────────────────────────────────────────────
    # Homeworks (Stage 03 output)
    # ──────────────────────────────────────────────────────────────
    def write_homework(self, lesson_id: str, rendered_md: str) -> Path:
        path = self.root / "homeworks" / f"{lesson_id}.md"
        path.write_text(rendered_md, encoding="utf-8")
        return path
