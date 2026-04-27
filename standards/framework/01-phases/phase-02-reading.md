---
name: Phase 2 — Reading
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.2 (lines 695-809) + §22 session
---

# Phase 2 — Reading

> **ACTIVE FOR: Til Fanlar (Language family) ONLY.**
> All other families skip this phase. The session routes directly from Phase 1 to Phase 3.
> Narrative content for other families is absorbed as follows:
> - Aniq Fanlar (Math): narrative woven into Preview panels (Phase 0-A)
> - Tabiy Fanlar (Sciences): narrative delivered inside Phase 4 Real-Life Challenge as a process-story intro
> - Ijtimoiy Fanlar (History/Social): narrative delivered in Phase 0-A Preview as primary-source framing

---

## Purpose (WHAT)

Build reading comprehension and language processing skills through an IELTS-style passage + gated comprehension task — transferring the student from passive recognition (Phase 1) to active meaning-making with a target-language text.

---

## Structure (HOW)

**Step 1 — Reading Passage (one continuous text, no headers or labels):**

- Length: 500–800 words (see Adaptable parameters for grade-band scaling)
- Language: target language of the subject (English for English, Russian for Rus Tili, Uzbek for Ona Tili)
- The passage is built around the current lesson's textbook content — it does NOT introduce external curriculum
- Passage construction follows a four-beat arc baked invisibly into the narrative:
  - **Problem** — opens with a genuine situation, question, or tension the reader wants to resolve
  - **Struggle** — characters or voices attempt familiar approaches; the tension holds
  - **Discovery** — the lesson concept emerges as the natural resolution tool
  - **Solution** — the concept is applied and the situation resolves; the reader has earned closure
- These beats are INGREDIENTS, not output labels. The student sees one flowing text — no "Muammo:", "Struggle:", "Discovery:" section headers. Any structural marker visible in the output is a production error.
- Real historical events, documented cases, or authentic narrative sources are preferred over invented scenarios when available.
- For English/Russian lessons: the passage is fully in the target language. L1 support is a UI toggle, not inline — it appears via a tap-to-reveal word-level gloss.
- For Ona Tili: Uzbek literary or informational text aligned to the current chapter.
- Pronoun policy: `00-core/pronoun-policy.md` applies. Uzbek = "Siz". Russian = "Вы".
- National Pride tag: each passage carries `setting_origin: "national" | "global"`. Rolling 55/45 balance across sessions (yearly guideline, not per-session mandate).

**Step 2 — Comprehension Questions (3–5 questions, gated):**

Question types drawn from IELTS-style comprehension taxonomy only:
- Main idea identification ("What is the central point of the passage?")
- Inference ("What can we conclude from the third paragraph?")
- Cross-segment comparison ("How does the character's approach in paragraph 2 differ from paragraph 4?")
- Author/character purpose ("Why does the narrator mention X?")
- Vocabulary in context ("As used in line 12, what does 'X' most nearly mean?")

Prohibited question types for this phase: fact recall ("What is the formula for X?"), fill-in-blank, translation drills. Fact recall belongs in Phase 1 Memory Sprint.

Gating mechanic:
- Student cannot advance past a question without a correct or accepted answer
- On wrong answer: show an explanation referencing the relevant passage sentence, then re-ask
- Maximum 2 retries per question. After 2 failures: a simplified restatement of the same question
- Time-on-passage monitored: < 30 seconds triggers a "Did you read the passage?" prompt (skimming flag)

**Stranger Test (quality gate before production):**
A person who has never seen the textbook chapter can follow the passage and answer the comprehension questions using only the narrative logic — no prior subject knowledge required. If prior knowledge is required to answer, the question is a recall item and must be moved to Phase 1. Passages that fail this test are returned to the content pipeline for rewrite.

**Buzan — 80/20 Keyword Tagging (pipeline-internal, not student-facing):**
Each passage has its `keywords_80_20` extracted — the ~20% of words carrying ~80% of meaning. These feed Phase 5 Consolidation branch labels and Phase 0-B Flash Card fronts.

---

## Cognitive load

| Axis | Range |
|------|-------|
| Bloom's taxonomy | L2 (Understand) — L4 (Analyze) |
| PISA literacy | L2 — L3 |
| Time budget | 5–7 min standard · ~10 min extended (longer passage + 5 questions) |
| Cognitive mode | Sequential reading → reflective comprehension → gated response |

---

## Inputs

- Textbook chapter/topic (current lesson only — no cross-chapter injection)
- Subject family tag: must be `til-fanlar` — if not, this phase is skipped
- Language of instruction (English / Russian / Uzbek)
- Grade band (determines passage length and question count — see Adaptable parameters)
- Archetype tag (Receptive and Productive archetypes use this phase; Lexical/Grammar may shorten or skip)
- `00-core/pronoun-policy.md`

---

## Outputs

- Per-question: correct/incorrect flag, time-on-question, retry count, skill tag `[Bloom: LX | PISA: LX]`
- Phase aggregate: comprehension score %, question-level skill breakdown
- `keywords_80_20` array (consumed by Phase 5 Consolidation and Phase 0-B Flash Cards)
- Skimming flag (boolean, passed to Phase 7 Reflection analytics)
- This phase does NOT emit a damage/HP delta — it is not scored against HP

---

## Adaptable parameters

| Parameter | G5–6 Default | G7–8 Default | G9–11 Default | Override condition |
|-----------|-------------|--------------|---------------|-------------------|
| Passage length | 500–600 words | 600–700 words | 700–800 words | Receptive archetype: upper bound; Lexical archetype: lower bound |
| Question count | 3 | 4 | 5 | Extended mode: +1 |
| Question format mix | Main idea + inference + vocabulary | All 5 types eligible | All 5 types, weighted toward inference + purpose | — |
| L1 gloss | ON by default, toggleable | OFF by default, toggleable | OFF, not available | Teacher override via teacher-controls |
| Retry limit | 2 | 2 | 1 | — |
| Skimming threshold | 30 s | 45 s | 60 s | Longer passages proportionally adjusted |

---

## Subject-specific examples

**English (Til Fanlar — Grade 7, lesson: Present Perfect vs. Past Simple)**

Passage spine: A short article about a Tashkent student who has just finished her first IT Park project (national setting). The text naturally uses both tenses in context. Questions probe: main idea, inference about why the writer chose "have finished" vs. "finished", vocabulary in context.

**Russian / Rus Tili (Grade 8, lesson: Причастный оборот)**

Passage: A news-style excerpt about the Afrosiyob high-speed train (national arena). Participial phrases appear naturally in the text. Questions: main idea, purpose of a specific clause, cross-paragraph comparison.

**Ona Tili (Grade 9, lesson: Murakkab qo'shma gap)**

Passage: Excerpt from a modern Uzbek short story or adapted literary text aligned to the chapter. Questions: inference, vocabulary in context, author purpose.

---

## Verification rules

1. **Family gate:** If `subject_family != "til-fanlar"` → phase must be absent from session output. Violation: any non-Language session containing a Phase 2 block.
2. **No beat labels in output:** The passage must not contain section headers, beat labels ("Muammo:", "Discovery:"), or numbered segments. Automated check: scan passage text for any of the prohibited label strings.
3. **Question type compliance:** Each question must be tagged with one of the five IELTS-style types. Fact-recall questions (answer derivable from memorized formula/definition without reading the passage) are rejected.
4. **Stranger Test gate:** Comprehension questions must be answerable from the passage text alone. If the correct answer requires knowledge not present in the passage, the question fails.
5. **Bloom/PISA tags required:** Every question carries `[Bloom: LX | PISA: LX]`. Missing tags = production block.
6. **Passage length bounds:** Passage word count must fall within grade-band range. Out-of-range passages are flagged by `scripts/check_blueprint_compliance.py`.
7. **Pronoun compliance:** All Uzbek-language passages and questions use "Siz", never "sen". Russian passages and questions use "Вы", never "ты". Reference: `00-core/pronoun-policy.md`.
8. **No external curriculum:** Every concept and vocabulary item tested must be traceable to the current textbook chapter. Cross-chapter injection is prohibited.

---

## Integration points

**Entry (called by Phase 1 exit):**
- Receives: phase-01 aggregate score, student PISA level estimate, family tag
- Guard: if `family != "til-fanlar"` → emit `phase_02_status: "skipped"` and route to Phase 3
- If entered: load passage + questions for current `standard_ref`

**Exit (calls Phase 3):**
- Emits: `phase_02_score` (comprehension %), `phase_02_keywords` array, `skimming_flag`
- Phase 3 game selection algorithm MAY use `phase_02_score` to weight stretch vs. reinforcement games
- Passes current `pisa_level` estimate (updated if comprehension score differs significantly from Phase 1 estimate)

**Cross-references:**
- `00-core/pronoun-policy.md` — enforced on all passage and question text
- `00-core/skill-taxonomy.md` — comprehension maps to "translation" and "critical-thinking" skill axes
- `00-core/pisa-framework.md` — question PISA tagging
- Phase 0-B Flash Cards — receive `keywords_80_20` from this phase
- Phase 5 Consolidation — receives `keywords_80_20` for branch labels

---

## UX/animation spec

**Passage display:**
- Single scrollable card with clean reading typography (no chrome distractions)
- Reading progress indicator: thin bar at top of card (scroll-position-based, not time-based)
- L1 gloss: tap any underlined word → inline tooltip with L1 translation (Grade 5–6 default ON; Grade 7+ default OFF)
- No autoplay audio unless student taps the speaker icon (reading aloud available as accessibility feature)

**Comprehension questions:**
- Questions appear one at a time below the passage (passage remains visible above the fold)
- Answer input: MC tap-select or short-answer text box depending on question type
- On wrong answer: relevant passage sentence highlighted in amber; explanation text shown below the question
- On correct answer: green pulse + brief positive feedback, next question slides in from right
- Retry simplified question: displayed with a "Try a simpler version" label — no penalty messaging

**Phase transitions:**
- Entry: passage fades in with a 300ms ease-in (no hard cut from Phase 1)
- Skip (non-Language families): silent, no animation — Phase 1 exit routes directly to Phase 3 without a visible "Phase 2 skipped" screen
- Exit: final question confirmed → progress bar fills → slide-right transition to Phase 3
