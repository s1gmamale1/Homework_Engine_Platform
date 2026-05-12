# Issue: Content can feel raw/generated

## 1. What is the issue?

* Location: Case-Based Preview, Flashcard Learning, Quizlet-Style Test / Memory Check, Practice Arc, Boss Arena, Reflection, and other major generated sections.
* Affects: Student engagement, gamified learning feel, content quality, and trust.
* Student result: Student feels they are reading AI-generated text instead of moving through a learning activity.
* Teacher/product result: Homework looks polished visually but still feels like a document, not an interactive learning experience.

## 2. How is it happening?

* Current mechanic: The system outputs `panels`, `pages`, and `blocks`, which creates a document/magazine layout.
* Current prompt behavior: Prompts ask the AI to describe topics through sections like "Concept Explanation," "Origin," and "Industry Application."
* Current flow behavior: Many sections ask the student to read first and act later.
* Missing requirement: No required field for "what the student does here" and no assembly-time check that learning events actually happen.

## 3. Why was it used originally?

* Original purpose: Convert textbook content into clear structured homework.
* What it solved: Fast content generation, consistent layout, easier frontend rendering.
* What is still valuable: The section structure is useful and should stay.
* What no longer works: Better writing alone does not make the homework feel gamified. The passive document shape remains.

## 4. Issue type and severity

* Type: Content quality / learning-flow design.
* Severity: P0 Rework.
* Evidence level: High — Issue 25 is listed as "Content can feel raw/generated," with the proposed need to reduce raw AI-style output.

## 5. Solution options

### Option A

* Pros: Add a six-element checklist to every major section: hook, conflict, choice, mistake, visual, payoff.
* Cons: Can create fake engagement props and make every section bloated.

### Option B

* Pros: Rewrite content as learning events using prediction-before-explanation, one Mistake-First slot, and session-level event validation.
* Cons: Requires prompt and schema/validator changes.

### Option C

* Pros: Keep current structure and add a rewrite/naturalness pass.
* Cons: Improves wording but does not fix the passive document shape.

## 6. Recommended solution

* Why this solution: Option B fixes the root cause: the system should stage student actions, not only write about topics.
* Better than alternatives because: It changes the content shape from document → event, instead of decorating the same document.
* Existing pieces we can reuse: Current Case-Based Preview, Memory Check event logic, Practice Arc games, answer-checker feedback, and session assembly.
* Real-life reference/pattern: Learning games work because the student predicts, chooses, fixes, explains, and commits — not because they read better paragraphs.

## 7. Implementation concept

* How it should work:

  1. Add **prediction-before-explanation** to every Case-Based Preview prompt: before introducing each new concept, the student must predict, match, or commit to an answer first. The explanation follows the prediction, not the other way around.
  2. Add **one Mistake-First Moment** per Case-Based Preview using real misconception data where possible.
  3. Add a **session-level completeness validator** checking that event types appear across the full homework.

* Where it belongs: Case-Based Preview prompts, assembly validator, and later schema design.

* What needs to change:

  * Add event-style fields such as `student_action`, `expected_response`, `feedback`, and `reveal`.
  * Add Mistake-First placement rule.
  * Add session-level event-type minimum.
  * Add forbidden patterns block.

* What stays: Current flow arc (Learning Sections → Unlock Gate → Practice Arc → Boss Arena → Reflection) and subject-specific learning goals.

### Mistake-First placement rule

The Mistake-First Moment sits between the opening Hook / Mission Question and the formal explanation in Case-Based Preview. Fixed position. Not scattered, not optional.

Reason: the student commits to or rejects the wrong idea before reading the textbook version, so the formal explanation reads as resolution of a tension they already feel — not as raw exposition.

Structure of the Mistake-First Moment:

1. State a common wrong belief students hold — as a peer's quote or "Ko'p o'quvchilar shunday o'ylaydi: ..."
2. Show *why* it feels right (the intuition behind it).
3. Reveal what actually happens.
4. Name why the wrong idea breaks.

### Session-level event-type minimum

Validator rule: across the session, each of the 5 event types appears at least 2 times.

* `predict` (e.g., "qaysi biri kattaroq o'sadi?")
* `choose` (e.g., select from 2-4 options)
* `fix` (e.g., correct a wrong answer, diagram, or sentence)
* `explain` (e.g., "nima uchun?" requiring 1+ sentence)
* `commit` (e.g., type or draw an answer before reveal)

If any type appears fewer than 2 times across the full session, assembly fails and the session must be regenerated.

### Forbidden patterns

Auto-reject at generation:

* Definition-first openings: "X — bu Y..." / "X — Y jarayoni" / "X deganda Y tushuniladi"
* Three consecutive declarative sentences with no question, prediction, or visual
* "Sodda so'zlar bilan" layer that paraphrases layer 1 instead of giving a new angle
* Sections with no second-person verb (`belgilang`, `taxmin qiling`, `tanlang`, `yozing`) in the first 150 words
* Any section where removing all student-action fields leaves the section still complete (means no action was integral)

## 8. Risks

* Possible downside: If overused, predictions and mistake moments can feel forced.
* How to reduce it: Do not force every section to include all engagement elements. Use session-level validation instead of per-section checklist. Mistake-First has exactly one slot per Case-Based Preview, in a fixed position.

## 9. Success criteria

* We know it worked when: The homework no longer feels like "AI text with games added." Each major section has a clear student action, feedback, and payoff, so students feel something is happening in their head.
* Quantitative: across 10 random sample sessions per subject, all 5 event types appear ≥2 times in every session, and zero sessions trigger any forbidden pattern at assembly.
