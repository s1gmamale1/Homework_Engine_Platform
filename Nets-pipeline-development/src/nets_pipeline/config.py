"""Environment config + project paths.

Loads .env (if present) and exposes typed settings for the rest of the runner.
No dynamic values here — this module is called at startup only.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Resolve project root (Nets-pipeline-development/) regardless of cwd
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORKS_DIR = PROJECT_ROOT / "frameworks"
SCHEMAS_DIR = FRAMEWORKS_DIR / "schemas"
PHASE_GRAPH_PATH = PROJECT_ROOT / "phase-graph.yaml"
MIGRATIONS_DIR = PROJECT_ROOT / "migrations"

# Load .env from project root if it exists
load_dotenv(PROJECT_ROOT / ".env", override=False)


@dataclass(frozen=True)
class Settings:
    # Postgres
    database_url: str

    # Kimi / Moonshot — api_key is optional at load time; the KimiClient
    # constructor is the true guard. Commands that don't call Kimi
    # (status, metrics, seed, review) work without a key in .env.
    moonshot_api_key: str | None
    moonshot_base_url: str
    moonshot_model: str

    # Storage
    storage_backend: str  # "local" | "s3"
    storage_path: Path

    # Runtime
    max_concurrent_tasks: int
    log_level: str
    cache_hit_target: float

    # Validator (optional — only needed in §15 Step 9)
    validator_provider: str | None
    validator_model: str | None
    anthropic_api_key: str | None
    gemini_api_key: str | None


def _require(key: str) -> str:
    v = os.environ.get(key)
    if not v:
        raise RuntimeError(
            f"Required env var '{key}' is not set. See .env.example."
        )
    return v


def _optional(key: str, default: str | None = None) -> str | None:
    return os.environ.get(key, default)


def load_settings() -> Settings:
    """Read environment once. Call at process start."""
    storage_path = Path(_optional("STORAGE_PATH", "./storage"))
    if not storage_path.is_absolute():
        storage_path = PROJECT_ROOT / storage_path

    return Settings(
        database_url=_require("DATABASE_URL"),
        moonshot_api_key=_optional("MOONSHOT_API_KEY"),
        moonshot_base_url=_optional("MOONSHOT_BASE_URL", "https://api.moonshot.ai/v1") or "",
        moonshot_model=_optional("MOONSHOT_MODEL", "kimi-k2-0711-preview") or "",
        storage_backend=_optional("STORAGE_BACKEND", "local") or "local",
        storage_path=storage_path,
        max_concurrent_tasks=int(_optional("MAX_CONCURRENT_TASKS", "4") or "4"),
        log_level=_optional("LOG_LEVEL", "INFO") or "INFO",
        cache_hit_target=float(_optional("CACHE_HIT_TARGET", "0.70") or "0.70"),
        validator_provider=_optional("VALIDATOR_PROVIDER"),
        validator_model=_optional("VALIDATOR_MODEL"),
        anthropic_api_key=_optional("ANTHROPIC_API_KEY"),
        gemini_api_key=_optional("GEMINI_API_KEY"),
    )
