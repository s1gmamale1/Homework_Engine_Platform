### 5.4 Phase 4 -- Real-Life Challenge: Transfer Application (3-5 min standard / 10 min extended)


**Purpose:** Force transfer -- apply textbook knowledge to a real-world scenario. This is the core skill PISA measures.

**UPDATED 2026-04-07 — First-Person Expert POV is mandatory.** All four AI demos used third-person scenarios ("Tomir's plant is dying", "Salimjon is in his garage"). Students were observers, not decision-makers. Every Real-Life Challenge must now put the student in the role of THE EXPERT who must solve a real case.

| Element | Requirement |
|---|---|
| **POV** | Direct address: "You are..." / "Your job is..." / "A client comes to you..." Never third-person. |
| **Role** | Student is positioned as a professional — project manager, analyst, engineer, consultant, business owner, researcher — NOT as a student answering a textbook question. Roles must feel modern and aspirational, not folksy or patronizing. |
| **Case** | A realistic professional scenario that could plausibly occur in a modern workplace, business, or research setting. Avoid cliché bazaar/village/folksy scenarios — students should feel like they're solving real problems, not acting in a school play. |
| **Tricky Questions** | Multiple-path questions with plausible wrong answers (distractors that look right to a novice). Forces real reasoning, not pattern matching. |
| **Explanation Required** | Student must justify their choice. AI evaluates the reasoning, not just the choice. ("What would you do AND why?") |
| **Subject Integration** | All reasoning must use concepts from the current lesson. No outside knowledge required. |

**Examples:**

> ❌ OLD (Kimyo / Combustion): *"Salimjon's garage has petrol. Should he light the stove?"*
> ✅ NEW: *"You are a fire safety inspector called to a workshop. The owner stores gasoline, uses a wood-burning stove, and keeps an asbestos fire blanket in the corner. He asks: 'Is my setup safe?' You look around and immediately spot 3 problems. What are they, and what do you tell the owner?"*

> ❌ OLD (Algebra / Linear Functions): *"A taxi charges 2000 + 1500 per km. Calculate the cost for 5 km."*
> ✅ NEW: *"You run a delivery startup. You're comparing two vehicle leasing plans for your fleet. Plan A: 2,000,000 so'm/month base + 1,500 so'm/km. Plan B: 3,000,000 so'm/month base + 1,000 so'm/km. Your drivers average 120 km/day. Which plan saves more money over a month? A partner says Plan B is always better — is that true? Show your analysis."*

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 3-5 minutes | 10 minutes |
| Scenario count | 1 scenario, 2-3 sub-questions | 1 scenario, 3-5 sub-questions |
| Context | Modern professional context — business, tech, infrastructure, research. Uzbek setting when natural, but never forced-folksy. | Same |
| AI Tier | Tier 2 (AI-generated, expert-reviewed) | Same |

**Buzan Injection — W5H Radiant Problem Solving Scaffold:**

Before the answer area opens, a 6-branch frame appears: **Who / What / Where / When / Why / How** radiating from the problem statement. The student fills at least 4 of 6 branches with brief notes (1-2 words each), forcing structured decomposition before writing. The frame stays visible as a sidebar reference while answering.

- **G5-6:** Mandatory, 4 of 6 branches minimum
- **G7-8:** Default ON, toggleable off, 5 of 6 branches
- **G9+:** Available via "Tahlil" (Analyze) button, not forced

The W5H frame itself is NOT scored — it's scaffolding. The student's final answer (which benefits from the structured thinking) is scored per the existing rubric.

*Where this does NOT apply:* Math-only Real-Life Challenges where the scenario is purely computational (e.g., "calculate the cost"). W5H works for scenarios requiring reasoning about multiple factors — Science investigations, History cause-effect, Geography resource decisions. It adds unnecessary friction to pure calculation tasks.

| Subject | W5H Scaffold Useful? | Why |
|---|---|---|
| Science | YES | Multi-factor investigations (fire safety, ecosystem analysis) |
| History | YES | Cause-effect reasoning (why did X happen?) |
| Geography | YES | Resource/location decisions with trade-offs |
| Math | SOMETIMES | Only for word problems with multiple factors, not pure calculation |
| Tarbiya | YES | Moral dilemmas have multiple stakeholders (Who matters here) |
| Tasviriy Sanat | NO | Creative challenges don't decompose into W5H |
| Language | NO | Text comprehension doesn't need spatial decomposition |

**Buzan Injection — Decision Mapping Scaffold (Method #5):**

For Real-Life Challenges that involve choosing between competing options (not single-answer problems), the W5H frame is extended with a **Decision Map**: two options radiate from the central problem, each with pro/con sub-branches. Student completes missing branches, assigns weights (1-5), selects their choice, and writes a 1-2 sentence justification.

Decision Mapping is a PROBLEM-SOLVING scaffold — it belongs here in Phase 4, not in the Boss (Phase 6). The Boss is an assessment gate that tests demonstrated competence. Adding scaffolding to assessment would inflate scores artificially.

- **Where it works:** Geography (two locations for a park — weigh cost vs access), Science (two experimental designs — weigh accuracy vs feasibility), History (two leadership strategies — weigh short vs long term), Tarbiya (moral dilemmas with competing values)
- **Where it does NOT work:** Math (has correct answers, not trade-offs), Language (grammar/comprehension doesn't involve decision trade-offs), Tasviriy Sanat (creative, not analytical)
- **Not every RLC needs it.** Only scenarios with genuine trade-offs between 2+ options. Single-answer expert scenarios (e.g., "spot the 3 fire safety problems") use W5H alone.

**National Pride Injection — "Wise Status" (30% of Phase 4 tasks):**

For approximately 1 in 3 Real-Life Challenges, the existing expert-role framing (§5.4) is enhanced with the "Wise Status" recipe:

1. **Status:** Professional title — "Bosh Muhandis," "Strategik Tahlilchi," "Laboratoriya Rahbari" — not generic praise.
2. **Arena (55/45):** National: anchor in real Uzbek achievement ("Afrosiyob tezyurar poyezdlari 250km/s aniqlikda ishlaydi"). Global: anchor in global standard ("CERN ning Katta Adron Kollayderi fizika chegaralarini kengaytirmoqda").
3. **Bridge:** Connect the textbook question to the arena. Academic core (formula, calculation, reasoning) is UNTOUCHED.
4. **Closing:** "Sizning aniqligingiz Uchinchi Renessansni quradi" (national) or "Sizning natijangiz global standartlarga mos" (global).

Source templates: `task_injections.json`. The 70% of Phase 4 tasks that don't get Wise Status play exactly as the existing spec defines — first-person expert POV, no heritage framing.

| Minimum PISA level | Level 2+ (below L2: replaced with extra Apply-level Adaptive Quiz) | Same |

**Scenario Structure:**

```json
{
  "title": "Toshkent bozorida mevalar",
  "context_narrative": "Toshkent bozorida Alisher onasiga yordam bermoqda. Ular 3/4 kg olma, 1/2 kg nok va 2/3 kg uzum sotib olishdi.",
  "textbook_refs": [
    { "standard": "UZ-MATH-5-FRAC-06", "connection": "operations with fractions" }
  ],
  "sub_questions": [
    {
      "question": "Jami necha kilogramm meva sotib olishdi?",
      "pisa_level": 3,
      "blooms": "apply",
      "pisa_process": "employ",
      "transition_skill": "L2->L3: multi-step procedure with unlike denominators",
      "correct_answer": "23/12 = 1 11/12 kg",
      "scoring_rubric": "Full marks: correct LCD + addition. Partial: correct method, arithmetic error."
    },
    {
      "question": "Agar sumkaga 2 kg sig'sa, bir sumka yetadimi? Nima uchun?",
      "pisa_level": 4,
      "blooms": "evaluate",
      "pisa_process": "interpret",
      "transition_skill": "L3->L4: interpret result in real-world context",
      "correct_answer": "Ha, yetadi. 1 11/12 < 2.",
      "scoring_rubric": "Full marks: correct comparison + reasoning. Partial: correct answer without explanation."
    }
  ]
}
```

*Source: Structure from original spec; Bazaar scenario from HOMEWORK_TASK_ENGINE.md Task 4. Cultural context confirmed by textbook analysis (Uzbek sum currency, bazaar settings, character names like Alisher, Malika, Sardor found in actual Grade 5 textbook).*