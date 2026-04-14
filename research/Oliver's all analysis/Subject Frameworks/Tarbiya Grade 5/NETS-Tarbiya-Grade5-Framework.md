# NETS Tarbiya — Grade 5 Subject Framework

**Version:** 1.0 (Chill Mode)
**Status:** Production-ready specification — single source of truth for Grade 5 Tarbiya homework
**Date:** 2026-04-08
**Supersedes:** none (first Tarbiya framework)
**Inherits from:** `NETS-Homework-Engine-UNIFIED.md` v2.0 + `NETS-Homework-Engine-Blueprint.docx` v1.0
**Psychology base:** `Researches/qwen-grade5-psychology-findings.md`
**Textbook source:** Tarbiya, 5-sinf "Baxt va Muvaffaqiyat Sirlari" (Quronov, Risyukova, Tigay et al., G'afur G'ulom, 2020, 112pp, ISBN 978-9943-6447-6-2)

> **Reading order:** §0 first (decisions log), then §2 (what is this subject), then §6 (the engine). Everything else is reference.

---

## §0. Resolution Log

Tarbiya is **the first NETS subject that breaks the universal homework mold by design.** It is values/character/civic education — reflective, narrative, no PISA domain, no objective "correct answer" for L2+ tasks. Forcing the standard NETS rigor on it would feel evaluative and joyless and would actively damage moral learning (overjustification effect, Deci/Koestner/Ryan 1999). The user's directive: *"make this subject more like gamified, students should be able to chill while doing homework."*

This resolution log records the decisions made when Tarbiya's nature collided with UNIFIED immutables.

| # | Conflict | Resolution | Reasoning |
|---|---|---|---|
| 1 | UNIFIED §6 mandates Final Boss with HP/defeat. Values content has no defeatable correct answer. | **REPLACE Final Boss with "Big Decision"** — single longer scenario, student picks + writes 1-sentence why, AI gives warm reflective response, no fail state, always passes. Big Decision satisfies the "session climax" requirement of UNIFIED §6 without the combat metaphor. | Defeating a moral dilemma is incoherent. Reflective tasks require psychological safety (Harter 2012); failure states trigger shame and disengagement. |
| 2 | UNIFIED §4 sets Standard session 30–45 min. | **Override to 15–25 min Standard** for Tarbiya. | Reflective/values content runs on System 2 (slow, effortful). Lower cognitive load is required (Sweller 1988). G5 sustained attention 20–30 min for academic work drops sharply for emotional/reflective work. |
| 3 | UNIFIED §11 gamification economy includes XP, streaks, leagues. Overjustification effect specifically warns against extrinsic rewards for moral behavior. | **Keep XP/streaks but reframe**: XP for *engagement/reflection effort*, never for "being virtuous." NO leagues at all for Tarbiya. Streaks are auto-frozen on miss (no shame). Replace ranking with **Fazilatlar Bog'i (Garden of Virtues)** — pure collection meta-game. | Overjustification is documented (Deci et al. 1999 meta-analysis). Rewarding moral choices with points teaches "virtue = points," which collapses when points stop. Collection/cosmetic rewards don't crowd out intrinsic motivation. |
| 4 | UNIFIED §6.2 Story Mode has comprehension checkpoints with "right answers." | **Tarbiya Story Mode uses branching dialogue with no wrong path.** Every choice advances the narrative. Choices are tracked for §17 sample chapter analytics, not scored. | Narrative transportation (Green & Brock 2000) and observational learning (Bandura 1977) work BEST when the reader feels safe to try perspectives. Wrong-answer gates break transportation. |
| 5 | UNIFIED §6 Phase 4 Real-Life Challenge has "tricky distractors" and "expert POV." | **Tarbiya RLC is "Sen bo'lsang nima qilarding?"** (What would YOU do?) — 3–4 valid choices, each gets a thoughtful Tier 2 AI response, no distractors, no "best answer." | Same psychological safety reasoning. Uzbek G5 students live in 35–38 student classrooms with rare individual attention (TIMSS 2023); the homework is one of few private spaces. |
| 6 | UNIFIED §3 mandates PISA tagging on every task. Tarbiya has no clean PISA fit. | **Use PISA Reading L1→L2 + PISA Creative Thinking as secondary tags. Primary tag = custom "Moral Reasoning" track (MR-L1→MR-L4) + SEL competency tag (5 SEL dimensions).** Document the custom track in §3. Standard codes use prefix `UZ-TAR-5-{TOPIC}-{SEQ}` and `TAR.5.{BOB}.{MAVZU}.{SEQ}`. | Tarbiya is mandated by Uzbek MoE; it can't be skipped just because PISA doesn't cover it. The Moral Reasoning track keeps the tagging schema intact. |
| 7 | UNIFIED §13 Anti-Cheat assumes a correctness signal. | **Tarbiya anti-cheat watches engagement quality only**: paste detection on reflection text (still meaningful), zero penalty for speed/length, mother-helping always reframed as collaborative. No verdicts above MONITOR. | Cheating on a values journal is functionally impossible. The only meaningful concern is whether the student actually engaged. |
| 8 | UNIFIED §16 Content Production targets ~80–120 task units/session. | **Tarbiya ~30–50 task units/session** (lighter content). | Shorter session, lower density. Each unit is "thicker" — a 90-second reflective scenario beats five 18-second drill items. |
| 9 | UNIFIED §6.5 Phase 5 Consolidation defaults to diagram recall before boss. | **Tarbiya Phase 5 = "Fazilatlar Bog'i" virtue collection moment** — student adds today's virtue card to their persistent garden, sees a brief animation, feels the unlock. No recall test. | The garden IS the consolidation; collecting symbolizes integrating the value. |
| 10 | UNIFIED §6.7 Reflection mandates 1 sentence minimum. | **Tarbiya Reflection is fully optional** — voice OR text OR drawing OR skip. XP identical regardless. | Mandatory reflection on values feels coercive. Optional reflection respects autonomy (SDT, Deci & Ryan 2000) and still captures engagement from students who want to share. |
| 11 | UNIFIED §10 requires content pool ≥85 items per topic. | **Tarbiya target ≥40 items per topic** (lower density acceptable). | Each item is denser; 85-item pools designed for drill subjects. Quality > quantity for reflective content. |
| 12 | UNIFIED bans Peer Teaching for many G5 contexts. | **Tarbiya KEEPS Peer Teaching as opt-in** via "Hikoyangizni ulashing" (Share your story) — student can post a reflection to a moderated class wall (teacher-approved). Never required. | Tarbiya benefits from prosocial visibility when safe. Opt-in + moderation prevents the issues that ban it elsewhere. |
| 13 | UNIFIED Boss retry limit (max 2 retries, then continue). | **N/A — no Boss for Tarbiya.** Big Decision has no retries because it has no fail state. |  |
| 14 | Religious framing | **Hold doctrinally-neutral line** (matches textbook). Cultural Islamic warmth implicit in cultural anchors §11; no Quranic citations, no halal/haram terminology. | Textbook itself is values-aligned without doctrine; preserve its accessibility across diverse families. |
| 15 | Family-bridge tasks (interview elders, observe family) | **All family-bridge tasks are OPT-IN side quests** — bonus XP, never required for session completion. In-app NPC fallback ("Bobo Sherzod" elder character) for students without access. | Some students have hard home lives; Tarbiya content about family/responsibility can trigger. Trauma-informed pedagogy basics. |
| 16 | UNIFIED bans visible difficulty labels. | **Tarbiya has no difficulty labels at all** because there are no difficulty tiers in the chill-mode design. Internally, content is tagged MR-L1 through MR-L4 for selection logic only. |  |

**16 resolutions logged. All trace to two roots:** (1) values content needs psychological safety > performance pressure, and (2) overjustification effect rules out scoring moral behavior.

---

## §1. Audience Profile

**Inherited from `qwen-grade5-psychology-findings.md` §1–2 + §7 (universal Grade 5 Uzbek base).** Subject-agnostic facts unchanged; Tarbiya-specific deltas noted inline.

**Cognitive (universal G5):**
- Late concrete operational (Piaget); abstract reasoning emerging but not reliable
- Working memory 4–5 chunks (Cowan 2001) → max 3 new concepts per instruction
- Sustained attention 20–30 min academic, **drops to 15–20 min for reflective/emotional work** (Tarbiya delta)
- Lexile 830–1010L; receptive vocab ~12–14k, productive ~6–8k
- Metacognitive accuracy ~0.4–0.5 — guided reflection only, never open-ended

**Social/emotional (universal G5):**
- Self-concept fragile under public evaluation (Harter 2012)
- Peer comparison sensitivity high and intensifying (Ruble et al. 2004)
- Failure tolerance low without reframing — attribute to strategy not ability (Dweck 2006)
- Reward sensitivity high for variable-ratio rewards tied to competence
- Recovery from negative feedback: 30–90 sec processing time (Thompson 2011)

**Tarbiya-specific cognitive load:**
- Values reasoning is System 2 (slow, effortful) — Kahneman dual-process — requires lower extrinsic load than drill
- Erikson Industry vs. Inferiority transition: students want to demonstrate competence but cannot tolerate public moral judgment
- Kohlberg conventional level 3 ("good boy/girl orientation") — they care intensely about being seen as good, which makes failure-as-bad framing especially toxic

**Uzbek context (from §7 of psychology base):**
- 35–38 student classes, teacher-centered, formal teacher-student dynamic
- Mother is primary homework supervisor; cultural attitude treats struggle as "not trying hard enough"
- Shared family smartphone primary device; mobile-first, low-bandwidth, portrait orientation
- After-school window 2–3 hrs; peak homework 17:00–19:00
- Resonant figures: Amir Temur, Navoiy, Ulugh Beg, Ibn Sino, Beruni, Avloniy
- Resonant places: Registan, Bukhara, Khiva, Aral, Chimgan
- Primary language Uzbek (Latin); Russian secondary, English A1–A2

---

## §2. Subject Identity

**Tarbiya** = upbringing/character/values/civic education. Mandatory in Uzbek schools from Grade 1; Grade 5 marks the start of basic secondary and the textbook's transition from concrete child-world (family, friends, body) to early civic identity (citizen, ancestor, heritage, environment).

**Pedagogical posture:** *Wonder, reflection, and quiet pride* — never preaching, never testing. The teacher's job is to ask "Sen bo'lsang qanday qilarding?" and let students discover virtue through narrative and choice. The textbook explicitly avoids doctrinal preaching; NETS preserves that.

**Content domains** (from Tarbiya G5 textbook analysis, organized into 6 thematic clusters):

1. **Civic identity & patriotism** (Bob I, mavzular 1–8) — Vatanga muhabbat, responsibility, rights & duties, environmental stewardship
2. **Emotional & interpersonal development** (Bob II, mavzular 9–14) — emotional literacy, empathy, mehr (compassion), aspiration, respect for human dignity
3. **Cooperation & friendship** (Bob III, mavzular 15–22) — helping others, hamkorlik, animal care, conduct/manners, health
4. **Personal aspiration & perseverance** (cross-cutting Bob II–III) — motivatsiya, tirishqoqlik, qat'iyatlilik, goal-setting
5. **Cultural memory & heritage** (Bob IV, mavzular 23–29) — historical memory, family lineage, national traditions, literary culture
6. **Environmental & global awareness** (Bob I, 7–8 + threaded) — ecological responsibility, conservation, global cooperation

**Standard code prefix:** `UZ-TAR-5-{TOPIC}-{SEQ}` (primary) · `TAR.5.{BOB}.{MAVZU}.{SEQ}` (alias)

**Textbook source of truth:** Tarbiya 5-sinf, Quronov et al. 2020. Every NETS task must trace to textbook page range.

**Chapter map → session map:**

| Bob | Mavzular | Sessions | Estimated LUs |
|---|---|---|---|
| I — Men fuqaroman | 1–8 (4 sections) | 6 | ~12 |
| II — Men insonman | 9–14 (6 sections) | 7 | ~16 |
| III — Men va do'stlarim | 15–22 (5 sections) | 6 | ~13 |
| IV — Men va ajdodlarim | 23–29 (4 sections) | 5 | ~10 |
| **Total** | **29 mavzular** | **24 sessions** | **~51 LUs** |

(Recommend ~60–70 micro-LUs in production for richer content variety; 1 session ≈ 1 mavzu where mavzular have 1–2 lessons, 0.5 session for combined mavzular.)

---

## §3. The Tarbiya Learning Track — Custom Domain

Tarbiya does not map to PISA Math/Reading/Science. We define a **custom 4-level Moral Reasoning (MR) track** plus 5 SEL competency tags. PISA Reading L1–L2 and PISA Creative Thinking are kept as **secondary tags** for cross-subject analytics.

### Moral Reasoning Levels

| Level | Code | Capability | Example task |
|---|---|---|---|
| **MR-L1** | Recognize | Identify a virtue/concept in a narrative | "Namoz Jumayev qaysi fazilatni ko'rsatadi?" (matching) |
| **MR-L2** | Apply | Apply a virtue to a familiar scenario | "Komila ukasiga g'amxo'rlik qilishi kerakmi yoki do'sti bilan gaplashishi kerakmi? Nega?" (scenario judgment) |
| **MR-L3** | Weigh | Weigh competing virtues in a dilemma | "Halollik va do'st bilan sodiqlik to'qnashganda nima qilasiz?" (open reasoning) |
| **MR-L4** | Construct | Construct a coherent moral argument with evidence | "Mas'uliyat haqida o'z fikringizni 3 jumlada yozing va misol keltiring." (construction) |

### SEL Competency Tags (CASEL-aligned, Uzbek-adapted)

Every task carries ONE primary SEL tag:
- **SA** Self-Awareness — recognizing emotions, strengths, limits
- **SM** Self-Management — perseverance, responsibility, goal-setting (tirishqoqlik, mas'uliyat)
- **SoA** Social Awareness — empathy, perspective-taking, respect (mehr, hurmat)
- **RS** Relationship Skills — cooperation, communication, conflict resolution (hamkorlik)
- **RDM** Responsible Decision-Making — ethical reasoning, systems thinking

### Distribution targets per session

| Bucket | % of session tasks | Purpose |
|---|---|---|
| MR-L1 (Recognize) | 30% | Onboarding, vocab anchoring, no-stress entry |
| MR-L2 (Apply) | 40% | Core practice — most session content |
| MR-L3 (Weigh) | 25% | Story Mode + Big Decision content |
| MR-L4 (Construct) | 5% | Optional reflection prompts only |

### Mandatory tagging schema (every task)

Every Tarbiya task carries:
- `mr_level` — MR-L1 through MR-L4
- `sel_competency` — SA / SM / SoA / RS / RDM
- `pisa_reading_l1_l2` — optional secondary tag if reading task
- `pisa_creative_thinking` — optional secondary tag if generative task
- `transition_skill` — narrative description of which capability the task scaffolds (e.g., "MR-L1→L2: take a virtue from a story and apply it to a real situation")
- `textbook_ref` — Bob/Mavzu/page

---

## §4. Psychology Filter — Applied Parameters

Applies the universal Grade 5 psychology base to Tarbiya, with chill-mode tuning.

### Session timing
- **Standard session: 15–25 min** (Tarbiya override; lower than universal 30–45)
- **Extended session: 25–35 min** (in-class, teacher-led, group reflection format)
- **Single phase max: 4–6 min** (lower than universal 5–9)
- **Inter-phase break: 8–20 sec** with Did You Know cultural facts (longer than universal because reflective work needs slower pacing)
- **1 session per day max** (no double sessions for reflective content)
- **Deploy window: 17:00–19:00** (after dinner, family-quiet time)

### "Difficulty" calibration (chill mode)
- **No success rate target** — there are no right answers for MR-L2+ tasks
- **Adapt every 2–3 tasks** based on engagement signals (time-on-task, choice depth, reflection length), not correctness
- **No difficulty labels, no tiering visible to student**
- **No pass threshold** — every session is "passed" by completing it
- **Recovery framing** — never use "Notog'ri" (Wrong); always "Boshqacha qarash" (Another perspective) or "Ko'proq o'ylab ko'ring" (Think a bit more)
- **Productive reflection time** — 30 sec is enough; do not push past 60 sec without offering a hint or alternative phrasing

### Banned techniques (Tarbiya-specific, citations from psychology base)
1. **Public wrong answers / leaderboards** — Harter 2012, fragile self-concept
2. **Real-time multiplayer competition** — Dweck 2006, demoralizes weaker students
3. **XP for "being virtuous"** — Deci/Koestner/Ryan 1999, overjustification effect
4. **Mandatory reflection writing** — Roebers 2017, metacognition immature; coercive
5. **Failure states / fail screens** — Dweck 2006, triggers shame
6. **Boss combat metaphor** — incoherent for moral content
7. **"Right answer" framing for L2+ tasks** — collapses authentic engagement
8. **Mandatory family-bridge tasks** — trauma-informed: not all students have safe family contexts
9. **Religious doctrinal framing** — textbook avoids; preserve accessibility
10. **Western emotion taxonomy** — textbook uses ijobiy/salbiy/betaraf; do not impose Western categories
11. **Timed reflection** — values reasoning is System 2; timer pressure breaks it
12. **Comparative ranking** ("you scored higher than 60% of classmates") — overjustification + shame
13. **"You're a good person" praise** — ability-praise variant, fixed-mindset risk; use effort/strategy framing instead
14. **Cosmetics purchasable with money** — UNIFIED rule, reaffirmed
15. **Why Chain ≥3 levels** — universal G5 working memory ceiling

### Mandatory inclusions
1. **Narrative-first content** — Mar & Oatley narrative theory; Bandura observational learning
2. **Branching dialogue with no wrong path** — psychological safety + autonomy (SDT)
3. **Effort/process praise only** — Dweck growth mindset
4. **Collection/cosmetic rewards via Virtue Garden** — variable-ratio without overjustification
5. **Cultural anchors in every session** — Uzbek names, places, scientists, proverbs
6. **Optional family-bridge side quests** — bonus XP, never required
7. **Warm Tier 2 AI reflective responses** to Big Decision (5–10 templated reactions per scenario)
8. **NPC elder fallback ("Bobo Sherzod")** for students without family-bridge access
9. **Calm, slow pacing** — longer inter-phase breaks, no countdown timers in any phase
10. **Did You Know cultural facts** between phases — anchoring, not pressure

---

## §5. Pre-Homework Sessions 0-A & 0-B

### 0-A Theme Preview (Mavzu Tanishuvi) — 2–3 min

**Format:** 8-panel swipe deck (vertical TikTok-style), student-paced, no scoring, no XP, no timer.

**Tarbiya 8-panel structure:**

| Panel | Content | Tarbiya example for Mavzu 10 (Mehr qadri) |
|---|---|---|
| 1. **Sarlavha** (Title) | Mavzu name + warm hook image | "Mehr qadri" + grandmother holding child's hand |
| 2. **Yaxshi tushuntirish** (Better explanation) | Concept defined with metaphor | "Mehr — bu boshqa odamning yuragini his qila olish. Ko'ylakdek issiq, qish kunidek zarur." |
| 3. **Misollar** (Examples) | 2–3 visual examples from daily Uzbek life | Mother bringing tea, friend sharing somsa, helping classmate carry books |
| 4. **Hayotiy hikoya** (Real-life story) | 3-sentence story featuring an Uzbek figure | Mini-story about Ibn Sino healing a poor patient without payment |
| 5. **Senga taalluqli** (Personal hook) | "Have you ever..." direct connection | "Sen kimga mehr ko'rsatgansan? Buni eslab ko'r." |
| 6. **Nega muhim** (Why it matters) | Long-arc significance | "Mehr bo'lmagan jamiyatda hech kim baxtli yashay olmaydi." |
| 7. **Hayotda qo'llanilishi** (Real application) | Modern Uzbek profession/context | A nurse, a teacher, a mahalla volunteer |
| 8. **Qo'shimcha materiallar** (Additional materials) | Optional extras (poem, song, video) | Avloniy quote about mehr; optional 30-sec animated video |

- **Animation:** 400 ms whoosh + 600 ms assembly per panel transition
- **Pagination dots, swipe forward only,** can skip back
- **No XP, no scoring, no timer** — pure exploration
- **One Did You Know between panels 4–5** (cultural/historical fact)
- **Stranger Test:** Could a Grade 5 Uzbek student understand and feel something from this without a teacher present? If no, rewrite.

### 0-B Flash Cards (Tezkor Kartochkalar) — 1–2 min

**Format:** 5–7 card carousel, 3D depth effect, returnable mid-session as reference (not counted as hint).

**Tarbiya Flash Card structure:** Each card has:
- **Front:** Concept name in Uzbek (e.g., "Mehr") + visual icon
- **Back:** 1-sentence definition + 1 visual example + 1 proverb or quote

**Cap: 5–7 cards** (Cowan working memory ceiling). Concepts are dense — better fewer, deeper.

**Example cards for Mavzu 10:**
1. Mehr — compassion/kindness
2. Mehribonlik — kindheartedness in action
3. Hurmat — respect
4. G'amxo'rlik — care/looking-after
5. Yordam — help

Card flip: 600 ms (slower than universal because Tarbiya is paced for reflection, not speed). Tap-to-prompt visibility 3–4 sec. Loop ding sound on flip. Russian/English equivalents in parentheses optional but discouraged for Tarbiya (cultural authenticity).

---

## §6. The 7-Phase Engine — Tarbiya Chill Mode

**Total session: 15–25 min** (Standard) including 0-A + 0-B + 7 phases.

### §6.1 Phase 1 — Mood Check-in (Kayfiyat) · ≤2 min

**Replaces universal Memory Sprint.** Drill-style recall is wrong opening for reflective content.

- **3 emoji-tap "How are you today?"** — happy / okay / tired / sad / excited (5 emoji bar)
- **1 soft recall** from previous session: "O'tgan darsda qaysi fazilatni o'rgandik?" (4-option visual MC)
- **No timer, no penalty for any answer**
- **XP awarded just for tapping** (engagement = success)
- **Warm response to mood**: sad → "Bugun ozgina sokinroq boshlaymiz" (Let's start gently today)
- **Tier 1 algorithmic** — pre-generated response bank by mood

**Adaptation gate:** If student taps "sad" or "tired" 3 sessions in a row → **Soft teacher flag** (privacy-respected — teacher sees "Aziza may need a check-in" not "Aziza is sad")

### §6.2 Phase 2 — Hikoya Vaqti (Story Time) · 5–7 min

**Replaces universal Story Mode.** Same shape (3 segments × 90 sec) but **branching dialogue, no wrong path.**

- **3 narrative segments**, each ending in a choice (not a comprehension question)
- **Choices are tracked** (which path the student took), not graded
- **Every choice advances the story** — no dead ends, no retries
- **Subject-specific narrative approach for Tarbiya:**
  - **Bob I (citizenship/ecology):** Real-Uzbek-place stories (Aral, mahalla, Chimgan) with environmental/civic dilemmas
  - **Bob II (emotions/aspiration):** Character-arc stories with Uzbek figures (Ulugh Beg, Avloniy, Beruni) showing perseverance and emotional growth
  - **Bob III (friendship/cooperation):** Peer-context stories in Uzbek school/mahalla settings
  - **Bob IV (heritage/memory):** Multi-generational stories with grandparent characters and historical depth
- **Lexile 830–1010L**, ≤14 word sentences, active voice, second-person ("Sen") POV
- **Stranger Test quality gate** on every segment
- **No timer visible** — student sets the pace
- **Tier 1 pre-generated** branches + **Tier 2** for occasional adapted variants

### §6.3 Phase 3 — O'yinlar Tanaffusi (Game Breaks) · 3–5 min

**Light, 2 games (not 3),** interleaved between Story segments OR after Story Mode ends — teacher's choice.

**Game slot rules:**
- **Slot 1: Visual/recognition warmup** — Tile Match (virtue cards), Memory Match (proverb pairs), Sentence Fill (Avloniy quote completion)
- **Slot 2: Light reasoning** — Mystery Box (Uzbek cultural fact reveal), Why Chain (max 2 levels, soft topic only — "Why is mehr important?"), Codebreaker (decode proverb)

**No Notebook Capture as core game** for Tarbiya — but offered as **optional bonus** for reflective drawing tasks (e.g., "Draw your family's most important value").

**Banned/limited mechanics for Tarbiya** (full table in §8):
- Adaptive Quiz NO
- Real-time multiplayer NO
- Connect Four / Tic Tac Toe vs AI YES (recreational, no values content)
- Speed Sort LIMITED (only for visual sequencing, never values judgment)

### §6.4 Phase 4 — Sen Bo'lsang? (What Would You Do?) · 3–5 min

**Replaces universal Real-Life Challenge.** No tricky distractors, no expert POV.

- **1 scenario card** with Uzbek-context dilemma
- **3–4 choices**, each is valid
- **Every choice gets a Tier 2 AI response** that explores the consequences (warm, reflective, never judgmental)
- **No "best answer" indicator** — student sees all responses if they tap "Boshqa javoblarni ko'rsat" (Show other answers)
- **Optional follow-up:** "Sen bunga qo'shilasanmi?" (Do you agree?) with thumbs up/down — pure expression, no scoring
- **Examples:**
  - *Bob I:* "Mahallangizda axlat to'kilgan. 4 xil yo'l bor: o'zing yig'asanmi, ota-onangga aytasanmi, qo'shnilarni chaqirasanmi yoki muhim emas, deb o'tib ketasanmi?"
  - *Bob III:* "Do'sting darsda kitob unutgan. 3 xil yo'l..."
- **Tier 2 budget:** ~5 templated responses per scenario in Uzbek

### §6.5 Phase 5 — Fazilatlar Bog'i (Garden of Virtues) · 2–3 min

**Replaces universal Consolidation.** No diagram recall, no test.

- **Today's virtue card unlocks** with a brief animation (4–5 sec)
- **Card joins the persistent Garden** — student sees garden grow over weeks
- **Tap to read virtue card details:** definition, today's story snippet, related Uzbek proverb
- **Garden visual:** plants/flowers grow as cards collect (Bob I = oak tree for citizenship, Bob II = flower for emotion, Bob III = bridge for friendship, Bob IV = old book for heritage)
- **No "did you remember it correctly?" gate** — collection IS the consolidation
- **5-card combo bonus:** every 5th unique virtue triggers a small celebration animation + cosmetic unlock (avatar accessory tied to virtue theme)
- **Tier 1** algorithmic, pre-generated card art

### §6.6 Phase 6 — Katta Qaror (The Big Decision) · 3–5 min

**REPLACES Final Boss.** This is the session climax — but it's a no-fail reflective decision, not combat.

**Format:**
1. **Setup** (30 sec) — A longer dilemma scenario (4–6 sentences) tied to today's mavzu, with rich Uzbek context. Often a callback to one of the Story Mode characters.
2. **Choice** — 3 options, each thoughtful. The student picks one.
3. **Justification** (the only "writing" task) — "Nega bu javobni tanlading? 1 jumlada yoz." (Why this choice? Write 1 sentence.) Voice input optional.
4. **AI response** (Tier 2 generative) — Warm, reflective, explores the student's reasoning. Templates:
   - Affirms: "Sening fikring meni o'ylantirib qo'ydi..."
   - Extends: "Bunga qo'shimcha qilish mumkin..."
   - Gentle counter-perspective: "Ba'zilar buni boshqacha ko'radi..."
5. **Always passes.** XP awarded. Garden card unlocked.

**No HP, no hints, no retries, no defeat, no fail screen, no difficulty tier.**

**Why this works as session climax:**
- Satisfies UNIFIED §6 requirement for a session culmination moment
- Triggers the "I made a real choice" feeling that Story Mode dialogue can't quite hit
- Generates the only sustained student writing in the session — used for §17 analytics + teacher summaries
- Tier 2 AI cost ~10–15¢ per session at scale (within $3–5/student/year budget)

**Tier escalation:** If student writes a particularly thoughtful 2+ sentence reflection, **Tier 3** is invoked once per session for a deeper personalized response. Hard-capped to control budget.

### §6.7 Phase 7 — O'ylab Ko'rish (Reflection) · 1–2 min · OPTIONAL

**Optional reflection. Skip is a valid path.** XP identical regardless.

**Three formats, student choice:**
1. **Voice** — record up to 30 sec
2. **Text** — write up to 2 sentences
3. **Draw** — quick sketch in app (touch input)
4. **Skip** — tap "Bugun yetarli" (Enough for today)

**Prompt rotation by today's mavzu** + general prompts:
- "Bugun qaysi fazilatni o'rgandik? Senga qanday yoqdi?"
- "Bu mavzu hayotingda qachon foydali bo'ladi?"
- "Bobongdan yoki onangdan bunday hikoya eshitganmisan?"

**Privacy:** student-only by default. Student can tap "Ulashish" (Share) to send to teacher's wall (moderated, opt-in). Never published without explicit student tap.

**No XP penalty for skipping. No streak penalty. No anything.**

---

## §7. Content Rules

### Narrative voice
- **Second-person ("Sen")** throughout — warm, partner-tone, never preachy
- **≤14 word sentences**, active voice, Lexile 830–1010L
- **Receptive vocab cap ~12k** — define new terms inline with visual + repetition (3+ exposures per term)
- **No idioms beyond G5 receptive range** — if used, gloss inline
- **Uzbek cultural names, places, foods, professions** as default frame; Russian/English code-switching only in §11 Additional Materials

### Emotional tone
- **Calm, warm, slow.** Never urgent, never breathless.
- **Affirming, never evaluative.** "Sening fikring qiziq" (Your thinking is interesting), not "To'g'ri javob" (Right answer)
- **Effort/strategy praise only.** "Yaxshi o'ylading" (You thought well), not "Sen aqlli" (You're smart)
- **Dweck growth-mindset language:** "Hali emas" (Not yet), never "Notog'ri" (Wrong)

### Visuals
- **Every concept has a visual.** Dual coding mandatory (Paivio 1986).
- **Mobile-first, 5" screen legible.** Min font 14px, labels 16px+.
- **≤800 ms animations.** Calm, never distracting.
- **Subject color: warm gold/honey `#F59E0B` primary + sage green `#84CC16` accent.** Distinct from Science purple, signals "warm + reflective" not "rigorous + scientific."
- **Dark mode** per universal UI/UX spec.

### Did You Know (loading/transitions)
- **Cultural/historical facts**, age-appropriate
- **One per phase transition**
- **Examples:** "Alisher Navoiy 30 dan ortiq kitob yozgan — birinchi kitobini 12 yoshida boshlagan"; "Ulug'bek Samarqandda dunyodagi eng katta osmon kuzatuv joyini qurgan"; "Ibn Sino tibbiyot bo'yicha kitobini Yevropada 600 yil davomida o'qitishgan"
- **Avoid:** anything scary, anything that implies family poverty, Western lifestyle comparisons, politics

---

## §8. Game Catalog Selections — Tarbiya G5

**Default Pool (16 mechanics from UNIFIED §6):**

| # | Mechanic | Tarbiya | Notes |
|---|---|---|---|
| 1 | Memory Sprint | **NO** | Replaced with Mood Check-in |
| 2 | Spaced Flashcards | YES | Used in 0-B Flash Cards only |
| 3 | Tile Match | YES (high) | Virtue cards, proverb halves |
| 4 | Sentence Fill | YES | Avloniy/Navoiy quote completion |
| 5 | Memory Palace | LIMITED | Bob IV heritage chapters only |
| 6 | Story Mode | **YES (highest)** | Branching, no wrong path |
| 7 | Adaptive Quiz | **NO** | Endless-test feeling, hostile to chill |
| 8 | Mystery Box | YES (high) | Uzbek cultural facts, virtue reveals |
| 9 | Movement Breaks | YES | Optional between phases |
| 10 | Why Chain | LIMITED | Max 2 levels, soft topics only |
| 11 | Peer Teaching | LIMITED (opt-in) | "Hikoyangizni ulashing" wall |
| 12 | Real-Life Challenge | **REPLACED** | Now "Sen bo'lsang?" no-fail |
| 13 | Reflection Journal | YES | Optional Phase 7 |
| 14 | Final Boss | **REPLACED** | Now "Big Decision" no-fail |
| 15 | Tic Tac Toe vs AI | YES | Recreational only, no values content |
| 16 | Notebook Capture | LIMITED (bonus) | Optional drawing tasks for reflective sketch |

**Interactive Catalog (12 mechanics):**

| Mechanic | Tarbiya | Use case |
|---|---|---|
| Connect Four vs AI | YES | Recreational |
| Codebreaker | YES | Decode proverbs |
| Memory Match Blitz | YES | Virtue/concept pairs |
| Reaction Chain | NO | Speed-based, wrong tone |
| Word Ladder | LIMITED | Vocabulary chains for value words |
| Puzzle Lock | NO | Wrong tone |
| Blackjack | NO | Gambling tone |
| Territory | NO | Competitive, wrong tone |
| Escape Room | LIMITED | Bob IV heritage chapters only |
| Bridge Builder | NO | Engineering, off-topic |
| Minefield | NO | Failure-state mechanic |
| **Tarbiya-specific: Garden Tend** | YES (new) | Tap-and-tend Virtue Garden between sessions |

**One Tarbiya-only mechanic introduced: "Garden Tend" (Bog' parvarishlash)** — between sessions, students can tap their Virtue Garden, water plants, see proverbs pop up. No XP, pure ambient interaction. ~30 sec optional.

---

## §9. Virtue Garden — Mechanic Spec

The **Fazilatlar Bog'i (Garden of Virtues)** is Tarbiya's signature meta-game and the primary engagement hook.

### Core loop
1. Each session unlocks **1 unique virtue card** in Phase 5
2. Card joins the persistent garden, plant grows visually
3. Garden has **4 zones** (one per Bob): Citizenship Oak Grove, Emotion Flower Meadow, Friendship Bridge Garden, Heritage Library Path
4. Each zone has **6–8 plant slots** corresponding to mavzular
5. Filling a zone unlocks a **zone-themed avatar accessory** (e.g., complete Bob II → unlock "warm scarf" cosmetic)
6. **24 virtue cards total** for Grade 5 (matches 24 sessions / 29 mavzular)

### Card design
Each virtue card has:
- **Front:** virtue name (Uzbek), visual icon, color-coded by Bob
- **Back:** 1-sentence definition, related proverb, link to today's story snippet, "Bobo Sherzod aytadi..." (NPC elder quote)

### Garden visual layers
- **Background:** Uzbek landscape (Chimgan mountains in distance, Registan dome silhouette)
- **Plants:** stylized, low-poly, grow over time (sapling → young plant → mature → blooming)
- **Ambient elements:** birds, butterflies, wind animation — peaceful
- **Tap-to-tend:** student can tap any plant to see proverb/quote (no XP, ambient delight)

### Progression
- **Cosmetic-only rewards** (avatar accessories, garden decorations)
- **No leaderboards, no comparison**
- **Sharable as screenshot** (optional, with student name/avatar)

### Why this works
- Variable-ratio reward schedule (which card unlocks next is partly surprising) without overjustification (cards aren't scored)
- Long-arc engagement (24 sessions to fill the garden = ~6 months of weekly Tarbiya)
- Pure intrinsic motivation: students return to *see their garden*, not *to win*
- Cultural anchoring in every visual element

---

## §10. Anti-Cheat Tuning (Tarbiya)

Tarbiya cheating is functionally meaningless. Anti-cheat focuses only on engagement quality.

| Signal | Tarbiya verdict |
|---|---|
| Speed anomaly (very fast) | **IGNORE** — kids tap fast on Tarbiya, expected |
| Length anomaly (very short reflection) | **IGNORE** — short is OK, skip is OK |
| Paste detection in Big Decision text | **MONITOR** — log only, never warn student. Teacher sees aggregate "X% of class pasted" |
| Vocabulary jump | **IGNORE** — irrelevant for values content |
| Mother helping detected | **WELCOMED** — explicit framing: "Mother is teaching alongside you. This is cooperation, not cheating." Teacher sees "collaborative session" tag, treated as positive. |
| Verdict ladder | **Capped at MONITOR** — never SOFT_WARNING, never TEACHER_ALERT for Tarbiya specifically |

Cultural framing reaffirmed: Uzbek mother-as-supervisor is collaborative scaffolding (universal NETS principle), but for Tarbiya it's actively encouraged because values are partially transmitted by family.

---

## §11. Cultural and Regional Anchors (Tarbiya-Specific)

### Names (rotate, ~10–12)
Aziza, Bekzod, Gulnara, Sardor, Malika, Jasur, Dilnoza, Otabek, Zarina, Anvar, Komila, Nigora

### Places
Tashkent, Samarkand, Bukhara, Khiva, Fergana, Pamir, Aral (environmental theme), Charvak, Chimgan, Registan, mahalla (neighborhood, used generically), Silk Road cities

### Historical figures (used as virtue exemplars)
- **Alisher Navoiy** — patriotism, language, intellectual courage (Bob I, IV)
- **Abdulla Avloniy** — moral integrity, education, perseverance (Bob II, IV)
- **Ulugh Beg** — curiosity, scholarship, Samarkand pride (Bob II, IV)
- **Ibn Sino (Avicenna)** — compassion in healing, intellectual humility (Bob II, III)
- **Abu Raykhan Beruni** — cross-cultural respect, observation, wonder (Bob I, IV)
- **Amir Temur** — leadership, vision, civic builder (Bob I, IV — used carefully, not as conqueror)
- **Bobur** — perseverance through hardship, literary achievement (Bob II, IV)
- **Namoz Jumayev** (modern) — environmental responsibility, civic action (Bob I)
- **Chingiz Aytmatov** (regional canon) — work ethic, literary culture (Bob II, IV)

### Modern Uzbek professions (used in scenarios)
Bog'bon (gardener), o'qituvchi (teacher), shifokor (doctor), muhandis (engineer), mahalla raisi (neighborhood elder), dehqon (farmer), hunarmand (craftsman), olim (scientist), shoir (poet), meteorolog, ekolog

### NPC characters (consistent across sessions)
- **Bobo Sherzod** — wise grandfather elder, recurring narrator/voice in Garden, family-bridge fallback when student has no living grandparent to interview
- **Buvi Saodat** — wise grandmother, alternating voice
- **Ustoz Komilov** — teacher figure for school-context scenarios

### Foods, plants, animals
Plov, non, somsa, choy, kovurma, chuchvara · cotton, mulberry, wheat, apricot, walnut · snow leopard, deer, sturgeon, cotton bollworm

### Currency
So'm (always)

### Things to avoid
- Western lifestyle comparisons (rural Uzbek students alienated)
- Pork, alcohol references
- Politics (Aral OK as environmental theme; political history avoided)
- Family poverty implications
- Explicit Quranic citations (cultural Islamic warmth implicit in mehr/hurmat/burch language is enough)
- Sectarian or doctrinal language

### Proverbs stock (rotate as Did You Know + Garden card backs)
- "Vatan tarkin bir nafas aylama..." (Navoiy)
- "Dangasalik har vaqt insonni xor qilur" (Avloniy)
- "Mehr bo'lmagan joyda yorug'lik bo'lmaydi" (folk)
- "Bir kun do'sting uchun, bir kun o'zing uchun" (folk)
- "Otaning aytgan gapi tilladek, onaning aytgani — kumushdek" (folk)
- (Curate ~30 proverbs total for the production pool)

---

## §12. Assessment, Scoring & Escalation

### Scoring philosophy
**There is no "score" in Tarbiya.** Engagement = success. Completion = pass.

| Engagement signal | Result |
|---|---|
| Session started + completed | XP awarded (flat ~50 XP base) |
| Big Decision attempted (any choice + 1-sentence why) | +25 XP bonus |
| Reflection (Phase 7) submitted in any format | +25 XP bonus |
| Family-bridge side quest completed | +30 XP bonus |
| Garden Tend (between-session ambient) | +5 XP per visit, max +15/day |
| 5-virtue combo unlocked | Cosmetic accessory (one-time) |
| Skip Phase 7 | No penalty, full XP |

### No reward labels
- No "Mukammal/A'lo/Juda yaxshi" (Excellent/Great/Good) labels — they imply ranking
- Replaced with: "Bugungi darsing tugadi. Fazilatlar bog'ing yana boyidi." (Today's lesson is done. Your Garden of Virtues has grown.)

### No Duolingo Mode
There's no "fail" → no remediation loop needed. If student seems disengaged for 3+ sessions in a row (Phase 1 mood = sad/tired, very short responses, no Reflection), **soft teacher flag** — teacher sees "Aziza may benefit from a check-in" with no detail beyond engagement-level.

### No teacher escalation for "wrong answers"
Because there are no wrong answers. Teacher dashboard for Tarbiya shows: completion rate, virtue garden progress per student, optional reflection submissions (only what student chose to share), aggregate class mood trends.

### Dual-pathway answer checking
- **Mood check-in, MC scenario choices, Tile Match, Sentence Fill** = Tier 1 algorithmic <100ms
- **Big Decision 1-sentence why** = Tier 2 generative response <5 sec, human fallback >10 sec
- **Reflection text** (when submitted) = Tier 2 sentiment analysis (private to student, not shown), no AI response unless student explicitly taps "Javob ber" (Respond)
- **Drawing reflection** = Tier 3 vision (optional, ≤10 sec, private)

---

## §13. AI Tier Strategy — Cost-Aware

Target: **stay within universal $3–5/student/year budget** despite Tarbiya's higher Tier 2 reliance.

| Phase | Tier | Notes |
|---|---|---|
| 0-A Theme Preview | Tier 2 | Personalized panel selection (Tier 1 fallback for cost) |
| 0-B Flash Cards | Tier 1 | Pre-generated card pool |
| Phase 1 Mood Check-in | Tier 1 | Pre-gen response bank |
| Phase 2 Story Mode | Tier 1 | Pre-gen branches; Tier 2 occasional adapted variants |
| Phase 3 Game Breaks | Tier 1 | Algorithmic |
| Phase 4 Sen Bo'lsang | Tier 2 | ~5 templated reactions per scenario, served algorithmically |
| Phase 5 Garden | Tier 1 | Pre-gen card art + animations |
| Phase 6 Big Decision | Tier 2 (Tier 3 once/session for thoughtful 2+ sentence) | Hard cap on Tier 3 use |
| Phase 7 Reflection | Tier 2 (only on explicit "respond" tap) | Default = no AI response |
| Notebook Capture (optional) | Tier 3 vision | Capped to 1 per session |
| Did You Know | Tier 2 | Curated pool, occasional fresh fact via Tier 2 |

**Cost estimate per session:** ~$0.04–0.06 (Big Decision Tier 2 = bulk of cost)
**Sessions per year per student:** ~24 (1/week × school year)
**Annual cost per student for Tarbiya:** ~$0.96–$1.44 — well within universal budget, leaves room for other subjects

---

## §14. Teacher Overrides

### Allowed (per session or per student)
- **Mode:** Standard (15–25 min) ↔ Extended (25–35 min, in-class, group reflection)
- **Phase 7 Reflection:** optional (default) ↔ required for in-class use
- **Family-bridge side quests:** show ↔ hide (for sensitive cohorts)
- **Big Decision sharing:** private ↔ moderated class wall opt-in
- **Mood check-in flags:** receive ↔ silent (some teachers prefer not to see)
- **Garden visibility:** student-only ↔ class garden mode (collective garden in class display)
- **Did You Know facts:** default pool ↔ teacher-curated subset

### Cannot override
- 7-phase structure (replaced phases retain structural slots)
- 0-A + 0-B mandatory
- Big Decision mandatory (cannot drop the climax)
- Stranger Test on narratives
- mr_level + sel_competency tag requirement
- Cultural framing (Uzbek-first)
- Banned mechanics list
- Doctrinally-neutral religious framing
- Cosmetic rewards never purchasable
- Reflection always optional for student (teacher cannot require it via the platform — only by classroom verbal instruction)

---

## §15. Tagging Schema

Every Tarbiya task is a JSON record with:

```json
{
  "task_id": "TAR-5-MEHR-S03-RLC-01",
  "subject": "Tarbiya",
  "grade": 5,
  "language": "uz",
  "textbook_ref": {
    "book": "Tarbiya 5-sinf (Quronov 2020)",
    "bob": 2,
    "mavzu": 10,
    "section_title": "Mehr qadri",
    "pages": "42-45"
  },
  "standard_ref": {
    "primary": "UZ-TAR-5-MEHR-01",
    "alias": "TAR.5.2.10.1"
  },
  "mr_level": "MR-L2",
  "sel_competency": "SoA",
  "pisa_secondary": {
    "reading_l1_l2": true,
    "creative_thinking": false
  },
  "transition_skill": "MR-L1→L2: take a virtue from a story and apply it to a familiar scenario",
  "blooms_level": "Apply",
  "phase": "Phase 4 — Sen Bo'lsang",
  "game_mechanic": "RLC (Tarbiya variant)",
  "ai_tier": 2,
  "estimated_time_sec": 90,
  "prompt_uz": "Mahallangizda yangi kelgan oila bor. Ular tilimizni bilmaydi. Sen nima qilasan?",
  "choices_uz": ["Salomlashishga boraman", "Ota-onamga aytaman", "O'qituvchimga aytaman", "Hech narsa qilmayman"],
  "expected_response_type": "choice + optional sentence",
  "evaluation_tier": "Tier 2 generative",
  "warm_response_templates": [
    "Salomlashishga borishing ularning yuragiga issiqlik beradi...",
    "Ota-onangga aytishing — ular kattalar bilan yaxshiroq yordam beradi...",
    "..."
  ],
  "cultural_anchors_used": ["mahalla", "Uzbek hospitality"],
  "garden_card_unlock": null,
  "scoring": "engagement_only"
}
```

Standard code structure: `UZ-TAR-5-{TOPIC}-{SEQ}` primary; `TAR.5.{BOB}.{MAVZU}.{SEQ}` alias.

---

## §16. Content Production Checklist

Per session (~24 sessions to cover 29 mavzular, some combined):

| Component | Volume per session |
|---|---|
| Theme Preview 8-panel deck | 8 panels |
| Flash Cards | 5–7 cards |
| Mood Check-in items | 1 (5 emoji + 1 soft recall) |
| Story Mode segments | 3 segments × 90 sec, 2–3 branches each → ~6–9 narrative variants |
| Game Breaks | 2 games (mechanic-specific content) |
| Sen Bo'lsang scenarios | 1 scenario, 3–4 choices, 5 templated AI responses |
| Garden virtue card | 1 unique card per session |
| Big Decision scenario | 1 scenario, 3 choices, 5–10 templated reflective AI responses |
| Reflection prompts | 3 (1 per accuracy bucket equivalent: engaged/quiet/shared) |
| Did You Know facts | 4–6 (one per phase transition) |
| Family-bridge side quest (opt-in) | 1 per session |
| All tagged with mr_level + sel_competency + transition_skill |  |

**Total per session: ~30–50 task units** (lower than Science 80–120 because each unit is denser)
**Total for full Grade 5: ~720–1,200 task units across 24 sessions**

Plus production pools:
- ~30 proverbs (rotated as Did You Know + Garden card backs)
- ~24 unique virtue cards (one per session)
- ~10–12 NPC dialogue trees (Bobo Sherzod, Buvi Saodat, Ustoz Komilov)
- ~6 garden zone visual states (sapling → blooming for each Bob)

---

## §17. Sample Session Walkthrough — Mavzu 10 "Mehr Qadri" (The Value of Mercy)

**Reference implementation. Match this shape for every session.**

### Metadata
- **Bob 2, Mavzu 10**, textbook pages 42–45
- **Standard:** UZ-TAR-5-MEHR-01 / TAR.5.2.10.1
- **Primary MR level:** MR-L2 (Apply)
- **SEL competency:** SoA (Social Awareness)
- **Transition skill:** "Recognize compassion in narrative → apply compassion concept to a familiar scenario"
- **Session length:** ~20 min
- **Garden card unlocked:** "Mehr" (Compassion) — joins Bob II Emotion Flower Meadow

### Pre-homework (3 min)

**0-A Theme Preview** (2 min, 8 panels):
1. *Sarlavha:* "Mehr qadri" + image of grandmother holding child's hand at Registan plaza
2. *Yaxshi tushuntirish:* "Mehr — bu boshqa odamning yuragini his qila olishdir. U ko'ylakdek issiq, qish kunidek zarur."
3. *Misollar:* 3 photos — onai choy beradi, do'st somsa ulashadi, sinfdosh kitob ko'taradi
4. *Hayotiy hikoya:* 3 sentences about Ibn Sino healing a poor patient in Bukhara without payment
5. *Senga taalluqli:* "Sen oxirgi marta kimga mehr ko'rsatganingni eslab ko'r."
6. *Nega muhim:* "Mehr bo'lmagan jamiyatda hech kim baxtli yashay olmaydi."
7. *Hayotda qo'llanilishi:* photos of nurse, teacher, mahalla volunteer
8. *Qo'shimcha:* Avloniy quote, optional 30-sec animated story

*Did You Know between panels 4–5:* "Ibn Sino tibbiyotga oid kitobini Yevropada 600 yil davomida o'qitishgan."

**0-B Flash Cards** (1 min, 5 cards):
- Mehr · Mehribonlik · Hurmat · G'amxo'rlik · Yordam (each with visual + 1-sentence definition + 1 proverb)

### Phase 1 — Mood Check-in (1 min)
- "Bugun qanday his qilyapsan?" — 5 emoji bar
- Soft recall: "O'tgan darsda qaysi fazilatni o'rgangan eding?" — 4 visual options (only Mavzu 9 was ostensibly "Bir-birimizni tushunish")
- Warm response based on mood selection

### Phase 2 — Hikoya Vaqti (6 min, 3 segments)

**Segment 1** (90 sec) — "Aziza maktabga ketayotgan edi. Yo'lda qariya qo'shnisi og'ir sumkalarni ko'tarib ketayotgan edi..." Choice: A) Yordam beraman, B) Salomlashib o'taman, C) Ko'rmaganga olaman. *All paths advance.*

**Segment 2** (90 sec) — Aziza chooses path A. "Qariya unga rahmat aytdi va onasining sirini aytdi: 'Mening onam ham yoshligimda menga shunday yordam bergan edi.'" Choice: A) Maqtanaman, B) O'ylab qolaman, C) Boshqa yo'l bilan ham yordam berishga harakat qilaman.

**Segment 3** (90 sec) — Story climax: Aziza arrives at school late. The teacher asks why. She tells the truth about helping. The teacher responds with quiet pride, not punishment. Choice: A) Sinfdoshlarga aytaman, B) O'zimga saqlayman, C) Onamga kechqurun aytaman.

*Stranger Test passed: Could a 10-year-old Uzbek girl finish this story and feel something? Yes.*

### Phase 3 — Game Breaks (4 min, 2 games)

**Game 1 — Tile Match Virtue Pairs** (2 min):
- 6 pairs: virtue word ↔ visual icon (mehr/heart, hurmat/bowing, yordam/helping hand, etc.)
- Engagement-XP only

**Game 2 — Sentence Fill (Avloniy quote)** (2 min):
- "____ bo'lmagan joyda yorug'lik bo'lmaydi." (mehr)
- "Dangasalik har vaqt insonni ____ qilur." (xor)
- 4 quotes total, word bank provided

### Phase 4 — Sen Bo'lsang? (4 min, 1 scenario)

**Scenario:** "Sinfingizda yangi o'quvchi keldi. U boshqa shahardan kelgan va hali hech kim bilan tanish emas. Sen nima qilasan?"

**4 choices:**
1. Birinchi o'zim salomlashaman → Tier 2 response: "Bu juda jasur va mehrli qaror. U sening salomlashganingni umrbod eslab qoladi..."
2. Do'stlarim bilan birga uni davraga qo'shamiz → "Guruh bo'lib mehr ko'rsatish kuchli ta'sir qiladi..."
3. O'qituvchimga aytaman → "Bu ham yaxshi yo'l. Kattalar yordami bilan u yengilroq moslashadi..."
4. O'zi tanishib oladi → "Ba'zilar shunday o'ylaydi. Ammo ba'zida yangi kelgan odamga birinchi qadam og'ir bo'ladi..."

Student picks one. Sees their response. Optional: tap "Boshqa javoblar" to see all four. Optional: thumbs up/down. No scoring.

### Phase 5 — Fazilatlar Bog'i (2 min)

- Brief animation (4 sec): "Mehr" virtue card unlocks
- Card art: warm glowing heart with Uzbek pattern border, gold/honey color
- Card back: Definition + Avloniy proverb + Bobo Sherzod quote
- Garden zoom-in: "Mehr" plant appears in Bob II Emotion Flower Meadow as a small bloom
- Tap-to-explore garden (optional, no XP)

### Phase 6 — Katta Qaror (4 min)

**Setup:** "Tasavvur qil: Sen 13 yoshdasan. Sening eng yaqin do'sting Bekzod yangi telefon olibdi va hammaga maqtanyapti. Lekin sen bilasanki, uning ota-onasi ko'p ishlaydi va bu telefonni olishi uchun ko'p qiyinchilik chekkan. Bekzod boshqa do'stlaringga 'mening telefonim sizlarnikidan yaxshiroq' deyapti. Sen do'stingnisan, lekin u yomon ish qilyapti..."

**3 choices:**
1. **Bekzodga to'g'ridan-to'g'ri aytaman** — "Bu mehr ko'rsatishning bir shakli. To'g'ridan-to'g'ri gapirish do'stning haqiqiy haqi..."
2. **Boshqa do'stlarga uning ahvolini tushuntiraman** — "Sen ularning his-tuyg'ularini himoya qilishni istaysan. Bu ham mehr..."
3. **Hech narsa qilmayman, vaqt o'tadi** — "Ba'zida shunday qilishingiz mumkin. Ammo o'ylab ko'r — agar do'stingga oyna ushlab tursang, u o'zini ko'radi..."

**Student writes 1 sentence: "Nega bu javobni tanlading?"**

Tier 2 generates a warm reflective response based on what the student wrote, exploring their reasoning further. Always passes. XP awarded.

### Phase 7 — O'ylab Ko'rish (1–2 min, optional)

**Prompt:** "Bugun qaysi fazilatni o'rgandik? Senga qanday yoqdi?"

Student can:
- Voice (30 sec)
- Text (2 sentences)
- Draw
- Skip ("Bugun yetarli")

All paths give same XP. If submitted, optional "Ulashish" tap to send to teacher wall.

### Post-session
- Total XP: ~125 (50 base + 25 Big Decision + 25 Reflection + 25 garden combo if applicable)
- Garden updated
- Mood logged (private)
- Teacher dashboard: "Aziza completed Mavzu 10 — engaged, shared reflection"
- Did You Know facts shown: 4 total across phase transitions

---

## §18. Open Questions / Things to Validate

1. **Garden Tend persistence cost** — does between-session ambient mechanic add server load? Need engineering review.
2. **Big Decision Tier 3 cap** — 1-per-session sufficient, or do we need stricter limits to control budget?
3. **Mood flag escalation threshold** — 3 consecutive "sad/tired" → soft teacher flag is the proposed default, but cultural validation needed (does Uzbek teacher culture welcome or resist this?)
4. **Garden zone unlocks** — do we want students to see other students' gardens in opt-in class mode? Validate with teachers.
5. **Bobo Sherzod NPC voice** — does it need voice actor recording or text-only? Voice is warmer but expensive.
6. **Big Decision content sourcing** — 24 dilemmas needed; some can be derived from textbook scenarios, others must be original. Who writes them?
7. **Family-bridge opt-out detection** — how does the system detect a student should be offered NPC fallback automatically vs. opt-in toggle?
8. **Religious framing edge cases** — what if a student writes a Quranic-style reflection? Affirm warmly without echoing doctrine?
9. **MR-L4 task feasibility at G5** — psychology says construction-level is hard for 10-year-olds. Cap MR-L4 at 5% of session content; validate after pilot.
10. **Sharing wall moderation** — who moderates Hikoyangizni ulashing? Teacher? AI pre-screen + teacher approve? Define moderation pipeline.
11. **Tarbiya in Russian-language schools** — sibling framework needed for Tarbiya 5-sinf Russian edition; flag for next phase.
12. **Class Garden mode logistics** — single shared garden for class? Or class wall of individual gardens? Validate with teachers.

---

## §19. Production Handoff

### Contract for content team

Build Tarbiya G5 content matching the **§17 walkthrough shape exactly**. For each of ~24 sessions:

1. **Source from textbook** — every task traces to a Bob/Mavzu/page range
2. **Apply §4 psychology parameters** — 15–25 min, calm pacing, no failure states, warm tone
3. **Use §11 cultural anchors** — rotate names/places/figures, no Western anchors
4. **Tag every task** per §15 schema (mr_level, sel_competency, transition_skill, textbook_ref)
5. **Pass Stranger Test** on every Story segment + Big Decision scenario
6. **Pre-generate Big Decision warm response banks** — 5–10 templates per scenario
7. **Author Garden card art** — 24 unique virtue cards (one per session)
8. **Curate Did You Know pool** — ~60 facts (4–6 per session × 24 sessions, with overlap allowed)
9. **Author NPC voices** — Bobo Sherzod, Buvi Saodat, Ustoz Komilov consistent across all sessions
10. **Validate against §18 open questions** before production locks

### Quality gates
- **Pedagogy review** by 1 pedagogy lead + 1 G5 Uzbek classroom teacher
- **Language review** by Uzbek native speaker (Lexile + cultural authenticity)
- **Pilot in 2 classrooms** (1 urban Tashkent, 1 rural Fergana valley) before full rollout
- **Mood-flag false positive review** — engineering monitors first 4 weeks

### Timeline
- Research phase complete (this doc): ~ done
- Content authoring (24 sessions): ~10–12 weeks
- Pilot + validation: ~4 weeks
- Full rollout: ~ pilot + 4 weeks

---

## §20. Versioning and Review

- **Version 1.0** — 2026-04-08, Tarbiya G5 first framework, "Chill Mode" design
- **Reviewers needed:**
  - Product/pedagogy lead (Claude/orchestrator)
  - Uzbek G5 Tarbiya teacher (1–2)
  - Curriculum specialist (Tarbiya domain)
  - Content lead
- **Next revision** after first 5 sessions stress-tested in pilot
- **Sibling frameworks to create after this:**
  - Tarbiya G5 Russian edition (sibling)
  - Tarbiya G6, G7 (next grades, same chill-mode shape)
  - Apply chill-mode learnings to other reflective subjects (e.g., Native Language literature units)

---

**End of NETS Tarbiya G5 Framework v1.0.**

*Companion docs:* `NETS-Homework-Engine-UNIFIED.md` (universal WHAT) · `NETS-Homework-Engine-Blueprint.docx` (universal HOW) · `NETS-UI-UX-Design-Spec.docx` (universal LOOK) · `Researches/qwen-grade5-psychology-findings.md` (G5 psychology base) · `Book & Resourses/_tarbiya_extracted.txt` (textbook source) · `Book & Resourses/Tarbiya_5_uzb_2020_www.idum.uz.pdf` (textbook PDF)
