# NETS Homework Framework — Grade 5 (Uzbek) — History (Tarix)

**Version:** 1.0
**Date:** 2026-04-10
**Status:** Draft specification — first iteration for Grade 5 uz History homework.

**Pipeline position:**

```
Universal Framework (NETS-Homework-Engine-UNIFIED.md v2.0, 2026-04-07)
        │
        ▼
Psychology Filter (qwen-grade5-psychology-findings.md)
        │
        ▼
THIS DOCUMENT  ←  Grade 5 uz History adapted spec
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
- `5-sinf_Tarixdan_hikoyalar_yangi_darslik..pdf` — Grade 5 History textbook (U. Jo'rayev, Q. Usmonov, A. Nurqulov, G. Jo'rayeva, 2020)
- `DEMO-Tarix-5sinf-Documentation.md` - History Demo documentation

This is a **delta layer** — overrides, parameter tunings, and History-specific selections on top of the universal blueprint. Anything not mentioned here inherits from UNIFIED unchanged.

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

## 2. Subject identity — what is "Grade 5 Tarix"?

**Tarix** = History. Grade 5 History in Uzbekistan focuses on **"Tarixdan hikoyalar" (Stories from History)**, which is an introductory course covering general historical concepts, significant events, and figures within a narrative framework. It aims to build foundational historical literacy before more specialized historical periods are introduced in later grades.

**Subject scope (broad introductory):**
- Understanding what history is and why it's studied
- Introduction to historical sources (material, written)
- Concepts of time and chronology (calendars, eras, centuries)
- Role of archaeology and maps in historical study
- Key historical events and figures relevant to Uzbekistan and broader world history

**Pedagogical posture:** History at this age is about developing a sense of time, understanding causality, appreciating cultural heritage, and engaging with historical narratives. Lean heavily on:
- Story-driven learning (narrative engagement)
- Concrete examples of historical artifacts and events
- Visual representations (maps, timelines, images of artifacts)
- Understanding the "why" and "how" of historical events
- Fostering an appreciation for Uzbekistan's rich history and its place in global context

### Chapter map (textbook source: 5-sinf Tarixdan hikoyalar, 2020)

| Bob | Title (Uzbek) | English | Pages (from doc) | Sessions | Domain |
|---|---|---|---|---|---|
| I | TARIX – O‘TMISH GUVOHI VA BUGUNGI KUN UCHUN IBRAT MAKTABI | HISTORY – WITNESS OF THE PAST AND A SCHOOL OF LESSONS FOR TODAY | 5-21 | 7 | History/Chronology |
| | 1-§. TARIX FANI NIMANI O‘RGANADI? | What does history study? | 6-8 | 1 | History/Sources |
| | 2-§. AMALIY DARS | Practical Lesson | 8-9 | 1 | Local History |
| | 3-§. KALENDARLAR TARIXIDAN | From the History of Calendars | 9-11 | 1 | Chronology |
| | 4-§. XRONOLOGIYA HAQIDA | About Chronology | 12-13 | 1 | Chronology |
| | 5-§. TARIXDA YIL HISOBI | Time Reckoning in History | 14-17 | 1 | Chronology |
| | 6-§. TARIXNI O‘RGANISHDA ARXEOLOGIYANING O‘RNI | The Role of Archeology in Studying History | 18-19 | 1 | Archeology |
| | 7-§. DUNYO XARITASI TARIXI | The History of World Maps | 20-21 | 1 | Cartography |
| II | ENG QADIMGI DAVRLARDA DUNYO XALQLARI | PEOPLES OF THE WORLD IN ANCIENT TIMES | 24-27 | 1 | Ancient History |
| | 8-§. ENG QADIMGI ODAMLAR VA ULARNING MANZILGOHLARI | Ancient Humans and Their Settlements | 25-27 | 1 | Anthropology |
| III | KISHILIK MADANIYATINING SHAKLLANISHI | FORMATION OF HUMAN CULTURE | 27-42 | 5 | Cultural History |
| | 9-§. SAN’ATNING PAYDO BO‘LISHI | The Emergence of Art | 28-30 | 1 | Art History |
| | 10-§. YOZUV – INSONIYATNING BUYUK KASHFIYOTI | Writing – A Great Invention of Humankind | 30-33 | 1 | History of Writing |
| | 11-§. «AVESTO» – AJDODLARIMIZ YARATGAN ILK YOZMA TARIXIY MANBA | "Avesto" – The First Written Historical Source Created by Our Ancestors | 33-35 | 1 | Ancient Sources |
| | 12-§. MUZEYLAR | Museums | 36-39 | 1 | Museology |
| | 13-§. AFSONA VA RIVOYATLAR | Legends and Narratives | 39-42 | 1 | Folklore/Oral History |
| IV | QADIMGI SHAHARLAR VA DAVLATLAR | ANCIENT CITIES AND STATES | 42-51 | 3 | Urban/Political History |
| | 14-§. QADIMGI SHAHARLARNING PAYDO BO‘LISHI | The Emergence of Ancient Cities | 43-46 | 1 | Urban History |
| | 15-§. DUNYONING QADIMGI DAVLATLARI | Ancient States of the World | 46-49 | 1 | Political History |
| | 16-§. QADIMGI DUNYONING YETTI MO‘JIZASI | The Seven Wonders of the Ancient World | 49-51 | 1 | Cultural History |
| V | SAVDO VA ALOQA | TRADE AND COMMUNICATION | 52-70 | 6 | Economic/Social History |
| | 17-§. TANGALAR – TARIX GUVOHI | Coins – Witness of History | 53-55 | 1 | Numismatics |
| | 18-§. SAVDO YO‘LLARI | Trade Routes | 55-61 | 2 | Economic History |
| | (incl. 19-§. BUYUK GEOGRAFIK KASHFIYOTLAR) | (incl. Great Geographical Discoveries) | 58-61 | 1 | Exploration |
| | 20-§. ISHLAB CHIQARISH TEXNIKASINING PAYDO BO‘LISHI | The Emergence of Manufacturing Technology | 61-64 | 1 | History of Technology |
| | 21-§. TRANSPORT VOSITALARINING IXTIRO ETILISHI | The Invention of Transport Means | 65-67 | 1 | History of Transport |
| | 22-§. ALOQA VOSITALARINING IXTIRO ETILISHI | The Invention of Communication Means | 68-70 | 1 | History of Communication |
| VI | JAHON ILM-FANINING JAVOHIRLARI | GEMS OF WORLD SCIENCE | 70-81 | 4 | History of Science/Art |
| | 23-§. YURTIMIZDA ILM-FAN TARAQQIYOTI | The Development of Science in Our Country | 71-73 | 1 | National Science History |
| | 24-§. MIRZO ULUG‘BEK VA UNING AKADEMIYASI | Mirzo Ulugh Beg and His Academy | 74-76 | 1 | History of Science |
| | 25-§. ADABIYOT VA SAN’AT RAVNAQI | The Development of Literature and Art | 76-79 | 1 | History of Art/Literature |
| | 26-§. YEVROPADA ILM-FAN KASHFIYOTLARI | Scientific Discoveries in Europe | 79-81 | 1 | European Science History |

**Total:** 6 chapters · 26 sections · ~26 homework sessions to produce (for the extracted chapters).
*(Note: Full chapter map will be expanded upon further extraction of textbook content.)*

### Standard code pattern

`UZ-HIST-5-{TOPIC}-{SEQ}` — e.g., `UZ-HIST-5-SOURCES-01`, `UZ-HIST-5-CHRONO-03`. Alias dotted: `HIST.5.{bob}.{section}.{seq}`.

---

## 3. PISA History mapping — Grade 5 target

Per UNIFIED §3 + §7.3, Grade 5 History targets **L1 → L2 transition** as the dominant scaffold, with L2 → L3 stretch goals for top quartile. History is not a separate PISA domain but relies heavily on Reading and Social Sciences competencies.

| PISA Level | What student can do (History context) | G5 expected coverage | Bloom's pairing |
|---|---|---|---|
| L1 | Recall simple historical facts, identify key figures/dates | 30% of tasks | Remember |
| **L2** | **Explain familiar historical events/concepts, identify simple cause-effect** | **40% of tasks (target)** | **Understand, Apply** |
| L3 | Interpret basic historical sources, evaluate simple evidence | 25% of tasks (stretch) | Analyze |
| L4 | Multi-source synthesis (comparing perspectives) | 5% (top decile only) | Evaluate |
| L5–L6 | Mythical Boss only (<5% random) | n/a | Create |

**Mandatory `transition_skill` tags for G5 History** — every task must carry one of:

- `L1→L2: identify historical facts from narrative/text`
- `L1→L2: classify historical sources (material vs. written)`
- `L2→L3: interpret simple timelines or maps`
- `L2→L3: identify cause-and-effect in historical events`
- `L3→L4: compare and contrast different historical accounts/sources`

DRAFT tasks without one of these tags are rejected by content review.

---

## 4. Psychology filter — applied parameters

The universal blueprint exposes parameters. Grade 5 History sets them as follows.

### 4.1 Session timing (overrides Universal §4.1)

| Parameter | Universal | Grade 5 History |
|---|---|---|
| **Standard session total** | 30–45 min | **30–40 min** (includes 0-A + 0-B + 7 phases) |
| **Single phase max** | varies | **4–8 min** (hard ceiling) |
| **Inter-phase break** | varies | **5–15 sec** loading screen with Did You Know |
| **Daily homework cap** | not specified | **1–2 sessions / 30–60 min total** |
| **Recommended deployment window** | not specified | **17:00–19:00** (Uzbek after-dinner norm) |

### 4.2 Difficulty calibration (overrides Universal §9)

| Parameter | Universal | Grade 5 History |
|---|---|---|
| **Flow state success rate** | 70–80% | **70–80%** (consistent with universal) |
| **Adapt frequency** | every 3–5 questions | **every 3–4 questions** |
| **Difficulty visibility** | not specified | **HIDDEN** — never label questions internally to UI |
| **Pass threshold** | not specified | **60% minimum** (mastery learning floor for this age) |
| **Tier-down trigger** | <60% | **<65%** (catch slipping students 5 pts earlier) |
| **Productive struggle ceiling** | not specified | **30 seconds** before scaffolding |
| **Wrong answer language** | "Try again" | **"Hali emas" / "Not yet"** (Yeager 2019, +40% persistence) |
| **New technical terms** | not capped | **max 1–3 per session** (vocab ceiling) |
| **New concepts per instruction** | not capped | **max 3** (Cowan WM) |

### 4.3 Banned techniques for G5 History (filter list)

These are filtered OUT from the universal mechanic/feature roster (same as Science unless specified):

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
17. ❌ Adaptive Quiz mechanic — IRT feels like endless test
18. ❌ Peer Teaching mechanic — Uzbek classroom culture mismatch

### 4.4 Mandatory additions for G5 History

1. ✅ **Timeline integration:** Visual timelines are critical for historical understanding.
2. ✅ **Map literacy:** Every session should involve an interactive map component where relevant.
3. ✅ **CPA progression** — Concrete → Pictorial → Abstract for every concept.
4. ✅ **Dual coding** — Story Mode never text-only, image+text always.
5. ✅ **Worked example before independent practice**.
6. ✅ **Spaced retrieval** — Memory Sprint pulls Day 1/3/7/14, not just current chapter.
7. ✅ **Effort + strategy feedback** — never ability framing.
8. ✅ **Cultural anchors** — Ulugh Beg, Amir Temur, Ibn Sina, Al-Biruni, Al-Khwarizmi, Samarkand, Bukhara, Khiva. Emphasize Uzbek historical figures and locations.
9. ✅ **Mobile-first portrait, low-bandwidth** — shared family smartphone is the access point.
10. ✅ **Variable-ratio reward windows** — opportunity earned via competence.
11. ✅ **Hidden difficulty tiering** — adapts silently.
12. ✅ **30-second productive struggle window** before scaffolding.

---

## 5. Pre-homework — Sessions 0-A and 0-B (UNIFIED §4.4 + §4.5)

Both run before the 7-phase engine. Timer does not start until the student taps **"Boshlash" / "Start my Homework"**. No XP, no scoring, no penalties.

### 5.1 Session 0-A — Theme Preview (Swipe Deck)

**Refers to:** Universal §4.4. The 8 panels are mandatory; this section tunes them for Grade 5 History.

**Duration:** 2–3 min, student-paced
**Format:** Vertical swipe deck (TikTok/Tinder-style cards)
**Tier:** AI Tier 2 generates personalized framing per student PISA level + interests

| Parameter | Universal | Grade 5 History |
|---|---|---|
| Panel count | 8 mandatory | 8 — unchanged |
| Reading level | not specified | **Lexile 830–1010L**, average sentence ≤14 words, active voice |
| Visual-first ratio | "preferred" | **Mandatory** — every panel leads with photo/diagram/short clip; text is secondary |
| Language | not specified | **Uzbek only** for student-facing text; Russian/English permitted only in Additional Materials |
| POV | first-person | **Second-person Uzbek** — *"Sen bilasanmi…?"* / *"Sen ko'rganmisan…?"* |
| Personal Hook (panel 5) | not specified | Use 10–11 yr old life experiences only: family history, local landmarks, old photos, stories from elders. **Avoid** abstract or pre-teen experiences. |
| Industry Application (panel 7) | not specified | Use jobs G5 students recognize: `tarixchi`, `arxeolog`, `muzey xodimi`, `arxivchi`, `o'qituvchi`, `gid`. **Avoid** "data scientist," "biotech engineer." |
| Real-Life Research (panel 4) | not specified | Lead with a **named historical figure** when possible. **Preference order:** Central Asian first (Amir Temur, Ulugh Beg, Al-Biruni, Ibn Sina, Al-Khwarizmi), then global (Herodotus, Cleopatra, Columbus). **At least 1 in every 5 sessions must feature a Central Asian figure.** |
| Additional Materials (panel 8) | "any language" | Video > article. YouTube short / 360° photo of historical site > written article. Allow English/Russian/Uzbek mix. |
| Animation language | per UI/UX spec | Whoosh + letter-assembly transition between panels — 400ms whoosh + 600ms assembly. Do NOT slow down; fast = engagement at this age. |
| Skip behavior | swipe / dots | Both. Pagination dots double as "I'm done" jump. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate. |
| Did You Know | universal §6.5 | Inject **one** Did You Know themed to upcoming homework topic between panels 4 and 5. |

**Mandatory 8 components** (in order):

1. **Summary of Book Content** — 2-3 sentence textbook chapter summary
2. **Better Explanation** — same concept rephrased with metaphor + concrete analogy
3. **Examples** — 2-3 short examples (Concrete → Pictorial, never abstract-only)
4. **Real-Life Research** — historical/archeological discovery angle, Central Asian figure preferred
5. **Personal Hook** — direct "you" framing tied to student's daily life
6. **Why This Matters** — connects to identity, heritage, understanding present through past
7. **Industry Application** — Uzbek professionals using historical concepts
8. **Additional Materials** — links/embeds in any language

**Quality gate:** Run the **"10-year-old Stranger Test"** before publishing. Show the 8 panels to someone who's never seen the textbook. If they can describe the lesson and feel curious, it passes. If lost or bored, rewrite.

### 5.2 Session 0-B — Flash Cards

**Refers to:** Universal §4.5. The carousel is mandatory; this section tunes the deck for Grade 5 History.

**Duration:** 1–2 min initial pass, **returnable throughout homework via floating "Flash Cards" button** (NOT a hint, no penalty)
**Tier:** AI Tier 1 (pre-generated per chapter)

| Parameter | Universal | Grade 5 History |
|---|---|---|
| **Card count per session** | not capped | **5–7 cards max** (Cowan WM 4–5 + 1–2 buffer). Never more than 7. |
| Card categories | Formula/Concept/Rule/Definition | Prefer **Concept** and **Definition** — key terms, dates, figures. |
| One concept per card | mandatory | **Strictly enforced** — no compound cards. If a section has >7 key concepts, split into two sessions. |
| Visual on every card | not specified | **Mandatory** — front shows term + small icon/photo/drawing. Text-only forbidden. |
| Carousel layout | 3D circular | Center 1.0× sharp, neighbors 0.7× blurred. Tap to flip. |
| Flip animation | 500ms | **600ms** for G5 (extra processing time) |
| Tap-to-flip prompt | fades after 2s | Visible **3–4 sec** for first-time confidence |
| Language | not specified | **Uzbek only.** Front in Uzbek; back in plain Uzbek with one Russian/English equivalent in parentheses if commonly bilingual. |
| Cyclic loop | yes | **Yes** — loop "ding" sound when wrapping signals deck completion. |
| Returnable mid-homework | yes | **MANDATORY for History** — key dates/figures often need reference. NOT counted as hint. |
| "Boshlash" button styling | per UI/UX | **Visually rewarding** — full-width, primary color (`#60A5FA` History sapphire accent), gentle pulse animation. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate |

**Quality gate:** Every Flash Card must pass the **"5-second readability test"** — a G5 student reads front, flips, reads back, feels they "got it" in under 5 seconds per side.

---

## 6. The 7-Phase Engine — Grade 5 History

### 6.1 Phase 1 — Memory Sprint (≤2 min, 5–7 items)

| Parameter | Spec |
|---|---|
| Item count | 5–7 (low end — WM ceiling + warm-up buffer) |
| Format mix | Speed Match (term ↔ image/definition), Quick MC (dates/figures), Sentence Fill. Mix formats. **No pure typed recall** (slow + frustrating). |
| Source | **Spaced retrieval pull** — Day 1 / Day 3 / Day 7 / Day 14 schedule from prior chapters of Tarix, plus 1–2 items from current chapter glossary |
| Visual scaffolding | Every term must show with its visual representation |
| Streak bonus | Visible at 3+ correct (fire animation) |
| Wrong answer feedback | Immediate, soft, 5–10 sec positive framing window before next question |
| Remediation gate | <60% → route to remediation chapter before Story Mode (UNIFIED §5.1) |

### 6.2 Phase 2 — Story Mode (5–7 min)

**Story arc:** Universal Problem → Struggle → Discovery → Solution maps perfectly to **historical narratives** at this age. Focus on personalizing historical events.

**Structure:** 3 segments × ~90 sec each, interleaved with checkpoint games. Total ~5–7 min including checkpoints.

| Story arc beat | History version |
|---|---|---|
| **Problem** | A historical mystery or challenge. *"Qadimgi odamlar vaqtni qanday o'lchashgan? Soat va kalendar yo'q edi-ku?"* (How did ancient people measure time? There were no clocks or calendars, right?) |
| **Struggle** | Past attempts and solutions. *"Ular yulduzlarni, oyning fazalarini kuzatishgan. Lekin bu unchalik aniq emas edi."* (They observed stars, moon phases. But it wasn't very accurate.) |
| **Discovery** | The historical solution/concept lands. *"Misrliklar Nil daryosining toshqiniga qarab birinchi kalendarni yaratishdi."* (Egyptians created the first calendar based on the Nile's floods.) |
| **Solution** | Resolution + the principle. *"Endi ular qachon ekin ekishni, qachon hosil yig'ishni bilishardi. Bu ularning hayotini osonlashtirdi."* (Now they knew when to plant and harvest. It made their lives easier.) |

**Hard rules for G5 History Story Mode:**

- **CPA mandatory** — every concept touches Concrete → Pictorial → Abstract. 60–70% of exposures need a concrete or pictorial anchor.
- **Personalized narratives preferred** — use a child protagonist (e.g., Sardor from the demo) engaging with historical concepts.
- **Stranger Test** applies: a reader who's never seen the textbook should be able to answer the checkpoint from the narrative alone.
- **Checkpoint questions are comprehension, not recall.** Focus on "why did this happen?" or "what does this mean?"
- **Reading level cap:** Lexile 830–1010L. Average sentence ≤14 words. Avoid passive voice.
- **Max 2 retries per checkpoint** → simplified scaffold version.

**Domain-specific Story Mode tuning:**

| Domain | Phenomenon hook | Predict gate | Results gate | Explain gate |
|---|---|---|---|---|
| Historical Concepts | Narrative of discovery/challenge | "What do you think happened next?" MC | Show historical outcome/solution | Free-text or scaffolded sentence |
| Sources/Archeology | Image of artifact/dig site | "What kind of source is this?" MC | Reveal source type + info | Tile-Match source→info |
| Chronology/Maps | Animated timeline/map | "When did this happen?" MC | Reveal date/location | Why-Chain (2 levels) |

### 6.3 Phase 3 — Game Breaks (6–9 min, 3 games)

**Universal rule:** 3 games per session, ≥1 from Interactive Catalog + ≥2 from Default 16. Grade 5 History overrides the *selection priority*.

**Slot rules for G5 History:**

> **Slot 1:** Tile Match OR Memory Match Blitz OR Speed Match (visual/conceptual pairing)
> **Slot 2:** Why Chain (max 2 levels) OR Codebreaker OR Mystery Box (pattern + reasoning/historical context)
> **Slot 3:** **Timeline Builder in 1 of every 3 sessions**; otherwise Tic Tac Toe vs AI or Escape Room

**Selection algorithm:**
1. **Reinforcement game** at student's current Bloom's level on chapter's main concept
2. **Stretch game** one Bloom's level above
3. **Transition-skill game** scaffolding the L1→L2 (or L2→L3) skill chosen for the session

### 6.4 Phase 4 — Real-Life Challenge (3–5 min)

**First-person expert POV mandatory** (UNIFIED §5.4). Expert must be a Uzbek-context role:

- History/Sources → *"Sen tarixchisan / arxeologsan…"*
- Chronology → *"Sen arxivchisan / muzey xodimisan…"*
- Maps → *"Sen sayohatchisan / tadqiqotchisan…"*

**Hard rules:**
- First-person address only. *"Sen tarixchisan…"* Never *"Ali tarixchidir…"*
- **Real Uzbek context preferred** — family history, local landmarks, historical sites in Uzbekistan.
- **Tricky distractors** — at least one plausible-but-wrong answer requiring reasoning to eliminate.
- **Justify your answer** — student MUST explain reasoning; AI evaluates the *reasoning*, not just the choice (UNIFIED §6.7 dual-pathway).
- **Inquiry hook (History-specific):** every RLC ends with one of: *"Qanday tekshirasiz?"* / *"Qaysi manbaga murojaat qilardingiz?"* / *"Buni qanday isbotlaysiz?"* — scaffolds `Tadqiqotchilik ko'nikmalari`.
- **Eligibility gate:** PISA Reading L2+. Below L2 → fallback adaptive scaffolded version.

### 6.5 Phase 5 — Consolidation (3–5 min)

**Default technique for G5 History: Memory Palace.** History thrives on narrative and connecting abstract concepts to memorable locations.

**Per-chapter Phase 5 default:**

| Bob | Palace location | Why this place |
|---|---|---|
| I (History Overview) | Registon maydoni (Samarqand) | Center of historical knowledge, various significant buildings |

*(Note: Specific loci and concepts will be defined per section.)*

**Structure for Memory Palace:** 5 loci tied to 5 concepts; each locus has location image + concept text + visual mnemonic + 1 recall question. End with 3-question recall test cycling through loci.

**Why Memory Palace default for History:** Historical concepts, especially abstract ones like "chronology" or "sources," benefit greatly from being anchored to vivid mental images and spatial memory. Cultural landmarks in Uzbekistan provide rich context. Labeled diagrams can be used as an alternative when a specific visual process (e.g., calendar calculation) is central.

**Duration cap:** 3–5 min. Should feel calm and confident, not stressful. The "I'm ready" moment before Boss.

### 6.6 Phase 6 — Final Boss / Sub Boss (6–8 min)

**Tiered boss HP defaults (based on student PISA level):**

| Student PISA level | Boss tier | HP | Pattern |
|---|---|---|---|
| Below L1 (baseline ≈355) | Sub Boss Easy | **30 HP** | L1 questions only, scaffolded |
| L1–L2 (median G5) | Sub Boss Medium | **50 HP** | L1–L2 mix, win expected after 1 retry |
| L2–L3 (top quartile) | Sub Boss Hard | **80 HP** | L2–L3 mix, real challenge |
| L3+ (top decile) | Big Boss + occasional Mythical | **80–100 HP** | L3–L4 stretch |

**Boss content for History MUST include (5 questions, distribution Easy 40% / Medium 40% / Hard 20%):**
- 1 historical fact/concept definition question
- 1 source classification/interpretation question (artifact image/text snippet)
- 1 cause-effect question related to a historical event
- 1 chronology/timeline interpretation question
- Optional Hard: 1 evaluation question (e.g., "Which source is more reliable and why?")

**MC allowed at G5 Boss:** **Up to 30%** of questions may be multiple choice. Universal "no MC" rule is too strict for this age — pure open reasoning overwhelms WM at 10–11.

**Each Boss question MUST carry:**
- Step-by-step worked solution (visible after answer)
- 2–3 progressive **Hints** (revealed on request, not auto-pushed)
- **Common Errors** list — at least 1 known wrong answer with diagnostic explanation.

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

**Big Boss + Mythical Boss** apply per UNIFIED §5.6, capped at 70–80% target rate within the boss.

### 6.7 Phase 7 — Reflection (1–2 min)

**Duration cap:** 1–2 min only — metacognition is limited at this age (Roebers 2017).

**Tier 2 AI generates ONE prompt per session, selected from a bank by accuracy bucket:**

| Accuracy bucket | Prompt style | History G5 example |
|---|---|---|
| **≥80% (mastery)** | Strategy reflection — what worked | *"Bugun qaysi strategiya sizga muvaffaqiyat keltirdi? Tarixiy sanalarni tushunishda nima yordam berdi?"* |
| **60–79% (passing)** | Struggle + recovery — what was hard, how solved | *"Qaysi savol qiyin bo'ldi? Siz uni qanday hal qildingiz?"* |
| **<60% (Duolingo Mode)** | Support-seeking — what's still unclear | *"Bu mavzuni yaxshiroq tushunish uchun nima kerak? Qaysi qism chalkash bo'ldi?"* |

**Universal History prompts (rotate when not bucket-overridden):**
- *"Bugun qaysi tarixiy voqeani yangidan tushundingiz?"*
- *"Qadimgi odamlarning hayoti haqida nima sizni hayratda qoldirdi?"*
- *"Bu mavzu sizning oila tarixingiz bilan qanday bog'liq?"*

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
| Sentence structure | Active voice. |
| Vocabulary | Stay within ~12,000 word receptive range. Introduce new terms with concrete examples + visual + repeat 3+ times across the session. |
| Cultural anchors | Uzbek names (Gulnara, Bekzod, Aziza, Sardor, Malika, Jasur, Dilnoza, Otabek). Uzbek places (Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral, Charvak, Chimgan). Uzbek historical events and figures where relevant.
| Scientist references | Mix global (Herodotus, Columbus, Caesar) with Central Asian (Ulugh Beg, Al-Biruni, Ibn Sina, Al-Khwarizmi). **At least 1 Central Asian historical figure per 5 sessions.** |

### 7.2 Visuals

| Rule | Detail |
|---|---|
| Every concept gets a visual | CPA mandatory: real photo OR diagram OR pictorial representation. No text-only concept introductions. |
| Mobile-first sizing | All visuals legible on a 5" smartphone screen. No tiny labels, no fine detail. |
| Animation budget | Universal motion principles (≤800ms, transform+opacity only). |
| Dark mode default | Per UI/UX spec subject color: History = `#60A5FA` (sapphire) primary, `#3B82F6` (blue) accent. |

### 7.3 "Did You Know" facts (loading screen + phase transitions)

Per UI/UX spec, loading screens rotate Quote Cards / Fun Facts / Corny Lines. For G5 History the **Fun Facts pool** should be heavily History-themed AND age-appropriate:

- ✅ "Did you know? The Great Wall of China is not visible from space with the naked eye."
- ✅ "Did you know? Ancient Egyptians used to sleep on pillows made of stone."
- ✅ "Did you know? The shortest war in history lasted only 38 minutes."
- ✅ "Did you know? Amir Temur's empire stretched from India to Turkey."
- ❌ Anything involving death, violence, complex political facts, abstract economic theories.

**Quote Cards** for History loading screens should preferentially cite historians or historical figures, especially Central Asian ones — Ibn Sina on knowledge, Ulugh Beg on learning, Al-Biruni on discovery.

**Frequency:** 1 Did You Know per phase transition (loading screen, ≤8 sec each, AI Tier 2 generated/curated).

---

## 8. Game catalog selections — final list

### 8.1 Default 16 mechanics — usage at G5 History

| # | Mechanic | Use? | Notes |
|---|---|---|---|
| 1 | Memory Sprint | YES (P1 default) | Flexible format, mix MC + Speed Match |
| 2 | Spaced Flashcards | YES | Vocabulary/concept recall (also 0-B) |
| 3 | Tile Match | **YES (high priority)** | Visual-concept pairing, peak fit |
| 4 | Sentence Fill | YES | Reinforce key definitions/sentences from text |
| 5 | Memory Palace | **YES (P5 default)** | Cultural landmarks, historical concepts |
| 6 | Story Mode | YES (P2 default) | With narrative arc + Stranger Test |
| 7 | Adaptive Quiz | **NO** |
| 8 | Mystery Box | **YES (high priority)** | Case-opening, historical artifacts/sources |
| 9 | Movement Breaks | YES | Optional 30-sec stretch between phases |
| 10 | Why Chain | **YES (high priority, max 2 levels)** | Causal reasoning in historical events |
| 11 | Peer Teaching | **NO** |
| 12 | Real-Life Challenge | YES (P4 default) | First-person expert POV |
| 13 | Reflection Journal | YES (P7 default) | 1-sentence minimum |
| 14 | Final Boss | YES (P6 default) | Tiered HP, MC 30% allowed |
| 15 | Tic Tac Toe vs AI | YES | Familiar game, recall under stakes |
| 16 | Notebook Capture | **YES (moderate priority for History)** | Map sketching, timeline creation |

### 8.2 Interactive Game Catalog 12 — usage at G5 History

| Mechanic | Use? | Notes |
|---|---|---|
| Tic Tac Toe vs AI | YES | (also in Default 16) |
| Connect Four vs AI | YES | Visual + strategy |
| Codebreaker (Mastermind) | YES | Pattern deduction, historical codes/ciphers |
| Memory Match Blitz | YES | Photo pairs of historical figures/artifacts |
| Reaction Chain | LIMITED | Procedural sequences (e.g., steps in archeological dig) |
| Word Ladder Climb | NO | Not ideal for history, focus on concepts |
| Puzzle Lock (Sliding) | LIMITED | Ordering events on a timeline |
| Blackjack 21 | NO |
| Territory Conquest | YES | Map-based historical expansion/geography |
| Escape Room | YES | 4 locks, 5-min limit, history-themed mystery |
| Bridge Builder | NO |
| Minefield Navigator | NO |

### 8.3 History-specific mechanics

1. **Timeline Builder:** Student arranges historical events/figures on an interactive timeline.
2. **Map Explorer:** Interactive maps to locate historical sites, empires, or trade routes.

---

## 9. Notebook Capture — History task pool

Notebook Capture (Universal §6.8) is important for Grade 5 History, especially for map literacy and visual timelines. Use in **1 of every 4-5 sessions minimum.** (Less frequent than Science, as conceptual mapping is often done through Memory Palace/Timelines.)

| Task type | Example prompt |
|---|---|
| Map sketching | *"Daftaringga O'zbekistonning sodda xaritasini chiz va qadimgi Buxoro shahrining joyini belgilaydi."* |
| Timeline creation | *"Daftaringga 5 ta eng muhim tarixiy voqeani va ularning sanalarini yozib, sodda bir vaqt chizig'i (timeline) chiz."* |
| Historical figure drawing | *"O'zingga eng yoqqan tarixiy qahramonning rasmini chiz va uning 3 ta eng muhim ishi haqida yoz."* |
| Source identification | *"Daftaringga o'z mahallangdagi eski binoni chiz. Bu qanday manba bo'lishi mumkinligini yoz (moddiy/yozma)?"* |

**AI vision evaluation rubric:** Lenient on artistic skill, **strict on conceptual accuracy and label placement**.

**Latency:** ≤10 sec Tier 3 vision processing, with human fallback if exceeded.

**Accessibility:**
- Visually impaired → audio task substitute
- Motor disability → teacher toggle OFF
- No notebook → in-app sketch (max 80% XP per UNIFIED §6.8)

---

## 10. Anti-cheat tuning for Grade 5

| Rule | Universal | Grade 5 History |
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
- **Places**: Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral Sea, Charvak reservoir, Chimgan mountains, ancient Silk Road cities.
- **Foods**: plov, non, somsa, choy, kovurma (where historically relevant)
- **Animals**: animals historically significant to the region (e.g., horses, camels for trade routes).
- **Plants**: cotton, mulberry, wheat (historically relevant crops).
- **Currency**: so'm (contemporary context), historical currencies.
- **Historical Figures**: Amir Temur, Ulugh Beg, Al-Biruni, Ibn Sina/Avicenna, Al-Khwarizmi, Beruni, Ptolemy, Eratosthenes, Julius Caesar (from textbook).

### 11.2 Avoid

- Direct comparisons to Western lifestyles (*"Like an American kid, you..."*)
- Pork or alcohol references
- Politically sensitive topics (Aral Sea OK as environmental/historical, not politicized)
- Anything implying the child's family is poor or struggling

---

## 12. Assessment, scoring & escalation

### 12.1 Pass threshold

- **60% minimum** to pass session (G5 override)
- Below 60% → **Duolingo Mode** triggers automatically

### 12.2 Score → Reward mapping

| Score | Rating (Uzbek) | Reward |
|---|---|---|
| 100% | *Mukammal!* | Confetti, max XP, title: *"Yangi tarixchi"* (New Historian) — effort-framed |
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
| Story Mode | T1 (scripted media + checkpoints) | Static historical narratives + scripted gates |
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

- Session mode (Standard 30–40 / Extended 40–50)
- Boss HP modifier 50–150%
- Difficulty floor (student PISA ±1)
- Game pool selection (Auto / Manual)
- RLC required/optional (default: required for History)
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
  "task_id": "UZ-HIST-5-SOURCES-01-T07",
  "textbook_ref": {
    "book": "Tarixdan hikoyalar 5-sinf (Jo'rayev et al., 2020)",
    "chapter": 1,
    "section": "1.1",
    "pages": [6, 7]
  },
  "standard_ref": {
    "primary": "UZ-HIST-5-SOURCES-01",
    "alias": "HIST.5.1.1.1"
  },
  "pisa_ref": {
    "domain": "Reading",
    "sub_domain": "Access and retrieve information",
    "level_target": 2,
    "transition_skill": "L1→L2: identify historical facts from narrative/text"
  },
  "blooms_level": "Understand",
  "game_mechanic": "sentence_fill",
  "phase": "game_break",
  "prompt_uz": "Tarix — bu ______ haqidagi fan.",
  "expected_uz": "o'tmish",
  "evaluation_tier": 1,
  "estimated_time_sec": 30
}
```

---

## 16. Content production checklist

For each of the ~7 sessions in Chapter 1, content team must produce:

- [ ] Theme Preview 8-panel deck (Tier 2 prompt + assets) — Lexile 830–1010L, second-person Uzbek
- [ ] Flash Card pool: 5–7 cards (Concept/Definition/Dates prefer; visual mandatory)
- [ ] 30–50 Memory Sprint items (mixed Tile Match/MC/Sentence Fill, spaced retrieval)
- [ ] 1 Story Mode arc (3 segments × 90 sec) with historical media + 2 checkpoint sets, Stranger Test passed
- [ ] 6–9 Game Break activities across 3+ mechanics per slot rules (incl. Timeline Builder/Map Explorer)
- [ ] 1 Real-Life Challenge case (first-person expert + Uzbek context + inquiry hook)
- [ ] 1 Memory Palace exercise (default Phase 5) OR Labeled Diagram (alternative)
- [ ] 1 Sub Boss Easy + 1 Sub Boss Medium + 1 Sub Boss Hard question pool — each with worked solution + hints + Common Errors
- [ ] 1 Big Boss pool (cross-session, 3 weakest standards)
- [ ] Reflection prompt bank (3 accuracy buckets + 3 universal)
- [ ] 3 Did You Know facts (theme-aware, age-appropriate)
- [ ] All items dual-coded (`UZ-HIST-5-...` + alias)
- [ ] All items carry `transition_skill` from §3 list
- [ ] Notebook Capture task (1 in every 4-5 sessions)

**Total estimated content per session (Chapter 1):** ~80–120 task units.

---

## 17. Sample chapter walkthrough — I Bob, 1-§ "Tarix fani nimani o'rganadi?"

This is the **reference implementation** based on the existing demo and textbook content. Every other chapter session should match this shape.

### 17.1 Session metadata

| Field | Value |
|---|---|
| Bob | I: TARIX – O‘TMISH GUVOHI VA BUGUNGI KUN UCHUN IBRAT MAKTABI |
| Section | 1-§: Tarix fani nimani o'rganadi? |
| Textbook pages | 6–8 |
| Standard ref | `UZ-HIST-5-SOURCES-01` / `HIST.5.1.1.1` etc. |
| PISA target | Reading L2, PISA Level 2-3 |
| Bloom's coverage | Remember, Understand, Apply, Analyze |
| Transition skill | `L1→L2: classify historical sources (material vs. written)` |
| Total session time | 30-40 min (incl. 0-A + 0-B) |
| Mode | Standard |

### 17.2 Pre-Homework

**Theme Preview (8 panels, ~3 min, student-paced):**

1. **Summary** — *"Tarix — bu o'tmish haqidagi fan. U insonlarning qanday yashaganini, qanday voqealar bo'lganini o'rganadi. Tarixiy manbalar (moddiy va yozma) o'tmishni bilishga yordam beradi."*
2. **Better Explanation** — *"Tasavvur qiling, siz detektivsiz! Tarixchi ham shunday, faqat o'tmishdagi sirlarni ochadi. U topilmalar va eski yozuvlar orqali o'tmishdagi odamlar nima qilganini aniqlaydi."*
3. **Examples** — Photo of ancient pottery (moddiy manba), a page from "Avesto" (yozma manba), an archeologist at a dig site.
4. **Real-Life Research** — *"Qadimgi yunon tarixchisi Gerodotni "tarixning otasi" deyishadi. U uzoq sayohat qilib, ko'rgan va eshitganlarini yozgan. Yoki buyuk bobomiz Al-Biruniy o'tmishni o'rganish uchun qanday manbalar kerakligini tushuntirgan."*
5. **Personal Hook** — *"Sizning oilaviy albomingizda eng eski surat qaysi? U kimni ko'rsatadi va qachon olingan?"*
6. **Why This Matters** — *"O'z tarixingni bilish o'zingni, oilangni va Vataningni tushunishga yordam beradi. O'tmishdan saboq olib, kelajakni qurish mumkin."*
7. **Industry Application** — *"Toshkentdagi Tarix muzeyida ishlaydiganlar, arxeologlar, arxivchilar — bularning hammasi tarixni o'rganish va saqlash bilan shug'ullanadi."*
8. **Additional Materials** — Short video on archeological discoveries in Uzbekistan; 360° virtual tour of Afrosiyob (Samarkand); Russian explainer on types of historical sources.

**Flash Cards (~2 min, 6 cards):**

| # | Front | Back |
|---|---|---|
| 1 | 📜 Tarix | O'tmish haqidagi fan |
| 2 | 🏺 Moddiy manba | Ashyoviy dalil (tanga, qurol, sopol) |
| 3 | ✍️ Yozma manba | Yozuv orqali saqlangan ma'lumot (kitob, hujjat) |
| 4 | ⛏️ Arxeolog | Moddiy manbalarni qidiruvchi olim |
| 5 | 🏛️ Arxiv | Eski hujjatlar saqlanadigan joy |
| 6 | 📖 Avesto | Eng qadimgi yozma manba (Markaziy Osiyo) |

→ **Boshlash** button → timer starts.

### 17.3 The 7-phase session (based on DEMO-Tarix-5sinf-Documentation.md)

**Phase 1 — Memory Sprint (2 min, 6 items):** Speed Match + MC drawn from Kirish/Introduction chapter (e.g., "Vatan" meaning, Islom Karimov quote).

**Phase 2 — Story Mode (6 min, 3 × 90 sec segments interleaved with games):**
- **Narrative:** "Yosh arxeolog — Registon siri" (or similar, featuring Sardor and his bobo/Barno opa) covering:
    - What is History?
    - Material Sources (museum visit)
    - Written Sources (library visit, Avesto)
- **Checkpoints:** Comprehension questions after each segment.

**Phase 3 — Game Break finale (6-9 min, 3 games):**
- Slot 1: Tile Match ("Manbalarni juftla")
- Slot 2: Sentence Fill ("Bo'shliqni to'ldiring")
- Slot 3: Why Chain ("Nima uchun?" zanjiri)

**Phase 4 — Real-Life Challenge (4 min):**
- **Scenario:** "Bobongizning sandiq siri" (from demo) or "Mahallangiz tarixchisi" (from demo homework design).
- Questions focusing on classifying sources and evaluating their reliability.

**Phase 5 — Consolidation (3 min):**
- **Memory Palace:** Registon maydoni (Samarkand), connecting 5 key concepts (Tarix, Moddiy manba, Yozma manba, Arxiv, Arxeolog) to 5 loci.

**Phase 6 — Sub Boss Medium (7 min, 50 HP, 5 questions):** (based on demo's Boss configuration)
- Questions similar to demo: defining history, examples of sources, comparing material/written sources, importance of written sources, hypothetical city without written sources. Each with worked solution + hints + Common Errors. Combo bonus 3-in-row → 2× next damage. Hint tax −5 HP. Max 3 attempts.

**Phase 7 — Reflection (2 min):** Tier 2 generates 1 prompt by accuracy bucket. Min 1 sentence. Effort-praise framing only.

**Did You Know facts at phase transitions:**
1. *"Did you know? The word 'History' comes from a Greek word meaning 'inquiry' or 'knowledge acquired by investigation'."*
2. *"Did you know? The oldest known piece of writing is over 5,000 years old, from ancient Mesopotamia."*
3. *"Did you know? Before paper, people wrote on clay tablets, papyrus, and animal skins!"*

### 17.4 Post-session

Per §12.2 score → reward mapping. Auto-flag teacher if 3 consecutive sub-60% sessions on this standard.

---

## 18. Open questions / things to validate before production

1. **Full chapter map for Grade 5 History** — need to extract all chapters from the textbook.
2. **PISA Reading L2 gate for RLC** — many G5 students will be below L2; design fallback explicitly.
3. **Did You Know fact pool** — needs Uzbek-language curation.
4. **Central Asian historical figure content accuracy** — verify Story Mode material.
5. **Adaptive scaffolded fallback for below-L2 students** — needs explicit specification.
6. **Scholar pairing rule** from Geografiya G5: "every world geographer paired with a Central Asian one" — how should this be applied to History for figures (e.g., Herodotus ↔ Al-Biruni)?
7. **Custom track pattern for History:** Define a specific "Historical Reasoning (HR)" track (HR-L1 → HR-L4) like other non-PISA-pure subjects.

---

## 19. Production handoff

This framework is the **input contract** for the content team / openclaw when producing per-section homework lessons.

**What every produced session must do:**
1. Match the **shape** of §17 (Theme Preview → Flash Cards → 7 Phases → Post-session)
2. Apply **all** parameters from §4 (timing, difficulty, formats)
3. Use **Uzbek language only** for student-facing text
4. Include **at least one Notebook Capture task** in every 4-5 sessions
5. Include **at least one Did You Know fact** per phase transition
6. Use **first-person Expert POV** for every Real-Life Challenge
7. Use **real historical / cultural anchors** wherever possible
8. Generate boss questions to hit the **70–80% expected success rate**
9. Tag every item with `standard_ref`, `pisa_level`, `transition_skill`, `blooms_level` per §15
10. Validate against §18 Open Questions before deploying

---

## 20. Versioning and review

- **v1.0 (2026-04-10)** — Initial draft based on textbook content and demo documentation.
- **Reviewers needed:** product/pedagogy lead, 1+ Uzbek elementary history teacher, content team lead.
- **Next revision trigger:** after 5+ sections of Chapter 1 Grade 5 History homework are produced and stress-tested with real students, and full chapter map extracted.
- **Sibling adaptations to be created later, same template:**
  - `grades/5/uz/biology/`, `grades/5/uz/math/`, `grades/5/uz/literature/`, `grades/5/uz/geography/`, `grades/5/uz/english/`, `grades/5/uz/russian/`, `grades/5/uz/native_language/`, `grades/5/uz/informatics/`
  - Russian-language siblings under `grades/5/ru/`

---

**End of framework.** Initial draft for Grade 5 uz History homework production.
