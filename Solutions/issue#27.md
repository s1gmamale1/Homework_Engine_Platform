# Issue: Uzbek context can feel forced

## 1. What is the issue?

* Location: Preview, Origin, Industry Application, Real-Life/Mission, Why This Matters, and subject-specific examples.
* Affects: All subjects, especially History, Biology, Physics, Math/Algebra, English, and Origin panels.
* Student result: Students notice Uzbek names, places, or references that feel pasted in instead of useful.
* Teacher/product result: Content looks quota-filled and AI-generated, even when the explanation is technically correct.

## 2. How is it happening?

* Current mechanic: Some prompts use a fixed national/local context expectation, such as a 55/45 national/global ratio.
* Current prompt behavior: The AI tries to satisfy “Uzbek context” by adding names, places, scholars, or local settings.
* Current flow behavior: Local context appears even when it does not change the task, answer, reasoning, or student action.
* Missing requirement: No strict gate that asks whether the local context actually affects the learning task.

## 3. Why was it used originally?

* Original purpose: Make homework feel relevant to Uzbek public-school students.
* What it solved: Prevented content from feeling fully foreign or disconnected from the student’s environment.
* What is still valuable: Local context is useful when it makes the concept easier to imagine, calculate, compare, remember, or reason about.
* What no longer works: A fixed ratio turns Uzbek context into a quota. The model adds decoration to comply.

## 4. Issue type and severity

* Type: Content quality / cultural relevance / prompt logic.
* Severity: P0 Readjust.
* Evidence level: High — Issue 27 identifies that Uzbek context can feel forced and proposes using local context only when it naturally improves understanding. 

## 5. Solution options

### Option A

* Pros: Keep the current local-context ratio.
* Cons: Forced references continue because the model must hit a quota.

### Option B

* Pros: Lower the ratio, for example from 55/45 to 30/70.
* Cons: Still keeps the quota problem. The model will still add local references when they are not needed.

### Option C

* Pros: Remove the ratio entirely and replace it with a relevance gate: the swap test.
* Cons: Requires prompt changes and output testing.

## 6. Recommended solution

* Why this solution: Option C directly fixes the root cause. The problem is not local context itself; the problem is quota-driven local context.
* Better than alternatives because: It keeps Uzbek relevance when useful, but removes decorative name/place insertion.
* Existing pieces we can reuse: Current local-context rules, Milliylik idea, subject examples, Origin guardrails from Issue 26.
* Real-life reference/pattern: Good localization changes the task or understanding. Bad localization only swaps names or places.

## 7. Implementation concept

* How it should work:

  * Drop the 55/45 ratio and do not replace it with another ratio.

  * Add the **swap test** as the main gate:

    ```text
    If you can swap the Uzbek name/place for a generic name/place without changing the cognitive task, remove the Uzbek reference.
    ```

  * Allow Uzbek/local context only in three cases:

    * **Units, currency, or measurements** affect the task, such as so‘m, local distances, or familiar quantities.
    * **Geography affects the answer**, such as climate, terrain, region, water, agriculture, or language environment.
    * **Cultural assumption changes the reasoning**, such as mahalla structure, school context, food ingredients, family/community roles, or local practice.

  * Forbid decorative Uzbek scholar attribution in Origin panels unless there is a documented source.

* Where it belongs: All subject prompts, especially Preview, Origin, Industry Application, Real-Life/Mission, and Why This Matters.

* What needs to change:

  * Remove fixed national/global percentage requirements.
  * Add the swap test to every relevant prompt.
  * Add the three allowed local-context cases.
  * Add a forbidden pattern rule for undocumented Uzbek scholar references.
  * Add output checks for decorative local context.

* What stays:

  * Uzbek/local context stays when it improves understanding.
  * Uzbek public-school relevance stays as the product goal.
  * Textbook fidelity stays the main source rule.

## 8. Risks

* Possible downside: The model may still add Uzbek context under uncertainty because it was previously encouraged to do so.
* How to reduce it: Test sample outputs after the change. If local references still appear often without passing the swap test, strengthen the rule: “Default to neutral context unless one of the three allowed cases applies.”

## 9. Success criteria

* We know it worked when:

  * Decorative name swaps disappear.
  * Forced IT Park, Samarkand, Bukhara, Chorsu, Yashil Makon, or similar settings disappear unless they affect the task.
  * Uzbek scholar references in Origin panels are source-supported or removed.
  * Local context appears only when it changes what the student observes, calculates, compares, decides, or remembers.
