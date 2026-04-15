# NETS Game Mechanics — Functional Documentation
## Why Chain · Peer Teaching · Reflection Journal · Puzzle Lock

Version: 1.0 | April 2026 | For: NETS Content & Engineering Teams

---

# 1. WHY CHAIN

## What It Is
A recursive Socratic conversation. The AI asks one "Why?" question. The student answers. The AI acknowledges and asks "Why?" again — drilling one layer deeper each time — until the student reaches the mechanism, principle, or root cause behind a concept. The chain only ends at the target depth or when the 3-minute timer expires.

## How It Is Played

### Step-by-step flow
1. AI presents Level 1 question (surface observable fact)
2. Student types answer in free text
3. AI reads response, acknowledges it, asks the next deeper "Why?"
4. Student answers again
5. Repeat for 3–5 levels
6. At final level: AI confirms the student has reached the core concept and names it
7. Grade awarded based on levels completed and reasoning quality

### Chain structure

| Level | Target | AI Behaviour |
|---|---|---|
| 1 — Surface | Observable fact | Asks why the observation exists |
| 2 — Mechanism | How it actually works | Asks what enables that mechanism |
| 3 — Process | The step-by-step of the mechanism | Asks why those steps work |
| 4 — Principle | Underlying law or rule | Asks what would happen if the principle changed |
| 5+ — Synthesis | Competing explanations, edge cases | Accepts multiple valid answers |

### AI rules (hard constraints)
- NEVER give the direct answer — only probe, acknowledge, redirect
- ALWAYS acknowledge before probing: "Yaxshi boshlanish!" / "Ajoyib!" before the next Why
- ALWAYS reference specific textbook pages if the student is stuck: "Sahifa 7ga qarang"
- When student answer is wrong: do not say "wrong" — ask a redirecting question instead
- When student answer is partially right: build on the correct part, probe the gap

### Parameters
- Timer: 3 minutes
- Minimum chain depth: 3 levels (configurable per topic)
- Grade: Type B (Rubric-Based) — Chain depth (% of levels reached) + Reasoning quality (% of levels with substantive answers). See GRADING-SYSTEM.md.
- AI Tier: 2 (live generative — most expensive Phase 3 mechanic)
- Input: free text (typed), minimum 3 characters per response

### PISA scaling

| PISA Level | Chain depth | Scaffolding style |
|---|---|---|
| L2–3 | 2–3 levels | Guided — AI suggests which direction to think |
| L3–4 | 4 levels | Moderate — AI waits longer before nudging |
| L5–6 | 5+ levels | Open — competing explanations accepted, no single right answer |

## Subject Implementations

### Natural Sciences — Photosynthesis
- L1: "Why do plants need sunlight?"
- L2: "Why does light give them energy specifically?"
- L3: "What do plants do with that energy — step by step?"
- L4: "Why can plants make food from CO₂ and water but animals can't?"
- L5+: "What would happen to life on Earth if the sun emitted only infrared light?"

### Natural Sciences — Ecosystems
- L1: "Why do ecosystems need both predators and prey?"
- L2: "What happens to plant populations if all wolves disappear?"
- L3: "Why does removing one species cause a cascade across the whole ecosystem?"
- L4: "What is the underlying principle that keeps ecosystems in balance?"

### Social Sciences / History — Silk Road
- L1: "Why did traders use the Silk Road instead of sea routes?"
- L2: "Why did cities like Samarkand grow specifically along the route?"
- L3: "Why did cultural exchange happen alongside trade — why didn't merchants just trade and leave?"
- L4: "What is the underlying principle that causes trade routes to produce cultural change?"

### Social Sciences / History — Cause of World War I
- L1: "Why did Franz Ferdinand's assassination start a world war?"
- L2: "Why did one assassination trigger so many countries to fight?"
- L3: "Why did the alliance system make the war spread rather than stay contained?"
- L4: "What structural conditions made WWI inevitable regardless of the assassination?"

### Exact Sciences — Gravity (Physics, G7+)
- L1: "Why do objects fall to the ground?"
- L2: "Why does mass cause attraction — what is gravity actually doing?"
- L3: "Why does the Moon not fall to Earth even though gravity pulls it?"
- L4: "Why does the same force that keeps the Moon in orbit also cause tides?"

### Reading / Literature
- L1: "Why did the main character lie to his father?"
- L2: "Why did he feel he had no other choice?"
- L3: "Why did the author make him feel trapped — what does this tell us about the theme?"
- L4: "Why do stories need characters who make bad choices?"

## Subject Restrictions

| Subject Family | Status | Depth cap |
|---|---|---|
| Natural Sciences | Primary mechanic | 5 levels |
| Social Sciences / History | Primary mechanic — intro chapters excluded | 3 levels |
| Reading / Literature | Secondary mechanic | 4 levels |
| Exact Sciences | Secondary, G6+ only | 2 levels G5, 3 levels G6+ |
| Language Sciences | Rarely used | 2 levels max |
| Arts / Tarbiya | Not recommended | — |

**History restriction:** Do not use Why Chain in introductory/Chapter 1 lessons. Students lack the prior knowledge base to sustain causal reasoning. Reserve for middle and later chapters of any unit.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 or 3 (Stretch or Transition Skill slot)**

```
Game Break 1 — Reinforcement (at current level)
    ↓
→ WHY CHAIN — Stretch (one level above current) ←
    ↓
Game Break 3 — Transition skill target
```

**Why this position:**
- Why Chain targets Bloom's Analyze — requires the student to have first encountered the content in Story Mode
- Should never be the first Game Break (student hasn't absorbed content yet)
- Works best as the "stretch" mechanic — after reinforcement builds confidence, the chain pushes deeper
- Not suitable as the final game before the Boss — the open-ended nature doesn't give the tight recall consolidation the Boss requires

---

# 3. PEER TEACHING

## What It Is
The student becomes the teacher. They are given a scenario involving a fictional younger student or confused classmate and must explain, help, or correct — in writing. The AI evaluates whether the explanation is complete, clear, and factually correct.

It is the only mechanic in the catalog where the student produces knowledge for someone else rather than retrieving it for themselves.

## How It Is Played

### Step-by-step flow
1. Scenario card appears with fictional student name and situation
2. Student reads the scenario and selects scenario type (A / B / C) — or AI pre-selects
3. Large text area opens for the student's explanation
4. Student writes their explanation (no word limit, no minimum displayed)
5. "Yuborish" (Submit) button
6. AI evaluates against rubric in real time (Tier 1 or Tier 2 depending on subject)
7. Score breakdown shown: Completeness / Clarity / Accuracy
8. If inaccurate: flagged for teacher review (not auto-failed)
9. Grade awarded based on rubric dimensions

### Three scenario types

| Type | Demand | Best for |
|---|---|---|
| **A — Explain from scratch** | Build understanding in someone with zero prior knowledge | Bloom's Understand |
| **B — Help someone stuck** | Diagnose confusion and re-explain with a different approach | Bloom's Apply |
| **C — Correct a wrong answer** | Identify the exact error and explain the correct path | Bloom's Evaluate |

### Scoring rubric

Grade: Type B (Rubric-Based) — Three dimensions tracked as percentages: Completeness (%), Clarity (%), Accuracy (%). Composite accuracy feeds the learning curve.

| Criterion | What AI checks |
|---|---|
| Completeness | All key concepts present — no critical gaps |
| Clarity | Language appropriate for the fictional audience |
| Accuracy | Factually correct against textbook content |

### AI evaluation behaviour
- Tier 1: keyword matching + logical flow check (Exact Sciences, straightforward topics)
- Tier 2: semantic evaluation (History, Literature, open-ended explanations)
- Flags for teacher review if factually inaccurate — does NOT auto-fail
- Never reveals the "correct" explanation to the student before they submit

### Availability
- Grades 5–11 only (below G5: developmental readiness insufficient for formulating explanations)
- All subject families (no subject restriction)

## Subject Implementations

### Exact Sciences
- A: "Explain to a Grade 4 student what a negative number means using a real example from daily life"
- A: "Explain why we can't divide by zero — use a story or example, not a definition"
- B: "Sardor keeps getting the wrong answer when multiplying fractions. Walk him through the correct method step by step"
- B: "Malika calculated speed as distance × time and got 240 km/h. She doesn't understand why this is wrong. Help her"
- C: "A student said 1/2 + 1/3 = 2/5. Explain exactly what error they made and what the correct answer is"
- C: "A student wrote: speed = distance + time. What is wrong and why?"

### Natural Sciences
- A: "Explain photosynthesis to a Grade 4 student without using the word 'photosynthesis'"
- A: "Explain why we have seasons — your classmate thinks it's because Earth gets closer to the Sun in summer"
- B: "Rustam drew his food chain as: Wolf → Rabbit → Grass. His teacher marked it wrong. He's confused. Help him"
- B: "Feruza thinks veins always carry deoxygenated blood. She found a website that says the same thing. Help her understand the full picture"
- C: "A student said 'arteries always carry oxygenated blood.' The teacher marked it wrong. Explain why"
- C: "A student said 'deserts are always hot.' Give three specific pieces of evidence that prove this wrong"

### Language Sciences
- A: "Explain the difference between past simple and past perfect to a student who has never heard of verb tenses"
- A: "Explain what a syllable is — use 5 words from today's lesson as examples"
- B: "Dilnoza keeps putting adjectives after nouns in English (e.g. 'a car red'). She can't understand why this is wrong. Help her"
- C: "A student wrote: 'Yesterday I go to school and buyed some food.' Identify and explain every error"

### Social Sciences / History
- A: "Explain to a Grade 4 student what a primary source is — give two examples from Uzbek history"
- B: "Temur thinks the Mongol invasion was purely destructive. He can't understand how the Timurid Renaissance happened so soon after. Help him"
- C: "A student answered: 'The Silk Road was only an economic phenomenon — it was just about trade.' The teacher gave 2/5. Explain what the answer is missing"

### Arts / Tarbiya
- A: "Explain what respect means in practice — give 3 specific examples, not a dictionary definition"
- C: "A student said 'being cooperative means always agreeing with the team.' Explain what is incomplete about this"

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 or 3 (Evaluate/Create slot)**

```
Game Break 1 — Reinforcement (Apply)
    ↓
Story Segment 2
    ↓
→ PEER TEACHING — Stretch (Evaluate) ←
    ↓
Story Segment 3 → Real-Life Challenge
```

**Why this position:**
- Peer Teaching requires the student to have absorbed content (cannot explain what they haven't encountered)
- Should come after at least one Story Segment and one reinforcement Game Break
- Naturally feeds into the Real-Life Challenge (Phase 4) — both require applying knowledge to an external context
- Not suitable as the final mechanic before the Boss — the open production format doesn't give tight consolidation

**Not recommended:**
- As the first Game Break (student hasn't encountered content yet)
- In Recovery Sessions (cognitive overhead too high for struggling students)
- For students below PISA L2 (scaffolding insufficient — use Adaptive Quiz instead)

---

# 4. REFLECTION JOURNAL

## What It Is
The metacognitive closure mechanic. After the Boss Fight and Remediation, the student is shown a prompt that asks them to look back at what happened in the session — what they understood, what confused them, and what they would do differently. They write a short response. No grading. No wrong answers.

It completes the TEFCAS loop: Trial → Event → Feedback → Check → Adjust → **Success** — the Reflection Journal is the conscious "Adjust" step, making the brain's natural error-correction process explicit.

## How It Is Played

### Step-by-step flow
1. Reflection prompt appears (AI-generated based on performance pattern)
2. Student reads the prompt
3. Text area opens — minimum 10 characters required (2 sentences in Extended Mode)
4. Student writes response — no time limit, no AI evaluation of content
5. "Tugatdim" (Finish) button
6. Response stored privately — student-only. Teacher sees themes only, not individual text.
7. Session closure screen

### Prompt types (AI selects based on performance)

| Performance pattern | Prompt type | Example |
|---|---|---|
| Strong session (2–3 stars) | Depth probe | "You understood today's topic well. What is the one thing that would help you explain it to a younger student?" |
| Weak session (0–1 star) | Growth frame | "You found today's topic difficult. Name one specific thing that confused you. What question would you ask the teacher?" |
| Inconsistent (good game breaks, poor boss) | Gap identification | "You did well on the practice games but struggled on the Boss. What was different about the Boss questions?" |
| First time on topic | Curiosity hook | "You just learned about [topic] for the first time. What surprised you most? What do you still want to know?" |
| Returning after failure | Re-engagement | "Last time you struggled with [standard]. Today you tried again. What felt different this time?" |

### Parameters
- No timer — student-paced
- No minimum quality threshold — any 10+ character response accepted
- No AI evaluation of content
- Privacy: content visible to student only. Teacher dashboard shows aggregate themes (e.g. "12 students mentioned confusion about denominators") — never individual entries
- Grade: Type D (Participation-Based) — No accuracy grade. Recorded as 'completed' or 'skipped.' No penalty for skipping.
- AI Tier: 1 for prompt generation (pre-pattern matching, not generative)

## Subject Implementations

### Exact Sciences
- After strong session: "Today you worked with fractions. Write one real situation from your life where you would need to add fractions"
- After weak session: "Which step in today's problem confused you the most? Draw it out in your mind and describe where you got lost"
- After inconsistent session: "You got the practice problems right but struggled on the Boss. What was different about the Boss question?"

### Natural Sciences
- After strong session: "You understood photosynthesis today. Describe it as if you were explaining it to a plant"
- After weak session: "Which part of the cell cycle confused you? What would help it make more sense?"
- Curiosity hook: "You just learned about the human immune system. What is one thing about it that surprised you?"

### Language Sciences
- After strong session: "You learned 8 new vocabulary words today. Which one will you actually use this week, and where?"
- After weak session: "Which grammar rule from today still feels unclear? Write it out in your own words — even if you're not sure it's right"

### Social Sciences / History
- After strong session: "Today you studied [historical event]. What would you have done differently if you were the decision-maker at the time?"
- After weak session: "What is one question about today's topic that the textbook didn't answer for you?"
- Curiosity hook: "You just learned about the Silk Road. What one thing about it do you want to know more about?"

### Arts / Tarbiya
- After any session: "What is one thing you did today that you feel proud of — inside or outside of your homework?"
- Character prompt: "You studied [character value] today. Describe one moment this week when you saw that value in real life — or when you wished you had shown it"

## Where It Fits in the Homework

**Position: Phase 8 — After Remediation, before Session Closure**

```
Phase 6 — Boss Fight
    ↓
Phase 7 — AI Analysis (server-side, invisible)
    ↓
Phase 8a — Remediation (targeted micro-exercises)
    ↓
→ REFLECTION JOURNAL ←
    ↓
Session Closure
```

**Why this position:**
- Must come after all assessment is complete — the student needs to know how they performed before they can reflect on it
- Must come before the reward sequence — the emotional closure of writing grounds the dopamine hit of the reward chest
- Cannot be moved earlier — reflecting before the Boss Fight creates test anxiety (student is thinking about what they got wrong, not fighting the Boss)

**Skippable:** Yes — Type D (Participation-Based). If the student taps "Skip" the session closes normally. Recorded as 'skipped' rather than 'completed.'

---

# 5. PUZZLE LOCK (SLIDING TILE)

## What It Is
A classic sliding tile puzzle (15-puzzle / 8-puzzle) where the ability to move tiles is gated by knowledge questions. Correct answer → student chooses which tile to slide. Wrong answer → a random adjacent tile slides automatically, potentially making the puzzle harder. The student must reach the solved state (tiles in correct order) before the timer expires.

## How It Is Played

### Step-by-step flow
1. Scrambled tile grid appears (3×3 = 8 tiles + 1 empty, or 4×4 = 15 tiles + 1 empty)
2. Student taps a tile adjacent to the empty space to attempt a move
3. Question modal appears immediately
4. Student answers the question
5. **Correct answer:** chosen tile slides into the empty space (student's intended move)
6. **Wrong answer:** a random valid adjacent tile slides instead (not necessarily the student's choice)
7. Repeat until solved or timer expires
8. Solved = all tiles in correct order → celebration
9. Time expired without solving = partial credit based on progress

### Tile content options
The tiles can contain:
- **Numbers** (default — solve the classic 1-2-3...8 order)
- **Vocabulary words** (arrange in alphabetical or grammatical order)
- **Historical events** (arrange in chronological order)
- **Equation steps** (arrange in logical solution order)
- **Sentence fragments** (arrange into a grammatically correct sentence)
- **Classification categories** (arrange organisms from simple to complex)

### Parameters
- Grid sizes: 3×3 (G1–6), 4×4 (G7+)
- Timer: 3 minutes (3×3), 5 minutes (4×4)
- Grade: Type A (Accuracy-Based) + Efficiency — Correct answers / total attempts = accuracy level. Fewer wrong answers = higher efficiency score.
- Questions: one per attempted move (not per wrong answer)
- AI Tier: 1 (pre-generated questions, rule-based evaluation)

### Wrong answer penalty psychology
The random tile slide creates a "punishment" that is strategic, not punitive — the puzzle becomes harder, but the student can still win. This is the same psychology as the Minefield Navigator: consequences are real but not catastrophic. The student is motivated to answer correctly to maintain control of their strategy.

## Subject Implementations

### Exact Sciences
- **Number tiles:** Arrange steps of long division in correct order
- **Equation tiles:** Arrange steps of solving 2x + 5 = 13 in sequence
- **Formula tiles:** Arrange: "Speed = Distance ÷ Time" — tiles show Speed / = / Distance / ÷ / Time scrambled
- Questions asked: arithmetic, formula recall, unit conversion

### Natural Sciences
- **Classification tiles:** Arrange taxonomy levels from broadest to narrowest: Kingdom → Phylum → Class → Order → Family → Genus → Species
- **Process tiles:** Arrange the stages of mitosis in order: Interphase → Prophase → Metaphase → Anaphase → Telophase
- **Food chain tiles:** Arrange organisms from producer to apex predator
- Questions asked: organism identification, process step functions, habitat facts

### Language Sciences
- **Sentence tiles:** Arrange scrambled words into correct grammatical order
- **Alphabet tiles:** Arrange vocabulary words in alphabetical order
- **Story tiles:** Arrange 8 sentence fragments to reconstruct a paragraph in logical order
- Questions asked: vocabulary definitions, grammar rules, spelling

### Social Sciences / History
- **Timeline tiles:** Arrange historical events in chronological order (dates on each tile)
- **Cause-effect tiles:** Arrange events from root cause to final consequence
- **Map tiles:** Arrange regions of Central Asia (image puzzle — tiles form a map)
- Questions asked: dates, key figures, event significance

### Arts / Tarbiya
- **Sequence tiles:** Arrange steps of a creative process (sketch → draft → refine → final)
- **Value tiles:** Arrange character values from most personal to most social
- Questions asked: vocabulary, creative concepts, reflection questions

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement slot)**

```
Story Segment 1 → Checkpoint 1
    ↓
Movement Break
    ↓
→ PUZZLE LOCK — Game Break 1 (Reinforcement) ←
```

**Also suitable:**
- Game Break 2 (Apply/Analyze) when using content-ordered tiles (timeline, classification sequence)
- Phase 5 Consolidation alternative to Memory Palace when the lesson involves a sequential process

**Why this position:**
- Puzzle Lock is a medium-overhead mechanic — visual/spatial, immediately engaging, lower cognitive demand than Why Chain
- Excellent as the first Game Break because it re-engages spatial reasoning after the narrative focus of Story Mode
- The "arrange in order" tile formats reinforce the structural understanding introduced in Story Mode without requiring the student to generate new knowledge

**Not recommended:**
- As the only Game Break in a session (needs to be complemented by a more evaluative mechanic)
- For abstract, non-sequential content that doesn't lend itself to ordering (use Tile Match instead)

---

# 6. TILE MATCH

## What It Is
A card-flipping memory-and-knowledge mechanic. The board contains face-down paired cards. The student flips two cards to attempt a match — but only gets to keep the match if they answer a subject question correctly. Wrong answer and the matched pair flips back.

## How It Is Played

### Step-by-step flow
1. 4×4 grid of face-down cards (8 pairs) appears
2. Student taps first card — it flips to reveal content
3. Student taps second card — it flips
4. If the two cards are a pair: question modal appears
5. **Correct answer:** both cards lock face-up (matched)
6. **Wrong answer:** both cards flip back face-down (pair lost)
7. If the two cards are not a pair: both flip back automatically (no question)
8. Repeat until all 8 pairs are matched
9. XP awarded based on total attempts needed

### Parameters
- Grid: 4×4 (8 pairs), all subjects
- XP: ≤8 attempts = 300 XP | ≤12 = 200 XP | 13+ = 100 XP
- Tile content: term/definition pairs, concept/example pairs, word/translation pairs
- No timer (concentration mechanic — student-paced)
- AI Tier: 1 (pre-generated questions)

### Wrong answer psychology
Unlike Puzzle Lock where wrong answers cause random moves, Tile Match wrong answers cause the pair to disappear from view again — requiring the student to relocate it spatially. This is a double penalty: knowledge penalty AND memory penalty.

## Subject Implementations

### Exact Sciences
- Pairs: formula ↔ name (e.g. "E = mc²" ↔ "Mass-Energiya tenglamasi")
- Pairs: number ↔ square root (e.g. "64" ↔ "8")

### Natural Sciences
- Pairs: organism ↔ classification (e.g. "Ko'rshapalak" ↔ "Sutemizuvchi")
- Pairs: organ ↔ function (e.g. "O'pka" ↔ "Nafas olish")

### Language Sciences
- Pairs: word ↔ translation or synonym
- Pairs: verb ↔ past tense form

### Social Sciences / History
- Pairs: event ↔ year (e.g. "O'zbekiston mustaqilligi" ↔ "1991")
- Pairs: figure ↔ achievement

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement)**

```
Story Segment 1 → Checkpoint 1
    ↓
Movement Break
    ↓
→ TILE MATCH — Game Break 1 (Reinforcement) ←
```

**Why this position:**
- Medium spatial + knowledge demand — ideal warm-up game break
- Reinforces vocabulary and paired concepts introduced in Story Mode
- Self-paced nature suits post-Movement Break state (students settle back in)

**Not recommended:**
- As a timed mechanic (defeats the concentration purpose)
- For abstract/procedural content that doesn't pair naturally

---

# 8. SPACED FLASHCARDS

## What It Is
A digital implementation of the spaced repetition method. The student is shown a card front (question/term), thinks privately, reveals the back (answer), then rates their confidence on a 4-point scale. Cards rated "Again" return to the queue; cards rated "Easy" exit the session. The mechanic simulates the Leitner box system without physical cards.

## How It Is Played

### Step-by-step flow
1. Card front shown: question or term
2. Student thinks (no timer — deliberate recall is the goal)
3. "Show Answer" button tapped → card flips to reveal back
4. Student self-assesses and taps one of four rating buttons:
   - **Again (Qayta):** did not recall — card returns to queue end (0 XP)
   - **Hard (Qiyin):** recalled with difficulty (+20 XP)
   - **Good (Yaxshi):** recalled correctly (+50 XP)
   - **Easy (Oson):** recalled instantly (+80 XP)
5. Next card loads from queue
6. Session ends when no "Again" cards remain
7. Session summary shown: Easy/Good/Again counts + total XP

### Parameters
- Cards per session: 8 (expandable)
- No time limit — student-paced throughout
- "Again" cards recycle to end of queue (not discarded)
- XP: 0 / 20 / 50 / 80 per card depending on rating
- AI Tier: 0 (no AI — pure self-assessment)
- Privacy: ratings stored for teacher analytics; content is not evaluated

### Spaced repetition logic
"Again" cards always re-appear before session end. "Hard" and "Good" cards exit the current session but return in future sessions at shorter intervals. "Easy" cards return at longer intervals. This mirrors the Leitner system and Ebbinghaus forgetting curve.

## Subject Implementations

### All subjects
The mechanic is subject-agnostic. Card fronts and backs are populated from the lesson's vocabulary and concept list:
- **Exact Sciences:** formula ↔ name, term ↔ definition
- **Natural Sciences:** organism ↔ classification, process ↔ steps
- **Language Sciences:** word ↔ translation, irregular verb ↔ past tense
- **History:** event ↔ date, figure ↔ role
- **Arts/Tarbiya:** value ↔ behavioural example

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

```
Session opens
    ↓
→ SPACED FLASHCARDS — Memory Hook ←
    ↓
Story Segment 1
```

**Why this position:**
- Activates prior knowledge before new content is introduced
- Sets retrieval context — Ebbinghaus shows recall before re-exposure strengthens retention
- Low-stakes (no wrong answer, just self-rating) — appropriate for session opening

**Also suitable:**
- Phase 5 Consolidation — reviewing lesson vocabulary after all content is covered
- Recovery sessions — low cognitive overhead, no time pressure

---

# 9. MEMORY SPRINT

## What It Is
A two-phase rapid-fire memory mechanic. Phase 1 (Study): 6 items are displayed simultaneously for exactly 5 seconds. Phase 2 (Recall): items are hidden and the student answers 6 questions about them under a 30-second timer. The faster the student answers, the more of the timer remains. The mechanic exploits the Primacy/Recency recall curve by forcing active retrieval immediately after study.

## How It Is Played

### Step-by-step flow
**Phase 1 — Study (5 seconds):**
1. 6 items appear in a 3×2 grid — each item has an emoji + label
2. A visible countdown runs from 5 to 0
3. At 0, all items disappear simultaneously

**Phase 2 — Recall (30 seconds):**
4. Question 1 of 6 appears — 4-option multiple choice
5. Student answers
6. Immediate feedback (correct/wrong) + next question loads
7. Timer keeps counting — questions can be answered at any speed
8. Session ends when all 6 questions answered or timer hits 0
9. XP awarded per correct answer

### Parameters
- Study duration: 5 seconds (fixed — not adjustable)
- Recall timer: 30 seconds
- Items: 6 per round
- XP: +50 per correct answer (300 XP max)
- AI Tier: 1 (pre-generated item/question sets)
- No partial credit — correct or wrong only

### Cognitive design
The 5-second study window is short enough to require genuine attention (students cannot read slowly — they must scan and encode visually). The immediate recall phase exploits the working memory window before items decay. This is distinct from Spaced Flashcards (which tests long-term memory) — Memory Sprint tests working memory and initial encoding.

## Subject Implementations

### Exact Sciences
- Items: formulas, geometric shapes, number sequences
- Questions: "Which formula appeared?", "What was the value shown?"

### Natural Sciences
- Items: organisms, organs, ecosystem elements
- Questions: "Which organism was NOT shown?", "What was the 3rd item?"

### Language Sciences
- Items: vocabulary words in target language
- Questions: translation recall, spelling recall

### History
- Items: key figures, dates, places
- Questions: "Which year was shown?", "Which figure appeared?"

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

```
Session opens
    ↓
→ MEMORY SPRINT — Memory Hook ←
    ↓
Story Segment 1
```

**Why this position:**
- Pre-loads relevant items into working memory before Story Mode introduces them formally
- Creates a "familiar" feeling when items reappear in Story Mode (recognition advantage)
- 35-second total duration — minimal time cost at session start

**Not recommended:**
- As a Game Break (too short and cognitively light for mid-session use)
- G1–2 (reading speed and working memory capacity insufficient for 5-second study window)

---

# 10. SENTENCE FILL (CLOZE TEST)

## What It Is
A structured gap-fill mechanic. The student is shown a sentence with one or more words missing (replaced by a blank). They select the correct word from 4 options. Unlike free-text input, the multiple-choice format ensures accessibility across grade levels and enables AI Tier 1 evaluation. The mechanic targets Bloom's Understand — testing whether the student can use context to identify the correct concept.

## How It Is Played

### Step-by-step flow
1. Sentence with blank(s) appears on screen
2. Subject tag shown (e.g. "🌿 Tabiiy Fanlar")
3. Optional hint shown below sentence
4. Student selects one of 4 options
5. **Correct:** blank fills with the word in green; +50 XP
6. **Wrong:** blank fills with student's wrong choice in red; correct answer highlighted green
7. Next sentence loads after 1.2 seconds
8. 6 sentences per session; session summary at end

### Parameters
- Questions per session: 6
- Options per question: 4
- XP: +50 per correct answer; +100 bonus if zero wrong answers
- Timer: none (student-paced)
- AI Tier: 1 (pre-generated sentences with controlled vocabulary)
- Subjects: all families

### Difficulty scaling

| Level | Blank type | Example |
|---|---|---|
| L1–2 | Single content word | "O'simliklar _____ yordamida oziq tayyorlaydi" |
| L3–4 | Technical term | "Atom tarkibida _____ va elektronlar bor" |
| L5+ | Multi-blank or clause | "_____ jarayonida CO₂ _____ ga aylanadi" |

## Subject Implementations

### Exact Sciences
- "Uchburchak barcha burchaklari yig'indisi _____ teng." → 180°
- "Tezlik = _____ ÷ Vaqt" → Masofa

### Natural Sciences
- "O'simliklar _____ va suv yordamida oziq-ovqat tayyorlaydi." → yorug'lik
- "Inson qoni _____ orqali tanaga kislorod yetkazadi." → gemoglobin

### Language Sciences
- Fill-in-the-blank grammar: "Yesterday I _____ to school." → went
- Vocabulary: "The opposite of 'hot' is _____." → cold

### History
- "Ipak Yo'li _____ dan Yevropagacha cho'zilgan." → Xitoy

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 or 2 (Reinforce/Apply)**

**Why this position:**
- Tests Bloom's Understand — verifies comprehension of Story Mode content
- Low UI friction (tap to answer) — suitable for both Game Break 1 and 2
- Works well as a "cooldown" game break between more complex mechanics

**Not recommended:**
- As the only mechanic in a session (pair with higher-order mechanic)
- For open-ended creative or evaluative content (use Peer Teaching instead)

---

# 11. TIC TAC TOE

## What It Is
Classic 3×3 Tic Tac Toe with knowledge gating. The student plays X, the AI plays O. Before each X placement, the student must answer a subject question. Correct answer → X placed on chosen cell. Wrong answer → AI immediately places O on a random empty cell (player's intended X does not appear). The student must get 3 X's in a row before the AI does.

## How It Is Played

### Step-by-step flow
1. Empty 3×3 board appears
2. Student taps any empty cell
3. Question modal appears
4. **Correct answer:** X placed on chosen cell
5. **Wrong answer:** AI places O on a random cell (not the student's chosen cell)
6. Check for win/loss/draw after each move
7. AI does NOT answer questions — AI moves happen automatically after wrong answers only
8. Game ends on 3-in-a-row for either player, or board full (draw)
9. Score tracked across multiple games in session

### Parameters
- Board: 3×3 standard
- Win condition: 3 in a row (horizontal, vertical, diagonal)
- XP: Win = 200 XP | Draw = 100 XP | Loss = 50 XP; +30 XP per correct answer regardless of outcome
- AI strategy: random empty cell (not minimax — keeps game winnable)
- Questions: 1 per student move attempt
- AI Tier: 1

### Game psychology
The AI randomness means the student can win even after wrong answers — the game is never unwinnable. Wrong answers increase risk (AI gets free moves) without guaranteeing loss. This maintains engagement without frustration.

## Subject Implementations

### All subjects
Questions are drawn from the current lesson's concept pool. The game board is thematically neutral — the knowledge gate is the only subject-specific element.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply)**

**Why this position:**
- Familiar format requires zero explanation — cognitive load is minimal
- Strategic element (cell placement) adds a layer above pure Q&A
- Short game duration (3–9 moves) fits the 2–3 minute Game Break window

**Not recommended:**
- As the first Game Break (needs student to be settled — the competitive element can create anxiety early in session)
- Recovery sessions (competitive framing not appropriate)

---

# 12. CONNECT FOUR

## What It Is
Classic 7×6 Connect Four with knowledge gating. The student plays yellow discs, the AI plays red. The student selects a column and must answer a question before their disc drops. Correct answer → yellow disc drops into chosen column. Wrong answer → AI drops a red disc into a random column. First to connect 4 in a row (horizontal, vertical, or diagonal) wins.

## How It Is Played

### Step-by-step flow
1. 7×6 empty grid appears with column arrow buttons at top
2. Student taps a column arrow
3. Question modal appears
4. **Correct answer:** yellow disc drops into chosen column (bottom-most empty row)
5. **Wrong answer:** AI drops red disc into a random valid column
6. After correct student move: AI automatically plays one move
7. Win check after every disc placement
8. Game ends on 4-in-a-row or board full (draw)

### Parameters
- Grid: 7 columns × 6 rows (standard)
- Win condition: 4 consecutive discs in any direction
- XP: Win = 200 XP | Draw = 80 XP | Loss = 50 XP; +30 XP per correct answer
- AI: random valid column (not strategic — keeps game learnable)
- Questions: 1 per student move attempt
- AI Tier: 1

### Depth vs Tic Tac Toe
Connect Four has 4,531,985,219,092 possible game states vs Tic Tac Toe's 255,168. The longer game duration (average 36 moves) makes it more suitable for a full Game Break slot. The vertical/diagonal win conditions add genuine strategic thinking beyond simple Q&A.

## Subject Implementations

### All subjects
Questions drawn from lesson concept pool. The board itself is thematically neutral.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply/Analyze)**

**Why this position:**
- Longer game = more questions answered per session
- Spatial strategy element engages different cognitive resources than pure recall
- Higher replay motivation than Tic Tac Toe (more varied outcomes)

**Not recommended:**
- Game Break 1 (too complex for a first Game Break — student needs to be warmed up)
- G1–3 (Connect Four strategy requires abstract spatial planning)

---


# 14. MEMORY PALACE

## What It Is
A digital implementation of the Method of Loci (memory palace technique). A virtual room is divided into 6 named zones (e.g. Entrance, Window, Wall, Desk, Chair, Bookshelf). Each zone is assigned a knowledge item (emoji + label). The student studies the zone-item assignments, then the items are hidden and the student must tap the correct zone for each item presented.

## How It Is Played

### Step-by-step flow
**Phase 1 — Study (10 seconds):**
1. Room grid appears with all 6 items visible in their zones
2. Countdown timer from 10 to 0
3. At 0, items disappear

**Phase 2 — Recall:**
4. One item is presented at a time (emoji + name): "Where was this?"
5. Student taps the zone they believe the item was placed in
6. **Correct:** zone highlights green
7. **Wrong:** chosen zone highlights red; correct zone highlights green
8. Next item presented until all 6 recalled
9. XP awarded per correct recall

### Parameters
- Zones: 6 (named locations in a room)
- Study duration: 10 seconds
- Recall: untimed (self-paced)
- XP: +50 per correct zone; bonus for perfect recall
- AI Tier: 0 (no AI evaluation — correct answer is deterministic zone matching)

### Pedagogical basis
The Method of Loci exploits the brain's strong spatial memory by anchoring abstract content to familiar physical locations. Research (Bower, 1970; Yates, 1966) shows 2–3× better recall for loci-encoded material vs rote memorisation. In this mechanic, the "palace" is always the same room — familiarity with the palace grows over repeated sessions.

## Subject Implementations

### All subjects
The zone-item assignments are generated from the lesson's key concept list:
- **Natural Sciences:** photosynthesis steps → room zones
- **History:** Silk Road cities → room zones
- **Exact Sciences:** formula components → room zones
- **Language Sciences:** vocabulary clusters → room zones

## Where It Fits in the Homework

**Primary position: Phase 5 — Mustahkamlash (Consolidation)**

**Also suitable:**
- As alternative in consolidation slot (when content is list-based rather than vocabulary-based)

**Why this position:**
- Consolidation requires organising disparate items into a coherent structure — exactly what the palace provides
- Students have seen all items in Story Mode and Game Breaks; the palace re-organises them spatially
- The 10-second study window forces rapid scanning — mimics how expert memorisers encode

**Not recommended:**
- Phase 1 (student hasn't encountered items yet — nothing to anchor to zones)
- For procedural/sequential content (Puzzle Lock is better for ordered sequences)

---

# 15. STORY MODE

## What It Is
The narrative backbone of each homework session. Story Mode presents lesson content as a story with a protagonist, setting, and plot — not as a textbook explanation. Content is delivered in 3 segments of ~90 seconds each. Between segments, a Checkpoint question verifies comprehension before the story continues. The student is a passive reader/listener during segments and an active responder at checkpoints.

## How It Is Played

### Step-by-step flow
1. Scene card appears: icon + chapter label + narrative text (90 seconds reading time estimate)
2. "Davom etish" (Continue) button advances to next segment or checkpoint
3. At each checkpoint: question modal appears (no "Continue" button — question must be answered)
4. **Correct answer:** +80 XP, story continues
5. **Wrong answer:** 0 XP, story still continues (checkpoints are not blockers — they are measurement points)
6. After Segment 3: session summary + total XP
7. Story complete → transition to Game Breaks

### Segment structure

| Segment | Content | Bloom's level |
|---|---|---|
| 1 — Introduction | Hook + context + key concept introduced | Remember |
| Checkpoint 1 | Surface recall question | Remember/Understand |
| 2 — Mechanism | How/why the concept works | Understand |
| Checkpoint 2 | Comprehension question | Understand |
| 3 — Application | Real-world examples + connection to prior knowledge | Apply |
| Checkpoint 3 | Application question | Apply |

### Parameters
- Segments: 3 (expandable to 4 for complex topics)
- Checkpoints: 3 (one after each segment)
- XP: +80 per checkpoint correct answer (240 XP max from Story Mode)
- Checkpoints are non-blocking — wrong answer does not replay the segment
- AI Tier: 1 for checkpoints; Tier 2 for AI-generated narrative personalisation (future)
- Language: Uzbek (primary), Russian/English support planned

## Subject Implementations

### Natural Sciences — Photosynthesis
- S1: "Every morning the sun rises and plants wake up. For them, sunlight is not just light — it is energy..."
- CP1: "What energy source does photosynthesis use?"
- S2: "The leaf takes 3 things: light, water, CO₂. These combine to make sugar and oxygen..."
- CP2: "What does photosynthesis produce?"
- S3: "The green pigment chlorophyll captures light energy. Without leaves there is no photosynthesis..."
- CP3: "Which pigment plays the key role in photosynthesis?"

### History — Silk Road
- S1: "Centuries ago, camel caravans crossed the desert between China and Europe..."
- S2: "Cities like Samarkand grew not just because of trade, but because of what traveled alongside goods..."
- S3: "The Silk Road was not just an economic route — it was a channel for ideas, religions, and languages..."

## Where It Fits in the Homework

**Position: Phase 2 — Hikoya (the only mechanic in this phase)**

```
Phase 1 — Memory Hook (Spaced Flashcards / Memory Sprint)
    ↓
→ STORY MODE — Phase 2 (all 3 segments + checkpoints) ←
    ↓
Phase 3 — Game Breaks
```

**Mandatory phase:** Story Mode cannot be skipped. All subsequent game mechanics assume the student has been exposed to the content through Story Mode. Without Story Mode, Why Chain and Peer Teaching have no knowledge base to operate on.

---

# 16. ADAPTIVE QUIZ

## What It Is
A 10-question multiple-choice quiz where difficulty adjusts in real time based on student performance. Starting at Level 1 (L1), each correct answer raises difficulty by 1 level after 2 consecutive correct answers; each wrong answer drops difficulty by 1 level. The quiz ends after 10 questions. Final PISA level estimate and XP are based on the highest sustained difficulty level reached.

## How It Is Played

### Step-by-step flow
1. Question 1 appears at difficulty Level 1
2. Student selects one of 4 options
3. Immediate feedback shown (correct/wrong)
4. Difficulty adjusts for next question (up after 2 consecutive correct, down after any wrong)
5. Streak counter resets on any wrong answer
6. Repeat for 10 questions
7. Session summary: correct count, final level, XP earned

### Difficulty levels

| Level | PISA Equivalent | Question type |
|---|---|---|
| L1 | Below L2 | Direct recall, simple arithmetic |
| L2 | L2–L3 | Single-step reasoning, basic application |
| L3 | L3–L4 | Multi-step, concept connection |
| L4 | L4–L5 | Analysis, cause-effect reasoning |
| L5 | L5–L6 | Synthesis, evaluation, edge cases |

### Scoring
- XP per question: Level × 30 (L1 = 30 XP, L5 = 150 XP)
- Bonus: 3+ consecutive correct at L4–L5 = streak multiplier ×2
- Total XP range: 300 (all L1 correct) to ~1,200 (all L5 correct)

### Parameters
- Questions: 10 fixed
- Difficulty range: L1–L5 (5 levels)
- Escalation: +1 level after 2 consecutive correct
- De-escalation: −1 level after any wrong
- AI Tier: 1 (pre-banked question pool per level per subject)

## Subject Implementations

### All subjects
Each subject has a question bank organised by the 5 difficulty levels. Questions at L1 test vocabulary and surface recall; questions at L5 test analysis and synthesis.

## Where It Fits in the Homework

**Primary position: Phase 6 — Boss Fight**

```
Phase 5 — Consolidation
    ↓
→ ADAPTIVE QUIZ — Boss Fight ←
    ↓
Phase 7 — AI Analysis
    ↓
Phase 8 — Remediation
```

**Why the Boss position:**
- The Boss Fight must assess the full range of student ability — fixed-difficulty quizzes miss both very weak and very strong students
- Adaptive difficulty ensures every student is challenged appropriately
- The 10-question structure provides sufficient data for the post-session AI analysis
- Rising difficulty creates emotional arc: students feel the quiz "getting harder" as they succeed

**Not recommended:**
- As a Game Break (Boss position is its design purpose — using it earlier undermines the Boss Fight significance)
- Without the full question bank populated per subject (thin bank = repeated questions within session)

---

# 17. MYSTERY BOX

## What It Is
A surprise-reward mechanic built around knowledge gating. A 3×3 grid of 9 mystery boxes is presented — each concealing a different reward (large XP, medium XP, small XP, penalty, or empty). The student selects a box, answers a question, and if correct the box opens to reveal its contents. Wrong answer triggers a small XP penalty but the box still opens (revealing the prize regardless — the question is the gate, not the reveal).

## How It Is Played

### Step-by-step flow
1. 3×3 grid of identical mystery boxes (contents unknown)
2. Student taps any box
3. Question modal appears
4. **Correct answer:** box opens to reveal prize; full XP awarded
5. **Wrong answer:** −30 XP penalty; box opens anyway (student still sees what was inside)
6. Repeat until all 9 boxes opened
7. Session summary: big prizes / medium prizes / penalty count / total XP

### Prize distribution (fixed per session, randomised placement)
| Prize type | Count | XP value |
|---|---|---|
| Large prize (🏆) | 1 | +300 XP |
| Medium prize (⭐) | 3 | +150 XP each |
| Small prize (💫) | 3 | +80 XP each |
| Penalty (💀) | 1 | −30 XP |
| Empty (📭) | 1 | 0 XP |

### Parameters
- Grid: 3×3 (9 boxes)
- Prize placement: randomised each session
- Wrong answer cost: −30 XP (does not affect box reveal)
- AI Tier: 1
- All subjects

### Psychological design
The box-opening reveal creates genuine anticipation — students do not know which box has the large prize. This variable reward schedule (Skinner, 1938) is among the most powerful engagement drivers in game design. The knowledge gate ensures XP is earned, not just discovered. The penalty box creates mild risk-aversion without catastrophic consequences.

## Subject Implementations

Questions are drawn from the lesson concept pool — identical format to other Game Break mechanics. The Mystery Box shell is subject-agnostic; only the questions change per lesson.

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 1 (Reinforcement)**

**Why this position:**
- High novelty and engagement — ideal for the first Game Break where motivation is most critical
- Low cognitive overhead (standard MCQ) allows focus on the surprise element
- Short per-box interaction (tap + answer + reveal) maintains pace

**Also suitable:**
- As a bonus mechanic after completing other Game Breaks (reward feel)

**Not recommended:**
- As the only mechanic in a session (no depth beyond surprise; needs a higher-order mechanic alongside it)
- Boss Fight position (lacks the assessment rigor required there)

---

# 18. MEMORY MATCH BLITZ

## What It Is
An accelerated variant of Tile Match with a critical addition: all cards are briefly revealed at the start of the game. Before the timer begins, all 16 cards are shown face-up for exactly 3 seconds — then hidden simultaneously. The student then has 60 seconds to find all 8 pairs from memory alone. No question gating — pure speed and spatial memory.

## How It Is Played

### Step-by-step flow
1. Empty 4×4 board displayed
2. "Boshlash" (Start) tapped
3. **Peek phase:** all 16 cards flip face-up simultaneously — 3 second countdown
4. At 0: all cards flip back face-down — timer starts at 60 seconds
5. Student taps two cards to flip them
6. **Match:** both cards lock face-up (+40 XP)
7. **No match:** both flip back face-down after 0.7 seconds
8. Game ends when all 8 pairs matched OR timer reaches 0
9. Final XP: matched pairs × 40, minus wrong flips × 5

### Parameters
- Grid: 4×4 (8 pairs)
- Peek duration: 3 seconds (fixed)
- Game timer: 60 seconds
- XP: +40 per matched pair; −5 per wrong flip attempt; speed bonus if all 8 matched with >20 seconds remaining
- No question gating (pure memory — no knowledge questions)
- AI Tier: 0

### Difference from Tile Match

| Feature | Tile Match | Memory Match Blitz |
|---|---|---|
| Knowledge gate | ✅ Question per match | ❌ No questions |
| Preview | ❌ No preview | ✅ 3-second preview |
| Timer | ❌ Untimed | ✅ 60 seconds |
| Bloom's level | Remember + Apply | Remember (pure) |
| Phase placement | Game Break 1 | Memory Hook (Phase 1) |

## Where It Fits in the Homework

**Primary position: Phase 1 — Xotira (Memory Hook)**

**Why this position:**
- The 3-second preview pre-loads visual items into working memory before lesson content arrives
- No question gate = no knowledge required = appropriate before content is taught
- 60-second duration fits the Memory Hook time budget

**Not recommended:**
- As a Game Break (no knowledge gate = no content reinforcement)
- G1–2 (3-second encoding window too fast for early readers)

---

# 19. REACTION CHAIN

## What It Is
A rapid categorisation mechanic. Items (emoji + name) appear one at a time and the student must tap the correct category bucket to sort them. The faster and more accurately they sort, the longer their "chain" grows. Correct sorts extend the chain and increase the XP multiplier; any wrong sort breaks the chain and resets the multiplier to ×1. The session runs for 90 seconds.

## How It Is Played

### Step-by-step flow
1. 4 category buckets displayed (e.g. Living / Non-living / Natural / Man-made)
2. Timer starts: 90 seconds
3. Item appears in centre: emoji + name + hint question
4. Student taps the correct bucket
5. **Correct:** item counted in bucket; chain length +1; chain display updates
6. **Wrong:** chain resets to 0; chain display clears
7. Next item appears immediately (no delay)
8. Session ends when timer reaches 0
9. Final XP: correct × 30, with chain multiplier (×2 at chain ≥3)

### Chain mechanics

| Chain length | XP multiplier |
|---|---|
| 1–2 | ×1 (30 XP per item) |
| 3–5 | ×2 (60 XP per item) |
| 6–9 | ×2 + combo banner |
| 10+ | ×3 (90 XP per item) |

### Parameters
- Timer: 90 seconds
- Categories: 4 (subject-specific per lesson)
- XP: base 30 per correct, multiplied by chain
- No question modal — answer IS the bucket tap (instant feedback)
- AI Tier: 0 (rule-based categorisation, no generative AI)

## Subject Implementations

### Natural Sciences
- Categories: Tirik (Living) / Jonsiz (Non-living) / Tabiiy (Natural) / Insoniy (Man-made)
- Items: animals, minerals, rivers, machines

### Exact Sciences
- Categories: Kasrlar / Butun sonlar / Geometrik shakllar / Algebraik ifodalar
- Items: mathematical expressions sorted by type

### Language Sciences
- Categories: Noun / Verb / Adjective / Adverb
- Items: words to be classified by part of speech

### History
- Categories: Qadimgi davr / O'rta asrlar / Yangi davr / Zamonaviy davr
- Items: historical events sorted by period

## Where It Fits in the Homework

**Primary position: Phase 3 — Game Break 2 (Apply)**

**Why this position:**
- Bloom's Apply — student must know categories well enough to sort instantly
- The 90-second duration and rapid-fire pace suit the mid-session energy peak
- Chain mechanic creates natural excitement arc in the middle of the session

**Not recommended:**
- Phase 1 (student hasn't learned the categories yet)
- For nuanced content where categorisation is ambiguous (use Sentence Fill instead)

---

# 20. WORD LADDER CLIMB

## What It Is
A word transformation puzzle where the student changes one letter at a time to transform a start word into a target word — each intermediate step must be a valid word. Before each letter change is accepted, the student must answer a subject question. Correct answer → change applied, rung added to the ladder. Wrong answer → change rejected, student tries again. The visual ladder grows upward as the student climbs toward the target.

## How It Is Played

### Step-by-step flow
1. Start word shown at bottom of ladder; target word shown at top
2. Student taps a letter in the current word to select it
3. Student taps a replacement letter from the on-screen alphabet
4. "Qo'llash" (Apply) button confirms the change
5. If the proposed word is not on the valid path: rejected immediately (no question asked)
6. If the proposed word is valid: question modal appears
7. **Correct answer:** new word appears as the next rung on the ladder (+60 XP)
8. **Wrong answer:** change rejected, student must re-attempt (+0 XP, wrong counter +1)
9. Repeat until target word reached
10. Bonus +100 XP for zero wrong answers

### Ladder display
- Each completed rung shows the word with the changed letter underlined/highlighted
- Target rung shown in blue throughout (constant visual goal)
- Current word shown in amber (active position)
- Completed rungs shown in green

### Parameters
- Word length: 3–4 letters (expandable to 5 for G7+)
- Ladder depth: 3–5 steps depending on puzzle
- XP: +60 per valid step + 100 bonus for clean run
- No timer (strategic puzzle — student-paced)
- AI Tier: 1 (pre-constructed valid paths)
- Subject: Language Sciences primary; all subjects for abbreviation-based variants

## Subject Implementations

### Language Sciences (Primary)
- CAT → COT → COG → DOG (English vocabulary)
- HOT → HOD → COD (3-step)
- COLD → CORD → WORD → WARD → WARM (5-step)

### All subjects (Abbreviation variant)
- ATOM → ATOP → STOP → STEP (science abbreviations as waypoints)
- Questions at each step test the meaning of the word/abbreviation being changed to

## Where It Fits in the Homework

**Primary position: Phase 5 — Mustahkamlash (Consolidation)**

**Why this position:**
- Requires deliberate letter-level attention — deepens vocabulary encoding after surface exposure
- Strategic puzzle nature suits the consolidation phase (student has time to think, not racing)
- The visual ladder provides clear progress metaphor aligned with the session's "climb" narrative

**Also suitable:**
- Language Sciences sessions as a Phase 3 Game Break (vocabulary focus)

**Not recommended:**
- Phase 1 (vocabulary hasn't been taught yet)
- Non-language subjects as primary (letter manipulation has weak connection to most content areas)
- Recovery sessions (puzzle complexity too high for struggling students)
