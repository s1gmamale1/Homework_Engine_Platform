# NETS Library Framework — Subject Classification & Content Catalog

**Version:** 0.5 — Draft (UNIFIED-Buzan alignment)
**Date:** 2026-04-14
**Changelog v0.5:** Updated dependency from UNIFIED to UNIFIED-Buzan. Added National Pride cross-family inheritance note (Part 8). Added GRADING-SYSTEM.md as Layer 4 dependency. No changes to family definitions, mechanic tables, boss formats, or Buzan integration.
**Changelog v0.4:** Fixed TEFCAS/IRT relationship, renamed Phase 0 to Pre-Session, removed speculative features from main body, fixed SMASHIN' SCOPE terminology, removed duplicate summary, updated Weekly PISA to all-tier, added Radiance Score implementation contract.
**Changelog v0.3:** Added Part 7 — Buzan Cognitive Science Integration (TEFCAS engine as core difficulty logic, memory systems Link/Peg/Major/Memory Palace/SMASHIN' SCOPE/SEM3, BOST study technique mapped to Phase 0-A/0-B, Mind Mapping 7 Laws with G5-G6 WM-respecting adaptations, speed reading eye-tracking/chunking/sub-vocalization with UI/UX metrics, radiant navigation architecture, anti-cheat radiance score, quantifiable metrics table with 16+ empirical values). Updated version header. Added Buzan research wave to completed list.
**Changelog v0.2:** Added `{lang}` to content addressing schema (bilingual system). Raised L2 unlock threshold from 70% to 80% (flow-state headroom). Replaced L3 label "Sinovga tayyorlan" with "Ustoz yo'li" (SOUL Principle 3 — hidden difficulty). Added ADR-pending markers for Literature and Informatics family placement. Added PE/Movement Breaks clarification. Added ADR requirement for DTM full-exam Assessment Mode. Added Lyceum Delta citation to Gemini research. Defined quality check criteria. Added cost estimate. Added formative completion gates for Creative Lab and Music Production. Added multi-path UX note. Flagged monthly Basic PISA as proposal requiring product decision. Updated scope declaration.
**Depends on:** `NETS-Homework-Engine-UNIFIED-Buzan.md` v2.0 (Layer 0), `NETS-System-Design-v1.md` (Layer 1), `GRADING-SYSTEM.md` v1.0 (Layer 4)
**Scope:** Library architecture — classification, levels, paths, catalog hierarchy, and placement guidance. Basic/Premium tier overlay mechanics are defined separately in the Tier Overlay spec; placement suggestions in Part 6 describe where library content surfaces in the product but do not define tier pricing or gating rules.

---

## Part 1: Subject Family Classifications

### What a Subject Family Is

A Subject Family groups subjects that share the same cognitive demands, answer formats, Boss evaluation patterns, and game mechanic fit. The family does the heavy lifting: once a family framework exists, every subject beneath it inherits the cognitive profile, mechanic emphasis table, Boss format rules, and Notebook Capture frequency. Subject authors only fill in textbook-specific content.

This is the scale mechanism. 5 families → 29 subjects → ~110 subject×grade frameworks → thousands of content items.

**Rule:** Family membership is locked. A subject cannot move between families without a formal ADR (Architecture Decision Record).

---

### Family 1: Aniq Fanlar — Exact Sciences

**Uzbek gloss:** "Aniq" = precise, exact, derivable

**Subjects in this family:**

| Subject | UZ Name | RU Name | Grade Range | Notes |
|---------|---------|---------|-------------|-------|
| Mathematics | Matematika | Математика | G5-6 | Unified subject, splits at G7 |
| Algebra | Algebra | Алгебра | G7-9 | Split from Matematika |
| Geometry | Geometriya | Геометрия | G7-9 | Split from Matematika |
| Algebra & Analysis | Algebra va analiz asoslari | Алгебра | G10-11 | Advanced continuation |
| Geometry (advanced) | Geometriya | Геометрия | G10-11 | Advanced continuation |
| Physics | Fizika | Физика | G7-11 | |
| Chemistry | Kimyo | Химия | G7-11 | |
| Informatics | Informatika / Dasturlash / Robototexnika | Информатика | G5-11 | Includes programming track at G11. **ADR-pending:** default placement is Aniq Fanlar (algorithmic thinking, formal notation). If G5 Informatics framework reveals cognitive demands are more creative/constructive than derivation-based, raise ADR for reclassification. See System Design v1 §10 #2. |

**What this family teaches:** Formal reasoning. Every concept in Aniq Fanlar is either (a) a definition/axiom, (b) a derivation from prior concepts, or (c) an application of a derived rule to solve a specific problem. The family builds the student's ability to move fluently between concrete representations (objects, diagrams), symbolic notation (formulas, equations), and verbal reasoning ("because X, therefore Y").

**Cognitive demands:**
- Multi-step calculation and derivation
- Formal notation reading and production
- Error detection in worked solutions
- Spatial reasoning (geometry, physics diagrams)
- Algorithmic thinking (informatics)
- Rule memorization for formula recall
- Concept understanding before procedure execution (never the reverse)

**Pedagogical principles (best practices):**

1. **CPA progression is mandatory** — every new concept appears first as a concrete scenario (physical objects, real quantities), then pictorial (bar models, diagrams, number lines), then abstract (symbols, formulas). No exceptions. Sweller's Cognitive Load Theory: reduce extraneous load before introducing intrinsic complexity.

2. **Worked examples before problem solving** — students see a fully solved example before attempting a similar problem. The worked example uses the "completion effect": later examples have gaps the student fills, gradually removing scaffolding until independent problem solving.

3. **Error analysis as a teaching tool** — deliberately-wrong worked examples are presented for students to diagnose. This builds meta-cognitive error detection, which transfers to self-correction during independent work.

4. **Dual coding for formulas** — every formula is presented with both symbolic notation AND a visual/verbal explanation of what it means. "A = πr²" is accompanied by "the area of a circle equals pi times the radius squared — if you double the radius, the area quadruples."

5. **Interleaved practice** — once a skill is acquired, it is mixed with previously-learned skills in subsequent practice sessions. This prevents the "I just learned it, so I know which tool to use" illusion.

**Mechanic emphasis (primary):**
- Worked examples (Generation Effect — students complete partial solutions)
- CPA progression (mandatory before any symbolic work)
- Tile Match (formula assembly, drag-and-drop equation components)
- Notebook Capture (photograph handwritten calculations — 25-40% retention gain over typing)
- Error Analysis (deliberately-wrong examples for diagnosis)

**Mechanic emphasis (secondary):**
- Adaptive Quiz (difficulty-calibrated practice)
- Speed Match (arithmetic fluency drills)
- Why Chain (2-level max for G5, 3-level for G6+)

**Boss format:**
- Open numerical or derivation problem — never multiple-choice for G6+
- G5 override: up to 30% MC allowed (ADR-005)
- Rubric-based partial credit: correct method with arithmetic error still earns points
- Notebook Capture accepted: student photographs handwritten solution

---

### Family 2: Til Fanlari — Languages

**Uzbek gloss:** "Til" = tongue, language

**Subjects in this family:**

| Subject | UZ Name | RU Name | Grade Range | Notes |
|---------|---------|---------|-------------|-------|
| Uzbek Language | Ona tili | Узб. язык | G5-11 | Native language grammar & composition |
| Russian Language | Rus tili | Русский язык | G5-11 | Native/second language |
| English | Ingliz tili | Англ. язык | G5-11 | Foreign language |
| Literature | Adabiyot / Литература | Литература | G5-11 | Literary analysis, reading comprehension. **ADR-pending:** default placement is Til Fanlari (textual comprehension, literary production). May move to a standalone Humanities subfamily if drafting G5 Literature + Ijtimoiy Fanlari simultaneously reveals better interpretive-skill clustering. See System Design v1 §10 #3. |
| German | Nemetskiy yazyk | Немецкий язык | G11 RU | Edge case — appears only in G11 RU |

**What this family teaches:** Communication through structured language acquisition. Unlike Aniq Fanlar (where truth is derivable), language is conventional — rules are agreed-upon patterns, not logical necessities. The family builds four core competencies: comprehension (reading/listening) and production (writing/speaking), each at increasing levels of complexity.

**Cognitive demands:**
- Vocabulary acquisition and long-term retention (spaced repetition)
- Grammar rule application in context (not isolated drills)
- Reading fluency and textual inference
- Listening comprehension from audio stimuli
- Writing production: sentences → paragraphs → essays
- Narrative interpretation and perspective-taking (Literature)
- Genre recognition and appropriate register selection

**Pedagogical principles (best practices):**

1. **Comprehensible input (Krashen)** — students acquire language when they understand messages slightly above their current level (i+1). Story Mode narratives, graded readers, and contextualized grammar instruction all deliver i+1 input. Isolated grammar drills do not.

2. **Spaced repetition for vocabulary** — every new word enters the student's spaced repetition deck immediately. Review intervals follow the Ebbinghaus forgetting curve: 1 day, 3 days, 7 days, 21 days, 60 days. Words the student consistently recalls graduate to "mastered"; words they miss reset to shorter intervals.

3. **Grammar in context, not in isolation** — grammar rules are introduced within a story or text first, then extracted as an abstract rule statement. Students encounter the pattern in use before they learn its name.

4. **Dual coding for vocabulary** — every new word is introduced with image + native-language gloss (for foreign languages). For native language grammar, rules are introduced with concrete sentence examples before formal rule statements.

5. **Scaffolded production** — writing tasks progress from guided production (sentence stems provided, G5) to prompted free production (G6+) to independent composition (G9+). Students are never asked to produce without scaffolding first.

**Mechanic emphasis (primary):**
- Spaced Repetition flashcard decks (vocabulary, orthographic rules)
- Cloze / Sentence Fill (grammar in context)
- Listening tasks (audio stimulus + comprehension questions)
- Dialogue exercises (prompted response, not open sandbox)
- Dictation tasks (hearing → writing, dual-coding effect)
- Story Mode for Literature (narrative arc drives engagement)

**Mechanic emphasis (secondary):**
- Memory Palace (vocabulary clusters, idiomatic phrases)
- Word Ladder (morphological awareness)
- Tile Match (sentence construction — drag words into grammatical order)

**Boss format:**
- Writing production task evaluated by Tier 2 LLM against rubric
- G5 Boss: guided production (sentence stem or paragraph frame provided)
- G6+ Boss: prompted free production ("Write 3-5 sentences about...")
- G9+ Boss: extended composition with structural requirements (introduction, body, conclusion)
- Literature Boss: textual analysis ("What does this passage reveal about the character?")

---

### Family 3: Tabiat Fanlari — Natural Sciences

**Uzbek gloss:** "Tabiat" = nature

**Subjects in this family:**

| Subject | UZ Name | RU Name | Grade Range | Notes |
|---------|---------|---------|-------------|-------|
| Biology | Biologiya | Биология | G5-11 | |
| Geography | Geografiya | География | G5-11 | |
| Combined Science | Science / Tabiiy fanlar / Естествознание | Естествознание | G5-6 | Transitional combined science before split |
| Astronomy | Astronomiya | Астраномия | G11 only | |

**What this family teaches:** How natural systems work. Every concept in Tabiat Fanlari is either (a) an observation about the natural world, (b) a classification system for organizing observations, or (c) a causal model explaining why a system behaves as it does. The family builds scientific thinking: observe → classify → hypothesize → explain → predict.

**Cognitive demands:**
- Concept model construction (how systems work: photosynthesis, water cycle, plate tectonics)
- Classification and taxonomy (organism groups, rock types, climate zones)
- Diagram interpretation and labeling (cell structure, ecosystems, maps)
- Observation and hypothesis formation
- Cause-effect chains (why does this happen? because of X → why X? because of Y)
- Critical thinking about natural phenomena (evaluate claims, identify variables)
- Data interpretation from scientific visualizations (graphs, cross-sections, satellite imagery)

**Pedagogical principles (best practices):**

1. **Discovery narrative framing** — every concept is introduced as a problem someone faced and solved. "Scientists noticed that fossils of the same species appeared on continents now separated by oceans. How could this be?" This matches the historiographic arc and makes abstract classification feel like detective work.

2. **Concrete-to-abstract progression (CPA adapted)** — physical/pictorial examples first (a real leaf, a photograph of a volcano, a map), then classification systems (plant vs. animal, igneous vs. sedimentary, tropical vs. temperate), then abstract models (chemical equations for photosynthesis, climate zone formulas).

3. **Uzbek-context anchoring** — every concept is introduced via a familiar local example: the Aral Sea for environmental science, local ecosystems for biology, Central Asian geography for climate studies. Abstract global examples follow only after the local case is understood.

4. **Diagram as first-class representation** — unlike Aniq Fanlar (where formulas dominate), Tabiat Fanlari uses diagrams as the primary representational format. Students must be able to read, label, interpret, and eventually produce diagrams. Notebook Capture for hand-drawn diagrams is heavily emphasized.

5. **Cross-referencing with Aniq Fanlar** — when a Tabiat concept requires quantitative reasoning (e.g., population growth rates, chemical equations in biology), it explicitly references the relevant Aniq Fanlar concept. The boundary between families is permeable for student learning.

**Mechanic emphasis (primary):**
- Diagram Labeling (Notebook Capture — draw and annotate by hand)
- Memory Palace (organism classification, geographic features, geological periods)
- Story Mode (discovery narrative: "here is the problem this scientist faced")
- Tile Match (classification sorting, ecosystem assembly)
- Speed Match (species/feature pair recognition)

**Mechanic emphasis (secondary):**
- Why Chain (causal chains: 2-level for G5, 3-level for G6+)
- Adaptive Quiz
- Observation tasks with photograph analysis

**Boss format:**
- Explanation task — "describe the process" or "explain why" — evaluated by Tier 2 LLM
- G5 Boss: may include diagram labeling via Notebook Capture (photograph hand-drawn diagram)
- G6+ Boss: multi-part explanation requiring causal chain ("A causes B because... B causes C because...")
- Partial credit for identifying correct components even if full causal chain is incomplete

---

### Family 4: Ijtimoiy Fanlari — Social Sciences

**Uzbek gloss:** "Ijtimoiy" = social

**Subjects in this family:**

| Subject | UZ Name | RU Name | Grade Range | Notes |
|---------|---------|---------|-------------|-------|
| History (World) | Jahon tarixi | Всемирная история | G7-11 | Splits from unified Tarix at G7 |
| History (Uzbekistan) | O'zbekiston tarixi | История Узбекистана | G7-11 | Splits from unified Tarix at G7 |
| History (Ancient) | Tarix Qadimgi Dunyo / Tarix | История | G5-6 | Unified history before split |
| Law | Huquq | Право | G8-11 | |
| Economy | Iqtisodiy bilim asoslari / Iqtisodiyot | Экономика | G8-11 | |
| Entrepreneurship | Tadbirkorlik | Основы предпринимательства | G11 only | |
| Civic Prep | CHQBT (G10 UZ) / NВП (G10-11 RU) | Основы пред. / НВП | G10-11 | Military/civic preparation |

**What this family teaches:** How human systems work — institutions, events, laws, economies, and the reasoning required to navigate them. Unlike Aniq Fanlar (where answers are derivable) or Tabiat Fanlari (where answers are observable), Ijtimoiy Fanlari deals with interpretive truth: multiple valid perspectives, source reliability, and principled reasoning under uncertainty.

**Cognitive demands:**
- Concept understanding (what is this institution/event/principle?)
- Primary and secondary source analysis (who wrote this? when? why? for whom?)
- Critical thinking — evaluate a claim against evidence
- Case reasoning — apply a principle to a novel situation
- Chronological and causal modeling (what happened first? what caused what?)
- Perspective-taking (how would different people view this event?)
- Institutional reasoning (how do laws, economies, and governments function?)

**Pedagogical principles (best practices):**

1. **Historical narrative arc** — all events are introduced through a human narrative before abstraction. "In 1991, a 15-year-old in Tashkent watched the flags change on government buildings. What did that moment mean?" This matches the Problem → Struggle → Discovery → Resolution Story Mode structure and makes history feel like lived experience, not a list of dates.

2. **Source comparison as core skill** — students are given two or more short texts about the same event from different perspectives and asked to identify agreements, disagreements, and what each source reveals. This is the fundamental critical thinking skill of the family.

3. **Principle-before-case, then case-reinforces-principle** — legal and economic principles are introduced via an Uzbek everyday scenario before formal definition. "If you sell homemade bread at the bazaar, what rules apply to you?" → then the formal legal/economic concept.

4. **Chronological visualization** — timelines are the primary representational format for history. Students build, extend, and compare visual timelines before verbal description. Tile Match for timeline construction is a primary mechanic.

5. **Case reasoning for assessment** — rather than asking "what year did X happen?", Boss tasks ask "given this situation, what principle applies and why?" This tests transfer, not recall.

**Mechanic emphasis (primary):**
- Story Mode (historical narrative — Problem → Struggle → Discovery → Resolution)
- Memory Palace (chronological sequences, legislative structures, economic principles)
- Tile Match (timeline construction, cause-effect chain assembly)
- Source Comparison task (two short texts, student identifies agreement/disagreement)

**Mechanic emphasis (secondary):**
- Why Chain (3-level max: event → cause → deeper cause)
- Adaptive Quiz
- Boss as structured case-study debate

**Boss format:**
- Case reasoning task — "given this situation, what is the right principle to apply and why?" — evaluated by Tier 2 LLM against rubric
- History Boss may include a short primary source excerpt for source analysis
- Law/Economy Boss: "Here is a scenario. Which law/principle applies? What would be the outcome?"
- No multiple-choice for G6+

---

### Family 5: Tarbiya / Sanat — Soft & Formative

**Uzbek gloss:** "Tarbiya" = upbringing, character formation; "Sanat" = art

**Subjects in this family:**

| Subject | UZ Name | RU Name | Grade Range | Notes |
|---------|---------|---------|-------------|-------|
| Character Education | Tarbiya | Воспитание | G5-11 | |
| Music | Musiqa | Музыка | G5-9 | |
| Visual Art | Tasviriy san'at | ИЗО | G5-9 | |
| Technology | Texnologiya | Технология | G5-11 | Practical skills, crafts, digital literacy |
| Physical Education | Jismoniy tarbiya | Физкультура | All grades | **EXCLUDED from Library content** — no video lessons. Note: Movement Break mechanics remain mandatory in all family sessions for Grades 1-4 per UNIFIED spec §5. PE has no standalone Library content, but its mechanics are embedded in the session engine. |
| Drafting | Chizmachilik | Черчение | G8-9 only | Technical drawing |
| Spirituality | Ma'naviyat asoslari | — | G5-10 UZ only | No RU equivalent |
| Future Hour | kelajak soati / час будущего | час будущего | All grades | Career awareness, future skills |

**What this family teaches:** Expression, appreciation, and formation — not derivation or analysis. The cognitive demand is fundamentally different: students are not proving theorems or analyzing sources; they are creating, responding, moving, and reflecting. The family intentionally uses minimal gamification because over-gamifying character education or physical education produces the extrinsic-reward plateau problem documented in developmental psychology research.

**Cognitive demands:**
- Engagement and sustained attention
- Expressive output (visual, musical, physical, verbal)
- Character formation (empathy, responsibility, cooperation)
- Aesthetic appreciation (recognizing quality, understanding style)
- Physical skill development (coordination, technique)
- Emotional literacy (identifying and articulating feelings)
- Career awareness (what exists in the world of work?)

**Pedagogical principles (best practices):**

1. **Low-stakes creative expression** — tasks are intentionally lightweight. A drawing exercise, a described emotional response, a movement demonstration. There is no "wrong answer" in the sense of Aniq Fanlar. Feedback is encouraging and descriptive, not evaluative.

2. **Minimal gamification** — no Boss in the standard sense. Optional formative prompts ("share one thing you created this week") receive encouraging responses only. No scoring, no rubric-based evaluation. This is a deliberate architectural constraint to avoid the extrinsic-reward plateau.

3. **Process over product** — the value is in the act of creating, not the quality of the output. A student who draws a simple house with genuine engagement has achieved more than a student who copies a masterpiece mechanically.

4. **Cultural anchoring** — art, music, and technology tasks reference Uzbek cultural heritage: traditional patterns, folk music, local crafts, regional architecture. This makes the family a natural home for the Bilim Bazasi metagame's cultural aesthetic.

5. **Career awareness integration** — "kelajak soati" (Future Hour) introduces students to the world of work: what jobs exist, what skills they require, what a day in that job looks like. This is the family's most practically useful output and bridges to the cross-subject courses (IT, AI Literacy, Economy).

**Mechanic emphasis:**
- Reflection Journal (written or drawn response)
- Movement Breaks (physical activity for PE)
- Expressive output prompts ("draw," "describe," "respond")
- Creative Lab (open-ended creation with light constraints)

**Mechanic emphasis (secondary):**
- Memory Palace (for cultural knowledge, traditional patterns)
- Story Mode (for historical art/music context, career narratives)

**Boss format:**
- Optional formative prompt only — "share one thing you created this week"
- Encouraging response, no scoring
- No rubric-based evaluation
- No contribution to PISA progression or session pass/fail

---

### Family Summary Table

| Family | Subject Count | Cognitive Core | Primary Boss Format | PISA Relevance |
|--------|--------------|----------------|-------------------|----------------|
| Aniq Fanlar | 8 (with splits) | Formal reasoning, derivation | Open derivation problem | Math, Science |
| Til Fanlari | 5 | Language acquisition, production | Writing production (LLM-graded) | Reading |
| Tabiat Fanlari | 4 | System modeling, causal explanation | Explanation task (LLM-graded) | Science |
| Ijtimoiy Fanlari | 7 (with splits) | Interpretive reasoning, source analysis | Case reasoning (LLM-graded) | Reading (extended) |
| Tarbiya/Sanat | 8 | Expression, formation, appreciation | None (optional formative) | N/A |

---

### Research Gaps — What We Need to Fill

These slots are **empty pending research** and marked for later insertion:

| Gap | Where It Goes | Research Needed |
|-----|--------------|-----------------|
| DTM exam specs per subject | Each family's "Paths" section | Part 1 of Gemini brief |
| Olympiad topic lists per subject | Each family's "Paths" section | Part 3 of Gemini brief |
| International cert specs (IELTS, etc.) | Til Fanlari "Paths" section | Part 2 of Gemini brief |
| Lyceum/advanced curriculum topics | Each family's "Levels" section | Part 3 of Gemini brief |
| Competitor pricing & course inventory | Cross-Subject Courses section | Part 4 of Gemini brief |
| Employer/university skills gap data | Placement Suggestions section | Part 6 of Gemini brief |

---

*End of Part 1: Subject Family Classifications*
*Next: Part 2 — Universal Level System*

---

## Part 2: Universal Level System

### What Levels Are

Every subject in NETS has a difficulty progression — a vertical axis from "what the textbook teaches" to "what experts compete for." Levels define **how hard** the content is, independent of **what path** the student is on. A student on the Standard Path and a student on the DTM Path both encounter Level 1 and Level 2 content; they diverge at Level 3+.

This system applies uniformly across all five families. What changes per family is the **content** at each level, not the **definition** of the level.

### The 4-Level Model

| Level | Name | What It Means | Who Gets It | Source |
|-------|------|-------------|------------|--------|
| **L1** | Textbook Canon | Exactly what the national curriculum requires. Every student must master this. | All students (Basic) | Uzbek textbook |
| **L2** | Extended Textbook | Same topics as L1 but deeper: harder problems, more connections, cross-chapter synthesis. | Opt-in (Premium) | NETS-authored extensions |
| **L3** | Exam Prep | Topics and difficulty targeting a specific external exam: DTM, IELTS, Olympiad qualifiers. | Opt-in (Premium) | Exam specifications |
| **L4** | Expert | Beyond any exam: Olympiad medal level, university freshman content, original problem creation. | Opt-in (Premium) | International competition standards |

### Level Definitions Per Family

**Source for L2 "Lyceum Delta" topics across all families:** Extended topics at L2 are drawn from Gemini's research in `Lyceum_Detailed_Curricula.md`, covering 4 lyceum tracks (Engineering, Medical, Humanities, Foreign Philology) with per-subject delta topics and credit-module system. Content authors should cross-reference that document for verified topic lists before authoring L2 content.

#### Aniq Fanlar — Level Breakdown

| Level | Content Profile | Example (Math) | Example (Physics) | PISA Level |
|-------|----------------|----------------|-------------------|------------|
| **L1** | National curriculum topics, standard difficulty | Solve 2x + 5 = 13 | Calculate F = ma given all values | L2-3 |
| **L2** | Lyceum "Delta" topics: set theory, complex numbers, calculus intro, rigid body dynamics, Kirchhoff's Laws, organic mechanisms, Hardy-Weinberg, constitutional law analysis | Solve systems of 3 equations; intro to limits and derivatives; complex number operations | Multi-force problems with friction; moments of inertia; Kirchhoff's Laws for complex circuits; Carnot cycle efficiency | L3-4 |
| **L3** | DTM exam topics + harder variants; Olympiad regional level | Quadratic inequalities, function transformations, sequence proofs | Conservation of energy with non-trivial setups; circuit analysis with Kirchhoff; RLC circuits | L4-5 |
| **L4** | National Olympiad finals, IMO/Physics Olympiad qualifying level | Combinatorics proofs, number theory (Fermat/Euler), advanced geometry (Menelaus/Ceva), AM-GM inequalities | Lagrangian mechanics intro, statistical mechanics (Maxwell distribution), Biot-Savart/Lorentz force, Young's double-slit | L5-6 |

**L1 → L2 transition skill examples (Aniq Fanlar):**
- L1→L2: multi-step algebraic manipulation; extract data from word problems before solving
- L2→L3: model unfamiliar situations mathematically; select appropriate problem-solving strategy
- L3→L4: construct proofs; generalize patterns; link multiple representations

#### Til Fanlari — Level Breakdown

| Level | Content Profile | Example (English) | Example (Literature) | CEFR Equivalent |
|-------|----------------|-------------------|---------------------|-----------------|
| **L1** | National curriculum vocabulary and grammar; basic reading comprehension | Present simple vs. continuous exercises; 200-word reading passage with literal questions | Identify main idea and character traits in a short story | A1-A2 |
| **L2** | Extended vocabulary; complex grammar in context; inference questions; shift to Academic English (EAP) for lyceum | Past perfect continuous; 500-word passage requiring inference and opinion | Compare two characters' motivations; identify author's purpose; basic literary analysis | B1 |
| **L3** | IELTS/TOEFL prep; academic writing; timed reading; linguistics and translation theory intro | IELTS Task 2 essay (opinion); 800-word academic passage with detail + inference questions | Analyze literary devices; contextualize work historically | B2 |
| **L4** | Advanced academic English; C1-C2 level composition; critical literary theory; literature analysis in target language | IELTS Band 8+ writing; nuanced argumentation; synthesis of multiple sources | Evaluate competing critical interpretations; write original analysis with textual evidence | C1-C2 |

**L1 → L2 transition skill examples (Til Fanlari):**
- L1→L2: infer meaning from context; produce multi-sentence coherent paragraphs
- L2→L3: write under time pressure; analyze implicit meaning in texts
- L3→L4: synthesize multiple sources; produce academically appropriate register

#### Tabiat Fanlari — Level Breakdown

| Level | Content Profile | Example (Biology) | Example (Geography) | PISA Level |
|-------|----------------|-------------------|---------------------|------------|
| **L1** | Organism identification, basic system descriptions, diagram labeling | Label parts of a cell; describe photosynthesis in 2-3 sentences | Identify climate zones on a map; name rock types | L2 |
| **L2** | Lyceum Delta: ATP synthesis, Krebs cycle, photosynthesis light/dark phases, Hardy-Weinberg intro, linked inheritance, epistasis, PCR basics | Explain how enzymes work; interpret a population growth graph | Explain monsoon formation; analyze a topographic map cross-section | L3 |
| **L3** | Molecular-level mechanisms, experimental design, multi-variable analysis | Describe DNA replication steps; design an experiment to test enzyme activity | Analyze satellite imagery for land-use change; model plate boundary interactions | L4 |
| **L4** | Research-level problem solving; genetic calculations; advanced ecological modeling | Solve Punnett squares for multi-gene inheritance with epistasis; analyze epidemiological data | Model climate change scenarios using real data; evaluate competing geological theories | L5-6 |

#### Ijtimoiy Fanlari — Level Breakdown

| Level | Content Profile | Example (History) | Example (Law) | PISA Level |
|-------|----------------|-------------------|---------------|------------|
| **L1** | Event recall, date matching, basic cause identification | "When did the Silk Road begin?" "Name one cause of WWII" | "What is a constitution?" | L2 |
| **L2** | Lyceum Delta: historiography intro, source criticism, 2023 Constitution analysis, Cold War deep study, criminology basics | "Compare how two historians describe this event" | "Given this dispute between neighbors, which civil code article applies?"; Constitutional Law detailed analysis | L3 |
| **L3** | Historiographical analysis, constitutional reasoning, economic modeling | "Evaluate the reliability of a primary source given its author's position" | "Analyze whether this law violates constitutional principle X" | L4 |
| **L4** | Original historical argument construction; legal brief writing; policy analysis | "Construct a thesis about why this civilization declined, using 4+ sources" | "Draft a legal argument for a novel case using precedent" | L5-6 |

#### Tarbiya/Sanat — Level Breakdown

| Level | Content Profile | Notes |
|-------|----------------|-------|
| **L1** | Basic creative tasks, skill practice, cultural knowledge | "Draw a pattern using traditional motifs" |
| **L2** | Structured creative projects with constraints | "Create a composition using 3 traditional elements and 1 original element" |
| **L3** | Independent creative work with reflection | "Create an original piece and write 3 sentences about your creative choices" |
| **L4** | N/A — this family intentionally caps at L3 | Formative subjects do not benefit from competitive pressure |

### Level Progression Rules

1. **L1 is mandatory** — every student encounters L1 content for their grade. This is the Basic tier guarantee.
2. **L2 requires L1 mastery** — a student must demonstrate ≥80% success on L1 before L2 content is offered. Rationale: the UNIFIED spec targets 70-80% success for flow state. A student at 70% on L1 is at the *floor* of flow — pushing them to harder L2 content would drop them below flow state into frustration. The ≥80% threshold ensures headroom: the student is comfortably in flow on L1 and ready for a step up.
3. **L3 requires path enrollment** — a student must be on an exam prep path (DTM, IELTS, Olympiad) to encounter L3 content.
4. **L4 requires L3 performance** — a student must demonstrate ≥80% success on L3 content before L4 is offered.
5. **Levels are per-subject, not per-student** — a student can be L2 in Math, L1 in Biology, and L3 in English simultaneously.

### Level Indicators (What the Student Sees)

**Levels are never labeled with numbers in the UI.** The 10-year-old does not see "Level 3 Physics." Instead:

| Internal Level | Student-Facing Label | Visual Metaphor |
|---------------|---------------------|-----------------|
| L1 | (no label — default) | Standard task appearance |
| L2 | "Chuqurroq" (Deeper) | Slightly more ornate frame |
| L3 | "Ustoz yo'li" (Master's path) | Distinctive badge icon |
| L4 | "Chempion" (Champion) | Gold border, rare |

**Design note:** L3 was originally labeled "Sinovga tayyorlan" (Test prep) but this violates SOUL Principle 3 — difficulty must be hidden from the student. Labeling content as "test prep" makes difficulty visible and creates anxiety. "Ustoz yo'li" (Master's path) is aspirational and neutral, consistent with the hidden-difficulty constraint.

---

*End of Part 2: Universal Level System*
*Next: Part 3 — Path System*

---

## Part 3: Path System

### What Paths Are

Paths are the **horizontal axis** of the library. Levels (Part 2) define *how hard* the content is. Paths define *why* the student is learning it — what goal the content serves. A path selects which levels to encounter, in what order, with what emphasis.

Every path is a curated sequence of content items drawn from the level system. Paths can share content: the Standard Path and DTM Path both use L1 content; they diverge at L2+ where DTM pulls exam-specific topics.

### The 5 Universal Paths

| Path | Code | Who It's For | Levels Used | Goal |
|------|------|-------------|-------------|------|
| **Standard** | `STD` | All students, all grades | L1 (mandatory), L2 (optional) | Master national curriculum, reach PISA L2-3 |
| **DTM / University Entrance** | `DTM` | G9-11 targeting university | L1, L2, L3 | Score ≥68.0 on BBA entrance exam (state grant threshold) |
| **Olympiad** | `OLY` | Top performers, G5-11 | L1, L2, L3, L4 | Win at regional/national Olympiad; international competition |
| **International Certification** | `CERT` | Language students, G7-11 | L1, L2, L3, L4 | Achieve target cert score (IELTS 6.5+, CEFR B2+, TORFL B2) |
| **PISA Excellence** | `PISA` | High-performers, G5-11 | L2, L3, L4 | Reach PISA Level 4-6; international benchmark competitiveness |

### Path Definitions Per Family

#### Aniq Fanlar — Paths

**Standard Path (STD):**
- Follows the national curriculum chapter-by-chapter
- Covers all textbook topics at L1 difficulty
- Boss format: open derivation problems matching textbook complexity
- Target: pass school year with strong grades, reach PISA L2-3
- Available to all students (Basic tier)

**DTM Path (DTM):**
- Target: BBA entrance exam, 180 min, 90 MCQs, 189 points
- Content pulls from L1 (mandatory block topics), L2 (harder variants), L3 (specialty block)
- Topic weight follows DTM specification:
  - Math: Algebra 65%, Geometry 35%
  - Physics: Mechanics 30%, Molecular/Thermo 20%, Electrodynamics/Optics 40%, Quantum 10%
  - Chemistry: General 35%, Inorganic 30%, Organic 35%
- Specialty block alignment: Math for Engineering/IT/Econ tracks; Physics for Engineering/IT; Chemistry for Medical/ChemTech
- Practice exams use DTM format: MCQ, 4 options (A/B/C/D), timed per block
- Target score: ≥68.0 (state grant), ≥56.7 (tuition-based minimum)

**Olympiad Path (OLY):**
- 4-stage progression: School → District → Regional → National
- National winners get direct university admission (no exam)
- Content at L3-L4 difficulty, aligned with international Olympiad standards:
  - **Math (IMO):**
    - Algebra: Vieta's formulas, AM-GM/Cauchy-Schwarz/Jensen inequalities, functional equations, recursive sequences, limits
    - Geometry: Triangle centers, cyclic quadrilaterals, Power of a Point, Menelaus/Ceva theorems, homothety, spatial geometry
    - Number Theory: Euclidean algorithm, Fermat's Little Theorem, Euler's Totient Theorem, Chinese Remainder Theorem, Diophantine equations (linear, Pell's basics)
    - Combinatorics: Inclusion-Exclusion, Stars and Bars, graph theory (trees, Eulerian/Hamiltonian paths, planar graphs), Pigeonhole/Extremal/Invariance principles
  - **Physics (IPhO):**
    - Mechanics: Rigid body dynamics (torque, moments of inertia), fluid mechanics (Bernoulli, viscosity), conservation laws, elastic/inelastic collisions
    - Thermodynamics: MKT, Maxwell distribution, entropy, Carnot cycle, adiabatic processes
    - Electromagnetism: Gauss's Law, Kirchhoff's Laws (complex circuits), RLC circuits, Lorentz force, Biot-Savart, Faraday/Lenz induction
    - Optics: Snell's Law, thin lens, Young's double-slit interference, diffraction, polarization
    - Modern: Photoelectric effect, Compton scattering, Bohr model, nuclear binding energy
  - **Chemistry (IChO):**
    - Physical: Quantum numbers, VSEPR/hybridization, Gibbs free energy, rate laws, Kp/Kc equilibrium, Ksp
    - Inorganic: Periodic trends, s/p-block compounds, d-block coordination chemistry (ligands, isomerism, crystal field theory)
    - Organic: Stereoisomerism, SN1/SN2/E1/E2 mechanisms, electrophilic addition, carbonyl/acid/amine chemistry, polymerization
    - Analytical: Flame tests, precipitation, volumetric titrations (acid-base, redox, complexometric)
  - **Biology (IBO):**
    - Cytology: Prokaryotic/eukaryotic structure, membrane transport, glycolysis/Krebs/oxidative phosphorylation, photosynthesis (light/dark), mitosis/meiosis checkpoints
    - Genetics: Mendelian laws, pedigrees, linkage mapping, Hardy-Weinberg population genetics, epistasis, linked inheritance
    - Molecular Biology: Central Dogma (replication/transcription/translation), gene regulation, PCR, cloning basics, CRISPR-Cas9
    - Anatomy: Nephron function, action potentials, heart structure, xylem/phloem transport, plant hormones
    - Biochemistry: Macromolecule structure, Michaelis-Menten enzyme kinetics, metabolic pathway interconnectivity
  - **Informatics (IOI):**
    - Graph algorithms (shortest path, MST, DAG), dynamic programming, tree structures, competitive programming via Robocontest.uz platform
- International tracks: IMO, IPhO, IChO, IBO, IOI
- Boss format: Olympiad-style proof/construction problems, time-extended sessions
- Official portals: olympiad.uzedu.uz, piima.uz, robocontest.uz, idum.uz, bilimlar.uz

**PISA Excellence Path (PISA):**
- Targets PISA Math L4-6 (score 482+)
- Content emphasizes: complex modeling, multi-representation integration, reflection on results
- Boss format: open-ended reasoning with real-world context (PISA item style)
- Cross-references real PISA items and OECD framework descriptors

#### Til Fanlari — Paths

**Standard Path (STD):**
- National curriculum vocabulary, grammar, reading comprehension
- L1-L2 difficulty, A1-B1 CEFR equivalent for foreign languages
- Boss: writing production (sentences → paragraphs), literature analysis
- Target: pass school year, functional communication

**DTM Path (DTM):**
- For Uzbek/Russian native language and Literature subjects
- DTM format: MCQ, spelling, grammar parsing, literary knowledge
- L2-L3 difficulty: high-speed test patterns, stylistic analysis
- Ona tili DTM topics: orthography (X/H rules), morphology (12 parts of speech), syntax, literary works (Navoi, Babur)

**International Certification Path (CERT):**
- **IELTS Track (English):**
  - L1 = A1-A2 (school curriculum)
  - L2 = B1 (extended vocabulary, inference)
  - L3 = B2 (IELTS 5.5-6.5): Task 1 reports, Task 2 essays, academic reading, Speaking Parts 1-3
  - L4 = C1-C2 (IELTS 7.0-9.0): advanced argumentation, synthesis, creative/academic writing
  - Practice tests mirror IELTS structure: Listening (40 Q, 40 min), Reading (40 Q, 60 min), Writing (2 tasks, 60 min), Speaking (3 parts, 11-14 min)
  - Writing scored against 4 criteria (25% each): Task Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy
  - Speaking scored against: Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation
  - Target band: 6.5+ (university entrance), 7.0+ (teacher salary bonus: +50%)
- **TOEFL iBT Track (English):**
  - Adaptive format, shorter test, US/STEM university focus
  - Alternative to IELTS for students targeting American universities
- **Cambridge FCE/CAE Track (English):**
  - Permanent qualification (unlike IELTS 2-year validity)
  - FCE = B2, CAE = C1. Highly valued for teacher certification in Uzbekistan
- **TORFL Track (Russian as foreign language):**
  - 5 parts: Grammar, Reading, Writing, Listening, Speaking
  - B2 required for Master's admission in Russian universities
  - Alternative for students whose target is Russian-language higher education

**PISA Excellence Path (PISA):**
- Targets PISA Reading L4-6
- Content: multi-source integration, nuance interpretation, credibility evaluation
- Boss: extended textual analysis with competing sources

#### Tabiat Fanlari — Paths

**Standard Path (STD):**
- National curriculum: organism identification → system descriptions → process explanations
- L1-L2 difficulty, PISA Science L2-3 target
- Boss: explanation tasks, diagram labeling

**DTM Path (DTM):**
- Biology DTM topic weights: General Bio 35%, Anatomy 25%, Zoology 20%, Botany 20%
- Chemistry DTM topic weights: General 35%, Inorganic 30%, Organic 35%
- L1-L3 difficulty, MCQ practice format
- Specialty block for Medical direction (Biology primary + Chemistry secondary)

**Olympiad Path (OLY):**
- Biology: IBO syllabus — population genetics (Hardy-Weinberg), bioinformatics, CRISPR-Cas9, PCR, advanced experimental design
- Chemistry: IChO syllabus — multistep synthesis, spectroscopy, kinetics, crystal field theory
- Geography: spatial analysis, satellite imagery interpretation, climate modeling
- L3-L4 difficulty

**PISA Excellence Path (PISA):**
- Targets PISA Science L4-6
- Content: data interpretation from complex graphs, experimental design, multi-variable analysis
- Boss: open scientific reasoning problems

#### Ijtimoiy Fanlari — Paths

**Standard Path (STD):**
- National curriculum: event knowledge, basic cause identification, institutional concepts
- L1-L2 difficulty
- Boss: source comparison, principled reasoning

**DTM Path (DTM):**
- History DTM topic weights: Uzbekistan History 60%, World History 40%
- L2-L3 difficulty: source analysis, multi-cause reasoning
- Specialty block for Law direction (History primary + Foreign Language secondary)
- Law DTM: constitutional concepts, civil code basics, human rights framework

**Olympiad Path (OLY):**
- History: comparative history, historiographical analysis (Annales vs. Marxist vs. Liberal)
- Law: constitutional reasoning, legal brief construction
- Economy: macroeconomic modeling, policy analysis
- L3-L4 difficulty

**PISA Excellence Path (PISA):**
- Extended Reading framework applied to social science texts
- Targets L4-6: evaluate credibility, synthesize diverse sources, construct novel interpretations

#### Tarbiya/Sanat — Paths

**Standard Path (STD) only:**
- This family does not have DTM, Olympiad, or Certification paths
- Creative expression, skill practice, cultural knowledge
- L1-L3 only (no L4 — intentionally capped)
- No exam preparation, no competitive tracks

### Path Enrollment Rules

1. **Standard Path is automatic** — every student is enrolled from day one
2. **DTM Path opens at G9** — before G9, the curriculum does not cover DTM specialty subjects
3. **Olympiad Path requires qualification** — student must demonstrate ≥80% success on L2 content in the subject
4. **Certification Path requires readiness assessment** — a short diagnostic test places the student at the correct CEFR level before starting
5. **PISA Path requires teacher recommendation or self-enroll at G7+** — prevents anxiety from premature exposure to high-difficulty content
6. **Multiple paths can be active simultaneously** — a G11 student can be on STD (Math) + DTM (Biology+Chemistry for Medical track) + CERT (English IELTS) at the same time. **UX implication:** The Library surface must handle multi-path students cleanly. Suggested approach: the Library shows the student's active paths as filter tabs (e.g., "Barcha" / "DTM" / "IELTS"), with content items tagged to relevant paths. The Today surface shows the *highest-priority* path's next session. Path priority: DTM > CERT > OLY > PISA > STD (by deadline urgency). Detailed UX spec deferred to the product/UX team.

### Path-to-DTM Specialty Mapping

This table maps every university direction to the paths students should enroll in:

| University Direction | Path(s) | Specialty 1 (3.1 pts) | Specialty 2 (2.1 pts) |
|---------------------|---------|----------------------|----------------------|
| Medical | STD all + DTM Bio+Chem | Biology | Chemistry |
| Engineering | STD all + DTM Math+Phys | Mathematics | Physics |
| Law | STD all + DTM Hist+Lang | History | Foreign Language |
| Economics/Finance | STD all + DTM Math+Lang | Mathematics | Foreign Language |
| IT/CS | STD all + DTM Math+Phys | Mathematics | Physics (or Foreign Lang) |
| Chemical Technology | STD all + DTM Chem+Math | Chemistry | Mathematics |
| Agriculture | STD all + DTM Bio+Chem | Biology | Chemistry |

**Strategic note:** Students on the CERT path who achieve B2 (IELTS 5.5+) receive automatic maximum points (63.0) for the Foreign Language block — this is a massive strategic advantage for Law, Economics, and IT tracks. *(Source: Gemini research — `DTM_Exam_Specs.md`. Content authors should verify against current DTM regulations before surfacing this claim to students, as exam policies may change between academic years.)*

---

*End of Part 3: Path System*
*Next: Part 4 — Cross-Subject Courses*

---

## Part 4: Cross-Subject Courses

### What Cross-Subject Courses Are

Cross-subject courses do not belong to a single textbook subject. They draw content from multiple families, synthesize skills across domains, and target real-world competencies that the national curriculum does not explicitly teach. They are the **premium differentiators** — the "why pay for Premium" content layer.

Each course maps to at least one employer-identified skills gap and at least one 2030 strategic target.

### The 16 Cross-Subject Courses

#### Course 1: Critical Thinking

| Field | Value |
|-------|-------|
| **Code** | `CSC-001` |
| **Family** | Cross-cutting (draws from Ijtimoiy + Aniq + Til) |
| **Grades** | G6-G11 |
| **Levels** | L1 (G6-7), L2 (G8-9), L3 (G10-11) |
| **Skills gap addressed** | #1 employer deficit — only 19% reach basic math modeling proficiency (PISA 2022) |
| **Content** | Socratic inquiry, logical fallacy detection, cognitive bias identification, news/media literacy, argument structure analysis, evidence evaluation |
| **Mechanics** | Source Comparison (Ijtimoiy), Error Analysis (Aniq), Cloze/Sentence Fill (Til), Why Chain |
| **Boss format** | Case analysis: "Here is a claim with supporting evidence. Identify the fallacies, evaluate the evidence quality, and state whether the claim is justified." |
| **Research sources** | Foundation for Critical Thinking, SHEG Stanford (Reading Like a Historian) |

#### Course 2: Academic Writing

| Field | Value |
|-------|-------|
| **Code** | `CSC-002` |
| **Family** | Til Fanlari (extended) |
| **Grades** | G9-G11 |
| **Levels** | L3 (IELTS Band 6-7), L4 (Band 7-9) |
| **Skills gap addressed** | English proficiency — #1 technical hiring barrier (49% of employers) |
| **Content** | IELTS Task 1 reports (data description, process diagrams, maps), Task 2 essays (opinion, discussion, problem-solution), academic citations, research methods, paragraph coherence, thesis construction |
| **Mechanics** | Writing production (Boss as essay), Cloze/Sentence Fill (grammar refinement), Story Mode (model essays as narratives) |
| **Boss format** | Timed essay writing (40 min), evaluated by Tier 2 LLM against IELTS 4-criterion rubric |
| **Research sources** | Purdue OWL, British Council Uzbekistan, IELTS official band descriptors |

#### Course 3: Debate & Rhetoric

| Field | Value |
|-------|-------|
| **Code** | `CSC-003` |
| **Family** | Til Fanlari + Ijtimoiy Fanlari |
| **Grades** | G7-G11 |
| **Levels** | L1 (introductory), L2 (structured), L3 (competitive) |
| **Skills gap addressed** | Communication & socio-emotional skills — #1 missing attribute in entry-level hires |
| **Content** | Logical fallacy recognition (cross-ref Critical Thinking), Parliamentary debate format, Lincoln-Douglas format, World Schools format, constructive speech writing, rebuttal techniques, evidence-based argumentation |
| **Mechanics** | Dialogue exercises, Story Mode (historical speeches as models), Reflection Journal |
| **Boss format** | "Here is a motion. Write a 3-minute constructive speech with 3 arguments and anticipated rebuttals." Evaluated by Tier 2 LLM for structure, evidence quality, and rhetorical technique. |
| **Research sources** | World Schools Debate, Lincoln-Douglas format guides |

#### Course 4: Financial Literacy

| Field | Value |
|-------|-------|
| **Code** | `CSC-004` |
| **Family** | Ijtimoiy Fanlari (extended) + Aniq Fanlari (quantitative) |
| **Grades** | G5-G11 |
| **Levels** | L1 (G5-7: saving, budgeting), L2 (G8-9: banking, interest), L3 (G10-11: investing, risk) |
| **Skills gap addressed** | Economic literacy for 2030 targets; personal finance is absent from national curriculum |
| **Content** | G5-7: budgeting, saving, needs vs. wants, basic entrepreneurship concepts. G8-9: banking system, compound interest, loans, credit, basic risk management. G10-11: personal investing, inflation, taxation in Uzbekistan, retirement planning, cryptocurrency basics |
| **Mechanics** | Real-Life Challenge (Uzbek-context scenarios: "You earn 2M UZS/month. Plan your budget."), Adaptive Quiz, Story Mode |
| **Boss format** | Financial planning scenario: "Given this income, expenses, and financial goal, create a 6-month plan and justify your choices." |
| **Research sources** | Everfi K-12, Uzbekistan banking sector data |

#### Course 5: IT & Programming

| Field | Value |
|-------|-------|
| **Code** | `CSC-005` |
| **Family** | Aniq Fanlari (Informatics extended) |
| **Grades** | G7-G11 |
| **Levels** | L1 (G7-8: Python basics), L2 (G9: data structures), L3 (G10-11: web dev, algorithms), L4 (G11: competitive programming) |
| **Skills gap addressed** | IT literacy — "talent war" for software engineering, data analytics, AI (74% use AI without formal training) |
| **Content** | **L1 (G7-8): Python Fundamentals** — Variables, loops, functions, basic I/O, algorithmic thinking. Source: OMUC Introductory Stage (120 hrs).<br><br>**L2 (G9): Data Structures & Analysis** — Arrays, lists, dictionaries, stacks, queues, basic sorting/searching. Data Analysis track intro: SQL basics (Joins, Aggregations, Subqueries), NumPy/Pandas for 1D/2D data, descriptive statistics, Matplotlib/Seaborn visualization. Source: OMUC Data Analysis Nanodegree.<br><br>**L3 (G10-11): Specialization Tracks** —<br>• *Front-End:* HTML5, CSS3, JS (ES6+), Flexbox/Grid, Bootstrap, jQuery, DOM manipulation, async JS (fetch API), React.js intro. Source: OMUC Front-End Nanodegree.<br>• *Back-End:* Python 3, Flask, PostgreSQL, SQLAlchemy (ORM), RESTful API design, JWT/Auth0 auth, Docker deployment to AWS. Source: OMUC Full-Stack Nanodegree.<br>• *Android:* Kotlin, Android Studio, Jetpack (Navigation, Room, ViewModel), Retrofit for APIs. Source: OMUC Android Nanodegree.<br>• *Game Dev:* Unity + C#, Unreal Engine 5 + C++, Blender 3D modeling intro. Source: IT Park GameDevHQ/Xsolla Academy.<br>• *Cybersecurity:* Python, Linux (Kali/Ubuntu), Wireshark, Metasploit, network basics, SOC monitoring. Source: ITPU Cybersecurity program.<br><br>**L4 (G11): Competitive Programming** — Graph algorithms (shortest path, MST, DAG), dynamic programming, tree structures. Practice via Robocontest.uz platform. |
| **Mechanics** | Worked examples (code completion), Notebook Capture (pseudocode → code), Tile Match (syntax assembly), Error Analysis (bug fixing) |
| **Boss format** | Programming problem: "Write a program that solves X." Evaluated by automated test cases (not LLM — deterministic). |
| **Research sources** | One Million Uzbek Coders (Udacity) — 4 tracks with full Nanodegree syllabi, IT Park Academy/University (ITPU), Robocontest.uz, GameDevHQ/Xsolla Academy |

#### Course 6: AI Literacy & ML

| Field | Value |
|-------|-------|
| **Code** | `CSC-006` |
| **Family** | Aniq Fanlari (Informatics + Math cross-reference) |
| **Grades** | G10-G11 |
| **Levels** | L1 (concepts), L2 (applications), L3 (hands-on) |
| **Skills gap addressed** | AI integration capability — 74% of professionals use AI tools without strategic training |
| **Content** | L1: What is AI? Neural networks (conceptual), supervised vs. unsupervised learning, ethical AI, bias in ML, LLMs (how they work, limitations). L2: Training a simple model (conceptual), data labeling, evaluation metrics (accuracy, precision, recall), real-world AI applications in Uzbekistan. L3: Hands-on with no-code ML tools, prompt engineering, building a simple classifier |
| **Mechanics** | Story Mode (history of AI, from Turing to transformers), Tile Match (model architecture assembly), Real-Life Challenge (ethical dilemmas) |
| **Boss format** | Case analysis: "Given this dataset and this problem, which ML approach is most appropriate? Justify your choice and identify potential biases." |
| **Research sources** | Elements of AI, Khan Academy AI content |

#### Course 7: Medical School Prep

| Field | Value |
|-------|-------|
| **Code** | `CSC-007` |
| **Family** | Tabiat Fanlari (Biology + Chemistry extended) |
| **Grades** | G10-G11 |
| **Levels** | L3 (MCAT-lite), L4 (medical school freshman) |
| **Skills gap addressed** | Medical school entrance competitiveness; DTM Biology+Chemistry specialty depth |
| **Content** | Advanced anatomy (organ systems at tissue level), biochemistry (amino acids, enzyme kinetics, metabolic pathways), molecular biology (DNA replication, transcription, translation, gene regulation), cell biology (membrane transport, signaling, cell cycle), organic chemistry (reaction mechanisms, stereochemistry) |
| **Mechanics** | Diagram Labeling (anatomical structures, molecular pathways), Memory Palace (metabolic pathway sequences), Why Chain (biochemical causal chains) |
| **Boss format** | "Explain the complete process of X from molecular mechanism to organism-level effect." Evaluated by Tier 2 LLM against medical school rubric. |
| **Research sources** | Khan Academy MCAT prep, IBO syllabus |

#### Course 8: Environmental Science

| Field | Value |
|-------|-------|
| **Code** | `CSC-008` |
| **Family** | Tabiat Fanlari (Biology + Geography + Chemistry cross-reference) |
| **Grades** | G7-G11 |
| **Levels** | L1 (awareness), L2 (analysis), L3 (modeling) |
| **Skills gap addressed** | Uzbekistan 2030 sustainability targets; Aral Sea crisis understanding |
| **Content** | Climate systems and modeling, biodiversity and conservation, pollution and remediation, sustainability and resource management, Uzbekistan-specific environmental challenges (Aral Sea, water management, desertification), global climate agreements |
| **Mechanics** | Story Mode (environmental discovery narratives), Diagram Labeling (ecosystems, carbon cycle), Real-Life Challenge (Uzbek-context scenarios) |
| **Boss format** | "Analyze this environmental data set. Identify trends, causes, and propose evidence-based interventions." |
| **Research sources** | National Geographic Education, Aral Sea research |

#### Course 9: GIS & Cartography

| Field | Value |
|-------|-------|
| **Code** | `CSC-009` |
| **Family** | Tabiat Fanlari (Geography extended) + Aniq Fanlari (data science) |
| **Grades** | G8-G11 |
| **Levels** | L1 (map reading), L2 (spatial analysis), L3 (GIS software) |
| **Skills gap addressed** | Geospatial literacy for urban planning, agriculture, environmental management |
| **Content** | Map projections and coordinate systems, topographic map interpretation, satellite imagery analysis, GIS fundamentals (layers, queries, spatial joins), data visualization (heat maps, choropleth, 3D terrain), remote sensing basics |
| **Mechanics** | Diagram Labeling (map features), Tile Match (layer assembly), Real-Life Challenge (spatial problem scenarios) |
| **Boss format** | "Given these two data layers (e.g., population density + flood risk zones), identify the optimal locations for X and justify using spatial reasoning." |
| **Research sources** | Esri K-12 GIS curriculum |

#### Course 10: Law & Civic Rights

| Field | Value |
|-------|-------|
| **Code** | `CSC-010` |
| **Family** | Ijtimoiy Fanlari (Law extended) |
| **Grades** | G9-G11 |
| **Levels** | L1 (concepts), L2 (application), L3 (analysis) |
| **Skills gap addressed** | Civic literacy; constitutional awareness; DTM Law specialty preparation |
| **Content** | Constitutional law (Uzbekistan Constitution, rights and duties), human rights framework (UDHR, regional conventions), civil law basics (contracts, property, family law), criminal law fundamentals, administrative law, legal reasoning and case analysis, Uzbek court system |
| **Mechanics** | Story Mode (landmark legal cases as narratives), Source Comparison (competing legal interpretations), Case reasoning |
| **Boss format** | "Given this legal scenario, identify the applicable law, analyze both sides' arguments, and reach a justified conclusion." |
| **Research sources** | Amnesty Academy, Uzbekistan Constitution, civil code |

#### Course 11: Applied Economics

| Field | Value |
|-------|-------|
| **Code** | `CSC-011` |
| **Family** | Ijtimoiy Fanlari (Economy extended) |
| **Grades** | G10-G11 |
| **Levels** | L1 (personal), L2 (market), L3 (macro) |
| **Skills gap addressed** | Economic literacy for 2030 strategy; entrepreneurship skills |
| **Content** | Micro: supply and demand, market structures, pricing, consumer behavior. Macro: GDP, inflation, unemployment, monetary and fiscal policy, Uzbekistan's economy (transition from planned to market, key sectors: agriculture, textiles, mining, services). Entrepreneurship: business plans, market research, risk assessment, funding sources |
| **Mechanics** | Real-Life Challenge (Uzbek market scenarios), Adaptive Quiz (economic calculations), Why Chain (causal economic chains) |
| **Boss format** | "Analyze this economic situation. Identify the market failure (if any), propose policy interventions, and predict secondary effects." |
| **Research sources** | Marginal Revolution University, World Bank Uzbekistan reports |

#### Course 12: Historiography

| Field | Value |
|-------|-------|
| **Code** | `CSC-012` |
| **Family** | Ijtimoiy Fanlari (History extended) |
| **Grades** | G9-G11 |
| **Levels** | L2 (source analysis), L3 (comparative), L4 (methodological) |
| **Skills gap addressed** | Critical historical thinking; university-level humanities preparation |
| **Content** | Historiographical schools (Annales, Marxist, Liberal, Post-colonial), source criticism methods, archival research basics, comparative history (how different historians interpret the same event), Central Asian historiography (Silk Road, Timurid, Colonial, Soviet, Post-Soviet interpretations) |
| **Mechanics** | Source Comparison (primary mechanic), Story Mode (historiographical debates as narratives), Memory Palace (historiographical schools and their key figures) |
| **Boss format** | "Compare how three historians from different schools interpret Event X. What does each reveal? What does each obscure? Construct your own interpretation." |
| **Research sources** | SHEG Stanford, Central Asian historiography research |

#### Course 13: Creative Lab (Digital Art)

| Field | Value |
|-------|-------|
| **Code** | `CSC-013` |
| **Family** | Tarbiya/Sanat (Art extended) |
| **Grades** | G5-G11 |
| **Levels** | L1 (basics), L2 (composition), L3 (original creation) |
| **Skills gap addressed** | Digital creative skills for the modern economy |
| **Content** | Digital illustration fundamentals, color theory, composition and layout, UI/UX basics, 3D modeling introduction, Uzbek traditional patterns in digital form, portfolio building |
| **Mechanics** | Expressive output, Reflection Journal, Creative Lab |
| **Boss format** | "Create an original digital piece themed on X. Write 2-3 sentences about your creative choices." No scoring — encouraging feedback only. |
| **Completion gate** | Formative: student submits 3 creative pieces per level to advance. No rubric score — submission + reflection = completion. This ensures progress tracking without extrinsic evaluation pressure. |
| **Research sources** | Adobe Education Exchange |

#### Course 14: Music Production

| Field | Value |
|-------|-------|
| **Code** | `CSC-014` |
| **Family** | Tarbiya/Sanat (Music extended) |
| **Grades** | G7-G11 |
| **Levels** | L1 (basics), L2 (composition), L3 (production) |
| **Skills gap addressed** | Creative industry skills; cultural preservation through modern medium |
| **Content** | DAW basics (logic, rhythm, Ableton concepts), sound design fundamentals, MIDI and digital instruments, mixing and mastering basics, digital composition incorporating Uzbek traditional music elements |
| **Mechanics** | Expressive output, Movement Breaks (rhythm exercises), Reflection Journal |
| **Boss format** | "Create a 1-minute composition that blends traditional Uzbek musical elements with modern production. Describe your creative process." |
| **Completion gate** | Formative: student submits 3 compositions per level to advance. No rubric score — submission + reflection = completion. |
| **Research sources** | Berklee Pulse |

#### Course 15: Sports Science

| Field | Value |
|-------|-------|
| **Code** | `CSC-015` |
| **Family** | Tarbiya/Sanat (PE extended) + Tabiat Fanlari (Biology cross-reference) |
| **Grades** | G8-G11 |
| **Levels** | L1 (anatomy), L2 (physiology), L3 (application) |
| **Skills gap addressed** | Health literacy; athletic performance understanding |
| **Content** | Kinesiology (muscle groups, movement patterns, biomechanics), sports nutrition (macros, hydration, supplementation basics), exercise physiology (energy systems, training principles, recovery), injury prevention and first aid basics, sports psychology (motivation, goal-setting, visualization) |
| **Mechanics** | Real-Life Challenge (training plan scenarios), Diagram Labeling (anatomy, muscle groups), Why Chain (physiological causal chains) |
| **Boss format** | "Design a 4-week training plan for athlete X with goal Y. Justify your exercise selection, intensity progression, and nutrition recommendations." |
| **Research sources** | NSCA Education |

#### Course 16: Mathematical Logic

| Field | Value |
|-------|-------|
| **Code** | `CSC-016` |
| **Family** | Aniq Fanlari (Math + Informatics cross-reference) |
| **Grades** | G8-G11 |
| **Levels** | L1 (basics), L2 (formal proofs), L3 (applications) |
| **Skills gap addressed** | Formal reasoning skills; DTM Math specialty depth; programming foundation |
| **Content** | Propositional logic (truth tables, logical connectives, tautologies), predicate logic (quantifiers, variables, predicates), boolean algebra (De Morgan's laws, logic gates), proof techniques (direct proof, contradiction, induction, pigeonhole principle), set theory (operations, cardinality, relations), applications to programming and circuit design |
| **Mechanics** | Worked examples (proof completion), Tile Match (logic gate assembly), Error Analysis (invalid proof diagnosis), Why Chain (logical implication chains) |
| **Boss format** | "Prove statement X using technique Y. Each step must be justified by a named rule or axiom." Evaluated by Tier 2 LLM against formal proof rubric. |
| **Research sources** | Brilliant.org logic courses, discrete mathematics textbooks |

### Cross-Subject Course Summary Table

| Code | Course | Family Source | Grades | Levels | Primary Skills Gap |
|------|--------|--------------|--------|--------|-------------------|
| CSC-001 | Critical Thinking | Ijtimoiy + Aniq + Til | G6-11 | L1-L3 | Critical thinking (#1) |
| CSC-002 | Academic Writing | Til | G9-11 | L3-L4 | English (#1 technical) |
| CSC-003 | Debate & Rhetoric | Til + Ijtimoiy | G7-11 | L1-L3 | Communication |
| CSC-004 | Financial Literacy | Ijtimoiy + Aniq | G5-11 | L1-L3 | Economic literacy |
| CSC-005 | IT & Programming | Aniq | G7-11 | L1-L4 | IT talent shortage |
| CSC-006 | AI Literacy & ML | Aniq | G10-11 | L1-L3 | AI strategic skills |
| CSC-007 | Medical School Prep | Tabiat | G10-11 | L3-L4 | Medical entrance |
| CSC-008 | Environmental Science | Tabiat | G7-11 | L1-L3 | Sustainability (2030) |
| CSC-009 | GIS & Cartography | Tabiat + Aniq | G8-11 | L1-L3 | Geospatial literacy |
| CSC-010 | Law & Civic Rights | Ijtimoiy | G9-11 | L1-L3 | Civic literacy |
| CSC-011 | Applied Economics | Ijtimoiy | G10-11 | L1-L3 | Economic literacy (2030) |
| CSC-012 | Historiography | Ijtimoiy | G9-11 | L2-L4 | Critical history |
| CSC-013 | Creative Lab | Tarbiya/Sanat | G5-11 | L1-L3 | Digital creative skills |
| CSC-014 | Music Production | Tarbiya/Sanat | G7-11 | L1-L3 | Creative industry |
| CSC-015 | Sports Science | Tarbiya/Sanat + Tabiat | G8-11 | L1-L3 | Health literacy |
| CSC-016 | Mathematical Logic | Aniq | G8-11 | L1-L3 | Formal reasoning |

---

*End of Part 4: Cross-Subject Courses*
*Next: Part 5 — Library Catalog Hierarchy*

---

## Part 5: Library Catalog Hierarchy

### How Everything Organizes

The library is a tree. Every content item in NETS has exactly one home in this hierarchy. The hierarchy determines what content is available, when, to whom, and in what order.

```
NETS LIBRARY
│
├── SUBJECT FAMILIES (5)
│   ├── Aniq Fanlar
│   ├── Til Fanlari
│   ├── Tabiat Fanlari
│   ├── Ijtimoiy Fanlari
│   └── Tarbiya/Sanat
│   │
│   ├── [FAMILY]
│   │   ├── Subjects (per family, ~4-8 each)
│   │   │   └── [SUBJECT] (e.g., Matematika)
│   │   │       ├── Grades (G5-G11 where subject exists)
│   │   │       │   └── [GRADE] (e.g., Grade 7)
│   │   │       │       ├── Chapters (textbook sequence)
│   │   │       │       │   └── [CHAPTER N]
│   │   │       │       │       ├── Content Blocks (L1: textbook canon)
│   │       │       │       │       │   ├── recall_items
│   │       │       │       │       │   ├── narrative_segments
│   │       │       │       │       │   ├── checkpoint_questions
│   │       │       │       │       │   ├── game_items
│   │       │       │       │       │   ├── transfer_scenarios
│   │       │       │       │       │   ├── mnemonic_exercises
│   │       │       │       │       │   ├── boss_questions
│   │       │       │       │       │   └── reflection_prompts
│   │       │       │       │       │
│   │       │       │       │       └── Extended Content (L2: deeper)
│   │       │       │       │           ├── harder_game_items
│   │       │       │       │           ├── complex_transfer_scenarios
│   │       │       │       │           └── harder_boss_questions
│   │       │       │       │
│   │       │       │       └── Path Content (L3-L4)
│   │       │       │           ├── DTM practice exams
│   │       │       │           ├── Olympiad problem sets
│   │       │       │           └── PISA excellence items
│   │       │       │
│   │       │       └── Supplemental Materials
│   │       │           ├── Worked example banks
│   │       │           ├── Formula sheets / reference cards
│   │       │           ├── Diagram libraries
│   │       │           └── Practice drill sets
│   │       │
│   │       └── Cross-Grade Resources (subject-wide, not grade-specific)
│   │           ├── Formula reference (Math, Physics, Chem)
│   │           ├── Vocabulary master list (Languages)
│   │           └── Diagram atlas (Biology, Geography)
│   │
│   └── [NEXT FAMILY] ...
│
├── CROSS-SUBJECT COURSES (16)
│   ├── CSC-001: Critical Thinking
│   ├── CSC-002: Academic Writing
│   ├── CSC-003: Debate & Rhetoric
│   ├── CSC-004: Financial Literacy
│   ├── CSC-005: IT & Programming
│   ├── CSC-006: AI Literacy & ML
│   ├── CSC-007: Medical School Prep
│   ├── CSC-008: Environmental Science
│   ├── CSC-009: GIS & Cartography
│   ├── CSC-010: Law & Civic Rights
│   ├── CSC-011: Applied Economics
│   ├── CSC-012: Historiography
│   ├── CSC-013: Creative Lab
│   ├── CSC-014: Music Production
│   ├── CSC-015: Sports Science
│   └── CSC-016: Mathematical Logic
│   │
│   └── [COURSE]
│       ├── Levels (L1-L4 as defined per course)
│       │   └── [LEVEL]
│       │       ├── Content Blocks (same 8 types as subject chapters)
│       │       └── Course-specific content types
│       └── Supplemental Materials
│
├── WEEKLY PISA LESSONS
│   ├── PISA Math lessons
│   ├── PISA Reading lessons
│   └── PISA Science lessons
│   │
│   └── [LESSON N]
│       ├── Target PISA level
│       ├── Domain (quantity, space_and_shape, etc.)
│       ├── 7-phase session content
│       └── Cross-referenced subject content
│
└── SUPPLEMENTAL LIBRARIES (cross-cutting)
    ├── Worked Example Banks (per family)
    ├── Practice Drill Sets (per family)
    ├── Formula / Reference Sheets (per family)
    ├── Diagram / Image Libraries (per family)
    ├── Vocabulary Master Lists (Til Fanlari)
    └── Assessment Item Banks (per path per family)
```

### Content Block Types (Re-stated from Universal Framework)

Every content item in the library is one of these 8 types:

| Type | Phase Used In | Purpose | Example |
|------|--------------|---------|---------|
| `recall_item` | Phase 1: Memory Sprint | Recall from prior chapters | "What is the formula for area of a circle?" |
| `narrative_segment` | Phase 2: Story Mode | Textbook content as story | "Al-Khwarizmi faced a problem: how to divide inheritance..." |
| `checkpoint_question` | Phase 2: Story Mode | Comprehension gate | "Why did Al-Khwarizmi need a new method here?" |
| `game_item` | Phase 3: Game Breaks | Practice via game mechanic | Tile Match: drag formula components into correct equation |
| `transfer_scenario` | Phase 4: Real-Life Challenge | Uzbek-context application | "You run a dukan in Samarkand. How do you price your goods?" |
| `mnemonic_exercise` | Phase 5: Consolidation | Memory Palace / lock | "Place these 5 steps in your Memory Palace hallway" |
| `boss_question` | Phase 6: Final Boss | PISA-calibrated assessment | Open derivation: "Prove that the sum of angles in a triangle is 180°" |
| `reflection_prompt` | Phase 7: Reflection | Metacognition | "Which step was hardest? Why do you think that is?" |

### Content Addressing Schema

Every content item gets a unique address in the library:

```
{family_code}/{subject_code}/{grade}/{lang}/{chapter}/{level}/{block_type}/{item_id}
```

The `{lang}` segment is mandatory — NETS is a bilingual system serving both Uzbek (`uz`) and Russian (`ru`) instruction tracks. A Russian-language version of the same content item is a different library item with its own address.

**Examples:**
- `ANIQ/MATH/7/uz/3/L1/game_item/tile_match_001` — Aniq Fanlar, Math, Grade 7, Uzbek, Chapter 3, Level 1, Tile Match game item #1
- `TIL/ENG/9/uz/5/L3/boss_question/writing_001` — Til Fanlari, English, Grade 9, Uzbek, Chapter 5, Level 3, Boss writing task #1
- `ANIQ/MATH/7/ru/3/L1/game_item/tile_match_001` — Russian-language sibling of the first example
- `CSC/CSC-001/L2/uz/game_item/source_compare_005` — Cross-Subject Course, Critical Thinking, Level 2, Uzbek, Source Comparison game #5
- `PISA/MATH/WK4/uz/L3/transfer_scenario/modeling_002` — Weekly PISA Lesson, Math, Week 4, Uzbek, Level 3, Transfer scenario #2

**Note for cross-subject courses and PISA lessons:** The `{lang}` segment follows the level (not the grade) since these don't have grade-specific chapters. Format: `{code}/{course_code}/{level}/{lang}/{block_type}/{item_id}`.

### Content Tagging (Mandatory, from Universal Framework)

Every item carries these tags before entering the live pool:

```json
{
  "textbook_ref": { "textbook_id": "...", "grade": 7, "subject": "math", ... },
  "standard_ref": { "primary_code": "UZ-MATH-7-ALG-03", "alias_code": "MAT.7.2.3.1", ... },
  "pisa_ref": { "domain": "mathematics", "proficiency_level": 3, ... },
  "blooms_level": "apply",
  "language": "uz",
  "ai_tier": 1,
  "review_status": "approved",
  "game_mechanic": "tile_match",
  "transition_skill": "L2->L3: sequential decision-making",
  "library_address": "ANIQ/MATH/7/3/L2/game_item/tile_match_001",
  "path_tags": ["STD", "DTM"],
  "course_code": null
}
```

**Additional tags for cross-subject courses:**
```json
{
  "course_code": "CSC-001",
  "path_tags": ["STD"],
  "skills_gap_ref": "critical_thinking_01",
  "textbook_ref": null
}
```

### Content Production Pipeline

Content is produced through a pipeline that moves items from draft to live:

```
Draft → Family Framework Review → Subject Framework Authoring → 
Tagging Complete → Quality Check (compliance checklist) → Live Pool

**Quality Check:** Every content item must pass a compliance checklist before entering the live pool. The checklist validates: mandatory tag completeness (all 10 tags present — `textbook_ref`, `standard_ref`, `pisa_ref`, `blooms_level`, `language`, `ai_tier`, `review_status`, `game_mechanic`, `transition_skill`, `library_address`), tag consistency (PISA level matches Bloom's level, transition_skill matches pisa_ref), textbook-truth alignment (content does not contradict textbook), SOUL principle compliance (no pay-to-win gating, difficulty hidden, "Hali emas" framing), and family mechanic rules (no banned mechanics used, dual-catalog rule met). Full checklist to be defined in the Content Quality Assurance spec.
```

**Current production state (from content audit):**
- ~8 chapters/demos built out of ~110+ needed
- Highest priority: Matematika G5 (13 chapters, strong CPA), Science G5 (gold-standard framework)
- 12 subjects have zero completed content — need framework authoring from scratch

### Library Size Projections

| Layer | Items (estimate) | Notes |
|-------|-----------------|-------|
| Subject chapters (L1) | ~55,000 items | 110 subject×grade frameworks × ~500 items each |
| Extended content (L2) | ~27,500 items | ~50% of L1 items have L2 extended variants |
| DTM path content (L3) | ~10,000 items | 7 specialty subjects × 7 DTM topic areas × ~200 items |
| Olympiad path (L3-L4) | ~5,000 items | 5 Olympiad subjects × ~1,000 items |
| Cross-subject courses | ~8,000 items | 16 courses × ~500 items average |
| Weekly PISA lessons | ~5,000 items | 52 weeks × 3 subjects × ~32 items per lesson |
| Supplemental libraries | ~15,000 items | Worked examples, drills, references, diagrams |
| **Total** | **~125,500 items** | Full library at production scale |

**Production cost estimate:** UNIFIED spec §10 estimates ~$61 per textbook for AI-assisted content generation (Tier 1 template + Tier 2 refinement). At ~110 subject×grade frameworks averaging ~500 L1 items each, the core L1 layer costs roughly $6,700. Extended content (L2-L4), cross-subject courses, and PISA lessons add approximately 2-3x the base cost. **Rough total: $15,000-$25,000 for full library production** using AI-assisted pipeline. Human QA review is the primary bottleneck — not generation cost. Production timeline and team sizing deferred to the Content Production Plan.

---

*End of Part 5: Library Catalog Hierarchy*
*Next: Part 6 — Placement Suggestions*

---

## Part 6: Placement Suggestions

### Where Content Goes and How Students Encounter It

This section maps every library component to its placement in the product experience — when it appears, through what surface, and with what trigger. This is the bridge between the library (what exists) and the user experience (what students see).

### Weekly PISA Lesson — Placement

**What:** A standalone 7-phase PISA-calibrated session, delivered weekly.

**Placement:** All tiers, weekly, 7-day rolling async window, ~20 minutes, teacher dashboard tracks completion. Premium students receive expanded content pool (L3-L4 items, AI analysis, personalized plans). Basic students receive standard L1-L2 PISA content.

**Suggested placement:**
- Appears on the **Today** surface every Monday (or first login of the week)
- Labeled as "Haftalik PISA" (Weekly PISA) — distinct visual treatment from regular homework
- Subject rotates weekly: Week 1 = Math, Week 2 = Reading, Week 3 = Science, Week 4 = Math, etc.
- PISA level targets student's current level + 0.5 (pushes the flow state upper boundary)
- Completion feeds into Bilim Token economy (large award) and streak system

**Weekly PISA for ALL tiers (product decision confirmed):** Weekly PISA lessons are available to ALL students regardless of tier — Basic and Premium alike. Premium students receive expanded PISA content (additional practice items, deeper L3-L4 difficulty variants, AI-powered analysis of weak domains, and personalized PISA study plans). Basic students receive the standard weekly PISA session (L1-L2 difficulty, standard 7-phase format, ~20 minutes). This ensures every student in the national system gets regular PISA exposure — consistent with NETS's mission that no student is academically disadvantaged by tier.

**Cross-reference with paths:** Students on the PISA Excellence Path get harder PISA lessons (L3-L4) than Standard Path students (L2). The system pulls from different level pools based on active path.

### Cross-Subject Courses — Placement

**What:** 16 premium courses, each a standalone learning track.

**Placement in System Design v1:** Premium specialized courses. Upsell surfaces: "Want to try the harder version?" after strong session; "Want 5 minutes with the AI tutor?" after struggle.

**Suggested placement:**
- **Library surface** → Dedicated "Courses" tab, separate from subject browsing
- Courses displayed as cards with: title, grade range, current level, progress bar, skills gap it addresses
- Recommended courses surfaced based on:
  - Student's PISA weakness → suggests relevant course
  - Student's university direction interest → suggests DTM-aligned courses
  - Student's performance patterns → suggests enrichment (high performer → Olympiad; struggling → Critical Thinking fundamentals)

**Specific course placement suggestions:**

| Course | When to Suggest | Trigger |
|--------|----------------|---------|
| Critical Thinking | All students G6+ | PISA math modeling < Level 2 |
| Academic Writing | G9-11, English students | Writing Boss score < 60% |
| IT & Programming | G7+ any student | Informatics performance ≥ 80% |
| Financial Literacy | G5+ all students | Available from G5, no trigger needed |
| IELTS Prep | G7+ English students | CEFR diagnostic shows B1+ readiness |
| Medical School Prep | G10-11, DTM Bio+Chem path | Student enrolls in Medical direction |
| Mathematical Logic | G8+ Math students | DTM Math specialty enrollment |
| AI Literacy | G10-11 | Available to all G10+, no trigger |
| Debate & Rhetoric | G7+ | Language performance ≥ 80% |
| Environmental Science | G7+ | Tabiat Fanlari performance ≥ 75% |

### Extended Content (L2) — Placement

**What:** Same topics as L1 but deeper — harder problems, cross-chapter synthesis.

**Suggested placement:**
- Unlocks automatically after student demonstrates ≥70% success on L1 content for a chapter
- Labeled "Chuqurroq" (Deeper) — never "Level 2" or "Advanced"
- Appears as an optional extension after completing the standard chapter session
- Visual distinction: slightly more ornate frame, but same phase flow
- **Not pushed** — student must opt in. The upsell surface says "Ready for a deeper challenge?" after strong chapter completion

**Placement for DTM path students:** L2 content is automatically included in DTM path sessions — it is not optional for them, because DTM exam questions routinely exceed textbook difficulty.

### DTM Practice Exams — Placement

**What:** Full-format DTM simulation exams (90 MCQs, 180 min, specialty-aligned).

**Suggested placement:**
- Available as standalone "Practice Exam" sessions — not part of the 7-phase homework flow
- Separate entry point: "DTM Practice" button on Today surface (visible only to G9-11 on DTM path)
- Full exam simulation: 180-min timer, 90 questions, specialty block weighting
- Results dashboard shows: score per block, topic breakdown, comparison to state grant threshold (68.0)
- Weekly practice exam recommended; system tracks improvement trajectory

**ADR REQUIRED:** Full DTM practice exams (180 min, 90 MCQ) do not fit the 7-phase session structure, which is locked at Layer 0 (UNIFIED spec). This is an intentional exception — exam simulation must replicate actual DTM format to be useful, and wrapping 90 MCQs in Story Mode → Game Breaks → Boss would defeat the purpose. **Proposed ADR:** DTM Practice Exams are classified as "Assessment Mode" sessions — a new session type alongside Standard/Extended/Recovery. Assessment Mode sessions follow exam format (not 7-phase) and do not count toward homework completion, streak, or BT earnings. They are purely diagnostic. This ADR must be approved before DTM path content is authored.

**Partial practice** (smaller units):
- "DTM Drill" sessions: 10-15 questions on a specific topic (e.g., "Physics: Electrodynamics")
- Available between homework sessions as supplemental practice
- Uses Adaptive Quiz + Speed Match mechanics
- Timed (shorter: 15-20 min) but not full exam simulation
- **Note:** DTM Drills CAN fit the 7-phase structure (short sprint → drill → mini-boss) and do NOT require the Assessment Mode ADR. Only full-format 90-MCQ simulations need the exception.

### Olympiad Content — Placement

**What:** L3-L4 difficulty problem sets targeting 4-stage Olympiad progression.

**Suggested placement:**
- Available only after qualification (≥80% L2 success)
- Appears as "Chempion" challenges on Today surface
- Distinctive visual treatment: gold border, rare framing
- Olympiad problem sets are standalone sessions — not mixed with regular homework
- Monthly "Olympiad Practice" events simulate district/regional exam conditions
- Top performers in monthly practice get flagged for teacher recommendation to actual Olympiad

### Supplemental Libraries — Placement

**What:** Worked example banks, formula sheets, diagram libraries, practice drill sets, vocabulary master lists.

**Suggested placement:**
- **Not sessions** — these are reference materials, accessible on-demand
- **Formula sheets:** Available as in-session hints during homework. Student can tap "Reference" during any Aniq Fanlar session to see relevant formulas.
- **Worked example banks:** Accessible from Library surface → Subject → "Examples" tab. Student browses by chapter and topic.
- **Diagram libraries:** Accessible during Tabiat Fanlari sessions as reference. Also browsable from Library.
- **Vocabulary master lists:** Accessible from Til Fanlari Library → "Words" tab. Integrates with spaced repetition — words the student has mastered are marked; words pending review are highlighted.
- **Practice drill sets:** Short 5-10 question sessions, available between homework. "Quick practice" option on Today surface. Uses fastest mechanics (Speed Match, Tile Match).

### Content Gap Remediation — Placement

**What:** Targeted micro-exercises for specific weaknesses identified by AI analysis.

**Suggested placement:**
- Triggered automatically in Phase 7 (Reflection + Remediation) of the 7-phase session
- AI analyzes student's error patterns → generates 2-3 micro-exercises targeting the specific gap
- If remediation fails twice → escalates to Tier 3 Socratic tutoring (Premium) or teacher alert
- Micro-exercises use the simplest game mechanics available for the skill (lower cognitive load for remediation)

### Teacher Dashboard Integration Points

The teacher dashboard should surface library data at these points:

| Dashboard Element | Library Data Source | Purpose |
|------------------|-------------------|---------|
| Class attendance | Homework session completion logs | Who did/didn't complete this week |
| Per-student mastery map | PISA transition skill tags | Which skills each student has mastered |
| Anti-cheat flag log | Behavioral baseline comparison | MONITOR / SOFT_WARNING / TEACHER_ALERT |
| Weekly PISA completion | PISA lesson completion records | All classes (Premium shows expanded content status) |
| Path enrollment status | Active path tags per student | Who is on DTM/Olympiad/CERT paths |
| Content gap report | Remediation trigger frequency | Which topics the class collectively struggles with |
| Library utilization | Supplemental material access logs | Which reference materials students actually use |

### Content Production Priority (Based on Gap Analysis)

Given ~125,500 total items needed and ~8 chapters built:

**Phase 1 — Foundation (Highest Priority):**
1. Matematika G5 full framework (13 chapters, strongest CPA foundation)
2. Science G5 framework (gold-standard prototype, reuse as template)
3. Algebra G7, Kimyo G7 (2 chapters each, expand to full)
4. Biologiya G7 (3 chapters, expand)

**Phase 2 — Core Subjects (G5-7, all families):**
5. All G5 subjects (17 UZ + 13 RU = 30 frameworks)
6. All G6 subjects (18 UZ + 14 RU = 32 frameworks)
7. All G7 subjects (21 UZ + 19 RU = 40 frameworks)

**Phase 3 — DTM Path Content (G9-11):**
8. DTM practice exams for 7 specialty subjects
9. DTM Drill sets per topic area
10. Full-format mock exams (7 subjects × 10 exams each = 70 exams)

**Phase 4 — Cross-Subject Courses:**
11. Critical Thinking (CSC-001) — addresses #1 skills gap
12. IT & Programming (CSC-005) — addresses IT talent shortage
13. Academic Writing / IELTS (CSC-002) — addresses #1 technical barrier
14. Remaining 13 courses

**Phase 5 — Olympiad + PISA Excellence:**
15. Olympiad problem sets for 5 subjects
16. Weekly PISA lessons (52 weeks × 3 domains = 156 lessons)
17. PISA excellence items (L3-L4)

**Phase 6 — Extended Content (L2) + Supplemental Libraries:**
18. L2 extended variants for all L1 content
19. Worked example banks, formula sheets, diagram libraries
20. Vocabulary master lists, practice drill sets

---

## Research Gaps — Resolved

All initial research gaps have been filled by Gemini's three research waves:

| Gap | Source File | Status |
|-----|------------|--------|
| DTM topic percentages per subject | `DTM_Exam_Specs.md` | **Resolved** |
| IELTS band descriptors + CEFR mapping | `Language_Certifications.md` | **Resolved** |
| Olympiad full syllabi (IMO, IPhO, IChO, IBO, IOI) | `Olympiad_Full_Syllabi.md` | **Resolved** — complete topic lists per subject, 4-stage system, official portals |
| Lyceum detailed curricula per track | `Lyceum_Detailed_Curricula.md` | **Resolved** — 4 tracks (Engineering, Medical, Humanities, Foreign Philology), Delta topics per subject, credit-module system |
| Competitor pricing and course catalogs | `DTM_IELTS_Prep_Market.md` | **Resolved** |
| Employer/University skills gaps | `Employer_University_Expectations.md` | **Resolved** |
| IT Park / 1M Coders full syllabi | `IT_Programs_Syllabi.md` | **Resolved** — 4 Udacity tracks (Data Analysis, Android, Front-End, Full-Stack) with module-by-module syllabi, IT Park Academy/ITPU courses, GameDev, Cybersecurity |
| Presidential School Cambridge mapping | `Specialized_School_Tracks.md` | **Resolved** |
| Content audit for grades 5-7 | `NETS_Content_Audit.md` | **Resolved** |
| Buzan cognitive science (TEFCAS, memory, BOST, Mind Mapping, speed reading) | 6 Buzan research files | **Resolved** — see Part 7 |

### Remaining Research Needs (Future Waves)

| Need | Why | Priority |
|------|-----|----------|
| DTM question bank samples | We have structure but not actual question examples | High — needed for DTM path content authoring |
| PISA item bank samples | We have framework descriptors but not actual item formats | High — needed for PISA lesson authoring |
| G8-11 content audit | Current audit covers G5-7 only | Medium |
| Teacher dashboard UX research | How Uzbek teachers actually use dashboards on smartphones | Medium |
| Russian-language subject mappings | Some RU subjects have no UZ equivalent (e.g., немецкий язык G11) | Low |
| Group Mind Map multiplayer UX | Collaborative study session design patterns | Low — future feature |

**Note:** XP measures effort. The Learning Curve Grade (Level, Velocity, Efficiency, Attempts) measures learning progress. See `standards/framework/GRADING-SYSTEM.md` for the grading overlay that sits on top of all mechanics. XP remains as the student-facing reward; the Learning Curve Grade is the teacher/parent-facing assessment.

---

*End of Part 6: Placement Suggestions*
*Next: Part 7 — Buzan Cognitive Science Integration*

---

## Part 7: Buzan Cognitive Science Integration

### Why Buzan

Tony Buzan's research on Radiant Thinking, memory systems, and the Organic Study Technique (BOST) provides the cognitive science backbone for how NETS delivers content. Every phase, every game mechanic, and every mnemonic is designed to work with how the brain actually stores and retrieves information — not against it.

### The TEFCAS Model — Core Engine Logic

**Source:** `Buzan_Scientific_Research.md`, `Buzan_Mind_Maps_Kids.md`

TEFCAS (Trial → Event → Feedback → Check → Adjust → Success) is Buzan's cybernetic feedback loop that mirrors how the nervous system acquires skills. TEFCAS models the *student's learning cycle* — how a learner progresses through attempts. The UNIFIED spec's IRT (Item Response Theory) models *item difficulty calibration* — how the system selects appropriately challenging questions. These are complementary: IRT calibrates the question pool, TEFCAS describes how the student moves through it. Together, they enable TEFCAS feedback cycles within an IRT-calibrated environment. TEFCAS is NOT a replacement for IRT — it is the pedagogical framing layer on top of the statistical engine.

| TEFCAS Step | Definition | NETS Mapping |
|-------------|-----------|--------------|
| **T — Trial** | Initial attempt; "Try-All" approach | Every question in every phase is a Trial; Final Boss is the ultimate Trial |
| **E — Event** | The outcome of the trial | Student sees their score, HP bar changes, visual/audio response |
| **F — Feedback** | Sensory info from the event | Socratic tutor provides guiding feedback (not answers); IRT shows difficulty adjustment |
| **C — Check** | Analytical comparison vs. Goal | IRT engine checks current Theta (proficiency) against item difficulty |
| **A — Adjust** | Modifying approach for next trial | IRT adjusts difficulty to keep student in Flow Zone (70-80% success) |
| **S — Success** | Achieving the target | XP gain, badge award, boss defeat, streak increment |

**Key Maxim:** "There is no such thing as failure, only feedback."

**G5 "Hali emas" Framing:** When a student fails a Final Boss, the AI says: *"Hali emas! Your brain just got some Feedback. Let's look at your Bilim Bazasi. Which branch needs a new 'Adjust' line?"* This reframes failure as a mapping exercise rather than a verdict.

**TEFCAS Gamified Achievements:**
- **"The Try-All"** — Awarded for attempting 3 different methods to solve a single Final Boss problem
- **"Pivot Master" Badge** — Student misses a question but gets the subsequent (adjusted) item correct on first try
- **"Radiant Streak"** — Bonus XP for using 5+ distinct Basic Ordering Ideas in a consolidation Mind Map
- **"Merz's Retention" Bonus** — Extra XP for passing a Spaced Repetition check 24h after initial lesson

### The "Most Important Graph" (MIG) — Memory Effects

**Source:** `Buzan_Use_Your_Memory.md`

The MIG defines recall curves during a learning session. The 7-phase architecture is designed to exploit these effects:

| Effect | Description | NETS Phase Mapping |
|--------|-------------|-------------------|
| **Primacy Effect (P)** | Highest recall at the START of a session | Phase 1 (Memory Sprint) — lock foundational items when primacy is maximal |
| **Recency Effect (R)** | Highest recall at the END of a session | Phase 7 (Reflection) — consolidate while recency is high |
| **Association Effect (A)** | We remember things linked to prior knowledge | Phase 2 (Story Mode) — narrative association engine |
| **Von Restorff Effect (VR)** | We remember the unique, weird, outstanding | Phase 3 (Game Breaks) — bizarre, standout imagery |
| **The "Sag"** | Recall dips in the MIDDLE of long sessions | **NETS Solution:** 7 phases with Game Breaks RESET Primacy/Recency curves multiple times |

**Quantifiable Rule:** The sag begins after ~20-25 minutes of continuous linear content. Each phase boundary acts as a "fresh start" that resets the primacy effect.

### Memory Systems

**Source:** `Buzan_Use_Your_Memory.md`

#### Link System
- **Mechanism:** Vivid chain of images where each item triggers the next
- **NETS Phase 1 (Memory Sprint):** Link System chains for vocabulary clusters instead of standard MCQs
- **NETS Phase 2 (Story Mode):** The narrative itself IS a Link System — each story event triggers the next, embedding curriculum content

#### Peg System
- **Number-Shape Pegs:** 1 = Spear, 2 = Swan, 3 = Heart, 4 = Sailboat, etc.
- **Number-Rhyme Pegs:** 1 = Sun, 2 = Shoe, 3 = Tree, 4 = Door, etc.
- **NETS Phase 1 (Memory Sprint):** Quick-fire Number-Shape Pegs for math rules
- **NETS Phase 3 (Game Breaks):** Tic Tac Toe — to place an 'X', student converts a number into its Peg image. *Playtesting required: dual-task (peg encoding + game rules) may exceed G5 working memory ceiling. Do not ship without G5 user testing.*

#### Major System
- **Phonetic code:** 0=s/z, 1=t/d, 2=n, 3=m, 4=r, 5=l, 6=j/sh/ch, 7=k/g, 8=f/v, 9=p/b
- **NETS History:** Alisher Navoi birth year 1441 → "TRRT" → Image: a "TuRTle" wearing a Tara
- **NETS Chemistry:** Periodic table group numbers mapped to phonetic codes with vivid sensory triggers

#### Memory Palace (Method of Loci)
- **NETS Phase 3/5:** **Registan Square** as the default Loci environment. Students place science concepts (cell organelles, physics formulas) in specific corners of Sher-Dor Madrasah
- **NETS Phase 5 (Consolidation):** Memory Palace serves as the "mnemonic lock" before the Final Boss

#### SMASHIN' SCOPE — Quality Gate for Mnemonics

All AI-generated mnemonic images must maximize these 12 qualities (age-appropriately filtered for G5-8):

| Letter | Quality | Example |
|--------|---------|---------|
| **S** | Synaesthesia (multi-sensory) | A formula that "sounds like" a drumbeat |
| **M** | Movement | A chemical reaction shown as an explosion |
| **A** | Association | Linking a new concept to a familiar object |
| **S** | Vitality / Life Energy | A glowing, vibrant, "alive" cell |
| **H** | Humor | A ridiculous image for a boring fact |
| **I** | Imagination | Something impossible in real life |
| **N** | Number | Counting elements in the image |
| **S** | Symbolism | A crown = "most important" |
| **C** | Color | Bright, contrasting colors |
| **O** | Order | Sequential arrangement |
| **P** | Positive | Encouraging, not threatening imagery |
| **E** | Exaggeration | Huge, tiny, or impossible scale |

**NETS Implementation:** AI-generated mnemonics pass through a SMASHIN' SCOPE checklist. The AI tutor prompts students to add at least 3 SMASHIN' SCOPE qualities to their own mental images.

#### SEM3 (Master Memory Matrix) — Future Exploration

> **Not in current scope.** SEM3 (10,000-item grid combining Major System images with Master Categories) is a theoretical long-term architecture. It requires validation with G5-G6 students before inclusion in any production spec. Deferred to future research phase.

### Buzan Organic Study Technique (BOST)

**Source:** `Buzan_Use_Your_Head.md`

BOST is a structured 2-phase path for tackling any subject. It maps directly to NETS's Pre-Session Stage A/B design:

| BOST Step | NETS Phase | Implementation |
|-----------|-----------|----------------|
| Browse + 5-min Mind Map | Pre-Session Stage A (Theme Preview) | "What do you already know about [Topic]?" + partially completed Radiant Anchor |
| Questions/Goals | Pre-Session Stage A (Component #6: "Why This Matters") | "What's one thing you want to figure out today?" — stored and displayed in Phase 7 |
| Overview + Preview | Pre-Session Stage B (Flash Cards) | Rapid review of formulas and definitions before practice |
| Inview (detailed work) | Phase 2 (Story) + Phase 3 (Games) | Core content delivery maintaining "momentum" |
| Review (Gestalt synthesis) | Phase 5 (Consolidation) + Phase 7 (Reflection) | Memory Palace + Reflection Journal synthesize the "whole picture" |

**Naming clarification:** Pre-Session Stages A and B are NOT phases. The UNIFIED spec's 7-phase structure (P1 Memory Sprint through P7 Reflection) is locked at Layer 0. Pre-Session stages are preparatory steps that run before the session timer starts, as defined in UNIFIED spec §4.1. The "Phase 0" label used in earlier drafts is retired to avoid confusion.

**BOST Review Intervals** (aligned with NETS Spaced Repetition):

| Review | Timing | NETS Mapping |
|--------|--------|-------------|
| First | 10 minutes after learning | Phase 5 (Consolidation) or Phase 7 (Reflection) |
| Second | 24 hours later | Next day's Phase 1 (Memory Sprint) — spaced repetition check |
| Third | 1 week later | Weekly review session or "Boss Rematch" |
| Fourth | 1 month later | Monthly mastery assessment or "Champion's Arena" |

**NETS Meta-Learning Badges (from BOST cortical synergy):**
- **Cortical Synergist:** Mastering games that combine image, sound, and logic (Tile Match + Audio clues)
- **Mind Map Master:** Completing a 5-level "Why Chain" branch successfully
- **Radiant Thinker:** Identifying cross-subject connections in the Mystery Box mechanic

### Mind Mapping — Laws and Phase Integration

**Sources:** `Buzan_Mind_Map_Book.md`, `Buzan_Mind_Maps_Kids.md`

#### The 7 Laws of Mind Mapping
1. **Central Image:** Colorful image in center (landscape orientation)
2. **Organic Branches:** Curved lines, thickest at center, thinning toward tips
3. **Hierarchy:** Basic Ordering Ideas (BOIs) for main branches
4. **Keywords (One Per Line):** Exactly one keyword per branch
5. **Emphasis:** Different sizes, fonts, bolding for visual hierarchy
6. **Association:** Arrows, colors, codes for cross-links
7. **Images & Colors:** Icons, symbols, at least 3 colors per map

#### G5-G6 Adaptations (WM-Respecting)

G5 students have a Working Memory ceiling of ~4-5 chunks. Mind maps are the direct antidote:

| Adaptation | Rule |
|-----------|------|
| **Landscape Orientation** | Always sideways — "freedom of movement" |
| **Central Image without Words** | Acts as anchor for focus |
| **One Word Per Branch** | Forces identification of the most important "hook" — prevents cognitive overload |
| **Color-Coded Zones** | Each main branch and sub-branches share a distinct color |
| **Icon-First Rule** | Draw icon BEFORE writing the word — lowers barrier for struggling readers |
| **"Supernova" Effect** | Every word is a "little exploding star" — gamifies brainstorming |
| **Secret Symbols** | Kids create own codes (lightbulb = great idea, ? = ask teacher, ♥ = love this topic) |
| **Minimum 3 Colors** | Required for visual memory stimulation |

**Empirical Evidence:**
- **Merz Study (Germany, cited in Buzan 2006):** 10-15% increase in factual retention with Mind Maps vs. linear notes. *Note: original study details limited; effect size cited from Buzan secondary source, not primary RCT.*
- **Farrand, Hussain, & Hennessy (2002):** Mind mapping improved factual recall by 10% over traditional methods; higher engagement, lower cognitive load

#### Mind Mapping by NETS Phase

| Phase | Mind Map Application |
|-------|--------------------|
| **Pre-Session** | 5-min BOST Mind Map — "What do you already know?" |
| **Phase 1: Memory Sprint** | 4-branch Radiant Anchor of prior lesson (G5 WM-respecting) |
| **Phase 2: Story Mode** | Radiant Narrative — story unfolds radiantly, not linearly |
| **Phase 3: Game Breaks** | Digital Memory Palace (Registan Square), Major System, Pegs |
| **Phase 4: Real-Life Challenge** | Divergent Thinking — "branching" Why Chains |
| **Phase 5: Consolidation** | Radiant Summaries — partially completed Mind Map drag-and-drop synthesis |
| **Phase 6: Final Boss** | TEFCAS full cycle — the Boss is the ultimate Trial |
| **Phase 7: Reflection** | Recency Effect — review Radiant Summary, identify weak branches, AI targets remediation |

### Speed Reading Integration

**Source:** `Buzan_Speed_Reading.md`

#### Reading Mechanics (Implementable Subset)

| Concept | Definition | Quantifiable Metric |
|---------|-----------|-------------------|
| **Fixations** | Brief pauses (0.25-1.5s) where eye absorbs info | Target: reduce from 8-10 to 2-3 fixations/line |
| **Saccades** | Rapid jerky jumps between fixations. Brain is "blind" during saccade. | Information only processed during fixations |
| **Regressions** | Re-reading words/sentences — destroys rhythm | Eliminate via pacer/guide |
| **Peripheral Vision** | Trained to recognize word "shapes" and context | *Theoretical — not implementable without eye-tracking hardware. Excluded from NETS scope.* |

#### Chunking
- **Definition:** Grouping 3-5 words into a single meaningful unit
- **Effect:** Reduces fixations per line, increases speed without losing conceptual gist

#### Sub-vocalization
- **Problem:** Inner voice pronounces words. Limits speed to ~150 WPM.
- **Solution:** Visual pacing (pacer forces eyes faster than inner voice), direct Visual → Brain pathway

#### UI/UX Quantifiable Rules

| Rule | Metric |
|------|--------|
| **Column Width** | 50-75 characters (66 ideal) |
| **Font** | High-legibility Sans-Serif (Arimo for Uzbek Latin/Cyrillic) |
| **Line Height** | 1.5x font size — prevents line-skipping during rapid saccades |

#### NETS Mappings

**Story Mode — Pacing and Chunking:**
- **Guided Pacer:** AI-driven highlight or "focus dot" moves across text at target WPM (IRT-adjusted). Acts as digital pacer to eliminate regressions
- **Chunked Presentation:** G5-G6 text in "meaningful chunks" (visual clusters) rather than standard blocks

**NETS Speed Reading Mini-Games:**
| Game | Target | Description |
|------|--------|-------------|
| **Scanning Sprint** | PISA L1/L2 | 500-word excerpt. Find specific name/city within 15 seconds |
| **Structural Skimming** | PISA L3 | Read only headings, bold terms, first sentences. Construct a 5-branch Mind Map in 3 minutes |

### Radiant Navigation — UI Architecture

**Concept:** Replace linear sidebar/sidebar navigation with Radiant Map for subject learning journeys.

| Element | Implementation |
|---------|---------------|
| **Subject Journey as Radiant Map** | Current chapter = "active branch," past/future chapters visible but faded — shows "Growth of Knowledge" |
| **Bilim Bazasi as Persistent Radiant Map** | Grows as student completes lessons. If student drew a "Fire" icon for a History lesson, that exact icon appears in their digital map |
| **Landscape for G5-G6** | All Mind Map interfaces default to landscape |
| **Group Mind Map** | *Future feature — deferred. Not in current scope.* |

### Anti-Cheat: Radiance Score

**Concept:** AI/LLM and rote-copying produce highly linear, predictable semantic structures.

**Detection Mechanism:** "Radiant" response patterns in open-reasoning tasks are characterized by:
- Idiosyncratic associations
- Non-linear logic jumps
- Personal "keywords"

**Flag:** Responses that lack these "radiant" signatures (too "perfectly" linear) are high-probability AI/Copy-paste detections.

**NETS Implementation Contract:**

| Parameter | Value |
|-----------|-------|
| **Input** | Student response text + 5 most recent historical responses for baseline comparison |
| **Output** | Authenticity score (0.0-1.0). Threshold: <0.3 = FLAG, 0.3-0.6 = MONITOR, >0.6 = CLEAN |
| **AI Tier** | Tier 2 only (cheap LLM inference). NOT Tier 3. |
| **Token cost** | ~200-400 tokens per evaluation (response + baseline + prompt) |
| **Fallback** | If Tier 2 unavailable, Radiance Score defaults to 0.5 (MONITOR) — never blocks session |
| **Rollout** | Phase 1: MONITOR-level only (no student-visible action). Promote to SOFT_WARNING after 6 months of accuracy validation with teacher feedback |
| **Integration** | Added as 6th flag type alongside SPEED_ANOMALY, LENGTH_ANOMALY, PASTE_DETECTED, VOCAB_JUMP, STRUCTURE_ANOMALY. Does NOT replace any existing flag. |

### Buzan Integration Summary — By Phase

| NETS Phase | Buzan Techniques Applied |
|-----------|------------------------|
| **Pre-Session** | BOST Preparation (Browse, 5-min Mind Map, Questions/Goals), Theme Preview priming |
| **Phase 1: Memory Sprint** | Primacy Effect, Link System, Number-Shape Pegs, 4-branch Radiant Anchor (G5 WM-respecting) |
| **Phase 2: Story Mode** | Association Effect, Link System narrative, Radiant Narrative, Guided Pacer (speed reading), Chunked presentation (G5-G6), 80/20 Rule for text value |
| **Phase 3: Game Breaks** | Von Restorff Effect, Digital Memory Palace (Registan Square), Major System, Alphabet Pegs, Tile Match (cortical synergy), Scanning Sprint, Tic Tac Toe + phonetic code |
| **Phase 4: Real-Life Challenge** | Association Effect (local context mapping), Divergent Thinking (branching Why Chains), PISA L3 structural scanning |
| **Phase 5: Consolidation** | Radiant Summaries, Mind Map synthesis, Buzan Review Intervals (10m), SMASHIN' SCOPE mnemonic lock, Memory Palace |
| **Phase 6: Final Boss** | TEFCAS full cycle, "Hali emas" framing, Try-All achievement |
| **Phase 7: Reflection** | Recency Effect, Socratic TEFCAS prompts, Theme Preview goal check, Metacognition via Radiant Summary review, Buzan review intervals (24h, 1w, 1mo scheduling) |

### Quantifiable Metrics Summary

| Metric | Value | Source |
|--------|-------|--------|
| Working Memory ceiling (G5) | 4-5 chunks | Buzan / Cognitive Load Theory |
| Fixation duration | 0.25-1.5 seconds | Buzan Speed Reading |
| Target fixations per line | 2-3 (vs. 8-10 traditional) | Buzan Speed Reading |
| Chunk size | 3-5 words per fixation | Buzan Speed Reading |
| Sub-vocalization speed limit | ~150 WPM | Buzan Speed Reading |
| Ideal column width | 50-75 characters (66 ideal) | Buzan Speed Reading / Baymard |
| Line height | 1.5x font size | Buzan Speed Reading |
| Colors per Mind Map | Minimum 3 | Buzan Mind Map Book |
| Mind Map retention improvement | 10-15% | Merz Study |
| Mind Map recall improvement | 10% | Farrand et al. (2002) |
| Review intervals | 10m, 24h, 1w, 1mo | Buzan Use Your Memory |
| Flow state success rate | 70-80% | NETS spec (Csikszentmihalyi) |
| Memory sag onset | After ~20-25 min continuous content | MIG analysis |
| SMASHIN' SCOPE qualities | 12 dimensions | Buzan Use Your Memory |
| TEFCAS steps | 6 (T-E-F-C-A-S) | Buzan Scientific Research |

---

*End of Part 7: Buzan Cognitive Science Integration*
*End of NETS Library Framework v0.4*

---

**Document summary:**
- Part 1: 5 Subject Family Classifications (29 subjects, definitions, pedagogy)
- Part 2: Universal Level System (L1-L4, per-family breakdowns, progression rules)
- Part 3: Path System (5 paths, per-family definitions, DTM specialty mapping)
- Part 4: 16 Cross-Subject Courses (definitions, content, mechanics, boss formats)
- Part 5: Library Catalog Hierarchy (tree structure, addressing, tagging, production pipeline)
- Part 6: Placement Suggestions (PISA lessons, courses, extended content, supplemental libraries, teacher dashboard)
- Part 7: **Buzan Cognitive Science Integration** — TEFCAS learning cycle (complementary to IRT), memory systems (Link/Peg/Major/Memory Palace/SMASHIN' SCOPE), BOST study technique, Mind Mapping laws + G5 adaptations, speed reading (implementable subset), Radiance Score anti-cheat (with implementation contract)
- Part 8: **National Pride — Cross-Family Inheritance** — 55/45 origin balance, 20% task injection, gate quotes, Wise Status titles, Third Renaissance closing (inherited from UNIFIED-Buzan Section 1.5)

---

## Part 8: National Pride — Cross-Family Inheritance

All 5 subject families inherit the National Pride & Progress Module ("Milliy G'urur va Taraqqiyot") from UNIFIED-Buzan Section 1.5. These rules apply uniformly across families and are NOT overridable per-family:

| Rule | Applies to | Excluded from |
|------|-----------|---------------|
| **55/45 Origin Balance** — Rolling 10-item window: ~55% Uzbekistan references, ~45% global | All content across all families | — |
| **20% Task Injection** — Every 5th task gets national pride framing | Phases 1, 2, 4, 5, 7 | Phase 3 (Game Breaks), Phase 6 (Final Boss) |
| **70/30 Type Balance** — At XP milestones (30% and 60% session progress): 70% facts, 30% quotes | Break screens between phases | — |
| **Gate Quote** — Wisdom quote displayed in Phase 0-A with 5-second skip lock | Phase 0-A (Theme Preview) | — |
| **Wise Status Titles** — 30% of Phase 4 tasks assign professional titles ("Bosh Muhandis") | Phase 4 (Real-Life Challenge) | — |
| **Third Renaissance Closing** — Session closing line in Phase 7 | Phase 7 (Reflection) | — |

**Content production rule:** When producing homework for any family, the 55/45 ratio applies to Real-Life Challenge scenarios, Story Mode cultural references, and Memory Sprint prior-chapter questions. The content agent inherits these ratios from UNIFIED-Buzan — do not hardcode them in family-specific frameworks.

**Data source:** `standards/system/narrative/quotes_database.json` (600 quotes), `standards/system/narrative/Bilarmidingiz_faktlar.md` (300 facts), `standards/system/narrative/task_injections.json` (injection rules).

For full specification, see UNIFIED-Buzan Section 1.5.

---

**Total estimated library at production scale: ~125,500 content items**
**Research waves completed:** 4 (DTM/IELTS, Olympiad/Lyceum/IT, Employer/Market, Buzan Cognitive Science)

---
