# NETS Tier Overlay Specification — Layer 3

**Document status:** Draft — pending founder review
**Version:** 2.0 (aligned with UNIFIED-Buzan v2.0)
**Date:** 2026-04-14
**Parent:** `NETS-System-Design-v1.md` Section 4
**Constitution:** `NETS-Homework-Engine-UNIFIED-Buzan.md` v2.0 (unchanged)
**Layer:** 3 (inherits Layers 0–2; cannot contradict them)

---

## 0. Design Principle

The Rule: **Basic = the full UNIFIED-Buzan product. Premium = Basic + enrichment on top.**

Both Basic and Premium are **paid tiers**. There is no free tier.

Basic delivers the **full product** — everything specified in UNIFIED-Buzan v2.0 and all subject frameworks. A Basic student receives a complete, gamified, AI-supported learning experience covering the full national curriculum.

Premium delivers **everything in Basic plus more** — smarter AI (Tier 3), more practice (weekly PISA, specialized courses, on-demand games), richer feedback (parent dashboard, Notebook Capture analysis), and access equity (offline mode). Premium is an enrichment layer, not the "real" product.

**The test:** If removing Premium from NETS would leave Basic students with an incomplete or inferior education, the tier split is wrong. Basic alone must be sufficient to hit the PISA mission targets.

**What this document specifies:** For each product dimension, exactly what Basic includes (inherited from Layers 0–2) and what Premium adds on top. This is a **delta document** — it only describes what Premium adds, because Basic is the full product as-is.

---

## 1. Tier Comparison Matrix

### 1.1 Session Structure

| Component | Basic | Premium Adds |
|---|---|---|
| Pre-Session 0-A (Theme Preview) | Full 8 components, gate quote, 5-sec lock | Same |
| Pre-Session 0-B (Flash Cards) | Full reference deck | Same |
| Phase 1 Memory Sprint | Full (5-8 items, flexible format) | Same |
| Phase 2 Story Mode | Full (3 segments + checkpoints, CPA) | Tier 3 narrative branching (personalized story paths) |
| Phase 3 Game Breaks | Full (3 games, dual-catalog rule) | Same in-session + on-demand game access outside sessions + cosmetic polish |
| Phase 4 Real-Life Challenge | Full | Same |
| Phase 5 Consolidation | Full (Memory Palace, Peg, Link, Radiant, SMASHIN' SCOPE) | AI-generated connection maps linking lessons |
| Phase 6 Final Boss | Full (HP system, 2 attempts, Tier 2 eval) | Tier 3 Socratic tutor on failure (unlimited retries + question regen) |
| Phase 7 Reflection | Full | Tier 3 personalized "what to focus on next" |
| National Pride injection | Full (55/45, 20% task, gate quotes) | Same |

### 1.2 AI Tiers

| Tier | Basic | Premium |
|---|---|---|
| Tier 1 (rule-based, ~$0) | ~80% of interactions | Same |
| Tier 2 (small LLM) | Boss eval (2 attempts), anti-cheat, story checkpoints | Same |
| Tier 3 (Opus-grade) | Not available | Personal AI tutor on Boss failure, Socratic "why?" on any question, study plans, writing feedback, exam prep |
| Cost target | $3-5/student/year | $8-15/student/year |

**This is the biggest differentiator.** Basic students who fail the Boss twice → marked as failed, next session continues. Premium students → AI tutor activates, unlimited guided retries.

### 1.3 Content

| Dimension | Basic | Premium Adds |
|---|---|---|
| Textbook curriculum | 100% — all chapters, all subjects | Same |
| Difficulty band | Adaptive up to student's level + 1 | Level + 2 (L5-L6 stretch tasks when >85%) |
| Specialized courses | Not available | AI Literacy, Critical Thinking, Economy & Finance, Law, IT & Programming, Language Enrichment, Extended PISA Prep |
| Exam prep tracks | Not available | Structured revision targeting student's PISA weaknesses |

### 1.4 Games

| Dimension | Basic | Premium Adds |
|---|---|---|
| In-session (Phase 3) | All 28 mechanics, dual-catalog rule | Same |
| Outside sessions | Not available | On-demand game access from Library anytime |
| Game modes | Standard | + Timed challenge, head-to-head, Master Mode |
| Visual polish | Standard | Enhanced animations/audio (cosmetic only) |

### 1.5 PISA Events

| | Basic | Premium |
|---|---|---|
| Monthly PISA checkpoint | Yes | Yes |
| Weekly PISA lesson (~20 min) | Not available | Yes (async 7-day window, teacher-tracked) |

### 1.6 Metagame (Bilim Bazasi)

| | Basic | Premium |
|---|---|---|
| Base building, BT earning, heroes, streaks | Full | Full |
| Mystery Boxes | BT-only (no real money) | Same |
| Tournaments | Class-level | + School-level, regional |
| Seasonal events | Not available | Time-limited themed events |
| Cosmetic collections | Standard | + Premium architectural styles, extended hero lore |

**Rule:** BT never has a real-money entry point in either tier.

### 1.7 Dashboards

| | Basic | Premium |
|---|---|---|
| Parent | Weekly auto-summary (3-5 lines) | Full interactive: PISA trajectory graph, skill heatmap, AI narrative report, weekend recommendations |
| Teacher | Full: attendance, mastery map, anti-cheat, session metrics | + Weekly PISA tracker, class analytics, CSV/PDF exports |

### 1.8 Infrastructure

| | Basic | Premium |
|---|---|---|
| Offline mode | Not available | Downloadable session packs (Tier 1 only, Boss queued for online) |
| Session modes | Standard + Recovery (auto) | + Extended on-demand at home (45-60 min) |
| Notebook Capture frequency | Per subject framework | Same frequency + Tier 3 detailed feedback |

---

## 2. Detailed Dimension Specifications

### 2.1 Content

**Basic:** Every chapter, every topic, every standard in the Uzbek national textbook canon. Content coverage is 100% of the curriculum assigned to the student's grade and subject. All content is tagged with dual standard codes (`UZ-MATH-5-FRAC-01` / `MAT.5.3.4.1`), PISA levels, and `transition_skill` tags per UNIFIED-Buzan v2.0 Section 2.

**Premium adds:**
- **Beyond-textbook extensions:** Deeper explorations of curriculum topics that go past what the textbook covers. Example: G5 Science textbook covers "The Solar System" in one chapter → Premium adds an extended module on space exploration with PISA L4-L5 tasks.
- **Exam preparation tracks:** Structured revision sessions targeting specific upcoming assessments, calibrated to the student's current PISA level.
- **Elective modules:** Cross-subject enrichment courses (see Section 2.6) not part of the standard curriculum.

**Rule:** No curriculum-required content is Premium-exclusive. If the textbook teaches it, Basic has it.

### 2.2 Homework Sessions

**Basic:** The full 7-phase session as specified in UNIFIED-Buzan v2.0 Section 4-5:
- Phase 0-A: Theme Preview (mandatory)
- Phase 0-B: Flash Cards (mandatory)
- Phase 1: Memory Sprint
- Phase 2: Story Mode
- Phase 3: Game Breaks (dual-catalog rule: ≥1 Interactive Catalog + ≥2 Default Pool)
- Phase 4: Real-Life Challenge
- Phase 5: Consolidation
- Phase 6: Final Boss (or subject-specific climax — Big Decision, The Make, etc.)
- Phase 7: Reflection

All session parameters per subject framework apply: duration, flow targets, mechanic bans, Notebook Capture frequency, Boss HP tiers, Why Chain caps, etc.

**Premium adds:**
- **Expanded difficulty band:** After a student consistently scores above 85% at their current PISA level, Premium unlocks L5-L6 "stretch" tasks within the session. Basic caps adaptive difficulty at the student's current level + 1; Premium allows current + 2.
- **Richer per-phase AI feedback:** In Story Mode, Premium students receive Tier 3 narrative branching (personalized story paths based on prior answers). In Consolidation, Premium gets AI-generated connection maps linking today's lesson to previous sessions. In Reflection, Premium gets a Tier 3 personalized "what to focus on next" summary.
- **Session replay with analysis:** Premium students can replay completed sessions with AI commentary highlighting where they did well and where they struggled.

**Rule:** The 7-phase structure, phase sequence, immutables (Stranger Test, transition_skill tags, cosmetics-never-purchasable, 0-A/0-B mandatory), and all subject framework overrides apply identically to both tiers. Premium never skips phases or changes the learning loop.

### 2.3 Games

**Basic:** Phase 3 Game Breaks operate per UNIFIED-Buzan v2.0 dual-catalog rule every session. The student gets 3 games (≥1 from Interactive Catalog Pool, ≥2 from Default Pool), selected by subject eligibility + Bloom's target + PISA level. All 28 mechanics are available per subject framework allowances.

**Premium adds:**
- **On-demand game access:** Premium students can launch any unlocked game from the Library at any time outside of sessions. Basic students access games only within Phase 3 of a session.
- **Higher-polish game variants:** Enhanced visuals, animations, and audio for the same game mechanics. Gameplay and learning outcomes are identical — the polish is cosmetic.
- **Premium-exclusive game modes:** Timed challenge variants, head-to-head modes against classmates, and "Master Mode" (harder parameterization of existing mechanics).

**Rule:** Within a session, both tiers get the same Phase 3 experience. The dual-catalog rule is never violated for either tier. Premium's game advantage is access *outside* sessions and cosmetic polish *within* sessions.

### 2.4 AI Tier

**Basic:** Tier 1 (rule-based, ~$0) handles ~80% of all tasks: MC, matching, numeric, exact string. Tier 2 (small LLM, cents/student/year) handles Boss evaluation (2 attempts max), anti-cheat analysis (behavioral baseline + semantic anomaly detection), and story checkpoints. If the student fails the Boss twice, they are **marked as failed** for that session and move on — the next session picks up the Boss. Cost target: $3-5/student/year.

**Premium adds:**
- **Tier 3 Personal AI Tutor on Boss failure:** When a Premium student fails the Boss twice, instead of being marked as failed, a Tier 3 Socratic tutor activates. The tutor guides the student through the problem with multi-turn dialogue (without revealing answers), and the Boss question is regenerated for a fresh attempt. This cycle continues until the student defeats the Boss. The AI tutor acts as a personal teacher — Premium students effectively get unlimited guided retries on the Boss.
- **Tier 3 on any question, any phase:** Beyond Boss failure, Premium students can ask "why?" on any task and receive a guided Tier 3 dialogue toward understanding.
- **Personalized cross-subject study plans:** Weekly AI-generated plan analyzing weaknesses across all enrolled subjects.
- **Detailed writing feedback:** Rubric-based analysis of open-ended responses with specific improvement suggestions.
- **Exam preparation adaptation:** Dynamically generated practice sets targeting the student's weakest transition skills.

**The framing:** The Tier 3 Boss tutor is like having a personal teacher. It's not that Basic students get a worse Boss — they get the same Boss, the same 2 attempts, the same Tier 2 evaluation. Premium students just get a tutor who helps them through if they're stuck. The Boss with Tier 3 help earns the student extra credit for persistence and mastery.

**Rule:** Tier 2 anti-cheat runs for both tiers — cheating detection is not a Premium feature. Fallback discipline applies to both tiers: if Tier 2 or Tier 3 is unreachable, the system falls back to Tier 1 with rule-based evaluation. No session ever fails because AI is unavailable.

### 2.5 Notebook Capture

**Basic:** Frequency per subject framework:
- Science G5: ≥1 in every 3 sessions (highest priority)
- Texnologiya G5: ≥1 in every 2 sessions
- Tasviriy Sanat G5: every session (The Make IS Notebook Capture)
- Geografiya G5: 1 in every 4 sessions (map labeling only)
- Other subjects: per family/subject framework specification

AI evaluation at Tier 2: presence detection, basic structure check, pass/fail + one tip.

**Premium adds:**
- **Enhanced Tier 3 vision feedback:** Detailed rubric-based evaluation (not just pass/fail). For Science: feedback on diagram accuracy, labeling completeness, conceptual correctness. For Tasviriy Sanat: technique analysis, comparison to master works, specific improvement suggestions. For Texnologiya: safety compliance check, step completeness, craftsmanship assessment.
- **Notebook Capture portfolio:** AI-curated gallery of the student's best captures across subjects, with progression commentary.

**Rule:** Notebook Capture frequency is not changed by tier. If the subject framework says 1-in-3, both Basic and Premium do 1-in-3. The difference is feedback depth, not occurrence.

### 2.6 Specialized Courses (Premium-exclusive)

These are cross-subject enrichment courses not part of the standard Uzbek curriculum. They exist only in Premium and are delivered as standard 7-phase sessions using the same engine.

| Course | Description | PISA Domain |
|---|---|---|
| AI Literacy | How AI works, prompt thinking, ethical considerations | Creative Thinking + Reading |
| Critical Thinking | Argument analysis, logical fallacies, evidence evaluation | Reading + Science |
| Economy & Finance | Personal finance, market basics, economic reasoning | Math + Reading |
| Law & Civic Rights | Constitutional basics, rights and responsibilities, case analysis | Reading |
| IT & Programming | Computational thinking, basic coding concepts, algorithm design | Math + Creative Thinking |
| Language Enrichment | Beyond-curriculum vocabulary, advanced grammar, literary analysis | Reading |
| Extended PISA Preparation | Intensive PISA-style practice across Math, Reading, Science | All domains |

**Rule:** These courses follow UNIFIED-Buzan v2.0 100% — same 7 phases, same tagging requirements, same immutables. The only difference is their content is not textbook-derived (Principle 1 exception: these supplement, not transform, the textbook). Each task still requires a `transition_skill` tag (Principle 2: every task earns its existence).

### 2.7 PISA Events

**Basic:** Monthly PISA checkpoint — a standard session with PISA-style tasks drawn from the student's active subjects. Automatically scheduled. Results visible to student and teacher.

**Premium adds:**
- **Weekly PISA lesson:** ~20 minutes, structured as a standard 7-phase session with PISA-style content. Delivered within a 7-day async rolling window (student picks their time). Teacher dashboard tracks completion.
- **Strict-deadline enforcement:** Future configurable option (not launch default). Fixed weekly cutoff with teacher-visible non-completion flag. Requires school administrator buy-in and consequence design that respects Principle 3 (the 10-year-old is not a small adult).

**Rule:** Monthly checkpoints are identical for both tiers. Premium's weekly lesson is additional, not a replacement.

### 2.8 Metagame (Bilim Bazasi)

**Basic:** Full access to the persistent metagame:
- Bilim Bazasi visual base — grows with chapter completions and skill mastery
- Bilim Tokens (BT) earned by: completing sessions (small), mastering PISA transition skills (medium), defeating Bosses (large), streak milestones (large)
- BT spent on: cosmetic buildings, Central Asian heritage decorations, hero unlocks (Al-Khwarizmi, Ibn Sina, Ulugh Beg, Beruniy) with lore vignettes and mini-missions, Mystery Boxes (BT-only, never real money)
- Streaks with earned freeze (mastery-based, not purchased)
- Class-level tournaments (weekly reset, relative rank only)

**Premium adds:**
- **Faster BT earning:** Premium tournament participation awards bonus BT (the multiplier is a playtesting variable — see Open Questions).
- **Additional cosmetic collections:** Seasonal sets, premium architectural styles, extended hero lore chapters.
- **Seasonal events:** Time-limited themed events with unique cosmetic rewards. Events are bonus opportunities — never required for PISA progression (FOMO protection per UNIFIED Principle 3).
- **School-level and regional tournament tiers:** Class-level is default for both. Premium unlocks opt-in to school-wide and regional tournaments.

**Rule:** BT has no real-money entry point in either tier. No BT purchase provides academic advantage. Mystery Boxes are BT-only in both tiers. The Bilim Bazasi cosmetics are signals of learning history, not purchased status symbols. A Basic student's base can grow just as large as a Premium student's — Premium just has more decorating options.

### 2.9 Parent Dashboard

**Basic:** Weekly auto-generated progress summary delivered via notification or in-app. Contains:
- Sessions completed this week
- Current streak
- Subjects active
- One-line AI summary of performance trend ("Improving in Science, steady in Math")

**Premium adds:**
- **Full interactive dashboard:**
  - PISA level trajectory graph per domain (Math, Reading, Science, Creative Thinking)
  - Transition-skill heatmap: which skills are mastered, in-progress, or struggling
  - Weekly AI-written narrative report (Tier 3): "This week, [Name] mastered fraction comparison (L2→L3) but struggled with multi-step word problems. Recommended practice: 10 minutes of Real-Life Challenge tasks in Math."
  - "What to practice this weekend" personalized recommendations
  - Cross-subject weakness analysis
  - Historical progress view (month-over-month PISA trajectory)

### 2.10 Teacher Dashboard

**Basic:** Full operational dashboard:
- Class-level attendance heatmap
- Per-student mastery map (PISA transition skills completed/in-progress/not-started)
- Anti-cheat flag log (MONITOR / SOFT_WARNING / TEACHER_ALERT)
- Session duration and phase completion rates
- Mobile-first design (usable on basic smartphone)

**Premium adds:**
- **Weekly PISA lesson completion tracker:** Which Premium students completed the weekly lesson, when, and how they scored.
- **Premium class analytics:** Aggregate class-level PISA trajectory, class-wide skill gap identification, comparison to school/regional averages (anonymized).
- **Exportable reports:** CSV and PDF exports for integration with school administrative systems.

### 2.11 Offline Mode

**Basic:** Not available. Sessions require internet connectivity for Tier 2 AI evaluation and anti-cheat analysis.

**Premium adds:**
- **Downloadable session packs:** Pre-generated sessions (using Tier 1 evaluation only) that can be completed offline and synced when connectivity returns.
- **Offline scope:** Memory Sprint, Story Mode, Game Breaks (Default Pool only — Interactive Catalog games require server validation), Consolidation, Reflection. Boss and RLC require connectivity and are queued for the next online session.
- **Anti-cheat:** Offline sessions use behavioral timing analysis only (no Tier 2 semantic check). Flagged for review on sync.

**Rule:** Offline mode exists to serve students in rural areas with unreliable internet. It is not a "convenience" feature — it is an access equity feature gated by Premium because of the engineering cost of offline-first architecture.

### 2.12 Session Modes

**Basic:** Standard (30-45 min, daily homework) + Recovery (15-20 min, auto-triggered for missed sessions). Extended mode (45-60 min) available only via teacher override for in-class use.

**Premium adds:**
- **Extended mode on-demand:** Premium students can choose Extended (45-60 min) sessions at home without teacher override. Useful for exam preparation or deep practice sessions.
- **Subject-specific duration overrides remain unchanged:** Science G5 35-45 min, Tarbiya G5 15-25 min, etc. Premium Extended adds time on top of the subject's standard duration.

---

## 3. What Is NOT Tier-Gated (Immutables)

These elements are identical in both tiers and cannot be moved to Premium:

| Element | Reason |
|---|---|
| 7-phase structure + Phase 0-A/0-B | Core learning loop — removing phases breaks pedagogical design |
| Full curriculum coverage | Basic students pay for education — curriculum is not a Premium feature |
| All 28 game mechanics | Mechanics are pedagogical tools, not entertainment features |
| Dual-catalog rule | Session game selection is part of the learning design |
| Flow state targets (70-80%) | Adaptive difficulty is core, not premium |
| Boss must be defeated | Mastery requirement is universal |
| Anti-cheat (Tier 2 for both) | Academic integrity is universal |
| Notebook Capture frequency | Per subject framework — frequency is pedagogical, not tier-based |
| Remediation routing | Support for struggling students is not gated |
| TEFCAS failure framing ("Hali emas!") | G5 psychology requirement — universal |
| National Pride injection | Universal design principle — 55/45 ratio, 20% task injection, gate quotes |
| Uzbek-first cultural framing | Universal design principle |
| Cosmetics-never-purchasable | Applies to both tiers — Premium cosmetics are unlocked by BT, not bought with money |

---

## 4. Premium Upsell Surfaces

Upsell prompts are contextual, soft, and never blocking. They appear after session completion, not during.

| Trigger | Prompt | Links to |
|---|---|---|
| Student scores >85% on session | "Want to try the harder version?" | Premium difficulty band preview |
| Student fails Boss twice | "Want 5 minutes with the AI tutor?" | Tier 3 Socratic tutoring preview |
| After monthly PISA checkpoint | "Premium students get weekly PISA practice" | Weekly PISA lesson info |
| Student browses Library | Locked Premium chapters visible with one-sentence preview | Specialized course preview |
| End of session (1 in 5 frequency) | "Your parent can see your full progress with Premium" | Parent dashboard info |

**Rules:**
- Never shown during a session phase — only on completion/transition screens
- Maximum 1 upsell prompt per session
- Student can dismiss permanently ("Don't show me this again")
- No upsell prompt implies academic inadequacy ("You need Premium to succeed" is forbidden)
- Upsell copy must be approved and cannot use anxiety/FOMO language

---

## 5. Cost Model Impact

| Tier | Primary cost drivers | Target cost per student per year |
|---|---|---|
| Basic | Tier 2 LLM (Boss evaluation, anti-cheat, story checkpoints) | $3-5 |
| Premium | Tier 3 LLM (Socratic tutoring, study plans, writing feedback, vision) + specialized course content + offline infra | $8-15 (estimate — requires validation) |

**Basic cost protection:** 80% of Basic interactions are Tier 1 (rule-based, ~$0). Tier 2 handles ~15% at cents/student/year. Tier 3 is used only on Boss failure for Basic (the existing spec), keeping costs within the $3-5 target.

**Premium cost drivers:** Unlimited Tier 3 access is the largest variable. Per-student Tier 3 cost depends on usage frequency (how often students invoke Socratic tutoring). The $8-15 estimate assumes ~2-3 Tier 3 interactions per session on average. Requires validation with real usage data.

---

## 6. Implementation Notes

### 6.1 How the Platform Distinguishes Tiers

The Tier Overlay is implemented as a feature flag layer in the platform, not as separate content. Both tiers run the same session engine, the same frameworks, the same mechanics. The platform checks the student's tier at specific decision points:

- **Before Phase 3:** Basic = session games only. Premium = session games + Library on-demand access flag.
- **On Boss failure (2x):** Basic = marked as failed, continue next session. Premium = Tier 3 personal tutor activates, unlimited guided retries with question regeneration until Boss is defeated.
- **On any question "why?" tap:** Basic = static hint from pre-authored hint bank. Premium = Tier 3 live Socratic dialogue.
- **On session complete:** Basic = static summary. Premium = Tier 3 personalized analysis.
- **On Notebook Capture evaluation:** Basic = Tier 2 pass/fail + tip. Premium = Tier 3 detailed rubric feedback.
- **On Library browse:** Basic = curriculum content. Premium = curriculum + specialized courses + on-demand games.
- **On parent login:** Basic = static weekly summary. Premium = full interactive dashboard.

### 6.2 Data Model Delta

The Tier Overlay requires these additions to the platform data model:

- `student.tier`: enum (`BASIC`, `PREMIUM`)
- `student.tier_start_date`: timestamp
- `student.tier_end_date`: timestamp (for subscription management)
- `session.tier_at_time`: snapshot of tier when session was created (prevents mid-session tier changes)
- `premium_game_access_log`: tracks on-demand game usage outside sessions
- `premium_pisa_weekly`: weekly PISA lesson completion records
- `offline_session_pack`: pre-generated session data for offline mode
- `parent_dashboard_access`: tier-gated parent portal access level

### 6.3 Migration Path

For the existing 5 G5 frameworks (Science, Tarbiya, Texnologiya, Tasviriy Sanat, Geografiya): no changes needed. They describe the full learning experience, which IS the Basic tier. Premium features layer on top via platform feature flags, not framework modifications.

---

## 7. Open Questions

1. **Premium pricing.** Family-paid subscription, school-licensed institutional purchase, government-sponsored (free Premium for rural/low-income), corporate-sponsored, or hybrid. Affects everything from upsell copy to teacher dashboard features. Decision authority: founder + business team.

2. **BT multiplier for Premium tournaments.** How much faster should Premium students earn BT in tournaments? Too high = feels pay-to-win (violates Principle 5). Too low = not a meaningful Premium benefit. Requires playtesting.

3. **Premium cost per student validation.** The $8-15 estimate for Premium assumes ~2-3 Tier 3 calls per session. Actual usage patterns may vary significantly. Needs real usage data from pilot.

4. **Offline mode engineering scope.** Pre-generating sessions with Tier 1 only is technically straightforward. Syncing anti-cheat data on reconnect, handling Boss queue, and preventing offline cheating are harder problems. Needs engineering assessment.

5. **Specialized course content pipeline.** Who writes the AI Literacy, Critical Thinking, etc. courses? They don't have textbook sources (Principle 1 exception). Need a content creation process and quality bar.

6. **Parent dashboard Tier 3 cost.** Weekly AI-written narrative reports for every Premium parent could be expensive at scale. May need to be generated batch (not real-time) to manage costs.

7. **Upsell prompt localization.** All upsell copy needs Uzbek and Russian versions. Tone must be culturally appropriate — avoid aggressive Western SaaS conversion language.

8. **Extended mode on-demand impact on learning outcomes.** Does letting Premium students self-select 45-60 min sessions at home improve or hurt outcomes? Longer sessions risk attention fatigue (G5 psychology: 20-30 min attention window). May need a "recommended break" prompt at the 35-min mark.

9. **RESOLVED — Tier 3 Boss failure.** Basic students get 2 Boss attempts with Tier 2 evaluation; fail twice = marked as failed, next session continues. Premium students get a Tier 3 personal AI tutor on Boss failure with unlimited guided retries + question regeneration. The AI tutor is framed as a personal teacher, not a paywall on learning. UNIFIED-Buzan v2.0 needs a versioned note that Tier 3 Boss tutoring is now a Premium feature, with Basic retaining the existing "max 2 retries, next session continues" behavior.

---

*Document path: `All analysis/Full Design Rework/NETS-Tier-Overlay-Spec.md`*  
*Parent: `All analysis/NETS-System-Design-v1.md` Section 4*  
*Constitution: `All analysis/Universal Specs/NETS-Homework-Engine-UNIFIED.md` v2.0*
