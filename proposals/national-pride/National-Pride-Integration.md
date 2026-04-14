# National Pride Module — Integration Analysis into NETS Homework Engine

The proposal introduces a "Milliy G'urur va Taraqqiyot" (National Pride & Progress) system that injects Uzbek national pride content and global wisdom into homework sessions. This analysis shows what fits, what doesn't, and what needs adjustment — mapped against the UNIFIED spec.

---

## What the Proposal Contains

5 components:
1. **55/45 Rule** — 55% National / 45% Global content ratio for all injected content
2. **70/30 Rule** — 70% Facts ("Bilarmidingiz?") / 30% Quotes ("Hikmatlar") at XP milestones
3. **"Wise Status" Role Injection** — Students addressed as professionals ("Bosh Muhandis," "Strategik Tahlilchi") in Phase 4
4. **Phase-by-Phase Trigger Map** — Where to inject national/global content across the session
5. **Data Assets** — 4,800+ quotes/facts in a structured JSON database

---

## Component-by-Component Analysis

### 1. The 55/45 National/Global Ratio

- **What:** All injected content maintains 55% Uzbekistan / 45% Global balance.
- **Why it's good:** Prevents "cringe glazing" (100% national) or cultural disconnection (100% global). Students see their country as part of the world, not separate from it.
- **Why it fits NETS:** The UNIFIED spec already mandates "Uzbek cultural context" for Phase 4 Real-Life Challenges and Story Mode narratives. This formalizes the ratio instead of leaving it to content author discretion.
- **How to implement:** Tag every quote/fact in `quotes_database.json` with `origin: "National"` or `origin: "Global"` (already done). Selection algorithm enforces 55/45 over a rolling 10-item window. Individual sessions may deviate, but any 10 consecutive injections must stay within 50-60% national.
- **Where Not:** Phase 1 (Memory Sprint) and Phase 3 (Game Breaks) — the proposal correctly says 0% injection here. These are high-speed academic phases. Injecting pride content would break flow and dilute the learning objective. Phase 6 (Boss) — assessment is subject-pure, no injection.

**Verdict: FITS. Adopt as-is.**

---

### 2. The 70/30 Facts/Quotes Ratio

- **What:** Between-phase content is 70% "Bilarmidingiz?" facts and 30% "Hikmatlar" wisdom quotes.
- **Why it's good:** Facts trigger curiosity (cognitive engagement). Quotes trigger reflection (emotional engagement). 70/30 leans toward curiosity because that's what drives PISA performance — students who are curious learn faster.
- **Why it fits NETS:** The UNIFIED spec §6.5 already defines **"Did You Know..." loading screen insights** between phases. The proposal's facts ARE these loading screen insights. They're already supposed to exist — the proposal just provides the data and the national/global balance.
- **How to implement:** Merge `quotes_database.json` into the "Did You Know..." content pool (§6.5). Each transition between phases draws one item from the pool, respecting 70/30 type balance and 55/45 origin balance.
- **Adjustment needed:** The proposal says facts play at "XP milestones (30% and 60% session progress)." The UNIFIED spec says insights play at EVERY phase transition. Go with UNIFIED — every transition is better. More touchpoints = more exposure without adding session time.
- **Where Not:** Inside phases (during active learning). Between-phase ONLY. Never interrupt a Game Break or Story Mode segment with a fact/quote.

**Verdict: FITS. Merge into existing §6.5 "Did You Know..." system. Use every-transition frequency, not milestone-only.**

---

### 3. "Wise Status" Role Injection (Phase 4)

- **What:** In Phase 4 Real-Life Challenge, the student is addressed with a high-status professional title ("Bosh Muhandis," "Strategik Tahlilchi," "Laboratoriya Rahbari") and the problem is anchored in a real Uzbek or global context.
- **Why it's good:** This is ALREADY what Phase 4 does. The UNIFIED spec §5.4 mandates: "Student is positioned as an expert — fire safety inspector, scientist, engineer, consultant." The proposal adds two things the UNIFIED spec doesn't have: (a) the heritage hook connecting the role to an Uzbek ancestor/achievement, and (b) the closing line connecting the student's work to national progress.
- **Why it fits NETS:** Phase 4 already puts students in expert roles. The heritage hook and closing line add emotional resonance without changing the academic task. "Calculate P(A) = 3/10" is the same math whether the context is abstract or anchored in "IT-Park rezidentlari."
- **How to implement:** 
  - Use `task_injections.json` as the source for role/hook/closing templates per subject group
  - For 30% of Phase 4 tasks (not 100% — the proposal says 30%), apply the "Wise Status" baking recipe: Status → Arena → Bridge → Closing
  - The academic core (formula, calculation, reasoning) is UNTOUCHED — only the framing changes
  - 55/45 rule applies: 55% of Wise Status tasks use national arena, 45% use global arena
- **Adjustment needed:** The proposal says 20% of ALL homework tasks get national injection ("every 5th task"). This is too aggressive — it would inject pride content into Memory Sprint, Game Breaks, and Boss questions where it doesn't belong. **Limit to Phase 4 only, at 30% of Phase 4 tasks.** The other phases get pride content through between-phase facts/quotes, not inside tasks.
- **Where Not:** Phase 1 (2-minute warm-up, no time for role framing). Phase 3 (Game Breaks — games have their own engagement, adding role framing adds cognitive overhead). Phase 6 (Boss — pure assessment, no framing). Phase 5 (Consolidation — mnemonics, not role-play).

**Verdict: FITS for Phase 4 at 30%. Do NOT apply the 20% "every 5th task" rule across all phases — that violates the "No Busywork" rule (§1.3) by adding non-PISA content to academic phases.**

---

### 4. Phase 0-A Gate Quote

- **What:** Phase 0-A (Theme Preview) opens with a mandatory inspirational quote. 5-second skip lock — student must read it before proceeding.
- **Why it's partially good:** Starting with a mindset-setting quote aligns with BOST's "Prime" step. A well-chosen quote related to the topic can activate schemas. Example: Before a math lesson, showing al-Xorazmiy's "Tartib va mantiq — ilmning poydevoridir" sets the right mental frame.
- **Problem — 5-second skip lock:** The UNIFIED spec §4.4 explicitly says Theme Preview is "student-paced, no timer pressure." A 5-second forced lock contradicts this. Students who are eager to start will find the lock frustrating. Students who need more time will feel rushed. The lock is a UX anti-pattern.
- **Adjustment needed:** Show the quote but make it dismissable immediately (tap to continue). The quote is valuable — the lock is not. Students who want to read it will. Students who don't want to are not going to absorb a quote they're forced to stare at for 5 seconds.
- **How to implement:** Add a `gate_quote` component to Phase 0-A, positioned before Panel 1. Pulls from `quotes_database.json` (type: "quote", filtered by subject relevance if tagged). No timer lock. Dismissable.
- **Subject relevance:** If the quote is topic-relevant (al-Xorazmiy for Math, Ibn Sino for Science, Navoiy for Literature), it adds value. If it's generic ("Ilm — kuch"), it's filler. Content authors should tag quotes with subject relevance.
- **Where Not:** Recovery Sessions (15-20 min, no time for a gate quote). Sessions where the student is retrying after Boss failure (they need to jump back in, not read quotes).

**Verdict: FITS without the 5-second lock. Show quote, make dismissable. Tag quotes by subject for relevance.**

---

### 5. Phase 2 Story Mode — Ambient Setting

- **What:** Story Mode narratives are set in Uzbek or global hubs (55/45 ratio).
- **Why it fits:** The UNIFIED spec §5.2 already has a Grade-Level Narrative Framework with Uzbek cultural settings (Samarkand, Silk Road, Registan, Tashkent, etc.). The proposal formalizes the balance — 55% stories set in Uzbekistan, 45% in global contexts.
- **How to implement:** Content pipeline already produces narratives in Uzbek cultural contexts. Add a `setting_origin: "national" | "global"` tag to each `narrative_segment`. The session assembler ensures the rolling average stays near 55/45 across sessions (not per-session — a single session can be 100% national if the textbook topic is Uzbek history).
- **Where Not:** Don't force global settings on inherently Uzbek topics (Uzbek Literature, Uzbek History). Don't force national settings on inherently global topics (World History, English Language). The 55/45 balance is a GUIDELINE across the year, not a per-session mandate.

**Verdict: FITS. Formalize as a content pipeline tag with rolling balance across sessions.**

---

### 6. Phase 7 Reflection — Connection to Future Contribution

- **What:** Phase 7 reflection closes with a metacognitive prompt connecting today's learning to future contribution ("Your knowledge builds the Third Renaissance").
- **Why it fits:** Phase 7 already has TEFCAS-framed reflection prompts + BOST goal recall. Adding a closing line connecting knowledge to purpose (national or global) reinforces intrinsic motivation — the student learns not for XP but for something bigger.
- **How to implement:** After the TEFCAS reflection prompts and BOST goal recall, add one closing line. 55/45 ratio: "Sizning bilimingiz Uchinchi Renessansning poydevoridir" (national) or "Sizning aniq fikrlashingiz global standartlarga mos keladi" (global). Template-based, Tier 1.
- **Where Not:** Low-performance sessions (< 60%). When a student is struggling, a closing line about "building the Third Renaissance" feels tone-deaf. Use a gentler framing: "Har bir urinish miyangizni kuchaytiryapti" (Every attempt strengthens your brain) — which is TEFCAS, not pride content.

**Verdict: FITS for high-performance sessions (≥ 60%). Skip or soften for struggling students.**

---

## Components that DON'T Fit

### The 5-Second Skip Lock (UI)
- **Why not:** Contradicts UNIFIED §4.4 "student-paced, no timer pressure." Forced attention doesn't create genuine engagement — it creates resentment. Remove the lock, keep the quote.

### The 20% All-Task Injection Rule
- **Why not:** Injecting national pride into 20% of ALL homework tasks (across all phases) violates the "No Busywork" rule (§1.3). Every task must scaffold ONE specific PISA transition skill. A Memory Sprint question with "Siz IT-Park Bosh muhandisisiz..." framing adds 15 words of non-PISA content to a 2-minute warm-up. Limit to Phase 4 at 30%.

### Phase 6 "Certification" Framing
- **Why not:** The proposal says Phase 6 Boss should feel like a "professional certification." But the Boss already has its own identity — HP system, 3-tier bosses (Sub/Big/Mythical), Socratic failure flow. Adding "certification" language conflicts with the game metaphor (you don't "certify" against a boss — you defeat it). The Boss framing is strong as-is. Don't dilute it.

### Dark Mode (#0a0a0a) as Mandatory
- **Why not:** The UNIFIED UI/UX spec already handles theming. Dark mode is a user preference, not a national pride feature. Don't tie visual design to this module.

---

## Data Asset Quality Check

| Asset | Items | Quality | Issue |
|---|---|---|---|
| `quotes_database.json` | 4,800+ | Good structure (type, author, text, category, origin, id) | `category: "General"` on most items — needs subject-specific tags (Math, Science, History, etc.) for relevant matching |
| `Milliy_hikmatlar.md` | 248 lines | Rich — Mirziyoyev, Karimov, Temur, Navoiy, Ibn Sino, Beruni, Xorazmiy, Farobiy, Ulugbek, Babur, Behbudi, Qodiriy, Cho'lpon, Tomiris, Manguberdi | Some quotes are very political (Karimov, Mirziyoyev) — may need sensitivity review for classroom context |
| `Jahon_hikmatlari.md` | 123 lines | Good range — Buzan, Einstein, Jobs, Mandela, Ford, Curie, Gandhi, da Vinci, Adam Smith, Buffett | Buzan quotes already in the system — avoid duplication with Buzan injection |
| `Bilarmidingiz_faktlar.md` | 51 lines (template) | Shows first 40 of planned 300 | Needs completion — only 40/300 national facts written. Global facts section is placeholder ("davom etadi") |
| `task_injections.json` | 5 items | Good templates but only 5 subject groups covered | Needs expansion — 5 templates for ~15 subjects is insufficient |

---

## Final Integration Map

| NETS Phase | National Pride Injection | Source | Frequency |
|---|---|---|---|
| **0-A: Theme Preview** | Topic-relevant quote (dismissable, no lock) | `quotes_database.json` (type: quote, subject-tagged) | 1 per session |
| **0-B: Flash Cards** | None | — | — |
| **1: Memory Sprint** | None (high-speed recall, no injection) | — | — |
| **Transitions (between any phases)** | "Bilarmidingiz?" fact or "Hikmatlar" quote (70/30, 55/45) | `quotes_database.json` | 1 per transition |
| **2: Story Mode** | Ambient setting tagged national/global (55/45 rolling) | Content pipeline (narrative_segment.setting_origin) | Per story |
| **3: Game Breaks** | None (game mechanics own the engagement) | — | — |
| **4: Real-Life Challenge** | "Wise Status" role + heritage hook + closing (30% of tasks) | `task_injections.json` | ~1 in 3 sessions |
| **5: Consolidation** | Heritage anchor in mnemonic link sentences (natural, not forced) | Content pipeline | When organically relevant |
| **6: Final Boss** | None (pure assessment) | — | — |
| **7: Reflection** | Closing line connecting learning to contribution (≥60% sessions only) | Template (55/45 national/global) | 1 per session |

---

## What Needs to Happen Before Implementation

1. **Complete the facts database** — only 40/300 national facts written, global facts are placeholder
2. **Subject-tag all quotes** — current `category: "General"` is useless for relevant matching. Every quote needs a subject tag (Math, Science, History, Language, etc.)
3. **Expand task_injections.json** — 5 templates for ~15 subjects. Need at least 3 per subject = ~45 templates
4. **Sensitivity review** — political quotes (Karimov, Mirziyoyev) may need review for classroom appropriateness. Educational wisdom is fine; political slogans may not be
5. **Remove Buzan duplicate quotes** — Jahon_hikmatlari.md has 10 Buzan quotes. These overlap with the Buzan injection module. Use them in the pride module OR the Buzan module, not both
6. **Remove 5-second skip lock** from the spec — contradicts UNIFIED's student-paced rule
7. **Remove 20% all-task injection** — replace with Phase 4 only at 30%
