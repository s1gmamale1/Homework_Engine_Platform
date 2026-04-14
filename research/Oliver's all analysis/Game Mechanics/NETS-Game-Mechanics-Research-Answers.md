# Game Mechanics — Research Answers for 15-Field Spec

**Date:** 2026-04-08
**Purpose:** Evidence-based answers to design questions for 7 game mechanics. These inform the full 15-field spec that will follow.
**Sources:** See citations at bottom of each section. Universal (subject-agnostic, grade-agnostic).

---

## MEMORY PALACE (Default #5)

### Q1: Location set or only Registan? Fallback for rural kids?

**Answer:** Set of culturally-relevant locations — Uzbek hovli (courtyard home), school layout, neighborhood bazaar route, local park. **Registan is one option, not the only one.** Fallback: "your home" layout for rural kids who've never seen Registan. Matteo Ricci (1596) successfully localized MoL for Chinese scholars using Chinese architecture, not European cathedrals. Procedural-generation study (MDPI 2025) found unfamiliar layouts cause cognitive fatigue — **do not algorithmically generate random palaces.**

### Q2: 3D walkthrough, interactive image with hotspots, or text-only?

**Answer:** **Interactive labeled image with 5 hotspots (2.5D/isometric).** 3D adds navigation load without proportional recall benefit on mobile screens. Text-only relies on mental imagery that young students lack. For mobile: isometric view + clickable hotspots is optimal. Dual coding theory: every hotspot shows both a visual image AND a text label. 3D/VR superiority (Krokos 2019: +30% retention) applies to VR headsets, not smartphone screens.

### Q3: How does student place a concept?

**Answer:** **Tap a hotspot → select from 2-3 pre-designed visual images representing the concept → drag to lock.** The cognitive work (forming the association) happens during image selection + the act of dragging. Biorxiv 2025 found that **distinct encoding representations** (unique item-location associations) predict long-term retention. If the UI auto-places items, it bypasses the cognitive work. Student must actively participate. For ages 6-8: use pre-placed associations with guided mental walks. For ages 9+: use the hybrid image-selection + drag-to-place model.

### Q4: Recall test format?

**Answer:** **Primary: free recall** — "Walk through your palace and tell me everything you remember." **Secondary: temporal order** — "Which concept was at location X?" **Avoid pure MC** as the primary assessment — it underestimates actual MoL retention by bypassing active retrieval. Biorxiv 2025 explicitly found MC formats underestimate MoL-trained memory. The spatial clustering effect means students naturally recall items placed near each other together.

### Q5: Palace persistence across sessions?

**Answer:** **Persists across sessions.** Revisited via spaced repetition (SM-2 schedule). One palace per topic to avoid cross-topic interference. New topics get new palaces. Biorxiv 2025 found 6 weeks of MoL training yielded sustained improvements measurable after 4 months — but only with repeated revisit. Spatial scaffolding alone decays without reinforcement (MDPI 2025). Over time, students build a collection of palaces (one per major topic).

### Age & Capacity Alignment

| Age Range | Min Age | Optimal Loci | Interaction |
|-----------|---------|-------------|-------------|
| 6-8 years | Guided MoL feasible from 7-8 | 3-5 loci | Pre-placed, guided walkthrough |
| 9-11 years | Independent use from 9-10 | 5-10 loci | Image selection + drag-to-place |
| 12-14 years | Full capacity approaching | 10-15 loci | Full hybrid model |
| 15-18 years | Near-adult effectiveness | 15-20+ loci | Full hybrid + self-built palaces |

### Key Citations

- Qureshi et al. 2014 (PMC4056179) — shared pre-selected environment for novices
- Moll & Sykes 2023 (Virtual Reality, PMC9540171) — VR MoL recall improvements
- Krokos et al. 2019 — 30% VR advantage over 2D
- biorxiv 2025 (doi:10.1101/2025.02.24.639840v2) — distinct encoding, free recall, 4-month retention
- MDPI Applied Sciences 2025 (doi:10.3390/app15052304) — procedural generation warning, unfamiliar layouts
- Cowan 2001 — working memory ~4 chunks
- Matteo Ricci 1596 — cross-cultural MoL localization
- Paivio 1971 — Dual Coding Theory
- Roediger & Karpicke 2006 — retrieval practice
- Twomey & Kroneisen 2021 — MoL meta-analysis

---

## STORY MODE (Default #6)

### Q1: Pre-authored or AI-generated on the fly?

**Answer:** **Human-authored master narrative per chapter** as the source of truth. AI generates localized variants, difficulty adjustments, and scaffolded checkpoint variants on failure — but **never generates the core story on the fly.** Cao et al. 2023 found AI and human content perceived as equivalent by students, but **learning gains and long-term retention were not measured.** Seductive details meta-analysis (Sanchez & Wiley 2006; Rey et al. 2018) confirms decorative narrative elements impair transfer — AI can't judge which details matter pedagogically. Human-authored templates with AI-assisted adaptation is the pragmatic approach at scale.

### Q2: Comprehension gates — MC or open short-answer?

**Answer:** **Mixed format: 2 MC + 1 short-answer per checkpoint.** MC items use distractors derived from actual textbook misconceptions (not random wrong answers). Short-answer tests generative processing and catches "lucky guessers." Ozuru et al. 2007 found MC alters how students process text (recognition/elimination vs. genuine comprehension). For G1-2: MC only (typing too slow). For G3+: mixed format. The CR item should be 1-2 sentences, scored via keyword matching with fallback to teacher review.

### Q3: Interactive (pick a path) or passive reading?

**Answer:** **Linear backbone with micro-choices.** Narrative follows fixed sequence aligned to textbook content, but at 2-3 points the student makes a choice that changes *how* the next segment is presented (same content, different framing — e.g., farmer's perspective vs. scientist's perspective). Full branching is prohibitively expensive at NETS scale and risks students missing core content. Adams & Mayer 2011 found narrative elements increase engagement but can reduce transfer if not aligned to learning objectives. Rowe et al. 2007 found narrative presence works best when every story event serves a pedagogical purpose.

### Q4: Voice-over (TTS) or text-only?

**Answer:** **Text + illustrations is the pragmatic default for launch.** Mayer's modality principle (2002) favors narration + visuals over text + visuals, but Uzbek is a low-resource language for TTS. Current Uzbek TTS options (Sayro TTS, Aisha Group) are improving but not production-reliable. Poor-quality TTS creates *more* cognitive load than it saves. Offer TTS as an **optional toggle** for struggling readers. When TTS quality reaches validated benchmarks, switch to narration + visuals for G1-5, retain text + visuals for G6+.

### Q5: Length — fixed or scales with chapter difficulty?

**Answer:** **Fixed by grade band, NOT by chapter difficulty.** Segment count and length scale by grade band: G1-3: 30-60s segments, 3-4 checkpoints. G4-6: 60-90s segments, 4-6 checkpoints. G7-9: 90-120s segments, 5-7 checkpoints. Content *density* within segments adjusts, not segment duration. Cognitive capacity is the constraint, not content difficulty. Meta-analysis by Rey et al. (41 studies, N=3,113) found optimal segment length is 30-90 seconds or 1-3 core concepts per segment.

### Narrative Structures by Age (Piaget Alignment)

| Age Range | Piaget Stage | Narrative Structure |
|-----------|-------------|-------------------|
| 6-7 years | Preoperational | Linear, concrete, character-driven. Single protagonist, simple cause-effect, heavy illustration. |
| 8-11 years | Concrete Operational | Linear with mild complexity, problem-solution arc. Concrete settings, simple metaphors. |
| 12-14 years | Early Formal Operational | Multi-perspective, thematic. Abstract themes, irony, moral ambiguity. |
| 15-18 years | Formal Operational | Complex, layered. Abstract reasoning, hypothetical scenarios, meta-narrative. |

### Key Citations

- Cao et al. 2023 (arXiv:2306.10509) — AI vs. human educational content perceived equivalent
- Sanchez & Wiley 2006; Rey et al. 2018 — seductive details impair transfer
- Adams & Mayer 2011 (Instructional Science) — narrative vs. non-narrative instruction
- Rowe, McQuiggan & Lester 2007 (AAAI) — narrative presence in learning environments
- Mayer 2002/2009 (Cambridge Handbook) — Cognitive Theory of Multimedia Learning
- Rey, Beege et al. 2023 meta-analysis (Educational Psychology Review, g=0.51, 41 studies) — segmentation effect
- Ozuru et al. 2007 — how MC shapes reading comprehension construct
- Cowan 2001 — working memory ~4 chunks
- Hsiao et al. 2020 (Computers & Education) — systematic review of narrative-based learning

---

## ADAPTIVE QUIZ (Default #7)

### Q1: Pre-calibrated item bank or live calibration?

**Answer:** **Pre-calibrated item bank required.** IRT requires a reference frame to place students on the theta scale. Standard approach: (1) field test 3-5x the target number of items, (2) calibrate via Rasch/2PL (Winsteps, IRTPRO, mirt in R), (3) deploy calibrated bank for CAT, (4) rotate in new pilot items for online calibration. For NETS at scale, a **simplified Rasch calibration (1PL, difficulty only)** with 30-50 items per subject-chapter is realistic. Live calibration of new "pilot" items interspersed among calibrated items is possible for ongoing improvement.

### Q2: Feedback timing — immediate or delayed?

**Answer:** **Immediate after each question.** Hattie places feedback at d=0.70-0.75 — one of the highest-impact interventions. Immediate feedback prevents encoding of misconceptions. Delayed feedback advantage (Butler effect) applies only to high-stakes summative assessment, not practice-phase learning. Azevedo & Bernard 1995 meta-analysis (computer-based instruction): d=0.38 for delayed posttests with immediate feedback. 2026 meta-analysis in JEP: immediate feedback significantly outperforms delayed on conceptual knowledge learning.

### Q3: Wrong answer — hint first or reveal?

**Answer:** **Sequenced scaffold: attempt → hint → partial solution → answer + explanation.** Kapur's Productive Failure research (2008, 2016) shows initial struggle before instruction enhances conceptual understanding and transfer. But productive failure requires structured scaffolding after failure — not just showing the answer. Tier 1: metacognitive prompt ("What do you know about X?"). Tier 2: worked partial solution. Then answer + full explanation contrasting student's likely misconception with correct reasoning. Do NOT just reveal the answer — the learning benefit comes from the consolidation phase after failure.

### Q4: Per-framework bans?

**Answer:** **Yes — universal mechanic registry with per-framework override flags.** This is the Strategy Pattern in software design. Example: `"science_grade5": "banned"` because Science uses Final Boss assessment. The ban list should be explicit so designers can see why a mechanic is excluded from their framework. Implementation: `framework_bans: ["science_grade5", "tarbiya_grade5"]`.

### Q5: Round length — fixed or theta-stabilizes?

**Answer:** **Hybrid: fixed 5-7 questions with early termination.** Babcock & Weiss 2012 found variable-length CATs provide no significant accuracy advantage for average students but create highly variable session lengths (some 3 items, some 20). For homework context, predictability matters more than measurement precision. Minimum 5 questions; if last 3 are all correct at student's ceiling, stop early. 2025 Eurasia J. Math study found variable-length CATs achieved equivalent accuracy with 15-25% fewer items on average, but the variance in session length is a usability problem.

### Key Citations

- Babcock & Weiss 2012 — termination criteria in CAT
- Hattie 2009 — feedback effect size d=0.70-0.75
- Azevedo & Bernard 1995 — computer-based feedback meta-analysis
- Kapur 2008/2016; Sinha & Kapur 2019 (Computers & Education) — productive failure
- Kulik & Kulik 1988 — immediate vs. delayed feedback
- 2025 Eurasia J. Math, Science and Technology Education — variable-length CAT study

---

## MYSTERY BOX (Default #8)

### Q1: Box count — fixed, student-chosen, or system-chosen?

**Answer:** **System-chosen: 3 boxes default, 4 for higher-difficulty tiers.** Rohrer's interleaving studies consistently use 3-4 problem types. With only 2 categories, contrast is too obvious; with 5+, cognitive load overwhelms the benefit. Taylor & Rohrer 2010 and Rohrer et al. 2020 (RCT, 7th-grade math, Journal of Educational Psychology) used exactly 4 problem types. InnerDrive research: "typically about 3 different topics interleaved." The cognitive mechanism is discriminative contrast — comparing between categories forces deeper processing.

### Q2: Category visible or fully blind?

**Answer:** **Vague thematic label** — "Something about plants..." / "Remember last week?" — but NOT the specific problem type or difficulty. Loewenstein's Information Gap Theory (1994): curiosity arises from the gap between what is known and what one wants to know. The gap must be noticeable but not overwhelming. Kang et al. 2009 and Kidd et al. 2012 (PLoS ONE) confirmed: fully blind causes anxiety, fully labeled kills curiosity. Inverted-U relationship between uncertainty and curiosity.

### Q3: Interleaving source — same subject or cross-subject?

**Answer:** **Near-transfer (same subject, prior chapters) is primary.** Far-transfer (cross-subject) has weak empirical support — Barnett & Ceci 2002 found near-transfer benefits are 10x larger than far-transfer. A 2024 Learning Scientists study found "no significant difference on far transfer cases between blocked and interleaved learning conditions." Far transfer requires explicit bridging instruction, not just mixing content. Occasionally (1 in 10-15 boxes) a cross-subject "bonus connection" can appear, but it should be explicitly framed as such.

### Q4: Two meanings — split them?

**Answer:** **YES. Absolutely split into two separate mechanics.** These are fundamentally different:

| Aspect | Mystery Box (Interleaved Practice) | Reward Chest (Variable-Ratio Reward) |
|--------|-----------------------------------|-------------------------------------|
| Purpose | Retrieval practice across mixed categories | Engagement hook, XP/cosmetic rewards |
| Psychology | Discriminative contrast (Bjork) | Variable ratio schedule (Skinner) |
| Research base | Rohrer, Taylor, Dunlosky | Behavioral economics |
| Risk | None | Potential gambling-like concerns in K-11 |

The gacha version (random case-opening with cosmetic/XP rewards) is an **extrinsic motivation mechanic**, not a learning mechanic. In K-11 education, gambling-like mechanics raise ethical and potentially regulatory concerns. Rename the reward version (`Reward Chest` or `Lucky Star`) to eliminate confusion.

### Q5: Order — sequential or student picks?

**Answer:** **Student picks any order.** Self-Determination Theory (Deci & Ryan 2000): autonomy is a basic psychological need. Patall et al. 2010 (Journal of Educational Psychology) found choice increases motivation, liking, and perceived competence. Order doesn't affect interleaving efficacy, so the autonomy benefit is pure upside. Schmidt et al. 2018 found choice can increase perceived difficulty but also increases task investment and effort.

### Key Citations

- Rohrer et al. 2020 (Journal of Educational Psychology) — interleaving RCT
- Taylor & Rohrer 2010 — interleaved practice effects
- Loewenstein 1994 — information gap theory of curiosity
- Kang et al. 2009 (Journal of Research in Personality) — inverted-U curiosity
- Kidd, Piantadosi & Aslin 2012 (PLoS ONE) — curiosity peaks at intermediate complexity
- Barnett & Ceci 2002 — near vs. far transfer
- Deci & Ryan 2000 — Self-Determination Theory
- Patall, Cooper & Wynn 2010 (JEP) — choice enhances motivation
- Dunlosky et al. 2013 — interleaving as effective learning technique

---

## MEMORY MATCH BLITZ (Interactive #4)

### Q1: Grid size — fixed or scales?

**Answer:** **Scales, but capped at 4×5 (20 cards, 10 pairs).** Cowan 2001: children's working memory ~3-4 chunks. A 6×6 grid (36 cards, 18 pairs) exceeds G5 capacity and shifts the task from memory strategy to random search. Recommended: Easy (L1-L2): 3×4 grid (12 cards, 6 pairs). Medium (L3-L4): 4×4 grid (16 cards, 8 pairs). Hard (L5+): 4×5 grid (20 cards, 10 pairs). The 6×6 grid is appropriate for adults, not Grade 5.

### Q2: Pair found → confirmation question. If wrong — re-hide or just not count?

**Answer:** **Re-hide the pair.** Retrieval practice research (Roediger & Karpicke 2006): retrieval with corrective feedback is the effective combination. If the pair stays revealed after a wrong confirmation answer, the student has just encoded incorrect information with a "correct" visual signal. Correct behavior: wrong → reveal correct answer for 3 seconds → re-hide. Student must try again later in the round. This forces a second retrieval attempt and leverages the hypercorrection effect (Butterfield & Metcalfe 2006): errors made with high confidence, when corrected, are less likely to be repeated.

### Q3: Time pressure — hard timer or soft penalty?

**Answer:** **Soft penalty.** Points decrease over time, but the round does NOT end. Hard timers are a hindrance stressor that increases extraneous cognitive load, interfering with the primary learning task. For students already below proficiency level, time pressure induces anxiety which further degrades working memory (Ashcraft & Kirk 2001). Fluency research (Arevart & Nation 1991; Garside 2020) supports time pressure for fluency development specifically — but only *after* accuracy is established, not during initial learning. Add a "fluency bonus" for completing pairs quickly, but never force a session end due to time.

### Q4: Confirmation question — about the matched pair or random?

**Answer:** **About the matched pair specifically.** Bjork's Desirable Difficulties (1994) and the Region of Proximal Learning (Metcalfe & Bjork) specify that difficulty is productive when it is connected to the learning target. A confirmation question about the matched pair directly strengthens the association between the visual concept (the card pair) and its verbal/declarative knowledge. A random question from the pool adds no such association and breaks the learning loop.

### Key Citations

- Cowan 2001 — working memory ~4 chunks
- Roediger & Karpicke 2006 (Psychological Science) — retrieval practice
- Butterfield & Metcalfe 2006 — hypercorrection effect
- Arevart & Nation 1991; Garside 2020 — fluency training
- Ashcraft & Kirk 2001 — math anxiety and working memory
- Bjork 1994 — desirable difficulties
- Metcalfe & Bjork — Region of Proximal Learning

---

## REACTION CHAIN (Interactive #5)

### Q1: Visual representation — linear chain, dominoes, or process diagram?

**Answer:** **Default: linear node chain** (cheapest to build, works for any content). **Ideal for high-traffic chains: process-diagram-style visualization** (photosynthesis steps look like a process flow, not abstract nodes). Dominoes adds engagement but no learning benefit — the falling animation is cosmetic, not representational. Content-specific representations are superior to generic ones, but cost more to produce. The linear chain is the baseline; invest in process-diagram representations only for the most important/high-traffic chains.

### Q2: "3 wrong in a row breaks the chain" — reset to 0 or end session?

**Answer:** **Reset to 0 (partial streak loss), NOT session end.** Total streak loss is already a strong negative motivator. Adding session termination creates a catastrophic failure state linked to disengagement, particularly in younger learners. The "perfectionism mindset" problem: when failure feels catastrophic, students avoid risk-taking and either game the system or quit. On break: streak resets to 0, offer recovery scaffold — "Your streak was [X]. Let's rebuild it together" with a slightly easier next question. Reframe as "minor setback, not a failure."

### Q3: Time pressure — hard countdown or no timer?

**Answer:** **Optional soft timer.** Default mode (accuracy): no timer or generous 20-30s soft timer. Fluency mode (practice round replay): 10-15s timer with streak bonus for speed. Timer is a challenge layer, not a gate — running out of time counts as wrong but does not end the session. Response time research in educational measurement indicates 10-15 seconds is the typical window for Grade 5 students to process and answer a single-concept question.

### Q4: Nodes conceptually sequential or unrelated?

**Answer:** **MUST be conceptually sequential.** Otherwise it is just a quiz with a streak counter — the "chain" is cosmetic. Reaction Chain is for inherently sequential content: photosynthesis steps, water cycle, historical timelines, cause-effect chains, multi-step procedures. NOT for vocabulary recall, factual recall, or isolated definitions. The learning objective is **process understanding**, not knowledge coverage. If the nodes are unrelated questions, this is functionally a regular quiz with gamification skin.

### Key Citations

- Sequential learning and process visualization research
- Streak-based motivation research (Cohorty analysis 2025)
- Arevart & Nation 1991; Garside 2020 — fluency training
- Response time research in educational measurement (2016)

---

## WORD LADDER CLIMB (Interactive #6)

### Q1: Language — Uzbek, English, or both?

**Answer:** **Uzbek ladders for Uzbek language instruction. English ladders for English/CEFR subject.** Adapts to language of instruction. But see Q3 — this mechanic has severely limited applicability beyond language subjects.

### Q2: Ladder rule — change 1 letter, must intermediates be real words?

**Answer:** **Change 1 letter per step. Each intermediate MUST be a real dictionary word.** Carroll's original Doublets rules (1878, Vanity Fair): every step must be a valid common word (proper nouns excluded). Allowing non-words destroys the orthographic learning benefit — the exercise becomes arbitrary letter manipulation without vocabulary reinforcement. For Uzbek: requires a pre-built word ladder database validated against an Uzbek dictionary. You cannot procedurally generate valid ladders without dictionary validation.

### Q3: "Biology terminology" claim — valid?

**Answer:** **INVALID. Remove biology from use cases.** Biology terms (photosynthesis, chloroplast, mitochondria, ecosystem) differ by many letters, not one. You cannot build a meaningful word ladder from "cell" to "nucleus" through single-letter substitutions where every intermediate is a valid word. Uzbek is a **Turkic, agglutinative language** with rich morphology — words build via suffix chains, not letter substitution. Finding valid 1-letter-different word pairs in Uzbek vocabulary is significantly harder than in English.

Word ladders are genuinely useful only for:
- **Native language instruction** (spelling patterns, phonics, orthographic awareness)
- **Foreign language learning** (CEFR A1-A2 vocabulary, word families)
- Tightly curated related-word sets (short vowel patterns: cat → cot → cut → hut)

For science subjects, consider a **"Suffix Ladder" variant** — adding/removing suffixes to build morphological awareness. This is linguistically appropriate for agglutinative languages like Uzbek.

### Q4: Subject question separate from word change?

**Answer:** **Two distinct phases: (1) answer a subject question to unlock the letter change, then (2) perform the letter change as a secondary puzzle.** The word change is the *reward* for answering the question, not the question itself. Subject learning is the primary objective; the word game is the engagement layer. In standard educational word ladder implementations, the subject question gates the word change. Wrong answer = hint (not a revealed change).

### Q5: Hints / skips budget?

**Answer:** **1 hint per step** (show first/last letter of target word, or a definition clue). **1 skip per ladder total** (jump to next rung without solving current one). If student uses both hint and skip on the same step, the ladder is too difficult — recommend dropping to an easier ladder. Wood/Bruner/Ross scaffolding theory: just-enough support to keep learner in Zone of Proximal Development.

### Key Citations

- Carroll 1878 (Vanity Fair) — original Doublets rules
- MorphUz analyzer (arXiv 2024/2025) — Uzbek agglutinative morphology
- arXiv 2024 (NLP for Central Asian Turkic languages) — Uzbek low-resource challenges
- Vygotsky ZPD; Wood, Bruner & Ross 1976 — scaffolding theory
- Orthographic depth research — word ladder effectiveness across writing systems

---

## Architectural Recommendations

### 1. Split Mystery Box into two mechanics
- **Mystery Box** = interleaved practice (learning mechanic, Default #8)
- **Reward Chest / Lucky Star** = variable-ratio reward event (engagement hook, separate entry)
- Different purposes, different research bases, different ethical considerations for K-11

### 2. Remove "biology" from Word Ladder use cases
- It doesn't fit the mechanic. Language subjects only.
- Consider "Suffix Ladder" variant for agglutinative languages like Uzbek

### 3. Add `framework_bans` field to every mechanic definition
- Explicitly lists which subject-grade frameworks ban it
- E.g., `"science_grade5": "banned"` for Adaptive Quiz
- This is a universal architectural pattern, not a per-mechanic workaround

### 4. Universal mechanic registry with per-framework overrides
- Strategy Pattern: mechanic interface is universal, each framework declares applicability
- Ban list is explicit (not implicit) so designers see why a mechanic is excluded

---

## Summary Matrix

| Mechanic | Core Research Base | Key Finding | NETS Recommendation |
|----------|-------------------|-------------|---------------------|
| **Memory Palace** | MoL/Method of Loci (2000+ years of research, modern neuroscience) | Distinct encoding + free recall + spaced revisit = durable memory | Interactive isometric map with hotspots; persists across sessions; free recall primary test |
| **Story Mode** | Narrative-based learning (Hsiao 2020), multimedia learning (Mayer) | Linear with micro-choices; segmentation at 30-90s; human-authored core | Human master narrative + AI variants; 2 MC + 1 short-answer per checkpoint |
| **Adaptive Quiz** | IRT/CAT (Babcock & Weiss 2012), productive failure (Kapur) | Pre-calibrated bank required; immediate feedback; 2-tier hints | Simplified Rasch (1PL); 5-7 fixed questions; hint→partial→answer sequence |
| **Mystery Box** | Interleaving (Rohrer 2020), curiosity (Loewenstein 1994) | 3-4 categories optimal; vague labels; near-transfer only | 3 boxes, vague labels, prior-chapter content, split reward mechanic |
| **Memory Match Blitz** | Retrieval practice (Roediger 2006), desirable difficulties (Bjork) | Re-hide wrong pairs; soft timer; pair-specific questions | 3×4 → 4×5 max; re-hide on wrong; soft timer; pair-tied confirmation |
| **Reaction Chain** | Sequential learning, fluency training (Arevart & Nation) | Nodes must be sequential; reset streak; optional timer | Process-diagram content; streak reset + recovery; optional 10-15s timer |
| **Word Ladder Climb** | Orthographic awareness (Carroll 1878), morphological analysis | Works for language only; real-word intermediates required | Deploy for Uzbek/English only; 1 hint/step, 1 skip/ladder; remove biology |
