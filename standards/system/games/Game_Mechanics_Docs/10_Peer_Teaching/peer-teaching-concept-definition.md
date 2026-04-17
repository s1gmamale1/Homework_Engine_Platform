# Peer Teaching (O'rgatuvchi bo'ling!)

> Default Mechanic #12 — Protege Effect Teaching Simulation

**Players:** 1 | **Mode:** Solo + AI Evaluation | **Buzan Integrated** | **Bloom's:** Evaluate | **PISA:** 4-5 | **AI Tier:** Tier 1

---

## 1. Core Game Mechanics

Peer Teaching places the student in the role of **teacher explaining a concept to a hypothetical classmate**. The AI evaluates the explanation across three dimensions: completeness, clarity, and accuracy.

**Three scenario types:**

- **Scenario A — "Tushuntiring" (Explain from scratch):** A fictional student (e.g., "Hamza, 4-sinf") asks a genuine question about a concept they don't understand. The teaching student must explain the concept from the ground up, as if to a beginner. Example: "1/2 nima degani? Nima uchun tepada va pastda raqam bor?"
- **Scenario B — "Yordam bering" (Help someone stuck):** A fictional student is stuck on a problem or has started solving it but is confused. The teaching student must diagnose the confusion and provide targeted guidance. Example: "2/3 + 1/4 = 3/7 deb hisobladim. Nima uchun bu xato?"
- **Scenario C — "Xatoni toping" (Correct a wrong answer):** A fictional student has given a wrong answer and the teaching student must identify what went wrong and explain why it's incorrect. Example: "1/2 + 1/3 = 2/5 dedim. O'qituvchi xato dedi. Nima noto'g'ri?"

**Evaluation criteria (AI-scored, three dimensions):**

- **Completeness (To'liqlik) — up to +100 XP:** Does the explanation cover all essential elements of the concept? Are key terms defined? Are steps not skipped?
- **Clarity (Aniqlik) — up to +100 XP:** Is the explanation well-structured? Does it use appropriate language for the target student's grade? Are examples or analogies provided?
- **Accuracy (To'g'rilik) — up to +200 XP:** Is the content factually correct? Are there misconceptions or errors in the explanation? This dimension carries the highest weight because accuracy is the most critical teaching quality.

**Grade range:** Grades 5-11 only. The mechanic requires sufficient metacognitive maturity to explain concepts to others. Below Grade 5, students are still developing their own understanding and cannot reliably teach.

**Subject coverage:** All subject families — Matematika, Biologiya, Tarix, Ingliz tili, Fizika, Kimyo, and any future additions. The scenario library is topic-specific and aligned to the current lesson content.

**Minimum response:** 20 characters. The system rejects responses below this threshold with a prompt to write more.

---

## 2. Tier-Based Access Control

Peer Teaching is available to all tiers during Phase 3 sessions. Premium adds scenario variety, evaluation depth, and teaching tools.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 (Game Break rotation) | Same + on-demand access from Library for extra practice |
| **Scenario Variety** | 3 scenarios per subject (9 total across 3 subjects shown) | 6+ scenarios per subject (18+ total), refreshed weekly |
| **Evaluation Engine** | Keyword-based matching against predefined answer criteria | LLM-powered holistic evaluation — assesses reasoning quality, not just keyword presence |
| **Feedback Detail** | 3-level feedback (low/medium/high) with generic encouragement messages | Personalized feedback — identifies specific strengths and gaps in the explanation |
| **Scenario Types** | All three types (A, B, C) available | All three + Scenario D: "Debate Defense" — defend a position against a fictional opponent's counterarguments |
| **Retry System** | One attempt per scenario per session | Unlimited retries within a session — each retry generates a fresh evaluation |
| **XP Reward** | Standard (max 400 XP per scenario) | Standard + +100 XP bonus for "Master Teacher" (all three dimensions at maximum) |

> **Basic Tier Guarantee:** The core teaching experience is identical for both tiers — the student reads a scenario, writes an explanation, and receives three-dimensional scoring. Premium adds evaluation sophistication, more scenarios, and a fourth scenario type. The Protege Effect benefit is available to all.

---

## 3. Buzan Integration: Teaching as Radiant Organization

Peer Teaching implements **Tony Buzan's Hierarchical Order and Association** principles by requiring students to organize knowledge for transmission to another mind.

- **Color Hooks (Three-Dimension Encoding):** Each evaluation dimension has a signature color displayed in the results bar: Completeness = indigo (structure), Clarity = gold (illumination), Accuracy = green (correctness). When the results appear, each bar animates in its color, creating a visual triad that the student can quickly scan. Per Buzan, color-coded categories help the brain organize feedback into distinct cognitive buckets — the student immediately knows whether their weakness was in coverage, communication, or correctness.
- **Radiant Branches (Explanation Structure):** A good explanation radiates from a central concept outward to examples, applications, and connections. The AI evaluation implicitly assesses whether the student's explanation follows this radiant structure — starting from the core concept, branching to supporting details, then connecting to broader knowledge. Students who write linear, single-point explanations score lower on Clarity than those who build branching explanatory structures.
- **Imagery Through Character Personas:** Each scenario features a fictional student with a name, grade, and avatar emoji (e.g., "Hamza (4-sinf)" with a boy emoji). These personas create an emotional anchor — the teaching student is not writing to an abstract grader but to "Hamza," a real-seeming peer who needs help. Buzan emphasizes that personal, emotional connections strengthen memory encoding. The avatar and persona make the teaching act feel socially meaningful, not academically abstract.
- **The Protege Effect as Self-Teaching:** The core mechanism — explaining a concept to someone else — forces the student to reorganize their own knowledge into a coherent structure. Buzan's Radiant Thinking describes exactly this process: knowledge becomes stronger when it is re-expressed from a new angle (the teacher's perspective). The student who can explain fractions to "Hamza" has a deeper understanding than the student who can only solve fraction problems.

---

## 4. Question Styles & Interaction Mechanics

Peer Teaching presents a scenario (a fictional student's question or mistake) and the teaching student writes a free-text explanation. The AI evaluates across three dimensions using keyword matching and structural analysis.

| PISA Level | Scenario Type | Scenario Prompt Style | Acceptance Criteria (AI Evaluation) | Cognitive Target |
|-----------|--------------|----------------------|-----------------------------------|-----------------|
| **L1-L3** | colspan="4" style="text-align:center;" | Peer Teaching does not operate below L4 — students need sufficient conceptual mastery before they can teach. Minimum entry is L4. | N/A |
| **L4** | Scenario A (Explain) or B (Help stuck) | A fictional student asks a direct question about a process or principle. The teaching student must explain the full mechanism. | Completeness: 2+ key concepts mentioned. Clarity: structured explanation (not just keywords). Accuracy: no factual errors in the explanation. | Process analysis — explain how and why a system works |
| **L5** | Scenario B (Help stuck) or C (Correct wrong) | A fictional student has made a reasoning error or partial attempt. The teaching student must diagnose the error and explain the correct approach. | Completeness: identifies the error AND provides the correction. Clarity: uses the fictional student's framing (meets them where they are). Accuracy: correction is fully correct. | Evaluation — diagnose reasoning errors and construct corrections |
| **L6** | Scenario C (Correct wrong) or D (Debate — Premium) | A fictional student has proposed a sophisticated but flawed argument. Or a fictional opponent challenges the student's position. | Completeness: addresses all dimensions of the error/challenge. Clarity: builds a structured counterargument. Accuracy: demonstrates mastery of competing theories. | Synthesis — construct novel arguments from first principles, evaluate competing frameworks |

> **Teacher Flag System:** When the AI scores Accuracy at 0/200 (the explanation contains significant factual errors), a "Teacher Warning" flag appears: "O'qituvchi tekshiradi" (Teacher will review). This signals that the student's explanation contains misconceptions that require human teacher intervention. The flag is visible to the teacher dashboard and triggers a notification. This is the only mechanic where the AI can escalate to a human reviewer.

---

## 5. Victory Conditions & Scoring

### A. Standard Scoring

Every submitted explanation receives three-dimensional scoring:

- **Completeness (To'liqlik):** +0 to +100 XP — based on coverage of essential concepts.
- **Clarity (Aniqlik):** +0 to +100 XP — based on structure, language appropriateness, and use of examples.
- **Accuracy (To'g'rilik):** +0 to +200 XP — based on factual correctness of the explanation.
- **Maximum total: +400 XP per scenario.**

### B. Score Levels and Feedback

| Accuracy Score | Feedback Message | Teacher Flag |
|---------------|-----------------|--------------|
| **0 / 200** | "Urinish uchun rahmat! Ko'proq tafsilot qo'shishga harakat qiling." | ⚠️ "O'qituvchi tekshiradi" — explanation contains significant errors |
| **100 / 200** | "Ajoyib! Siz asosiy tushunchalarni yaxshi tushuntiryapsiz." | None — partial accuracy, encouragement to refine |
| **200 / 200** | "Mukammal! Siz haqiqiy o'qituvchisiz!" | None — full mastery demonstrated |

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Completeness (low) | +40 | Minimal coverage — some concepts mentioned |
| Completeness (medium) | +60 | Partial coverage — most concepts addressed |
| Completeness (full) | +100 | All essential concepts covered |
| Clarity (low) | +60 | Basic structure — keywords only, no examples |
| Clarity (medium) | +80 | Good structure — some examples, grade-appropriate |
| Clarity (full) | +100 | Excellent structure — analogies, examples, clear language |
| Accuracy (wrong) | +0 | Significant factual errors — teacher flag triggered |
| Accuracy (partial) | +100 | Mostly correct — minor errors or gaps |
| Accuracy (full) | +200 | Fully correct explanation |
| Premium: Master Teacher | +100 bonus | All three dimensions at maximum (100 + 100 + 200 = 400 base + 100 bonus = 500 total) |
| Retry (Basic) | N/A | One attempt per session — no retry in Basic |
| Retry (Premium) | Re-evaluated | Unlimited retries — each attempt scored independently |

### D. Maximum Possible XP

- **Basic Tier (per scenario):** 100 + 100 + 200 = **400 XP**
- **Premium Tier (per scenario, Master Teacher):** 400 + 100 bonus = **500 XP**

> **Research basis:** The Protege Effect (Chase et al., 2009) demonstrates that students who teach material to others show +25% better retention than students who study for themselves. The three-dimensional scoring reflects this: Accuracy (the most heavily weighted dimension) ensures the student actually understands the content; Completeness ensures they can articulate the full picture; Clarity ensures they can communicate it effectively. The teacher flag system adds a safety net — misconceptions caught by the AI are escalated for human review.

---

*NETS Elite Mechanic Specification — Peer Teaching (O'rgatuvchi bo'ling!) v1.0*
