"""Task queue enumerator.

Per §03: "Before a run starts, the system enumerates every (subject,
grade, language, lesson) tuple that has a source PDF, and writes one
row per tuple into task_queue with status 'pending'."

Two seeding modes:
  (a) manifest.yaml — explicit list, operator-controlled.
  (b) textbooks dir walk — convention-based:
      textbooks/{subject}/{grade}/{lang}/*.pdf

Use manifest for production pilot runs; dir walk for quick ad-hoc.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass
from pathlib import Path

import yaml

from .config import PROJECT_ROOT, Settings
from .db import DB
from .logging_setup import get_logger

log = get_logger(__name__)


@dataclass
class TaskSeed:
    subject: str
    grade: int
    lang: str
    lesson_id: str
    pdf_uri: str


async def seed_from_manifest(db: DB, manifest_path: Path) -> int:
    """Load tasks from a YAML manifest. Returns number of rows inserted.

    Relative pdf_uri values are resolved against the manifest file's
    directory, so manifests can use short paths.
    """
    manifest_path = manifest_path.resolve()
    manifest_dir = manifest_path.parent

    with manifest_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    tasks = data.get("tasks") or []
    if not tasks:
        log.warning("seed_manifest_empty", path=str(manifest_path))
        return 0

    seeds: list[TaskSeed] = []
    for i, t in enumerate(tasks):
        try:
            raw_uri = t["pdf_uri"]
            path_str, fragment = _split_fragment(raw_uri)
            pdf_path = Path(path_str)
            if not pdf_path.is_absolute():
                pdf_path = (manifest_dir / pdf_path).resolve()
            if not pdf_path.exists():
                raise FileNotFoundError(
                    f"manifest entry {i} pdf_uri '{raw_uri}' does not resolve "
                    f"to an existing file (tried {pdf_path})"
                )
            seeds.append(
                TaskSeed(
                    subject=t["subject"],
                    grade=int(t["grade"]),
                    lang=t["lang"],
                    lesson_id=t["lesson_id"],
                    pdf_uri=str(pdf_path) + fragment,
                )
            )
        except KeyError as e:
            raise ValueError(f"manifest entry {i} missing key {e}") from e

    return await _insert_seeds(db, seeds)


async def seed_from_textbooks_dir(
    db: DB,
    root: Path,
    subject_filter: str | None = None,
    grade_filter: tuple[int, int] | None = None,
    lang_filter: str | None = None,
) -> int:
    """Convention walk: root/{subject}/{grade}/{lang}/*.pdf.

    grade_filter is (min, max) inclusive when supplied.
    """
    if not root.exists():
        raise FileNotFoundError(f"Textbooks root not found: {root}")

    seeds: list[TaskSeed] = []
    for pdf_path in sorted(root.rglob("*.pdf")):
        rel = pdf_path.relative_to(root)
        parts = rel.parts
        if len(parts) < 4:
            continue
        subject, grade_str, lang, *_ = parts
        try:
            grade = int(grade_str.replace("grade_", ""))
        except ValueError:
            continue

        if subject_filter and subject != subject_filter:
            continue
        if grade_filter and not (grade_filter[0] <= grade <= grade_filter[1]):
            continue
        if lang_filter and lang != lang_filter:
            continue

        lesson_id = f"{subject}_G{grade}_{lang}_{pdf_path.stem}"
        seeds.append(
            TaskSeed(
                subject=subject,
                grade=grade,
                lang=lang,
                lesson_id=lesson_id,
                pdf_uri=str(pdf_path.resolve()),
            )
        )

    return await _insert_seeds(db, seeds)


async def _insert_seeds(db: DB, seeds: list[TaskSeed]) -> int:
    """Insert seeds into task_queue, skipping duplicates by lesson_id."""
    if not seeds:
        return 0
    inserted = 0
    async with db.conn() as c, c.cursor() as cur:
        for s in seeds:
            # Skip if a task already exists for this lesson_id
            await cur.execute(
                "SELECT 1 FROM task_queue WHERE lesson_id = %s LIMIT 1",
                (s.lesson_id,),
            )
            if await cur.fetchone():
                continue
            await cur.execute(
                """
                INSERT INTO task_queue (task_id, subject, grade, lang, lesson_id, pdf_uri)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    str(uuid.uuid4()),
                    s.subject,
                    s.grade,
                    s.lang,
                    s.lesson_id,
                    s.pdf_uri,
                ),
            )
            inserted += 1
    log.info("seed_complete", inserted=inserted, total_candidates=len(seeds))
    return inserted


def default_textbooks_root(settings: Settings | None = None) -> Path:
    """Conventional textbooks/ location under the main repo root (parent of
    Nets-pipeline-development)."""
    return PROJECT_ROOT.parent / "textbooks"


def _split_fragment(uri: str) -> tuple[str, str]:
    """Return (path_part, '#fragment' or '')."""
    if "#" not in uri:
        return uri, ""
    path_part, frag = uri.split("#", 1)
    return path_part, "#" + frag
