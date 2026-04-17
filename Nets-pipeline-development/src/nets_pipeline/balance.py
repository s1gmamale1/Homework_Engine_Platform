"""National Pride origin-balance tracker.

Per `frameworks/system/phase_worker_base.md` Invariant 6:

  "55/45 origin balance — rolling 10-item window across the session:
   ~55% Uzbek references, ~45% global. The runner tracks the window;
   you honor whichever bucket this task calls for (passed in dynamic
   context)."

Injection phases (from phase_worker_base.md Invariant 6):
  - phase_0a  (gate quote from quotes_database.json)
  - phase_2   (Story Mode — ambient setting national or global)
  - phase_4   (~30% Wise Status injection)
  - phase_5   (mnemonic palace — Registan default, heritage anchor 20%)
  - phase_7   (Third Renaissance closing line on ≥60% accuracy)

NOT injected:
  - phase_0b, phase_1, phase_3, phase_6

Current strategy (v1 — deterministic, no worker feedback loop yet):
  Hash-seeded bucket assignment per (lesson_id, subject, phase_id).
  Over many lessons this tends toward the 55/45 target via the law of
  large numbers. Future iterations can wire in post-phase feedback to
  close the loop on a true rolling window.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

INJECTION_PHASES: frozenset[str] = frozenset(
    {"phase_0a", "phase_2", "phase_4", "phase_5", "phase_7"}
)

NATIONAL_TARGET_PCT: int = 55
GLOBAL_TARGET_PCT: int = 45


@dataclass
class BalanceTracker:
    """Per-lesson tracker. One instance per lesson.

    `plan` maps injection phase_id → 'national' | 'global'. It's computed
    once at lesson start and read by each phase's dynamic context.
    """
    lesson_id: str
    subject: str
    plan: dict[str, str] = field(default_factory=dict)

    def dynamic_context_for(self, phase_id: str) -> dict[str, str | int]:
        """Return the origin-balance hint to pass in Layer 7 dynamic context."""
        if phase_id not in INJECTION_PHASES:
            return {
                "origin_bucket": "either",
                "target_national_pct": NATIONAL_TARGET_PCT,
                "target_global_pct": GLOBAL_TARGET_PCT,
                "note": "not an injection phase",
            }
        bucket = self.plan.get(phase_id, "either")
        return {
            "origin_bucket": bucket,
            "target_national_pct": NATIONAL_TARGET_PCT,
            "target_global_pct": GLOBAL_TARGET_PCT,
        }


def build_tracker(lesson_id: str, subject: str) -> BalanceTracker:
    """Compute the bucket assignment for all injection phases at lesson start.

    Deterministic given (lesson_id, subject) — same inputs produce the same
    plan, which is useful for reruns and testing.
    """
    plan: dict[str, str] = {}
    for phase_id in INJECTION_PHASES:
        seed = f"{lesson_id}|{subject}|{phase_id}"
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
        bucket_value = int(digest[:8], 16) % 100
        plan[phase_id] = "national" if bucket_value < NATIONAL_TARGET_PCT else "global"
    return BalanceTracker(lesson_id=lesson_id, subject=subject, plan=plan)
