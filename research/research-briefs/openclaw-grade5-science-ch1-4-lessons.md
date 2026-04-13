# Production Brief — Grade 5 (uz) Science: First 10 Homework Sessions

**For:** openclaw (`openclaw-grade5-science-content` on the dashboard)
**From:** Claude (orchestrator) — 2026-04-08
**Priority:** normal
**Estimated effort:** large — 10 full homework sessions, each session ~600-900 lines of structured markdown
**Dashboard:** Register / heartbeat at `Dashboard/.agent-dashboard.json` per `Dashboard/AGENT-DASHBOARD-PROTOCOL.md`. You're already registered as `openclaw-grade5-science-content`. Pick up this task on your next heartbeat — copy this task description into `current_task`, set `status: running`, then call `POST http://localhost:9999/api/clear-pending/openclaw-grade5-science-content` to remove it from your pending queue. Heartbeat every 2 min while you work; mark `status: completed` when done.

---

## What you're producing

Ten complete homework sessions for Grade 5 (Uzbek-language) **Science** (`tabiiy fanlar`), one session per textbook section, covering the first 10 sections of the textbook.

The 10 target sections (in order):

| # | Chapter.Section | Uzbek title | Topic | Pages |
|---|---|---|---|---|
| 1 | 1.1 | Gul | The flower (reproductive organs) | 8-11 |
| 2 | 1.2 | Gulli o'simliklarning ko'payishi | How flowering plants reproduce | 12-19 |
| 3 | 1.3 | Urug'larning unib chiqishi | Seed germination | 20-24 |
| 4 | 2.1 | Yashash muhitiga moslanish | Adapting to the living environment | 25-31 |
| 5 | 2.2 | Gulli o'simliklarning moslanishlari | Flowering plant adaptations | 32-37 |
| 6 | 2.3 | Yirtqichlar va ularning o'ljalaridagi moslanishlar | Predator and prey adaptations | 38-44 |
| 7 | 3.1 | Qattiq, suyuq va gazsimon moddalarning tuzilishi | Solid, liquid, gas — structure of matter | 45-51 |
| 8 | 3.2 | Bug'lanish va kondensatsiya | Evaporation and condensation | 52-59 |
| 9 | 4.1 | Suvning xossalari | Properties of water | 60-66 |
| 10 | 4.2 | Erituvchi, eruvchi va eritma | Solvent, solute, solution | 67-73 |

**Section 1 (Ch 1.1 "Gul") is the reference implementation in the framework.** Use it as your gold standard — your output should match its shape and quality. You're not copying it verbatim; you're recreating an equivalent session for the same section using your own creativity, with the same parameters.

---

## Where to find everything

| What | Path |
|---|---|
| **Subject framework (THE input contract — read this first)** | `standards/standards_specifications/grades/5/uz/science/grade5-uz-science-framework.md` |
| **Textbook PDF (source of truth for facts)** | `textbooks/grade_5/uz/Science/5-sinf tabiiy 2024 (@elekton_darslikbot).pdf` |
| **Textbook table of contents** | `standards/standards_specifications/grades/5/uz/science/textbook-toc.md` |
| **Universal homework engine spec (the WHAT)** | `standards/NETS-Homework-Engine-UNIFIED.md` |
| **Universal blueprint (the HOW)** | `standards/NETS-Homework-Engine-Universal-Blueprint.docx` |
| **UI/UX & animation spec** | `standards/NETS-UI-UX-Design-Spec.md` |
| **Interactive Game Catalog (12 games complementary pool)** | `standards/NETS-Interactive-Game-Catalog.md` |
| **Qwen psychology research (why the parameters are what they are)** | `research-briefs/qwen-grade5-psychology-findings.md` |
| **Dashboard protocol** | `Dashboard/AGENT-DASHBOARD-PROTOCOL.md` |
| **OUTPUT FOLDER (write your lessons here)** | `standards/standards_specifications/grades/5/uz/science/lessons/` |

## Output naming convention

Save each lesson as a separate markdown file:

```
lessons/
├── lesson-01-ch1.1-gul.md
├── lesson-02-ch1.2-gulli-osimliklarning-koayishi.md
├── lesson-03-ch1.3-uruglarning-unib-chiqishi.md
├── lesson-04-ch2.1-yashash-muhitiga-moslanish.md
├── lesson-05-ch2.2-gulli-osimliklarning-moslanishlari.md
├── lesson-06-ch2.3-yirtqichlar-va-oljalaridagi-moslanishlar.md
├── lesson-07-ch3.1-moddalarning-tuzilishi.md
├── lesson-08-ch3.2-buglanish-va-kondensatsiya.md
├── lesson-09-ch4.1-suvning-xossalari.md
└── lesson-10-ch4.2-erituvchi-eruvchi-eritma.md
```

Use lowercase, hyphens, ASCII (drop apostrophes from filenames — keep them in the content). Section content is Uzbek.

---

## Lesson structure — what each file must contain

Match the **§10.2 sample chapter walkthrough** in the framework exactly. Every lesson file must have these sections:

### Required sections per lesson

```markdown
# Grade 5 (uz) Science — Lesson NN: <Uzbek Section Title>

## Metadata
- chapter
- section
- textbook pages
- standard_ref (use format UZ-SCI-5-<TOPIC>-NN — invent topic codes per your judgment, document them)
- pisa_target (Reading L?, Science L?)
- blooms_coverage (which levels)
- transition_skill (L? → L?: <skill description>)
- total_session_time (must fit 25-35 min — Grade 5 cap)

## Pre-Homework
### Theme Preview (8 panels — full Uzbek copy, ≤14-word sentences, Lexile 830-1010)
1. Summary of book content
2. Better Explanation
3. Examples
4. Real-Life Research (prefer Central Asian scientist when topic allows: Ibn Sina, Al-Biruni, Ulugh Beg, Al-Khwarizmi)
5. Personal Hook (10-11 yr old life experience)
6. Why This Matters
7. Industry Application (age-recognizable jobs only)
8. Additional Materials (link suggestions: video > article)

### Flash Cards (5-7 cards max — never more than 7)
| # | Front (term + icon) | Back (≤14-word Uzbek definition) |

## The 7-phase session

### Phase 1 — Memory Sprint (≤2 min, 5-7 mixed-format items)
- Use prior chapters of Tabiiy Fanlar for source (or Grade 4 if this is Ch 1)
- Mix Speed Match + Quick MC; avoid pure typed recall
- Each item: question, format, answer

### Phase 2 — Story Mode (5-7 min, 3 segments × 90s)
For each segment, write the FULL Uzbek narrative (≤14-word sentences, active voice, second-person). Story arc = Problem → Struggle → Discovery → Solution distributed across the 3 segments. Real historical discovery preferred. Stranger Test must pass.
- Segment 1 (Problem)
- Checkpoint 1 (comprehension question, NOT fact recall)
- Segment 2 (Struggle / Discovery)
- Checkpoint 2 (inference question)
- Segment 3 (Solution)
- Checkpoint 3 (main idea)

### Phase 3 — Game Breaks (3 games interleaved with Story Mode segments)
Per Universal §6.9 dual-catalog rule: ≥1 game from Interactive Catalog + ≥2 from Default 16. Per framework §3.5 Science-tuned selection:
- Slot 1: Tile Match OR Memory Match Blitz OR Speed Match
- Slot 2: Why Chain (max 3 levels) OR Codebreaker OR Mystery Box
- Slot 3: Notebook Capture (every 3rd session, mandatory) OR Tic Tac Toe vs AI OR Escape Room

For each game, write: name, prompt text in Uzbek, items/questions, scoring, expected duration.

### Phase 4 — Real-Life Challenge (4-6 min, first-person Expert POV)
- Student is THE expert (doctor, vet, ranger, farmer, beekeeper, weather forecaster, cook, etc. — pick what fits the topic)
- Real or realistic case
- Tricky multiple-choice with at least one plausible distractor
- Justification REQUIRED — student must explain reasoning
- Provide the prompt + 4 answer options + the correct reasoning

### Phase 5 — Consolidation (2-3 min)
Use "labeled diagram recall" variant for Science (not generic Memory Palace). Provide the diagram concept + the labels that need recall.

### Phase 6 — Sub Boss (6-8 min, HP 80)
4 questions per Boss. Distribution: 1 easy MC (-10 HP), 2 medium open reasoning (-20 each), 1 hard open reasoning + creative justification (-30 HP). Up to 30% MC permitted at Grade 5. Hint tax -5 HP. Combo +2× on 3-streak.
For each question: prompt in Uzbek, type, difficulty, damage, expected answer, 2-3 socratic hints (never reveal answer), 1-2 common errors with remediation.

### Phase 7 — Reflection (1-2 min)
Single Uzbek prompt, 1-sentence minimum response.

## Did You Know facts (4 cards — one per phase transition)
1, 2, 3, 4 — short facts in Uzbek related to the lesson topic. Real, verifiable, age-appropriate. No scary medical, no death, no abstract physics.

## Standards / tagging block
- standard_ref:
- pisa_level:
- transition_skill:
- blooms_levels: [list per phase]
- game_mechanics_used: [list]
- estimated_difficulty_band:
- expected_success_rate: target 75-85% per Qwen
```

---

## Hard rules (non-negotiable)

1. **All student-facing text in Uzbek (Latin script).** No mixed-language content. Russian/English only allowed in panel #8 of Theme Preview (Additional Materials) where the student picks.
2. **Sentence length cap: ≤14 words average.** Active voice. Lexile 830-1010L. This matches Grade 5 reading level.
3. **Flash Cards: 5-7 max per session.** Working memory ceiling. Never exceed 7.
4. **First-person Expert POV mandatory in Phase 4.** "Sen shifokorsen…" — never "Salim is the doctor…"
5. **Story Mode arc mandatory in Phase 2.** Problem → Struggle → Discovery → Solution. No exposition disguised as narrative.
6. **Stranger Test on every Story Mode segment** — a reader who's never seen the textbook must be able to follow the story and answer the checkpoint from narrative logic alone.
7. **Did You Know facts must be verifiable.** No fabricated trivia. No "scientists say…" without a name.
8. **Cultural anchors mandatory** — Uzbek names (Aziza, Bekzod, Gulnara, Sardor, Malika, Jasur, Dilnoza, Otabek), Uzbek places (Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral Sea, Charvak, Chimgan), Uzbek food/animals/plants when relevant.
9. **At least 1 Central Asian scientist per 5 lessons** in the Theme Preview Real-Life Research panel (Ibn Sina, Al-Biruni, Ulugh Beg, Al-Khwarizmi).
10. **Notebook Capture in lesson 3, 6, and 9** (every 3rd session minimum per framework §6 / Universal §6.8.1).
11. **Total session length: 25-35 min.** Pre-Homework (Theme Preview + Flash Cards) is additional and student-paced.
12. **Boss target success rate 75-85%.** Calibrate question difficulty to hit this. Don't make boss too hard.
13. **Pass threshold: 60% minimum.** Below 60% triggers Duolingo Mode (loop with simpler scaffolding until 60%+). Document this in your reflection section.
14. **Tag every item with `standard_ref`, `pisa_level`, `blooms_level`, `transition_skill`** per Universal §16 schema.

---

## Quality bar

- **Every Story Mode segment passes the Stranger Test.** If a 10-year-old who's never seen the textbook can't follow your narrative and answer the checkpoint, rewrite it.
- **Every Real-Life Challenge feels like a real decision a real expert would make.** "Sen bog'bonsen, qo'shning bog'i ko'p mevali, sening bog'ing oz mevali — sababini ayt" YES. "Hisobla: 5 + 3 ?" NO.
- **Every Notebook Capture task is something a kid CAN draw with crayons in 5 minutes.** Not a research project.
- **Every Did You Know fact triggers a "wait really?" reaction.** Boring facts get cut.
- **Run a self-check before saving each lesson:** does it match the §10.2 reference walkthrough's shape? Does it pass all 14 hard rules? Does the boss feel achievable at 75-85%?

---

## Process

1. **Pick up the task.** Copy this brief's task description into your `current_task` field, set `status: running`, call `POST http://localhost:9999/api/clear-pending/openclaw-grade5-science-content` to remove it from your pending queue.

2. **Read the framework end-to-end** (`standards/standards_specifications/grades/5/uz/science/grade5-uz-science-framework.md`) — especially §3.A, §3.B, §3.3-3.9, §10.2 sample walkthrough, and §10.5 production rules. This is your input contract.

3. **Read the textbook section by section** as you work. You can render PDF pages to text using PyMuPDF in the venv at `C:/Users/DaddysHere/Documents/Notion---Video-Lesson/.venv/Scripts/python` if you need raw text. Don't analyze or rewrite — just extract facts to ground your homework in. Example:
   ```python
   import fitz
   doc = fitz.open("textbooks/grade_5/uz/Science/5-sinf tabiiy 2024 (@elekton_darslikbot).pdf")
   text = doc.load_page(7).get_text()  # page 8 (0-indexed)
   ```

4. **Produce one lesson at a time.** Save each as you finish — don't batch all 10 at the end. Heartbeat between lessons. This way if you get interrupted, work isn't lost.

5. **Update `files_touched`** with each lesson file you save.

6. **Update `completed_percent`** as you go: 10% per lesson finished.

7. **When all 10 lessons are saved, set `status: "completed"` and `completed_percent: 100`** with a final log entry summarizing total word count, any sections you struggled with, and any flags you want the orchestrator to review.

---

## Out of scope

- **Don't modify the framework.** If you find a bug or gap in the framework, log it with `status: blocked` and `current_task: "BLOCKED: <reason>"` and the orchestrator will fix the framework.
- **Don't generate content for chapters beyond Ch 4.2.** Only the 10 sections listed.
- **Don't translate to English** anywhere except in your dashboard logs and final report.
- **Don't add features** (rewards, customization, social) — those are framework concerns, not content concerns.
- **Don't write in Russian.** All content is Uzbek-only.
- **Don't analyze the textbook content beyond fact-extraction.** Your job is HOW the content is delivered, not WHAT the content says — the textbook is the source of truth on facts.

---

## When you're done

1. All 10 files saved in `standards/standards_specifications/grades/5/uz/science/lessons/`
2. Dashboard entry shows `status: completed`, `completed_percent: 100`, all 10 file paths in `files_touched`
3. Final log entry under 200 words with: total word count across the 10 lessons, any sections that were hard, any framework gaps you hit, any cultural/factual claims you'd want a human to verify before deploying with real students.

Then stand by for the next batch (Ch 5-10 will follow).

**Go.**
