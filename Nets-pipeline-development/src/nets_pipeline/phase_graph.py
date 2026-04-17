"""Phase graph loader.

Parses phase-graph.yaml into typed records. Used by:
  - stages/phase.py to look up framework_ref + games_used per phase
  - scheduler.py (§15 Step 5) for topological sort + parallel wave planning

Doc §04 Phase Graph plug:
  "The system doesn't care what's in it as long as the graph is valid
   (no cycles, every framework_ref resolves)."

We validate both on load.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

from .config import FRAMEWORKS_DIR, PHASE_GRAPH_PATH, PROJECT_ROOT


@dataclass(frozen=True)
class PhaseSpec:
    id: str
    name: str
    depends_on: tuple[str, ...]
    framework_ref: str
    schema_ref: str | None = None
    games_used: tuple[str, ...] = field(default_factory=tuple)


class PhaseGraphError(Exception):
    pass


def load_phase_graph(path: Path = PHASE_GRAPH_PATH) -> dict[str, PhaseSpec]:
    """Parse the YAML, validate, return {phase_id: PhaseSpec}."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    raw_phases = data.get("phases") or []
    if not raw_phases:
        raise PhaseGraphError(f"No 'phases' found in {path}")

    specs: dict[str, PhaseSpec] = {}
    for block in raw_phases:
        pid = block.get("id")
        if not pid:
            raise PhaseGraphError(f"Phase entry missing 'id': {block}")
        if pid in specs:
            raise PhaseGraphError(f"Duplicate phase id: {pid}")

        framework_ref = block.get("framework_ref")
        if not framework_ref:
            raise PhaseGraphError(f"Phase {pid} missing framework_ref")
        if not _resolve(framework_ref).exists():
            raise PhaseGraphError(
                f"Phase {pid}: framework_ref '{framework_ref}' does not resolve to a file"
            )

        schema_ref = block.get("schema_ref")
        if schema_ref and not _resolve(schema_ref).exists():
            raise PhaseGraphError(
                f"Phase {pid}: schema_ref '{schema_ref}' does not resolve"
            )

        games = tuple(block.get("games_used") or ())
        for g in games:
            if not (FRAMEWORKS_DIR / "games" / f"{g}.md").exists():
                raise PhaseGraphError(
                    f"Phase {pid}: game '{g}' not found in frameworks/games/"
                )

        specs[pid] = PhaseSpec(
            id=pid,
            name=block.get("name", pid),
            depends_on=tuple(block.get("depends_on") or ()),
            framework_ref=framework_ref,
            schema_ref=schema_ref,
            games_used=games,
        )

    # Validate dependencies reference real phases
    for pid, spec in specs.items():
        for dep in spec.depends_on:
            if dep not in specs:
                raise PhaseGraphError(
                    f"Phase {pid}: depends_on references unknown phase '{dep}'"
                )

    # Cycle detection (Kahn's algorithm)
    _check_acyclic(specs)
    return specs


def _resolve(ref: str) -> Path:
    p = Path(ref)
    return p if p.is_absolute() else PROJECT_ROOT / ref


def _check_acyclic(specs: dict[str, PhaseSpec]) -> None:
    in_degree = {pid: 0 for pid in specs}
    for spec in specs.values():
        for dep in spec.depends_on:
            in_degree[spec.id] = in_degree.get(spec.id, 0) + 1
    queue = [p for p, d in in_degree.items() if d == 0]
    visited = 0
    while queue:
        current = queue.pop(0)
        visited += 1
        for spec in specs.values():
            if current in spec.depends_on:
                in_degree[spec.id] -= 1
                if in_degree[spec.id] == 0:
                    queue.append(spec.id)
    if visited != len(specs):
        raise PhaseGraphError("Phase graph contains a cycle")


def topological_waves(specs: dict[str, PhaseSpec]) -> list[list[str]]:
    """Return phases grouped into parallel waves (Kahn's, layered).

    Wave N contains all phases whose deps all live in waves 0..N-1.
    Within a wave, phases can run concurrently. Used by §15 Step 5 scheduler.
    """
    remaining: dict[str, set[str]] = {p: set(s.depends_on) for p, s in specs.items()}
    waves: list[list[str]] = []
    while remaining:
        ready = sorted(p for p, deps in remaining.items() if not deps)
        if not ready:
            raise PhaseGraphError("Cycle detected during wave planning")
        waves.append(ready)
        for p in ready:
            remaining.pop(p)
        for deps in remaining.values():
            deps.difference_update(ready)
    return waves


def filter_phases(specs: dict[str, PhaseSpec], ids: Iterable[str]) -> dict[str, PhaseSpec]:
    """Subset of specs keyed by a subset of phase ids, preserving structure."""
    wanted = set(ids)
    return {p: s for p, s in specs.items() if p in wanted}
