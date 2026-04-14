# NETS Homework Framework — Grade 5 (Uzbek) — Science (Tabiiy Fanlar)

**Version:** 3.0 (merged)
**Date:** 2026-04-08
**Status:** Production-ready specification — single source of truth for Grade 5 uz Science homework.
**Supersedes:** `NETS-Science-Grade5-Blueprint.md` (v2.0) and `grade5-uz-science-framework.md` (v1.0). Merged document; do not edit those upstream files for Grade 5 Science going forward.

**Pipeline position:**

```
Universal Framework (NETS-Homework-Engine-UNIFIED.md v2.0, 2026-04-07)
        │
        ▼
Psychology Filter (qwen-grade5-psychology-findings.md)
        │
        ▼
THIS DOCUMENT  ←  Grade 5 uz Science adapted spec
        │
        ▼
Per-chapter homework sessions (produced by content team / openclaw)
```

**Source documents:**
- `NETS-Homework-Engine-UNIFIED.md` — master spec (the WHAT)
- `NETS-Homework-Engine-Blueprint.docx` — universal session lifecycle (the HOW)
- `NETS-Homework-Engine-Standards-Summary.docx` — standards/PISA framework
- `NETS-Homework-Engine-Blueprint-Summary.docx` — phase summary
- `qwen-grade5-psychology-findings.md` — Grade 5 cognitive/psychological research
- `5-sinf_tabiiy_2024.pdf` — Grade 5 Science textbook (Aleksandr Grey, Marshall Cavendish, Novda Edutainment 2024)

This is a **delta layer** — overrides, parameter tunings, and Science-specific selections on top of the universal blueprint. Anything not mentioned here inherits from UNIFIED unchanged.

---

## 0. Resolution log — what this merge decided

These are the calls made when v1.0 and v2.0 disagreed:

| Topic | Decision | Source |
|---|---|---|
| Session duration | **35–45 min Standard** (user instruction overrides "tighter" research bound) | User 2026-04-08 |
| Adaptive Quiz | **BANNED** for G5 (IRT feels like endless testing at age 10) | v1.0 §3.5 |
| MC in Boss | **30% allowed** at G5 (universal "no MC" rule too strict) | v1.0 §3.8 |
| Peer Teaching | **BANNED** (Uzbek classroom culture: 35–38 students, teacher-centered) | v1.0 §3.5 |
| Flash Card count | **5–7 cap** (Cowan WM ceiling) | v1.0 §3.B |
| Notebook Capture frequency | **1 in every 3 sessions** (highest priority for Science) | v1.0 §6 |
| Why Chain depth | **2 levels max** (more conservative WM safety) | v2.0 §0.A |
| Boss HP | **Tiered 30/50/80 by PISA level** (differentiated instruction) | v2.0 §5.6 |
| Story Mode segments | **3 segments × 90 sec** structurally + total 5–7 min including game-break interleaving | hybrid |
| Memory Palace vs labeled diagrams | **Labeled diagram recall is default** for Science; Memory Palace is alternative for Bio/Earth chapters where loci feel natural | v1.0 §3.7, v2.0 §5 |
| Anti-cheat cultural framing | **Mother-as-supervisor as collaborative scaffolding** (not cheating) | v1.0 §7 |
| Assessment & scoring system | **Full score→reward table + Duolingo 5-step + dual-pathway checking** | v2.0 §8.5 |
| AI tier cost strategy | **Per-phase T1/T2/T3 budget** ($3–5/student/year) | v2.0 §8 |
| Content production checklist | **§16 with volume estimates** (~900–1,200 task units) | v2.0 §10 |
| Big/Mythical Boss | **Cross-session strategy** preserved from v2.0 | v2.0 §5.6 |

---

## 1. Audience profile

| Dimension | Value (from qwen research) |
|---|---|
| Age | 10–11 years old |
| Cognitive stage | Late concrete operational (Piaget) — concrete reasoning solid, abstract emerging but unreliable |
| Working memory | 4–5 chunks (Cowan, 2001) |
| Sustained academic attention | 20–30 min (35–40 min for gamified content) |
| Reading level | Lexile 830–1010L |
| Receptive vocabulary | 12,000–14,000 words |
| Productive vocabulary | 6,000–8,000 words |
| Metacognitive monitoring accuracy | 0.4–0.5 correlation with actual performance |
| Self-concept fragility | High — public failure causes lasting disengagement |
| Peer comparison sensitivity | Peaks at this age |
| Productive struggle ceiling | ~30 sec before scaffolding required |
| Recovery time after wrong answer | 30–90 sec before re-engagement |
| Schooling structure | Grade 5 = first year of *basic secondary* (transition from primary 1–4) |
| Class size (Uzbek urban) | 35–38 students |
| Device reality | Shared family smartphone — mobile-first non-negotiable |
| Internet | 89–93% mobile penetration (urban 94.3%, rural 92.6%) |
| After-school window | 2–3 hours, peak 17:00–19:00 |
| Primary homework supervisor | Mother (cultural norm, Grades 5–7) |
| Primary language | Uzbek (Latin script). Russian/English allowed in Additional Materials only. |

---

## 2. Subject identity — what is "Grade 5 Tabiiy Fanlar"?

**Tabiiy fanlar** = Natural Sciences. Grade 5 is the **first integrated science course** in the Uzbek curriculum, before students split into Biology / Chemistry / Physics / Geography in Grade 6+.

**Subject scope (broad introductory):**
- Living world (plants, animals, basic anatomy)
- Non-living world (matter, water, air, soil, rocks)
- Earth and sky (day/night, seasons, weather, simple astronomy)
- Phenomena and observation (scientific method at its simplest)
- Environment and conservation (Aral Sea, local ecology)
- Forces, sound, magnetism — physics introductions

**Pedagogical posture:** Science at this age is about *wonder* and *observation*, not jargon mastery. Lean heavily on:
- Concrete phenomena (things you can see, touch, hear, measure)
- Real-world Uzbek examples
- Notebook drawing and observation tasks
- "Why does X happen?" curiosity hooks
- Discovery-story narratives (real scientists making real discoveries)

### Chapter map (textbook source: Tabiiy fanlar 5-sinf, Aleksandr Grey, 2024)

| Bob | Title (Uzbek) | English | Pages | Sessions | Domain |
|---|---|---|---|---|---|
| 1 | Gulli o'simliklar | Flowering plants | 8–24 | 3 | Biology |
| 2 | Moslanishlar | Adaptations | 25–44 | 3 | Biology |
| 3 | Moddaning agregat holatlari | States of matter | 45–59 | 2 | Phys/Chem |
| 4 | Moddalarning o'zaro ta'siri | Substance interactions | 60–73 | 2 | Phys/Chem |
| 5 | Kuchlar | Forces | 74–87 | 2 | Physics |
| 6 | Tovush | Sound | 88–99 | 2 | Physics |
| 7 | Magnitlar va magnit kuchi | Magnets and magnetic force | 100–110 | 2 | Physics |
| 8 | Atmosfera. Suvning tabiatda aylanishi | Atmosphere, water cycle | 111–124 | 3 | Earth |
| 9 | Atrof-muhitning ifloslanishi | Environmental pollution | 125–136 | 2 | Earth |
| 10 | Yer sayyorasining harakati | Earth's motion | 137–164 | 2 | Earth |

**Total:** 10 chapters · 23 sections · ~23 homework sessions to produce.

### Standard code pattern

`UZ-SCI-5-{TOPIC}-{SEQ}` — e.g., `UZ-SCI-5-FLOWER-01`, `UZ-SCI-5-MAGNET-03`. Alias dotted: `SCI.5.{bob}.{section}.{seq}`.

---

## 3. PISA Science mapping — Grade 5 target

Per UNIFIED §3 + §7.3, Grade 5 Science targets **L1 → L2 transition** as the dominant scaffold, with L2 → L3 stretch goals for top quartile.

| PISA Level | What student can do | G5 expected coverage | Bloom's pairing |
|---|---|---|---|
| L1 | Recall simple scientific facts, recognize familiar phenomena | 30% of tasks | Remember |
| **L2** | **Explain familiar phenomena, identify simple causes** | **40% of tasks (target)** | **Understand, Apply** |
| L3 | Interpret data, evaluate simple evidence | 25% of tasks (stretch) | Analyze |
| L4 | Multi-source synthesis | 5% (top decile only) | Evaluate |
| L5–L6 | Mythical Boss only (<5% random) | n/a | Create |

**Mandatory `transition_skill` tags for G5 Science** — every task must carry one of:

- `L1→L2: explain familiar phenomena from observation`
- `L1→L2: identify a simple cause-effect relationship`
- `L2→L3: interpret a simple data table or diagram`
- `L2→L3: design a fair test (control variables)`
- `L3→L4: integrate evidence from two different sources`

DRAFT tasks without one of these tags are rejected by content review.

---

## 4. Psychology filter — applied parameters

The universal blueprint exposes parameters. Grade 5 Science sets them as follows.

### 4.1 Session timing (overrides Universal §4.1)

| Parameter | Universal | Grade 5 Science |
|---|---|---|
| **Standard session total** | 30–45 min | **35–45 min** (includes 0-A + 0-B + 7 phases) |
| **Single phase max** | varies | **5–9 min** (hard ceiling) |
| **Inter-phase break** | varies | **5–15 sec** loading screen with Did You Know |
| **Daily homework cap** | not specified | **1–2 sessions / 30–60 min total** |
| **Recommended deployment window** | not specified | **17:00–19:00** (Uzbek after-dinner norm) |

### 4.2 Difficulty calibration (overrides Universal §9)

| Parameter | Universal | Grade 5 Science |
|---|---|---|
| **Flow state success rate** | 70–80% | **75–85%** (higher floor for kids) |
| **Adapt frequency** | every 3–5 questions | **every 3–4 questions** |
| **Difficulty visibility** | not specified | **HIDDEN** — never label questions internally to UI |
| **Pass threshold** | not specified | **60% minimum** (mastery learning floor for this age) |
| **Tier-down trigger** | <60% | **<70%** (catch slipping students 10 pts earlier) |
| **Productive struggle ceiling** | not specified | **30 seconds** before scaffolding |
| **Wrong answer language** | "Try again" | **"Hali emas" / "Not yet"** (Yeager 2019, +40% persistence) |
| **New technical terms** | not capped | **max 1–2 per session** (vocab ceiling) |
| **New concepts per instruction** | not capped | **max 3** (Cowan WM) |

### 4.3 Banned techniques for G5 Science (filter list)

These are filtered OUT from the universal mechanic/feature roster:

1. ❌ Public displays of wrong answers — fragile self-concept
2. ❌ Absolute-rank leaderboards — only improvement ranking or class goals
3. ❌ Real-time multiplayer competition — skill gaps demoralize
4. ❌ Pure discovery / unbounded sandbox — lacks self-direction
5. ❌ Random rewards without competence link
6. ❌ Purchasable cosmetics — earned only
7. ❌ Abstract-only puzzles — CPA mandatory
8. ❌ Complex multi-step instructions without worked examples
9. ❌ Delayed feedback (>seconds)
10. ❌ "You're smart" / ability praise — use effort + strategy
11. ❌ The word "wrong" — use "not yet" / "close — here's why"
12. ❌ Brain breaks every 5 min — disruptive at this attention span
13. ❌ Learning styles matching (visual/auditory/kinesthetic)
14. ❌ Why Chain ≥3 levels — over WM ceiling
15. ❌ Visible difficulty labels in UI — triggers self-handicapping
16. ❌ Group/peer-correction as primary feedback — solo-first for concept acquisition
17. ❌ **Adaptive Quiz** mechanic — IRT feels like endless test
18. ❌ **Peer Teaching** mechanic — Uzbek classroom culture mismatch

### 4.4 Mandatory additions for G5 Science

1. ✅ **CPA progression** — Concrete → Pictorial → Abstract for every concept (even physics/chem)
2. ✅ **Dual coding** — Story Mode never text-only, image+text always
3. ✅ **Worked example before independent practice**
4. ✅ **Spaced retrieval** — Memory Sprint pulls Day 1/3/7/14, not just current chapter
5. ✅ **Effort + strategy feedback** — never ability framing
6. ✅ **Cultural anchors** — Ulugh Beg, Aral Sea, Registon, Amir Temur, Ibn Sina, Al-Biruni, Al-Khwarizmi
7. ✅ **Mobile-first portrait, low-bandwidth** — shared family smartphone is the access point
8. ✅ **Variable-ratio reward windows** — opportunity earned via competence
9. ✅ **Hidden difficulty tiering** — adapts silently
10. ✅ **30-second productive struggle window** before scaffolding

---

## 5. Pre-homework — Sessions 0-A and 0-B (UNIFIED §4.4 + §4.5)

Both run before the 7-phase engine. Timer does not start until the student taps **"Boshlash" / "Start my Homework"**. No XP, no scoring, no penalties.

### 5.1 Session 0-A — Theme Preview (Swipe Deck)

**Refers to:** Universal §4.4. The 8 panels are mandatory; this section tunes them for Grade 5 Science.

**Duration:** 2–3 min, student-paced
**Format:** Vertical swipe deck (TikTok/Tinder-style cards)
**Tier:** AI Tier 2 generates personalized framing per student PISA level + interests

| Parameter | Universal | Grade 5 Science |
|---|---|---|
| Panel count | 8 mandatory | 8 — unchanged |
| Reading level | not specified | **Lexile 830–1010L**, average sentence ≤14 words, active voice |
| Visual-first ratio | "preferred" | **Mandatory** — every panel leads with photo/diagram/short clip; text is secondary |
| Language | not specified | **Uzbek only** for student-facing text; Russian/English permitted only in Additional Materials |
| POV | first-person | **Second-person Uzbek** — *"Sen bilasanmi…?"* / *"Sen ko'rganmisan…?"* |
| Personal Hook (panel 5) | not specified | Use 10–11 yr old life experiences only: family meals, garden, school walk, weather, animals at home, helping mum, bee stings, grass stains. **Avoid** abstract or pre-teen experiences. |
| Industry Application (panel 7) | not specified | Use jobs G5 students recognize: `shifokor`, `o'qituvchi`, `dehqon`, `asalarichi`, `veterinar`, park ranger, baker, cook. **Avoid** "data scientist," "biotech engineer." |
| Real-Life Research (panel 4) | not specified | Lead with a **named historical scientist** when possible. **Preference order:** Central Asian first (Ibn Sina, Al-Biruni, Ulugh Beg, Al-Khwarizmi), then global (Pasteur, Newton, Curie, Darwin, Linnaeus). **At least 1 in every 5 sessions must feature a Central Asian scientist.** |
| Additional Materials (panel 8) | "any language" | Video > article. YouTube short / 360° photo > written article. Allow English/Russian/Uzbek mix. |
| Animation language | per UI/UX spec | Whoosh + letter-assembly transition between panels — 400ms whoosh + 600ms assembly. Do NOT slow down; fast = engagement at this age. |
| Skip behavior | swipe / dots | Both. Pagination dots double as "I'm done" jump. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate. |
| Did You Know | universal §6.5 | Inject **one** Did You Know themed to upcoming homework topic between panels 4 and 5. |

**Mandatory 8 components** (in order):

1. **Summary of Book Content** — 2-3 sentence textbook chapter summary
2. **Better Explanation** — same concept rephrased with metaphor + concrete analogy
3. **Examples** — 2-3 short examples (Concrete → Pictorial, never abstract-only)
4. **Real-Life Research** — historical/scientific discovery angle, Central Asian scientist preferred
5. **Personal Hook** — direct "you" framing tied to student's daily life
6. **Why This Matters** — connects to safety, health, daily decisions
7. **Industry Application** — Uzbek professionals using this concept
8. **Additional Materials** — links/embeds in any language

**Quality gate:** Run the **"10-year-old Stranger Test"** before publishing. Show the 8 panels to someone who's never seen the textbook. If they can describe the lesson and feel curious, it passes. If lost or bored, rewrite.

### 5.2 Session 0-B — Flash Cards

**Refers to:** Universal §4.5. The carousel is mandatory; this section tunes the deck for Grade 5 Science.

**Duration:** 1–2 min initial pass, **returnable throughout homework via floating "Flash Cards" button** (NOT a hint, no penalty)
**Tier:** AI Tier 1 (pre-generated per chapter)

| Parameter | Universal | Grade 5 Science |
|---|---|---|
| **Card count per session** | not capped | **5–7 cards max** (Cowan WM 4–5 + 1–2 buffer). Never more than 7. |
| Card categories | Formula/Concept/Rule/Definition | Prefer **Concept** and **Definition** — formulas barely exist at G5 |
| One concept per card | mandatory | **Strictly enforced** — no compound cards. If a section has >7 key concepts, split into two sessions. |
| Visual on every card | not specified | **Mandatory** — front shows term + small icon/photo/drawing. Text-only forbidden. |
| Carousel layout | 3D circular | Center 1.0× sharp, neighbors 0.7× blurred. Tap to flip. |
| Flip animation | 500ms | **600ms** for G5 (extra processing time) |
| Tap-to-flip prompt | fades after 2s | Visible **3–4 sec** for first-time confidence |
| Language | not specified | **Uzbek only.** Front in Uzbek; back in plain Uzbek with one Russian/English equivalent in parentheses if commonly bilingual. |
| Cyclic loop | yes | **Yes** — loop "ding" sound when wrapping signals deck completion. |
| Returnable mid-homework | yes | **MANDATORY for Science** — labeled diagram recall in Phase 5 often needs reference. NOT counted as hint. |
| "Boshlash" button styling | per UI/UX | **Visually rewarding** — full-width, primary color (`#10B981` Science emerald accent), gentle pulse animation. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate |

**Quality gate:** Every Flash Card must pass the **"5-second readability test"** — a G5 student reads front, flips, reads back, feels they "got it" in under 5 seconds per side.

---

## 6. The 7-Phase Engine — Grade 5 Science

### 6.1 Phase 1 — Memory Sprint (≤2 min, 5–7 items)

| Parameter | Spec |
|---|---|
| Item count | 5–7 (low end — WM ceiling + warm-up buffer) |
| Format mix | Speed Match (term ↔ image), Quick MC, Sentence Fill. Mix formats. **No pure typed recall** (slow + frustrating). |
| Source | **Spaced retrieval pull** — Day 1 / Day 3 / Day 7 / Day 14 schedule from prior chapters of Tabiiy Fanlar, plus 1–2 items from current chapter glossary |
| Visual scaffolding | Every term must show with its visual representation |
| Streak bonus | Visible at 3+ correct (fire animation) |
| Wrong answer feedback | Immediate, soft, 5–10 sec positive framing window before next question |
| Remediation gate | <60% → route to remediation chapter before Story Mode (UNIFIED §5.1) |

### 6.2 Phase 2 — Story Mode (5–7 min)

**Story arc:** Universal Problem → Struggle → Discovery → Solution maps perfectly to **real scientific discoveries** at this age.

**Structure:** 3 segments × ~90 sec each, interleaved with checkpoint games. Total ~5–7 min including checkpoints.

| Story arc beat | Science version |
|---|---|
| **Problem** | A real natural phenomenon nobody understood. *"In 1769, Captain Cook's sailors were dying. They didn't know why. Their teeth were falling out and their wounds wouldn't heal..."* |
| **Struggle** | Past attempts that failed. *"They tried praying. They tried bloodletting. Nothing worked."* |
| **Discovery** | The concept lands. *"A doctor named James Lind tried something nobody had tried — he gave some sailors lemons..."* |
| **Solution** | Resolution + the principle. *"The lemons saved them. Lind had discovered Vitamin C."* |

**Hard rules for G5 Science Story Mode:**

- **CPA mandatory** — every concept touches Concrete → Pictorial → Abstract. 60–70% of exposures need a concrete or pictorial anchor (Bruner 1966). Skipping concrete = failure.
- **Real historical discoveries preferred** over invented scenarios. Pool: Pasteur's milk experiment, Newton's apple, Galileo's pendulum, Curie's radium, Darwin's finches, Mendeleev's table, Avicenna's medicine treatises, Ulugh Beg's astronomical observations, Al-Biruni's measurements. **Use Central Asian / Islamic Golden Age scientists wherever the topic allows.**
- **Stranger Test** applies: a reader who's never seen the textbook should be able to answer the checkpoint from the narrative alone. If a student needs to know "water boils at 100°C" before the prediction gate, it's a fail.
- **Checkpoint questions are comprehension, not recall.** "Why did Lind's experiment matter?" YES. "What is Vitamin C made of?" NO (that's Memory Sprint).
- **Reading level cap:** Lexile 830–1010L. Average sentence ≤14 words. Avoid passive voice.
- **Max 2 retries per checkpoint** → simplified scaffold version.

**Domain-specific Story Mode tuning:**

| Domain | Phenomenon hook | Predict gate | Results gate | Explain gate |
|---|---|---|---|---|
| Biology (Bob 1–2) | Time-lapse / image of plant or animal behavior | "What will happen if…?" MC | Animation / photo sequence | Free-text or scaffolded sentence |
| Phys/Chem (Bob 3–7) | Demo video (water boiling, magnet on filings, string vibrating) | Predict outcome with reasoning | Show actual result | Tile-Match cause→effect |
| Earth (Bob 8–10) | Satellite image or weather event | Predict pattern | Reveal data | Why-Chain (2 levels) |

### 6.3 Phase 3 — Game Breaks (6–9 min, 3 games)

**Universal rule:** 3 games per session, ≥1 from Interactive Catalog + ≥2 from Default 16. Grade 5 Science overrides the *selection priority*.

**Slot rules for G5 Science:**

> **Slot 1:** Tile Match OR Memory Match Blitz OR Speed Match (visual recognition warmup)
> **Slot 2:** Why Chain (max 2 levels) OR Codebreaker OR Mystery Box (pattern + reasoning)
> **Slot 3:** **Notebook Capture in 1 of every 3 sessions**; otherwise Tic Tac Toe vs AI or Escape Room

**Selection algorithm:**
1. **Reinforcement game** at student's current Bloom's level on chapter's main concept
2. **Stretch game** one Bloom's level above
3. **Transition-skill game** scaffolding the L1→L2 (or L2→L3) skill chosen for the session

### 6.4 Phase 4 — Real-Life Challenge (3–5 min)

**First-person expert POV mandatory** (UNIFIED §5.4). Expert must be a Uzbek-context role:

- Biology → *"Sen bog'bonsen / asalarichisen / veterinarsan…"*
- Phys/Chem → *"Sen fizika o'qituvchisisan / oshpazisan…"*
- Earth → *"Sen meteorologsan / ekologsan / yer o'lchovchisan…"*

**Hard rules:**
- First-person address only. *"Sen bog'bonsen…"* Never *"Salimjon bog'bondir…"*
- **Real Uzbek context preferred** — Aral Sea ecology, Tashkent air quality, cotton agriculture, mountain weather, Silk Road heritage
- **Tricky distractors** — at least one plausible-but-wrong answer requiring reasoning to eliminate
- **Justify your answer** — student MUST explain reasoning; AI evaluates the *reasoning*, not just the choice (UNIFIED §6.7 dual-pathway)
- **Inquiry hook (Science-specific):** every RLC ends with one of: *"Qanday tekshirasiz?"* / *"Qaysi nazorat o'zgaruvchisi bo'lardi?"* / *"Buni qanday isbotlaysiz?"* — scaffolds `Tadqiqotchilik ko'nikmalari`
- **Eligibility gate:** PISA Reading L2+. Below L2 → fallback adaptive scaffolded version (no Adaptive Quiz mechanic, but a simpler text version)

### 6.5 Phase 5 — Consolidation (3–5 min)

**Default technique for G5 Science: Labeled diagram recall.** Show a diagram with labels removed, student fills them back in. Tactile, visual, ties to the CPA stage they came from.

**Per-chapter Phase 5 default:**

| Bob | Diagram template | Labels to fill |
|---|---|---|
| 1 | Flower cross-section | gulbarg, gulkosa, androtsey, ginetsey |
| 2 | Habitat zone diagram | yashash muhiti, moslanish belgilari |
| 3 | States of matter triangle | qattiq / suyuq / gaz, transition arrows |
| 4 | Solution beaker | erituvchi, eruvchi, eritma |
| 5 | Force diagram | tortish, itarish, muvozanat, ishqalanish |
| 6 | Sound wave + ear diagram | manba, to'lqin, quloq |
| 7 | Bar magnet + field lines | N, S qutblar, magnit maydoni |
| 8 | Water cycle | bug'lanish, kondensatsiya, yog'in, oqim |
| 9 | Pollution sources | havo, suv, tuproq ifloslanishi |
| 10 | Earth orbit + tilt | aylanma, ekvator, qutblar, fasllar |

**Alternative technique (Memory Palace) — for Bio + Earth chapters where loci feel natural:**

| Bob | Palace location | Why this place |
|---|---|---|
| 1, 2 | Chimgan tog'lari + o'rmon | Living systems, plant/animal habitats |
| 8 | Registon maydoni + osmon | Atmosphere, weather, water cycle |
| 9 | Orol dengizi (Aral Sea) | Pollution, environmental change, human impact |
| 10 | Ulug'bek rasadxonasi (Samarqand) | Earth motion, astronomy, cultural heritage |

**Structure for Memory Palace alternative:** 5 loci tied to 5 concepts; each locus has location image + concept text + visual mnemonic + 1 recall question. End with 3-question recall test cycling through loci.

**Why labeled diagrams default for Science:** Drawing IS the natural Science assessment. Diagrams beat loci for physics/chem/anatomy at this age. Memory Palace stays as alternative for cultural anchoring on bio/earth chapters.

**Duration cap:** 3–5 min. Should feel calm and confident, not stressful. The "I'm ready" moment before Boss.

### 6.6 Phase 6 — Final Boss / Sub Boss (6–8 min)

**Tiered boss HP defaults (based on student PISA level):**

| Student PISA level | Boss tier | HP | Pattern |
|---|---|---|---|
| Below L1 (baseline ≈355) | Sub Boss Easy | **30 HP** | L1 questions only, scaffolded |
| L1–L2 (median G5) | Sub Boss Medium | **50 HP** | L1–L2 mix, win expected after 1 retry |
| L2–L3 (top quartile) | Sub Boss Hard | **80 HP** | L2–L3 mix, real challenge |
| L3+ (top decile) | Big Boss + occasional Mythical | **80–100 HP** | L3–L4 stretch |

**Boss content for Science MUST include (5 questions, distribution Easy 40% / Medium 40% / Hard 20%):**
- 1 phenomenon-explanation question (Tier 3 AI evaluates reasoning)
- 1 data-interpretation question (chart, table, or diagram from textbook)
- 1 cause-effect chain question
- 1 vocabulary/recall question (anchors L1)
- Optional Hard: 1 inquiry-design question (which control variable?) — Sub Boss Hard / Big Boss only

**MC allowed at G5 Boss:** **Up to 30%** of questions may be multiple choice. Universal "no MC" rule is too strict for this age — pure open reasoning overwhelms WM at 10–11.

**Each Boss question MUST carry:**
- Step-by-step worked solution (visible after answer)
- 2–3 progressive **Hints** (revealed on request, not auto-pushed)
- **Common Errors** list — at least 1 known wrong answer with diagnostic explanation (e.g., *"Forgetting to convert to grams — common when reading kg labels"*)

**Difficulty labels (`[EASY]` / `[MEDIUM]` / `[HARD]`) are INTERNAL ONLY** — never shown to student in UI.

**Mechanics:**
- **Hint tax:** −5 HP each (gentler than universal −10 — encourage hint use over giving up)
- **Combo bonus:** 3 in a row → 2× damage on next
- **Max attempts:** 3, with growth-mindset framing on retry (*"Hali emas — yana bir bor sinaymiz"*)

**Mastery Stars (1–3):**

| Stars | Condition |
|---|---|
| ⭐ 1 | Boss defeated (any number of attempts within retry limit) |
| ⭐⭐ 2 | Boss defeated in ≤2 attempts AND >50% HP remaining |
| ⭐⭐⭐ 3 | Boss defeated on FIRST attempt, no hints used, >80% HP remaining |

**Failure → Boss Regeneration:** If student fails all retries, Tier 3 AI runs **Socratic tutoring** based on wrong answers, then **regenerates new boss questions** tailored to the gap for next session continuation. Auto-flags teacher dashboard after **3 failed sessions on the same standard**.

**Big Boss + Mythical Boss** apply per UNIFIED §5.6, capped at 75–85% target rate within the boss.

### 6.7 Phase 7 — Reflection (1–2 min)

**Duration cap:** 1–2 min only — metacognition is limited at this age (Roebers 2017).

**Tier 2 AI generates ONE prompt per session, selected from a bank by accuracy bucket:**

| Accuracy bucket | Prompt style | Science G5 example |
|---|---|---|
| **≥80% (mastery)** | Strategy reflection — what worked | *"Qaysi strategiya sizga muvaffaqiyat keltirdi? Magnit kuchini tushuntirishda nima yordam berdi?"* |
| **60–79% (passing)** | Struggle + recovery — what was hard, how solved | *"Qaysi savol qiyin bo'ldi? Siz uni qanday hal qildingiz?"* |
| **<60% (Duolingo Mode)** | Support-seeking — what's still unclear | *"Buni yaxshiroq tushunish uchun nima kerak? Qaysi qism chalkash bo'ldi?"* |

**Universal Science prompts (rotate when not bucket-overridden):**
- *"Bugun qaysi tabiat hodisasini yangidan tushundingiz?"*
- *"Tajribangizda nima kutilganidan boshqacha bo'ldi?"*
- *"Bu mavzu kundalik hayotingizda qayerda uchraydi?"*

**Rules:**
- Min 1 sentence (universal asks 10 chars; G5 should not be pushed to write essays)
- Bloom's = Create, PISA = L3-4 (metacognitive only — not advanced reasoning)
- **Effort + strategy language only** — never ability framing
- Privacy: student-only; teacher sees aggregate themes
- Optional peer-explanation prompt (since Peer Teaching mechanic is banned, use as reflection only): *"Bu mavzuni darsda yo'q bo'lgan do'stingizga qanday tushuntirgan bo'lardingiz?"*

---

## 7. Content rules

### 7.1 Narrative voice

| Element | Rule |
|---|---|
| POV | Second-person (*"Sen ko'rasanmi?"*). Never third-person observer. |
| Tone | Curious, warm, never condescending. The student is a smart partner figuring something out alongside the narrator. |
| Language register | Conversational Uzbek. No academic jargon unless explicitly being introduced. |
| Sentence length | Average ≤14 words. |
| Sentence structure | Active voice. *"Asalari guldan gulga uchadi"* YES. *"Changlanish asalari tomonidan bajariladi"* NO. |
| Vocabulary | Stay within ~12,000 word receptive range. Introduce new terms with concrete examples + visual + repeat 3+ times across the session. |
| Cultural anchors | Uzbek names (Gulnara, Bekzod, Aziza, Sardor, Malika, Jasur, Dilnoza, Otabek). Uzbek places (Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral, Charvak, Chimgan). Uzbek food and animals where relevant. |
| Scientist references | Mix global (Newton, Curie, Pasteur, Darwin) with Central Asian (Ulugh Beg, Al-Biruni, Ibn Sina, Al-Khwarizmi). **At least 1 Central Asian scientist per 5 sessions.** |

### 7.2 Visuals

| Rule | Detail |
|---|---|
| Every concept gets a visual | CPA mandatory: real photo OR diagram OR pictorial representation. No text-only concept introductions. |
| Mobile-first sizing | All visuals legible on a 5" smartphone screen. No tiny labels, no fine detail. |
| Animation budget | Universal motion principles (≤800ms, transform+opacity only). |
| Dark mode default | Per UI/UX spec subject color: Science = `#8B5CF6` (purple) primary, `#10B981` (emerald) accent. |

### 7.3 "Did You Know" facts (loading screen + phase transitions)

Per UI/UX spec, loading screens rotate Quote Cards / Fun Facts / Corny Lines. For G5 Science the **Fun Facts pool** should be heavily Science-themed AND age-appropriate:

- ✅ "Did you know? An octopus has three hearts and blue blood."
- ✅ "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey that was still edible."
- ✅ "Did you know? The Sun is so big that one million Earths could fit inside it."
- ✅ "Did you know? Bananas are technically berries, but strawberries aren't."
- ❌ Anything involving death, violence, scary medical facts, complex physics, abstract chemistry

**Quote Cards** for Science loading screens should preferentially cite scientists, especially Central Asian ones — Ibn Sina on observation, Al-Biruni on measurement, Ulugh Beg on the stars.

**Frequency:** 1 Did You Know per phase transition (loading screen, ≤8 sec each, AI Tier 2 generated/curated).

---

## 8. Game catalog selections — final list

### 8.1 Default 16 mechanics — usage at G5 Science

| # | Mechanic | Use? | Notes |
|---|---|---|---|
| 1 | Memory Sprint | YES (P1 default) | Flexible format, mix MC + Speed Match |
| 2 | Spaced Flashcards | YES | Vocabulary recall (also 0-B) |
| 3 | Tile Match | **YES (high priority)** | Visual-concept pairing, peak fit |
| 4 | Sentence Fill | LIMITED | Too text-heavy; sparingly |
| 5 | Memory Palace | YES (alternative) | Bio/Earth chapters only; labeled diagrams default |
| 6 | Story Mode | YES (P2 default) | With story arc + Stranger Test |
| 7 | Adaptive Quiz | **NO** | IRT feels like endless test; G7+ only |
| 8 | Mystery Box | **YES (high priority)** | Case-opening, science questions |
| 9 | Movement Breaks | YES | Optional 30-sec stretch between phases |
| 10 | Why Chain | **YES (high priority, max 2 levels)** | Causal reasoning is heart of science |
| 11 | Peer Teaching | **NO** | Uzbek classroom culture mismatch |
| 12 | Real-Life Challenge | YES (P4 default) | First-person expert POV |
| 13 | Reflection Journal | YES (P7 default) | 1-sentence minimum |
| 14 | Final Boss | YES (P6 default) | Tiered HP, MC 30% allowed |
| 15 | Tic Tac Toe vs AI | YES | Familiar game, recall under stakes |
| 16 | **Notebook Capture** | **YES (HIGHEST priority for Science)** | 1-in-3 sessions minimum |

### 8.2 Interactive Game Catalog 12 — usage at G5 Science

| Mechanic | Use? | Notes |
|---|---|---|
| Tic Tac Toe vs AI | YES | (also in Default 16) |
| Connect Four vs AI | YES | Visual + strategy |
| Codebreaker (Mastermind) | YES | Pattern deduction = scientific method |
| Memory Match Blitz | YES | Photo pairs |
| Reaction Chain | LIMITED | Procedural sequences (water cycle steps) |
| Word Ladder Climb | NO | Language game, not Science fit |
| Puzzle Lock (Sliding) | LIMITED | Ordering tasks (planets by distance) |
| Blackjack 21 | NO | Gambling theme inappropriate |
| Territory Conquest | NO | Geography fit, not Science |
| Escape Room | YES | 4 locks, 5-min limit, science-themed |
| Bridge Builder | NO | Physics-only, save for G8+ |
| Minefield Navigator | NO | Stress-inducing for G5 |

### 8.3 Sorting Lab (Science-specific mechanic)

A simple drag-to-categorize game (living/non-living, magnetic/non-magnetic, solute/solvent, gas/liquid/solid). Not in universal catalog — Science extension. Counts as a Default 16 substitute when relevant.

---

## 9. Notebook Capture — Science task pool

Notebook Capture (Universal §6.8) is the **highest-leverage mechanic** for Grade 5 Science. Use in **1 of every 3 sessions minimum.**

| Task type | Example prompt |
|---|---|
| Labeled diagram | *"Daftaringga gul rasmini chiz va quyidagi qismlarni belgila: gulbarg (petal), poya (stem), barg (leaf), ildiz (root)."* |
| Observation drawing | *"Tashqariga chiq. Bir hashorat yoki o'simlik top. Ko'rganingni chiz. 3 ta narsani belgila."* |
| Process diagram | *"Suvning aylanishini 4 qutida chiz: bug'lanish, bulutlar, yomg'ir, daryo."* |
| Compare and contrast | *"Baliq va qushni yonma-yon chiz. Qanday nafas olishlarini doira ichiga ol."* |
| Map sketch | *"Uyingning xaritasini chiz. Ertalabki quyosh nuri qayerga tushishini belgila."* |
| Hypothesis test | *"2 ta o'simlik ol. Birini deraza yoniga, birini qorong'i shkafga qo'y. 3 kundan keyin ikkalasini chiz."* |
| Measurement record | *"Soyangni soat 8da, peshinda va soat 4da o'lcha. Uchchalasini ham chiz. Nega uzunliklari farqli?"* |

**AI vision evaluation rubric:** Lenient on artistic skill, **strict on conceptual accuracy**. A child's stick-figure drawing of "sun → water → cloud → rain" is a CORRECT water cycle even if it's not pretty.

**Latency:** ≤10 sec Tier 3 vision processing, with human fallback if exceeded.

**Accessibility:**
- Visually impaired → audio task substitute
- Motor disability → teacher toggle OFF
- No notebook → in-app sketch (max 80% XP per UNIFIED §6.8)

---

## 10. Anti-cheat tuning for Grade 5

| Rule | Universal | Grade 5 Science |
|---|---|---|
| Speed anomaly threshold | varies | **Be lenient** — kids click fast or stare for minutes, neither is suspicious |
| Length anomaly | varies | Don't expect long typed answers — short sentences are normal |
| Paste detection | enabled | Keep enabled (mother might be helping by typing) |
| Vocabulary jump | enabled | Calibrate against Lexile 830–1010 baseline |
| Verdict ladder | 0=CLEAN, 1=MONITOR, 2=SOFT_WARNING, 3+=TEACHER_ALERT | Same |
| Soft warning language | not specified | **NEVER blame the child.** Frame as *"Biz X ni payqadik — hammasi yaxshimi?"* |
| **Mother-helping reality** | not addressed | Add a TEACHER_NOTE: *"homework supervision is normal in this culture; treat it as collaborative scaffolding, not cheating."* |

---

## 11. Cultural and regional anchors

### 11.1 Always-include list

- **Names** (rotate): Aziza, Bekzod, Gulnara, Sardor, Malika, Jasur, Dilnoza, Otabek
- **Places**: Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral Sea, Charvak reservoir, Chimgan mountains
- **Foods**: plov, non, somsa, choy, kovurma
- **Animals**: cotton bollworm, snow leopard (Pamir), Bukhara deer, sturgeon (Aral)
- **Plants**: cotton, mulberry, wheat, apricot, walnut
- **Currency**: so'm
- **Scientists**: Ulugh Beg (astronomy), Al-Biruni (measurement, geography), Ibn Sina/Avicenna (medicine), Al-Khwarizmi (math, scientific method roots)

### 11.2 Avoid

- Direct comparisons to Western lifestyles (*"Like an American kid, you..."*)
- Pork or alcohol references
- Politically sensitive topics (Aral Sea OK as environmental, not politicized)
- Anything implying the child's family is poor or struggling

---

## 12. Assessment, scoring & escalation

### 12.1 Pass threshold

- **60% minimum** to pass session (G5 override)
- Below 60% → **Duolingo Mode** triggers automatically

### 12.2 Score → Reward mapping

| Score | Rating (Uzbek) | Reward |
|---|---|---|
| 100% | *Mukammal!* | Confetti, max XP, title: *"Aniq tadqiqotchi"* (Precise researcher) — effort-framed |
| 90–99% | *A'lo!* | Full XP + streak fire animation |
| 80–89% | *Juda yaxshi!* | First-time-80%+ bonus XP |
| 60–79% | *O'tdi!* | Standard XP, repass offered (max 2 attempts) |
| <60% | *Hali emas* (never "Failed") | Duolingo Mode, 0 XP this attempt |

**Avatar/cosmetic items:** earned only via competence thresholds — never purchasable.

### 12.3 Duolingo Mode (<60% pass)

1. Identify wrong questions
2. Re-present with additional scaffolding (worked example + hint exposed)
3. Reduce difficulty by 1 tier
4. Repeat until 60% achieved
5. **Auto-flag teacher dashboard after 3 consecutive failed sessions on the same standard**

### 12.4 Answer checking (dual pathway)

| Task type | Method | Latency |
|---|---|---|
| MC, Tile Match, Sentence Fill, ordering, binary | Tier 1 rule-based exact match | <100 ms |
| Open reasoning (RLC, Boss explanations, Reflection) | Tier 3 AI semantic evaluation | ≤5 sec, human fallback if >10 sec |
| Notebook Capture (sketches, diagrams) | Tier 3 vision rubric scoring | ≤10 sec, human fallback |

---

## 13. AI tier strategy (cost-aware)

Inherits UNIFIED §13 budget targets ($3–5/student/year).

| Phase | Tier | Why |
|---|---|---|
| Session 0-A Theme Preview | T2 | Personalized framing per student profile |
| Session 0-B Flash Cards | T1 | Pre-generated per chapter |
| Memory Sprint | T1 | Pre-generated MC/Tile Match items |
| Story Mode | T1 (scripted media + checkpoints) | Static phenomenon videos + scripted gates |
| Game Breaks | T1 | Pre-generated game pools per chapter |
| Real-Life Challenge | T2 | Multi-path reasoning evaluation, adaptive prompts |
| Consolidation | T1 + T2 | Standard pool + flow-state adjustment |
| Final Boss | T2 normally; **T3 generative on failure only** | Socratic re-teach + question regeneration |
| Reflection | T2 | One AI-tailored prompt per session |
| Notebook Capture | T3 vision | Rubric-driven scoring |
| Did You Know facts | T2 | Curated/generated theme-aware insights |

---

## 14. Teacher overrides

### 14.1 Allowed

- Session mode (Standard 35–45 / Extended 45–60)
- Boss HP modifier 50–150%
- Difficulty floor (student PISA ±1)
- Game pool selection (Auto / Manual)
- RLC required/optional (default: required for Science)
- Notebook Capture frequency

### 14.2 Cannot override

- 7-phase structure
- Sessions 0-A and 0-B (always present)
- Boss is mandatory
- Stranger Test on Story Mode
- `transition_skill` tag requirement
- 60% pass threshold
- Banned mechanics list (§4.3)
- Cultural framing (Uzbek language, anchors)

---

## 15. Tagging schema (per UNIFIED §16)

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

## 16. Content production checklist

For each of the 23 sessions, content team must produce:

- [ ] Theme Preview 8-panel deck (Tier 2 prompt + assets) — Lexile 830–1010L, second-person Uzbek
- [ ] Flash Card pool: 5–7 cards (Concept/Definition prefer; visual mandatory)
- [ ] 30–50 Memory Sprint items (mixed Tile Match/MC/Sentence Fill, spaced retrieval)
- [ ] 1 Story Mode arc (3 segments × 90 sec) with phenomenon media + 2 checkpoint sets, Stranger Test passed
- [ ] 6–9 Game Break activities across 3+ mechanics per slot rules
- [ ] 1 Real-Life Challenge case (first-person expert + Uzbek context + inquiry hook)
- [ ] 1 labeled diagram (default Phase 5) OR Memory Palace (Bio/Earth alternative)
- [ ] 1 Sub Boss Easy + 1 Sub Boss Medium + 1 Sub Boss Hard question pool — each with worked solution + hints + Common Errors
- [ ] 1 Big Boss pool (cross-session, 3 weakest standards)
- [ ] Reflection prompt bank (3 accuracy buckets + 3 universal)
- [ ] 3 Did You Know facts (theme-aware, age-appropriate)
- [ ] All items dual-coded (`UZ-SCI-5-...` + alias)
- [ ] All items carry `transition_skill` from §3 list
- [ ] Notebook Capture task (1 in every 3 sessions)

**Total estimated content per session:** ~80–120 task units. **Total for Grade 5 Science (23 sessions):** ~1,800–2,800 task units.

---

## 17. Sample chapter walkthrough — Bob 1.1 "Gul" (The Flower)

This is the **reference implementation**. Every other chapter session should match this shape.

### 17.1 Session metadata

| Field | Value |
|---|---|
| Bob | 1: Gulli o'simliklar (Flowering plants) |
| Section | 1.1: Gul (The Flower) |
| Textbook pages | 8–11 |
| Standard ref | `UZ-SCI-5-FLOWER-01` / `SCI.5.1.1.1` |
| PISA target | Reading L2, Science L2 |
| Bloom's coverage | Remember, Understand, Apply, Analyze |
| Transition skill | `L1→L2: identify parts of a system from a labeled diagram` |
| Total session time | 38 min (incl. 0-A + 0-B) |
| Mode | Standard |

### 17.2 Pre-Homework

**Theme Preview (8 panels, ~3 min, student-paced):**

1. **Summary** — *"Gul — bu o'simlikning ko'payish a'zosi. Har bir gulda yoshlangan qismlar bor: gulbarg, gulkosa, ginetsey va androtsey."*
2. **Better Explanation** — *"Sen gulni bilasanmi? U faqat go'zal narsa emas. Gul — bu o'simlikning bola ko'rish joyi."*
3. **Examples** — Photo of an apricot blossom (`o'rik guli`), a tulip from Pamir, a cotton flower, each with arrows
4. **Real-Life Research** — *"Carl Linnaeus ismli olim 250 yil avval gullarni o'rganib, har bir o'simlikni guli bo'yicha turkumlash usulini topdi."*
5. **Personal Hook** — *"Sen bahorda bog'da qaysi gullarni ko'rganingni eslaysanmi?"*
6. **Why This Matters** — *"Gullarni tushunsang, qanday qilib mevalar paydo bo'lishini bilasan. O'rik, olma, gilos — hammasi guldan boshlanadi."*
7. **Industry Application** — *"Ziroatchilar gullarni o'rganadi. Asalarichilar gullardan asal yig'adi. Botaniklar yangi gul navlarini yaratadi."*
8. **Additional Materials** — Time-lapse video of a flower opening; 360° photo of Bukhara botanical garden; Russian explainer

**Flash Cards (~2 min, 6 cards):**

| # | Front | Back |
|---|---|---|
| 1 | 🌸 Gulbarg | The colored petal — attracts insects with color and smell |
| 2 | 🌿 Gulkosa | The green sepals at the base — protect the bud |
| 3 | 🌼 Androtsey | The male part (stamens) — makes pollen |
| 4 | 🌱 Ginetsey | The female part (pistil) — receives pollen, becomes fruit |
| 5 | ✨ Changlanish | Pollination — pollen moves from stamen to pistil |
| 6 | 🐝 Asalari | Bees and other insects help carry pollen |

→ **Boshlash** button → timer starts.

### 17.3 The 7-phase session

**Phase 1 — Memory Sprint (2 min, 6 items):** Speed Match + MC drawn from Grade 4 prior knowledge (parts of a plant: barg, ildiz, poya, gul; photosynthesis basics).

**Phase 2 — Story Mode (6 min, 3 × 90 sec segments interleaved with games):**

- **Segment 1 — Problem (90 sec):** *"O'rik daraxti har yili gullaydi, lekin ba'zi yillarda bitta meva ham hosil qilmaydi. Bobur ismli bola buvasidan so'radi: 'Buva, nima uchun gullar bor, lekin meva yo'q?'"*
  - Checkpoint: *"Bobur nimani tushunmadi?"*
- **Game 1 — Tile Match (2 min):** Match 6 photos to terms (gulbarg ↔ petal, etc.)
- **Segment 2 — Struggle/Discovery (90 sec):** Bobur opens a book, sees the stamens and pistil, realizes pollen can't move on its own.
  - Checkpoint: *"Nima uchun chang ginetseyga 'o'zicha' tusha olmaydi?"*
- **Game 2 — Why Chain (2 min, 2 levels max):** Why bees come to flowers → what they carry → result
- **Segment 3 — Solution (90 sec):** Bobur understands pollination. Goes outside to watch bees with new eyes.
  - Checkpoint: *"Bobur o'zining qaysi savoliga javob topdi?"*

**Phase 3 — Game Break finale + Notebook Capture (5 min):** Notebook task — *"Daftaringga oddiy gul rasmini chiz. Quyidagi 4 qismni belgila: gulbarg, gulkosa, androtsey, ginetsey."* AI vision evaluates labels for conceptual correctness; stick figures fully accepted.

**Phase 4 — Real-Life Challenge (4 min):** *"Sen bog'bonsen. O'rik daraxting har bahorda chiroyli gullarga to'la, lekin yozda kamida meva hosil qiladi. Qo'shning bog'i to'liq mevali. Qo'shningdan farqi nima bo'lishi mumkin?"* with 4 plausible distractors. Justification required; AI evaluates reasoning. Inquiry hook: *"Buni qanday tekshirasiz?"*

**Phase 5 — Consolidation (3 min):** **Labeled diagram recall** — show flower diagram from textbook with labels removed; student drags 4 labels back into place.

**Phase 6 — Sub Boss Medium (7 min, 50 HP, 5 questions):**

| # | Question | Type | Difficulty | Damage |
|---|---|---|---|---|
| 1 | *"Gulning erkak qismi nima deyiladi?"* | MC | easy | -10 HP |
| 2 | *"Changlanish nimaga olib keladi?"* | Open reasoning | medium | -15 HP |
| 3 | *"Agar bog'da asalari bo'lmasa, nima sodir bo'ladi va nima uchun?"* | Open reasoning + justification | medium | -15 HP |
| 4 | *"Quyidagi rasmda gulning qaysi qismi yetishmaydi?"* | Diagram interp | medium | -5 HP |
| 5 | *"Bog'bonga ko'proq meva olish uchun bitta maslahat ber. Sababini tushuntir."* | Open reasoning + creative | hard | -5 HP |

Each Q has worked solution + 2-3 hints + Common Errors. Combo bonus 3-in-row → 2× next damage. Hint tax −5 HP. Max 3 attempts with growth-mindset framing.

**Phase 7 — Reflection (2 min):** Tier 2 generates 1 prompt by accuracy bucket. Min 1 sentence. Effort-praise framing only.

**Did You Know facts at phase transitions:**
1. *"Did you know? A single bee visits about 5,000 flowers in one day."*
2. *"Did you know? The biggest flower in the world is called Rafflesia. It smells like rotten meat."*
3. *"Did you know? Without bees, almost all the apricots, apples, and cherries in Uzbekistan would disappear."*

### 17.4 Post-session

Per §12.2 score → reward mapping. Auto-flag teacher if 3 consecutive sub-60% sessions on this standard.

---

## 18. Open questions / things to validate before production

1. **MC at G5 Boss (30%)** — needs approval from product/pedagogy lead
2. **Mother-as-supervisor anti-cheat framing** — confirm with Uzbek teachers
3. **Notebook Capture frequency 1-in-3** — may be too much given mother is supervisor; verify
4. **PISA Reading L2 gate for RLC** — many G5 students will be below L2; design fallback explicitly
5. **Did You Know fact pool** — needs Uzbek-language curation
6. **Central Asian scientist content accuracy** — verify Ibn Sina / Ulugh Beg / Al-Biruni Story Mode material
7. **Adaptive scaffolded fallback for below-L2 students** — needs explicit specification
8. **Bob 10 (Yer sayyorasining harakati) capstone format** — standard 7-phase or project-based?
9. **L0→L1 bridge** — Uzbek baseline (~355) is below L2; should we add a pre-Memory-Sprint bridge phase for below-baseline students?

---

## 19. Production handoff

This framework is the **input contract** for the content team / openclaw when producing per-section homework lessons.

**What every produced session must do:**
1. Match the **shape** of §17 (Theme Preview → Flash Cards → 7 Phases → Post-session)
2. Apply **all** parameters from §4 (timing, difficulty, formats)
3. Use **Uzbek language only** for student-facing text
4. Include **at least one Notebook Capture task** in every 3rd session
5. Include **at least one Did You Know fact** per phase transition
6. Use **first-person Expert POV** for every Real-Life Challenge
7. Use **real historical / cultural anchors** wherever possible
8. Generate boss questions to hit the **75–85% expected success rate**
9. Tag every item with `standard_ref`, `pisa_level`, `transition_skill`, `blooms_level` per §15
10. Validate against §18 Open Questions before deploying

---

## 20. Versioning and review

- **v3.0 (2026-04-08)** — merged from `NETS-Science-Grade5-Blueprint.md` (v2.0) + `grade5-uz-science-framework.md` (v1.0). Resolutions logged in §0.
- **Reviewers needed:** product/pedagogy lead, 1+ Uzbek elementary science teacher, content team lead.
- **Next revision trigger:** after 5+ chapters of Grade 5 Science homework are produced and stress-tested with real students.
- **Sibling adaptations to be created later, same template:**
  - `grades/5/uz/biology/`, `grades/5/uz/math/`, `grades/5/uz/history/`, `grades/5/uz/literature/`, `grades/5/uz/geography/`, `grades/5/uz/english/`, `grades/5/uz/russian/`, `grades/5/uz/native_language/`, `grades/5/uz/informatics/`
  - Russian-language siblings under `grades/5/ru/`

---

**End of framework.** Single source of truth for Grade 5 uz Science homework production going forward.
