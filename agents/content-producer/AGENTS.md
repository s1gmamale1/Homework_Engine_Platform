# AGENTS.md — Content Producer Workspace

## Workspace Files

| File | What It Contains |
|------|-----------------|
| SOUL.md | Framework summaries (7-phase structure, 5 families, mechanic tables, PISA/Bloom's, Buzan) + repo map + constraints |
| SKILLS.md | Production process, phase-by-phase template, context management, logging |
| SCHEMA.md | Output format (docx naming, structure summary, formatting rules) |
| TOOLS.md | Environment paths, available tools, models |
| IDENTITY.md | Agent metadata |
| USER.md | Project owner context |
| HEARTBEAT.md | Monitoring checklist |

## Session Startup

1. Read SOUL.md — you now know the framework, the families, the mechanics, the rules
2. Read SKILLS.md — you now know the production process and output template
3. Wait for assignment (or read from task message)
4. If assignment specifies chapters → do those chapters
5. If assignment says "whole book" or just names a subject → do all chapters sequentially
6. If unclear → ask: "Specific chapters or the whole book?"

**You should NOT need to re-read the full framework docs for every chapter.** SOUL.md has enough summary. Only read the full docs when:
- You need a detail not in the summary (edge case, grade-band override)
- You compacted context and lost framework knowledge
- The assignment references a rule you don't recognize

## Assignment Handling

**Single chapter:**
```
Subject: Grade 5 Math, Uzbek. Textbook: [path]. Chapter 1. Produce homework docx.
```
→ Produce 1 file: `Matematika_Grade5_Ch1_uz.docx`

**Whole book:**
```
Subject: Grade 5 Math, Uzbek. Textbook: [path]. Produce homework for all chapters.
```
→ Read TOC, produce 1 file per chapter sequentially. Update STATUS.md after each.

## Context Management

When context approaches 90%:
1. Update STATUS.md with current progress
2. Summarize completed work (don't carry full docx content in memory)
3. Compact context
4. Re-read SOUL.md summaries (they're designed to reload quickly)
5. Read STATUS.md to find where you left off
6. Continue from next unfinished chapter

**Never restart from scratch. Never lose progress.**

## Logging & Heartbeat

**STATUS.md** in the output directory is your heartbeat. Update it after EVERY docx:
- Chapter done, file name, timestamp, any issues
- Total progress (X/Y chapters complete)

External monitoring (cron/heartbeat) reads STATUS.md to determine:
- Is the agent still producing? (timestamp advancing)
- Did it error? (❌ status with error message)
- Is it done? (all chapters ✅)

## Red Lines

- Never modify framework documents (standards/ folder contents)
- Never delete existing files
- Never push to git
- Never access .env or credentials
- Output only to the assigned output_path
- When in doubt, log the issue and continue — never block the pipeline
