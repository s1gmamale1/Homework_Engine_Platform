# Issue: Origin panels are repetitive

## 1. What is the issue?

* Location: Origin / Discovery panels in Preview.
* Affects: Biology, Physics, Math/Algebra, Chemistry, and any subject with “who discovered this?” style content.
* Student result: Students see the same biography pattern again and again, so Origin feels boring and skippable.
* Teacher/product result: The section looks like filler instead of helping the lesson.

## 2. How is it happening?

* Current mechanic: Origin is treated as a fixed panel.
* Current prompt behavior: The AI is asked to explain who discovered/described the concept.
* Current flow behavior: Origin appears even when it does not create a useful learning event.
* Missing requirement: No rule to decide whether Origin should be full, brief, skipped, or staged through a useful story archetype.

## 3. Why was it used originally?

* Original purpose: Make textbook concepts feel more human, memorable, and connected to discovery.
* What it solved: Added historical context and made abstract concepts feel less random.
* What is still valuable: Origin is useful when it explains why the concept was needed, disputed, discovered, or changed later thinking.
* What no longer works: A mandatory “scientist biography” format becomes repetitive and document-like.

## 4. Issue type and severity

* Type: Content quality / repetition / weak storytelling.
* Severity: P1 Readjust.
* Evidence level: Medium-high — Issue 26 directly identifies repetitive Origin panels and proposes origin archetypes instead of fixed biographies. 

## 5. Solution options

### Option A

* Pros: Keep Origin panel but make it shorter.
* Cons: Shorter biography is still biography. Repetition remains.

### Option B

* Pros: Replace fixed biographies with conditional Origin modes: full archetype story, brief origin note, or skip.
* Cons: Requires prompt logic and source-confidence rules.

### Option C

* Pros: Remove Origin panels completely.
* Cons: Loses useful context when the origin genuinely helps understanding.

## 6. Recommended solution

* Why this solution: Option B keeps the valuable part of Origin but removes the repetitive format.
* Better than alternatives because: It changes Origin from “describe a discoverer” into “stage why this idea mattered,” while still allowing skip when Origin adds no learning value.
* Existing pieces we can reuse: Current Origin panel location inside Preview.
* Real-life reference/pattern: Good educational stories usually start from a problem, failure, conflict, accident, debate, or surprising discovery — not a résumé.

## 7. Implementation concept

* How it should work:

  * Before generating Origin, choose an Origin mode:

    * `full`
    * `brief`
    * `skip`

  * If `full`, choose one source-supported archetype:

    * `rivalry`
    * `failure`
    * `accident`
    * `debate`
    * `rediscovery`
    * `hidden_figure`

  * Then stage the Origin as a short learning event:

    * What was confusing before?
    * What happened?
    * What changed after?
    * What should the student notice, predict, or check?

* Where it belongs: Preview prompt, especially Origin / Discovery panel.

* What needs to change:

  * Add an `origin_mode` field.
  * Add an `origin_archetype` field.
  * Add `source_confidence`.
  * Add “brief note” and “skip” as valid outputs.
  * Add rule: Origin must support the lesson objective.
  * Add rule: Origin archetype must be supported by textbook/source content or common verified scientific/history knowledge.

* What stays: Origin remains available when it improves understanding.

Example schema:

```json
{
  "origin_mode": "full | brief | skip",
  "origin_archetype": "rivalry | failure | accident | debate | rediscovery | hidden_figure | none",
  "source_confidence": "high | medium | low"
}
```

## 8. Risks

* Possible downside: AI may force a dramatic story where none exists.
* How to reduce it: If source confidence is low or Origin does not help the concept, use `brief` or `skip` instead of inventing a story.

## 9. Success criteria

* We know it worked when: Origin panels stop sounding like repeated biographies and instead explain why the concept became necessary, surprising, disputed, rediscovered, or useful — or they are skipped when they do not help learning.
