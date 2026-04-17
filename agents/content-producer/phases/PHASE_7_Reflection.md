### 5.7 Phase 7 -- Battle Replay: Reflection (2-3 minutes)

---
## 📚 REFERENCE FILES — LOAD THESE ALONGSIDE THIS PHASE

The agent MUST load these files as additional context before generating this phase:

- standards/library/subject-family/{Family}/{Subject}/{Subject}_Subject_Framework.md — "Phase 7 Reflection Guide" section
- standards/system/narrative/quotes_database.json — Closing line / Third Renaissance lines
---


**Purpose:** Build metacognitive awareness. Students who reflect on their thinking improve 20-30% on subsequent assessments.

| Parameter | Value |
|---|---|
| Duration | 2-3 minutes |
| AI Tier | Tier 1 (template-based) |
| Privacy | Student-only (teacher sees summary themes only) |

**AI Prompt Generation (TEFCAS-framed):**
```
IF accuracy >= 80%:
  -> "Bugungi eng yaxshi Trial (urinish) qaysi edi? Qaysi strategiya Success ga olib keldi?"
     (What was your best Trial today? What strategy led to Success?)
IF accuracy 60-79%:
  -> "Miyangiz qanday Feedback oldi? Keyingi safar nimani Adjust qilasiz?"
     (What Feedback did your brain receive? What will you Adjust next time?)
IF accuracy < 60%:
  -> "Har bir Trial miyangizni kuchaytiryapti. Bitta kichik Adjust tanlang — nima qilasiz boshqacha?"
     (Every Trial strengthens your brain. Pick one small Adjust — what will you do differently?)

IF hesitation detected on concept X:
  -> "[X] savoli qiyin bo'ldi. Miyangiz qanday Feedback oldi?"
     ([X] question was hard. What Feedback did your brain get?)

IF streak >= 5:
  -> "[X] ta ketma-ket to'g'ri! Supernovangiz porlayapti — qaysi strategiya ishladi?"
     ([X] correct in a row! Your Supernova is glowing — what strategy worked?)
```

**Buzan Injection — Recency Effect + BOST Goal Recall:**

Phase 7 exploits the Recency Effect — the last thing in a session sticks. TEFCAS vocabulary makes the reflection feel like a deliberate learning step, not a chore.

At the end of every Phase 7, regardless of performance, resurface the BOST learning goal from Phase 0-A: *"Eslatma: Bugun siz '[stored_learning_goal]' ni bilmoqchi edingiz. Bildingizmi?"* (Remember: Today you wanted to learn '[goal]'. Did you figure it out?). Student responds: Yes / Partially / Not yet.

*Where TEFCAS language is unnecessary in Phase 7:* The performance summary data (total questions, correct, hints) stays as-is. TEFCAS framing applies only to the reflection PROMPTS, not to the raw statistics.

**National Pride Injection — Closing Line (≥60% accuracy sessions only):** After TEFCAS prompts and BOST goal recall, one closing line connects today's learning to contribution. 55/45 national/global: *"Sizning bilimingiz Uchinchi Renessansning poydevoridir"* (national) or *"Sizning aniq fikrlashingiz global standartlarga mos keladi"* (global). For sessions below 60% accuracy, skip pride framing — use TEFCAS encouragement instead ("Har bir urinish miyangizni kuchaytiryapti").

**Structure:**

```json
{
  "performance_summary": {
    "total_questions": 8,
    "correct": 6,
    "incorrect": 2,
    "hints_used": 1,
    "time_spent": "12:34",
    "hardest_question": { "standard": "UZ-MATH-5-FRAC-04", "blooms": "analyze" },
    "hesitation_points": ["question_3", "question_7"],
    "answer_changes": ["question_5"]
  },
  "reflection_prompts": [
    "Qaysi savol eng qiyin bo'ldi? Nima uchun?",
    "Keyingi safar nimani boshqacha qilgan bo'lar edingiz?",
    "Bugungi darsdan eng muhim narsa nima edi?"
  ],
  "student_writes": "...",
  "standards_mastered": ["UZ-MATH-5-FRAC-01", "UZ-MATH-5-FRAC-04"],
  "standards_needs_work": ["UZ-MATH-5-FRAC-06"]
}
```

**Response Requirements:**
- Minimum 10 characters (2 sentences for Extended Mode)
- No auto-grade (all valid responses accepted)
- Teacher dashboard shows aggregate themes, not individual entries

---

