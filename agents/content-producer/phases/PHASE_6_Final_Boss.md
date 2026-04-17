### 5.6 Phase 6 -- Final Boss: Assessment Gate (5-10 min standard / 10-15 min extended)

---
## 📚 REFERENCE FILES — LOAD THESE ALONGSIDE THIS PHASE

The agent MUST load these files as additional context before generating this phase:

- standards/system/games/Game_Mechanics_Docs/21_Final-Boss/ — Boss mechanic spec
- standards/library/subject-family/{Family}/{Subject}/{Subject}_Subject_Framework.md — Boss design rules + HP overrides
---


**Purpose:** PISA-calibrated assessment that gates homework completion. The student MUST demonstrate competence at their target PISA level to pass.

**UPDATED 2026-04-07 — 3-Tier AI Boss System.** The Final Boss is no longer a single type. There are now three distinct AI Boss tiers, each serving a different pedagogical purpose. The remaining boss specification (HP system, damage tiers, failure flow, mastery stars) below applies to all three tiers unless explicitly overridden.

| Boss Tier | Trigger | Scope | Difficulty | Reward | Purpose |
|---|---|---|---|---|---|
| **Sub Boss** | End of every homework session (default) | Current lesson's content only | Calibrated to student's PISA level | Standard XP + stars | Assess mastery of current topic |
| **Big Boss** | Weekly (once per week per student, replaces that week's final Sub Boss) | ALL subjects passed up to current point, focusing on weakest 3 standards | One tier above student's current PISA level | **2× XP** + weekly badge + streak freeze if >80% | Spaced cross-subject retrieval, weak-point remediation |
| **Mythical Boss** | Random appearance, **<5% chance** per session — student cannot predict, force, or farm it | ALL subjects passed up to current point | PISA Level 5-6 regardless of student level — designed to overwhelm | **5× XP** + exclusive title + avatar frame + Hall of Fame entry | Elite challenge, aspiration driver, identifies top performers |

**Sub Boss** (the default — every homework session): Operates as documented in the rest of this section. HP, damage, hints, Socratic tutoring on failure all apply.

**Big Boss** (weekly):
- Auto-assigned once per week per student. Replaces that week's final Sub Boss.
- Cross-subject scope: AI identifies the student's 3 weakest standards across ALL subjects and builds the question set around them.
- Difficulty: one tier above the student's current PISA level in each subject (e.g., Math 1.7 → questions target PISA L2-3).
- Format: same as Sub Boss — open reasoning, no MC for Grade 5+, Socratic hints available (cost HP as usual).
- Reward: 2× XP, weekly leaderboard badge, streak freeze token if score > 80%.
- Failure: weak standards persist into next week's Big Boss until mastered.

**Mythical Boss** (random elite event):
- Trigger: <5% random chance per homework session. Student cannot predict, force, or farm. Appears as a surprise: *"⚠️ A Mythical Boss has appeared!"*
- Scope: ALL subjects passed up to the current point. Questions can span Math, Science, Biology, History — any completed content.
- Question type — one of two formats:
  1. **Real-World Case Scenario:** extremely complex problem requiring multi-subject reasoning. Example: *"A city's water supply is contaminated. Using chemistry (filtration), math (flow rate), and biology (bacterial growth), design a solution."*
  2. **Advanced Mathematical Challenge:** requires high-level equations, multi-step derivations, or cross-disciplinary math.
- Difficulty: PISA L5-6 regardless of student's current level. Designed to overwhelm. Most students will fail — that's by design.
- Hints: **ZERO**. No Socratic tutoring. **One attempt only**.
- Reward (if passed):
  - **5× normal session XP**
  - Exclusive title displayed on profile ("Mythical Slayer", "The Chosen One", etc.)
  - Permanent exclusive avatar frame (visually distinct)
  - Entry into "Mythical Hall of Fame" (opt-in, class-visible)
- If failed: NO penalty. Small participation XP. *"The Mythical Boss retreats... for now."*
- Psychological role: aspiration, social buzz, legend status. The rarity makes it legendary.

---

**The remainder of §5.6 (HP system, damage tiers, question schema, failure flow, mastery stars) applies to all three boss tiers below.**


| Parameter | Grades 1-4 | Grades 5-8 | Grades 9-11 |
|---|---|---|---|
| Boss HP | 50 HP | 100 HP | 150 HP |
| Question Types | Multiple choice + short answer | Short answer + open reasoning (no MC for 5+) | Open reasoning + extended response only |
| Hint Tax | -5 HP (boss regains) | -10 HP | -15 HP |
| Combo Bonus | 3 correct -> 2x next damage | Same | Same |
| Skippable | **NO. Zero exceptions.** | Same | Same |
| AI Tier | Tier 3 (premium -- Socratic tutoring on failure) | Same | Same |

**PISA-Tiered Damage System:**

*Resolution: Leonardo's gap analysis identified that Final Boss was inconsistently mapped to PISA Level 3-4 in one spec and Level 5-6 in another. The unified solution: Final Boss is tiered by difficulty, with each tier explicitly mapped to a PISA level.*

| Difficulty Tier | Damage | PISA Level | Bloom's Level | Example |
|---|---|---|---|---|
| Easy | -10 HP | Level 3 | Apply | "Calculate the total area of a combined shape" |
| Medium | -20 HP | Level 4 | Analyze | "Explain why method A gives a different result than method B" |
| Hard | -30 HP | Level 5-6 | Evaluate/Create | "Design a budget for a class trip to Samarkand using all constraints" |

**Question Distribution:**
```
Boss question set = {
  40% Easy (at or below student's CURRENT PISA level -- should get most right),
  40% Medium (at student's TARGET PISA level -- the real test),
  20% Hard (one level ABOVE target -- challenge bonus, not required to win)
}
```

**Every Boss Question MUST Include:**

```json
{
  "question_text": "Bozorda 1 kg olma narxi 15,000 so'm. Jasur 2.4 kg olma va 1.8 kg nok sotib oldi. Nok narxi olmadan 20% qimmat. Jasur qancha pul to'ladi?",
  "standard_ref": "UZ-MATH-5-FRAC-06",
  "textbook_ref": { "chapter": "Oddiy kasrlar", "section": "Kasrlar ustida amallar", "page": "83" },
  "pisa_level": 3,
  "pisa_domain": "mathematics",
  "pisa_content": "quantity",
  "pisa_process": "employ",
  "pisa_context": "personal",
  "transition_skill": "L2->L3: multi-step procedure with strategy selection",
  "blooms_level": "apply",
  "difficulty_tier": "medium",
  "correct_answer": "68,400 so'm",
  "scoring_rubric": {
    "full_marks": "Correct final answer with clear working",
    "partial_marks": "Correct method, arithmetic error -> 50% credit",
    "no_marks": "Random answer or no working shown"
  },
  "solution_steps": [
    "1. Olma narxi: 2.4 x 15,000 = 36,000 so'm",
    "2. Nok narxi per kg: 15,000 x 1.20 = 18,000 so'm",
    "3. Nok umumiy: 1.8 x 18,000 = 32,400 so'm",
    "4. Jami: 36,000 + 32,400 = 68,400 so'm"
  ],
  "socratic_hints": [
    "Avval 1 kg nok narxini toping. Olmadan 20% qimmat degani nima?",
    "Endi har bir mevaning umumiy narxini alohida hisoblang.",
    "Oxirgi qadam -- ikkala narxni qo'shing."
  ],
  "common_errors": [
    { "error": "54,000", "misconception": "Forgot to add 20% to pear price", "remediation_hint": "20% qimmat degani asosiy narxga 20% qo'shish kerak" }
  ]
}
```

**Buzan Injection — TEFCAS Failure Language (Method #10, #11):**

*All failure responses in Phase 6 use "Hali emas!" (Not yet!) — never "Wrong" or "Noto'g'ri."* The Socratic tutoring walks the student through TEFCAS: "Let's **Check** where the gap is → How would you **Adjust** your approach? → Now try again for **Success**."

*CUT — Decision Map was originally proposed here but moved to Phase 4 (Real-Life Challenge). Reason: the Boss is an assessment gate that tests demonstrated competence. Decision Mapping is a problem-solving scaffold. Adding scaffolding to assessment inflates scores. It belongs in Phase 4 where the student practices expert-role reasoning.*

**Failure Flow:**
```
IF boss NOT defeated (HP > 0 after all questions):
  1. IDENTIFY which learning objectives the student failed on
  2. MAP failures back to specific textbook sections and standards
  3. ACTIVATE Socratic Tutoring (Tier 3 AI) — TEFCAS framed:
     - "Hali emas! Miyangiz Feedback oldi." (Not yet! Your brain received Feedback.)
     - CHECK: "Keling, tekshiramiz — qayerda tushunmovchilik bor?" (Let's check — where's the gap?)
     - ADJUST: "Buni boshqacha yondashsangiz nima o'zgaradi?" (What changes if you approach this differently?)
     - AI asks guiding questions, NEVER gives answers
     - Routes student back to the SPECIFIC Story Mode segment they need
  4. REGENERATE boss questions (same standards, different numbers/context)
  5. Student re-attempts boss → SUCCESS

IF boss defeated:
  -> Proceed to Phase 7
  -> Calculate Mastery Stars
```

**Mastery Star Calculation:**

| Stars | Criteria | Unlocks |
|---|---|---|
| 1 Star | Boss defeated (any number of attempts) | Chapter complete |
| 2 Stars | Boss defeated in <=2 attempts, >50% HP remaining | Bonus avatar item |
| 3 Stars | Boss defeated on FIRST attempt with no hints used, >80% HP | Special badge progress |