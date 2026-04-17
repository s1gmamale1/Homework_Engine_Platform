"""JSON Schema validation.

Validates phase/extractor outputs against frameworks/schemas/*.json.
Used by the session runner between call_model() and persist() per §08.

Schema validation failures trigger one re-prompt with the error shown to
the model, then fail the task (§11 retry policy).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator, ValidationError

from .config import FRAMEWORKS_DIR


class SchemaValidationError(Exception):
    """Raised when a model output fails its JSON Schema."""

    def __init__(self, message: str, errors: list[str]) -> None:
        super().__init__(message)
        self.errors = errors


@lru_cache(maxsize=32)
def load_schema(phase_or_lesson_id: str) -> dict[str, Any]:
    """Load a schema by id. Cached for the process lifetime.

    id examples: 'lesson', 'phase_0a', 'phase_1', 'phase_7'
    """
    path: Path = FRAMEWORKS_DIR / "schemas" / f"{phase_or_lesson_id}.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate(output: dict[str, Any], schema_id: str) -> None:
    """Raise SchemaValidationError if output violates schema."""
    schema = load_schema(schema_id)
    validator = Draft7Validator(schema)
    errors = [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in validator.iter_errors(output)
    ]
    if errors:
        raise SchemaValidationError(
            f"Output failed schema '{schema_id}' with {len(errors)} error(s)",
            errors,
        )
