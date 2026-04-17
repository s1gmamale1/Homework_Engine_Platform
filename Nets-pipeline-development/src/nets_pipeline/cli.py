"""CLI — the 'one click' operator interface.

Per §03:
  "A single command: nets-run --subject history --grades 5-11 --lang uz.
   It enumerates the queue, spawns the worker pool, streams progress,
   and is interruptible at any point without corrupting state."

Commands:
  seed    — populate task_queue from manifest.yaml or textbooks/
  run     — claim and process tasks (respects filters)
  status  — print queue summary
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import typer

# Windows default asyncio loop (ProactorEventLoop) is incompatible with
# psycopg3's async mode. Switch to the selector-based policy before any
# asyncio.run() call in this process.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from .batch import run_batch
from .config import PROJECT_ROOT, load_settings
from .dashboard import (
    cost_rollup,
    phase_breakdown,
    queue_summary,
    recent_failures,
    render_cost,
    render_failures,
    render_phases,
    render_queue,
    render_subjects,
    subject_breakdown,
)
from .db import DB
from .logging_setup import configure_logging
from .seed import default_textbooks_root, seed_from_manifest, seed_from_textbooks_dir

app = typer.Typer(add_completion=False, help="NETS autonomous homework pipeline.")


def _parse_grades(s: str | None) -> tuple[int | None, int | None]:
    if not s:
        return None, None
    if "-" in s:
        a, b = s.split("-", 1)
        return int(a), int(b)
    g = int(s)
    return g, g


# ══════════════════════════════════════════════════════════════════════
# seed
# ══════════════════════════════════════════════════════════════════════
@app.command()
def seed(
    manifest: Path = typer.Option(
        None, help="YAML manifest listing tasks. Falls back to --textbooks-dir."
    ),
    textbooks_dir: Path = typer.Option(
        None,
        help="Convention walk: {dir}/{subject}/{grade}/{lang}/*.pdf. "
        "Default: <repo>/textbooks",
    ),
    subject: str | None = typer.Option(None, help="Filter by subject."),
    grades: str | None = typer.Option(None, help="Grade or range, e.g. '5' or '5-11'."),
    lang: str | None = typer.Option(None, help="Filter by language (uz|ru)."),
) -> None:
    """Enumerate PDFs into task_queue."""
    settings = load_settings()
    configure_logging(settings.log_level)

    async def _run() -> int:
        db = DB(settings)
        await db.open()
        try:
            if manifest:
                return await seed_from_manifest(db, manifest)
            root = textbooks_dir or default_textbooks_root(settings)
            grade_min, grade_max = _parse_grades(grades)
            grade_filter = (
                (grade_min, grade_max)
                if grade_min is not None and grade_max is not None
                else None
            )
            return await seed_from_textbooks_dir(
                db,
                root=root,
                subject_filter=subject,
                grade_filter=grade_filter,
                lang_filter=lang,
            )
        finally:
            await db.close()

    n = asyncio.run(_run())
    typer.echo(f"Seeded {n} tasks.")


# ══════════════════════════════════════════════════════════════════════
# run
# ══════════════════════════════════════════════════════════════════════
@app.command()
def run(
    subject: str | None = typer.Option(None, help="Filter by subject."),
    grades: str | None = typer.Option(None, help="Grade or range, e.g. '5' or '5-11'."),
    lang: str | None = typer.Option(None, help="Filter by language (uz|ru)."),
    phases: str | None = typer.Option(
        None, help="Comma-separated phase ids to run (default: all)."
    ),
) -> None:
    """Run the batch: claim tasks and produce homework files."""
    grade_min, grade_max = _parse_grades(grades)
    phase_ids = [p.strip() for p in phases.split(",")] if phases else None

    counts = asyncio.run(
        run_batch(
            subject=subject,
            grade_min=grade_min,
            grade_max=grade_max,
            lang=lang,
            phase_ids=phase_ids,
        )
    )
    typer.echo(
        f"Batch complete — claimed={counts['claimed']} "
        f"done={counts['done']} failed={counts['failed']}"
    )


# ══════════════════════════════════════════════════════════════════════
# status
# ══════════════════════════════════════════════════════════════════════
@app.command()
def status() -> None:
    """Print counts per status in task_queue."""
    settings = load_settings()
    configure_logging(settings.log_level)

    async def _run() -> list[tuple[str, int]]:
        db = DB(settings)
        await db.open()
        try:
            async with db.conn() as c, c.cursor() as cur:
                await cur.execute(
                    "SELECT status, COUNT(*) AS n FROM task_queue GROUP BY status ORDER BY status"
                )
                rows = await cur.fetchall()
                return [(r["status"], r["n"]) for r in rows]
        finally:
            await db.close()

    rows = asyncio.run(_run())
    if not rows:
        typer.echo("task_queue is empty.")
        return
    typer.echo("Status       Count")
    typer.echo("-" * 24)
    for s, n in rows:
        typer.echo(f"{s:<12} {n}")


# ══════════════════════════════════════════════════════════════════════
# validate (§15 Step 9 — post-hoc async validator)
# ══════════════════════════════════════════════════════════════════════
@app.command()
def validate(
    limit: int = typer.Option(100, help="Max phase_outputs to check in this sweep."),
    concurrency: int = typer.Option(4, help="Concurrent validator calls."),
    subject: str | None = typer.Option(None, help="Filter by subject."),
    lang: str | None = typer.Option(None, help="Filter by language."),
) -> None:
    """Run the async validator over unvalidated phase_outputs."""
    settings = load_settings()
    configure_logging(settings.log_level)

    # Lazy import — nets_validator brings in the anthropic SDK only when this
    # command is used. Main pipeline doesn't require it.
    from nets_validator.sweep import run_sweep

    result = asyncio.run(
        run_sweep(
            settings=settings,
            limit=limit,
            concurrency=concurrency,
            subject=subject,
            lang=lang,
        )
    )
    typer.echo(
        f"Sweep: evaluated={result.evaluated} "
        f"pass={result.pass_n} flag={result.flag_n} "
        f"fail={result.fail_n} errors={result.errors}"
    )


@app.command()
def review(
    verdict: str = typer.Option("flag", help="pass | flag | fail"),
    limit: int = typer.Option(20, help="Rows to show."),
    summary_only: bool = typer.Option(
        False, "--summary", help="Show verdict counts only."
    ),
) -> None:
    """Read the validator's review queue."""
    settings = load_settings()
    configure_logging(settings.log_level)

    from nets_validator.review import (
        recent_items,
        render_items,
        render_summary,
        verdict_counts,
    )

    async def _run() -> None:
        db = DB(settings)
        await db.open()
        try:
            if summary_only:
                typer.echo(render_summary(await verdict_counts(db)))
                return
            items = await recent_items(db, verdict=verdict, limit=limit)
            typer.echo(render_items(items))
        finally:
            await db.close()

    asyncio.run(_run())


# ══════════════════════════════════════════════════════════════════════
# metrics (§15 Step 8 observability)
# ══════════════════════════════════════════════════════════════════════
@app.command()
def metrics(
    failures: bool = typer.Option(False, "--failures", help="Show recent failed tasks."),
    subjects: bool = typer.Option(False, "--subjects", help="Breakdown by subject."),
    phases: bool = typer.Option(False, "--phases", help="Breakdown by phase_id."),
    failures_limit: int = typer.Option(10, help="Rows to show with --failures."),
) -> None:
    """Print dashboard metrics. Default view: queue + cost rollup."""
    settings = load_settings()
    configure_logging(settings.log_level)

    async def _run() -> None:
        db = DB(settings)
        await db.open()
        try:
            if failures:
                typer.echo(render_failures(await recent_failures(db, failures_limit)))
                return
            if subjects:
                typer.echo(render_subjects(await subject_breakdown(db)))
                return
            if phases:
                typer.echo(render_phases(await phase_breakdown(db)))
                return

            # Default: queue summary + cost rollup
            typer.echo(render_queue(await queue_summary(db)))
            typer.echo("")
            typer.echo(render_cost(await cost_rollup(db), settings.cache_hit_target))
        finally:
            await db.close()

    asyncio.run(_run())


if __name__ == "__main__":
    app()
