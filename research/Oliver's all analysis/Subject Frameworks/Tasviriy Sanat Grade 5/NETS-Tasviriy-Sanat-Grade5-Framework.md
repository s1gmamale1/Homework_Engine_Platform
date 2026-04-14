# NETS Tasviriy Sanat — Grade 5 Subject Framework

**Version:** 1.0 (Maker-First Mode)
**Date:** 2026-04-08
**Status:** Production-ready specification — single source of truth for Grade 5 Tasviriy Sanat homework
**Supersedes:** none (first Tasviriy Sanat framework)
**Inherits from:** `NETS-Homework-Engine-UNIFIED.md` v2.0 + `NETS-Homework-Engine-Blueprint.docx` v1.0
**Psychology base:** `Researches/qwen-grade5-psychology-findings.md`
**Textbook source:** Tasviriy san'at, 5-sinf (Kuziyev, Abdirasilov, Nurtoyev, Sulaymonov, "O'zbekiston" NMIU, 2020, 128pp, ISBN 978-9943-28-336-7)

> **Reading order:** §0 first (decisions log), then §2 (subject identity), then §6 (the Maker-First engine). Everything else is reference.
>
> **One-line summary:** Every Tasviriy Sanat session — even theory lessons about Leonardo or Nabiyev — ends with the student physically making something. The Make is the climax. There is no Final Boss; the Make replaces it. A digital fallback exists for students without supplies.

---

## §0. Resolution Log

Tasviriy Sanat is **the second NETS subject built around a non-PISA creative discipline** (after Tarbiya), and **the first subject where physical making is the engine's center of gravity**. Textbook analysis showed ~65% of lessons are hands-on creation (drawing, painting, sculpting, ornament design) and ~30% are theory/history (artist biographies, art genres, Uzbek and world masters). The user's directive: **Maker-First** — every session, even theory lessons, ends with the student physically making something inspired by today's content.

This log records the decisions made when Tasviriy Sanat's nature collided with UNIFIED immutables.

| # | Conflict | Resolution | Reasoning |
|---|---|---|---|
| 1 | UNIFIED §6 mandates Final Boss with HP/defeat. Art has no defeatable correct answer. | **REPLACE Final Boss with "The Make" (Phase 6)** — student physically draws/paints/sculpts something inspired by today's lesson, photographs it, uploads. Tier 3 vision gives warm rubric-based feedback. No HP, no defeat, always passes. | Combat metaphor is incoherent for art. The Make satisfies the climax requirement of UNIFIED §6 by becoming the session's effortful peak — the student spends 10–12 min in focused creative work. |
| 2 | UNIFIED §4 sets Standard session 30–45 min. | **Maker-First sessions run 25–35 min.** The Make alone is 10–12 min; need ~15 min for the rest of the engine. | Longer than Tarbiya's 15–25 min Chill Mode because making takes real time. Shorter than Science 35–45 because we drop drill phases. |
| 3 | UNIFIED §6.1 Memory Sprint = 5–8 recall items. | **REPLACE Memory Sprint with "Warm-up Sketch" (Phase 1)** — 3-min hand-loosening exercise (e.g., "draw 5 different eyes, 30 sec each"). No upload required. | The hand needs to warm up before the mind. Drill recall is the wrong opening for a making subject. Pencil warm-ups are standard art studio practice. |
| 4 | UNIFIED §6.3 Game Breaks = 3 games per session. | **REPLACE with "Skill Drill" (Phase 3)** — 1 light game + 1 micro-make. Total 4 min. | Three games is too much fragmentation when the student needs to build creative momentum toward the main Make. |
| 5 | UNIFIED §6.4 RLC has expert POV + tricky distractors. | **REPLACE with "Choice + Plan" (Phase 4)** — student picks WHAT to make today (3 options) and plans the composition (1 min reflection). | This is the bridge between theory and the Make. Student needs to commit to a creative direction before the timer starts. |
| 6 | UNIFIED §6.5 Consolidation = diagram recall before boss. | **REPLACE with "Master Painters Hall" (Phase 5)** — today's painter card unlocks in the persistent gallery. Calm 1-min beat before the Make. | The card collection IS the consolidation; the moment of quiet pride before the creative push. |
| 7 | UNIFIED §6.6 Final Boss → REPLACED with "The Make" (see #1). | The Make is the session climax. 10–12 min of focused physical creation, photo upload, Tier 3 vision feedback. | See #1. |
| 8 | UNIFIED §3 mandates PISA tagging on every task. Tasviriy Sanat has no clean PISA fit. | **Use PISA Creative Thinking as PRIMARY tag + PISA Reading L1→L2 as SECONDARY (for art history texts) + custom Visual Arts (VA) track L1→L4 as practice spine.** Standard codes use prefix `UZ-TSV-5-{TOPIC}-{SEQ}` and `TSV.5.{LESSON}.{SEQ}`. | Creative Thinking is the closest official PISA domain. Reading covers art history texts. The custom VA track captures making/observation skills not in PISA. |
| 9 | UNIFIED §6 assumes scoring based on correctness. Art has no correct answers. | **Engagement-only scoring for the Make** — completion of upload = success. Tier 3 vision provides *warm reflective feedback*, not grades. Optional self-assessment checklist (3 prompts: composition / use of value / personal expression). | Same root reasoning as Tarbiya: overjustification effect (Deci/Koestner/Ryan 1999). Grading creative work crowds out intrinsic motivation. |
| 10 | UNIFIED §11 gamification economy includes XP, streaks, leagues. | **Keep XP/streaks (engagement-tied) but NO leagues, NO public ranking. Replace ranking with two collection meta-games: Master Painters Hall (artist cards, ~24 cards/year) + Galereya (student's own uploaded artworks).** | Artists want to be seen, not ranked. The Galereya satisfies the "show my work" instinct without comparative damage. |
| 11 | UNIFIED bans purchasable cosmetics (immutable). | **Honored.** All cosmetics in Tasviriy Sanat are earned via Master Painters Hall completion (e.g., complete the "Renaissance Masters" set → unlock a Renaissance frame for your Galereya). | UNIFIED rule, no override. |
| 12 | UNIFIED §10 requires content pool ≥85 items per topic. | **Tasviriy Sanat target ≥40 items per lesson** (lower because each Make is one item replacing many drill items). | Science 80–120/session is built around drill. Tasviriy Sanat ~30–50/session because the Make is one rich unit. |
| 13 | What if a student has no physical supplies (no notebook, no pencil, no paint)? | **Digital fallback baked in from day one.** Tap "I have no supplies today" in Phase 6 → engine offers an in-app digital make (drag face features, choose colors from a palette, build a portrait or landscape). Tier 2 evaluates choices, gives warm feedback. Full XP awarded. Galereya entry tagged "digital make" so teachers can spot patterns. | Without this, sessions are blocked for students on shared phones with no art supplies (common in rural Uzbekistan). The fallback removes the supply risk while preserving the make-something climax. |
| 14 | UNIFIED §13 cost budget $3–5/student/year. Tier 3 vision per session is expensive. | **Capped at 1 Tier 3 vision call per session for The Make** + 1 fallback Tier 2 call if digital make. Pre-projected ~$0.50–0.70/student/year for vision specifically. Full annual cost ~$2.00–2.80, within budget. | Vision is the only expensive call. Capping at 1/session keeps it affordable. |
| 15 | UNIFIED §6.7 Reflection mandates 1 sentence minimum. | **Optional reflection.** Voice / text / draw / skip — same XP. | Same as Tarbiya. Mandatory reflection on creative work feels coercive. |
| 16 | Theory lessons (Lessons 1, 8–9, 11, 13, 27) have no inherent making requirement. | **Maker-First override: theory lessons still end with The Make, but the prompt is style-imitation or response art.** "Today you learned about Van Gogh's swirling brushwork. Now draw a 10-min sketch in his style, OR draw something Van Gogh would have liked." | This is the core Maker-First commitment: theory days don't break the rhythm. The Make is always there. |
| 17 | Religious/cultural framing | **Hold doctrinally-neutral cultural Islamic warmth** (matches textbook). The textbook celebrates Uzbek folk crafts (naqsh, ceramics, miniature) without doctrine. NETS preserves this. | Textbook is values-neutral; preserve accessibility. |
| 18 | Family-bridge: should students show family their work? | **Optional warm prompt at session end: "Buvingga ko'rsat" (Show your grandmother).** Never required. No XP attached. | Shared art is shared joy. But a student with a hard home life shouldn't be pressured. Trauma-informed default = optional. |
| 19 | UNIFIED bans visible difficulty labels. | **Honored — no difficulty labels.** The Make has a single suggested time (10 min) and prompt; no Easy/Medium/Hard tier. | UNIFIED immutable. |
| 20 | The Stranger Test (UNIFIED §6.2 quality gate on Story Mode). | **Honored, extended:** Story segments must pass Stranger Test. The Make prompts must also pass a "10-year-old can attempt this in 10 minutes with basic supplies" test. | The Make is the make-or-break feature. If a 10-year-old can't try it, the framework fails. |

**20 resolutions logged. The single most important decision: every session ends with The Make (Phase 6 replaces Final Boss), and the digital fallback ensures no student is ever blocked.**

---

## §1. Audience Profile

**Inherited from `qwen-grade5-psychology-findings.md` §1–2 + §7 (universal Grade 5 Uzbek base).** Tasviriy Sanat-specific deltas noted inline.

**Cognitive (universal G5):**
- Late concrete operational (Piaget); abstract reasoning emerging
- Working memory 4–5 chunks (Cowan 2001) → max 3 new technique concepts per session
- Sustained attention 20–30 min academic, **extends to 35–40 min for engaged creative work** (the Make is genuinely engaging, not effortful)
- Lexile 830–1010L for art history texts
- Spatial reasoning still developing — 2D before 3D, simple shapes before complex figures
- Fine motor coordination still maturing — pencil grip varies, watercolor control limited

**Social/emotional (universal G5):**
- Self-concept fragile under public evaluation (Harter 2012)
- **Art self-concept especially fragile** — "I can't draw" is a common self-limiting belief at this age, often life-long
- Failure tolerance low — never frame the Make as "good vs bad"
- Reward sensitivity high for collection/cosmetic rewards
- Peer comparison sensitivity peaking — no leaderboards, no public ranking of Makes

**Tasviriy Sanat-specific cognitive load:**
- Creative making is intrinsically motivating IF the prompt is age-appropriate and the framing is non-evaluative
- The "blank page" problem is real at this age — students freeze when given unlimited choice. The "3 options" pattern (Phase 4 Choice + Plan) eliminates blank-page paralysis
- 10–12 minute making sessions are at the upper edge of G5 sustained attention for fine motor work; longer = fatigue

**Uzbek context:**
- Mother is primary supervisor; mother-as-co-art-teacher is welcomed (especially for traditional crafts like naqsh, embroidery)
- Shared family smartphone — mobile-first photo upload (camera permission required)
- Art supplies vary wildly: urban families have full kits, rural families may have only pencil + notebook. **The digital fallback is essential.**
- Traditional Uzbek crafts (kashtachilik, naqsh, miniature painting, ceramics) are part of cultural identity — students recognize these from family/mahalla life

---

## §2. Subject Identity

**Tasviriy Sanat** = Visual Arts / Fine Arts. Mandatory in Uzbek schools. Grade 5 covers drawing fundamentals, color theory, composition, art history, and traditional Uzbek folk arts. Roughly 1–2 lessons per week across the academic year (~34 lessons).

**Pedagogical posture:** *Make, observe, wonder, share.* The textbook teaches by demonstrating technique step-by-step (4-phase scaffolds), then asking students to create. NETS preserves this rhythm: theory feeds making, making feeds reflection.

**Content domains** (from textbook analysis, organized into 5 thematic clusters):

1. **Drawing fundamentals** (Lessons 2–7) — pencil, line, value, geometric form, perspective, landscape, sculpture warm-up
2. **Color & painting** (Lessons 8–10, 17–23) — color theory, watercolor, still-life, contrast, harmony, mood
3. **Composition & ornament** (Lessons 12, 14–16, 21, 24–26) — sketching, decorative naqsh, themed compositions, wall newspapers, architectural drawing
4. **Genres & art history** (Lessons 1, 8–9, 11, 13, 27) — expressive means, color painters (world + Uzbek), landscape mood, animalistic genre, portrait genre
5. **Portraiture & character** (Lessons 28–34) — cartoon characters, clay relief portraits, literary characters, historical figures (Amir Temur, Bobur), industrial robot drawing

**Pedagogical posture by lesson type:**
- **Maker lessons (~22 lessons):** Step-by-step technique scaffold → student creates
- **Theory lessons (~7 lessons):** Art history/genre context → in Maker-First, still ends with style-imitation Make
- **Hybrid lessons (~5 lessons):** Wall newspaper, themed projects combining research + illustration

**Standard code prefix:** `UZ-TSV-5-{TOPIC}-{SEQ}` (primary) · `TSV.5.{LESSON}.{SEQ}` (alias)

**Textbook source of truth:** Tasviriy san'at 5-sinf, Kuziyev/Abdirasilov/Nurtoyev/Sulaymonov, "O'zbekiston" NMIU, 2020, 128pp. Every NETS task must trace to a lesson + page range.

**Lesson map → session map:**

| Quarter | Lessons | Sessions | LU type |
|---|---|---|---|
| I (Lessons 1–9) | 9 | 9 | 1 theory + 6 maker + 2 theory-with-make |
| II (Lessons 10–16) | 7 | 7 | 1 theory-with-make + 5 maker + 1 hybrid |
| III (Lessons 17–26) | 10 | 10 | All maker (still-life, ornament, composition) |
| IV (Lessons 27–34) | 8 | 8 | 1 theory-with-make + 7 maker (portrait) |
| **Total** | **34 lessons** | **34 sessions** | **~22 maker + ~7 theory-with-make + ~5 hybrid** |

In Maker-First, **all 34 sessions end with The Make** — the only difference is what *kind* of Make (technique-driven vs. style-imitation vs. composition-driven).

---

## §3. PISA Mapping + Visual Arts (VA) Custom Track

Tasviriy Sanat does not map cleanly to PISA Math/Science. We use a **track-aware triple-tagging strategy**:

### Primary tag: PISA Creative Thinking
The closest official PISA domain. Covers:
- **Generating ideas** — coming up with original visual responses
- **Evaluating ideas** — choosing between compositional options
- **Improving ideas** — refining a sketch into a finished piece
- **Originality** — personal expression in style

### Secondary tag: PISA Reading L1→L2
Used **only on theory lessons** that involve reading about artists, art history, or analyzing reproductions in text:
- Lesson 1 (expressive means)
- Lessons 8–9 (color painting characteristics)
- Lesson 11 (expressive landscape analysis)
- Lesson 13 (animalistic genre)
- Lesson 27 (portrait genre)

### Custom Visual Arts (VA) track — practice spine

Every task carries one VA level (the spine of the framework):

| Level | Code | Capability | Example task |
|---|---|---|---|
| **VA-L1** | Recognize | Identify a technique, artist, or art concept by name | "Bu rasmni kim chizgan? (Mona Liza → Leonardo)" |
| **VA-L2** | Apply | Use a learned technique in a guided make | "Geometrik shaklni qalamda chiz, soyalash bilan" |
| **VA-L3** | Compose | Make creative choices in composition, color, mood | "Manzara chiz — quyoshning botishi yoki tongni tanla" |
| **VA-L4** | Express | Make personal/expressive work that reflects mood, style, intent | "O'zingni xohlagan rangda avtoportret chiz — his-tuyg'ungni ko'rsat" |

### Distribution targets per session

| Bucket | % of session tasks | Purpose |
|---|---|---|
| VA-L1 (Recognize) | 25% | Theme Preview, Flash Cards, Memory Sprint warm-up, Phase 3 game |
| VA-L2 (Apply) | 35% | Technique demos, micro-makes |
| VA-L3 (Compose) | 30% | The Make (most sessions) |
| VA-L4 (Express) | 10% | The Make on style-imitation theory days; reflection sketches |

### Mandatory tagging schema (every task)

Every Tasviriy Sanat task carries:
- `va_level` — VA-L1 through VA-L4
- `pisa_creative_thinking` — true/false (primary)
- `pisa_reading_l1_l2` — true/false (only on theory content)
- `transition_skill` — narrative description of which VA capability the task scaffolds (e.g., "VA-L2→L3: take a pencil technique and use it to make a personal compositional choice")
- `make_type` — `none` / `micro` / `main` / `digital_fallback`
- `textbook_ref` — Lesson number + page range

---

## §4. Psychology Filter — Applied Parameters

Applies the universal Grade 5 psychology base to Tasviriy Sanat, with Maker-First tuning.

### Session timing
- **Standard session: 25–35 min** (Maker-First override; longer than Tarbiya 15–25, shorter than Science 35–45)
- **Extended session: 35–45 min** (in-class, teacher-led, group critique format)
- **The Make alone: 10–12 min** (extendable to 15 if student wants to keep going)
- **Single non-Make phase max: 4–5 min**
- **Inter-phase break: 5–10 sec** with Did You Know art facts
- **1 session per day max** (creative fatigue is real)
- **Deploy window: 17:00–19:00** (after-dinner family time, mother nearby for supplies)

### Adaptation calibration
- **No success rate target for The Make** — completion = success
- **Adapt every 2–3 non-Make tasks** based on engagement signals (time on prompt, choice of Make type, photo upload completion rate)
- **No difficulty labels, no tiering** for The Make
- **Recovery framing** — never "Wrong"; use "Boshqacha qarash" (Another perspective) or "Yana bir bor sinab ko'r" (Try once more)
- **Productive struggle ceiling for non-Make tasks: 30 sec** before scaffolding
- **The Make has no struggle ceiling** — student paces themselves; mid-make checkpoint at 5 min asks "Davom et yoki bir nafas ol?"

### Banned techniques (Tasviriy Sanat-specific)
1. **Public ranking of student artworks** — Harter 2012, fragile self-concept
2. **Comparative grading of Makes** — Deci et al. 1999, overjustification
3. **"Good drawing / bad drawing" framing** — Dweck 2006, fixed mindset
4. **Forced sharing of Makes** — psychological safety
5. **Failure states for The Make** — incoherent for art
6. **"You're talented" praise** — ability framing; use effort/process
7. **Boss combat metaphor** — incoherent
8. **Mandatory written reflection** — Roebers 2017
9. **Western-only artist canon** — Uzbek masters always paired with world masters
10. **Religious doctrinal framing** — held neutral
11. **Real-time multiplayer drawing competitions** — speed pressure breaks creative flow
12. **Adaptive Quiz mechanic** — IRT feels like endless testing
13. **Why Chain ≥3 levels** — universal G5 WM ceiling
14. **Cosmetics purchasable with money** — UNIFIED rule
15. **Timer countdown on The Make** — visible timer creates anxiety; show only if student opts in

### Mandatory inclusions
1. **Every session ends with The Make** — Maker-First core commitment
2. **Digital fallback always available** — never block a student for missing supplies
3. **3-option choice pattern** in Phase 4 — eliminates blank-page paralysis
4. **Effort/process praise only** — Dweck growth mindset
5. **Master Painters Hall + Galereya** — dual collection meta-game
6. **Cultural anchors in every session** — Uzbek artists, places, traditions, naqsh
7. **Warm Tier 3 vision feedback** on every Make upload — never grades, always reflection
8. **Optional family-bridge** — "Buvingga ko'rsat" never required
9. **Calm, slow pacing** in non-Make phases — no countdown timers in any phase by default
10. **Did You Know art facts** between phases — anchoring delight, never pressure

---

## §5. Pre-Homework Sessions 0-A & 0-B

### 0-A Theme Preview (Mavzu Tanishuvi) — 2–3 min

**Format:** 8-panel swipe deck (vertical), student-paced, no scoring, no XP, no timer. Same shape as Tarbiya/Science but tuned for Tasviriy Sanat.

**Tasviriy Sanat 8-panel structure** (example for Lesson 17 — Color Still-Life):

| Panel | Content | Lesson 17 example |
|---|---|---|
| 1. **Sarlavha** | Lesson title + warm hook image | "Rangtasvirda natyurmort chizish bosqichlari" + photo of a finished watercolor still-life |
| 2. **Yaxshi tushuntirish** | Concept defined with metaphor | "Natyurmort — bu jonsiz narsalardan jonli rasm yasash. Olma, ko'za, gul — sen ularni qaytadan tug'dirasan." |
| 3. **Misollar** | 2–3 visual examples (master + student) | Cézanne still-life, Ahmedov "Yoz ne'matlari," a real student watercolor |
| 4. **Hayotiy hikoya** | 3-sentence story about an artist | "Rahim Ahmedov o'z natyurmortlarida Uzbek mevalarini chizishni yaxshi ko'rardi. U aytar edi: 'Mening xonadonimda olma — bu mehmon kabi.'" |
| 5. **Senga taalluqli** | "Have you ever..." direct connection | "Sen onangning piyolaga choy quyganini kuzatganmisan? Bu ham natyurmort sahnasi." |
| 6. **Nega muhim** | Long-arc significance | "Natyurmort sening ko'zingni o'rgatadi — oddiy narsalarda go'zallikni ko'rishga." |
| 7. **Hayotda qo'llanilishi** | Modern Uzbek context | Photos of pottery shops in Gijduvan, market still-life shots, food photography |
| 8. **Bugun nima qilasan?** | **Replaces "Additional Materials"** — preview of what student will MAKE today | "Bugun sen 4 ta narsadan natyurmort chizasan: olma, piyola, non, va bir gul." |

- **Animation:** 400 ms whoosh + 600 ms assembly per panel
- **Pagination dots, swipe forward only,** can skip back
- **No XP, no scoring, no timer**
- **One Did You Know between panels 4–5** (art fact: "Cézanne natyurmortini 4 oy davomida chizar edi — olmalar bir necha marta chirib, almashtirilgan")
- **Stranger Test:** Could a Grade 5 Uzbek student understand and feel inspired without a teacher? If no, rewrite.

### 0-B Flash Cards (Tezkor Kartochkalar) — 1–2 min

**Format:** 5–7 card carousel, returnable mid-session as reference.

**Tasviriy Sanat Flash Card structure:** Each card has:
- **Front:** Concept name (Uzbek) + visual icon or thumbnail
- **Back:** 1-sentence definition + 1 mini-demo sketch showing the concept in action + 1 master example

**Example cards for Lesson 17 (Color Still-Life):**
1. Natyurmort — still-life
2. Kompozitsiya — composition (where things sit on the page)
3. Yorug'lik manbai — light source (where light comes from)
4. Soya — shadow
5. Issiq rang / Sovuq rang — warm/cool color
6. Akvarel — watercolor

Card flip: 600 ms. Tap-to-prompt visibility 3–4 sec. **Tasviriy Sanat-specific feature: each card's mini-demo sketch is the most important element** — students learn by seeing technique, not by reading definitions.

---

## §6. The 7-Phase Engine — Tasviriy Sanat Maker-First

**Total session: 25–35 min** (Standard) including 0-A + 0-B + 7 phases. The Make alone is 10–12 min.

### §6.1 Phase 1 — Warm-up Sketch (Qo'l Mashqi) · 3 min

**Replaces universal Memory Sprint.** The hand warms up before the mind.

- **3-min warm-up exercise** tied to today's lesson:
  - Portrait day: "Daftaringga 5 ta turli ko'z chiz. Har biri 30 soniya."
  - Still-life day: "5 ta turli shakl chiz: doira, kvadrat, uchburchak, oval, yulduz. Har birini 30 soniyada."
  - Landscape day: "5 ta turli daraxt chiz: tik, egilgan, shamol uchirgan, qishki, gulli."
  - Naqsh day: "5 ta turli ornament elementi chiz: doira, gul, barg, yulduz, spiral."
- **No upload required for warm-up** — this is just to loosen the hand
- **Soft recall** of last session's main concept (1 visual MC, 4 options)
- **No timer pressure** — countdown optional, hideable
- **XP awarded just for tapping through** — engagement = success
- **If student taps "no supplies"** → warm-up becomes a digital tap-and-trace exercise on screen
- **Tier 1 algorithmic** — pre-generated warm-up bank by lesson type

### §6.2 Phase 2 — Hikoya + Demo (Story + Technique Demo) · 5–6 min

**Replaces universal Story Mode.** Same shape (3 segments × 90 sec) but **interleaved with 30-sec technique demos.**

- **3 narrative segments**, each followed by a 30-sec embedded technique demo video
- Story arc: Problem → Discovery → Solution (universal NETS)
- Technique demos are **the textbook's step-by-step scaffolds turned into video**
- Each segment ends with an **invitation** (not requirement) to "try it real quick" in the student's notebook — micro-practice

**Subject-specific narrative approach:**
- **Drawing fundamentals lessons:** Stories about artists discovering technique (Leonardo's first sketch, Nabiyev's apprentice years)
- **Color/painting lessons:** Stories about color discoveries (Van Gogh's sunflowers, Ahmedov's Uzbek summer palette)
- **Composition/ornament lessons:** Stories about Uzbek folk masters (Khorazm woodcarvers, Bukhara naqsh designers)
- **Theory lessons (Lessons 1, 8–9, 11, 13, 27):** Stories about famous paintings being made — Leonardo + Mona Lisa, Nabiyev + Amir Temur portrait, etc.

**Hard rules:**
- Lexile 830–1010L, ≤14 word sentences, second-person ("Sen") POV
- Stranger Test on every segment
- No comprehension checkpoints with right/wrong answers — choices are reflective, not graded
- Tier 1 pre-generated narrative + Tier 1 pre-recorded demo videos

### §6.3 Phase 3 — Skill Drill (Mahorat Mashqi) · 4 min

**Replaces universal Game Breaks.** One light game + one micro-make.

**Game (2 min):** One mechanic from this rotating pool:
- **Tile Match:** 6 pairs of art concepts (master ↔ painting, technique ↔ result, ornament element ↔ name)
- **Memory Match:** 6 pairs of art elements
- **Mystery Box:** Reveal 3 art curiosities (famous painting details, hidden symbols)
- **Sentence Fill:** Complete a quote from a master ("Yorug'lik bo'lmagan joyda ____ ham bo'lmaydi" → soya)
- **Sequence ordering:** Put the 4 phases of a technique in order (sketch → tone → detail → color)

**Micro-make (2 min):** A small drawing exercise in the student's notebook, optional photo upload, no scoring. Examples:
- Portrait day: "Bitta ko'zni his-tuyg'u bilan chiz — hayron / xafa / xursand"
- Still-life day: "Bitta olmani chiz, soyasi bilan"
- Landscape day: "Bitta daraxtni chiz, ildizidan tepasiga"
- Ornament day: "Bitta naqsh elementini chiz, takrorlash bilan"

If no supplies → micro-make becomes a digital drag-and-drop exercise.

### §6.4 Phase 4 — Tanlov + Reja (Choice + Plan) · 3 min

**Replaces universal Real-Life Challenge.** No tricky distractors. Student picks WHAT to make today.

**Format:**
1. **3 prompt options** with starter thumbnails. Examples for Lesson 17 (Still-Life):
   - **A) Klassik:** "4 ta narsa — olma, piyola, non, gul"
   - **B) Kayfiyat:** "Sening eng yoqtirgan 3 ta narsang"
   - **C) Tasavvur:** "Sehrli xonaga sahna yarat — 5 ta narsa"
2. **Student picks one** (or taps "Boshqa fikr bor" and types their own — Tier 2 affirms warmly)
3. **1-min plan prompt:** "Qog'ozni qaysi shaklda joylashtirasan? Yorug'lik qayerdan keladi? Asosiy narsa qayerda turadi?" — pure planning, no drawing
4. **Plan is private** — never graded, just a thinking moment

**Why this works:**
- The 3-option pattern eliminates blank-page paralysis (psychology-backed; reduces choice overload at G5)
- The plan moment forces a 60-second pause that improves the Make (pre-planning beats blank-paper diving)
- Free-text option respects student autonomy (SDT)

### §6.5 Phase 5 — Master Painters Hall (Ustozlar Saroyi) · 1–2 min

**Replaces universal Consolidation.** Quiet pride moment before the Make.

- **Today's painter card unlocks** (1 unique card per session, or 1 paired card on theory days — see card design below)
- Brief animation (4–5 sec) — card slides in with master's portrait + name + 1 quote
- **Card joins persistent Master Painters Hall** — student sees collection grow over weeks
- **Tap to read card details:** master's bio (3 sentences), 1 famous work thumbnail, 1 quote, link to today's story segment
- **Hall has 4 zones:** Renaissance Masters · Modern Masters · Uzbek Masters · Folk Tradition Masters
- **Card pairing on theory days:** Lesson 27 unlocks Leonardo da Vinci (Renaissance) + Malik Nabiyev (Uzbek) as a pair — world master + Uzbek master always together
- **34 cards total** for Grade 5 (one per session)
- **Calm, slow** — this is the breath before the Make
- **Tier 1** algorithmic, pre-generated card art

### §6.6 Phase 6 — ⭐ KARTINA (The Make) · 10–12 min

**REPLACES Final Boss.** This is the session climax — the entire engine builds to this moment.

**Format:**

1. **Setup screen** (15 sec) — Today's prompt locked in from Phase 4. Materials reminder: "Sen tanladingmi: qalam, daftar, akvarel?" Tap "Tayyorman" (Ready).
2. **Optional reference panel** — Master examples from today's painters stay visible in a sidebar (collapsible). Aziza can peek at Leonardo or Nabiyev for inspiration.
3. **Optional calm music** — instrumental, no lyrics. Off by default.
4. **Optional timer** — 10 min suggested, hideable. Student can extend to 15 if engaged.
5. **Mid-make checkpoint at 5 min** — gentle prompt: "Qanday ketyapti? Davom et yoki bir nafas ol?" — never a forced break.
6. **Photo upload** when done — student takes a photo with phone camera. Auto-crop assist.
7. **Tier 3 vision evaluation** (≤10 sec):
   - Recognizes the make matches today's prompt category (yes/no — never used as fail signal, just for analytics)
   - Identifies what's working: composition / use of value / color choices / personal expression
   - Notes 1 thing to try next time (gentle, never "wrong")
   - Generates a warm 2-sentence response in Uzbek
8. **Always passes.** Photo joins persistent **Galereya**. XP awarded.
9. **Optional self-assessment checklist** (3 prompts, optional, 30 sec):
   - "Mening kompozitsiyam balanced ko'rinadimi?"
   - "Yorug'lik va soya farqi sezilarli?"
   - "Bu rasm menga yoqdimi?"

**Digital fallback** (if "no supplies" tapped):
- In-app digital make tool — drag features, choose colors from palette, build composition
- Tier 2 evaluates choices, gives warm feedback
- Full XP awarded
- Galereya entry tagged "digital make" (visible to teacher in dashboard analytics, never to student)
- Teacher dashboard alert if same student uses digital fallback ≥3 sessions in a row → soft outreach for supplies

**No HP, no hints, no retries, no defeat, no fail screen, no difficulty tier.** The Make is the climax through *effort*, not through *combat*.

**Tier 3 cost:** 1 vision call per Make. Capped to 1/session. Pre-projected ~$0.02/call × ~34 sessions/year = ~$0.68/student/year for vision specifically.

### §6.7 Phase 7 — O'ylab Ko'rish (Reflection) · 1–2 min · OPTIONAL

**Optional reflection. Skip is a valid path.** XP identical regardless.

**Three formats, student choice:**
1. **Voice** — record up to 30 sec
2. **Text** — write up to 2 sentences
3. **Draw** — quick sketch in app
4. **Skip** — tap "Bugun yetarli"

**Prompt rotation:**
- "Bugungi rasming senga qanday yoqdi?"
- "Qaysi qism eng qiyin bo'ldi?"
- "Agar yana 5 daqiqa bo'lganida, nimani o'zgartirgan bo'larding?"
- "Ustozlar Saroyidan qaysi rassom bugun seni hayron qoldirdi?"

**Privacy:** student-only by default. Student can tap "Ulashish" (Share) to send to teacher's wall (moderated, opt-in).

**Optional family-bridge prompt at end:** "Buvingga ko'rsat?" (Show your grandmother?) — pure suggestion, no XP, no requirement.

---

## §7. Content Rules

### Narrative voice
- **Second-person ("Sen")** — warm, partner-tone, never preachy
- **≤14 word sentences**, active voice, Lexile 830–1010L
- **Receptive vocab cap ~12k** — define new art terms inline with visual + repetition
- **Uzbek cultural names, places, foods, professions** as default frame
- **Master pairing rule:** every world master mentioned must be paired with a Uzbek master (Leonardo + Nabiyev, Van Gogh + Akmal Nur, Rembrandt + Choriyev, etc.)

### Emotional tone
- **Warm, affirming, never evaluative** for The Make and reflection
- **"Sening fikring qiziq"** not "To'g'ri javob"
- **Effort/process praise only** — "Yaxshi mehnat qilding," not "Sen rassomsan"
- **Dweck growth-mindset language** — "Yana bir bor sinab ko'r" never "Notog'ri"

### Visuals
- **Every concept has a visual.** Dual coding mandatory.
- **Mobile-first, 5" screen legible.** Min font 14px, labels 16px+.
- **Demo videos: ≤30 sec, no music, slow hand-cam style** — student can mimic
- **Subject color: deep purple `#7C3AED` primary + warm cream `#FEF3C7` accent** (signals creativity + warmth + tradition; visually distinct from Science purple `#8B5CF6`, Tarbiya gold `#F59E0B`)
- **Dark mode** per universal UI/UX spec.

### Did You Know (loading/transitions)
- **Art history facts**, age-appropriate
- **One per phase transition**
- **Examples:**
  - "Leonardo da Vinchi 'Mona Liza'ni 4 yil chizgan va to'liq tugatmagan deb o'ylagan."
  - "Malik Nabiyev Amir Temurning rasmini chizish uchun tarixchi va olimlardan maslahat olgan."
  - "Van Gogh hayoti davomida faqat 1 ta rasm sotgan — bugun esa uning rasmlari million dollar turadi."
  - "O'zbek miniaturasi 600 yildan beri qog'ozda emas, asosan kitoblarda ishlangan."
- **Avoid:** anything scary, Western lifestyle comparisons, politics, family poverty implications, doctrinal religious framing

---

## §8. Game Catalog Selections — Tasviriy Sanat G5

**Default Pool (16 mechanics from UNIFIED §6):**

| # | Mechanic | Tasviriy Sanat | Notes |
|---|---|---|---|
| 1 | Memory Sprint | **NO** | Replaced with Warm-up Sketch (Phase 1) |
| 2 | Spaced Flashcards | YES | 0-B Flash Cards only |
| 3 | Tile Match | YES (high) | Master ↔ painting, technique ↔ result, ornament ↔ name |
| 4 | Sentence Fill | YES | Master quotes completion |
| 5 | Memory Palace | LIMITED | Lessons about Uzbek folk tradition centers (Bukhara, Khiva) |
| 6 | Story Mode | **YES (highest)** | With interleaved technique demos |
| 7 | Adaptive Quiz | **NO** | Endless-test feeling, hostile to creative flow |
| 8 | Mystery Box | YES (high) | Hidden painting details, art curiosities |
| 9 | Movement Breaks | YES | Optional between phases |
| 10 | Why Chain | LIMITED | Max 2 levels, technique reasoning ("Why use warm colors here?") |
| 11 | Peer Teaching | LIMITED (opt-in) | "Ulashish" — student can share Make to moderated class wall |
| 12 | Real-Life Challenge | **REPLACED** | Now "Tanlov + Reja" (Choice + Plan) |
| 13 | Reflection Journal | YES | Optional Phase 7 |
| 14 | Final Boss | **REPLACED** | Now "Kartina" (The Make) |
| 15 | Tic Tac Toe vs AI | YES | Recreational only, no art content |
| 16 | Notebook Capture | **YES (CORE — every session)** | The Make IS Notebook Capture, elevated to engine center |

**Interactive Catalog (12 mechanics):**

| Mechanic | Tasviriy Sanat | Use case |
|---|---|---|
| Connect Four vs AI | YES | Recreational |
| Codebreaker | YES | Decode artist quotes |
| Memory Match Blitz | YES (high) | Master/work pairs |
| Reaction Chain | NO | Speed-based, wrong tone |
| Word Ladder | LIMITED | Vocab chains for art terms |
| Puzzle Lock | NO | Wrong tone |
| Blackjack | NO | Gambling tone |
| Territory | NO | Competitive |
| Escape Room | LIMITED | Lesson 16/25 wall newspaper themed only |
| Bridge Builder | NO | Engineering focus, off-topic |
| Minefield | NO | Failure-state |
| **Tasviriy Sanat-specific: Style Mimic** | **YES (NEW)** | Mini-game where student matches a brushstroke style to an artist |

**Two Tasviriy Sanat-only mechanics introduced:**
1. **Kartina (The Make)** — the core engine moment, 10–12 min physical creation + photo upload (replaces Final Boss)
2. **Style Mimic (Uslub Taqlidi)** — light interactive game where student matches brushstroke samples to master painters (Van Gogh swirls, Rembrandt shadows, Nabiyev flatness, Choriyev portraits)

---

## §9. The Make + Galereya — Mechanic Spec

The **Kartina (The Make)** is Tasviriy Sanat's signature mechanic. The **Galereya (Gallery)** is its persistent collection meta-game.

### The Make — task pool (per lesson type)

| Lesson type | Make prompt template | Time | Tier 3 vision focus |
|---|---|---|---|
| **Drawing fundamentals** (L2–7) | Technique-specific (geometric shapes, landscape, sculpture, light/shadow) | 10 min | Composition, line quality, value range |
| **Color/painting** (L8–10, 17–23) | Watercolor still-life, landscape, color exploration | 12 min | Color choice, mood, brushwork |
| **Composition/ornament** (L12, 14–16, 21, 24–26) | Themed compositions, naqsh patterns | 10–12 min | Symmetry, repetition, balance |
| **Genre/art history** (L1, 8–9, 11, 13, 27) | **Style imitation Make** — "Draw something in [today's master]'s style" OR "Draw a scene [today's master] would have painted" | 10 min | Personal interpretation, evidence of style awareness |
| **Portrait** (L28–34) | Self-portrait, family member, literary character, historical figure | 12 min | Face proportion, character, expression |

### Tier 3 vision evaluation rubric

The vision call is **never grading**. It identifies what's working and offers one gentle suggestion. Sample warm responses:

> "Aziza, sening natyurmortingda olmaning shakli juda yaxshi chiqibdi. Keyingi safar yorug'lik qaysi tomondan kelishini ko'rsatib ko'r — bu rasmni yanada jonliroq qiladi."

> "Bekzod, sening manzarangda osmon va er o'rtasida chiroyli muvozanat bor. Keyingi safar bitta narsani — daraxt yoki tog' — markazga olib ko'r."

> "Malika, sening ornamenting takrorlanish ritmi juda chiroyli. Bu qadimgi Bukhara naqshlarini eslatadi."

**Cost:** ~$0.02 per vision call. ~34 calls/year = ~$0.68/student/year.

### Digital fallback spec

When student taps "I have no supplies today":
- Engine offers 1 of 3 in-app digital tools (depending on lesson type):
  - **Drawing tool** — finger/stylus sketch on canvas, basic color palette, undo
  - **Composition builder** — drag pre-made elements (shapes, lines, colors) onto canvas
  - **Style picker** — choose from 4 master styles, build a composition by tapping elements
- Tier 2 evaluates choices, gives warm feedback (cheaper than Tier 3 vision)
- Full XP awarded
- Galereya entry tagged `make_type: digital_fallback`

### Galereya — student's persistent gallery

- **Every Make joins the Galereya** (physical or digital)
- **Organized by date** + filterable by lesson topic
- **Visual layout:** grid of thumbnails, tap to view full size + read warm response + see master pairing from that day
- **Optional sharing:** student can tap "Sinfga ulashish" (Share to class) — moderated by teacher before public
- **End-of-quarter milestone:** Galereya generates a "Mening Choragim" (My Quarter) summary — collage of all the quarter's makes + 1 highlighted favorite (student picks)
- **Cosmetic unlocks** — completing Master Painters Hall zones unlocks frames for the Galereya (e.g., Renaissance gold frame, Uzbek folk frame)
- **No leaderboards. No ranking. No comparison with classmates.**

### Master Painters Hall — second collection meta-game

- **34 painter cards** unlock over the year (1 per session)
- **4 zones:** Renaissance Masters · Modern Masters · Uzbek Masters · Folk Tradition Masters
- **Card pairing rule:** theory days unlock paired cards (world master + Uzbek master)
- **Card details:** portrait, name, dates, 1 famous work, 1 quote, link to today's story
- **Zone completion bonuses:** unlock Galereya frame + cosmetic accessory
- **Pure cosmetic / collection joy** — never scored, never ranked

---

## §10. Anti-Cheat Tuning (Tasviriy Sanat)

Tasviriy Sanat cheating is functionally complicated — what counts as cheating on a creative make? Anti-cheat focuses on engagement quality.

| Signal | Tasviriy Sanat verdict |
|---|---|
| Speed anomaly (very fast) | **IGNORE** for non-Make tasks; **MONITOR** for The Make (a 30-sec photo upload after 10-min timer is fine, but a 10-sec total session signals skip-through) |
| Length anomaly (very short reflection) | **IGNORE** — short is OK, skip is OK |
| **Photo authenticity** (is this actually their drawing?) | Tier 3 vision can flag stock images / photos of professional art → MONITOR + soft prompt: "Bu rasm sening qo'lingdan bo'lganmi?" (Is this from your hand?). Never accusatory. |
| **Repeated identical uploads** | MONITOR — same photo across 3 sessions = soft teacher flag |
| Mother helping detected (in a photo: adult hand or text style) | **WELCOMED** — explicit framing: collaboration, not cheating |
| Vocabulary jump in reflection text | **IGNORE** — irrelevant for art content |
| Verdict ladder | **Capped at MONITOR** — never SOFT_WARNING, never TEACHER_ALERT for art content |

**Cultural framing:** Mother-as-co-art-teacher is welcomed. Uzbek mothers often teach naqsh, embroidery, kashtachilik to daughters as part of family tradition. NETS preserves this — anti-cheat never penalizes shared making.

---

## §11. Cultural and Regional Anchors (Tasviriy Sanat-Specific)

### Uzbek Master Painters (used in Master Painters Hall)
- **Malik Nabiyev** — historical portraiture (Amir Temur)
- **Rahim Ahmedov** — still-life, landscape (Yoz ne'matlari)
- **Ro'zi Choriyev** — portraiture (Keksa)
- **O'rol Tansiqboyev** — landscape master
- **Abdulhaq Abdullayev** — portrait + historical themes
- **Javlon Umarbekov** — sculpture (Bobur monument)
- **Bahodir Jalolov** — sculpture
- **Alisher Mirzayev** — color painting
- **Akmal Ikromjonov** — landscape
- **Akmal Nur** — landscape (Munavvar tong)
- **A. Mo'minov** — graphics (Chorvoq kuylari)
- **T. Pirmatov** — landscape (Tong)
- **X. Rahimova** — portrait painter (Bukhara)

### Uzbek Sculptors
- **I. Jabborov** — Amir Temur monument (Samarkand)
- **J. Mirtojiyev** — G'afur G'ulom monument (Tashkent), Bobur monument
- **A. Boymatov** — sculpture master
- **A. Rahmatullayev & L. Ryabsev** — Ulug'bek monument (Tashkent)

### Uzbek Folk Artisans + Craft Centers
- **Ceramic masters (Gijduvan):** U. Umarov, A. Hazratqulov, M. Nazrullayev
- **Toy/ceramic workshops (Samarkand):** U. Jo'raqulov, A. Muxtorov
- **Woodcarving (Khorazm):** B. Boisov, R. Matchonov
- **Woodcarving (Tashkent):** K. Turobov, Yu. Ziyomuhamedov
- **Regional centers:** Tashkent, Samarkand, Bukhara, Khiva, Khorazm, Andijan, Namangan, Urgut, Denov

### World Master Painters (always paired with Uzbek master)
- **Renaissance:** Leonardo da Vinci, Raphael Santi, Michelangelo, Albrecht Dürer
- **Dutch Golden Age:** Rembrandt
- **19th-century landscape:** I. Levitan, I. Shishkin, A. Savrasov, A. Kuindji
- **Modern:** Vincent Van Gogh, Henri Matisse, Pablo Picasso, K. Bryullov

### Traditional Art Forms
- **Naqsh (ornament):** islimiy (Islamic floral) · girih (geometric) · murakkab (complex)
  - Elements: madohil (tulip motif), shkufta (spirals), lola, tumor (teardrop)
- **Miniature painting** — Uzbek manuscript tradition, 600+ years
- **Kashtachilik** (embroidery) — folk craft
- **Atlas/adras** — ikat textile tradition (Margilan)
- **Pottery** — Gijduvan, Rishtan, Khiva regional schools

### Names (rotate, ~10–12)
Aziza, Bekzod, Gulnora, Sardor, Malika, Jasur, Dilnoza, Otabek, Zarina, Anvar, Nigora, Komila

### Places
Tashkent, Samarkand, Bukhara, Khiva, Margilan, Khorazm, Andijan, Fergana, Pamir, Chimgan, Registan, mahalla

### Things to Avoid
- Western lifestyle comparisons
- Pork, alcohol references
- Politically sensitive topics
- Family poverty implications
- Doctrinal religious framing
- Ranking Uzbek masters as "below" world masters — always treat as equal

---

## §12. Assessment, Scoring & Escalation

### Scoring philosophy
**There are no grades on Makes.** Engagement = success. Completion = pass.

| Engagement signal | Result |
|---|---|
| Session started + completed | Base XP (~75 XP — higher than Tarbiya 50 because the Make is real effort) |
| The Make uploaded (any photo, any quality) | +50 XP bonus |
| Self-assessment checklist completed | +15 XP bonus |
| Reflection (Phase 7) submitted in any format | +20 XP bonus |
| Galereya share to class (opt-in) | +10 XP bonus |
| Family-bridge "Buvingga ko'rsat" tapped | +10 XP bonus |
| Master Painters Hall zone completed | Cosmetic frame unlocked |
| Skip Phase 7 | No penalty, full base + Make XP |

### No Duolingo Mode
There's no "fail" → no remediation loop needed. If student uses digital fallback ≥3 sessions in a row → soft teacher flag for supplies outreach. If student skips The Make ≥2 sessions in a row → soft teacher check-in.

### No reward labels
- No "Mukammal/A'lo/Yaxshi" labels
- Replaced with: "Bugungi rasming Galereyanga qo'shildi. Yangi ustoz Saroyga keldi: [name]."

### Dual-pathway answer checking
- Mood, MC choices, Tile Match, Sentence Fill = Tier 1 algorithmic <100ms
- Phase 4 Choice + Plan free-text = Tier 2 sentiment check (warm affirmation)
- The Make photo upload = Tier 3 vision rubric ≤10 sec, human fallback >10 sec
- Reflection text/voice = Tier 2 sentiment (private, no AI response by default)
- Drawing reflection = Tier 3 vision (private, ≤10 sec)

---

## §13. AI Tier Strategy — Cost-Aware

Target: **stay within universal $3–5/student/year budget.**

| Phase | Tier | Notes |
|---|---|---|
| 0-A Theme Preview | Tier 2 | Personalized panel selection (Tier 1 fallback) |
| 0-B Flash Cards | Tier 1 | Pre-generated card pool |
| Phase 1 Warm-up Sketch | Tier 1 | Pre-gen warm-up bank |
| Phase 2 Story + Demo | Tier 1 | Pre-gen narrative + pre-recorded demo videos |
| Phase 3 Skill Drill | Tier 1 | Algorithmic game pool |
| Phase 4 Choice + Plan | Tier 2 | Free-text affirmation |
| Phase 5 Master Painters Hall | Tier 1 | Pre-gen card art |
| Phase 6 The Make | **Tier 3 vision** (1 call/session, hard cap) | Warm rubric feedback |
| Phase 6 Digital fallback | Tier 2 | Cheaper than vision |
| Phase 7 Reflection | Tier 2 (only on explicit "respond" tap) | Default = no AI response |
| Did You Know | Tier 2 | Curated pool |

**Cost projection per session:**
- Tier 3 vision (The Make): ~$0.02
- Tier 2 (Phase 4 + Did You Know + occasional Phase 7): ~$0.04
- Tier 1: ~$0
- **Total per session: ~$0.06**

**Annual cost per student:**
- ~34 sessions × $0.06 = **~$2.04/student/year**
- Comfortably within universal $3–5 envelope
- Re-validate if vision pricing changes or session count increases

---

## §14. Teacher Overrides

### Allowed (per session or per student)
- **Mode:** Standard (25–35 min) ↔ Extended (35–45 min, in-class group critique)
- **The Make timer:** visible ↔ hidden ↔ extendable (default: hidden, extendable)
- **The Make sharing:** private ↔ moderated class wall opt-in
- **Digital fallback:** allow ↔ disallow (some teachers may want students to insist on physical supplies)
- **Phase 7 Reflection:** optional (default) ↔ required for in-class use
- **Family-bridge prompt:** show ↔ hide
- **Master Painters Hall visibility:** student-only ↔ class hall mode (collective hall in classroom display)
- **Did You Know facts:** default pool ↔ teacher-curated subset

### Cannot override
- 7-phase structure (replaced phases retain structural slots)
- 0-A + 0-B mandatory
- **The Make mandatory** (cannot drop the climax — this is the Maker-First commitment)
- Stranger Test on narratives + Make prompts
- va_level + transition_skill tag requirement
- Cultural framing (Uzbek-first, master pairing rule)
- Banned mechanics list
- Doctrinally-neutral religious framing
- Cosmetic rewards never purchasable
- Reflection always optional for student
- Digital fallback availability (cannot be permanently disabled — students without supplies must always have a path)

---

## §15. Tagging Schema

Every Tasviriy Sanat task is a JSON record with:

```json
{
  "task_id": "TSV-5-PORT-L27-MAKE-01",
  "subject": "Tasviriy Sanat",
  "grade": 5,
  "language": "uz",
  "textbook_ref": {
    "book": "Tasviriy san'at 5-sinf (Kuziyev et al. 2020)",
    "lesson": 27,
    "lesson_title": "Tasviriy san'atda portret janri",
    "pages": "92-95"
  },
  "standard_ref": {
    "primary": "UZ-TSV-5-PORT-01",
    "alias": "TSV.5.27.1"
  },
  "va_level": "VA-L4",
  "pisa_creative_thinking": true,
  "pisa_reading_l1_l2": true,
  "transition_skill": "VA-L3→L4: take an art history concept and express it through a personal style-imitation make",
  "blooms_level": "Create",
  "phase": "Phase 6 — Kartina (The Make)",
  "game_mechanic": "Notebook Capture (The Make)",
  "make_type": "main",
  "make_prompt_uz": "Bugun sen Leonardo va Nabiyevdan ilhom oldin. Endi sen ham 10 daqiqada bir portret chiz — oilangdagi kimnidir.",
  "make_options": [
    "Avtoportret (oynaga qara yoki o'zingni eslab)",
    "Oilangdagi yaqin odam",
    "Tasavvuringdagi qahramon"
  ],
  "ai_tier": 3,
  "estimated_time_sec": 600,
  "vision_evaluation_focus": ["face proportion", "expression", "composition", "personal interpretation"],
  "warm_response_templates": [
    "Sening portretingda ko'zlarning his-tuyg'usi juda kuchli...",
    "Sening kompozitsiyang oilaviy issiqlikni eslatadi...",
    "..."
  ],
  "cultural_anchors_used": ["Nabiyev portret an'anasi", "Leonardo sfumato"],
  "master_painters_hall_unlock": ["Leonardo da Vinci", "Malik Nabiyev"],
  "scoring": "engagement_only",
  "digital_fallback_available": true
}
```

Standard code structure: `UZ-TSV-5-{TOPIC}-{SEQ}` primary; `TSV.5.{LESSON}.{SEQ}` alias.

---

## §16. Content Production Checklist

Per session (~34 sessions to cover 34 lessons):

| Component | Volume per session |
|---|---|
| Theme Preview 8-panel deck | 8 panels |
| Flash Cards | 5–7 cards (each with mini-demo sketch) |
| Warm-up Sketch prompt | 1 (with pre-gen variants for "no supplies" digital fallback) |
| Story Mode segments | 3 segments × 90 sec, 2–3 narrative variants each |
| Technique demo videos | 3 × 30 sec embedded in Story Mode |
| Skill Drill | 1 game + 1 micro-make prompt |
| Choice + Plan | 3 options + free-text fallback |
| Master Painters Hall card | 1 card per session (or 1 paired card on theory days) |
| The Make prompt | 1 main prompt + 3 option variants + 5–10 templated warm responses |
| Digital fallback tool | 1 in-app tool option per lesson type |
| Reflection prompts | 4 (rotating) |
| Did You Know facts | 4–6 (one per phase transition) |
| Family-bridge prompt (opt-in) | 1 per session |
| All tagged with va_level + transition_skill + textbook_ref |  |

**Total per session: ~30–50 task units** (lower than Science 80–120 because The Make is one rich unit replacing many drill items)

**Total for full Grade 5: ~1,000–1,700 task units across 34 sessions**

Plus production pools:
- ~34 Master Painters Hall cards (one per session, paired on theory days)
- ~30 art proverbs/quotes (rotated as Did You Know + card backs)
- ~12 NPC dialogue trees (Bobo Sherzod, Buvi Saodat, Ustoz Komilov reused from Tarbiya for cross-subject NPC consistency, plus art-specific NPCs)
- ~6 Galereya frame designs (cosmetic unlocks for zone completion)
- ~3 digital fallback tools (drawing tool, composition builder, style picker)

---

## §17. Sample Session Walkthrough — Lesson 27 "Tasviriy San'atda Portret Janri" (Portrait Genre)

**Reference implementation. Match this shape for every session.** This is a **theory lesson** showing how Maker-First handles art history days — the session still ends with The Make.

### Metadata
- **Lesson 27**, textbook pages 92–95
- **Standard:** UZ-TSV-5-PORT-01 / TSV.5.27.1
- **Lesson type:** Theory (art history)
- **Primary VA level:** VA-L4 (Express)
- **PISA tags:** Creative Thinking (primary) + Reading L1–L2 (secondary, for art history text)
- **Transition skill:** "VA-L3→L4: take an art history concept and express it through a personal style-imitation make"
- **Session length:** ~28 min
- **Master Painters Hall unlocks:** Leonardo da Vinci + Malik Nabiyev (paired card — Renaissance + Uzbek)

### Pre-homework (3 min)

**0-A Theme Preview** (2 min, 8 panels):
1. *Sarlavha:* "Portret janri" + Mona Lisa + Nabiyev's Amir Temur side by side
2. *Yaxshi tushuntirish:* "Portret — bu odamning yuzini emas, ruhini ko'rsatish."
3. *Misollar:* 3 portraits — Mona Lisa, Rembrandt self-portrait, Nabiyev's Amir Temur
4. *Hayotiy hikoya:* Leonardo painted Mona Lisa for 4 years, never finished it
5. *Senga taalluqli:* "Sen oilangda eng ko'p qaralgan rasm qaysi?"
6. *Nega muhim:* "Portret — insoniyatning xotirasi."
7. *Hayotda qo'llanilishi:* Modern: passport photos, family albums, Instagram
8. *Bugun nima qilasan:* **"Bugun sen ham bir portret chizasan — 10 daqiqada, oddiy qalam bilan."**

*Did You Know between panels 4–5:* "Mona Liza 1911-yilda Luvr muzeyidan o'g'irlangan — 2 yil davomida topilmadi."

**0-B Flash Cards** (1 min, 6 cards): Portret · Avtoportret · Profil · Anfas · Xarakter · Ruhiy holat (each with mini-demo sketch on the back)

### Phase 1 — Warm-up Sketch (3 min)
- "Daftaringga 5 ta turli ko'z chiz. Har biri 30 soniya. Hayron / xafa / xursand / charchagan / hayratlangan."
- No timer pressure, no upload required
- Soft recall: "O'tgan darsda binokorlik kompozitsiyasini qildik. Eng muhim qoida nima edi?" (visual MC)

### Phase 2 — Hikoya + Demo (6 min, 3 segments × 90 sec + 3 demos × 30 sec)

**Segment 1** (90 sec) — Story: "1503-yil. Florensiya. Bir savdogar Leonardoga keldi: 'Mening rafiqamning rasmini chizib bering.' Leonardo ishni boshladi. Ammo u uch yil davomida tugatmadi..."
**Demo 1** (30 sec) — Embedded video: "Yuz shaklini chizish — oddiy oval bilan boshla. Ko'zlar yuzning yarmida. Burun ko'z va iyak orasida."

**Segment 2** (90 sec) — Story: "Leonardo yangi texnika ixtiro qildi — 'sfumato' deb atadi. Bu — qog'ozda tutun kabi yumshoq o'tish."
**Demo 2** (30 sec) — Embedded video: "Soyalashni barmoq bilan sekin yumshatib ko'r."

**Segment 3** (90 sec) — Story: "1968-yil. Toshkent. Malik Nabiyev o'z ustaxonasida o'tirar edi. Uning oldida bo'sh qog'oz. U Amir Temurning rasmini chizmoqchi edi — lekin Amir Temur 600 yil oldin yashagan, hech kim uni ko'rmagan. Nabiyev nima qildi?"
**Demo 3** (30 sec) — Embedded video: "Xarakterli yuzni chizish — qoshlar yo'nalishi kayfiyatni ko'rsatadi."

After each segment, optional "Daftaringda tezda sinab ko'r" prompt (no upload, no scoring).

### Phase 3 — Skill Drill (4 min)

**Game** (2 min) — Memory Match: 6 master/painting pairs
- Leonardo ↔ Mona Liza
- Rembrandt ↔ Avtoportret
- Van Gogh ↔ Avtoportret (qishki)
- Nabiyev ↔ Amir Temur portreti
- Choriyev ↔ Keksa
- Ahmedov ↔ Yoz ne'matlari

**Micro-make** (2 min) — "Daftaringga bitta ko'zni his-tuyg'u bilan chiz: hayron / xafa / xursand. O'zing tanla."

### Phase 4 — Tanlov + Reja (3 min)

**Aziza picks today's Make from 3 options:**
1. **Avtoportret** — "Oynaga qarab yoki o'zingni eslab chiz"
2. **Oilangdagi kimnidir** — "Onangni, dadangni, bobongni, buvingni, ukangni, opangni"
3. **Tasavvuringdagi qahramon** — "Adabiy yoki tarixiy qahramon — kim seni qiziqtirsa"

Aziza picks Option 2 — onasi.

**1-min plan prompt:** "Onangning yuzini qaysi tomondan ko'rasan — old yoki yon? Eng muhim narsa nima — ko'zlarmi yoki tabassummi? Yorug'lik qayerdan keladi?"

### Phase 5 — Master Painters Hall (1 min)

Today's paired card unlocks:
- **Leonardo da Vinci** (Renaissance Masters zone) — "Sfumato — yumshoq nur kabi"
- **Malik Nabiyev** (Uzbek Masters zone) — "Tarixiy obrazlar — bizning xotiramiz"

Both cards slide into the Hall with brief animation. Aziza taps to read backs.

### Phase 6 — KARTINA (10–12 min) ⭐

**Setup** (15 sec): "Sening tanlovingni eslab qoldim — onangning portreti. Tayyormisan? Qalam, daftar, va sevgi kifoya."

**Reference panel** (sidebar, collapsible): Leonardo Mona Lisa thumbnail + Nabiyev Amir Temur thumbnail. Aziza can peek for inspiration.

**Optional calm music** — off by default.

**Optional timer** — hidden by default. Aziza can show it.

**Aziza draws her mother for ~10 minutes.** Pencil on notebook. She tries to remember her mother's eyes from memory, the way her hair falls, her gentle smile. The Mona Lisa thumbnail in the sidebar reminds her that even Leonardo took years — she has 10 minutes, but that's enough for one honest sketch.

**Mid-make checkpoint at 5 min:** "Qanday ketyapti? Davom et yoki bir nafas ol?" Aziza taps "Davom et."

**At 10 min**, Aziza taps "Tayyor" and takes a phone photo of her drawing. Auto-crop assist helps her square it.

**Tier 3 vision evaluation (8 sec):**

> "Aziza, sening onangning portretida ko'zlarning his-tuyg'usi juda kuchli — xuddi mehrli onaga qaragandek. Keyingi safar yorug'lik qaysi tomondan kelishini ham ko'rsatib ko'r — bu portretni yanada jonliroq qiladi. Sening rasming Galereyangga qo'shildi."

Galereya updated. ~150 XP awarded.

**Optional self-assessment** (Aziza taps to skip — already feels good).

### Phase 7 — O'ylab Ko'rish (1 min, optional)

Prompt: "Bugungi portreting senga qanday yoqdi?"

Aziza taps voice mode and says (15 sec): "Onamning ko'zlarini chizishda qiyinchilik bo'ldi, lekin men o'ylaymanki uning tabassumi yaxshi chiqdi. Men bu rasmni unga ko'rsataman."

Optional family-bridge prompt: **"Buvingga yoki onangga ko'rsat?"** Aziza taps "Ha, ko'rsataman."

### Post-session
- Total XP: ~155 (75 base + 50 Make + 20 Reflection + 10 family-bridge)
- Galereya updated with onasi portret
- Master Painters Hall: Leonardo + Nabiyev unlocked
- Mood logged (private)
- Teacher dashboard: "Aziza completed Lesson 27 — uploaded Make, shared reflection, will show family"
- Did You Know facts shown across phase transitions: Mona Lisa stolen 1911 · Rembrandt 80 self-portraits · Nabiyev studied at Surikov Institute

---

## §18. Open Questions / Things to Validate

1. **Vision evaluation accuracy on student art** — Tier 3 vision needs piloting on actual G5 student photos to confirm warm-feedback rubric works (not too technical, not too vague).
2. **Digital fallback tool design** — 3 tool types (drawing / composition builder / style picker) need UX prototyping.
3. **Photo upload reliability on shared family smartphones** — bandwidth, camera permissions, photo quality on low-end devices.
4. **Master Painters Hall pairing logic** — confirm with curriculum lead which world masters pair with which Uzbek masters across all 34 sessions.
5. **The Make timer visibility default** — should it be hidden or shown? Pilot both, measure engagement.
6. **Galereya class-share moderation pipeline** — teacher pre-approves vs. AI pre-screen + teacher approves?
7. **Style Mimic mini-game content** — needs ~6 master brushstroke samples, hand-curated.
8. **Family-bridge "Buvingga ko'rsat" cultural validation** — confirm with Uzbek teachers that family-show prompt resonates.
9. **Quarterly "Mening Choragim" summary collage** — auto-generated end-of-quarter Galereya highlights — needs UX design.
10. **Cross-subject NPC sharing** — Bobo Sherzod / Buvi Saodat from Tarbiya — should they appear in Tasviriy Sanat too, or have art-specific NPCs?
11. **Vision call cost re-validation** — ~$0.02/call assumed; re-check if Anthropic vision pricing changes.
12. **Theory-day Make prompts** — style-imitation Makes need careful piloting to avoid feeling like "copy this artist." Should be "respond to this artist."

---

## §19. Production Handoff

### Contract for content team

Build Tasviriy Sanat G5 content matching the **§17 walkthrough shape exactly** for every session — even theory lessons end with The Make. For each of ~34 sessions:

1. **Source from textbook** — every task traces to Lesson + page range
2. **Apply §4 psychology parameters** — 25–35 min, calm pacing, no failure states, warm tone
3. **Use §11 cultural anchors** — rotate Uzbek masters, ALWAYS pair with world masters
4. **Tag every task** per §15 schema (va_level, pisa tags, transition_skill, textbook_ref, make_type)
5. **Pass Stranger Test** on every Story segment + Make prompt
6. **Pre-generate Make warm response banks** — 5–10 templates per Make prompt
7. **Author Master Painters Hall cards** — 34 cards (one per session, paired on theory days)
8. **Curate Did You Know pool** — ~80 facts (4–6 per session × 34 sessions, with overlap allowed)
9. **Author technique demo videos** — 3 × 30 sec per session = ~100 short videos (slow hand-cam style, no music, mimicable)
10. **Build digital fallback tools** — 3 tool types covering all 34 sessions
11. **Validate against §18 open questions** before production locks

### Quality gates
- **Pedagogy review** by 1 pedagogy lead + 1 G5 Uzbek Tasviriy Sanat teacher
- **Language review** by Uzbek native speaker
- **Cultural validation** by Uzbek art historian (master pairing accuracy)
- **Vision rubric piloting** with 50+ real G5 student photos before launch
- **Pilot in 2 classrooms** (1 urban Tashkent with full art supplies, 1 rural Fergana with limited supplies — test digital fallback)

### Timeline
- Research phase complete (this doc): done
- Content authoring (34 sessions): ~12–14 weeks
- Technique demo video production: ~8 weeks (parallel)
- Vision rubric piloting: ~3 weeks
- Pilot + validation: ~4 weeks
- Full rollout: ~ pilot + 4 weeks

---

## §20. Versioning and Review

- **Version 1.0** — 2026-04-08, Tasviriy Sanat G5 first framework, "Maker-First" design
- **Reviewers needed:**
  - Product/pedagogy lead
  - Uzbek G5 Tasviriy Sanat teacher (1–2)
  - Uzbek art historian (cultural validation)
  - Curriculum specialist
  - Content lead
  - Vision evaluation engineer (Tier 3 cost/accuracy review)
- **Next revision** after first 5 sessions stress-tested in pilot
- **Sibling frameworks to create after this:**
  - Tasviriy Sanat G5 Russian edition (sibling)
  - Tasviriy Sanat G6, G7 (next grades, same Maker-First shape)
  - Apply Maker-First learnings to other making subjects (Texnologiya Service track for cooking/sewing — could borrow the digital fallback pattern)

---

**End of NETS Tasviriy Sanat G5 Framework v1.0.**

*Companion docs:* `NETS-Homework-Engine-UNIFIED.md` · `NETS-Homework-Engine-Blueprint.docx` · `NETS-UI-UX-Design-Spec.docx` · `Researches/qwen-grade5-psychology-findings.md` · `Extracted Texts/_tasviriy_sanat_extracted.txt` · `Book & Resourses/5-sinf_Tasviriy_sanat__2020_(elekton_darslikbot).pdf`
