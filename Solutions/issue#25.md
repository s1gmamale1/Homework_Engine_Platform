# Issue: Content can feel raw/generated

## 1. What is the issue?

* Location: Preview panels, Origin, Industry Application, Real-Life/Mission, Reflection, and other major generated sections.
* Affects: Student engagement, gamified learning feel, content quality, and trust.
* Student result: Student feels they are reading AI-generated text instead of moving through a learning activity.
* Teacher/product result: Homework looks polished visually but still feels like a document, not an interactive learning experience.

## 2. How is it happening?

* Current mechanic: The system outputs `panels`, `pages`, and `blocks`, which creates a document/magazine layout.
* Current prompt behavior: Prompts ask the AI to describe topics through sections like “Concept Explanation,” “Origin,” and “Industry Application.”
* Current flow behavior: Many phases ask the student to read first and act later.
* Missing requirement: No required field for “what the student does here” and no assembly-time check that learning events actually happen.

## 3. Why was it used originally?

* Original purpose: Convert textbook content into clear structured homework.
* What it solved: Fast content generation, consistent layout, easier frontend rendering.
* What is still valuable: The phase structure is useful and should stay.
* What no longer works: Better writing alone does not make the homework feel gamified. The passive document shape remains.

## 4. Issue type and severity

* Type: Content quality / learning-flow design.
* Severity: P0 Rework.
* Evidence level: High — Issue 25 is listed as “Content can feel raw/generated,” with the proposed need to reduce raw AI-style output. 

## 5. Solution options

### Option A

* Pros: Add a six-element checklist to every major section: hook, conflict, choice, mistake, visual, payoff.
* Cons: Can create fake engagement props and make every panel bloated.

### Option B

* Pros: Rewrite content as learning events using prediction-before-explanation, one Mistake-First slot, and session-level event validation.
* Cons: Requires prompt and schema/validator changes.

### Option C

* Pros: Keep current structure and add a rewrite/naturalness pass.
* Cons: Improves wording but does not fix the passive document shape.

## 6. Recommended solution

* Why this solution: Option B fixes the root cause: the system should stage student actions, not only write about topics.
* Better than alternatives because: It changes the content shape from document → event, instead of decorating the same document.
* Existing pieces we can reuse: Current Preview panels, Memory Sprint event logic, game phases, answer-checker feedback, and session assembly.
* Real-life reference/pattern: Learning games work because the student predicts, chooses, fixes, explains, and commits — not because they read better paragraphs.

## 7. Implementation concept

* How it should work:

  1. Add **prediction-before-explanation** to every Preview prompt.
  2. Add **one Mistake-First Moment** per Preview using real misconception data where possible.
  3. Add a **session-level completeness validator** checking that event types appear across the full homework.
* Where it belongs: Preview prompts, assembly validator, and later schema design.
* What needs to change:

  * Add event-style fields such as `student_action`, `expected_response`, `feedback`, and `reveal`.
  * Add validator rule: across the session, each event type appears at least 2 times: `predict`, `choose`, `fix`, `explain`, `commit`.
* What stays: Current phase arc and subject-specific learning goals.

## 8. Risks

* Possible downside: If overused, predictions and mistake moments can feel forced.
* How to reduce it: Do not force every panel to include all engagement elements. Use session-level validation instead of per-panel checklist.

## 9. Success criteria

* We know it worked when: The homework no longer feels like “AI text with games added.” Each major phase has a clear student action, feedback, and payoff, so students feel something is happening in their head.
