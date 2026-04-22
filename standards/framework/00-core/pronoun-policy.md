---
name: pronoun-policy
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED §4.4 line 576 | §22 session decision
---

# Pronoun Policy

## Rule

All student-facing content in Uzbek uses **"Siz"** (formal/respectful second person). Never use "sen" (informal). In Russian content, use **"Вы"** (formal), never "ты". English has no equivalent distinction — use "you" naturally.

This rule is unconditional. It applies to every line of student-facing text regardless of phase, subject, or grade band.

## Scope

- Every phase: Phase 0-A (Theme Preview), 0-B (Flash Cards), Phase 1–7
- Every subject and every subject family
- All question stems, prompts, narrative passages, story mode text, scenario framing, feedback messages, reflection prompts, closing lines

## Examples

| Language | Correct | Incorrect |
|----------|---------|-----------|
| Uzbek | "Siz qanday deb o'ylaysiz?" | "Sen qanday deb o'ylaysan?" |
| Russian | "Вы можете объяснить..." | "Ты можешь объяснить..." |
| English | "What do you think..." | (no distinction required) |

## Verification

Automated regex scan after content generation:

```bash
grep -ri "\"sen\"" <output_file>
grep -ri "\"ты\"" <output_file>
```

Flag any match for human review. False positives (e.g., the Uzbek word "sen" inside a quoted example of incorrect usage) must be reviewed manually.

## Cross-references

- UNIFIED-Buzan §4.4 line 576 (canonical source)
- All subject framework production guides inherit this rule without restating it
- Agent config `agents/content-producer/SKILLS.md` — cite this file as authoritative
