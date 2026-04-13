# Agent Dashboard — Quick Reference

**Source of truth:** `Dashboard/AGENT-DASHBOARD-PROTOCOL.md` (337 lines)
**Dashboard JSON:** `Dashboard/.agent-dashboard.json`
**Web view:** `Dashboard/index.html` (open in browser)

> **PATH NOTE:** The protocol doc says `standards/.agent-dashboard.json` but the actual file is at `Dashboard/.agent-dashboard.json`. Always use the Dashboard/ location.

---

## TL;DR — What I MUST do every session

1. **REGISTER** myself as an agent at session start (one entry in `agents` object)
2. **HEARTBEAT** every 2 min OR after each milestone (update `last_heartbeat`)
3. **LOG** milestones (append to `logs`, 2-3 sentences each, past + future tense)
4. **TRACK** every file I touch (append to `files_touched`)
5. **STATUS** changes: idle / running / blocked / completed / error
6. **COMPLETE** with `status: "completed"`, `completed_percent: 100` when done

If `last_heartbeat` is older than **300 seconds (5 min)** → my agent is "stale" and other agents may take over my task.

---

## Schema

```json
{
  "heartbeat_interval_seconds": 120,
  "last_global_heartbeat": "ISO_TIMESTAMP",
  "agents": {
    "agent-name": {
      "current_task": "Brief description of what I'm doing right now",
      "status": "idle | running | blocked | completed | error",
      "completed_percent": 0,
      "last_heartbeat": "ISO_TIMESTAMP",
      "logs": [
        { "timestamp": "ISO", "entry": "What I did + what's next (2-3 sentences)" }
      ],
      "started_at": "ISO_TIMESTAMP",
      "files_touched": ["standards/file1.md", "scripts/script1.py"]
    }
  }
}
```

---

## Agent naming convention

Use descriptive names: `frontend-phase3-games`, `framework-unified-revision`, `content-kimyo-section33`, `test-compliance-checker`.

**No two agents may share a name.** If my chosen name is already registered with `status: "running"` and a heartbeat within 5 min — pick a different name.

For myself in this main interactive session, I'll use `claude-main-session`.

---

## Status meanings

| Status | When |
|---|---|
| `idle` | Before registration or after stopping |
| `running` | Actively working on current_task |
| `blocked` | Waiting on input/missing files/unresolved error |
| `completed` | current_task fully done |
| `error` | Critical failure preventing completion |

---

## Logging rules

**DO:**
- "Completed X. Found Y. Now doing Z."
- "Attempted X, failed because Y. Trying Z instead."
- "Generated 3 files at [path]. 135/135 compliance checks passed."
- "Blocked: missing textbook PDF for Grade 8 Kimyo."

**DON'T:**
- "Read file X" (too granular)
- "Running script" (no outcome)
- Long stacktraces (1-sentence summary instead)
- Every keystroke

**Rule:** 2-3 sentences max per entry. Append, never overwrite. One entry per milestone.

---

## Completed-percent buckets

| Range | Meaning |
|---|---|
| 0-10 | Just started, setup |
| 11-30 | Early progress, foundations done |
| 31-60 | Mid-work, core implementation |
| 61-85 | Late stage, polishing |
| 86-99 | Almost done, final touches |
| 100 | Done — set `status: "completed"` |

---

## Update workflow (atomic)

1. `Read` → `Dashboard/.agent-dashboard.json`
2. `Edit` → make my changes (heartbeat / log / status / files)
3. Save

Always read first to avoid clobbering another agent's update.

---

## Edge cases

**Stale agent (no heartbeat 5+ min):** Any other agent MAY change its status to `idle`, take over its task (rename to own name), and log the takeover.

**Two agents same task:** Higher `completed_percent` wins. Loser picks a different task. Both log the collision.

**Blocked:** Set `status: "blocked"` and put the reason in `current_task`. E.g., `"BLOCKED: Need Grade 8 Kimyo PDF — only Grade 7 in /textbooks/"`.

**Session resume:** Check own previous entry. If `running` or `blocked` → resume. If `completed` → register fresh. If `idle` → resume from `completed_percent`.

---

## Quick action card

| Action | Edit | How Often |
|---|---|---|
| Register | Add agent entry to `agents` | Once at start |
| Heartbeat | `last_heartbeat` + maybe `completed_percent` | Every 2 min |
| Status change | `status` | On state change |
| Log entry | Append to `logs` | After each milestone |
| File tracking | Add to `files_touched` | After each create/modify |
| Complete | `status: "completed"`, `completed_percent: 100` | When done |

---

## Dashboard view

Open `Dashboard/index.html` in a browser to see the live state of all agents. The HTML reads `.agent-dashboard.json` directly.
