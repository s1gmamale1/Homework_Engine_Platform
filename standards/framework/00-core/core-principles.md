---
name: core-principles
status: v0.1 draft — validated against §22 only
layer: 0 (core primitive)
source: UNIFIED-Buzan §1 (lines 41-194)
---

# Core Principles and Philosophy

## Content

### 1.1 The NETS Learning Pyramid

Every homework session MUST map to Bloom's Taxonomy through the NETS Learning Pyramid:

```
                    +-------------+
                    |  TRANSFER   | <-- Real-Life Challenges (PISA Level 5-6)
                   +---------------+
                  |    ANALYZE     | <-- Why Chain, Mystery Box (PISA Level 4)
                 +------------------+
                |      APPLY        | <-- Adaptive Quiz, Final Boss (PISA Level 3)
               +--------------------+
              |     UNDERSTAND       | <-- Story Mode, Tile Match (PISA Level 2)
             +------------------------+
            |       REMEMBER          | <-- Memory Sprint, Flashcards (PISA Level 1)
           +--------------------------+
           |     ENGAGE (Foundation)   | <-- Gamification, Flow State
           +---------------------------+
```

**NON-NEGOTIABLE:** Every homework session MUST include activities spanning at least 4 levels of the pyramid.

---

### 1.2 The 3 Sacred Principles

#### Principle 1: Textbook is Source of Truth, NETS is the Transformer

| What Textbook Does | What NETS Does |
|---|---|
| Provides core concepts | Forces REASONING with concepts |
| Presents information | Creates active engagement |
| Shows solved examples | Requires student to CONSTRUCT solutions |

**STANDARD:** Homework MUST NOT change core concepts from textbooks. It MUST adapt delivery method to active, gamified, AI-personalized learning.

*Source: Both specs agreed. Textbook analysis of Grade 5 Math (2024 RU edition) confirmed CPA progression already present in textbooks, making NETS integration natural.*

#### Principle 2: Flow State is Mandatory

Based on Csikszentmihalyi (1990), every student MUST be maintained in the flow channel:

```
Challenge Level
    |         ANXIETY (Overwhelmed - Student Quits)
    |              /
    |            /
    |          /  +===========+
    |        /    | FLOW      | <-- TARGET ZONE
    |      /      | 70-80%    |
    |    /        | Success   |
    |  /          +===========+
    |/___________________________
    |    SKILL Level    \
    |                     \
    |                       BOREDOM (Underwhelmed - Student Quits)
```

**STANDARD:** AI MUST adjust difficulty every 3-5 questions:
- Below 60% success rate --> Reduce difficulty by 1 tier
- Above 90% success rate --> Increase difficulty by 1 tier
- 70-80% success rate --> Maintain current tier

*Source: HOMEWORK_STANDARDS.md. Chosen over the original spec's "3 consecutive correct/2 consecutive wrong" rule because percentage-based thresholds are more robust against variance.*

#### Principle 3: Intrinsic Motivation > Extrinsic Rewards

All rewards MUST celebrate LEARNING PROGRESS, not compliance.

| DO (Intrinsic) | DON'T (Extrinsic) |
|---|---|
| "You mastered fractions!" | "You logged in 7 days!" |
| "Your reasoning improved!" | "You clicked 100 times!" |
| "You helped a classmate!" | "You watched an ad!" |

**STANDARD:** Zero pay-to-win mechanics. Zero real-money purchases. Every reward is earned through demonstrated learning.

*Source: HOMEWORK_STANDARDS.md Principle 3. Critical design constraint — the gamification economy (Section 11) must comply.*

---

### 1.3 The "No Busywork" Rule

**Every task must explicitly scaffold ONE specific PISA transition skill.** No filler questions. No repetition without purpose. If a task cannot be tagged to a transition skill, it does not enter the content pool.

*Source: HOMEWORK_TASK_ENGINE.md. This is the single most important design constraint for content creators.*

---

### 1.4 Teaching Methodology — Universal Principles

Two principles that apply to ALL families, ALL phases, ALL subjects:

#### A. Two-layer explanation (formal + simplified)
Every complex concept gets TWO presentations:
- **Layer 1:** Formal, accurate, complete. Uses correct terminology and notation for the subject.
- **Layer 2:** "In plain words" (Sodda so'zlar). Everyday language re-explanation using concrete metaphors. Not a summary — a RE-EXPLANATION of what Layer 1 said.
Both layers present for technical content in Panels 1-4 of Preview. Layer 1 teaches; Layer 2 locks.

#### B. Don't assume — explain
Never assume the student knows why a step, rule, or concept is valid. If a student could reasonably ask "why?" or "where did that come from?", the content must answer proactively.

**Family-specific teaching methods live in family adapters (`02-families/`), NOT here.** Each subject family has its own pedagogical approach:
- **Aniq Fanlar + Tabiy Fanlar:** Genetic method (origin journey), no-magic-moves (show every derivation), derivation transparency. See `02-families/family-aniq-fanlar.md` §Teaching Methodology.
- **Til Fanlar:** Immersion-first (Krashen i+1), pattern through exposure, contextual vocabulary, SkyEng narrative model. See `02-families/family-til-fanlar.md`.
- **Ijtimoiy Fanlar:** Narrative IS content, primary source analysis, causal chain building, multiple perspectives. See `02-families/family-ijtimoiy-fanlar.md`.

*Source: §22 session. Universal principles validated across all families. Family-specific methods validated against §22 (Math) only — Language and History methods are proposals pending first lesson builds.*

---

### 1.5 Buzan Cognitive Foundation

The NETS 7-phase structure is built on Tony Buzan's research into how the brain learns. Two frameworks underpin the session design:

**TEFCAS — The Learning Loop.** Every NETS session is a TEFCAS cycle: Trial (Phase 3 — student attempts problems) → Event (outcome) → Feedback (immediate per-item feedback) → Check (IRT engine recalculates proficiency) → Adjust (difficulty adapts + Phase 5 targets weak areas) → Success (Phase 6 Boss defeat). This is not a new addition — it is the *naming* of what the engine already does. The AI tutor uses TEFCAS vocabulary: failures are "Feedback," not errors. The system-wide maxim: **"There is no such thing as failure, only feedback."**

**The MIG — Why 7 Phases Exist.** Buzan's "Most Important Graph" describes recall during a session:
- **Primacy Effect** → Phase 1 (Memory Sprint) places key items first, when recall is highest
- **Recency Effect** → Phase 7 (Reflection) ensures the last mental act consolidates learning
- **Association Effect** → Phase 0-A/0-B activate prior schemas so new content anchors to existing knowledge
- **Von Restorff Effect** → Phase 3 (Game Breaks) mid-session anchor provides a memorable, outstanding moment
- **The Sag** → Game Breaks split the session into sub-sessions, resetting the Primacy/Recency curve multiple times

**BOST — The Study Technique the Engine Models.** The Buzan Organic Study Technique maps onto NETS: Browse (Phase 0-A Theme Preview) → Time/Amount (session timer) → Prime what you know (Phase 0-A "What do you already know?" prompt) → Questions/Goals (Phase 0-A "What do you want to learn?") → Overview (Phase 0-B Flash Cards) → Preview/Inview (Phase 2-3 Story + Games) → Review (Phase 5+7 Consolidation + Reflection).

**Where Buzan does NOT apply:** Buzan methods are delivery mechanisms — the HOW, never the WHAT. They never alter textbook content, curriculum standards, or PISA calibration. Sections 2 (Content Architecture), 3 (PISA Framework), 11 (Gamification Economy), 14 (Teacher Controls), and 15 (Integration Points) are unchanged by Buzan injection.

---

### 1.5 National Pride & Progress Module ("Milliy G'urur va Taraqqiyot")

The NETS engine embeds Uzbek national pride and global wisdom into homework sessions. This is NOT patriotic decoration — it connects learning to purpose ("Your knowledge builds something real") and positions Uzbekistan as part of the world, not separate from it.

**Two Ratios Govern All Injected Content:**

| Rule | Ratio | What It Means |
|---|---|---|
| **The Origin Balance** | **55% National / 45% Global** | Over any rolling 10-item window, ~55% of injected facts/quotes/settings reference Uzbekistan; ~45% reference global science, figures, or events. Individual sessions may deviate. |
| **The Type Balance** | **70% Facts / 30% Quotes** | Between-phase content is 70% "Bilarmidingiz?" curiosity facts and 30% "Hikmatlar" wisdom quotes. Facts trigger cognitive engagement; quotes trigger emotional reflection. |

**Where National Pride Content Appears:**

| Phase | What Gets Injected | How | Frequency |
|---|---|---|---|
| **0-A: Theme Preview** | Topic-relevant wisdom quote with 5-second skip lock | Gate quote before Panel 1. Pulled from `quotes_database.json`, subject-tagged. "Davom etish" (Continue) button disabled for 5 seconds with visible countdown. | 1 per session |
| **Transitions (between phases)** | "Bilarmidingiz?" fact or "Hikmatlar" quote | Merges into existing §6.5 "Did You Know..." loading screen insights. 70/30 type balance, 55/45 origin balance. | 1 per transition |
| **2: Story Mode** | Ambient setting tagged national or global | Narrative segments tagged `setting_origin: "national" | "global"`. Rolling 55/45 balance across sessions (not per-session — a single session about Uzbek History can be 100% national). | Per story |
| **4: Real-Life Challenge** | "Wise Status" role + heritage hook + closing | For 30% of Phase 4 tasks: student gets a professional title ("Bosh Muhandis," "Strategik Tahlilchi"), problem anchored in Uzbek or global achievement, closing connects to national/global progress. Academic core UNTOUCHED. | ~1 in 3 sessions |
| **5: Consolidation** | Heritage anchor in mnemonic link sentences | When organically relevant — e.g., Peg System link sentence: "Mirzo Ulug'bek yulduzlarni sanagan — siz ham shu aniqlikda hisoblang." Not forced. | When natural |
| **7: Reflection** | Closing line connecting learning to contribution | After TEFCAS prompts and BOST goal recall: "Sizning bilimingiz Uchinchi Renessansning poydevoridir" (national) or "Sizning aniq fikrlashingiz global standartlarga mos keladi" (global). | 1 per session (≥60% accuracy only) |

**Where National Pride Content Does NOT Appear:**

| Phase | Why Not |
|---|---|
| **0-B: Flash Cards** | Pure reference. No emotional framing. |
| **1: Memory Sprint** | 2-minute high-speed recall. Adding role framing wastes precious seconds. |
| **3: Game Breaks** | Game mechanics own the engagement. Pride framing adds cognitive overhead to games designed for flow. |
| **6: Final Boss** | Pure PISA assessment gate. No framing, no injection, no heritage hooks. The Boss tests demonstrated competence — adding pride content would dilute assessment validity. |

**"Wise Status" Recipe (Phase 4 only, 30% of tasks):**

1. **Assign Status:** Professional title, not praise. "Siz Bosh Muhandissiz" (You are the Chief Engineer), not "Siz juda aqllisiz" (You are very smart).
2. **Set the Arena:** National (55%): anchor in a real Uzbek achievement (Afrosiyob, IT-Park, Ulug'bek Observatory). Global (45%): anchor in a global standard (CERN, NASA, WHO).
3. **Bridge:** Connect the textbook question to the arena. The academic core (formula, calculation, reasoning) is UNTOUCHED.
4. **Closing:** "Sizning aniqligingiz Uchinchi Renessansni quradi" (national) or "Sizning natijangiz global standartlarga mos" (global).

**Additional Rules from National Pride Proposal:**

| Rule | Implementation |
|---|---|
| **5-second skip lock on Phase 0-A quote** | The gate quote in Phase 0-A has a 5-second countdown timer. The "Davom etish" (Continue) button is disabled until the timer expires. This ensures students read the mindset-setting quote before proceeding. |
| **20% all-task injection** | Every 5th homework task across Phases 1, 2, 4, 5, and 7 gets national pride framing — professional title + heritage/global context anchor. This applies to Memory Sprint (brief role intro before recall), Phase 4 (full Wise Status recipe), and Phase 5 (heritage mnemonic anchor). Phase 0-A/0-B, Phase 3 (Game Breaks), and Phase 6 Boss are excluded. |
| **Phase 6 "certification" framing** | Final Boss is reframed as a "professional certification." On Boss entry: *"Bu — sizning professional sertifikatingiz. Global standartga mos keling."* On Boss defeat: *"Sertifikatsiya muvaffaqiyatli! Siz [Role] sifatida tasdiqlandingiz."* The HP/Boss game mechanics remain unchanged — only the narrative framing changes. |
| **Dark mode (#0a0a0a) as default** | The platform defaults to dark mode (#0a0a0a background) for all National Pride injection screens (gate quote, between-phase facts/quotes, milestone breaks). In-session phases use the existing theme. Students can override in settings. |

**Data Source:** `quotes_database.json` (4,800+ items, structured with type/author/text/category/origin/id). Requires subject-tagging before deployment (current `category: "General"` is insufficient for relevant matching).

---

## Scope

These principles apply universally — every homework session, every subject, every grade band (G1-G11). They are the non-negotiable design contract that all downstream components must satisfy.

- Section 1.1 (Learning Pyramid): constrains phase selection and minimum Bloom's coverage per session.
- Section 1.2 (3 Sacred Principles): constrains content sourcing (Principle 1), adaptive engine thresholds (Principle 2), and the entire gamification economy design (Principle 3).
- Section 1.3 (No Busywork): constrains every single content item — no item enters the pool without a `transition_skill` tag.
- Section 1.4 (Buzan): constrains session phase ordering and the TEFCAS feedback vocabulary used by the AI tutor.
- Section 1.5 (National Pride): constrains narrative framing, between-phase content injection, and Phase 4/7 closing constructions.

## Cross-references

- `content-architecture.md` — inherits Principle 1 (textbook as source of truth); mandatory `transition_skill` tag in §2.5 enforces §1.3.
- `gamification-economy.md` — inherits Principle 3 (intrinsic motivation); all XP/badge/avatar rules must satisfy the zero pay-to-win constraint.
- `NETS-Homework-Engine-UNIFIED-Buzan.md §3` — PISA Framework; the Learning Pyramid maps directly to PISA proficiency levels.
- `NETS-Homework-Engine-UNIFIED-Buzan.md §4-§5` — Phase construction rules; Buzan MIG/BOST/TEFCAS map governs phase sequencing rationale.
- `system/narrative/quotes_database.json` — data source for National Pride module (§1.5).
- All subject frameworks (standards/library/subject-family/) — inherit these principles as their foundational constraints; delta layers may not override §1.2 or §1.3.

## Verification

- [ ] Every session spans ≥4 Bloom's levels (verify via `[Bloom: LX]` tags in output).
- [ ] No content item is deployed without a `transition_skill` tag (check `draft` status queue).
- [ ] Adaptive engine thresholds match exactly: <60% → reduce, >90% → increase, 70-80% → hold.
- [ ] No real-money purchases exist anywhere in the gamification economy.
- [ ] Phase 0-A gate quote has 5-second countdown lock implemented.
- [ ] Origin balance across 10-item rolling window ≈ 55% National / 45% Global.
- [ ] Type balance across between-phase content ≈ 70% Facts / 30% Quotes.
- [ ] Phase 6 Final Boss contains zero National Pride injections.
- [ ] "Wise Status" recipe applied to ~30% of Phase 4 tasks only (not other phases).
