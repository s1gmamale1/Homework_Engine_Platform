---
name: Subject Override — English (Ingliz Tili)
status: v0.1 draft
layer: 2 (subject override)
inherits: family-til-fanlar.md
---

# English (Ingliz Tili) — Subject Override

## Why a separate component

English in Uzbekistan is taught as a FOREIGN language by teachers who often lack fluency themselves. Students need maximum structured exposure every session. There is no "light" English lesson — every session must push comprehension, grammar, and production. This override forces Hard mode always and defines dynamic adaptation within it.

Inherits all base rules from `family-til-fanlar.md`. This file specifies ONLY what's different for English.

## Override: mode = ALWAYS HARD

```
English homework: Hard mode only. Easy mode is disabled.
Pipeline must NOT downgrade to Easy based on content classification.
If content is "simple" (e.g., basic vocabulary), Hard mode still runs —
but component weights shift dynamically (see below).
```

Hard pipeline (from family adapter):
```
Preview (Panels 1,2,3,6) → Flash Cards (8-12) → Sprint (7 items) → Reading (IELTS-style) → Games (3) → Final Challenge (Boss) → Reflection
```

Always 7 components. Practical part ~42 min (within 60-min cap). Learning part ~23 min additional. No shortcuts.

## Dynamic adaptation within Hard mode

The pipeline classifies each English lesson into one of 5 sub-types. Each sub-type has a FIXED weight profile — the LLM does not choose.

### Sub-type detection (pipeline decides, not LLM)

| Sub-type | Detection signal | How pipeline detects |
|----------|-----------------|---------------------|
| **Vocabulary** | Lesson introduces a new word set (10+ new terms) | Grep for word lists, glossary sections, "new words" headers in textbook |
| **Grammar** | Lesson teaches a grammatical rule or pattern | Grep for rule statements, conjugation tables, "Grammar:" headers, pattern drills |
| **Reading Comprehension** | Lesson centers on a passage with questions | Passage > 300 words is the primary content; questions follow |
| **Literature** | Lesson covers an author, work, or literary period | Author name + dates, excerpt from a named work, literary terms |
| **Writing/Speaking** | Lesson targets productive output | "Write about...", "Describe...", "Discuss...", dialogue exercises |

If multiple signals present → pick the DOMINANT one (most textbook page area). Ties → default to Reading Comprehension.

### Fixed profiles per sub-type

| Component | Vocabulary | Grammar | Reading Comp | Literature | Writing/Speaking |
|-----------|:---:|:---:|:---:|:---:|:---:|
| **Preview depth** | 3 panels (1,2,3) | 4 panels (1,2,3,6) | 3 panels (1,2,3) | 4 panels (1,2,3,6) | 3 panels (1,2,3) |
| **Flash Cards** | 10-12 (word-heavy) | 8-10 (rule cards) | 6-8 (passage vocab) | 8-10 (literary terms) | 6-8 (structure phrases) |
| **Sprint focus** | Word recognition | Rule identification | Passage recall priming | Author/period facts | Structure recognition |
| **Reading passage** | Vocab-in-context (400-600 words) | Rule-in-context (500-700 words, demonstrates grammar) | Full IELTS-style (600-800 words) | Literary excerpt (500-800 words) | Model text (300-500 words) |
| **Reading Qs** | 3 Qs (vocab meaning from context) | 4 Qs (grammar rule application) | 5 Qs (full IELTS: MC + T-F + short-answer) | 4 Qs (theme + literary device analysis) | 3 Qs (structure + register analysis) |
| **Game 1** | Sentence Fill (morphology in context) | Sentence Fill (cloze, primary) | Tile Match (text analysis pairs) | Tile Match (literary analysis pairs) | Sentence Fill (structure practice) |
| **Game 2** | Memory Match (L1↔L2 pairs) | Memory Match (rule↔example pairs) | Memory Match (vocab from passage) | Memory Match (term↔definition) | Memory Match (phrase pairs) |
| **Game 3** | Tile Match (synonym↔antonym) | Tile Match (sentence ordering pairs) | Memory Match (passage vocab pairs) | Sentence Fill (literary quote gaps) | Tile Match (register variants) |
| **Boss format** | Fill-blank + MC (receptive) | Error correction + sentence construction | Short-answer from passage | Essay prompt (G9+) / short-answer (G5-8) | Written production (paragraph) |
| **Boss weight** | 25% | 30% | 35% | 35% | 40% (production is the test) |

### Scoring weight shifts

| Weight | Vocabulary | Grammar | Reading Comp | Literature | Writing/Speaking |
|--------|:---:|:---:|:---:|:---:|:---:|
| Sprint | 10% | 10% | 10% | 10% | 10% |
| Reading | 20% | 15% | 25% | 25% | 15% |
| Games | 45% | 45% | 30% | 30% | 35% |
| Boss | 25% | 30% | 35% | 35% | 40% |

All profiles sum to 100%. 60% pass threshold applies to all.

## Teaching methodology (English-specific)

Inherits from `family-til-fanlar.md`:
- Krashen i+1 (exposure slightly above current level)
- Pattern through exposure (show examples before formalizing rules)
- Contextual vocabulary (never isolated word lists)
- SkyEng narrative model (story contains target structures)

Additional English-specific:
- **L1 gloss toggle always available** — student can tap any word to see Uzbek/Russian translation. This is a scaffold, not a crutch. Pipeline tracks gloss usage frequency as a proficiency signal.
- **CEFR hard targets:** G3-4 = A1→A2, G5-6 = A2→B1, G7-8 = B1→B1+, G9 = B1+→B2, G10-11 = B2→B2+. Passage difficulty MUST match target CEFR band. No above-range passages (frustration) or below-range (no growth).
- **Receptive before productive:** Reading Comprehension and Literature sub-types prioritize reading (receptive). Writing/Speaking sub-type is the only one that weights productive output heavily. Grammar and Vocabulary are balanced.
- **Error correction as Boss format for Grammar:** student identifies and corrects errors in a passage, then rewrites the corrected sentence. Tests both recognition AND production.

## Key rules (English-specific overrides)

- **EN-1:** Hard mode ALWAYS. Pipeline ignores Easy mode signal for English.
- **EN-2:** Sub-type classification is FORCED by pipeline content detection. LLM does not choose.
- **EN-3:** Reading phase is ALWAYS present (inherited from Til Fanlar Hard mode).
- **EN-4:** No Notebook Capture (no calculations in English).
- **EN-5:** L1 gloss usage tracked per session → feeds CEFR level adjustment.
- **EN-6:** Writing/Speaking Boss requires minimum word count: G5-6 = 30 words, G7-8 = 60 words, G9-11 = 120 words.
- **EN-7:** Passage CEFR level must match student's target band (not current band — Krashen i+1).
- **EN-8:** If Ona Tili or Rus Tili lesson covers the same grammar rule in the same week, English lesson references the L1 parallel explicitly in Preview Panel 2 ("You already learned this in Ona Tili as...").

## Cross-references
- Base family: `02-families/family-til-fanlar.md`
- Construction recipes: `standards/library/subject-family/Til Fanlar/English/`
- CEFR framework: absorbed from UNIFIED §19
- Reference implementation: [TBD — no English homework built yet]
