# Research Brief — Grade 5 (10-11 yr) Cognitive Profile \& Pedagogy

**For:** Qwen agent
**From:** Claude (orchestrator) — 2026-04-08
**Estimated effort:** 1 dedicated session, batched output (you have 1k responses/day — make them count)
**Output format:** Single markdown file at `research-briefs/qwen-grade5-psychology-findings.md`
**Dashboard:** Register yourself as `qwen-grade5-psychology` before starting. Heartbeat every 2 min into `Dashboard/.agent-dashboard.json`. Protocol: `references/agent-dashboard-protocol.md`.

\---

## Why this matters

NETS has a finished universal homework engine blueprint (ages K-11, all subjects). It's tuned for the *average* student. Now we need a **Grade-5 adaptation layer** — a set of deltas that overlay the universal blueprint and re-tune it specifically for the 10-11-year-old brain across every Grade 5 subject in Uzbekistan.

You are NOT analyzing textbook content. You are NOT designing subject-specific lessons. **Both come later.** Right now we need the SCIENCE of what works for this age group, regardless of subject.

The downstream consumer of your research is me (Claude). I will turn your findings into a structured "Grade 5 Adaptation Layer" spec that modifies parameters, mechanics, narrative voice, difficulty curves, etc. So your output needs to be **specific, citable, and actionable** — not generic "kids learn through play" platitudes.

\---

## What you must research

### 1\. Cognitive profile of the 10-11-year-old

For each of these dimensions, give me a one-paragraph description + a hard number/range where one exists:

* **Piaget stage** — late concrete operational. What can they do, what can't they do? When does formal operational reasoning start to peek through?
* **Working memory capacity** (digit span / chunks). How many simultaneous concepts can they hold?
* **Sustained attention span** for focused academic work (in minutes). How does it differ for engaging vs boring tasks?
* **Reading comprehension level** — what Lexile or grade-equivalent level is typical, and what trips them up (idiom, inference, multi-clause sentences)?
* **Vocabulary range** — receptive vs productive. New-word acquisition rate.
* **Abstract reasoning** — can they handle hypotheticals? Conditional logic? Variables (as in algebra)?
* **Metacognition** — do they yet have meaningful "thinking about thinking" capacity? How much self-monitoring is realistic?
* **Pattern recognition** — strong or weak relative to adults?
* **Spatial reasoning** — emerging vs mature?
* **Symbolic vs concrete** — when do they need a physical referent vs when can they reason from a symbol alone?

### 2\. Psychological \& social profile

* **Self-concept** — how stable is it, how fragile is it under public failure?
* **Peer comparison sensitivity** — when does it kick in hard? Is it different by gender at this age?
* **Intrinsic vs extrinsic motivation** — what's the actual research on whether stickers/XP help or hurt long-term engagement at this age?
* **Failure tolerance** — how do 10-11 year olds typically respond to failure? What recovery/reframing works?
* **Reward sensitivity** — are they more or less responsive to variable-ratio rewards than older kids?
* **Authority relationships** — how do they relate to a teacher vs an AI system vs a parent vs peers as a source of correction?
* **Identity exploration** — what role does avatar/customization play at this age? Real or marketing fluff?
* **Emotional regulation** — capacity to handle frustration, boredom, anxiety during academic tasks
* **Social/group dynamics** — pair work, group work, solo work — what works for what?

### 3\. Evidence-based teaching methods that work for this age

Give me a **top 10 list** of teaching techniques with strong evidence specifically for 9-12 year olds. For each:

* Name + one-sentence description
* Why it works at this age (cognitive/psychological reason)
* One real citation (researcher + year, or paper title)
* A concrete example of how it would look in a classroom

Methods I'd expect to see: spaced retrieval, dual coding, worked examples, concrete-pictorial-abstract progression, story-based learning, peer explanation, productive struggle, interleaving, scaffolding, formative feedback. But don't just rubber-stamp these — tell me which are genuinely strong for this age vs which are over-hyped.

### 4\. Age-appropriate game mechanics

Give me a **top 10 list of game mechanics that genuinely work for 10-11 year olds** in educational contexts. For each:

* Mechanic name
* Why it lands for this age (cognitive/psychological reason)
* Complexity ceiling — at what point does it become too much?
* Solo / cooperative / competitive
* Reward structure
* A real-world example (commercial game or educational product)

Then a **top 5 list of game mechanics that DON'T work** for this age — and why. (e.g., open-ended sandbox with no guidance, complex strategy with deferred reward, anything that punishes failure publicly, etc.)

### 5\. Optimal session structure for this age

* **Total session length** before fatigue hits (minutes)
* **Single-task focus length** before a break is needed (minutes)
* **Break length** that actually restores attention vs derails focus
* **Daily homework load tolerance** — how much practice per day before diminishing returns?
* **Best time of day** for focused academic work (with citation if you can)
* **Re-engagement after a wrong answer** — how long to recovery?

### 6\. Difficulty calibration for this age

* What % success rate maximizes engagement vs frustration? (Flow state research — Csikszentmihalyi 70-80% may not be the right number for 10-11)
* How fast can you ramp difficulty before they disengage?
* How visible should difficulty be? (Hidden, vague, or explicit?)
* How should "failed and have to redo" be framed to avoid shame?
* What does evidence say about 60% pass thresholds vs 70% vs 80% for this age?

### 7\. Cultural \& regional context — Uzbekistan specifically

This is where most generic Western research will fall short. Find what you can on:

* **Uzbek schooling norms** — what does a typical Grade 5 day look like? Class sizes? Discipline style? Teacher-student dynamic?
* **Family/parental involvement** — is homework supervised? Who helps? Cultural attitude toward academic struggle?
* **Device access** — what's realistic? Personal phone? Shared family tablet? Computer? Internet reliability?
* **After-school time budget** — how much time does a Grade 5 student in Uzbekistan realistically have for homework outside of in-class study and chores?
* **Cultural narratives** — what stories, heroes, places resonate with 10-11 year olds in Uzbekistan? (Amir Temur, Silk Road, Registan, Navoi, Ulugh Beg — what else?)
* **Language reality** — Uzbek as primary, but how much Russian/English exposure does a typical Grade 5 student have?

### 8\. Things to AVOID for this age

A **top 10 list of things NOT to do** when designing learning experiences for 10-11 year olds, with one-sentence reasons each. Examples I'd expect: public shaming, abstract-without-concrete-grounding, unbounded sandboxes, rewards without competence signal, cultural mismatches.

\---

## Deliverable format

Single markdown file at `research-briefs/qwen-grade5-psychology-findings.md` with these sections:

```
# Grade 5 (10-11 yr) — Cognitive Profile \& Pedagogy Research

## 1. Cognitive Profile
## 2. Psychological \& Social Profile
## 3. Top 10 Effective Teaching Methods (with citations)
## 4. Top 10 Age-Appropriate Game Mechanics + Top 5 to Avoid
## 5. Optimal Session Structure (numbers)
## 6. Difficulty Calibration (numbers + framing)
## 7. Uzbekistan-Specific Cultural \& Regional Context
## 8. Top 10 Things to Avoid

## Sources
\[List of every citation, organized by section]
```

\---

## Quality bar

* **Every claim with a number must have a citation.** "Working memory capacity is 5±2 chunks" needs a source.
* **Real citations only.** Researcher + year minimum. No fabricated papers, no "studies show".
* **Specificity over volume.** I'd rather have 8 well-sourced findings than 30 vague ones.
* **Actionable, not academic.** Each finding should let me make a design decision. "10-11 year olds prefer cooperative over competitive play" → I can adjust the leaderboard rules.
* **Flag uncertainty.** If research is mixed or weak, say so. Don't pretend certainty where there isn't any.

\---

## Out of scope (do NOT do these)

* Subject-specific content (we'll handle Math vs Science vs History adjustments later, per-subject)
* Reading the textbook PDFs
* Designing actual homework sessions
* Writing UI copy or game prompts
* Comparing to higher or lower grades — Grade 5 only

\---

## When you're done

1. Save the findings file to `research-briefs/qwen-grade5-psychology-findings.md`
2. Update your dashboard entry: `status: "completed"`, `completed\_percent: 100`
3. Add a final log entry summarizing word count, number of citations, and biggest surprise / counterintuitive finding
4. Notify (the orchestrator will check periodically; the dashboard heartbeat is enough)

\---

**Go.**

