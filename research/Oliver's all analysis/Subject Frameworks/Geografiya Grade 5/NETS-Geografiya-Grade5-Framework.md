# NETS Geografiya — Grade 5 Subject Framework

**Version:** 1.0
**Date:** 2026-04-08
**Status:** Production-ready specification — single source of truth for Grade 5 Geografiya homework
**Supersedes:** none (first Geografiya framework)
**Shape:** PISA-rigorous (Science G5 lineage)
**Inherits from:** `NETS-Homework-Engine-UNIFIED.md` v2.0 + `NETS-Homework-Engine-Blueprint.docx` v1.0
**Psychology base:** `Researches/qwen-grade5-psychology-findings.md`
**Textbook source:** Geografiya (Tabiiy geografiya boshlang'ich kursi), 5-sinf (Gulyamov, Qurbonniyozov, Avezov, Saidova, "Mitti Yulduz" Tashkent, 2020, 113pp, ISBN 978-9943-64-87-0-8)

> **Reading order:** §0 first (decisions log), then §2 (subject identity), then §6 (the engine). Everything else is reference.
>
> **One-line summary:** Geografiya G5 is a physical geography course teaching *why* Earth systems work — solar mechanics, plate tectonics, weather, climate zones — anchored in Uzbek regional examples (Aral, Amu-Darya, Tian Shan, Fergana Valley) and Central Asian scholarly heritage (Beruni, Khorazmi, Nasir Khosrow). Uses standard PISA-rigorous shape (Science G5 lineage) with two Geografiya-specific additions: a custom **Map Literacy (ML) track** and a **scholar pairing rule** (every world geographer paired with a Central Asian one).

---

## §0. Resolution Log

Geografiya G5 is the second NETS subject built on the **PISA-rigorous shape** (after Science G5 and Texnologiya G5). It maps cleanly to PISA Science (Earth & space systems) + PISA Reading L1→L2 (map literacy). Unlike Tarbiya or Tasviriy Sanat, it does NOT need a major shape override — the Final Boss, 35–45 min sessions, and standard 7-phase engine all work. The decisions below are deltas, not reinventions.

| # | Conflict | Resolution | Reasoning |
|---|---|---|---|
| 1 | Should Geografiya use Maker-First (Tasviriy Sanat shape) or PISA-rigorous (Science shape)? | **PISA-rigorous.** Textbook is ~45% Earth Science + ~25% Theory + ~20% Map Literacy + only ~5% hands-on. Causal reasoning is the core. | Maker-First would misrepresent the textbook's epistemological core (causal explanation). The hands-on % is too low to drive engine design. |
| 2 | Geography content has TWO domains: Earth science (lithosphere/hydrosphere/atmosphere) AND map literacy (coordinates, scale, symbols). One PISA tag won't cover both. | **Triple-tag strategy:** PISA Science (PRIMARY) + PISA Reading L1→L2 (SECONDARY, for map content) + custom **Map Literacy (ML) track L1→L4** as the practice spine for map skills. | Same pattern as Texnologiya (TR track) and Tasviriy Sanat (VA track). Captures domain-specific skills not in PISA. |
| 3 | Session duration | **35–45 min Standard** (matches Science G5 + Texnologiya G5 — same PISA-rigorous shape) | Consistent within shape family. |
| 4 | Final Boss | **KEEP standard Final Boss** (HP, tiered Easy/Medium/Hard, 30/50/80 HP, max 3 attempts) — unlike Tarbiya/Tasviriy Sanat which replaced it | Geography has objective right answers. Final Boss combat metaphor works fine. |
| 5 | MC in Boss | **30% allowed** at G5 (same as Science) | Universal "no MC" too strict for 10-yr-olds. MC works well for: place identification, climate zone matching, coordinate selection, scale calculation. |
| 6 | Notebook Capture frequency | **1 in every 4 sessions** (lower than Science 1-in-3, much lower than Tasviriy Sanat 1-in-1) | Hands-on is only ~5% of Geografiya. Notebook tasks reserved for: drawing simple weather symbols, sketching landform diagrams, plotting coordinates on a blank grid. Not the engine's core. |
| 7 | What about field observation (weather logs)? | **Optional bonus quest mechanic** — students can log weather observations across multiple sessions. Tracked as a long-arc side quest, not session-blocking. | Real field observation requires multi-day data collection. Single-session homework can't drive it, but a long-arc tracker can. |
| 8 | Map drawing | **NOT a core mechanic.** Students read/interpret maps; they don't draw them at G5. Optional Notebook Capture tasks for *labeling* existing maps (filling in country names, marking coordinates), not creating from scratch. | Textbook explicitly de-emphasizes map creation. Map drawing is more advanced (G6+). |
| 9 | Adaptive Quiz | **BANNED** (same as Science) | IRT feels like endless testing for G5. |
| 10 | Peer Teaching | **BANNED** (same as Science — Uzbek classroom culture, 35–38 students) | Consistent with Grade 5 psychology filter. |
| 11 | Why Chain depth | **Max 2 levels** (G5 working memory) | Universal G5 cap. |
| 12 | Boss HP tiering | **30/50/80 by PISA level** (same as Science) | Differentiated instruction. |
| 13 | Cultural anchoring — Central Asian scholars | **Scholar pairing rule:** every world geographer mentioned must be paired with a Central Asian one. Eratosthenes ↔ Beruni · Ptolemy ↔ Khorazmi · Magellan ↔ Nasir Khosrow · modern European cartography ↔ Mahmud Kashgari linguistic geography. | Same pattern as Tasviriy Sanat's "world master + Uzbek master" pairing. Builds geographic citizenship: Central Asia is not peripheral, it's central. |
| 14 | Uzbek regional content | **Embedded throughout, not segregated.** Every chapter must include at least one concrete Uzbek example: Aral Sea (Bob V Hydrosphere), Amu-Darya / Syr-Darya (V), Tian Shan / Pamir (IV Lithosphere), Fergana Valley tectonic formation (IV), Central Asian climate zone (II + VI), oasis cultural geography (VII). | Textbook itself does this. Don't undo it. |
| 15 | Religious framing | **Hold doctrinally-neutral cultural Islamic warmth** — Beruni, Khorazmi, Nasir Khosrow are referenced as scholars and scientists, not as religious figures. | Matches textbook. Preserve accessibility. |
| 16 | Mother-as-helper | **Welcomed for map reading and weather observation** (multi-generational geographic knowledge is part of Uzbek family tradition). Anti-cheat does not penalize. | Same pattern as Science / Texnologiya. |
| 17 | Pass threshold | **60% minimum** (same as Science) | G5 universal floor. |
| 18 | Flow target | **75–85%** (tighter than universal 70–80%) | Same as Science — kids need higher floor. |
| 19 | Visible difficulty labels | **Hidden** (UNIFIED immutable) |  |
| 20 | Standards code prefix | `UZ-GEO-5-{TOPIC}-{SEQ}` primary; `GEO.5.{BOB}.{SEQ}` alias |  |

**20 resolutions logged. The single most important insight: Geografiya is a PISA-Science clone with two custom additions — the ML track and the scholar pairing rule.**

---

## §1. Audience Profile

**Inherited from `qwen-grade5-psychology-findings.md` §1–2 + §7 (universal Grade 5 Uzbek base).** Geografiya-specific deltas noted inline.

**Cognitive (universal G5):**
- Late concrete operational (Piaget); abstract reasoning emerging
- Working memory 4–5 chunks (Cowan 2001) → max 3 new geographic concepts per session
- Sustained attention 20–30 min academic, 35–40 min for engaging content
- Lexile 830–1010L; receptive vocab ~12–14k
- **Spatial reasoning still developing** — 2D maps before 3D globes; simple coordinate grids before complex projections
- **Scale comprehension is hard at this age** — proportional reasoning is fragile; concrete-pictorial-abstract (CPA) progression mandatory for scale concepts

**Geografiya-specific cognitive load:**
- **"Why" questions are the engine** — Geografiya's core pedagogy is causal explanation (why seasons happen, why mountains form, why deserts exist). G5 students can handle 2-step causation but struggle with 3+ step chains. Why Chain capped at 2 levels enforces this.
- **Coordinate systems are abstract** — latitude/longitude is the most abstract concept in the course. Concrete anchor: "the lines you see on your school globe." Pictorial: simplified grid diagrams. Abstract: numerical coordinates. CPA mandatory.
- **Map symbols are a vocabulary** — like learning a new language. Visual scaffolding mandatory; flash cards essential; spaced retrieval works well.
- **Temporal scale is invisible** — tectonics happens over millions of years; G5 students conceptualize "long ago" but not "200 million years ago." Use comparative anchors ("when dinosaurs lived" / "before humans existed").

**Social/emotional (universal G5):**
- Self-concept fragile under public evaluation (Harter 2012)
- Failure tolerance low — attribute errors to strategy ("you read the legend wrong"), never ability ("you're bad at maps")
- Peer comparison sensitivity high — no leaderboards
- Recovery from negative feedback: 30–90 sec processing time

**Uzbek context:**
- Mother is primary supervisor; mother-as-co-learner welcomed for maps and weather observation
- Shared family smartphone — mobile-first, low-bandwidth
- After-school window 2–3 hrs; peak homework 17:00–19:00
- **Strong cultural pride in Central Asian geographic heritage** — students will recognize Aral, Tian Shan, Samarkand, etc. from family conversation; leverage this.
- Resonant historical figures: **Al-Beruni, Al-Khorazmi, Nasir Khosrow, Mahmud Kashgari, Ibn Sino** (geography overlaps with medicine via climate-and-health writings)

---

## §2. Subject Identity

**Geografiya** = Geography. Grade 5 is the **first year of formal geography education** in the Uzbek curriculum, focused on **physical geography** (Earth as a planet, Earth systems, map literacy). Subtitle: *Tabiiy geografiya boshlang'ich kursi* (Introductory Course in Physical Geography).

**Pedagogical posture:** *Curiosity, observation, explanation.* The textbook teaches by asking "why" — why do seasons change, why are mountains where they are, why do rivers flow toward the sea, why is the Aral Sea shrinking. NETS preserves this rhythm: observation → explanation → application.

**Content domains** (from textbook analysis, organized into 7 Bobs):

1. **Bob I — Geografiya fani va uning rivojlanishi** (Geography as a science and its development) — what is geography, ancient vs. modern, geographers across history
2. **Bob II — Yer — Quyosh sistemasidagi sayyora** (Earth as a planet in the Solar System) — celestial mechanics, Earth's shape/rotation/revolution, seasons, heat zones, coordinates, scale, map symbols
3. **Bob III — Geografik xaritalar** (Geographic maps) — map types, scale, legend, coordinate systems, practical work
4. **Bob IV — Yerning qattiq qobig'i — Litosfera** (Earth's lithosphere) — crust movements, landforms, ocean floor relief, weathering, soil, minerals
5. **Bob V — Yerning suv qobig'i — Gidrosfera** (Earth's hydrosphere) — water cycle, oceans, seas, rivers, lakes, glaciers
6. **Bob VI — Yerning havo qobig'i — Atmosfera** (Earth's atmosphere) — composition, pressure, temperature, wind, weather, climate
7. **Bob VII — Biosfera va inson** (Biosphere and humanity) — ecosystems, human-environment interaction, environmental protection, Uzbek oases

**Standard code prefix:** `UZ-GEO-5-{TOPIC}-{SEQ}` (primary) · `GEO.5.{BOB}.{SEQ}` (alias)

**Textbook source of truth:** Geografiya 5-sinf, Gulyamov et al. 2020. Every NETS task must trace to a Bob + section + page range.

**Chapter map → session map:**

| Bob | Title | Sections | Sessions | Estimated LUs |
|---|---|---|---|---|
| I | Geografiya fani | 2 sections | 2 | ~6 |
| II | Earth as planet | 8 sections | 5 | ~14 |
| III | Maps | 2 sections | 2 | ~6 |
| IV | Lithosphere | 6 sections | 5 | ~14 |
| V | Hydrosphere | 7 sections | 5 | ~14 |
| VI | Atmosphere | 10 sections | 6 | ~16 |
| VII | Biosphere | 4 sections | 3 | ~8 |
| **Total** | **7 Bobs** | **39 sections** | **~28 sessions** | **~78 LUs** |

(Recommend ~85–100 micro-LUs in production for richer content variety.)

---

## §3. PISA Mapping + Map Literacy (ML) Custom Track

Geografiya maps to PISA via a **triple-tagging strategy**.

### Primary tag: PISA Science L1→L2

The dominant fit. Covers all Earth-system content:
- **Earth & space systems** — solar mechanics, seasons, climate zones
- **Physical systems** — tectonics, water cycle, atmospheric processes
- **Living systems** — biosphere, ecosystems
- **Scientific reasoning** — causal explanation ("why" questions are the engine)
- **Evidence & observation** — weather data, map interpretation, observation logs

### Secondary tag: PISA Reading L1→L2

Used **only on map literacy content**:
- Reading maps, atlases, legends
- Interpreting coordinates, scale, symbols
- Locating places, calculating distances
- Cross-referencing thematic maps

### Custom Map Literacy (ML) track — practice spine

Every map-related task carries one ML level:

| Level | Code | Capability | Example task |
|---|---|---|---|
| **ML-L1** | Read symbols | Identify map symbols, legend elements, basic features by name | "Bu xaritada yashil rang nimani anglatadi?" (matching) |
| **ML-L2** | Locate & measure | Find places using coordinates, calculate distance with scale, determine direction with compass/azimuth | "Toshkentning koordinatalari nima? Buxorogacha qancha km?" |
| **ML-L3** | Interpret relationships | Read multiple map features together, explain spatial patterns ("why is this city here?") | "Nima uchun aksariyat shaharlar daryolar bo'yida joylashgan?" |
| **ML-L4** | Synthesize | Combine information from 2+ maps, draw conclusions, predict | "Iqlim xaritasi va relief xaritasini taqqosla. Qaysi mintaqalarda eng ko'p yog'in tushadi?" |

### Distribution targets per session

| Bucket | % of session tasks | Purpose |
|---|---|---|
| PISA Science L1 + ML-L1 | 25% | Memory Sprint, Flash Cards, Phase 3 game (recognition) |
| PISA Science L2 + ML-L2 | 40% | Story Mode comprehension, Game Breaks, Phase 4 RLC |
| PISA Science L2 + ML-L3 | 25% | Phase 4 RLC + Boss medium tier |
| PISA Science L2+ + ML-L4 | 10% | Boss hard tier, stretch tasks |

### Mandatory tagging schema (every task)

Every Geografiya task carries:
- `pisa_science_level` — L1 or L2
- `pisa_reading_l1_l2` — true/false (only on map literacy content)
- `ml_level` — ML-L1 through ML-L4 (only on map content)
- `transition_skill` — narrative description of which capability the task scaffolds (e.g., "ML-L2→L3: take a coordinate-finding skill and use it to explain why settlements cluster along rivers")
- `earth_system` — `lithosphere` / `hydrosphere` / `atmosphere` / `biosphere` / `celestial` / `cartography`
- `textbook_ref` — Bob + section + page range

### Mandatory transition_skill tags for G5 Geografiya

Every task must carry one of:
- `L1→L2: identify a feature on a map and name it correctly`
- `L1→L2: explain a familiar Earth phenomenon with one cause`
- `L1→L2: read map symbols and interpret a simple legend`
- `L2→L3: use coordinates and scale to locate a place and measure distance`
- `L2→L3: interpret a 2-step causal chain (e.g., latitude → temperature → vegetation)`
- `L2→L3: read a thematic map and explain a spatial pattern`
- `L3→L4: combine information from multiple maps to draw a conclusion`
- `L3→L4: predict consequences of an Earth process (climate change → Aral Sea)`

DRAFT tasks without one of these tags are rejected by content review.

---

## §4. Psychology Filter — Applied Parameters

### Session timing
- **Standard session: 35–45 min** (matches Science G5 / Texnologiya G5)
- **Extended session: 45–60 min** (in-class, teacher-led)
- **Single phase max: 5–9 min**
- **Inter-phase break: 5–15 sec** with Did You Know facts
- **1–2 sessions/day max** (30–60 min total)
- **Deploy window: 17:00–19:00**

### Difficulty calibration
- **Flow state success rate: 75–85%** (G5 floor higher than universal 70–80%)
- **Adapt every 3–4 questions**
- **Hidden difficulty tiering**
- **60% pass threshold**
- **Tier-down trigger:** <70% (catch slipping students 10 pts earlier)
- **Productive struggle ceiling: 30 sec** before scaffolding
- **"Hali emas" (Not yet) language** — never "wrong"
- **Max 1–2 new technical terms per session** (geography vocab is dense — vodiy, pasttekislik, materik, qit'a, ekvator, meridian, parallel — must be defined inline with visual)
- **Max 3 new concepts per instruction** (Cowan WM)

### Banned techniques (Geografiya-specific)
1. **Public wrong answers / leaderboards** — Harter 2012
2. **Real-time multiplayer competition** — Dweck 2006
3. **Adaptive Quiz mechanic** — IRT endless-test feeling
4. **Peer Teaching primary feedback** — Uzbek classroom mismatch
5. **Why Chain ≥3 levels** — G5 WM ceiling
6. **Visible difficulty labels** — self-handicapping risk
7. **"You're smart" praise** — ability framing
8. **Brain breaks every 5 min** — disruptive at this attention span
9. **Western-only geographer canon** — must always pair with Central Asian
10. **Forcing students to draw maps from scratch** — too advanced for G5; labeling/annotating only
11. **Memorization-only place lists** — without spatial reasoning context, becomes pure rote
12. **Cosmetics purchasable with money** — UNIFIED rule

### Mandatory inclusions
1. **CPA progression** — Concrete (real photo of feature) → Pictorial (diagram/map) → Abstract (definition/coordinate) for every concept
2. **Dual coding** — every concept gets text + visual
3. **Worked examples before independent practice** — show how to read a coordinate before asking student to find one
4. **Spaced retrieval** — Memory Sprint pulls Day 1/3/7/14
5. **Effort + strategy feedback** — never ability framing
6. **Cultural anchors in every session** — Uzbek places, Central Asian scholars
7. **Scholar pairing rule** — every world geographer paired with Central Asian
8. **Mobile-first portrait, low-bandwidth** — shared family smartphone
9. **30-second productive struggle window** before scaffolding
10. **Hidden difficulty tiering** — adapts silently
11. **Uzbek-first language** for student-facing text

---

## §5. Pre-Homework Sessions 0-A & 0-B

### 0-A Theme Preview (Mavzu Tanishuvi) — 2–3 min

**Format:** 8-panel swipe deck, student-paced, no scoring, no XP, no timer.

**Geografiya 8-panel structure** (example for Bob VI § "Wind types"):

| Panel | Content | Wind types example |
|---|---|---|
| 1. **Sarlavha** | Lesson title + hook image | "Shamol turlari" + photo of wind-shaped trees on Aral Sea coast |
| 2. **Yaxshi tushuntirish** | Concept defined with metaphor | "Shamol — bu havoning yugurishi. Issiq joydan sovuq joyga, yuqori bosimdan past bosimga." |
| 3. **Misollar** | 2–3 visual examples | Daily wind diagram (sea ↔ land) + monsoon diagram + Bukhara desert wind |
| 4. **Hayotiy hikoya** | 3-sentence story featuring a Central Asian scholar | "1000 yil oldin Beruni Khorazmda yashagan. U havo bosimini va shamol yo'nalishini o'rgangan. U birinchilardan bo'lib shamol harakatining sababini tushuntirgan." |
| 5. **Senga taalluqli** | "Have you ever..." direct connection | "Sen yozda Chimgan tog'iga chiqsang, kechqurun salqin shamolni his qilasanmi? Bu nima uchun?" |
| 6. **Nega muhim** | Long-arc significance | "Shamollarni tushunish — havo ob-havosi, qishloq xo'jaligi, hatto sog'liq uchun muhim." |
| 7. **Hayotda qo'llanilishi** | Modern Uzbek context | Wind farms in Uzbekistan, weather forecasting, agriculture |
| 8. **Qo'shimcha materiallar** | Optional extras | Short video of monsoon clouds; map of Uzbekistan wind patterns |

- **Animation:** 400 ms whoosh + 600 ms assembly per panel
- **Pagination dots, swipe forward only,** can skip back
- **No XP, no scoring, no timer**
- **One Did You Know between panels 4–5**
- **Stranger Test:** Could a Grade 5 Uzbek student understand without a teacher? If no, rewrite.

### 0-B Flash Cards (Tezkor Kartochkalar) — 1–2 min

**Format:** 5–7 card carousel, returnable mid-session as reference (not counted as hint).

**Geografiya Flash Card structure:** Each card has:
- **Front:** Concept name (Uzbek) + visual icon or map thumbnail
- **Back:** 1-sentence definition + visual + one concrete example (preferably Uzbek)

**Example cards for Bob VI § Wind types:**
1. Shamol — wind
2. Bosim — pressure
3. Passat shamollari — trade winds
4. Musson — monsoon
5. Mahalliy shamollar — local winds (sea/land breeze)
6. Anemometr — wind speed instrument
7. Shamol gulli (rose of winds) — wind rose diagram

Card flip: 600 ms. Tap-to-prompt visibility 3–4 sec. **Geografiya-specific feature: every card with a place or feature includes a small map thumbnail showing where it is on Earth.**

---

## §6. The 7-Phase Engine — Geografiya G5

**Total session: 35–45 min** (Standard) including 0-A + 0-B + 7 phases.

### §6.1 Phase 1 — Memory Sprint (≤2 min, 5–7 items)

| Parameter | Spec |
|---|---|
| Item count | 5–7 |
| Format mix | Tile Match (place ↔ map symbol, feature ↔ definition), Quick MC (capital city, climate zone, landform name), Sentence Fill (process sequences: "Quyosh nuri Yer yuziga ___ keladi" → tikkadan/qiyalashgan) |
| Source | **Spaced retrieval** Day 1/3/7/14 from prior chapters + 1–2 current chapter glossary terms |
| Visual scaffolding | Every term must show with its visual (real photo, diagram, map snippet) |
| Map symbols | Any map symbol recall gets **priority placement** (visual learning) |
| Streak bonus | 3+ correct → fire animation |
| Wrong answer feedback | Immediate, soft, 5–10 sec positive framing |
| Remediation gate | <60% → route to remediation chapter before Story Mode |

### §6.2 Phase 2 — Story Mode (5–7 min)

**Story arc for Geografiya:** Universal Problem → Struggle → Discovery → Solution maps to **real geographic exploration / phenomenon stories.**

**Structure:** 3 segments × ~90 sec each, interleaved with checkpoint games.

| Story arc beat | Geografiya version |
|---|---|
| **Problem** | A geographer/explorer/scholar faces a question. *"Beruni 1000 yil oldin Yer yumaloqligini bilardi. Lekin u qanday isbotladi?"* / *"Bobur Hindistonga safarida Tian Shan tog'idan o'tdi. U qanday yo'l tanladi?"* |
| **Struggle** | First attempts fail or reveal complexity. *"Beruni quyoshning yer ufqida turishini kuzatdi, lekin javob topmadi. Kerakli asboblar yo'q edi."* |
| **Discovery** | The concept/principle/method is introduced. *"Keyin u o'lchov ipini va astrolyabiyani ishlatib, soyaning uzunligini va quyosh burchagini o'lchadi. Yer aylanasini hisoblab chiqdi."* |
| **Solution** | Character succeeds with the right knowledge. *"Beruni Yer aylanasini 40,000 km deb topdi — bu hozirgi qiymatga juda yaqin!"* |

**Hard rules for G5 Geografiya Story Mode:**
- **CPA mandatory** — every concept touches Concrete (photo/real place) → Pictorial (diagram/map) → Abstract (rule/formula). 60–70% concrete or pictorial anchor.
- **Real geographers / scholars / explorers preferred** over invented scenarios. Pool: Beruni, Khorazmi, Nasir Khosrow, Kashgari, Eratosthenes, Ptolemy, Magellan, Columbus. **Scholar pairing rule applies — every world figure paired with Central Asian.**
- **Stranger Test** applies on every segment.
- **Checkpoint questions are comprehension, not recall.** "Why did the Aral Sea shrink?" YES. "What is the capital of Uzbekistan?" NO (that's Memory Sprint).
- **Reading level cap:** Lexile 830–1010L. Average sentence ≤14 words. Active voice.
- **Max 2 retries per checkpoint** → simplified scaffold version.

**Domain-specific Story Mode tuning:**

| Bob | Story focus | Predict gate | Result gate | Explain gate |
|---|---|---|---|---|
| I (Geography science) | Scholar discovers a method | "What did they need to measure?" | Show the result | "Why does this work?" |
| II (Earth as planet) | Why seasons / day-night happen | "What if Earth's tilt changed?" | Diagram of seasons | "Why is summer hot?" |
| III (Maps) | A traveler needs to find a place | "Which map should they use?" | Show the location | "How did they find it?" |
| IV (Lithosphere) | A mountain forms / a quake happens | "What's moving underground?" | Show tectonic process | "Why does this make mountains?" |
| V (Hydrosphere) | A river / sea changes | "Where does the water come from?" | Show water cycle | "Why is Aral shrinking?" |
| VI (Atmosphere) | A storm / climate phenomenon | "What's making the wind?" | Show pressure/temperature map | "Why does this happen?" |
| VII (Biosphere) | An ecosystem / human impact story | "What lives here?" | Show ecosystem | "What happens if humans change it?" |

### §6.3 Phase 3 — Game Breaks (6–9 min, 3 games)

**Universal rule:** 3 games per session, ≥1 from Interactive Catalog + ≥2 from Default 16.

**Slot rules for G5 Geografiya:**

> **Slot 1:** Tile Match OR Memory Match Blitz (place ↔ symbol, feature ↔ definition, scholar ↔ contribution — visual recognition warmup)
>
> **Slot 2:** Why Chain (max 2 levels) OR Codebreaker OR Mystery Box (causal reasoning, "what's behind the curtain")
>
> **Slot 3:** **Notebook Capture in 1 of every 4 sessions** (label a blank map, draw a weather symbol, plot coordinates on a grid); otherwise Tic Tac Toe vs AI, Escape Room, or Connect Four vs AI

**Selection algorithm:**
1. **Reinforcement game** at student's current Bloom's level on chapter's main concept
2. **Stretch game** one Bloom's level above
3. **Transition-skill game** scaffolding the ML-L1→L2 (or L2→L3) skill chosen for the session

### §6.4 Phase 4 — Real-Life Challenge (3–5 min)

**First-person expert POV mandatory.** Expert must be a Uzbek-context role:

- **Bob I/II:** *"Sen yosh astronommisan… / Sen Beruni davrida yashagansan…"*
- **Bob III (Maps):** *"Sen sayyohsan / xaritashunossan… / Sen ekspeditsiya yetakchisisan…"*
- **Bob IV (Lithosphere):** *"Sen geologsan… / Sen tog'da ish olib boruvchi muhandisansan…"*
- **Bob V (Hydrosphere):** *"Sen gidrologsan… / Sen Aral Sea atrofidagi qishloqlarni o'rganadigan ekologsan…"*
- **Bob VI (Atmosphere):** *"Sen meteorologsan… / Sen sayyohlik agentligida ob-havoni bashorat qilasan…"*
- **Bob VII (Biosphere):** *"Sen ekologsan… / Sen Buxoro mintaqasida tabiat qo'riqxonasi nazoratchisisan…"*

**Hard rules:**
- First-person address only. Never third-person observer.
- **Real Uzbek context preferred** — Aral Sea, Tashkent climate, Fergana Valley, Tian Shan, Amu-Darya, Charvak reservoir, Uzbek mahalla
- **Tricky distractors** — at least one plausible-but-wrong answer requiring reasoning to eliminate
- **Justify your answer** — student MUST explain reasoning; AI evaluates the *reasoning*, not just the choice
- **Map literacy required** — at least one RLC per session involves reading a map or coordinate
- **Eligibility gate:** PISA Reading L2+. Below L2 → fallback adaptive scaffolded version

### §6.5 Phase 5 — Consolidation (3–5 min)

**Default technique for G5 Geografiya: Labeled diagram / map recall.** Show a diagram or blank map with labels removed; student fills them back.

**Per-Bob Phase 5 default:**

| Bob | Diagram template | Labels to fill |
|---|---|---|
| I | Timeline of geographers | Beruni, Khorazmi, Eratosthenes, Magellan, etc. |
| II | Solar system + Earth tilt diagram | Quyosh, Yer, eksis, ekvator, qutblar, mavsumlar |
| III | Map legend + coordinate grid | Belgilar, koordinata, masshtab, kompas |
| IV | Cross-section of Earth + landforms | Qobiq, mantiya, yadro, tog', tekislik, vodiy |
| V | Water cycle diagram | Bug'lanish, kondensatsiya, yog'in, daryo, dengiz |
| VI | Atmosphere layers + pressure diagram | Troposfera, stratosfera, bosim, harorat |
| VII | Ecosystem food web (Uzbek desert/oasis example) | Ishlab chiqaruvchilar, iste'molchilar, parchalovchilar |

**Alternative technique (Memory Palace) — for chapters where spatial walkthrough feels natural:**

| Bob | Palace location | Why this place |
|---|---|---|
| IV (Lithosphere) | Tian Shan tog' tizimi | Mountain types, valleys, mineral resources |
| V (Hydrosphere) | Aral Sea bo'yi | Water cycle, ecological change, river systems |
| VII (Biosphere) | Fergana Valley oasis | Ecosystem zones, human-environment interaction |

**Structure:** 5 loci tied to 5 concepts; each locus has location image + concept text + visual mnemonic + 1 recall question.

**Duration cap:** 3–5 min. Calm, confident, "I'm ready" moment before Boss.

### §6.6 Phase 6 — Final Boss / Sub Boss (6–8 min)

**Tiered boss HP defaults (based on student PISA level):**

| Student PISA level | Boss tier | HP | Pattern |
|---|---|---|---|
| Below L1 (baseline) | Sub Boss Easy | **30 HP** | ML-L1 + PISA Science L1 only, scaffolded |
| L1–L2 (median G5) | Sub Boss Medium | **50 HP** | ML-L1–L2 + Science L1–L2 mix |
| L2–L3 (top quartile) | Sub Boss Hard | **80 HP** | ML-L2–L3 + Science L2 mix, real challenge |
| L3+ (top decile) | Big Boss + occasional Mythical | **80 HP** (Mythical 80–100 per UNIFIED §5.6) | ML-L3–L4 stretch |

**Boss content for Geografiya MUST include (5 questions, distribution Easy 40% / Medium 40% / Hard 20%):**
- 1 place/symbol identification question (Tier 1 rule-based or MC)
- 1 coordinate/scale calculation question (numerical answer or MC)
- 1 causal explanation question ("Why does X happen?" — open reasoning)
- 1 map interpretation question (read a map, answer a spatial question)
- Optional Hard: 1 cross-map synthesis question (combine 2 maps, predict or conclude) — Sub Boss Hard / Big Boss only

**MC allowed at G5 Boss:** **Up to 30%** of questions may be multiple choice.

**Each Boss question MUST carry:**
- Step-by-step worked solution (visible after answer)
- 2–3 progressive **Hints** (revealed on request, not auto-pushed)
- **Common Errors** list — at least 1 known wrong answer with diagnostic explanation

**Difficulty labels (`[EASY]` / `[MEDIUM]` / `[HARD]`) are INTERNAL ONLY** — never shown to student.

**Mechanics:**
- **Hint tax:** −10 HP each (universal default)
- **Combo bonus:** 3 in a row → 2× damage on next
- **Max attempts:** 3, with growth-mindset framing on retry (*"Hali emas — yana bir bor sinaymiz"*)

**Mastery Stars (1–3):**
| Stars | Condition |
|---|---|
| ⭐ 1 | Boss defeated (any number of attempts within retry limit) |
| ⭐⭐ 2 | Boss defeated in ≤2 attempts AND >50% HP remaining |
| ⭐⭐⭐ 3 | Boss defeated on FIRST attempt, no hints used, >80% HP remaining |

**Failure → Boss Regeneration:** If student fails all retries, Tier 3 AI runs **Socratic tutoring** based on wrong answers, then **regenerates new boss questions** tailored to the gap for next session continuation. Auto-flags teacher dashboard after **3 failed sessions on the same standard**.

### §6.7 Phase 7 — Reflection (1–2 min)

**Duration cap:** 1–2 min. Metacognition is limited at this age.

**Tier 2 AI generates ONE prompt per session, selected from a bank by accuracy bucket:**

| Accuracy bucket | Prompt style | Geografiya example |
|---|---|---|
| **≥80% (mastery)** | Strategy reflection — what worked | *"Bugun xaritani o'qishda qaysi usul yordam berdi?"* |
| **60–79% (passing)** | Struggle + recovery — what was hard | *"Qaysi savol qiyin bo'ldi? Sen uni qanday hal qilding?"* |
| **<60% (Duolingo Mode)** | Support-seeking — what's still unclear | *"Buni yaxshiroq tushunish uchun nima kerak?"* |

**Universal Geografiya prompts (rotate when not bucket-overridden):**
- *"Bugun Yerdagi qaysi yangi joyni eslab qolding?"*
- *"Qaysi geografik hodisani sen oilangga tushuntirib bera olasan?"*
- *"Agar sen sayohatga ketsang, qaysi xaritani olib ketgan bo'larding va nega?"*

**Rules:**
- Min 1 sentence
- Bloom's = Create, PISA = L3-4 (metacognitive only)
- **Effort + strategy language only** — never ability framing
- Privacy: student-only; teacher sees aggregate themes
- Optional peer-explanation prompt: *"Bu mavzuni darsda yo'q bo'lgan do'stingizga qanday tushuntirgan bo'lardingiz?"*

---

## §7. Content Rules

### 7.1 Narrative Voice
- POV: Second-person (*"Sen ko'rasanmi?"*)
- Tone: Curious, warm, observation-driven. Student is a young geographer/explorer figuring things out.
- Language register: Conversational Uzbek. Geographic terms defined inline with visual + plain language.
- Sentence length: ≤14 words average.
- Active voice. *"Daryo dengizga oqadi"* YES. *"Dengizga daryo tomonidan suv tashiladi"* NO.
- Vocabulary: ~12,000 receptive ceiling. Define new technical terms with visual + 3+ repetitions.
- **Scholar pairing rule:** every world geographer mentioned must be paired with a Central Asian one in the same lesson.

### 7.2 Visuals
- Every concept has a visual (real photo, map, diagram) — CPA mandatory
- Mobile-first sizing — legible on 5" screen, no tiny labels
- Animation budget: ≤800ms, transform+opacity only
- **Maps are first-class content** — every Bob III, IV, V, VI lesson includes at least one interactive map element
- **Subject color: deep teal `#0D9488` primary + sand `#FCD34D` accent** (signals earth + sky + Uzbek desert; visually distinct from Science purple, Tarbiya gold, Texnologiya amber, Tasviriy Sanat purple+cream)
- Dark mode default per UI/UX spec

### 7.3 "Did You Know" Facts
- Geographic curiosities, age-appropriate
- One per phase transition (~8 sec each)
- **Examples:**
  - "Did you know? Beruni 1000 yil oldin Yer aylanasini deyarli aniq hisoblab chiqqan — uning natijasi hozirgi qiymatdan atigi 200 km farq qilgan."
  - "Did you know? Aral dengizi 60 yil oldin dunyoning 4-eng katta ko'li edi. Bugun u o'z hajmining 10% iga ham yetmaydi."
  - "Did you know? Tian Shan tog'lari hozir ham yiliga 1 cm balandlashmoqda — chunki Hindiston plitasi Osiyo plitasiga bosim o'tkazmoqda."
  - "Did you know? Khorazmi 9-asrda jahonning birinchi yagona xaritasini tuzgan."
- **Avoid:** scary disasters without context, family poverty implications, Western lifestyle comparisons, politics, doctrinal religious framing.

---

## §8. Game Catalog Selections — Geografiya G5

### Default Pool (16 mechanics)

| # | Mechanic | Use? | Notes |
|---|---|---|---|
| 1 | Memory Sprint | YES (P1 default) | Mix MC + Tile Match |
| 2 | Spaced Flashcards | YES | Place names, map symbols, definitions (also 0-B) |
| 3 | Tile Match | **YES (HIGH)** | Place↔symbol, feature↔definition, scholar↔contribution |
| 4 | Sentence Fill | YES | Process sequences (water cycle steps) |
| 5 | Memory Palace | YES (alternative for Phase 5) | Tian Shan, Aral, Fergana Valley walkthroughs |
| 6 | Story Mode | YES (P2 default) | Geographer/explorer narratives, scholar pairing |
| 7 | Adaptive Quiz | **NO** | IRT feels like endless test |
| 8 | Mystery Box | **YES (HIGH)** | "What's hidden under this map area?" — material/feature reveal |
| 9 | Movement Breaks | YES | Optional 30-sec stretch |
| 10 | Why Chain | **YES (HIGH, max 2 levels)** | Causal reasoning is the heart of Geografiya |
| 11 | Peer Teaching | **NO** | Uzbek classroom culture mismatch |
| 12 | Real-Life Challenge | YES (P4 default) | First-person expert POV, map literacy required |
| 13 | Reflection Journal | YES (P7 default) | 1-sentence minimum |
| 14 | Final Boss | YES (P6 default) | Tiered HP, MC 30% allowed |
| 15 | Tic Tac Toe vs AI | YES | Recreational, no Geografiya content |
| 16 | Notebook Capture | LIMITED (1-in-4 sessions) | Map labeling, diagram completion, weather symbol drawing — not the engine core |

### Interactive Catalog (12 mechanics)

| Mechanic | Use? | Notes |
|---|---|---|
| Tic Tac Toe vs AI | YES | (also in Default 16) |
| Connect Four vs AI | YES | Visual strategy, place classification gates |
| Codebreaker (Mastermind) | YES | "Decode the map symbols" |
| Memory Match Blitz | **YES (HIGH)** | Place photo pairs, scholar/contribution pairs |
| Reaction Chain | LIMITED | Process sequences (water cycle, weather formation) |
| Word Ladder Climb | LIMITED | Geographic vocab chains |
| Puzzle Lock (Sliding) | YES | Ordering tasks (river systems, geological time) |
| Blackjack 21 | NO | Gambling theme inappropriate |
| Territory Conquest | LIMITED | Could fit Geografiya but skip for G5 — too competitive |
| Escape Room | YES | 4 locks, 5-min limit, geography-themed puzzles |
| Bridge Builder | NO | Engineering, off-topic |
| Minefield Navigator | NO | Stress-inducing for G5 |
| **Geografiya-specific: Map Detective** | **YES (NEW)** | Mini-game where student uses coordinates/scale/legend to find a hidden place on a map |

**One Geografiya-only mechanic introduced: Map Detective (Xarita Detektivi)** — student gets 4–5 clues (coordinates, scale measurements, climate hints, landform descriptions) and uses an interactive map to identify the hidden place. Reinforces ML-L2 and ML-L3.

---

## §9. Map Literacy (ML) — Task Pool & Notebook Capture for Geografiya

The **Map Literacy (ML) track** is the practice spine for all map-related content. Notebook Capture is used sparingly (1-in-4 sessions).

### ML task pool

| ML level | Task type | Example |
|---|---|---|
| **ML-L1** | Identify symbols on a legend | "Bu xaritada ko'k chiziq nimani anglatadi?" |
| **ML-L1** | Find a place by name | "O'zbekiston xaritasidan Buxoroni topib ko'rsat" |
| **ML-L2** | Read coordinates | "Toshkentning koordinatalari qanday?" |
| **ML-L2** | Calculate distance with scale | "Buxorodan Samarqandgacha qancha km?" |
| **ML-L2** | Determine direction with azimuth | "Toshkentdan Andijongacha qaysi yo'nalishda boriladi?" |
| **ML-L3** | Read a thematic map | "Iqlim xaritasiga qarab, qaysi mintaqa eng issiq?" |
| **ML-L3** | Explain a spatial pattern | "Nima uchun shaharlar daryolar bo'yida joylashgan?" |
| **ML-L4** | Combine 2+ maps | "Iqlim va relief xaritalarini taqqosla. Qaysi mintaqalarda eng ko'p yog'in tushadi va nima uchun?" |
| **ML-L4** | Predict from a map | "Iqlim o'zgarishi davom etsa, Aral mintaqasi 50 yildan keyin qanday ko'rinishi mumkin?" |

### Notebook Capture for Geografiya (limited)

Used in 1 of every 4 sessions. Tasks:
- **Label a blank map** — student gets a blank Uzbekistan map; AI vision evaluates filled-in labels
- **Draw a weather symbol** — simple icons (sun, rain, wind direction, cloud)
- **Sketch a landform diagram** — cross-section of mountain, river valley, ocean floor
- **Plot coordinates on a grid** — find a place from given coordinates

**AI vision evaluation rubric:** Lenient on artistic skill, **strict on conceptual accuracy.** Stick figures fully accepted. Spelling on labels accepted with reasonable variation.

**Latency:** ≤10 sec Tier 3 vision, with human fallback if exceeded.

**Accessibility:**
- Visually impaired → audio task substitute (describe the map verbally)
- Motor disability → teacher toggle OFF
- No notebook → in-app sketch (max 80% XP per UNIFIED §6.8)

---

## §10. Anti-Cheat Tuning for Grade 5 Geografiya

| Rule | Universal | Grade 5 Geografiya |
|---|---|---|
| Speed anomaly threshold | varies | **Be lenient** — kids click fast or stare at maps for minutes |
| Length anomaly | varies | Don't expect long typed answers |
| Paste detection | enabled | **Keep enabled** (parents may help type) |
| Vocabulary jump | enabled | Calibrate against Lexile 830–1010 + geographic terms |
| Verdict ladder | 0=CLEAN, 1=MONITOR, 2=SOFT_WARNING, 3+=TEACHER_ALERT | Same |
| Soft warning language | not specified | **NEVER blame the child.** *"Biz X ni payqadik — hammasi yaxshimi?"* |
| **Mother/family helping reality** | not addressed | TEACHER_NOTE: *"For Geografiya, family helping with maps and atlas reading is welcomed — multi-generational geographic knowledge is part of Uzbek family tradition."* |
| **Map screenshot detection** | not specified | If student uploads what looks like a screenshot of a published map for a Notebook Capture task → MONITOR + soft prompt: "Bu xaritani sen chizganmisan?" Never accusatory. |

---

## §11. Cultural and Regional Anchors

### 11.1 Always-Include List

**Names** (rotate): Aziza, Bekzod, Gulnora, Sardor, Malika, Jasur, Dilnoza, Otabek, Farrux, Nodira, Komila, Anvar

**Uzbek places (heavily used):**
- **Cities:** Tashkent, Samarkand, Bukhara, Khiva, Fergana, Margilan, Andijan, Urgench, Nukus, Termez
- **Mountains:** Tian Shan, Pamir, Chimgan, Hisar
- **Rivers:** Amu-Darya, Syr-Darya, Zarafshon, Chirchiq
- **Lakes/Reservoirs:** Aral Sea (environmental theme — used carefully), Charvak reservoir
- **Valleys:** Fergana Valley (tectonic formation example)
- **Deserts:** Kyzylkum, Karakum
- **Regions:** Uzbekistan as Central Asia, Silk Road geography

**Central Asian scholars / geographers (scholar pairing rule):**
- **Abu Rayhan Beruni** (973–1048) — Earth radius, Northern Hemisphere globe, geographic descriptions
- **Muhammad al-Khorazmi** (783–850) — "Surat ul-Arz" (Description of the Earth), early world map
- **Nasir Khosrow** (1004–1088) — "Safarnama" (Travel Book), Central Asian geography
- **Mahmud Kashgari** (11th century) — linguistic + geographic documentation (Diwan Lughat al-Turk)
- **Ibn Sino (Avicenna)** (980–1037) — climate-and-health writings, environmental medicine

**World geographers (always paired with Central Asian):**
- Eratosthenes (Earth circumference) ↔ Beruni
- Ptolemy (Geographia, world maps) ↔ Khorazmi
- Magellan / Columbus (exploration) ↔ Nasir Khosrow
- Modern European cartography ↔ Kashgari

**Foods/agriculture (used in biosphere/ecosystem chapters):**
- Cotton (paxta — "white gold"), wheat, mulberry, apricot, walnut, melons, grapes
- Plov, non, somsa, choy

**Currency:** so'm

**Cultural concepts:**
- Oasis (vohas) as engineered cultural artifact — "ariqlar qazish, to'g'on qurish, daryolardan suv chiqarish" (canals, dams, irrigation)
- Mahalla as spatial unit
- Silk Road as geographic-historical context

### 11.2 Avoid

- Direct comparisons to Western lifestyles
- Pork or alcohol references
- Politically sensitive topics (border disputes, ethnic minorities — Aral Sea OK as environmental theme)
- Anything implying the child's family is poor or struggling
- Dangerous natural disaster descriptions without safety/scientific context
- Doctrinal religious framing (scholars referenced as scientists, not as religious figures)
- Ranking Central Asian scholars as "below" world figures — always treat as equal contributors

### 11.3 Did You Know rotation pool

- "Beruni 1000 yil oldin Yer aylanasini hisoblagan."
- "Khorazmi 9-asrda 'Surat ul-Arz' kitobini yozgan."
- "Aral dengizi 1960-yilda dunyoning 4-eng katta ko'li edi."
- "Tian Shan tog'lari hozir ham yiliga 1 cm balandlashmoqda."
- "Fergana vodiysi 100,000 yildan ortiq vaqt davomida tektonik harakatlardan hosil bo'lgan."
- "Dunyodagi eng katta yer osti suv zaxiralaridan biri Qoraqalpog'iston ostida joylashgan."
- "O'zbekistondagi 17,000 dan ortiq daryolar bor — lekin ko'pchiligi mavsumiy."

(Curate ~50–60 facts total for the production pool.)

---

## §12. Assessment, Scoring & Escalation

### 12.1 Pass Threshold
- **60% minimum** to pass session (G5 override)
- Below 60% → **Duolingo Mode** triggers automatically

### 12.2 Score → Reward Mapping

| Score | Rating (Uzbek) | Reward |
|---|---|---|
| 100% | *Mukammal!* | Confetti, max XP, title: *"Geograf"* (Geographer) — effort-framed |
| 90–99% | *A'lo!* | Full XP + streak fire animation |
| 80–89% | *Juda yaxshi!* | First-time-80%+ bonus XP |
| 60–79% | *O'tdi!* | Standard XP, repass offered (max 2 attempts) |
| <60% | *Hali emas* (never "Failed") | Duolingo Mode, 0 XP this attempt |

**Avatar/cosmetic items:** earned only via competence — never purchasable. Geografiya-specific earnables: explorer badges, scholar frames (Beruni frame, Khorazmi frame), map collection items, place stamps (Bukhara stamp, Aral stamp).

### 12.3 Duolingo Mode (<60% Pass)
1. Identify wrong questions
2. Re-present with additional scaffolding (worked example + hint exposed)
3. Reduce difficulty by 1 tier
4. Repeat until 60% achieved
5. **Auto-flag teacher dashboard after 3 consecutive failed sessions on the same standard**

### 12.4 Answer Checking (Dual Pathway)

| Task type | Method | Latency |
|---|---|---|
| MC, Tile Match, Sentence Fill, ordering, binary | Tier 1 rule-based exact match | <100 ms |
| Open reasoning (RLC, Boss explanations, Reflection) | Tier 3 AI semantic evaluation | ≤5 sec, human fallback if >10 sec |
| Notebook Capture (map labels, diagrams) | Tier 3 vision rubric scoring | ≤10 sec, human fallback |

---

## §13. AI Tier Strategy (Cost-Aware)

Inherits UNIFIED §13 budget targets ($3–5/student/year).

| Phase | Tier | Why |
|---|---|---|
| Session 0-A Theme Preview | T2 | Personalized framing per student profile |
| Session 0-B Flash Cards | T1 | Pre-generated per chapter |
| Memory Sprint | T1 | Pre-generated MC/Tile Match items |
| Story Mode | T1 (scripted) + T2 (checkpoint adaptation) | Static narratives + adaptive gates |
| Game Breaks | T1 | Pre-generated game pools |
| Real-Life Challenge | T2 | Multi-path reasoning evaluation |
| Consolidation | T1 + T2 | Standard pool + flow adjustment |
| Final Boss | T2 normal; **T3 generative on failure only** | Socratic re-teach + question regeneration |
| Reflection | T2 | One AI-tailored prompt per session |
| Notebook Capture (1-in-4) | T3 vision | Rubric-driven scoring |
| Did You Know facts | T2 | Curated/generated theme-aware insights |

**Cost projection per session:** ~$0.04–0.05 (T3 vision only on Notebook Capture sessions)
**Cost projection per year:** ~28 sessions × $0.04 + ~7 vision calls × $0.02 ≈ **~$1.26/student/year** — well within $3–5 envelope.

---

## §14. Teacher Overrides

### 14.1 Allowed
- Session mode (Standard 35–45 / Extended 45–60)
- Boss HP modifier 50–150%
- Difficulty floor (student PISA ±1)
- Game pool selection (Auto / Manual)
- RLC required/optional (default: required)
- Notebook Capture frequency (default 1-in-4, can adjust 1-in-2 to 1-in-6)
- Map Detective availability per session
- Did You Know fact pool (default ↔ teacher-curated subset)

### 14.2 Cannot Override
- 7-phase structure
- Sessions 0-A and 0-B (always present)
- Boss is mandatory
- Stranger Test on Story Mode
- `transition_skill` tag requirement
- 60% pass threshold
- Banned mechanics list (§4.3)
- Cultural framing (Uzbek language, scholar pairing rule)
- ML track tagging requirement on map content
- Doctrinally-neutral framing of Central Asian scholars

---

## §15. Tagging Schema (per UNIFIED §16)

```json
{
  "task_id": "UZ-GEO-5-WIND-03-T07",
  "subject": "Geografiya",
  "grade": 5,
  "language": "uz",
  "textbook_ref": {
    "book": "Geografiya 5-sinf (Gulyamov et al. 2020)",
    "bob": 6,
    "section": "§24",
    "section_title": "Shamol turlari",
    "pages": [82, 84]
  },
  "standard_ref": {
    "primary": "UZ-GEO-5-WIND-03",
    "alias": "GEO.5.6.24"
  },
  "pisa_ref": {
    "domain": "Science",
    "sub_domain": "Earth & space — atmosphere",
    "level_target": 2,
    "transition_skill": "L1→L2: explain a familiar Earth phenomenon with one cause"
  },
  "pisa_reading_l1_l2": false,
  "ml_level": null,
  "earth_system": "atmosphere",
  "blooms_level": "Understand",
  "game_mechanic": "tile_match",
  "phase": "game_break",
  "prompt_uz": "Quyidagi shamol turlarini moslashtiring: Passat — ekvator atrofi, Musson — Hindiston okeani, Mahalliy — dengiz qirg'oqlari.",
  "expected_uz": "Passat → ekvator atrofi, Musson → Hindiston okeani, Mahalliy → dengiz qirg'oqlari",
  "evaluation_tier": 1,
  "estimated_time_sec": 45,
  "cultural_anchors_used": ["Beruni atmosfera kuzatishlari"],
  "scholar_pairing": ["Beruni", "Eratosthenes"],
  "is_safety_critical": false
}
```

---

## §16. Content Production Checklist

For each of the ~28 sessions:

- [ ] Theme Preview 8-panel deck (Tier 2 prompt + assets) — Lexile 830–1010L, second-person Uzbek, scholar pairing applied
- [ ] Flash Card pool: 5–7 cards (visual mandatory — place photos, map snippets, diagram thumbnails)
- [ ] 30–50 Memory Sprint items (mixed Tile Match/MC/Sentence Fill, spaced retrieval)
- [ ] 1 Story Mode arc (3 segments × 90 sec) with geographer/explorer narrative + scholar pairing + 2 checkpoint sets, Stranger Test passed
- [ ] 6–9 Game Break activities across 3+ mechanics per slot rules
- [ ] 1 Real-Life Challenge case (first-person expert + Uzbek context + map literacy + inquiry hook)
- [ ] 1 labeled diagram (default Phase 5) OR Memory Palace (Tian Shan / Aral / Fergana alternative)
- [ ] 1 Sub Boss Easy + 1 Sub Boss Medium + 1 Sub Boss Hard question pool — each with worked solution + hints + Common Errors
- [ ] 1 Big Boss pool (cross-session, 3 weakest standards)
- [ ] Reflection prompt bank (3 accuracy buckets + 3 universal)
- [ ] 3 Did You Know facts (theme-aware, age-appropriate, geographic)
- [ ] All items dual-coded (`UZ-GEO-5-...` + alias)
- [ ] All items carry `transition_skill` from §3 list
- [ ] All map-related items tagged with `ml_level`
- [ ] All items tagged with `earth_system`
- [ ] Notebook Capture task (1 in every 4 sessions)
- [ ] Scholar pairing applied wherever a world geographer is mentioned

**Total estimated content per session:** ~80–120 task units
**Total for Grade 5 Geografiya (~28 sessions):** ~2,200–3,400 task units

Plus production pools:
- ~30 scholar pairing entries (world ↔ Central Asian)
- ~50–60 Did You Know facts
- ~80 map snippets / diagrams (legend, scale bars, coordinate grids, water cycle, atmosphere layers, etc.)
- ~12 NPC dialogue trees (cross-subject NPC reuse from Tarbiya/Tasviriy Sanat where appropriate)
- ~6 Memory Palace location sets (Tian Shan, Aral, Fergana, Charvak, Bukhara desert edge, Tashkent metro)

---

## §17. Sample Chapter Walkthrough — Bob VI § 24 "Shamol Turlari" (Wind Types)

**This is the reference implementation. Every other chapter session should match this shape.**

### 17.1 Session Metadata

| Field | Value |
|---|---|
| Bob | VI: Yerning havo qobig'i — Atmosfera (Atmosphere) |
| Section | § 24: Shamol turlari (Wind types) |
| Textbook pages | 82–84 |
| Standard ref | `UZ-GEO-5-WIND-03` / `GEO.5.6.24` |
| PISA target | Science L2, ML-L2 |
| Earth system | Atmosphere |
| Bloom's coverage | Understand, Apply (with light Remember in P1) |
| Transition skill | `L1→L2: explain a familiar Earth phenomenon with one cause` |
| Total session time | 38 min (incl. 0-A + 0-B) |
| Mode | Standard |
| Scholar pairing today | Beruni ↔ Eratosthenes (atmospheric observation) |

### 17.2 Pre-Homework

**Theme Preview (8 panels, ~3 min):**

1. **Summary** — *"Shamol — bu havoning bir joydan ikkinchi joyga harakati. Issiq joydan sovuq joyga, yuqori bosimdan past bosimga oqadi."*
2. **Better Explanation** — *"Tasavvur qil: yozda dengiz bo'yida turibsan. Kunduzi quruqlik tezroq qiziydi. Issiq havo ko'tariladi, dengizdan sovuq havo uning o'rniga keladi. Bu — kunduzgi shamol."*
3. **Examples** — Photos: Aral Sea coast windmills, Bukhara desert wind, Tian Shan valley breeze
4. **Real-Life Research** — *"1000 yil oldin Beruni Khorazmda yashagan. U havo bosimini va shamol yo'nalishini o'rgangan. Bundan ham 1200 yil oldin yunon olimi Eratosfen ham havo harakatini kuzatgan. Ikki olim ham xuddi bir savolga javob izlagan: 'Nima uchun shamol esadi?'"*
5. **Personal Hook** — *"Sen yozda Chimgan tog'iga chiqsang, kechqurun salqin shamolni his qilasanmi? Bu nima uchun?"*
6. **Why This Matters** — *"Shamollarni tushunish — havo ob-havosi, qishloq xo'jaligi, hatto sog'lik uchun muhim."*
7. **Industry Application** — Modern Uzbek wind farms, weather forecasting agencies, agriculture planning
8. **Additional Materials** — Short video of monsoon clouds; map of Uzbekistan wind patterns; Russian/English equivalents (mussonlar — муссоны — monsoons)

*Did You Know between panels 4–5:* "Beruni 1000 yil oldin atmosfera bosimining balandlikka qarab pasayishini tushuntirgan."

**Flash Cards (~2 min, 6 cards):**

| # | Front | Back |
|---|---|---|
| 1 | 💨 **Shamol** (wind) | Havoning harakati. Issiq → sovuq, yuqori bosim → past bosim. |
| 2 | ⚖️ **Bosim** (pressure) | Havoning yer yuziga bosishi. Pasayganda — havo ko'tariladi. |
| 3 | 🌍 **Passat** (trade winds) | Ekvator atrofida doimo esadigan shamollar. Sharqdan g'arbga. |
| 4 | 🌧️ **Musson** (monsoon) | Yozda dengizdan quruqlikka, qishda quruqlikdan dengizga. Hindiston okeani atrofida. |
| 5 | 🏖️ **Mahalliy shamollar** (local winds) | Dengiz–quruqlik shamoli. Kunduzi va kechqurun yo'nalishi o'zgaradi. |
| 6 | 📊 **Shamol gulli** (rose of winds) | Diagramma — qaysi yo'nalishdan eng ko'p shamol esishini ko'rsatadi. |

→ **Boshlash** button → timer starts.

### 17.3 The 7-Phase Session

**Phase 1 — Memory Sprint (2 min, 6 items):** Tile Match (wind type ↔ region) + MC (pressure/temperature relationships) + 1 Sentence Fill ("Shamol ___ bosimdan ___ bosimga esadi"). Pulls 2 items from Bob V (water cycle — connecting hydrosphere ↔ atmosphere).

**Phase 2 — Story Mode (6 min, 3 × 90 sec segments):**

- **Segment 1 — Problem (90 sec):** *"Beruni 1020-yilda Khorazmda kuzatishlar olib borardi. U havoning balandlikka qarab nima uchun yengillashishini tushunmoqchi edi. Uning qo'lida atigi suv idishi va o'lchov tayoqchasi bor edi. U qanday boshladi?"*
  - **Checkpoint:** *"Beruni nima qilishi kerak edi — o'lchov olib borishni davom ettirish, taxmin qilish, yoki kitoblardan o'qish? Nima uchun?"* (3 MC, all defensible — engagement-graded)
- **Game 1 — Tile Match (2 min):** Match 6 wind types to their regions (Passat ↔ ekvator, Musson ↔ Hindiston okeani, Mahalliy ↔ dengiz qirg'oqlari, etc.)
- **Segment 2 — Discovery (90 sec):** "Beruni ikki narsani payqadi: havo issiq joyda yengilroq, sovuq joyda og'irroq. Issiq havo ko'tariladi, sovuq havo pastga tushadi. Bu — shamol harakatining sababi."
  - **Checkpoint:** *"Nega kunduzi dengiz qirg'og'ida shamol dengizdan quruqlikka esadi?"* (open reasoning, Tier 3)
- **Game 2 — Why Chain (2 min, 2 levels max):** Quyosh quruqlikni qizdiradi → Issiq havo ko'tariladi → Dengizdan sovuq havo o'rniga keladi → Mahalliy shamol hosil bo'ladi
- **Segment 3 — Solution (90 sec):** "Beruni o'z kuzatishlarini yozib qoldirgan. Eratosfen ham 1200 yil oldin xuddi shu hodisalarni kuzatgan. Ikki olim, ikki davr — bitta haqiqat. Bugun biz Beruni va Eratosfenga rahmat aytamiz: ular bizga shamollarni tushunishni o'rgatishgan."
  - **Checkpoint:** *"Beruni va Eratosfen orasida 1200 yil farq bor edi. Ikki olim qanday qilib bir xil natijaga keldi?"*

**Phase 3 — Game Break finale (5 min):** Mystery Box — 3 hidden weather phenomena reveals (each is a wind type with a hint, student guesses) + 1 micro-task: "Daftaringga shamol gullini chiz — bizning sinfimizda eng ko'p qaysi yo'nalishdan shamol kelganini bilasanmi?" (optional, no upload required).

**Phase 4 — Real-Life Challenge (4 min):** *"Sen meteorologsan. Toshkentda yozning qoqindiq kunlaridan biri. Soat 14:00. Sening oldingda ikkita xarita: harorat va havo bosimi. Toshkentda harorat 38°, Chimgan tog'larida 22°. Bosim Toshkentda past, Chimganda yuqori. Kechki paytda Toshkentliklar uchun qanday ob-havo bashorati berasan? Va nima uchun?"*

3 options + free text:
1. Issiq, shamolsiz kechki payt
2. **Tog'dan salqin shamol esadi** (correct, with reasoning) — sen tushuntirsang +bonus
3. Yomg'ir yog'adi
4. Boshqa: ___

Tier 3 evaluates reasoning. Justification required.

**Phase 5 — Consolidation (3 min):** **Labeled diagram recall** — show the wind formation diagram (sun heating land, hot air rising, cold air flowing in) with labels removed; student drags 5 labels back into place.

**Phase 6 — Sub Boss Medium (7 min, 50 HP, 5 questions):**

Each carries: `standard_ref`, `pisa_level`, `ml_level`, `transition_skill`, `earth_system`.

| # | Question | Type | Diff | Damage | Tags |
|---|---|---|---|---|---|
| 1 | *"Passat shamollari qaysi mintaqada esadi?"* | MC | easy | −10 | `WIND-03-B1` · Science L1 · ML-L1 · *identify a feature* · atmosphere |
| 2 | *"Quyidagi jarayonlarni to'g'ri tartibga keltir: havo qiziydi → ko'tariladi → sovuq havo o'rniga keladi → shamol hosil bo'ladi."* | Ordering | med | −15 | `WIND-03-B2` · Science L2 · *explain phenomenon with one cause* · atmosphere |
| 3 | *"Toshkent koordinatalarini ber. Uning yaqinida qaysi shamol turi ko'p uchraydi va nima uchun?"* | Open reasoning + map | med | −15 | `WIND-03-B3` · Science L2 + Reading L2 · ML-L2 · *use coordinates to locate a place + interpret pattern* · atmosphere |
| 4 | *"Nima uchun musson Hindistonda esadi, lekin Uzbekistonda emas?"* | Open reasoning | med | −5 | `WIND-03-B4` · Science L2 · *interpret 2-step causal chain* · atmosphere |
| 5 | *"Iqlim xaritasi va relief xaritasini taqqosla. Tian Shan tog' tizimida shamollar qanday yo'naladi va nima uchun?"* | Open reasoning + 2-map synthesis | hard | −5 | `WIND-03-B5` · Science L2 + Reading L2 · ML-L4 · *combine 2 maps to draw conclusion* · atmosphere + lithosphere |

Each Q has worked solution + 2-3 hints + Common Errors. Combo bonus 3-in-row → 2× next damage. Hint tax −10 HP. Max 3 attempts with growth-mindset framing.

**Phase 7 — Reflection (2 min):** Tier 2 generates 1 prompt by accuracy bucket. Min 1 sentence. Effort-praise framing only.

**Did You Know facts at phase transitions:**
1. *"Beruni 1000 yil oldin atmosfera bosimining balandlikka qarab pasayishini tushuntirgan."*
2. *"Hindistondagi musson shamollari 100 milliondan ortiq odamning oziq-ovqat ta'minoti uchun muhim."*
3. *"O'zbekistonda yiliga 200 dan ortiq quyoshli kun bor — bu shamol energiyasi uchun ham yaxshi sharoit yaratadi."*

### 17.4 Post-Session

Per §12.2 score → reward mapping. Auto-flag teacher if 3 consecutive sub-60% sessions on this standard.

---

## §18. Open Questions / Things to Validate Before Production

1. **Map interactivity at scale** — does the platform support pinch-zoom, pan, and tap-to-identify on maps for shared family smartphones with low bandwidth? Engineering review needed.
2. **Scholar pairing accuracy** — verify Central Asian scholar contributions with cultural reviewer + historian. Some pairings (Beruni ↔ Eratosthenes) are clean; others (Kashgari ↔ modern European cartography) may need refinement.
3. **Coordinate calculation as Tier 1** — can the rule-based answer checker handle coordinate input variations (38.5° vs 38°30' vs "38 daraja 30 daqiqa")?
4. **Memory Palace for Tian Shan / Aral / Fergana** — needs UX prototyping; spatial walkthrough on a smartphone is unusual.
5. **Notebook Capture for map labeling** — is 1-in-4 sessions the right frequency? Pilot to validate.
6. **Aral Sea environmental content** — politically sensitive (Soviet-era history). Frame as scientific/environmental story, not political. Validate with Uzbek MoE.
7. **Cross-subject scholar reuse** — Beruni, Khorazmi, Ibn Sino appear across Geografiya + Tarbiya + Tasviriy Sanat. Should they share NPC representations or be subject-specific?
8. **Map Detective mini-game design** — needs UX prototyping; new mechanic, no existing reference.
9. **Below-L2 fallback for map content** — Reading L2 gate may exclude many G5 students; design simpler map exercises for L1 fallback.
10. **Bob III Maps content depth** — only 2 textbook sections but central to entire course. May need to expand into 3+ NETS sessions.
11. **Field observation long-arc tracker** — weather logging across multiple sessions as a side quest. Engineering review for persistence.
12. **Scholar pairing rule scaling** — ~30 pairings needed across all sessions. Who curates? Cultural reviewer or content lead?

---

## §19. Production Handoff

### Contract for content team

Build Geografiya G5 content matching the **§17 walkthrough shape exactly**. For each of ~28 sessions:

1. **Source from textbook** — every task traces to a Bob/section/page range
2. **Apply §4 psychology parameters** — 35–45 min, calm pacing, no failure states, warm tone, CPA mandatory
3. **Use §11 cultural anchors** — rotate Uzbek places, ALWAYS pair with Central Asian scholars
4. **Tag every task** per §15 schema (pisa_science_level, ml_level if map content, transition_skill, earth_system, textbook_ref)
5. **Pass Stranger Test** on every Story segment + RLC scenario
6. **Apply scholar pairing rule** wherever a world geographer is mentioned
7. **Author Boss question pools** — Easy/Medium/Hard per session, with worked solutions + hints + Common Errors
8. **Curate Did You Know pool** — ~50–60 facts
9. **Validate against §18 open questions** before production locks
10. **Notebook Capture** in 1 of every 4 sessions only — keep limited; this isn't Maker-First

### Quality gates
- **Pedagogy review** by 1 pedagogy lead + 1 G5 Uzbek Geografiya teacher
- **Language review** by Uzbek native speaker (Lexile + cultural authenticity)
- **Cultural validation** by Uzbek historian (scholar pairing accuracy)
- **Map literacy validation** by Uzbek geographer (atlas + coordinate accuracy)
- **Pilot in 2 classrooms** (1 urban Tashkent, 1 rural Fergana valley) before full rollout

### Timeline
- Research phase complete (this doc): done
- Content authoring (28 sessions): ~10–12 weeks
- Map asset production (interactive maps, diagrams): ~6 weeks parallel
- Pilot + validation: ~4 weeks
- Full rollout: ~ pilot + 4 weeks

---

## §20. Versioning and Review

- **Version 1.0** — 2026-04-08, Geografiya G5 first framework, PISA-rigorous shape
- **Reviewers needed:**
  - Product/pedagogy lead
  - 1+ Uzbek G5 Geografiya teacher
  - Uzbek historian (scholar pairing accuracy)
  - Uzbek geographer (atlas + coordinate accuracy)
  - Content lead
- **Next revision** after first 5 sessions stress-tested in pilot
- **Sibling frameworks to create after this:**
  - Geografiya G5 Russian edition (sibling)
  - Geografiya G6, G7 (next grades — economic/human geography emerges)
  - Apply scholar pairing rule retroactively to other PISA-rigorous frameworks (Science G5 should also pair Central Asian scientists with world figures if not already)

---

**End of NETS Geografiya G5 Framework v1.0.**

*Companion docs:* `NETS-Homework-Engine-UNIFIED.md` · `NETS-Homework-Engine-Blueprint.docx` · `NETS-UI-UX-Design-Spec.docx` · `Researches/qwen-grade5-psychology-findings.md` · `Extracted Texts/_geografiya_extracted.txt` · `Book & Resourses/5-sinf_geografiya_2020_(elekton_darslikbot).pdf`
