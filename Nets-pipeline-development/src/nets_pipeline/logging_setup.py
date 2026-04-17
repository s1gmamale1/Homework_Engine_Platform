"""Structured logging setup.

Every session emits one structured event. See §13 "Observability & Failure Modes".
Log format is JSON to stdout — a downstream shipper (or dashboard) can parse it.
"""
from __future__ import annotations

import logging
import sys

import structlog

_CONFIGURED = False


def configure_logging(level: str = "INFO") -> None:
    """Configure structlog + stdlib logging once per process.

    Idempotent: multiple callers (CLI, batch runner, seed) can invoke
    this without stacking duplicate handlers on the root logger.
    """
    global _CONFIGURED
    if _CONFIGURED:
        return

    resolved_level = getattr(logging, level.upper(), logging.INFO)

    # Remove any pre-existing handlers on the root logger so reconfiguration
    # in long-running test environments doesn't double-emit.
    root = logging.getLogger()
    for h in list(root.handlers):
        root.removeHandler(h)

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=resolved_level,
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(resolved_level),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
    _CONFIGURED = True


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    return structlog.get_logger(name)
