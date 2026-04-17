# Notebook Capture

> Default Mechanic #16 — Handwritten Work AI-Evaluated Against Rubric

**Players:** 1 | **Mode:** Solo — Analog-to-Digital Bridge | **Buzan Integrated** | **Bloom's:** Apply / Analyze / Create | **PISA:** 2-5

---

## 1. Core Game Mechanics

The student **does the work by hand** — derivations, diagrams, sketches, proofs, calculations — on physical paper in their notebook. They then **photograph their work** using the device camera. An **AI vision model evaluates the submission** against a structured rubric and returns annotated feedback within **8-10 seconds**.

**End-to-end flow:**

1. **Prompt appears:** The system presents the task — e.g., "Derive the quadratic formula step by step," "Draw and label the water cycle," "Sketch the graph of y = 2x² - 4x + 1 and identify the vertex."
2. **Student works on paper:** The student completes the task by hand in their notebook. No time limit on the working phase (but the session timer continues).
3. **Client-side pre-validation:** When the student taps "Submit Photo," the device runs 3 quick checks before sending:
   - **Focus check:** Is the image sharp enough? (Laplacian variance threshold.) Blurry → prompt to retake.
   - **Page detection:** Is there a clear rectangular page/region in frame? No page detected → prompt to adjust angle.
   - **Lighting check:** Is brightness adequate and even? Too dark or blown out → prompt for better lighting.
4. **AI Vision evaluation (Tier 3 model):** The validated image is sent to the AI vision pipeline. The model evaluates against the task rubric within **8-10 seconds**.
5. **Results returned:** The student receives:
   - **Overall score** (percentage or rubric level)
   - **Partial credit breakdown** — which rubric criteria were met, which were partial, which were missed
   - **Specific feedback with annotations** — the AI overlays marks directly on the student's photo: green checkmarks on correct steps, yellow circles on partial/incomplete steps, red X marks on errors, with text explanations for each annotation

**Scheduling:** Notebook Capture appears approximately **1 in every 3-4 sessions** for students in **Grade 5 and above**. It is used in **Phase 3** (during a game break slot, as the "heavy cognitive lift" mechanic), **Phase 4** (as the primary assessment tool for complex tasks), or **Phase 6** (as the capstone demonstration of accumulated mastery).

**Grade scaling:**

- **Grades 5-6:** Tasks at PISA L2-L3. Rubric has 3 criteria. AI is lenient on handwriting quality — focuses on conceptual correctness. Tasks: label diagrams, show one-step calculations, draw basic shapes.
- **Grades 7-8:** Tasks at PISA L3-L4. Rubric has 4 criteria. AI evaluates logical flow of multi-step work. Tasks: derive formulas, sketch function graphs with labels, explain processes in writing.
- **Grades 9-10:** Tasks at PISA L4-L5. Rubric has 5 criteria. AI evaluates argument structure, evidence quality, and completeness. Tasks: multi-step proofs, data analysis with hand-drawn charts, essay outlines.
- **Grade 11:** Tasks at PISA L5+. Rubric has 5+ criteria. AI evaluates synthesis, originality, and rigor. Tasks: full derivations from first principles, system diagrams, critical analysis with evidence.

---

## 2. Tier-Based Access Control

Both tiers receive Notebook Capture as part of the 28-mechanic core. Premium unlocks enhanced evaluation depth and portfolio features.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3, 4, or 6 (1 in 3-4 sessions, G5+) | Same + on-demand "Practice Capture" from Library (up to 2/week) |
| **AI Vision Model** | Tier 3 standard model — evaluates against rubric, returns score + annotations | Tier 3 enhanced model — same + "what if" suggestions (e.g., "If you had used method X instead, step 3 would be simpler") |
| **Rubric Depth** | 3-5 criteria per task (grade-appropriate) | Up to 7 criteria for advanced tasks (e.g., separate scoring for creativity, elegance, rigor) |
| **Annotation Detail** | Green/yellow/red marks + brief text per annotation | Same + color-coded marginal notes, step-by-step alternative solutions overlaid on student's work |
| **Portfolio** | Last 5 captures saved to profile | Unlimited portfolio with timeline view, improvement trajectory graph, and "best work" showcase gallery |
| **Resubmission** | 1 resubmission allowed per task (same session) | 2 resubmissions allowed per task + "learn from feedback" guided mode that walks through each annotation |
| **Export** | Not available | Export annotated captures as PDF (shareable with teachers or parents) |

> **Basic Tier Guarantee:** During Phase 3/4/6 sessions, Basic students receive the full AI evaluation experience — the same rubric, the same 8-10 second turnaround, the same annotated feedback. Premium adds portfolio depth, alternative-solution suggestions, and export capabilities — these are enrichment and documentation tools, not required for PISA progression.

---

## 3. Buzan Integration: Embodied Creation & Color-Coded Mastery

Notebook Capture is the **most Buzan-aligned mechanic in the entire NETS system** — it directly implements the Generation Effect and Embodied Cognition principles at its core.

- **Generation Effect (Slamecka & Graf, 1978):** Students who *produce* information (writing, drawing, deriving by hand) retain it 25-40% better than students who only recognize or select it digitally. Notebook Capture forces generation — the student cannot tap, drag, or select. They must *create*. The physical act of forming letters, drawing lines, and structuring work on paper encodes knowledge in motor memory that screens cannot replicate. Expected retention gain: **+25-40% vs. digital input**.
- **Embodied Cognition (Kiefer & Trumpp, 2012):** Cognitive processing is grounded in the body's sensorimotor systems. The hand-eye coordination of writing equations, sketching diagrams, and laying out proofs on paper activates neural pathways that touchscreen taps do not. The spatial layout of a page (top-to-bottom derivations, left-to-right diagrams) creates a physical "memory palace" on the paper itself — students often remember "it was in the top-right corner of my page."
- **Color Hooks (AI Annotation Overlay):** The AI's annotations use a strict color system that maps to Buzan's radiant thinking: **Green checkmarks** = correct steps (positive reinforcement, color anchors "this is right"), **Yellow circles** = partial or incomplete (the "almost" color — signals there's more here, a branch not fully grown), **Red X marks** = errors (not punishment — diagnostic, always paired with a "here's why" text note). When the annotated photo appears, the colors bloom outward from each mark (0.4s animation), making the feedback visually radiant and emotionally salient.
- **Imagery & Personal Ownership:** Every Notebook Capture is *the student's own handwriting* — their personal visual identity. Unlike typed text, handwriting is uniquely idiosyncratic, making each submission a **personal artifact**. The system preserves the student's handwriting style in their portfolio, creating a visible record of their intellectual growth over time. Students who review their old captures often remark "I can't believe I wrote that" — a powerful metacognitive moment.

---

## 4. Question Styles & Interaction Mechanics

Notebook Capture does not use traditional "questions" — it uses **open-ended production tasks**. The student must create, derive, or explain by hand. Task complexity scales with PISA level.

| PISA Level | Task Style | Interaction Flow | Cognitive Target | Example |
|-----------|-----------|-----------------|-----------------|---------|
| **L2** | Direct production — follow a template | Task shown → student works on paper → photo → AI evaluates against 3-criterion rubric → annotated results in 8-10s | Apply — reproduce a known procedure or diagram | "Draw a triangle and label its base, height, and three angles. Write the formula for its area." |
| **L3** | Guided derivation — show your steps | Same flow, rubric has 4 criteria including logical flow and step completeness | Apply/Analyze — execute multi-step process with reasoning | "Show that the sum of interior angles of a pentagon is 540°. Draw it and explain your reasoning." |
| **L4** | Analysis task — interpret and represent | Same flow, task may include data or a scenario the student must analyze and represent visually | Analyze — break down information, identify patterns, represent findings | "Here is a table of monthly rainfall data. Draw a bar chart, identify the trend, and explain what it suggests about the climate." |
| **L5** | Open synthesis — create an argument or proof | Same flow, rubric has 5+ criteria including originality, evidence quality, and logical coherence. Evaluation may take the full 10 seconds. | Create/Synthesize — construct novel argument, proof, or model from principles | "Prove that √2 is irrational using a proof by contradiction. Write the full argument with clear logical steps." |

> **Anti-Cheating Measures:** The client-side pre-validation (focus, page detection, lighting) prevents low-effort submissions. Additionally, the AI model detects: (1) printed text vs. handwritten text (printed submissions are flagged and rejected), (2) photos of screens (detects pixel grid patterns), (3) previously-submitted images (perceptual hashing — same photo submitted twice triggers a "show new work" prompt). These safeguards ensure the Generation Effect is preserved — the student must actually do the work.

---

## 5. Victory Conditions & Scoring

### A. Rubric-Based Scoring

Each Notebook Capture task is evaluated against a rubric with 3-7 criteria (depending on grade and tier). The AI returns a score for each criterion:

- **Met (green):** Criterion fully satisfied. Full points awarded.
- **Partial (yellow):** Criterion partially satisfied — correct elements present but incomplete or with minor errors. Half points awarded.
- **Not Met (red):** Criterion not satisfied — missing, incorrect, or fundamentally flawed. Zero points for this criterion.

### B. Outcome Tiers

| Outcome | Score Range | Framing | Consequence |
|---------|------------|---------|-------------|
| **Masterpiece** | 90-100% | "Bu a'lo!" (Excellent!) + confetti + saved to portfolio as "Best Work" candidate | Full XP + bonus + mastery badge for the session |
| **Strong Work** | 70-89% | "Yaxshi!" (Good!) + annotations show specific areas for refinement | Full XP for met criteria + half XP for partial criteria |
| **Developing** | 50-69% | "Hali emas" (Not yet) + detailed annotations guide what to fix | XP for met criteria only. Resubmission offered (1 attempt Basic, 2 Premium). |
| **Needs Revision** | Below 50% | "Hali emas" (Not yet) + full annotation overlay showing every gap. Encouraging diagnostic framing. | Minimal XP. Must redo in Duolingo Mode (task broken into micro-steps). No resubmission in same session — requires separate practice session. |

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Each "Met" criterion | +100 | Full points per rubric criterion satisfied |
| Each "Partial" criterion | +50 | Half credit — recognizes effort and partial correctness |
| Masterpiece (90-100%) | +200 bonus | On top of criterion XP — "Bu a'lo!" recognition |
| Strong Work (70-89%) | +100 bonus | On top of criterion XP — "Yaxshi!" recognition |
| First Capture of the week | +50 | Encourages regular analog work habits |
| Improvement bonus | +25 to +100 | If score is higher than student's previous capture, bonus scales with improvement delta |
| Portfolio milestone (5 captures) | +150 | "Archivist" achievement — 5 annotated works saved |
| Portfolio milestone (20 captures) | +300 | "Scholar's Archive" — gold-tier achievement |
| Resubmission improvement | +50 per upgraded criterion | Each criterion that moves from Partial→Met or Not Met→Partial on resubmission |

### D. Defeat Framing & "Hali Emas" Philosophy

Notebook Capture is designed so that **there is no true failure — only diagnostic feedback.** Even a "Needs Revision" result provides actionable annotations. The "Hali emas" (Not yet) message is central:

- The annotated photo shows the student's *actual work* — not a generic solution. Every green checkmark validates what they did right. Every red X explains specifically what went wrong.
- The AI never says "wrong" — it says "this step has an issue" and explains why. This preserves the student's intellectual dignity while delivering honest assessment.
- Students who score below 50% enter Duolingo Mode for that specific task — the work is broken into micro-steps that can be practiced digitally. After Duolingo Mode clearance, the student may re-attempt the Notebook Capture in a future session.
- The student's annotated photo is *always saved to their profile*, even on low scores. This creates a visible record of growth — a student who revisits a "Needs Revision" capture from 3 months ago and compares it to a "Masterpiece" from today experiences a powerful mastery narrative.

---

*NETS Elite Mechanic Specification — Notebook Capture v1.0*
