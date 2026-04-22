# Prompt: Classify Lesson — English

You are classifying an English textbook unit on two axes:

1. **Difficulty mode** — EASY or HARD (structural — drives phase count)
2. **CEFR level** — A1 through B2 (language proficiency — drives complexity)

You see this one unit only.

## Input

- Textbook unit (image or text)
- Grade hint from textbook cover (used as prior, not anchor)

## Output

One line per axis. Then one sentence explaining both.

```
Mode: HARD
Level: B1
Reason: Unit teaches past perfect + reported speech with multi-paragraph reading and production tasks.
```

---

## Axis 1: Mode — EASY or HARD

### HARD signals (any one = HARD)

- Unit introduces a new grammar structure (present perfect, conditional, passive, reported speech, relative clauses, etc.)
- Unit requires production — writing, speaking tasks, dialogue completion, guided composition
- Reading passage 200+ words with inference or opinion questions
- Word → Structure translation needed (student must read a situation and produce the target form)
- "Grammar focus" / "Grammar reference" / "Practice" section with multi-step exercises
- Listening comprehension task with Q&A

### EASY signals (all must be true)

- Vocabulary-only unit: picture labels, word lists, matching exercises
- No new grammar introduced — only recycled from prior units
- Short dialogues (≤4 turns) or picture captions, no multi-paragraph reading
- Recognition tasks only — no free production, no multi-step writing

**Mixed → HARD.** Default to HARD when in doubt — language always rewards transfer practice.

---

## Axis 2: CEFR Level

Measure all four signal axes. Compute the mode across them.

### Signal 1: Average Sentence Length (words)

| Words/sentence | Level |
|:-:|:-:|
| ≤6 | A1 |
| 7–9 | A1+ |
| 9–12 | A2 |
| 11–14 | A2+ |
| 12–16 | B1 |
| 15–20 | B1+ |
| 18–25 | B2 |

### Signal 2: Tenses Present

| Tense set present | Level |
|---|:-:|
| Present simple/continuous + basic past | A1/A1+ |
| + past simple regular, can/could, comparatives | A2 |
| + past simple irregular, must/have to | A2+ |
| + past continuous, present perfect, will/going-to, 1st cond | B1 |
| + modals (should/might/could), passive present | B1+ |
| + past perfect, 2nd/3rd cond, reported speech, modal perfects | B2 |

Highest row where ≥2 structures from that row are present.

### Signal 3: Vocabulary Band

| B1+ vocab proportion | Level |
|:-:|:-:|
| < 10% | A1/A2 |
| 10–30% | A2+/B1 |
| 30–60% | B1+ |
| 60%+ | B2 |

### Signal 4: Text Type

| Text type | Level |
|---|:-:|
| Pictures + single-word labels | A1 |
| Short dialogues, picture captions | A1+/A2 |
| Paragraph reading passage | A2+/B1 |
| Multi-paragraph narrative or argumentative | B1+/B2 |

Pick the most demanding type present, not the simplest.

---

## Grade prior (tiebreaker only)

| Grade | Default |
|:-:|:-:|
| G5 | A1 |
| G6 | A1+ |
| G7 | A2+/B1 |
| G8 | B1 |
| G9 | B1+ |
| G10 | B1+/B2 |
| G11 | B2 |

Grade is a prior, not an anchor. If signals disagree with grade by more than one level, trust the signals and log the mismatch in the reason line.

---

## Classification Rule

1. Decide Mode first (EASY or HARD) from Axis 1 signals.
2. Score each of the four CEFR signals independently → each yields a level.
3. Compute the mode (most frequent level) across the four.
4. Tie → pick the higher level (err on challenge).
5. Output: two-line stamp + one-sentence reason.

---

## Examples

### Example 1 — G5 picture-label unit → EASY A1

Unit content: animal pictures with single-word labels, one 4-word dialogue.
- Mode: no new grammar, no production → EASY
- Sentence length 4 → A1. Tenses: "is" only → A1. Vocab: core → A1. Text type: labels → A1.

**Output:** `Mode: EASY · Level: A1 · Reason: Picture labels with present "is" only — no new grammar or production.`

### Example 2 — G7 internship reading → HARD B1

Unit content: 180-word IT internship passage, present perfect + 1st conditional grammar box, writing task at the end.
- Mode: new grammar (present perfect) + writing production → HARD
- Sentence length 14 → B1. Tenses: pres perf + 1st cond → B1. Vocab: 25% B1+ → B1. Text type: multi-para → B1+.

**Output:** `Mode: HARD · Level: B1 · Reason: New grammar (present perfect + 1st conditional) plus production task — sentence length and text type confirm B1.`

### Example 3 — G11 vocabulary-review unit → EASY B1+

Unit content: review chapter, word↔definition matching, no new grammar, short dialogues, average sentence 11 words.
- Mode: vocabulary only, recognition tasks → EASY
- Signals sit at A2/B1 boundary → pick higher = B1+. Grade default B2 overridden (mismatch).

**Output:** `Mode: EASY · Level: B1+ · Reason: Vocab-only review — grade default B2 overridden because tenses and text type sit at B1 boundary.`

---

## Rules

- Output is always two lines (Mode, Level) + one-sentence reason.
- Never "I think", "maybe", "it seems". Pick one mode and one level.
- Never output a level range. Pick one.
- Carry both Mode and Level forward through all phases. Do not re-classify mid-session.
