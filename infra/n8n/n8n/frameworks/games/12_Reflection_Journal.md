# Reflection Journal (Aks Etdirish Jurnali)

> Default Mechanic #13 — Metacognitive Self-Review

**Players:** 1 | **Mode:** Solo | **Buzan Integrated** | **Bloom's:** Create | **PISA:** 3-4 | **AI Tier:** Tier 1

---

## 1. Core Game Mechanics

Reflection Journal is a **metacognitive self-review** activity that appears as the **final element of Phase 7** — the session closer. The AI generates a personalized reflection prompt based on the student's performance pattern during the session, and the student writes or records their answer.

**Session context display:**

- Before the reflection prompt, the system displays a **session summary card** showing: the subject studied, the student's performance rating (star system), total XP earned, specific topics mastered (green checkmarks), and topics that need work (yellow warnings).
- Example: "Matematika — Kasrlar | 2/3 stars | 850 XP | Kasrlarni qo'shish | Aralash kasrlar (needs work)"

**AI-generated prompt:**

- The prompt is dynamically generated based on the session's performance data. Examples:
  - *"Mashqlarda yaxshi natija ko'rsatdingiz, lekin Bossda qiynaldingiz. Boss savollari nima bilan farq qildi? Keyingi safar nimani o'zgartirasiz?"*
  - *"Bugun hamma narsa oson edi. Eng qiyin narsa nima edi? Agar siz o'qituvchi bo'lsangiz, qanday savol berardingiz?"*
  - *"Aralash kasrlar sizni qiynadi. Nima uchun qiyin bo'ldi? Qaysi qismi eng noaniq?"*
- The prompt always references specific performance data — it is never generic.

**Unique properties — the only mechanic with these rules:**

- **No timer.** The student can spend as long as they want. Reflection is not speed-dependent.
- **No grading.** There is no right or wrong answer. The AI does not evaluate the quality of the reflection.
- **No minimum quality.** Any text above the 10-character minimum is accepted. There is no "correct" reflection.
- **Skippable.** This is the **only non-mandatory phase element** in the entire NETS system. The student can click "Keyingi safar" (Next time) and proceed without writing anything. No XP penalty, no session block.
- **Privacy: content visible to student only.** Individual journal entries are never shown to teachers, parents, or other students. They are the student's private space.

**Minimum response:** 10 characters. This is an extremely low bar — it exists only to prevent accidental submissions, not to enforce quality. The "Tugatdim" (Done) button remains disabled until 10 characters are typed.

**Grade range:** All grades where Phase 7 appears. No additional grade gating beyond the session structure itself.

---

## 2. Tier-Based Access Control

Reflection Journal is available to all tiers as a core Phase 7 element. Premium adds prompt sophistication, historical tracking, and export features.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Phase 7 (session closer) — always available | Same + optional mid-session reflection checkpoints for long sessions |
| **Prompt Generation** | Template-based prompts selected from a pool based on performance pattern (good/struggled/perfect) | LLM-generated personalized prompts referencing specific answers, mistakes, and breakthrough moments |
| **Journal History** | Student can view their own past entries (text only, chronological list) | Visual journal timeline with mood indicators, topic heat maps, and search functionality |
| **Export** | Not available | Student can export their journal as a PDF portfolio for self-review or (voluntarily) sharing with a teacher |
| **Voice Input** | Text only | Text or voice recording — students who prefer speaking to writing can record their reflection |
| **Theme Detection** | Not available | AI identifies recurring themes across journal entries (e.g., "Student frequently mentions difficulty with fractions") and surfaces them in the teacher dashboard as aggregate themes |
| **Teaser Message** | Generic next-session preview ("Keyingi dars: yangi mavzu!") | Personalized teaser based on session performance ("Keyingi dars: kasrlarni ko'paytirish — siz qo'shishni yaxshi bajardingiz, endi ko'paytirishni sinab ko'ring!") |

> **Basic Tier Guarantee:** The core reflection experience is identical for both tiers — the student sees their session summary, receives a performance-based prompt, and writes their reflection. Premium adds prompt sophistication, voice input, and historical analytics. The metacognitive benefit is available to all.

---

## 3. Buzan Integration: Self-Generated Mental Maps

Reflection Journal implements **Tony Buzan's Self-Reflection and Associative Integration** principles by requiring students to consciously examine their own learning process.

- **Color Hooks (Performance Encoding):** The session summary card uses the same color system as the rest of NETS — green checkmarks for mastered topics, yellow warnings for areas needing work. When the reflection prompt appears, it is displayed with a left-border accent in indigo (the color of introspection). Per Buzan, consistent color associations help the brain quickly categorize information — green means "done well," yellow means "needs attention," indigo means "think about this."
- **Radiant Branches (Connecting Session to Self):** The reflection prompt asks the student to connect the session's external events (scores, mistakes, successes) to their internal experience (confusion, confidence, strategy). This creates a radiant structure: the session is the central node, and the student's reflections branch outward to emotions, strategies, and future plans. Buzan emphasizes that self-generated connections are stronger than externally imposed ones — the student who writes "I struggled with mixed fractions because I forgot the common denominator step" has created a personal knowledge link that no teacher-provided summary could match.
- **Imagery Through Personal Narrative:** The journal entry becomes a personal narrative artifact. Over time, the student builds a collection of self-reflections that tell the story of their learning journey. Buzan emphasizes that personal meaning is the strongest memory anchor — a student who writes about their frustration with Boss questions and their satisfaction with finally understanding will remember that session far better than a student who simply sees a score.
- **Metacognition as Memory Tool:** The act of reflecting on "what was hardest and why" forces the student to retrieve and re-examine their own cognitive experience during the session. This retrieval is itself a memory-strengthening event. Buzan's principle of review and self-testing applies here: the student who reflects on their learning is implicitly reviewing the material while simultaneously building metacognitive awareness.

---

## 4. Question Styles & Interaction Mechanics

Reflection Journal presents an AI-generated prompt based on session performance, and the student writes a free-text response. There is no evaluation layer — any response meeting the 10-character minimum is accepted. The prompt complexity scales with the student's demonstrated PISA level.

| PISA Level | Prompt Style | Prompt Examples | Cognitive Target | Response Expectation |
|-----------|-------------|----------------|-----------------|---------------------|
| **L1-L2** | Simple self-assessment | "Bugun nima o'rgandingiz?" (What did you learn today?)<br>"Eng qiziqarli narsa nima edi?" (What was the most interesting thing?) | Basic self-awareness — identify what was learned | Simple statement of fact or preference. Any coherent sentence is sufficient. |
| **L3** | Process reflection | "Qaysi mashq eng oson edi? Nima uchun?" (Which exercise was easiest? Why?)<br>"Nima uchun Bossda qiynaldingiz?" (Why did you struggle on the Boss?) | Causal self-analysis — connect outcomes to personal factors | At least one causal statement ("because...") linking a session event to a personal factor. |
| **L4** | Strategy evaluation | "Boss savollari nima bilan farq qildi?" (How were the Boss questions different?)<br>"Keyingi safar nimani o'zgartirasiz?" (What will you change next time?) | Strategic metacognition — evaluate one's own approach and plan adjustments | Identification of a difference or strategy + a forward-looking intention. |
| **L5-L6** | Meta-level reasoning | "Agar siz o'qituvchi bo'lsangiz, qanday savol berardingiz?" (If you were the teacher, what question would you ask?)<br>"Bugungi dars sizning fikrlashingizni qanday o'zgartirdi?" (How did today's lesson change your thinking?) | Epistemic reflection — examine how one's own understanding has shifted | Recognition of a cognitive shift or a novel question demonstrating perspective-taking. |

> **Privacy Architecture:** Individual journal entries are stored encrypted and visible only to the student. The teacher dashboard shows **aggregate themes only** — for example, "This week, 60% of students mentioned difficulty with fractions in their reflections" — but never "Student X wrote that they don't understand fractions." The student's private thoughts about their own learning are protected. This is a deliberate design choice: metacognition requires honesty, and honesty requires safety.

---

## 5. Victory Conditions & Scoring

### A. Standard Completion

The student writes at least 10 characters and clicks "Tugatdim" (Done):

- **No XP reward.** Reflection Journal does not award XP. This is the only mechanic in NETS with zero XP value. The rationale: metacognition is intrinsically motivated — attaching XP would externalize the motivation and reduce the authenticity of the reflection.
- **"Hali emas" framing does not apply.** There is no failure state. The student who skips the journal experiences no penalty — the session simply proceeds to the next step.

### B. Skip Condition (Unique)

The student clicks "Keyingi safar" (Next time):

- **No penalty.** The session continues normally. The skip is recorded internally (for the student's own history) but does not affect XP, session completion status, or teacher reports.
- **Encouraging message:** "Mayli! Keyingi safar yozasiz" (That's okay! You'll write next time). The message is warm and non-judgmental — the system never shames a student for skipping reflection.

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Journal entry submitted (10+ characters) | 0 | No XP — intrinsic motivation only |
| Journal entry skipped | 0 | No penalty — session continues |
| Premium: Voice recording submitted | 0 | Same as text — no XP difference for input mode |

### D. Completion Tracking

- **Student-facing:** The student can see their own journal history — a chronological list of their past entries (text only in Basic; with visual analytics in Premium). This serves as a personal learning diary.
- **Teacher-facing:** The teacher dashboard shows **aggregate theme analysis** across all students' journal entries — not individual entries. Example themes: "Difficulty with fractions (mentioned by 45% of students this week)," "Boss anxiety (mentioned by 30%)," "High confidence in story-based learning (mentioned by 60%)." This gives teachers actionable intelligence without violating student privacy.
- **Session gating:** Reflection Journal is skippable — it does NOT block session completion. A student can skip the journal and the session is still counted as complete. This is unique: every other Phase 7 element (if any) is mandatory.

### E. Teaser Message (Post-Reflection)

After submission or skip, the system shows a brief teaser for the next session:

- **Basic:** "Keyingi dars: yangi mavzu!" (Next lesson: a new topic!)
- **Premium:** Personalized teaser referencing session performance — "Keyingi dars: Kasrlarni ko'paytirish — siz qo'shishni yaxshi bajardingiz, endi ko'paytirishni sinab ko'ring!" (Next lesson: Multiplying fractions — you did well with addition, now try multiplication!)

> **Research basis:** Metacognition (Flavell, 1979) demonstrates that students who reflect on their own learning processes show +20-30% better performance than those who do not. The Reflection Journal operationalizes this by making metacognition a structured, session-closing ritual. The decision to award zero XP is intentional — research on intrinsic vs. extrinsic motivation (Deci, 1971; Kohn, 1993) shows that attaching rewards to reflective activities can undermine their authenticity. The journal must remain a genuine space for self-examination, not a points-collecting exercise.

---

*NETS Elite Mechanic Specification — Reflection Journal (Aks Etdirish Jurnali) v1.0*
