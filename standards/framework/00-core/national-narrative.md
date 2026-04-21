---
name: National Narrative (Milliylik)
status: v0.1 draft
layer: 0 (core primitive)
source: UNIFIED §1.5 National Pride module + §22 session (Yashil Makon framing)
---

# National Narrative (Milliylik)

## Purpose

Weave Uzbekistan's national identity, achievements, and aspirations naturally into homework content. NOT forced patriotism — aspirational framing that makes students feel they're building their country's future through learning.

## Tone

| DO | DON'T |
|---|---|
| "You're building Uzbekistan's future" | "Praise the president" |
| "Uzbek scientists contributed to this field" | Forced historical connections where none exist |
| Modern, aspirational, professional | Preachy, nationalistic, political |
| Connected to the lesson naturally | Shoehorned into unrelated content |

## Injection points

| Phase | Element | Frequency | Rule |
|-------|---------|:---:|---|
| 0-A Preview | **Gate Quote** | Every session | 1 quote from `quotes_database.json`. Subject-tagged. 55% national / 45% global ratio. Displayed 5s before panels. |
| 0-A Preview | **Panel 4 Origin** (Math/Science) | When applicable | If concept has Uzbek/Central Asian connection (al-Khwarizmi, Ulugh Beg, Beruni), MUST include. If no connection exists, use global origin. |
| 4 Real-Life | **Scenario context** | Every Hard-mode Math/Science session | Presidential projects as scenario frames: Yashil Makon, IT Park, Yangi O'zbekiston, metro expansion, solar initiatives. MUST feel natural — scenario must actually USE the math/science concept. |
| 7 Reflection | **Closing line** | If score ≥ 60% | Single aspirational line on end screen. Example: "Siz O'zbekistonning kelajagini quryapsiz." |

## Decision gates (per decision-enforcement.md)

| Element | MUST INCLUDE IF | MUST SKIP IF |
|---------|----------------|-------------|
| Gate quote | Always (every session, every subject) | Never skipped (except Recovery/Boss-retry) |
| Panel 4 Uzbek connection | Concept has a genuine Central Asian historical link | No genuine link exists — don't fabricate |
| Real-Life presidential frame | Mode is Hard AND family is Aniq/Tabiy AND a current national project fits the concept | Connection would be forced/artificial OR family is Til/Ijtimoiy |
| Reflection closing line | Student scored ≥ 60% | Student scored < 60% (don't celebrate failure) |

## Content sources

- `standards/system/narrative/quotes_database.json` — 4,800+ quotes, subject-tagged
- `standards/system/narrative/task_injections.json` — Wise Status injection prompts (30% of Real-Life tasks)
- Presidential initiatives list (maintained separately): Yashil Makon, IT Park, Yangi O'zbekiston, Digital Uzbekistan, One Million Programmers, Green Energy 2030

## Cross-references
- `01-phases/phase-0a-preview.md` — gate quote + Panel 4 origin
- `01-phases/phase-04-real-life.md` — scenario context framing
- `01-phases/phase-07-reflection.md` — closing line
- `00-core/context-policy.md` — modern professional context (complementary, not overlapping)
