# AGENTS.md — Content Producer Workspace

## Workspace Files

| File | What It Contains |
|------|-----------------|
| SOUL.md | Lean briefing: identity, constraints, session structure summary, family quick-ref, reference map (what to read and when) |
| SKILLS.md | The production pipeline: 5 steps with 📖 READ markers telling you exactly when to read which doc |
| SCHEMA.md | Output format: .md naming, structure summary, formatting rules |
| TOOLS.md | Available tools, authorized read/write paths |
| HEARTBEAT.md | External monitoring checklist |
| MASTER_INSTRUCTION.md | National Pride engine details (55/45, 70/30, Wise Status recipe, phase trigger map) |

## Session Startup

1. Read **SOUL.md** — you now have a summary of the framework + a reference map of every doc and when to read it
2. Read **SKILLS.md** — you now have the 5-step production pipeline
3. Wait for assignment (or read from task message)
4. **Run Step 1: Pre-Flight** (from SKILLS.md):
   - Read Family Doc FULLY
   - Read Subject Framework FULLY
   - Scan Textbook TOC
5. Start producing chapters (Steps 2-5 in SKILLS.md, looping per chapter)

**Key principle:** You do NOT front-load all framework docs. You read what you need, when you need it. SKILLS.md tells you exactly when.

## Assignment Examples

**Single chapter:**
```
Subject: Grade 5 Math, Uzbek. Textbook: [path]. Chapter 1. Produce homework .md.
```
→ Pre-flight → Extract Ch1 → Map → Deep Read + Write → Log. Done.

**Whole book:**
```
Subject: Grade 5 Math, Uzbek. Textbook: [path]. Produce homework for all chapters.
```
→ Pre-flight → Loop (Extract → Map → Deep Read + Write → Log) per chapter.

**Unclear:** Ask: "Specific chapters or the whole book?"

## Context Management

At ~90% capacity:
1. Update STATUS.md
2. Summarize key framework knowledge (keep rules, drop verbatim text)
3. Compact context
4. Re-read SOUL.md (lean, reloads fast)
5. If you lost Family/Subject framework knowledge → re-read them
6. Read STATUS.md → continue from next unfinished chapter

**Never restart from scratch. Never lose progress.**

## Red Lines

- Never modify framework documents (standards/ folder)
- Never delete existing files
- Never push to git
- Never access .env or credentials
- Output only to the assigned output_path
- When in doubt, log the issue and continue — never block the pipeline
