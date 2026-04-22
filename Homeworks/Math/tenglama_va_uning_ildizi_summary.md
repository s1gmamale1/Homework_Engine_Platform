# Why This Homework Looks The Way It Does

**Lesson:** Tenglama va uning ildizi (Algebra · G7 · Chapter IV, Lesson 1)
**Companion files:** `tenglama_va_uning_ildizi.md` (homework) · `tenglama_va_uning_ildizi.html` (LMS preview) · `tenglama_va_uning_ildizi_framework_notes.md` (framework calibration)

---

## TL;DR

This is a ~33-minute software-delivered homework that formalizes three things a 7th-grader already half-knows (what an equation is, what a root is, what "solving" means), introduces one new technique (substitution checking), and lands two genuinely surprising ideas (equations can have no roots, or infinite roots). Every design choice was made against three filter questions: *Can a 7th grader understand it? Will they actually learn? Is it easy to follow?* When a framework rule served those questions we used it; when it didn't, we broke it. 12 rule-breaks are documented for framework calibration.

---

## The goal

Build a **gold-standard homework example** that can (a) be used in a real LMS classroom tomorrow, (b) serve as a calibration anchor for future auto-generated homeworks, and (c) expose which parts of our unified framework are over-engineered for short conceptual lessons.

Every design decision was filtered through three kid-facing questions:

1. **Can a 7th grader understand this?**
2. **Will they actually learn something?**
3. **Is it easy to follow?**

If an element failed any one of these, it was cut or redesigned — even if the framework said to keep it.

---

## What this lesson actually teaches (and why we scoped it this way)

The textbook introduces 5 new terms (tenglama, noma'lum, ildiz, yechish, teng kuchli), 1 new procedure (substitution checking), and 3 outcome patterns (1 root, 0 roots, ∞ roots). We audited every exercise in the textbook and found:

- ~70–80% of the exercises are pure substitution checking
- ~20–30% require light reasoning (proving no-root, recognizing identity, equivalence detection)

**The student isn't a blank slate.** They already know from G6 how to solve simple equations like `5x = 20 → x = 4`. They already know from Chapters 1–3 how to expand, simplify, and evaluate algebraic expressions. What's **actually new** in this lesson is:

- The formal vocabulary (naming what they've been doing)
- The checking tool as a deliberate technique (useful when equations get too hard to solve directly)
- The idea that equations can have zero or infinite roots (this breaks their G6 prior that every equation has one answer)

**What this lesson does NOT teach:** systematic equation solving (balance rule, transposition). That's 2–3 lessons later. The student can check any candidate but cannot yet solve equations like `−3(x+3) = 4x+5` from scratch.

**Why this matters for the homework design:** we couldn't ask the student to *solve* anything in Phase 4 or Phase 6, because the skill isn't there yet. Any framework rule that demanded solving had to be bent into a checking-mode variant.

---

## The 9 phases — why each one exists

| Phase | Duration | Why this phase is in the homework |
|---|---|---|
| **0-A · Mavzu Ko'rigi** | ~1 min | Orient the student without teaching. 3 compact screens. Screen 1 frames the new skill using the Aziza/Dilshod check-vs-solve contrast. Screen 2 fills three textbook gaps (word hierarchy, why "no root" isn't a paradox, why "infinite roots" isn't a paradox). Screen 3 captures the student's own learning goal (BOST) to resurface in Phase 7. |
| **0-B · Flesh Kartalar** | ~30s | 6-card reference deck with the 5 lesson terms + a 3-cases summary card. Accessible throughout the homework as a "Kartalar" overlay — if the kid forgets what "teng kuchli" means in Phase 3, they tap the card. Illustrative examples included on each card (we broke the framework's "no worked examples" rule here, documented in calibration notes). |
| **1 · Xotira Hurrasi** | ≤2 min | 6 tap-only warmup items. Primacy effect: Items 1–2 test the most fundamental distinctions (what's a tenglama vs a tenglik) before anything else. Items 3–4 put the two edge cases (identity / no-root) right in the warmup so they're not a shock in Phase 2. Items 5–6 test substitution accuracy under negatives. |
| **2 · Hikoya Rejimi** | ~5 min | One continuous narrative where Sevinch discovers the checking technique by watching two classmates struggle (Jasur tries solving, Dilshod gets stuck on a no-root equation). The story shows all 3 outcome cases through Sevinch working through them, not by abstract definition. Stranger Test passed: a reader without the textbook can answer the 3 checkpoints using only the story's logic. |
| **3 · O'yin Tanafuslari** | ~7–9 min | 3 games, each drilling a different sub-skill: Tile Match (pattern recognition: equation structure → outcome case), Mystery Box (the anchor game: predict-from-structure then verify-by-substitution), Adaptive Quiz (substitution fluency at the student's exact level). Von Restorff Anchor on the middle slot — Mystery Box is the memorable one. |
| **4 · Hayotiy Vazifa** | ~4 min | Student becomes a junior judge at the Al-Khwarizmi Math Olympiad. Three competitors submit claims — one correct (normal case), one wrong (no-root trap), one partially correct (identity trap where "only" is the error). The scenario requires only verification, no construction. Heritage anchor lands naturally here, not forced. |
| **5 · Xotira Mustahkamlash** | ~3 min | Radiant Summary mind map (Tenglama → 4 branches → 3 color-coded root cases) for active-drag consolidation. Then a step-reconstruction where the student fills in the middle of a substitution check. Re-encodes the lesson's core content through visual + kinesthetic channels. |
| **6 · Yakuniy Sinov** | ~7 min | 5-question boss with HP bar. Distribution: 2 Easy (simple checking) + 2 Medium (pattern recognition + equivalence) + 1 Hard (construct an equation with a given root — L5 Evaluate-Create). No MC anywhere. Every question tests only what was taught; none requires solving skills the student doesn't have yet. |
| **7 · Aks Ettirish** | ~2 min | 6 reflection beats. Session summary card, "what surprised you most?" curiosity hook (intro-lesson variant), 3 metacognitive prompts (accuracy-adapted), BOST goal recall from Phase 0-A, spaced-repetition schedule preview, al-Khwarizmi closing line that lands the etymology ("al-jabr" = "reunion of broken parts"). |

---

## Key design decisions (the big calls)

### 1. We kept all 9 phases — but they were close calls

Every phase earned its spot. **Phase 4 was almost dropped** because the framework's Algebra spec demanded students set up an equation from scratch (a skill they don't have yet). Instead of dropping the phase, we kept it and redefined its purpose: **verification scenario** (check a peer's claim) instead of **construction scenario** (build your own equation). The Olympiad judge framing was chosen because it's a genuine real-life role for a 7th grader AND it naturally carries the al-Khwarizmi heritage anchor.

### 2. Phase 0-A is 3 screens, not 8 panels

The framework defaults to 8 panels of 5–10 sentences each. For a tight conceptual lesson like this one, that's 30–40% of the total homework spent on orientation before any practice. **We compressed to 3 screens** because panels 6–8 (industry applications, mathematician spotlight) aren't load-bearing for a simple concept — they're ceremony. Heritage anchor moved to Phase 7 closing where it lands harder.

### 3. Phase 0-A Screen 2 became a "Better Explanation," not a prior-knowledge bridge

Original Screen 2 just listed what the student already knew. **Revised Screen 2 now fills three textbook gaps** the student will otherwise stumble on: the word hierarchy (tenglik/tenglama/ildiz/teng kuchli with one-line differences), why "no root" isn't a paradox (with an age-plus-5 analogy), and why "infinite roots" aren't a paradox (with the 3x+6=3x+6 expansion shown explicitly). The prior-knowledge bridge moved into Screen 1's hook.

### 4. The Phase 0-A hook honestly acknowledges prior G6 knowledge

Earlier drafts said *"today you learn to check without solving."* That framing was misleading — the student already knows how to solve simple G6 equations. The **revised hook honors their existing skill**: *"You already know how to solve simple equations. Today we formally define what a 'root' is, and introduce checking — a new tool for when equations get too hard for G6 methods. Systematic solving comes 2–3 weeks from now."* This sets up the lesson without pretending the student is a blank slate.

### 5. Three Phase 3 games, each drilling a different sub-skill

Rather than three variations of the same drill (which would be padding), we picked three mechanics that test three cognitively distinct sub-skills:

- **Tile Match** — *pattern recognition.* Read the equation structure, predict the outcome case.
- **Mystery Box** — *predict-then-verify.* The meta-skill of the whole lesson in one game.
- **Adaptive Quiz** — *substitution fluency.* IRT-adaptive, calibrates to the student's actual level.

Mystery Box deliberately sits in the middle slot (Von Restorff Anchor) because it's the most distinctive game — the kid will remember the two-stage predict-then-verify flow long after they've forgotten the other two.

### 6. Phase 6 boss avoids solving entirely

Framework says Phase 6 for Algebra should require students to solve equations with shown steps. **We couldn't, because the skill doesn't exist yet.** So the 5 boss questions instead drill: substitution (Q1–Q2), reasoning about structure (Q3), equivalence detection (Q4), and **construction from a given root** (Q5). Q5 is the creative reach — constructing an equation with root 6 is genuinely L5 Evaluate-Create using only lesson-available skills.

### 7. Al-Khwarizmi anchor lands once, at the end

Framework says algebra subjects must include al-Khwarizmi "minimum 1 per 3 sessions," typically in Phase 0-A Panel 8 or Phase 5. **We landed him once**, in Phase 7's closing, and briefly again in Phase 4's Olympiad framing. Dispersing the anchor across phases would dilute it — concentrating it at the end where the student has *earned* the cultural connection lands harder.

### 8. No National Pride injection in Phase 1

Framework defaults to ~1 in 5 Phase 1 items having a professional/cultural framing. **We skipped it.** Forcing *"Siz tahlilchisiz"* framing onto a vocabulary check would fail Q1 (can they understand it?). National Pride is load-bearing where it fits naturally (Phase 4, Phase 7) and noise where it doesn't.

---

## What we deliberately didn't do

| Choice | Why not |
|---|---|
| Include the 8-panel Phase 0-A | Ceremony for a tight concept. 3 screens serve the same purpose in 1/3 the time. |
| Add an Industry Application panel | Couldn't make "engineers use equations" serve the lesson's actual content without feeling bolted-on. |
| Add the BOST gate quote with 5-second lock | Framework ceremony without content value at this lesson's scale. |
| Use CPA (Concrete→Pictorial→Abstract) progression | The lesson is already symbolic. No natural concrete-object phase. CPA is for arithmetic/geometry, not definitional algebra. |
| Use an "Amir Temur Campaign" narrative frame | Classroom setting is more relatable for a 12-year-old. Amir Temur framing would feel alien forced onto a math puzzle. |
| Include a W5H scaffold in Phase 4 | W5H is for multi-factor trade-off scenarios. Our Phase 4 is single-skill verification × 3 instances — W5H would add noise without adding learning. |
| Include a Why Chain game | Framework explicitly bans it for introductory lessons (students lack the causal-reasoning prior). |
| Mandate handwriting upload (Notebook Capture) in Phase 6 | Listed as acceptable but not mandatory. Text input works equally well for showing substitution. |
| Include hesitation-triggered logic in Phase 7 | That's an LMS runtime feature (tracking per-question hesitation time), not homework content. Documented as a runtime concern. |
| Include a Big Boss or Mythical Boss | Those are cross-lesson aggregates. This homework is single-lesson. |

---

## What we learned that applies beyond this one lesson

Three things this design exercise surfaced for the broader framework:

1. **The framework needs an "introductory lesson" mode.** Phases 2, 4, and 6 all assume the student can perform the lesson's procedure. For *first-lessons-of-chapter* (where the procedure is new), those phases need novice-mode variants (story ends in verification not solution; Phase 4 is check-a-claim; Phase 6 allows construction in place of solving).

2. **Scope-binding needs to be enforced at the schema layer.** Prose instructions like "stay in current lesson" are ignorable by a generation pipeline. Adding required `concept_ref` fields to phase schemas would prevent the drift we saw in earlier Biology pilots.

3. **Phase 0-A should scale with lesson type.** 8 panels is right for rich procedural lessons. 3 screens is right for tight conceptual lessons. Framework should guide that sizing explicitly.

All three are flagged in the companion framework-notes file for systemic review.

---

## How to read this homework

- **The full homework content** is in `tenglama_va_uning_ildizi.md` — open this to see exactly what the student reads.
- **The interactive LMS preview** is in `tenglama_va_uning_ildizi.html` — open in a browser to experience the flow with flashcard flips, answer reveal, mystery boxes, and phase navigation.
- **The framework calibration** is in `tenglama_va_uning_ildizi_framework_notes.md` — open this to see which framework rules were used, which were broken, and which need restructuring.
- **This file** is the bridge between design intent and final artifacts — use it to answer "why did we choose X?" without having to scroll through transcripts.
