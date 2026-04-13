# Buzan Method Integration into NETS Homework Engine

Each entry: **What** (the method) → **Why** (what it improves) → **How** (concrete implementation) → **Where Not** (where it's unnecessary or harmful).

---

## Phase-Level Injections

### 1. TEFCAS Learning Loop
- **What:** Trial → Event → Feedback → Check → Adjust → Success. Buzan's model of how the brain acquires skills through cybernetic feedback. *(Source: Buzan, Scientific Research — The TEFCAS Model)*
- **Why:** The NETS session already follows this loop but doesn't name it. Naming it gives the AI tutor a consistent vocabulary and reframes all failure as "Feedback, not failure."
- **How:** 
  - All wrong-answer responses across ALL phases use **"Hali emas!"** (Not yet!) — the words "Wrong," "Incorrect," "Noto'g'ri," "Xato" are banned system-wide.
  - Phase 6 Socratic tutoring follows C→A→S: "Let's **Check** where the gap is → How would you **Adjust**? → Try again for **Success**."
  - Phase 7 reflection prompts use TEFCAS: "What **Feedback** did your brain receive? What will you **Adjust** next time?"
- **Where Not:** The raw performance data (correct count, XP, time) stays as numbers — TEFCAS language applies to student-facing prompts only, not analytics dashboards or teacher reports.

### 2. MIG — Most Important Graph (Primacy, Recency, Von Restorff, the Sag)
- **What:** Recall is highest at the start (Primacy) and end (Recency) of a session, dips in the middle (the Sag), and spikes on outstanding/unusual items (Von Restorff). *(Source: Buzan, Use Your Memory — The MIG)*
- **Why:** Explains why the 7-phase structure works. Makes phase ordering intentional rather than arbitrary.
- **How:**
  - **Phase 1 (Memory Sprint)** = Primacy window. Most important prior-knowledge items go here.
  - **Phase 3, Game Break 2 (middle game)** = Sag position. Tag this game as the **Von Restorff Anchor** — preferentially select content items tagged `outstanding: true` (surprising facts, humorous framing, unusual visuals). Content authors must tag at least 3 items per lesson as outstanding.
  - **Phase 7 (Reflection)** = Recency window. The last mental act consolidates learning.
- **Where Not:** Does not change Phase 2 (Story Mode) or Phase 4 (Real-Life Challenge) — those are content delivery phases, not recall-curve phases.

### 3. BOST — Buzan Organic Study Technique
- **What:** Browse → Time → Prime → Questions → Overview → Preview → Inview → Review. *(Source: Buzan, Use Your Head — BOST)*
- **Why:** The NETS session already maps to BOST at ~80%. Two small additions close the gap and complete the study cycle.
- **How:**
  - **Phase 0-A Panel 5** adds a Prior Knowledge prompt: *"Bu mavzu haqida nimalarni bilasiz?"* (What do you already know?). Student taps 2-3 keywords. This is the BOST "Prime" step — activates existing schemas. Stored for Phase 7.
  - **Phase 0-A Panel 6** adds a Learning Goal prompt: *"Bugun nimani bilmoqchisiz?"* (What do you want to learn?). Stored and resurfaced in Phase 7: *"You wanted to learn X. Did you?"*
- **Where Not:** Recovery Sessions (15-20 min, no time for prompts). First-ever lesson in a brand new subject (nothing to "already know").

### 4. Buzan Review Intervals
- **What:** Mandatory review at 10min → 24h → 1 week → 1 month after initial learning. *(Source: Buzan, Use Your Memory — Review Intervals)*
- **Why:** SM-2 may schedule reviews too late for "Easy" rated items. Buzan's intervals catch the steepest part of the forgetting curve.
- **How:** Add floor constraints to the Memory Sprint item selection algorithm: `actual_next_review = min(SM-2_schedule, Buzan_mandatory)` — whichever is sooner wins. The ~10min touchpoint is Phase 5 of the same session. The ~24h touchpoint injects into next day's Phase 1. If a student misses a session, the touchpoint shifts to the next available session — never skipped.
- **Where Not:** Does not override SM-2 when SM-2 schedules SOONER (e.g., student rated "Again"). Buzan intervals are a floor, not a ceiling.

### 5. 80/20 Keyword Extraction
- **What:** ~20% of words carry ~80% of a text's conceptual value. *(Source: Buzan, Speed Reading — The 80/20 Rule)*
- **Why:** Tagging keywords creates a shared resource used by Radiant Summary (branch labels), Flash Cards (card fronts), Memory Sprint (recall items), and Sentence Fill (blanked words).
- **How:** Content pipeline requirement: every `narrative_segment` must have a `keywords_80_20` array (3-8 keywords). Automated QA blocks segments with missing arrays.
- **Where Not:** Only for `narrative_segment` blocks. Game items, boss questions, and checkpoints are already keyword-dense by nature — no extraction needed.

### 6. Cortical Skills Synergy
- **What:** When left-brain (logic, words) and right-brain (imagery, spatial) skills work together, performance increases exponentially. *(Source: Buzan, Use Your Head — Cortical Skills)*
- **Why:** Without a constraint, the Phase 3 game selection algorithm could pick 3 verbal games — all left-brain, zero visual/spatial engagement.
- **How:** Tag each game mechanic with a cortical modality (Verbal/Logical, Visual/Spatial, Kinesthetic, Strategic, Productive). Add selection constraint: at least 2 of the 3 games per session must come from DIFFERENT modalities.
- **Where Not:** Recovery Sessions (only 1-2 games — diversity constraint would over-restrict).

### 7. Schema Activation
- **What:** New information anchors better when it connects to knowledge already active in working memory. *(Source: Buzan, Scientific Research — Schema Theory)*
- **Why:** If Phase 2 introduces "photosynthesis" but Phase 1 didn't activate any prerequisite (e.g., "plants," "sunlight"), the new concept floats unanchored.
- **How:** Session Assembler check: every new concept in Phase 2 must have at least 1 prerequisite activated in Phase 1 or Phase 0-B. If missing, auto-inject a prerequisite recall item into Memory Sprint.
- **Where Not:** First lesson in a subject where no prerequisites exist yet.

### 8. W5H Radiant Problem Solving
- **What:** Radiate Who/What/Where/When/Why/How from a central problem to see the whole picture before answering. *(Source: Buzan, Mind Map Book — Problem Solving)*
- **Why:** Students jump to answers without analyzing all factors. The W5H frame forces structured decomposition.
- **How:** Phase 4 (Real-Life Challenge): before the answer area opens, a 6-branch W5H frame appears. Student fills at least 4 of 6 branches with brief notes. Frame stays visible as sidebar while answering. NOT scored — it's scaffolding.
  - G5-6: mandatory, 4/6 minimum
  - G7-8: default ON, toggleable off, 5/6
  - G9+: available via button, not forced
- **Where Not:** Math-only computational challenges (pure calculation doesn't decompose into W5H). Tasviriy Sanat (creative challenges). Language comprehension tasks.

### 9. Decision Mapping
- **What:** Compare two competing options radiantly with weighted pros/cons. *(Source: Buzan, Mind Map Book — Decision Mapping)*
- **Why:** Linear pros/cons lists hide trade-offs. Radiant comparison makes them visible.
- **How:** Phase 4 (Real-Life Challenge) extension of W5H — for scenarios with genuine trade-offs between 2+ options. Two options radiate from the problem, each with pro/con sub-branches. Student completes missing branches, assigns weights (1-5), selects choice, writes justification.
- **Where Not:** Phase 6 Boss (assessment gate — scaffolding doesn't belong in assessment). Math (has correct answers, not trade-offs). Language (no decision trade-offs). Scenarios with a single correct answer (use W5H alone).

---

## Phase 5 Consolidation — Technique-by-Content-Structure

Phase 5 is Buzan's home phase. The technique is selected based on content structure, not randomly.

### 10. Radiant Summary (Mind Mapping)
- **What:** Partially completed mind map — student drags keywords onto correct branches. Central image, organic curved branches, one keyword per branch, 3+ colors. *(Source: Buzan, Mind Map Book — Radiant Thinking + 7 Laws)*
- **Why:** Hierarchical content (classifications, categories) is best encoded as a visual hierarchy. Fills the undefined "Mind maps" slot in Phase 5.
- **How:** Content author provides central image, 3-5 BOI branch labels, empty sub-branch slots, and 2-3 distractor keywords. Student drags correct keywords to correct branches. G5: max 4 branches (WM ceiling), Icon-First (image before text), landscape orientation. Optional Supernova Sprint: 30-sec timed association burst from one keyword after map completion.
- **Where Not:** Sequential content (use Link System). Spatial content (use Memory Palace). Discrete unrelated facts (use Peg System). History timelines (temporal, not hierarchical).
- **Best for:** Science classification (Kingdom Animalia), Math formula families, Tarbiya virtue categories, Geography biome types, Art elements.

### 11. Link System
- **What:** A vivid story chain where each item triggers the next. *(Source: Buzan, Use Your Memory — Link System)*
- **Why:** Sequential content (process steps, timelines) is best encoded as a chain — each item triggers recall of the next.
- **How:** Available in two places:
  - **Phase 1 (Memory Sprint)** as "Link Chain" format: 5 items with a SMASHIN' SCOPE story, 15s study, recall tested out of order.
  - **Phase 5 (Consolidation)** as a technique for sequential content.
  - Content author writes the chain story using the textbook's actual terms (never substitutes).
- **Where Not:** Unrelated vocabulary (no natural chain — use Peg System). Math formulas (not sequential narrative). Hierarchical content (use Radiant Summary).
- **Best for:** Science processes (water cycle, digestion), History timelines, cause-effect chains.

### 12. Peg System
- **What:** Number-Shape pegs (1=Candle, 2=Swan, 3=Heart, 4=Sailboat, 5=Hook) as permanent mental hooks for lesson concepts. *(Source: Buzan, Use Your Memory — Peg System)*
- **Why:** Gives random-access to numbered items (unlike Link System which is sequential). Fills the undefined "Peg system" slot in Phase 5.
- **How:** Student associates each lesson concept with a numbered peg image, aided by a "link sentence" connecting them. Recall tested both directions: peg→concept and concept→peg. Culturally adapted for Uzbekistan (shapes chosen to be universally recognizable). Can integrate with Tic Tac Toe: to place X on cell 3, recall the concept pegged to number 3.
- **Where Not:** Sequential processes (use Link System). Hierarchical categories (use Radiant Summary). Content with more than 5-7 items per lesson (peg overload).
- **Best for:** History key facts (5 Silk Road facts), Language vocabulary sets, Science key terms per chapter.

### 13. Major System (G7+ only)
- **What:** Phonetic digit code: 1=T, 2=N, 3=M, 4=R... Digits convert to consonants, then to a memorable word. *(Source: Buzan, Use Your Memory — Major System)*
- **Why:** Only mnemonic that works for raw numbers (dates, constants, statistical data).
- **How:** System presents a number (e.g., 1441 — Navoi's birth year), shows consonant conversion (T-R-R-T), suggests a memorable word ("Toshbaqa" = Turtle), pairs it with a vivid image. Student confirms or creates their own word.
- **Where Not:** G5-6 (abstract phonetic mapping exceeds developmental stage). Tarbiya (no numbers). Tasviriy Sanat (no numbers). Any subject where numbers aren't central to the content.
- **Best for:** History dates, Chemistry constants, Physics constants, Math (Pi digits).

### 14. SMASHIN' SCOPE Quality Gate
- **What:** 12-point vividness checklist for mnemonic content: Synaesthesia, Movement, Association, Substitution, Humor, Imagination, Number, Symbolism, Color, Order, Positive, Exaggeration. *(Source: Buzan, Use Your Memory — SMASHIN' SCOPE)*
- **Why:** Dry mnemonics perform no better than rote memorization. Vivid, multi-sensory imagery is what makes mnemonics work.
- **How:** Every `mnemonic_exercise` in the content pipeline must score 6+/12. Below 6 = returned for enrichment with specific criteria flagged. Content reviewer scores each criterion 0 or 1.
- **Where Not:** Non-mnemonic content (quizzes, boss questions, checkpoints, game items). Only applies to Memory Palace scenes, Peg associations, Link Chain stories, and Radiant Summary content.

### 15. Dual Coding
- **What:** Combining verbal + visual (or verbal + spatial, or visual + kinesthetic) encoding creates two retrieval paths. *(Source: Buzan, Scientific Research — Dual Coding Theory / Paivio)*
- **Why:** Doubles the chance of recall. Phase 5 IS the Dual Coding moment — concepts learned verbally in Phase 2 get re-encoded visually/spatially here.
- **How:** Pipeline QA gate: every `game_item`, `mnemonic_exercise`, and `boss_question` must declare 2+ encoding channels (VRB, VIS, SPA, AUD, KIN). Items with only 1 channel are flagged.
- **Where Not:** Movement Breaks (physical activity, not knowledge encoding).

---

## Game-Level Injections

### Tile Match
- **Method applied:** #15 Dual Coding
- **Why:** Tile Match is a pairing game — the student flips two cards to find a match. If both cards are text ("Fotosintez" ↔ "O'simliklar oziq tayyorlash jarayoni"), the brain uses only ONE encoding channel (verbal). If one card is an image and one is text (leaf diagram ↔ "Fotosintez"), the brain encodes through TWO channels (visual + verbal). Paivio's Dual Coding Theory shows this doubles recall probability. The game already requires pairs — making them cross-modal costs nothing and doubles the learning.
- **How:** Pairs must be image↔text (not text↔text). Content authors should always pair a visual representation with a textual term.
- **Where Not:** Already applies by default when content is well-authored. Only flag pairs where both sides are text-only.

### Why Chain
- **Method applied:** #1 Radiant Thinking
- **Why:** Why Chain IS radiant thinking — each "Why?" answer branches one level deeper from the surface toward the root cause. But the current UI renders it as a flat numbered list (L1, L2, L3...), which makes it look linear and hides the branching structure. Showing it as a growing tree reinforces that knowledge radiates outward from a central concept — the student literally SEES their understanding deepen.
- **How:** Visualize the chain as a downward radiant branch on screen, not a flat numbered list. Each level shows as a new branch growing from the previous answer.
- **Where Not:** The mechanic itself doesn't change. Only the VISUAL RENDERING changes from a flat list to a branching tree. Don't force radiant visualization for 2-level chains (too short to branch meaningfully).

### Sentence Fill
- **Method applied:** #5 80/20 Rule
- **Why:** Sentence Fill blanks a word and tests if the student can identify it from context. If you blank a random word ("O'simliklar _____ yordamida oziq tayyorlaydi" → "yorug'lik"), you test recall of one fact. But if you ALWAYS blank the 80/20 keyword — the word carrying the most meaning in that sentence — you train the student to identify the conceptual anchor of every sentence. Over time, this builds the habit of reading for meaning, not just reading words.
- **How:** The blanked words should BE the `keywords_80_20` from the narrative segment — the words carrying 80% of meaning. Not random words, not articles or prepositions.
- **Where Not:** Language grammar exercises where the blank IS a grammatical element (verb tense, preposition) — there the grammar point is the keyword, not the content word.

### Memory Palace
- **Method applied:** #14 SMASHIN' SCOPE, #4 Buzan Review Intervals
- **Why:** Memory Palace is already a Buzan method (Method of Loci), but the content PLACED at each hotspot can be dry ("Bug'lanish — suv gaz holatiga o'tishi") or vivid ("Darvozada kir qurimoqda — Quyosh suvi TORTIB olyapti, ko'rinmas bug' osmonga UCHIB ketyapti!"). SMASHIN' SCOPE ensures the imagery is vivid — because research shows dry loci placements perform no better than rote memorization. The palace only works if what's placed there is memorable. Buzan Review Intervals ensure palaces are revisited at the critical forgetting curve points, not just once.
- **How:** Content placed at hotspots must pass SMASHIN' SCOPE (6+/12). Palace revisits follow Buzan Review Intervals (Day 1 → Day 3 → Day 7 → Day 14 → Day 30). "Hali emas" framing on missed recalls.
- **Where Not:** Already fully defined in `NETS-Memory-Palace-Definition.md`. Don't duplicate the spec — just add the SMASHIN' SCOPE gate and review interval floor.

### Tic Tac Toe
- **Method applied:** #12 Peg System integration
- **Why:** Standard Tic Tac Toe gates each move with a generic knowledge question — the board position and the question are unrelated. By merging with Peg System, the board position BECOMES the recall cue: cell 3 = Heart peg = the concept pegged to Heart. Now the student's spatial strategy (where to place X) is fused with their mnemonic retrieval (what's at that peg number). This creates a third encoding channel (strategic/spatial) on top of the existing two (visual peg + verbal concept), deepening the memory trace through triple coding.
- **How:** When Peg System and Tic Tac Toe are both in the same session, merge them: the 9 cells are labeled with peg numbers. To place X on cell 3, student must recall the concept pegged to number 3. Correct recall = X placed.
- **Where Not:** Only when Peg System is also active in the same session. When Peg System isn't selected, Tic Tac Toe plays normally with standard knowledge-gating questions.

### Puzzle Lock
- **Method applied:** #11 Link System
- **Why:** Puzzle Lock requires arranging tiles in the correct order — timeline events, process steps, classification levels. This IS the Link System problem: remember the sequence. But without a story connecting the items, the student relies on rote memory of the order. With a Link Chain story available as a hint ("Remember: first the water EVAPORATES, then it CONDENSES into clouds, then it FALLS as rain..."), the student has a narrative scaffold that makes the correct order memorable, not just memorizable. The story reduces random guessing and teaches the student that sequences have causal logic, not arbitrary order.
- **How:** When tiles represent a sequence, content authors provide the Link Chain story as a hint available after 2 wrong moves: "Remember the story: first X, then Y, then Z..."
- **Where Not:** Number-ordering puzzles (1-2-3...8) — no narrative chain needed for pure number sequence. Sentence fragment puzzles — grammar logic, not mnemonic.

### Mystery Box
- **Method applied:** #2 Von Restorff Effect
- **Why:** Mystery Box uses variable reward (Skinner) — the student doesn't know which box has the big prize. But the QUESTION behind the big prize box is usually random. By making the big prize question the "outstanding" one — the most surprising fact, the funniest scenario, the most unusual visual — you create a double reward: the XP prize AND a memorable learning moment. The Von Restorff Effect means this one question will be remembered far better than the other 8. You're using the game's existing reward structure to amplify a specific piece of knowledge.
- **How:** The large prize box (🏆, 1 per session) should contain the "outstanding" question — the most surprising, funny, or unusual item. Content authors tag which question gets the large prize.
- **Where Not:** Don't make ALL questions outstanding. The effect works because ONE thing stands out. If everything is unusual, nothing is.

### Spaced Flashcards
- **Method applied:** #4 Buzan Review Intervals
- **Why:** SM-2 is excellent for struggling items (rated "Again" or "Hard") but can be too generous with "Easy" items — pushing them weeks into the future. Buzan's research shows the 24-hour and 1-week review points are critical regardless of perceived ease. A student who rates a card "Easy" today may forget it in 3 days if there's no touchpoint. The Buzan floor catches these overconfident ratings before they become gaps.
- **How:** Card scheduling follows Buzan's floor: cards rated "Easy" still return at 24h, 1w, 1mo minimum — SM-2 can't push them further out than Buzan's mandatory touchpoints.
- **Where Not:** Cards rated "Again" — SM-2 already brings these back immediately. Buzan floor only matters for "Good" and "Easy" rated cards.

### Adaptive Quiz
- **Method applied:** #1 TEFCAS
- **Why:** The adaptive difficulty mechanism IS TEFCAS — the student tries (Trial), gets a result (Event/Feedback), the system compares to the target (Check), adjusts difficulty (Adjust), and the student progresses toward mastery (Success). But the student doesn't SEE this cycle — they just see questions getting harder or easier with no explanation. By naming the transitions, the student understands WHY the difficulty changed: "Your brain Adjusted successfully — next level!" or "Feedback received — finding your flow zone." This turns a confusing difficulty swing into a visible learning process.
- **How:** When difficulty increases: *"Trial successful — Adjusting to next level!"* When difficulty decreases: *"Feedback received — Adjusting for your flow zone."*
- **Where Not:** Don't show TEFCAS labels on every single question. Only on difficulty TRANSITIONS (level up or level down). Anything more is noise.

### Peer Teaching
- **Method applied:** #1 TEFCAS failure framing
- **Why:** Peer Teaching is the only mechanic where students PRODUCE knowledge instead of retrieving it. When the AI says "Incorrect — the answer is X," it kills the production impulse. But when it says "Hali emas! Your explanation covers [X] but is missing [Y]. How would you Adjust it?" — it treats the student as a teacher who needs to refine their explanation, not a student who got it wrong. This preserves the expert identity the mechanic is built on.
- **How:** When the AI evaluates a student's explanation as incomplete or inaccurate, it uses: *"Hali emas! Your explanation covers [X] but is missing [Y]. How would you Adjust it?"*
- **Where Not:** When the explanation is factually dangerous (e.g., wrong safety information in Texnologiya). In that case, direct correction is necessary — you don't Socratic-method your way around a safety hazard.

### Reflection Journal
- **Method applied:** #1 TEFCAS, #3 BOST Goal Recall
- **Why:** Reflection Journal is the conscious "Adjust" step of TEFCAS — making the brain's error-correction process explicit. Generic prompts ("What was hard?") produce generic answers. TEFCAS-framed prompts ("What Feedback did your brain receive? What will you Adjust?") produce structured metacognition. The BOST goal recall ("You wanted to learn X — did you?") closes the loop opened in Phase 0-A and gives the student a sense of completion or an honest "not yet."
- **How:** Prompts use TEFCAS vocabulary. Session ends with BOST goal recall: *"You wanted to learn X. Did you?"*
- **Where Not:** The raw performance summary (questions, XP, time) stays unchanged. TEFCAS applies to prompts only.

### Story Mode
- **Method applied:** #5 80/20 Keyword Tagging
- **Why:** Story Mode delivers content through narrative. Without keyword tagging, the downstream mechanics (Radiant Summary, Flash Cards, Sentence Fill, Memory Sprint) have to guess which words matter. With `keywords_80_20` tagged by the content author, every downstream mechanic knows exactly which terms to test, which to use as branch labels, which to blank in Sentence Fill. The keywords are the skeleton of the lesson — tagging them once ensures consistency across all phases.
- **How:** Every narrative segment has tagged keywords that feed downstream mechanics. The Stranger Test quality gate already ensures comprehension quality.
- **Where Not:** Speed reading mechanics (Focus Guide, Forward Momentum, Semantic Chunking) are DEFERRED — G5 students' bottleneck is comprehension, not speed. See "Deferred Methods" below.

### Memory Sprint
- **Method applied:** #11 Link System (Link Chain format), #4 Buzan Review Intervals
- **Why:** Memory Sprint has 5 formats — all retrieval-based (recall what you already know). Link Chain adds a 6th format that's encoding-based: the student reads a vivid chain story, then is tested on the sequence. This is better than "Order the Steps" for content where the sequence has causal logic (water cycle, digestion) because the story EXPLAINS why the order matters, not just what the order is. Buzan Review Intervals ensure the most critical prior concepts always appear in the Sprint, even if SM-2 would have delayed them.
- **How:** Link Chain is the 6th approved format. Buzan Review Intervals are floor constraints on the item selection algorithm.
- **Where Not:** Link Chain is not for unrelated vocabulary or math formulas — there's no sequential story to tell. Use Flash Sprint or Speed Match for those.

### Games Where Buzan Adds Nothing

| Game | Why Not |
|---|---|
| **Movement Breaks** | Physical activity — no knowledge encoding. Buzan methods are cognitive. |
| **Connect Four** | Pure strategy with knowledge gating. The strategy IS the engagement. Adding mnemonic framing overcomplicates a simple mechanic. |
| **Blackjack 21** | Math-only, probability-focused. Live calculation doesn't benefit from mnemonics. |
| **Codebreaker** | Letter deduction logic. The Wordle-style process is its own cognitive method. Layering Buzan adds friction, not value. |
| **Notebook Capture** | Physical drawing/writing. The kinesthetic act IS the encoding — Buzan's visual methods are already embedded in the act of drawing. |

---

## Deferred Methods (Future: Reading Fluency Module)

These Buzan methods are CUT from the active injection. Reason: G5 students' bottleneck is **comprehension, not speed**. Rayner et al. (2016) found speed reading training does not improve comprehension — it teaches skimming. These may apply at G9+ after empirical validation.

| # | Method | Why Deferred |
|---|---|---|
| 16 | Focus Guide (Fixation Training) | Pushes past sub-vocalization, but G5 students NEED sub-vocalization to comprehend complex text |
| 17 | Saccade Optimization | Good typography practice but not a Buzan-specific injection — belongs in general UI/UX spec |
| 18 | Forward Momentum Rule | Regression is a LEGITIMATE comprehension strategy at G5-6, not a bad habit. Re-reading is often necessary for process-heavy subjects. |
| 19 | Peripheral Vision Training | Same as saccade — general typography |
| 20 | Semantic Chunking | Needs A/B testing for Uzbek-language text before deployment |
| 21 | Sub-vocalization Elimination | Sub-vocalization is a comprehension AID at G5-6 |
| 23 | Meta-Guiding | Merged with Focus Guide — same reason |

## Pending Empirical Validation

| # | Method | Issue | Validation Required |
|---|---|---|---|
| 15 | Anti-Cheat Radiant Signature | Students explaining sequential processes naturally produce "linear" text — not because they're cheating. False positive rate would be unacceptable. | Collect 500+ real G5-6 responses, label human vs AI, train classifier, precision must be ≥90% or it doesn't ship. |

## Not in Homework Engine (Belong Elsewhere)

| # | Method | Where It Belongs |
|---|---|---|
| 3 | Group Mind Mapping | Post-MVP roadmap (needs multiplayer) |
| 8 | Secret Symbols | NETS-System-Design-v1.md (Bilim Bazasi metagame) |
| 9 | Color-Coded Zones | NETS-UI-UX-Design-Spec (visual design system) |
| 31 | SEM³ Memory Matrix | NETS-System-Design-v1.md (backend data model) |
