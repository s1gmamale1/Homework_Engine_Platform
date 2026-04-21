### 5.2 Phase 2 -- Story Mode: Concept Delivery (5-7 min standard / 10 min extended)

---
## 📚 REFERENCE FILES — LOAD THESE ALONGSIDE THIS PHASE

The agent MUST load these files as additional context before generating this phase:

- standards/library/subject-family/{Family}/{Subject}/{Subject}_Subject_Framework.md — Story Mode arc table
- standards/system/narrative/quotes_database.json — Cultural references
---


**Purpose:** Deliver new textbook content in an engaging narrative format. Build conceptual understanding before practice.

**UPDATED 2026-04-07 — Story Arc Mandatory.** All four AI demos produced textbook paragraphs with checkpoint questions and called it "narrative". The original spec used the word *narrative* but never defined what makes something a story vs. exposition. Story Mode now requires a complete story arc.

**Required Story Arc Structure (every Story Mode segment):**

| Beat | Requirement |
|---|---|
| **Problem** | Opens with a genuine problem or mystery that the content will solve. NOT "Today we'll learn about..." but "In 1774, a priest named Priestley heated a red powder and something impossible happened..." |
| **Struggle** | The character/scientist tries familiar approaches and they fail. The student feels the tension. |
| **Discovery** | The new concept is introduced as the missing tool that breaks the deadlock. This is where the textbook content lands. |
| **Solution** | The character applies the concept and the situation resolves. The student doesn't end a segment hanging — they get the answer, but they EARNED it by following the logic. |

**CRITICAL — Blueprint vs Output:** The four beats above (Problem → Struggle → Discovery → Solution) are **INGREDIENTS for building ONE story** — NOT an output format, NOT section headers, NOT segments. You write ONE continuous flowing story where these beats happen naturally within the narrative. The student-facing output must be a **single, cohesive story** — like a short story in a book. 

**Do NOT:**
- Insert beat labels ("Muammo:", "Kurash:", "Kashfiyot:", "Yechim:") into the text
- Divide the story into 3 labeled segments or sections
- Write "Segment 1: Concrete", "Segment 2: Pictorial", etc.
- Break the narrative into separate chunks with headers between them

**DO:** Write one flowing story where a character faces a problem, struggles with it, discovers the concept, and solves it. Then ask comprehension questions. That's it. If you can see ANY structural labels, segments, or beat markers in the output — you did it wrong.

**Real-World Examples Preferred:** If the concept has a real historical discovery, real-world event, or documented case study — use that as the spine. Invented scenarios are a fallback, not the default.

**IELTS-Style Comprehension on Checkpoints:** Story Mode checkpoints test comprehension, not fact recall. Approved checkpoint question types:
- Main idea identification
- Inference ("What can we conclude from...?")
- Compare information across segments
- Identify the author's/character's purpose
- Vocabulary in context

> ✅ "Why did Priestley's experiment change chemistry?" (comprehension)
> ❌ "What is the formula of oxygen?" (fact recall — belongs in Memory Sprint)

This builds Reading PISA levels alongside subject content.

**Stranger Test (Quality Gate):** Before deployment, every Story Mode segment must pass the Stranger Test:

> *If a person who has never seen this textbook content can follow the segment and answer the checkpoint question using only the narrative logic (not prior knowledge), it passes. If it requires the reader to already know the content, it fails.*

Segments that fail the Stranger Test are returned to the content pipeline for rewrite.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 5-7 minutes | ~10 minutes |
| Story | **ONE continuous flowing story** covering the chapter's core concept. NOT segmented. NOT labeled. The 4-beat arc (Problem→Struggle→Discovery→Solution) is baked INTO the story invisibly. For Math: CPA progression (Concrete→Pictorial→Abstract) is woven into the narrative naturally. | Same, longer |
| Checkpoints | **3 comprehension questions AFTER the story** (or at natural pause points within the narrative). IELTS-style: main idea, inference, compare, purpose, vocabulary in context. Student must answer to proceed. | 3-5 checkpoints |
| Source | Textbook chapter/topic -- refined into learning script | Same |
| CPA staging (Maths) | Concrete -> Pictorial -> Abstract — woven into the story, NOT as labeled sections | Same |
| AI Tier | Tier 1 (pre-generated) for content; Tier 2 for dynamic adaptation | Same |

**Content Structure (per story, NOT per segment — the story is ONE piece):**

```json
{
  "textbook_ref": { "chapter": "Oddiy kasrlar", "section": "Teng kasrlar", "page_range": "52-58" },
  "standard_ref": "UZ-MATH-5-FRAC-04",
  "narrative_text": "...",
  "media": [
    { "type": "image", "url": "...", "alt": "Bar model showing 2/4 = 1/2" },
    { "type": "video_clip", "url": "...", "duration": 45 }
  ],
  "cpa_stage": "pictorial",
  "checkpoint": {
    "question": "Rasmga qarang. 2/4 va 1/2 nima uchun teng?",
    "correct_answer": "Chunki ikkalasi ham yarimni bildiradi",
    "blooms_level": "understand",
    "pisa_level": 2,
    "transition_skill": "L1->L2: interpret simple visual representations",
    "explanation_on_wrong": "Bar modelga qarang -- har ikkala kasrda ham yarimga teng qism bo'yalgan..."
  }
}
```

**Rules:**
- Student CANNOT skip ahead without answering the checkpoint correctly
- On wrong checkpoint answer: show explanation referencing the textbook section, then re-ask
- Maximum 2 retries per checkpoint. After 2 failures: simplified version of the question
- Story mode tracks time-per-segment to detect disengagement (<30 seconds = flagged as skimming)

**Buzan Injection — 80/20 Keyword Tagging (Method #22):**

Every narrative segment must have its `keywords_80_20` extracted (the ~20% of words carrying ~80% of meaning). These keywords feed Phase 5 Radiant Summary branches, Flash Card fronts, and Memory Sprint items. This is a content pipeline requirement, not a student-facing feature.

*CUT — Focus Guide, Forward Momentum Rule, Semantic Chunking, and Typography optimization (Methods #16, #17, #18, #19, #20, #21, #23) are moved to a standalone "Future: Reading Fluency Module" (see end of this document). Reason: G5 students' bottleneck is COMPREHENSION, not speed. Rayner et al. (2016) found speed reading training does not improve comprehension — it teaches skimming. Pushing G5 students (Lexile 830-1010L) to read faster would actively harm understanding. Regression is a legitimate comprehension strategy, not a bad habit, at this developmental stage. These methods may be appropriate for G9+ once reading fluency is established.*

**Grade-Level Narrative Framework:**

*Source: HOMEWORK_STANDARDS.md Section 2.3. Uzbek cultural narratives.*

| Grade | Semester Narrative | Cultural Elements |
|---|---|---|
| 3 | "The Young Explorer of Samarkand" | Registan, Silk Road, traditional crafts |
| 4 | "The Silk Road Expedition" | Caravans, trade, cultural exchange |
| 5 | "The Cotton Harvest Challenge" | Agriculture, family work, rural life |
| 6 | "Building the Registan" | Architecture, mathematics in design |
| 7 | "The Amir Temur Campaign" | History, strategy, leadership |
| 8 | "Modern Tashkent" | Urban life, technology, progress |
| 9-11 | Subject-specific narratives | Professional applications |

**Subject-Specific Adaptations:**

| Subject | Story Mode Approach | Source Layer |
|---|---|---|
| Mathematics | CPA staging: manipulate objects -> draw models -> write equations | Textbook (confirmed CPA in Grade 5 Math 2024) |
| Science | Present phenomenon -> predict -> reveal results -> explain | National standards |
| Literature | Read excerpt -> contextualize author/period -> discuss themes | Textbook |
| English/Russian | Immersive content in target language with L1 support available | Textbook + PISA |
| History | Narrative with primary source excerpts -> cause/effect framing | Textbook |

**National Pride Injection — Ambient Setting Tag:** Each `narrative_segment` is tagged `setting_origin: "national" | "global"`. Rolling 55/45 balance across sessions (not per-session — a single session on Uzbek History can be 100% national). Don't force global settings on inherently Uzbek topics or national settings on inherently global ones. The balance is a yearly guideline, not a per-session mandate.