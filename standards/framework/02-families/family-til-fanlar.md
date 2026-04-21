---
name: Til Fanlar (Language Family)
status: v0.1 draft
layer: 2 (family)
---

# Til Fanlar (Languages)

## Purpose

Language acquisition and communicative competence — reading, writing, grammar, vocabulary. Students absorb language patterns through structured exposure before rules are formalized.

## Subjects

| Subject | Uzbek Name | Grades |
|---------|------------|--------|
| Mother Tongue | Ona Tili | G1–11 |
| English | Ingliz Tili | G1–11 | **⚠ Subject override: always Hard mode — see `subject-english.md`** |
| Russian | Rus Tili | G1–11 |

## Learning outcomes

- Read and comprehend texts at grade-appropriate CEFR level
- Apply grammar rules in context (not isolated drills)
- Build vocabulary through contextual exposure, not word lists
- Produce written responses with correct structure and register
- Develop receptive skills (reading/listening) before productive (writing/speaking)

## Teaching methodology

- **Two-layer explanation:** formal grammar rule + simplified everyday example
- **Krashen i+1:** content always slightly above current level; L1 gloss toggle available at zero XP cost
- **Immersion-first:** expose to authentic content, let patterns click before formalizing rules
- **Contextual vocabulary:** words taught inside stories/dialogues/articles — never as isolated lists
- **SkyEng narrative model:** story contains target language structures; student absorbs through engagement, tested within the narrative
- **Panel 4 (Origin) SKIPPED** — nobody teaches "who invented the past tense"

## Easy mode pipeline

```
Preview (Panels 1,2,3) → Flash Cards (5-8) → Sprint (5 items) → Games (2) → Reflection
~35 min
```

Games: Sentence Fill (primary) + Memory Match (standard). No Adaptive Quiz. No Notebook Capture.

See `03-modes/easy-mode.md` for component specs and scaling.

## Hard mode pipeline

```
Preview (Panels 1,2,3,6) → Flash Cards (8-12) → Sprint (7 items) → Reading → Games (3) → Final Challenge → Reflection
~70 min | 7 components
```

**Reading phase ACTIVE** — Language is the ONLY family that uses Phase 2.
Games: Sentence Fill + Memory Match + Tile Match (Hard Slot 3).
Real-Life (Phase 4) SKIPPED — Reading covers transfer. Consolidation (Phase 5) SKIPPED.

See `03-modes/hard-mode.md` for component specs and scoring weights.

## Format specifics

| Phase | Formats | Notes |
|-------|---------|-------|
| Sprint | MC / T-F / YNNG | Vocabulary recognition, grammar identification |
| Reading | Passage + MC + T-F + short-answer | IELTS-style, 500-800 words, 3-5 questions |
| Games — Sentence Fill | Cloze (word bank or free recall G8+) | Primary language game; grammar in context; every 3rd-5th word removed |
| Games — Memory Match | 4×4 flip grid | Word pairs; word↔meaning, synonym pairs, L1↔L2 translation |
| Games — Tile Match | Drag-match pairs | Hard mode Slot 3; word↔category, grammar term↔example |
| Final Challenge | Mixed reading + writing | Short writing task G8+; MC/T-F for younger |
| Visuals | Grammar parse trees (Mermaid), vocab concept maps | See `00-core/visual-generation.md` |

### CEFR progression by grade

| Grade | CEFR target |
|-------|-------------|
| G1–2 | Pre-A1 / A1 |
| G3–4 | A1–A2 |
| G5–6 | A2–B1 |
| G7–8 | B1 |
| G9 | B1–B2 |
| G10–11 | B2–C1 |

G1–6: transition mode (L1 scaffolding present). G7–11: immersion mode (L1 on demand only).

## Key rules (compact)

- **TL-1:** Phase 2 Reading ACTIVE in Hard mode only — exclusive to this family
- **TL-2:** Phase 4 Real-Life SKIPPED in all modes
- **TL-3:** Phase 5 Consolidation SKIPPED in all modes
- **TL-4:** No Notebook Capture — no calculations
- **TL-5:** No mandatory Adaptive Quiz
- **TL-6:** Sentence Fill must appear in every Game Break session (Word Ladder is frozen to v2+)
- **TL-7:** Pronoun policy — Uzbek: "Siz" never "sen" / Russian: "Вы" never "ты" (`00-core/pronoun-policy.md`)
- **TL-8:** No cliché contexts — see `00-core/context-policy.md`

## Cross-references

- Phase specs: `01-phases/`
- Capture rule override: `00-core/capture-rule.md`
- Pronoun policy: `00-core/pronoun-policy.md`
- Context policy: `00-core/context-policy.md`
- Construction recipes (legacy, still valid): `standards/library/subject-family/Til Fanlar/`
- Reference implementation: [TBD — no Language homework built yet]
