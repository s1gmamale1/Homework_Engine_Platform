# Issue: Industry Application is often generic

## 1. What is the issue?

* Location: Industry Application panels and professional-use sections.
* Affects: Biology, Physics, Math/Algebra, Chemistry, English, and other subjects that try to show “real-world use.”
* Student result: Students read vague claims like “engineers use this” or “doctors need this,” but they do not see how the concept actually helps someone do a task.
* Teacher/product result: The section feels decorative and AI-generated instead of useful for learning.

## 2. How is it happening?

* Current mechanic: Industry Application is treated as a relevance paragraph.
* Current prompt behavior: The AI is asked to mention where professionals use the concept.
* Current flow behavior: The section names a job or field, but often does not create a decision, mistake, constraint, or student action.
* Missing requirement: No rule that the professional context must require the lesson concept to make a decision.

## 3. Why was it used originally?

* Original purpose: Show students that the school topic matters outside the classroom.
* What it solved: Added real-world relevance and career connection.
* What is still valuable: Professional context is useful when it shows why the concept changes a real task.
* What no longer works: Generic career claims do not create understanding or interactivity.

## 4. Issue type and severity

* Type: Content quality / real-world relevance / weak application.
* Severity: P1 Readjust.
* Evidence level: Medium-high — Issue 28 identifies that Industry Application is often generic and proposes concrete professional vignettes with role, task, stakes, mistake consequence, and concept link. 

## 5. Solution options

### Option A

* Pros: Keep current Industry Application paragraphs.
* Cons: Generic claims continue, and the section remains passive.

### Option B

* Pros: Convert Industry Application into short professional decision vignettes.
* Cons: Requires stronger prompt rules and a skip option.

### Option C

* Pros: Remove Industry Application entirely.
* Cons: Loses useful career/relevance connection when the concept genuinely supports a professional task.

## 6. Recommended solution

* Why this solution: Option B fixes the root cause by changing Industry Application from profession-name based to task-based.
* Better than alternatives because: It shows the student how the concept changes what someone does, instead of simply saying the topic is “important.”
* Existing pieces we can reuse: Current Industry Application panel, Real-Life/Mission logic, and student-action patterns from interactive phases.
* Real-life reference/pattern: Real professional relevance appears when a person must choose, diagnose, verify, compare, or explain using the lesson concept.

## 7. Implementation concept

* How it should work:

  * Industry Application should become a **professional decision vignette**, not a generic paragraph.

  * Each vignette must include:

    * specific role;
    * concrete task;
    * constraint or stakes;
    * mistake consequence;
    * concept link;
    * student action.

  * The student action must be one of:

    * choose;
    * diagnose;
    * verify;
    * compare;
    * interpret;
    * explain.

  * Add this hard pass test:

    ```text
    The vignette passes only if it stops working when the lesson concept is removed.
    If the decision can be made without the concept, the vignette is decoration.
    ```

  * Add a skip clause:

    ```text
    If no honest professional decision exists for this concept, skip Industry Application. Do not invent one.
    ```

  * Topics that may skip:

    * pure naming chapters;
    * basic arithmetic;
    * purely definitional content;
    * topics where a professional context would be fake or too advanced.

* Where it belongs: Preview prompts, Industry Application panels, and Real-Life/Mission generation rules.

* What needs to change:

  * Replace “explain where professionals use this concept” with:

    ```text
    Stage one short professional decision where the student must use the lesson concept to choose, diagnose, verify, compare, interpret, or explain.
    ```

  * Add a forbidden pattern:

    ```text
    Do not write “X kasbida muhim” or “Y sohada ishlatiladi” unless the next sentence gives a concrete task.
    ```

  * Add length cap:

    ```text
    2–4 sentences setup + 1 decision prompt.
    ```

* What stays:

  * Industry Application remains when it creates real learning value.
  * Career relevance remains part of the homework.
  * Short professional context is still allowed when it supports the concept.

## 8. Risks

* Possible downside: The model may force a professional scenario even when the concept does not need one.
* How to reduce it: Make `skip` a valid output and require the “concept removal” test. If the task still works without the lesson concept, remove or regenerate the vignette.

## 9. Success criteria

* We know it worked when:

  * Industry Application no longer says only “this is useful in medicine/engineering/technology.”
  * Each kept vignette has a real professional task and student decision.
  * The vignette becomes impossible or weaker if the lesson concept is removed.
  * Fake professional contexts are skipped instead of invented.
