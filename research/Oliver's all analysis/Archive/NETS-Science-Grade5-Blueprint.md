# NETS Homework Engine — Science Grade 5 Blueprint

**Source textbook:** Aleksandr Grey, *Tabiiy fanlar 5-sinf* (Marshall Cavendish, Toshkent: Novda Edutainment, 2024) — 164 pages, 10 boblar.
**Frameworks applied:** NETS-Homework-Engine-UNIFIED.md (v2.0), Blueprint-Complete, Standards-Summary, Blueprint-Summary.
**Developmental filter applied:** `qwen-grade5-psychology-findings.md` (Apr 2026, 50+ citations) — see §0 for the filter.
**Status:** Subject-specific instantiation. Inherits all immutables from UNIFIED; overrides only Science-relevant configuration; further constrained by Grade 5 cognitive/psychological reality.

---

## 0. Grade 5 Psychology Filter (overrides where research conflicts with universal)

The universal NETS engine targets K-11. Grade 5 (10-11 yr) has specific developmental constraints that override generic defaults. Every rule below either **adjusts a number** or **bans a technique**.

### A. Numeric overrides (use these, not universal defaults)

| Parameter | Universal default | **Grade 5 override** | Source |
|-----------|------------------|----------------------|--------|
| Flow state success rate | 70–80% | **75–85%** (higher floor) | Frontiers in Psych 2018, EEG flow research |
| Difficulty adapt cadence | every 3–5 questions | **every 3–4 questions** | slower whiplash for younger WM |
| Pass threshold (Memory Sprint, Boss) | 70% | **60%** minimum | Guskey 2010, mastery learning |
| Total session length | 30–45 min Standard / 45–60 Extended *(updated UNIFIED 2026-04-07)* | **35–45 min Standard** for G5 Science (includes 0-A + 0-B pre-homework + 7 phases) | UNIFIED §4 + attention research |
| Single phase length | varies | **never exceed 7–9 min** without transition | attention span data |
| New technical terms per session | not specified | **max 1–2** | Nagy & Herman 1987 vocab acquisition rate |
| New concepts in single instruction | not specified | **max 3** | Cowan 2001 (WM = 4-5 chunks) |
| Why Chain depth | 2-level (already in §5 game pool) | **stays at 2-level**, never 3+ for G5 | confirmed |
| Recovery time after wrong answer | not specified | **5–10 sec positive framing + hint, then proceed** | Thompson 2011 |
| Story Mode reading level | not specified | **Lexile 800–900L** — short sentences, no idioms, define new terms inline | MetaMetrics 2025 |
| Daily session cap | not specified | **max 1–2 sessions/day** (30–60 min total practice) | Cooper et al. 2006 |
| Best deployment window | not specified | **17:00–19:00** (Uzbek after-dinner homework window) | UNICEF Uzbekistan 2023 |

### B. Banned techniques (do NOT use in Grade 5 Science)

These are **filtered out** from the universal mechanic/feature roster:

1. ❌ **Public displays of wrong answers** — fragile self-concept; private correction only
2. ❌ **Absolute-rank leaderboards** — only improvement ranking ("you climbed 3 spots") or class-wide goals
3. ❌ **Real-time multiplayer competition** — skill gaps demoralize weaker students; use async ("beat your own score") instead
4. ❌ **Pure discovery / unbounded sandbox** — Grade 5 lacks self-direction; always provide guided structure
5. ❌ **Random rewards without competence link** — Mystery Box content can be random, but the *opportunity to open it* must be earned
6. ❌ **Purchasable cosmetics** — all avatar items must be earned through demonstrated competence
7. ❌ **Abstract-only puzzles** — every concept needs a concrete or pictorial referent (CPA mandatory, even for Science — not just Math)
8. ❌ **Complex multi-step instructions without worked examples** — show solved example before independent attempt
9. ❌ **Delayed feedback** — all feedback within seconds, never end-of-session-only
10. ❌ **"You're smart" / ability praise** — use effort + strategy praise: "You worked hard on this", "Good attempt — try a different approach"
11. ❌ **The word "wrong"** — use "not yet" / "not quite" / "close — here's why" (Yeager et al. 2019, +40% persistence)
12. ❌ **Brain breaks every 5 min** — disruptive at this attention span; phase transitions ARE the breaks
13. ❌ **Learning styles matching** (visual/auditory/kinesthetic) — no evidence; ignore
14. ❌ **Why Chain ≥3 levels** — over WM ceiling for G5
15. ❌ **Visible difficulty labels** ("Easy/Medium/Hard" shown to student) — triggers self-handicapping; tier hidden from UI
16. ❌ **Group/peer-correction as primary feedback** — solo-first for concept acquisition; peer explanation only as Phase 7 reflection option

### C. Mandatory additions (must do for Grade 5 Science)

1. ✅ **CPA progression for every Science concept** — Concrete (real object/photo) → Pictorial (diagram) → Abstract (definition/symbol). Not optional. Even for physics/chem.
2. ✅ **Dual coding** — every Story Mode segment must pair text WITH image, never text-only
3. ✅ **Worked example before independent practice** — show one solved instance before the student tries
4. ✅ **Spaced retrieval** — Memory Sprint pulls from Day 1 / Day 3 / Day 7 / Day 14 schedule, not just current chapter
5. ✅ **Effort + strategy feedback language** — "You found a strategy that didn't work — let's try another" (never "you got it wrong")
6. ✅ **Cultural anchors in Uzbek context** — Ulugh Beg observatory (astronomy/physics), Aral Sea (ecology/Bob 9), Registan/Silk Road cities (geography/Bob 8), Amir Temur era (cross-domain narrative). Replace generic Western names/places.
7. ✅ **Mobile-first, portrait orientation, low-bandwidth** — most G5 students access via shared family smartphone; design for that, not desktop
8. ✅ **Variable-ratio reward windows** — Mystery Box opportunity earned via competence; content randomized within earned tier
9. ✅ **Hidden difficulty tiering** — adapts silently; student never sees "you're on Easy"
10. ✅ **30-second productive struggle window** — let student wrestle for ~30 sec before offering hint, never immediate scaffold

---

## 1. Why a Science-specific engine

Universal engine assumes one generic flow. Science Grade 5 in Uzbekistan has constraints the universal flow ignores:

- **Triple-domain textbook** — biology (Ch.1–2), physics/chemistry (Ch.3–7), earth science/geography (Ch.8–10). One Story Mode template can't serve all three.
- **PISA Science L1→L2 transition is the national bottleneck** — baseline 355, target L2 (interpret data, explain familiar phenomena). Every session must scaffold this transition explicitly.
- **Textbook is inquiry-based** — chapters open with `O'ylab ko'ring` (think) and end with `Bilimingizni sinab ko'ring` (test). The engine must mirror this rhythm, not flatten it.
- **`Tadqiqotchilik ko'nikmalari`** (research/inquiry skills) is a transversal competency the textbook tags on every chapter. The engine must surface inquiry as a phase, not bury it inside Story Mode.

---

## 2. Inherited immutables (no override)

From UNIFIED §1, §4, §5:

- **Pre-homework Sessions 0-A (Theme Preview) + 0-B (Flash Cards)** — student-paced, no scoring, no XP, returnable; timer starts only after "Start my Homework" tap
- **7 phases + 16 game mechanics** (Memory Palace standalone #5, Tic-Tac-Toe vs AI #15, Notebook Capture #16 — per UNIFIED 2026-04-07)
- 30–45 min Standard / 45–60 min Extended *(G5 Science target: 35–45 Standard)*
- Flow state 70–80%, adaptive every 3–5 questions *(G5 override: 75–85%, every 3–4, see §0)*
- Bloom's distribution per LU: 4R / 3U / 3Ap / 2An / 1–2 E-C, span ≥4 levels
- Boss is mandatory, tiered (Sub / Big / Mythical)
- Textbook-as-source-of-truth, Stranger Test on Story Mode
- Mandatory tags: `textbook_ref`, `standard_ref`, `pisa_ref` (with `transition_skill`), `blooms_level`, `game_mechanic`

---

## 3. Science Grade 5 — Chapter & Domain Map

| Bob | Title (Uzbek) | English | Domain | PISA sub-domain | Page |
|-----|---------------|---------|--------|------------------|------|
| 1 | Gulli o'simliklar | Flowering plants | Biology — Living systems | Identify/Explain | 8 |
| 2 | Moslanishlar | Adaptations | Biology — Living systems | Interpret evidence | 25 |
| 3 | Moddaning agregat holatlari | States of matter | Phys/Chem — Physical systems | Identify/Explain | 41 |
| 4 | Moddalarning o'zaro ta'siri | Substance interactions | Phys/Chem — Physical systems | Interpret evidence | 60 |
| 5 | Kuchlar | Forces | Physics — Physical systems | Interpret evidence + Inquiry design | 78 |
| 6 | Tovushlar | Sounds | Physics — Physical systems | Identify/Explain | 102 |
| 7 | Magnitlar va magnit kuchi | Magnets and magnetic force | Physics — Physical systems | Identify/Explain | 114 |
| 8 | Atmosfera. Suvning tabiatda aylanishi | Atmosphere, water cycle | Earth — Earth & space systems | Interpret evidence | 125 |
| 9 | Atrof-muhitning ifloslanishi | Environmental pollution | Earth — Earth & space systems | Reflect/Evaluate | 139 |
| 10 | Tabiiy fanlarning hayotga tatbiqi | Science in daily life | Cross-domain | Reflect/Evaluate | 150 |

**Standard code pattern:** `UZ-SCI-5-{TOPIC}-{SEQ}` — e.g., `UZ-SCI-5-FLOWER-01`, `UZ-SCI-5-MAGNET-03`, `UZ-SCI-5-WATERCYC-02`. Alias dotted: `SCI.5.{bob}.{topic}.{seq}`.

---

## 4. PISA Science Mapping — Grade 5 target

Per UNIFIED §3 + §7.3, Grade 5 Science targets **L1 → L2 transition** as the dominant scaffold, with L2 → L3 stretch goals for top quartile.

| PISA Level | What student can do | G5 expected coverage | Bloom's pairing |
|------------|---------------------|----------------------|-----------------|
| L1 | Recall simple scientific facts, recognize familiar phenomena | 30% of tasks | Remember |
| **L2** | **Explain familiar phenomena, identify simple causes** | **40% of tasks (target)** | **Understand, Apply** |
| L3 | Interpret data, evaluate simple evidence | 25% of tasks (stretch) | Analyze |
| L4 | Multi-source synthesis, abstract reasoning | 5% of tasks (Final Boss Hard, top decile only) | Evaluate |
| L5–L6 | Mythical Boss only (<5% random) | n/a | Create |

**Mandatory transition_skill tags for Grade 5 Science:**
- `L1→L2: explain familiar phenomena from observation`
- `L1→L2: identify a simple cause-effect relationship`
- `L2→L3: interpret a simple data table or diagram`
- `L2→L3: design a fair test (control variables)`
- `L3→L4: integrate evidence from two different sources`

Every task in DRAFT without one of these tags is rejected by content review.

---

## 4.5. Pre-homework Sessions (0-A and 0-B)

Per UNIFIED §4.4 + §4.5 (updated 2026-04-07). These run **before** the 7-phase engine. Timer does not start until the student taps **"Start my Homework"**. No XP, no scoring, no penalties.

### Session 0-A — Theme Preview (Swipe Deck)

**Duration:** 2–4 min, student-paced (Science G5: target 3 min)
**Format:** Vertical swipe deck (TikTok/Tinder-style cards), one component per card, swipe up/down to navigate, may skip
**Tier:** AI Tier 2 generates personalized framing per student PISA level + interests
**Mandatory 8 components per card (UNIFIED §4.4):**

| # | Component | Science G5 instantiation |
|---|-----------|---------------------------|
| 1 | Summary of Book Content | 2-3 sentence textbook chapter summary in Uzbek (Lexile 800-900L) |
| 2 | Better Explanation | Same concept rephrased with metaphor + concrete analogy |
| 3 | Examples | 2-3 short examples (Concrete → Pictorial, never Abstract-only here) |
| 4 | Real-Life Research | Local Uzbek context — *"Aral dengizi qurib bormoqda — nima uchun?"*, *"Ulug'bek rasadxonasida yulduzlar qanday o'rganilgan?"* |
| 5 | Personal Hook | Direct "you" framing — *"Sizning telefoningizdagi kompas qanday ishlaydi? Magnit kuchi bor!"* |
| 6 | Why This Matters | Connects to student's life — health, safety, daily decisions |
| 7 | Industry Application | Uzbek professionals — meteorolog, agronom, ekolog, shifokor, muhandis |
| 8 | Additional Materials | Links/embeds: [uz] textbook page video, [ru] secondary resource, [en] simulator/visualization |

**Design rules:**
- No quiz, no pressure, no penalty for skipping
- Visual-first (photo/diagram/short clip preferred over text)
- First-person POV throughout ("you" not "the student")
- Lexile 800–900L, define new terms inline
- **Ends with explicit transition card:** *"Boshlashdan oldin — kerak bo'ladigan asosiy g'oyalar."* (*"Before we start — here are the key ideas you'll need."*) → leads into 0-B

### Session 0-B — Flash Cards

**Duration:** 1–2 min initial pass; **returnable throughout homework via "Flash Cards" button** (NOT a hint — pure reference)
**Format:** Swipeable card pool, one concept per card, no testing
**Tier:** AI Tier 1 (pre-generated per chapter)
**Card pool — must contain (per UNIFIED §4.5):**

- All **Key Formulas** for the chapter (e.g., density formula for Bob 4, force diagram conventions for Bob 5)
- All **Key Concepts** (e.g., *xona qiymati of magnet poles*, *adaptation*, *water cycle stages*)
- All **Key Rules** (e.g., *like poles repel, opposite attract*; *5 or more → round up*; *predator-prey balance*)

**Card structure:** Front = concept name + textbook page; Back = 1-2 sentence definition + image/diagram

**Design rules:**
- One concept per card (no cramming)
- Returnable mid-homework — student can swipe to "Flash Cards" any time except during Boss
- No right/wrong feedback — pure reference
- **Ends with prominent "Boshlash" / "Start my Homework" button.** Only after this button does the timer start and XP accrue.

### Why these matter for Science G5

- **Vocabulary scaffold** — 0-B preloads all new technical terms, satisfying the §0.A "max 1-2 new terms" rule by making the rest *familiar* before the timer starts
- **Cultural priming** — 0-A's Uzbek anchors lock in cultural relevance before the cognitive load begins
- **Anxiety buffer** — student-paced exploration with no penalty respects fragile G5 self-concept (§0.B.1)
- **Fairness for slow readers** — Lexile-controlled, swipeable, no time pressure

---

## 5. Phase-by-phase Science overrides

### Phase 1 — Memory Sprint (≤2 min)

**Inherits universal format.** Science-specific content rules:

- Recall items pull from `Ilmiy atamalar` (glossary) + prior chapter terminology
- Format mix for Science: 50% MC term-definition, 30% Tile Match (term ↔ image/diagram), 20% Sentence Fill (e.g., *"Suv ___ haroratda muzlaydi"*)
- No abstract calculation in Memory Sprint — that belongs in Game Breaks
- Remediation gate: <60% → route to remediation chapter before Story Mode (UNIFIED §5.1)

### Phase 2 — Story Mode (5–7 min standard)

**Science Story Mode template (overrides universal arc):**

```
Phenomenon  →  Predict  →  Observe/Results  →  Explain
```

This is the textbook's own pattern (`O'ylab ko'ring` → activity → explanation). Override the universal Problem-Struggle-Discovery-Solution arc for Science.

**Per-domain Story Mode flavor:**

| Domain | Phenomenon hook | Predict gate | Results gate | Explain gate |
|--------|------------------|---------------|---------------|---------------|
| Biology (Ch.1-2) | Time-lapse / image of plant or animal behavior | "What will happen if…?" multi-choice | Animation or photo sequence | Free-text or scaffolded sentence |
| Phys/Chem (Ch.3-7) | Demo video (water boiling, magnet on iron filings, string vibrating) | Predict outcome with reasoning | Show actual result | Tile-Match cause→effect |
| Earth (Ch.8-9) | Satellite image or weather event | Predict pattern | Reveal data | Why-Chain (2 levels) |

**Stranger Test for Science:** A non-expert must be able to predict and explain using only the phenomenon shown — no prior memorization required. If a student needs to know "water boils at 100°C" before the prediction gate, it's a fail.

**Checkpoints:** 1 prediction + 1 explanation per segment, max 2 retries → simplified scaffold.

### Phase 3 — Game Breaks (6–9 min)

**Science game selection (per UNIFIED §6.1 Decision Table, Science row):**

| Game mechanic | When to use in Science G5 | Bloom's | PISA scaffold |
|---------------|---------------------------|---------|----------------|
| **Tile Match** | Term ↔ diagram (cell parts, magnet poles, water states) | Remember/Understand | L1 |
| **Mystery Box** | "Which substance/force/material is this?" — given clues | Understand/Apply | L1→L2 |
| **Why Chain (2-level)** | Simple cause-effect (heat → melt → liquid) | Apply/Analyze | L2→L3 |
| **Sentence Fill** | Procedural science writing, fill scientific definitions | Understand | L1→L2 |
| **Adaptive Quiz** | Mixed Bloom's checkpoint | Variable | All |
| **Memory Palace** | Glossary load (`Ilmiy atamalar`) | Remember | L1 |
| **Tic-Tac-Toe vs AI** | Recall under stakes (good for periodic review) | Remember | L1 |
| **Sorting Lab** *(new for Science)* | Classify (living/nonliving, magnetic/non-magnetic, solute/solvent) | Understand/Apply | L1→L2 |

**Forbidden / discouraged for Science G5:**
- ❌ **Why-Chain 4+ levels** — too abstract, save for G7+
- ❌ **Creative Lab** — only auto-enabled at PISA L3+, expect <10% of G5 students
- ❌ **Debate** — language load too high, route to Reading instead

**Selection algorithm (3 games per session):**
1. **Reinforcement game** at student's current Bloom's level on the chapter's main concept
2. **Stretch game** one Bloom's level above
3. **Transition-skill game** that explicitly scaffolds the L1→L2 (or L2→L3) skill chosen for the session

### Phase 4 — Real-Life Challenge (3–5 min)

**Science RLC requirements (override universal):**

- **First-person expert POV mandatory** (UNIFIED §5.4) — and the expert must be a Uzbek-context role:
  - Biology → "You are a farmer in Andijon…", "You are a beekeeper…"
  - Phys/Chem → "You are a teacher demonstrating…", "You are a student in your kitchen…"
  - Earth → "You are a meteorologist in Tashkent…", "You are an environmental inspector at Aral Sea…"
- Must invoke the chapter's core concept on a **realistic** local case (not invented "imagine a magic land")
- Multi-path reasoning required: at least two valid approaches accepted by AI Tier 2 evaluator
- **Inquiry hook (Science-specific addition):** every RLC must end with one of: *"What would you measure?"* / *"What would your control group be?"* / *"How would you prove this?"* — this scaffolds `Tadqiqotchilik ko'nikmalari`

### Phase 5 — Consolidation / Mnemonic Lock (3–5 min)

**Default technique:** Memory Palace (mechanic #5, standalone per UNIFIED 2026-04-07) using a culturally-anchored Uzbek location as the loci structure. 5 loci = 5 concepts from the session, each with `concept + visual + recall question`.

**Per-chapter Memory Palace defaults (Science G5):**

| Bob | Palace location | Why this place |
|-----|-----------------|----------------|
| 1, 2 | **Chimgan tog'lari + o'rmon** | Living systems, plant/animal habitats |
| 3, 4 | **Toshkent kimyo laboratoriyasi** (school lab) | States of matter, substance interactions |
| 5 | **Bunyodkor stadioni** | Forces in action — running, jumping, balance |
| 6 | **O'zbek milliy musiqa zali** (chang, dutar, doira) | Sound — strings, vibration, pitch |
| 7 | **Ulug'bek rasadxonasi (Samarqand)** | Magnets, compass, navigation, astronomy heritage |
| 8 | **Registon maydoni + osmon** | Atmosphere, weather, water cycle |
| 9 | **Orol dengizi (Aral Sea)** | Pollution, environmental change, human impact |
| 10 | **Amir Temur muzeyi** | Cross-domain heritage capstone |

**Structure (every chapter follows this):**
1. **5 loci** mapped to 5 concepts from current chapter
2. Each locus card has: location image + concept text + visual mnemonic + 1 recall question
3. **Recall test** at end: 3 questions cycling through loci, no hints
4. Interleaving: 1 of the 5 loci must reference a concept from a prior chapter

**Why Memory Palace as default for Science G5:**
- Pattern recognition strength at this age (§0 qwen findings)
- Spatial reasoning anchor (concrete-visual)
- Cultural anchoring builds identity + relevance
- Meets `Tadqiqotchilik ko'nikmalari` by tying observation to memory

Optional alternative: Adaptive Quiz with instant feedback citing textbook page (use only if Memory Palace was used in prior session — avoid back-to-back same mechanic).

### Phase 6 — Final Boss

**Science boss tier defaults (Grade 5):**

| Student PISA level | Boss tier | HP / pattern | Expected outcome |
|--------------------|-----------|--------------|-------------------|
| Below L1 (baseline ≈355) | **Sub Boss Easy** | 30 HP, L1 questions only | Required win, scaffolded with hints |
| L1–L2 (median G5) | **Sub Boss Medium** | 50 HP, L1–L2 mix | Win expected after 1 retry |
| L2–L3 (top quartile) | **Big Boss** (weekly only) or Sub Boss Hard | 80 HP, L2–L3 mix | Real challenge |
| L3+ (top decile) | **Big Boss** + occasional **Mythical** | 100+ HP, L3–L4 | Stretch |

**Boss content for Science MUST include (5 questions, distribution Easy 40% / Medium 40% / Hard 20%):**
- 1 phenomenon-explanation question (Tier 3 AI evaluates reasoning)
- 1 data-interpretation question (chart, table, or diagram from textbook)
- 1 cause-effect chain question
- 1 vocabulary/recall question (anchors L1)
- Optional Hard: 1 inquiry-design question (which control variable?) — Sub Boss Hard / Big Boss only

**Each Boss question MUST carry (per Math file precedent + UNIFIED §5.6):**
- Step-by-step worked solution (visible after answer)
- 2-3 progressive **Hints** (revealed on request, not auto-pushed)
- **Common Errors** list — at least 1 known wrong answer with diagnostic explanation (e.g., *"Forgetting to convert to grams — common when reading kg labels"*)

**Difficulty labels (`[EASY]` / `[MEDIUM]` / `[HARD]`) are INTERNAL ONLY** — never shown to student in UI (per §0.B.15 hidden difficulty rule).

**Mastery Stars (1–3) — earned per session:**

| Stars | Condition |
|-------|-----------|
| ⭐ 1 | Boss defeated (any number of attempts within retry limit) |
| ⭐⭐ 2 | Boss defeated in ≤2 attempts AND >50% HP remaining |
| ⭐⭐⭐ 3 | Boss defeated on FIRST attempt, no hints used, >80% HP remaining |

**Failure → Boss Regeneration (UNIFIED 2026-04-07):** If student fails all permitted retries, Tier 3 AI runs **Socratic tutoring** based on the wrong answers, then **regenerates new boss questions** tailored to the gap for the next session continuation. Auto-flags teacher dashboard after **3 failed sessions on the same standard**.

Boss is **mandatory**. Max 2 retries per session; on 2× fail → next session continues from boss with simplified scaffold + Tier 3 Socratic intro (UNIFIED §5.6).

### Phase 7 — Reflection (2–3 min)

**Tier 2 AI generates ONE prompt per session, selected from a bank by accuracy bucket** (per Math file precedent):

| Accuracy bucket | Prompt style | Science G5 example |
|-----------------|--------------|---------------------|
| **≥80% (mastery)** | Strategy reflection — what worked | *"Qaysi strategiya sizga muvaffaqiyat keltirdi? Magnit kuchini tushuntirishda nima yordam berdi?"* |
| **60–79% (passing)** | Struggle + recovery — what was hard, how solved | *"Qaysi savol qiyin bo'ldi? Siz uni qanday hal qildingiz?"* |
| **<60% (Duolingo Mode)** | Support-seeking — what's still unclear | *"Buni yaxshiroq tushunish uchun nima kerak? Qaysi qism chalkash bo'ldi?"* |

**Universal Science prompts (rotate when not bucket-overridden):**
- *"Bugun qaysi tabiat hodisasini yangidan tushundingiz?"*
- *"Tajribangizda nima kutilganidan boshqacha bo'ldi?"*
- *"Bu mavzu kundalik hayotingizda qayerda uchraydi?"*

**Rules:**
- Min 10 characters (teacher configurable up to 5 sentences)
- Bloom's = Create, PISA = L3-4 (metacognitive only — not advanced reasoning)
- **Effort + strategy language only** — never "Were you smart enough?" Always "What strategy did you try?" (§0.B.10)
- Optional peer-explanation prompt: *"Bu mavzuni darsda yo'q bo'lgan do'stingizga qanday tushuntirgan bo'lardingiz?"* — taps peer-explanation effect (qwen findings §3 method #6)

---

## 6. Sample session — Bob 7 (Magnitlar va magnit kuchi)

**Topic:** §7.2 Magnit kuchi
**Standard:** `UZ-SCI-5-MAGNET-02` / alias `SCI.5.7.2.1`
**Textbook ref:** pp. 106–110
**Target PISA transition:** `L1→L2: explain familiar phenomena from observation`
**Mode:** Standard

| Phase | Time | Content |
|-------|------|---------|
| **0-A. Theme Preview** *(student-paced, no XP)* | 3 min | 8-card swipe deck: summary of magnetic force → metaphor (compass like a "miniature Ulug'bek star-finder") → 2 examples → Real-life: *"Telefoningizdagi kompas magnit ishlatadi"* → Personal hook → Why it matters → Industry (geolog, muhandis) → Materials links |
| **0-B. Flash Cards** *(no XP, returnable)* | 2 min | 6 cards: magnit qutbi / magnetik material / kompas / magnit kuchi / N-S qoidasi / iron filings pattern. Front=term, back=1-2 sentence definition + diagram |
| → **"Boshlash" tap → timer starts** | | |
| 1. Memory Sprint | 2 min | 7 items: glossary terms — Tile Match + MC + Sentence Fill. Pulls 2 items from Bob 4 (interleaving) |
| 2. Story Mode | 7 min | **Phenomenon:** video of iron filings forming pattern around bar magnet → **Predict** checkpoint: "Where will filings be densest?" → **Observe:** show pattern → **Explain** checkpoint: "Why are poles strongest?" (2-level Why Chain) |
| 3. Game Breaks | 8 min | Game 1: Sorting Lab (magnetic vs non-magnetic objects) — reinforcement L1. Game 2: Mystery Box (clues → identify magnetic/non-magnetic) — stretch L2. Game 3: Tic-Tac-Toe vs AI (each move requires answering pole question) — transition L1→L2 |
| 4. Real-Life Challenge | 4 min | *"Siz Toshkent maktabida fizika o'qituvchisisiz. O'quvchi qum qutisida sochto'g'nag'ichini tushirib qo'ydi. Qanday qilib magnit yordamida topasiz? Magnitni qayerda ishlatib BO'LMAYDI?"* (Inquiry hook: *"Qanday tekshirasiz?"*) |
| 5. Consolidation (Memory Palace — Ulug'bek rasadxonasi) | 5 min | 5 loci tied to magnetic concepts: rasadxona darvozasi (compass), Ulug'bek minorasi (magnet poles), katalog xonasi (magnetic materials), kuzatuv ayvoni (Earth's field), markaziy gumbaz (cause-effect chain). Recall test: 3 questions cycling loci |
| 6. Sub Boss Medium | 7 min | 50 HP, 5 questions (E×2, M×2, H×1). Q1: Why does compass needle point north? (phenomenon-explain) Q2: Diagram — predict filings pattern (data interp) Q3: Cause chain — magnet → iron filings → pattern → poles Q4: Vocab MC Q5: Inquiry — what control? Each Q has worked solution + hints + Common Errors list |
| 7. Reflection | 3 min | Tier 2 generates 1 prompt by accuracy bucket. Min 10 chars, effort-praise framing only |
| **Total (timed)** | **36 min** | Standard mode (within 35-45 G5 budget) |
| **Total incl. 0-A + 0-B** | **41 min** | |

**"Did You Know" insights** play during phase transitions (≤8 sec each, AI Tier 2):
- After Story Mode → *"Bilasizmi? Yer sayyorasi ham ulkan magnit — shimolda ham, janubda ham qutblar bor!"*
- After Game Breaks → *"Bilasizmi? Hozirgi kompaslar 1000 yil oldin Xitoyda kashf etilgan, Buyuk Ipak yo'lidan O'rta Osiyoga kelgan."*
- Before Boss → *"Bilasizmi? Eng kuchli magnitlar MRI apparatlarida ishlatiladi — shifokorlar miyangizni shu orqali ko'radi!"*

**Tag check:** ~25 task units total, all carry `textbook_ref=pp.106-110`, `standard_ref=UZ-SCI-5-MAGNET-02`, `pisa_ref={level:2, transition_skill:"L1→L2: explain familiar phenomena from observation"}`, `blooms_level`, `game_mechanic`. ✅

---

## 7. Tagging schema example (one task)

```json
{
  "task_id": "UZ-SCI-5-MAGNET-02-T07",
  "textbook_ref": {
    "book": "Tabiiy fanlar 5-sinf (Grey, 2024)",
    "chapter": 7,
    "section": "7.2",
    "pages": [108, 109]
  },
  "standard_ref": {
    "primary": "UZ-SCI-5-MAGNET-02",
    "alias": "SCI.5.7.2.1"
  },
  "pisa_ref": {
    "domain": "Science",
    "sub_domain": "Identify and explain phenomena",
    "level_target": 2,
    "transition_skill": "L1→L2: explain familiar phenomena from observation"
  },
  "blooms_level": "Understand",
  "game_mechanic": "tile_match",
  "phase": "game_break",
  "prompt_uz": "Quyidagi rasmlarni mos juftlarga ajrating: magnit qutbi ↔ kuchli tortish joyi.",
  "expected_uz": "Shimoliy qutb va janubiy qutb — har ikki uchda tortish kuchi eng katta.",
  "evaluation_tier": 1,
  "estimated_time_sec": 45
}
```

---

## 8. AI tier strategy for Science G5 (cost-aware)

Inherits UNIFIED §13 budget targets ($3–5/student/year).

| Phase | Tier | Why |
|-------|------|-----|
| Memory Sprint | T1 algorithmic | Pre-generated MC/Tile Match items |
| Story Mode | T1 (scripted media + checkpoints) | Static phenomenon videos + scripted gates |
| Game Breaks | T1 algorithmic | Pre-generated game pools per chapter |
| Real-Life Challenge | T2 enhanced logic | Multi-path reasoning evaluation, adaptive prompts |
| Consolidation | T1 + T2 (adaptive) | Standard pool + flow-state adjustment |
| Final Boss | T2 normally; **T3 generative on failure only** | Socratic re-teach + question regeneration |
| Reflection | T2 prompt generation | One AI-tailored prompt per session |

**Vision (T3) usage:** only for occasional Notebook Capture (Science benefits — labeled diagrams, free-body sketches, water cycle drawings). Frequency ~1 per 4 sessions G5 (per UNIFIED §6.8).

---

## 8.5. Assessment, Scoring & Escalation

### Pass threshold
- **60% minimum** to pass session (G5 override §0)
- Below 60% → **Duolingo Mode** triggers automatically

### Score → Reward mapping (per session)

| Score | Rating (Uzbek) | Reward |
|-------|----------------|--------|
| 100% | *Mukammal!* | Confetti, max XP, title: *"Aniq tadqiqotchi"* (Precise researcher) — effort-framed |
| 90–99% | *A'lo!* | Full XP + streak fire animation |
| 80–89% | *Juda yaxshi!* | First-time-80%+ bonus XP |
| 60–79% | *O'tdi!* (Passed) | Standard XP, repass offered (max 2 attempts) |
| <60% | *Hali emas* (Not yet — never "Failed") | Duolingo Mode, 0 XP this attempt |

**Avatar/cosmetic items:** earned only via competence thresholds (per §0.B.6 — never purchasable).

### Duolingo Mode (<60% pass)

1. Identify wrong questions
2. Re-present with additional scaffolding (worked example + hint exposed)
3. Reduce difficulty by 1 tier
4. Repeat until 60% achieved
5. **Auto-flag teacher dashboard after 3 consecutive failed sessions on the same standard** (UNIFIED 2026-04-07)

### Answer checking (dual pathway)

| Task type | Method | Latency |
|-----------|--------|---------|
| MC, Tile Match, Sentence Fill, ordering, binary | Tier 1 rule-based exact match | <100 ms |
| Open reasoning (RLC, Boss explanations, Reflection) | Tier 3 AI semantic evaluation | ≤5 sec, with human fallback if >10 sec |
| Notebook Capture (sketches, diagrams) | Tier 3 vision rubric scoring | ≤10 sec, with human fallback |

---

## 9. Teacher overrides allowed (Science G5)

Per UNIFIED §14:

- ✅ Session mode (Standard 20-30 / Extended 40-50)
- ✅ Boss HP modifier 50–150%
- ✅ Difficulty floor (student PISA ±1)
- ✅ Game pool selection (Auto / Manual)
- ✅ RLC required/optional (default: required for Science)
- ✅ Notebook Capture frequency
- ❌ Cannot override 7-phase structure
- ❌ Cannot skip Boss
- ❌ Cannot disable Stranger Test on Story Mode
- ❌ Cannot remove `transition_skill` tag requirement

---

## 10. Content production checklist (per chapter)

For each of the 10 boblar, content team must produce:

- [ ] 30–50 Memory Sprint items (tagged, mixed Tile Match/MC/Sentence Fill)
- [ ] 1 Story Mode arc per topic section (~3 per chapter), with phenomenon media + 2 checkpoint sets
- [ ] 6–9 Game Break activities across 3+ mechanics
- [ ] 3–5 Real-Life Challenge cases with Uzbek context + multi-path rubric
- [ ] 1 Sub Boss Easy + 1 Sub Boss Medium + 1 Sub Boss Hard question pool
- [ ] 1 Big Boss pool combining 3 weakest standards
- [ ] Reflection prompt bank (5+ prompts)
- [ ] Glossary load (`Ilmiy atamalar`) imported into Memory Palace
- [ ] All items dual-coded (`UZ-SCI-5-...` + alias)
- [ ] All items carry `transition_skill` from §4 list

**Total estimated content per chapter:** ~80–120 task units. **Total for Grade 5 Science:** ~900–1,200 task units.

---

## 11. Open decisions (need stakeholder input)

1. **Notebook Capture default ON or OFF for Science G5?** — UNIFIED says optional G1-4, encouraged G5+. Recommend ON for Science (diagrams are central) but flag for teacher discretion.
2. **Sorting Lab as 15th game mechanic** — currently a Science-specific extension. Either add to universal game roster or keep as Science-only.
3. **Bob 10 (Tabiiy fanlarning hayotga tatbiqi)** — cross-domain capstone. Should it use a unique session template (project-based) instead of standard 7-phase?
4. **PISA L1 floor for low-baseline G5 students** — Uzbek baseline is ~355 (below L2). Should we add a "L0→L1 bridge" phase before Memory Sprint for students below baseline? Not in UNIFIED but may be needed.

---

**End of blueprint.** Ready for content team handoff and stakeholder review. All overrides justified against UNIFIED sections; no immutables violated.
