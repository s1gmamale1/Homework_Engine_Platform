"""Review queue — read-side queries for humans.

§14: flagged items go to a review queue for you or a teacher to examine.
"""
from __future__ import annotations

from dataclasses import dataclass

from nets_pipeline.db import DB


@dataclass
class ReviewItem:
    lesson_id: str
    phase_id: str
    subject: str
    grade: int
    lang: str
    verdict: str
    summary: str
    validator_model: str


@dataclass
class ValidationSummary:
    verdict_counts: list[tuple[str, int]]   # [('pass', 120), ('flag', 10), ('fail', 2)]


async def verdict_counts(db: DB) -> ValidationSummary:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            "SELECT verdict, COUNT(*) AS n FROM validation_results "
            "GROUP BY verdict ORDER BY verdict"
        )
        rows = await cur.fetchall()
    return ValidationSummary(
        verdict_counts=[(r["verdict"], int(r["n"])) for r in rows]
    )


async def recent_items(
    db: DB, *, verdict: str = "flag", limit: int = 20
) -> list[ReviewItem]:
    async with db.conn() as c, c.cursor() as cur:
        await cur.execute(
            """
            SELECT vr.lesson_id, vr.phase_id, vr.verdict, vr.verdict_summary,
                   vr.validator_model, l.subject, l.grade, l.lang
            FROM validation_results vr
            JOIN lessons l ON l.lesson_id = vr.lesson_id
            WHERE vr.verdict = %s
            ORDER BY vr.validated_at DESC
            LIMIT %s
            """,
            (verdict, limit),
        )
        rows = await cur.fetchall()
    return [
        ReviewItem(
            lesson_id=r["lesson_id"],
            phase_id=r["phase_id"],
            subject=r["subject"],
            grade=int(r["grade"]),
            lang=r["lang"],
            verdict=r["verdict"],
            summary=(r["verdict_summary"] or "")[:140],
            validator_model=r["validator_model"],
        )
        for r in rows
    ]


def render_summary(s: ValidationSummary) -> str:
    if not s.verdict_counts:
        return "No validation results yet."
    lines = ["Verdict   Count", "-" * 20]
    for v, n in s.verdict_counts:
        lines.append(f"{v:<8}  {n:>6}")
    return "\n".join(lines)


def render_items(rows: list[ReviewItem]) -> str:
    if not rows:
        return "(no items)"
    lines = []
    for r in rows:
        lines.append(
            f"[{r.verdict}] {r.lesson_id}  {r.phase_id}  "
            f"[{r.subject} G{r.grade} {r.lang}]  "
            f"model={r.validator_model}"
        )
        if r.summary:
            lines.append(f"  → {r.summary}")
    return "\n".join(lines)
