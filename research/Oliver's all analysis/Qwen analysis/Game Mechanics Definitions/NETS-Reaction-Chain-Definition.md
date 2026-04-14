# NETS Game Mechanic Definition: Reaction Chain

**Mechanic ID:** `reaction_chain`
**Catalog:** Interactive Catalog Pool (Catalog #5)
**Version:** 1.0
**Date:** 2026-04-11
**Author:** ReactionChainResearcher (Paperclip agent d54914cd)
**Status:** Draft — pending content-ops review

---

## Design Decisions (Pre-Definition)

Before the full spec, four design questions require explicit decisions with rationale.

### Decision 1 — Visual Representation

**Options considered:** (A) Linear node chain with numbered nodes lighting up sequentially, (B) Falling dominoes, (C) Content-adaptive process diagram (photosynthesis arrows, historical timeline)

**Decision: Linear node chain as the base; content-adaptive skin per content type.**

The **chain metaphor is the constant** — 6-10 circular nodes connected by horizontal lines, lighting up left-to-right as the student progresses. The *skin* adapts to content:

| Content type | Visual skin | Example |
|---|---|---|
| Biological process | Molecule-and-arrow flow | Photosynthesis: H₂O → Chlorophyll → Glucose → O₂ → ATP (each node labeled) |
| Historical sequence | Timeline with event flags | Conquest: Migration → Trade post → Conflict → Treaty → Empire |
| Mathematical procedure | Step-ladder with notation | Equation: Given → Substitute → Simplify → Solve → Verify |
| Algorithm / procedure | Flowchart arrows | Boiling water: Fill pot → Place on heat → Watch → Remove at 100°C |
| Default (no clear process) | Abstract glowing beads on a chain | 8 vocabulary nodes, thematically connected |

This approach keeps the mechanic recognizable (same game loop across all subjects) while making the nodes semantically meaningful. Content authors specify the `chain_skin` in the input schema.

**Rationale:** Falling dominoes don't map to processes that have branching or bidirectional content (history has "what caused X?", not just "what came after X?"). Content-specific process diagrams require bespoke rendering per topic — too expensive to maintain at scale. The adaptive skin approach reuses one renderer with a style parameter.

---

### Decision 2 — Chain Break Behavior

**Options considered:** (A) Chain resets to node 1 (zero progress), session continues; (B) Session ends immediately; (C) Chain breaks but student jumps back only N nodes

**Decision: Chain resets to node 1 (restart from scratch); session continues. Maximum 3 breaks allowed before the whole game attempt is marked failed.**

- **A single break does NOT end the session.** The session exits only after 3 cumulative chain breaks OR successful chain completion, whichever comes first.
- On break: a "chain shatter" animation plays (particles burst from the break point), then all nodes go dark, then the student sees: *"Zanjir uzildi! Qaytadan boshlang."* ("Chain broken! Start again.") — no lecture, no shame, 2-second pause then auto-restart.
- **Why reset to 0 not N-nodes-back:** Partially completed chains let students memorize their position rather than the content. A full reset forces reconstruction of the full chain from memory, which is the learning mechanism (Generation Effect).
- **Why 3 breaks max:** Unlimited resets become grind. After 3 breaks, the student is clearly struggling with the underlying content — Duolingo Mode kicks in, targeting the specific nodes that caused the breaks.
- **Why NOT session-end on first break:** The mechanic is 1 of 3 games in Phase 3, not the session gate. Session-end-on-first-break would be disproportionately punishing for what is a practice game, not an assessment.

---

### Decision 3 — Time Pressure

**Options considered:** (A) Hard countdown per node (e.g., 15s, answer or wrong), (B) No timer at all ("just vibes"), (C) Momentum bar — visual pressure with no hard cut, draining over N seconds

**Decision: Momentum bar — soft time pressure, PISA-level-adaptive window. Bar expiry = wrong answer.**

Each node shows a glowing "momentum bar" beneath the chain. It drains from full to empty over a window calibrated to the student's PISA level:

| Student PISA level | Momentum window per node |
|---|---|
| Below L1 | 45 seconds |
| L1 | 35 seconds |
| L2 | 25 seconds |
| L3 | 20 seconds |
| L4+ | 15 seconds |

- **Bar drains to zero → treated as wrong answer** (counts toward the 3-break limit).
- **Answer before 50% bar drains → +15 XP speed bonus.**
- **Answer before 75% bar drains → +5 XP.**
- No audio countdown (no anxiety-inducing ticking). Bar is visual only — a color gradient shift from green → yellow → red.
- **Why not hard cut:** Hard per-node timers (option A) suit speed games but damage comprehension. Students who encounter an unfamiliar node should have time to reason, not just guess. The momentum bar preserves a sense of urgency (the chain wants to keep moving) without punishing slow readers.
- **Why not no timer:** "Just vibes" (option B) removes the defining tension of a chain — the feeling that momentum will carry you through. Without any pressure, Reaction Chain becomes indistinguishable from a flashcard quiz.

---

### Decision 4 — Content Structure (Sequential vs Thematic)

**Options considered:** (A) Nodes are always conceptually sequential (photosynthesis steps in order), (B) Nodes are independent questions thematically grouped, (C) Content author explicitly declares the mode

**Decision: Content author declares `chain_mode` as `ordered` or `thematic`. Both are supported.**

| Mode | Behavior | Best for |
|---|---|---|
| `ordered` | Nodes must appear in the declared sequence. Breaking the chain and restarting repeats nodes in the SAME order. | Biological processes, mathematical derivations, historical sequences, algorithms |
| `thematic` | Nodes are shuffled on restart. Sequence is decorative (the chain visual) not meaningful. Correct answers in any order. | Vocabulary sets, formula families, geography features, mixed-topic review |

**For `ordered` chains:** The content author declares the canonical sequence. The question at each node tests understanding of *that specific step and its link to the next step* ("Why does glucose form at this stage?" not just "Name this stage").

**For `thematic` chains:** Questions are standard recall/application items. The chain format adds visual streak motivation (watching beads light up) over a flat flashcard deck.

**Why this matters:** Forcing all Reaction Chain content into ordered mode would restrict it to process-heavy topics. Allowing thematic mode makes it usable for any vocabulary or mixed-topic session, which increases catalog utilization. The mode declaration means the rendering engine and the session assembly algorithm both know what they're getting.

---

## 1. Core Loop

One complete micro-loop for a single node:

```
NODE N BEGINS:
  → Chain displays N nodes (1 to max_nodes); nodes 1 to (N-1) lit green, node N pulsing
  → Momentum bar fills and begins draining (window based on student PISA level)
  → Question is displayed beneath the chain (text + optional image/formula)
  → Student types or selects answer

ANSWER SUBMITTED (or momentum bar expires):

  IF correct (or ≥ 60% AI credit on open reasoning):
    → Node N lights up green with a "spark" animation
    → Chain "conducts" — glowing pulse travels from node N toward node N+1
    → +100 XP base (+ speed bonus if early)
    → Momentum bar refills for node N+1
    → IF N = max_nodes: CHAIN COMPLETE → victory animation, full XP awarded

  IF incorrect (or momentum expired):
    → Node N flashes red 3×
    → Wrong_in_a_row counter increments
    → IF wrong_in_a_row = 1 or 2: node stays dark, student gets brief feedback ("Noto'g'ri. Davom eting."), momentum bar refills with a -10% penalty, student sees next node question (chain NOT yet broken)
    → IF wrong_in_a_row = 3:
        → CHAIN BREAK animation (particles, shatter sound)
        → break_count increments
        → wrong_in_a_row resets to 0
        → IF break_count < 3: restart from node 1
        → IF break_count = 3: game attempt FAILED → Duolingo Mode routing
```

**Wrong-in-a-row clarification:** The counter resets to 0 after any correct answer. It is NOT a cumulative wrong count — it specifically measures consecutive wrongs.

---

## 2. Input Format

What the content author provides when building a Reaction Chain game item.

### JSON Schema

```json
{
  "mechanic": "reaction_chain",
  "chain_id": "string (UUID)",
  "title": "string (display title, ≤60 chars, Uzbek)",
  "chain_mode": "ordered | thematic",
  "chain_skin": "default | biology_process | history_timeline | math_steps | algorithm_flow",
  "node_count": "integer (6–10)",
  "standard_ref": "string (UZ-{SUBJECT}-{GRADE}-{TOPIC}-{SEQ})",
  "alias_code": "string (dotted alias)",
  "pisa_level_target": "integer (1–6)",
  "blooms_level": "remember | understand | apply | analyze",
  "transition_skill": "string (e.g. 'L1->L2: sequence biological steps in order')",
  "textbook_ref": {
    "textbook_id": "string",
    "chapter": "string",
    "section": "string",
    "page_range": "string"
  },
  "nodes": [
    {
      "node_id": "integer (1–10, matches position in ordered mode)",
      "node_label": "string (short label shown ON the chain node, ≤20 chars)",
      "question": "string (question text, Uzbek)",
      "question_type": "mc | short_answer | open_reasoning",
      "media": {
        "type": "image | formula | none",
        "url": "string (optional)",
        "alt": "string (optional)"
      },
      "answer_options": ["string"] ,
      "correct_answer": "string",
      "partial_credit_threshold": "float (0.0–1.0, for open_reasoning)",
      "pisa_level": "integer (1–6)",
      "blooms": "remember | understand | apply | analyze",
      "transition_skill": "string",
      "on_wrong_feedback": "string (≤80 chars, Uzbek — shown on wrong answer)",
      "on_correct_feedback": "string (≤60 chars, optional, Uzbek)",
      "link_to_next": "string (optional — for ordered mode, explains WHY node N leads to node N+1, shown briefly on correct)"
    }
  ]
}
```

### Field Rules

| Field | Rule |
|---|---|
| `node_count` | 6 minimum (below 6 is just a quiz), 10 maximum (above 10 strains working memory at G5) |
| `chain_mode` | Mandatory. No default — content author must declare intent. |
| `question_type` | `mc` for Grades 1-4 and below-L2 students; `short_answer` for G5-8; `open_reasoning` allowed for G9+ or when pisa_level ≥ 4 |
| `node_label` | Shown on the node *before* the question is asked (the visual representation of the step). In ordered mode these form the readable process diagram. |
| `link_to_next` | Ordered mode only. 1 sentence. Shows after correct answer: "Chunki X, endi Y bo'ladi…" Reinforces causal chain understanding. |
| `on_wrong_feedback` | Must NOT give away the answer. Must redirect ("Yana bir bor o'ylab ko'ring: bu jarayon qanday energiya ishlatadi?") |
| `partial_credit_threshold` | Only evaluated for `open_reasoning`. Default 0.6. AI must score ≥ threshold for "correct" to count. |

### Minimal Worked Example (Input)

```json
{
  "mechanic": "reaction_chain",
  "chain_id": "rc-sci5-photo-01",
  "title": "Fotosintez zanjiri",
  "chain_mode": "ordered",
  "chain_skin": "biology_process",
  "node_count": 6,
  "standard_ref": "UZ-SCI-5-PHOTO-01",
  "alias_code": "SCI.5.4.2.1",
  "pisa_level_target": 2,
  "blooms_level": "understand",
  "transition_skill": "L1->L2: sequence biological process steps and explain each step's role",
  "textbook_ref": {
    "textbook_id": "sci-5-2024-uz",
    "chapter": "O'simliklar hayoti",
    "section": "Fotosintez",
    "page_range": "48-52"
  },
  "nodes": [
    {
      "node_id": 1,
      "node_label": "Quyosh nuri",
      "question": "O'simlik quyosh nuridan qanday foydalanadi?",
      "question_type": "mc",
      "correct_answer": "Yashil barglar quyosh nurini energiya sifatida yutadi",
      "answer_options": [
        "Yashil barglar quyosh nurini energiya sifatida yutadi",
        "Ildizlar quyosh nurini suvga aylantiradi",
        "Quyosh nuri fotosintez uchun kerak emas"
      ],
      "pisa_level": 1,
      "blooms": "remember",
      "transition_skill": "L1->L2: identify the role of sunlight in a biological process",
      "on_wrong_feedback": "Darslikdagi 48-betga qarang — barglar rangini nima beradi?",
      "link_to_next": "Yutilgan energiya keyingi bosqich — suvni parchalash uchun ishlatiladi."
    }
  ]
}
```

---

## 3. Output / Evaluation

### Evaluation Pathways

| Answer type | Evaluation method | Latency | Notes |
|---|---|---|---|
| `mc` (multiple choice) | Rule-based exact match | <0.1s | No AI needed. Engine compares student selection to `correct_answer`. |
| `short_answer` (keyword) | Rule-based, normalized string match | <0.1s | Lowercased, stripped of diacritics, trimmed. Synonyms listed in answer schema by content author. |
| `open_reasoning` | AI Tier 3 real-time semantic evaluation | ≤3s | AI receives: question, rubric (correct_answer + transition_skill), student response, student PISA level. Returns 0.0–1.0 score. Correct if ≥ partial_credit_threshold. |

### Outcomes Per Node

| Result | Condition | Effect |
|---|---|---|
| **Correct** | Rule match OR AI score ≥ threshold | Node lights green, chain advances, XP awarded |
| **Partial** | AI score 0.4–threshold | Treated as WRONG (chain does not advance), but feedback is softer ("Yaxshilab tushuntirishga harakat qiling…") |
| **Wrong** | Rule mismatch OR AI score < 0.4 OR momentum expired | Node flashes red, wrong_in_a_row counter increments |
| **Timeout** | Momentum bar expires before submission | Treated as wrong. No extra penalty beyond the wrong counter. |

### Chain Completion Scoring

| Outcome | XP | Notes |
|---|---|---|
| Chain completed, 0 breaks, all on first try | 500 XP base + speed bonuses | Maximum reward path |
| Chain completed, 0 breaks, some wrongs (recovered) | 350 XP base + speed bonuses | Wrongs without break still reduce final XP |
| Chain completed, 1 break | 200 XP base + speed bonuses | |
| Chain completed, 2 breaks | 100 XP base | No speed bonus on third attempt |
| 3 breaks — failed | 0 XP | Routes to Duolingo Mode |

**Speed bonus stack (per node):** Answer before 50% bar drained → +15 XP. Answer before 75% bar drained → +5 XP.

---

## 4. PISA Mapping

### Applicable PISA Levels and Domains

| PISA Level | Configuration | What the chain tests |
|---|---|---|
| L1 | 6 nodes, ordered, mc format, ≤2-step reasoning | Recall factual steps in a process ("Name the stage that produces oxygen") |
| L2 | 6-8 nodes, ordered or thematic, mc/short_answer | Understand WHY each step leads to the next; extract step roles from simple diagram |
| L3 | 8 nodes, ordered, short_answer/open_reasoning | Apply process knowledge to a modified scenario ("If there were no chlorophyll, which step would stop first?") |
| L4 | 8-10 nodes, ordered, open_reasoning | Analyze interdependencies ("Which two nodes are most tightly coupled, and why would disrupting one cascade through the others?") |

**Target zone for Reaction Chain:** L1–L3. Above L3, Why Chain and Real-Life Challenge are better matches (they require less linear structure and more argument construction). Reaction Chain should not be forced to L5-6.

### PISA Domains

| Domain | Reaction Chain fit | Notes |
|---|---|---|
| **Science** | ★★★★★ Best fit | Process sequences (photosynthesis, digestion, water cycle, combustion) are exactly what ordered chains model. |
| **Mathematics** | ★★★★☆ Strong | Multi-step procedures, proof steps, equation-solving chains. Works in ordered mode. |
| **Reading** | ★★★☆☆ Moderate | Narrative sequence (plot events, argumentation steps). Thematic mode for vocabulary chains. |
| **History** | ★★★★☆ Strong | Causal event chains, cause-and-effect sequences. Ordered mode. |
| **Geography** | ★★★☆☆ Moderate | Climate system cycles, map-reading sequences. Ordered mode for process; thematic for feature identification. |

### PISA Process Categories

Reaction Chain items may target:
- **Formulate** — describing a process (ordered, G5-8)
- **Employ** — applying process knowledge in a new context (ordered, G7+)
- **Interpret** — explaining why results follow from steps (ordered, G6+)

### Transition Skills

| Transition | Example node question design |
|---|---|
| `L1->L2: sequence biological process steps and explain each step's role` | "What is produced at this step?" (step is labeled) |
| `L1->L2: extract procedural steps from a visual diagram` | Node shows diagram segment; student names what occurs |
| `L2->L3: explain why each step in a process is necessary` | "Why would removing this step prevent the next step from occurring?" |
| `L2->L3: integrate multi-step procedural knowledge into causal reasoning` | "Which step stores energy and why is that critical for the organism?" |
| `L3->L4: analyze interdependencies in a multi-step process` | "If this node stopped, which downstream nodes would be affected and why?" |

---

## 5. Bloom's Band

| Bloom's Level | Supported? | How |
|---|---|---|
| **Remember** | ✅ Yes — primary | Node labels recall factual steps; mc questions test naming |
| **Understand** | ✅ Yes — primary | `link_to_next` and "why" questions test causal understanding |
| **Apply** | ✅ Yes — secondary | Modified scenarios; "what would happen if we changed step X?" |
| **Analyze** | ✅ Yes — at higher PISA/grade | Interdependency questions; comparing ordered vs. thematic chains |
| **Evaluate** | ❌ Not this mechanic | Evaluation requires comparing multiple approaches; linear chains don't support this structure. Use Why Chain or Real-Life Challenge. |
| **Create** | ❌ Not this mechanic | Creation requires open-ended design; chains are always pre-authored. Use Notebook Capture or Final Boss. |

**Primary band: Remember → Understand → Apply.** Content authors must not try to push Reaction Chain into Evaluate/Create — those levels need a different mechanic.

---

## 6. Subject Eligibility

### Eligible Subjects

| Subject | Eligibility | Best use |
|---|---|---|
| **Science (Tabiiy fanlar)** | ✅ Strongly eligible | Ordered chains for all major biological and chemical processes |
| **Biology (Biologiya)** | ✅ Strongly eligible | Digestion, respiration, cell cycle, food webs (ordered) |
| **Chemistry (Kimyo)** | ✅ Strongly eligible | Reaction mechanisms, combustion sequence, electrolysis steps |
| **Physics (Fizika)** | ✅ Eligible | Energy conversion chains, wave propagation steps, circuit state sequences |
| **Mathematics (Matematika)** | ✅ Eligible | Equation-solving steps, proof steps, algorithm execution. Not for concept lists. |
| **History (Tarix)** | ✅ Eligible | Causal event chains; historical process sequences |
| **Geography (Geografiya)** | ✅ Eligible | Water cycle, climate feedback loops, plate tectonics sequence |
| **Informatics (Informatika)** | ✅ Eligible | Algorithm steps, sorting process, network packet routing |
| **Literature / Language** | ⚠️ Limited | Thematic mode only (vocabulary chains). Plot-event chains are valid for narrative analysis. |
| **Tarbiya (Values / SEL)** | ❌ Not eligible | No sequential or thematic chains exist in Tarbiya content; chill-mode shape doesn't fit the urgency of a chain |
| **Tasviriy Sanat (Visual Arts)** | ❌ Not eligible | Creative process is non-linear; Maker-First shape requires open-ended making, not fixed-sequence recall |
| **Texnologiya** | ⚠️ Limited | Safety procedures and tool sequences are valid (ordered mode). Design process is non-linear (use Maker-First shape mechanics instead). |
| **PE / Music** | ❌ Not eligible | Physical/musical skill sequences require embodied demonstration, not text/MC answers |

### Why Tarbiya/Art are excluded

These subjects use Chill Mode and Maker-First shapes respectively. Both shapes explicitly avoid "right answer" tension mechanics — the defining feature of Reaction Chain (momentum bar, chain break, competitive speed). Importing this mechanic into those sessions would contradict their pedagogical intent.

---

## 7. Grade Eligibility

| Grade band | Eligible? | Configuration | Rationale |
|---|---|---|---|
| **G1-2** | ❌ No | — | Reading fluency not sufficient for chain mechanic; question comprehension too slow; momentum bar adds unnecessary anxiety |
| **G3-4** | ⚠️ Limited | `mc` only, 6 nodes, `thematic` mode, 45s window | Can be used with simple vocabulary or picture-based chains. Node labels must have images. Not for ordered process chains. |
| **G5-6** | ✅ Primary target | `mc` and `short_answer`, 6-8 nodes, both modes, 25-35s window | Ideal grade band. Science and History process chains. Ordered mode most useful here. |
| **G7-8** | ✅ Eligible | `short_answer` and `open_reasoning`, 8 nodes, both modes, 20-25s window | More complex causal chains. Open reasoning allowed when pisa_level ≥ 3. |
| **G9-11** | ✅ Eligible | `open_reasoning`, 8-10 nodes, ordered mode, 15-20s window | Advanced process analysis and multi-disciplinary chains. But at this level, Why Chain and Final Boss are often better alternatives. |

**Optimal deployment: G5-6, ordered mode, 6-8 nodes, process-content subjects.**

---

## 8. Parameters / Difficulty Knobs

The adaptive engine tunes the following parameters independently per student session:

| Parameter | Range | What it controls | Adaptive rule |
|---|---|---|---|
| `node_count` | 6–10 | Number of nodes (chain length) | Start at 6 for below-L2; increment by 1 after 2 consecutive clean completions; decrement after chain break |
| `momentum_window_seconds` | 15–45 | Time per node before bar expires | Set at session start based on student PISA level; decrease by 2s after clean completion; increase by 5s after chain break |
| `question_type` | mc → short_answer → open_reasoning | Cognitive demand of answer format | Elevate format when student completes 2 sessions at 0 breaks; lower when 2+ breaks in last 3 sessions |
| `ordered_complexity` | simple_label → causal_link → counterfactual | Depth of "why" in ordered chains | Controlled by `blooms_level` in the node schema; adaptive engine selects node pools by Bloom's band |
| `pisa_level_target` | 1–4 | Difficulty ceiling for questions | Managed by the global IRT-based student theta; Reaction Chain nodes are tagged with `pisa_level`, engine selects from appropriate range |
| `break_limit` | 3 (fixed) | Number of breaks before task fails | **NOT tunable.** Always 3. This is the mechanic's core tension. |
| `node_reshuffle_on_break` | true (thematic) / false (ordered) | Whether nodes reorder after break | Auto-set by `chain_mode`. Ordered chains always restart in same order (learning the sequence is the goal). |

### Difficulty Progression Rules

```
AFTER clean completion (0 breaks):
  → increment node_count by 1 (if < 10)
  → reduce momentum_window_seconds by 2 (if > 15)
  → next session selects 1 additional node at pisa_level+1

AFTER 1-break completion:
  → hold current configuration
  → no change to node_count or window

AFTER 2-break completion:
  → decrement node_count by 1 (if > 6)
  → increase momentum_window_seconds by 5
  → flag student to teacher dashboard if 3rd consecutive session with breaks

AFTER task failure (3 breaks):
  → activate Duolingo Mode on specific broken nodes
  → reset to minimum configuration (6 nodes, 35s window)
  → hold reset configuration for 2 sessions before adaptive engine re-engages
```

---

## 9. Failure / Retry Behavior

### Per-Node Wrong Answer (wrong_in_a_row < 3)

- Node flashes red (3×, 300ms each)
- Brief audio: short wrong-answer tone (no alarm, no harsh sound)
- `on_wrong_feedback` shown for 2 seconds below the node — a redirection hint, NEVER the answer
- Momentum bar refills with a 10% penalty (slightly shorter window for the next attempt at this node)
- Student immediately sees the SAME node question again
- **This is not a break — the chain has not broken. The student has another chance.**

### Chain Break (wrong_in_a_row = 3)

- All 3 consecutive wrong answers displayed in a brief "flash back" strip (no explanations, just the questions shown — the student sees *what* they struggled with)
- Chain shatter animation (500ms): nodes burst outward, chain line snaps
- Text displayed (Uzbek): *"Zanjir uzildi — 3 ta xato ketma-ket. Qaytadan boshlang."*
- 2-second pause, then automatic restart to node 1 (no button required — prevents students using pause as a rest)
- `break_count` increments; `wrong_in_a_row` resets to 0

### "Hali emas" Framing

In line with NETS Uzbek framing principles, wrong answers use patient, non-punishing language:

| Situation | Text (Uzbek) | Tone |
|---|---|---|
| Single wrong answer | *"Hali emas — yana o'ylab ko'ring."* | Encouraging |
| Second wrong in a row | *"Qiyin savolga duch keldingiz — lekin imkoningiz bor."* | Acknowledging |
| Third wrong (chain break) | *"Zanjir uzildi. Qaytadan boshlang — siz uddalaysiz."* | Resetting, not shaming |
| Task failed (3 breaks) | *"Keling, qiyin bo'lgan savollarga birga qaraylik."* | Transitioning to remediation |

### Duolingo Mode Entry (3 breaks)

When the task fails:
1. System identifies which specific nodes caused the 3rd wrong_in_a_row in each break (stored per break)
2. Compiles the "problem nodes" — the subset that repeatedly failed
3. Presents those nodes individually as flashcard-style review items (outside the chain, no pressure, no momentum bar)
4. After review, student may attempt the Reaction Chain ONE more time (chain_mode preserved, node_count preserved)
5. If the second attempt also fails (3 breaks): session progress is marked incomplete on those standards; teacher is flagged; student must redo the related Story Mode segment before next session

---

## 10. Anti-Cheat Surface

### Tier 2 Monitoring Points

| Signal | Detection method | Action |
|---|---|---|
| **Robotic timing** | All answers arrive within 1-2 seconds across all nodes, regardless of question complexity | Flag for review; apply human-timing variance model. If >80% of answers are suspiciously fast, silently switch to harder node variants |
| **Answer pattern replay** | Student answers in identical sequences across multiple sessions (memorizing positions, not content) | Ordered chains: shuffle answer options. Thematic chains: shuffle node order on retry. |
| **Copy-paste detection (open_reasoning)** | Short answer arrives < 0.5s after question display | Treat as blank submission. Surface note: *"Javobni o'zingiz yozing."* |
| **Second-device screenshot farming** | Photos of correct-answer screens shared within a class (social cheating) | Reaction Chain stores anonymized node-answer pairs; cross-student identical open-reasoning answers on the same chain flagged for teacher review |
| **Momentum bar exploit** | Student intentionally runs out bar (wrong) to skip hard nodes, then gets easy ones later | Tracked: if a student fails >40% of nodes via timeout but completes the chain, it's flagged as "skip-cheat attempt". Timeouts count toward wrong_in_a_row identically to wrong answers. |

### Anti-Cheat Limits

Reaction Chain does **not** implement biometric behavioral fingerprinting (that is a separate higher-tier system). These are Tier 2 passive signals only.

---

## 11. Telemetry Emitted

All telemetry is scoped to the session and student ID. No personally identifiable information beyond student_id.

### Events

| Event | Payload | Purpose |
|---|---|---|
| `rc_session_start` | `{student_id, chain_id, chain_mode, node_count, pisa_level_target, timestamp}` | Session initialization |
| `rc_node_attempt` | `{node_id, question_type, time_to_answer_ms, answer_hash, is_correct, ai_score (if open), momentum_pct_remaining, wrong_in_a_row_before}` | Per-node granular attempt record |
| `rc_node_correct` | `{node_id, xp_awarded, speed_bonus_xp}` | XP accounting |
| `rc_node_wrong` | `{node_id, wrong_in_a_row_after, was_timeout}` | Wrong answer tracking |
| `rc_chain_break` | `{break_count_after, breaking_node_id, wrong_nodes_in_sequence: [node_id, node_id, node_id]}` | Chain break record with the 3 nodes that caused it |
| `rc_chain_complete` | `{break_count, total_xp, time_elapsed_ms, completion_attempt}` | Completion record |
| `rc_task_failed` | `{total_breaks: 3, problem_nodes: [node_id, ...], duolingo_triggered: true}` | Failure record triggering Duolingo Mode |
| `rc_session_end` | `{outcome: complete | failed, total_xp, pisa_contribution, transition_skills_practiced: []}` | Session summary for teacher dashboard |

### Teacher Dashboard Contributions

| Dashboard metric | Source event |
|---|---|
| **Mastery map — process sequences** | `rc_node_correct` per standard_ref |
| **Struggle points heatmap** | `rc_chain_break.wrong_nodes_in_sequence` aggregated across class |
| **PISA progress** | `rc_session_end.pisa_contribution` (IRT-weighted delta per session) |
| **Time-on-task** | `rc_session_end.time_elapsed_ms` |
| **Chain break rate** | `rc_chain_break` count per student per topic |
| **Speed trend** | `rc_node_attempt.time_to_answer_ms` median per student over time |

### Student Profile Contributions

| Profile element | Source |
|---|---|
| Reaction Chain streak badge | Consecutive `rc_chain_complete` with `break_count = 0` |
| "Chain Master" title | 5× clean completions on same chain_id |
| PISA transition skill progress bar | `rc_session_end.transition_skills_practiced` |
| Engagement score input | Session completion rate (complete vs. failed) |

---

## 12. Dual-Catalog Role

**Catalog:** Interactive Catalog Pool (Catalog #5)
**Not in the Default 16** — Reaction Chain is exclusively an Interactive Catalog mechanic.

### Placement Rationale

Reaction Chain belongs in the Interactive Catalog because:
1. It wraps a knowledge-gated game mechanic (the chain with momentum and break rules) around content, not a pure pedagogical delivery mode
2. It has strategic consequences (chain break) that are absent from Default Pool mechanics
3. It requires a specialized renderer (chain visualization, node animations, momentum bar) beyond the content-delivery UI of Default mechanics
4. Per the dual-catalog selection rule, it fills the "≥1 Interactive Catalog" slot when the topic maps to a sequential process

### When the session assembly engine should select Reaction Chain

```
SELECT Reaction Chain for the Interactive Catalog slot WHEN:
  - topic maps to a sequential or causal process (biology, chemistry, math procedures, history chains)
  - AND chain_mode = ordered content exists in the pool for this standard_ref
  - AND student PISA level is L1–L3 (outside this range, consider Why Chain or Final Boss instead)
  - AND student has NOT played Reaction Chain in the last 2 sessions (no mechanic > 2× per session)
  - AND device passes render check (no known render failures for chain animation)

SELECT Thematic Reaction Chain WHEN:
  - topic is vocabulary-heavy or formula-set (no natural sequence)
  - AND student engagement score has dipped over last 3 sessions (novelty effect)
  - AND the session already has sufficient sequential mechanics from the Default Pool

DO NOT SELECT Reaction Chain WHEN:
  - subject is Tarbiya or Tasviriy Sanat (see §6)
  - student is below G3 (see §7)
  - student failed Reaction Chain 3× on this standard_ref (mark this mechanic as temporarily blocked for this standard; use alternative)
  - chain_mode = ordered but NO ordered chain content exists for this standard_ref (log CATALOG_FALLBACK warning)
```

---

## 13. Cost Profile

### Tier Breakdown

| Component | Tier | Cost | Frequency |
|---|---|---|---|
| Chain renderer (node animations, momentum bar) | **Tier 1** (client-side) | ~0 | Every node, every session |
| `mc` answer evaluation | **Tier 1** (rule-based) | ~0 | Every mc node |
| `short_answer` evaluation | **Tier 1** (normalized match) | ~0 | Every short_answer node |
| `open_reasoning` AI evaluation | **Tier 3** (AI call, <3s) | ~$0.003–0.008 per call | Only nodes with `question_type = open_reasoning` |
| `on_wrong_feedback` display | **Tier 1** (pre-authored text) | ~0 | On wrong answer |
| Duolingo Mode routing | **Tier 1** (algorithmic routing) | ~0 | On task failure |
| Teacher dashboard telemetry processing | **Tier 1** (aggregation) | ~0 | Per session end |

### Estimated Cost Per Session

| Scenario | AI calls | Estimated cost |
|---|---|---|
| 6-node chain, all mc/short_answer | 0 | $0 |
| 8-node chain, 3 open_reasoning nodes | 3 (max, if each answered once) | ~$0.01–0.02 |
| 10-node chain, all open_reasoning (G9+) | 10 (max) | ~$0.03–0.08 |

**For G5-6 (primary target, mc/short_answer):** Near-zero AI cost. Reaction Chain is one of the cheapest mechanics in the Interactive Catalog for the grade band where it is most used.

**Budget position:** Fits within the $3-5/student/year ceiling. G5-6 deployment with default mc/short_answer nodes is effectively cost-free from an inference perspective.

---

## 14. Device Requirements

### Minimum Specification

| Requirement | Minimum | Notes |
|---|---|---|
| **Screen size** | 4.5-inch / 320×568px | Chain of 6 nodes must be readable without scrolling on this screen |
| **Processor** | Any 2018+ mid-range mobile chip | Chain animations are CSS/canvas-based, not 3D — very low GPU requirement |
| **RAM** | 1 GB | Chain state held in JS; no heavy in-memory structure |
| **Browser / runtime** | Chrome 88+, Safari 14+, Firefox 86+, WebView Android 88+ | CSS animations + canvas 2D |
| **Bandwidth** | 256 Kbps (node question text loads on chain init, not per-node) | Pre-load all node questions at chain start to avoid mid-chain latency |
| **Offline** | ✅ Supported (after initial content sync) | Node questions pre-loaded; AI evaluation for open_reasoning requires connection — fallback to keyword match if offline |

### Special Hardware

**None required.** No camera, no microphone, no accelerometer, no stylus.

### Compared to Other Interactive Catalog Mechanics

Reaction Chain has the **lowest** device requirements in the Interactive Catalog. Bridge Builder and Minefield Navigator require canvas-heavy rendering; Territory Conquest requires a more complex game state engine. Reaction Chain's animation is a simple left-to-right light propagation with particle burst on break — achievable on any mid-range device from 2018.

**Low-end device behavior:** On devices that fail the render check threshold (set by the session assembly engine), fall back to a simplified "text chain" version — no animations, just a numbered list with progress indicators. Full functionality preserved; visual engagement reduced. Log as `RC_SIMPLIFIED_RENDER`.

---

## 15. Worked Example — G5 Science: Photosynthesis Chain

**Subject:** Science (Tabiiy fanlar), Grade 5
**Topic:** Fotosintez (Photosynthesis)
**Textbook:** 5-sinf Tabiiy fanlar 2024, Chapter 4 "O'simliklar hayoti", Section "Fotosintez", pages 48–52
**Standard:** UZ-SCI-5-PHOTO-01 / SCI.5.4.2.1
**Chain mode:** `ordered`
**Chain skin:** `biology_process`
**Node count:** 6
**PISA target:** L2
**Bloom's:** Understand
**Transition skill:** `L1->L2: sequence biological process steps and explain each step's role`
**Session phase:** Phase 3, Game Breaks (Interactive Catalog slot)

---

### Visual Layout (ordered, biology_process skin)

```
NODE 1          NODE 2          NODE 3          NODE 4          NODE 5          NODE 6
[Quyosh nuri] → [Suv]        → [Xlorofill]   → [CO₂]         → [Glukoza]     → [Kislorod]
  ●                ●               ●               ●               ●               ○
(lit green)    (lit green)    (lit green)    (lit green)    (lit green)    (pulsing — current)

───────────────────────────────────────────────────────────────────────────────────────────
MOMENTUM BAR: [▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░]  (25 seconds, 60% remaining — student PISA L2)
───────────────────────────────────────────────────────────────────────────────────────────

QUESTION (Node 6):
  O'simlik kislorodni qaerga chiqaradi va bu jarayon nima uchun muhim?

  Javoblar:
  (A) Barglar orqali atmosferaga; hayvonlar nafas olishi uchun
  (B) Ildizlar orqali tuproqqa; o'simlikning o'sishi uchun
  (C) Mevalarga; urug' etilishi uchun
```

---

### All 6 Nodes

**Node 1 — Quyosh nuri (Sunlight)**
- Question: *"O'simlik quyosh nuridan qanday foydalanadi?"*
- Type: mc
- Correct: *"Yashil barglar quyosh nurini energiya sifatida yutadi"*
- PISA: L1 | Bloom's: Remember
- Feedback (wrong): *"Darslikdagi 49-betga qarang — barglar rangini nima beradi?"*
- link_to_next: *"Bu energiya suvni parchalash uchun ishlatiladi."*

**Node 2 — Suv (Water)**
- Question: *"O'simlik qaysi organ orqali suv oladi va u qayerdan keladi?"*
- Type: mc
- Correct: *"Ildizlar orqali tuproqdan"*
- PISA: L1 | Bloom's: Remember
- Feedback (wrong): *"O'simlikning qaysi qismi tuproqda joylashgan?"*
- link_to_next: *"Ildiz suvini bargga yetkazgach, xlorofill ikkala moddani birlashtiradi."*

**Node 3 — Xlorofill (Chlorophyll)**
- Question: *"Xlorofill barglarda nima uchun zarur? U qanday vazifa bajaradi?"*
- Type: short_answer
- Correct answer keywords: ["quyosh nurini yutadi", "fotosintez", "energiyani o'zlashtiradi"]
- PISA: L2 | Bloom's: Understand
- Feedback (wrong): *"Xlorofill — bu bargning 'quyosh batareyasi'. U nima uchun barg yashil rangda?"*
- link_to_next: *"Xlorofill energiyasi CO₂ va suvni biriktirib, glukoza hosil qiladi."*

**Node 4 — CO₂ (Carbon Dioxide)**
- Question: *"O'simlik CO₂ ni qayerdan oladi va u qaysi organ orqali kiradi?"*
- Type: mc
- Correct: *"Havadan, barglardagi stomalar (teshikchalar) orqali"*
- PISA: L2 | Bloom's: Understand
- Feedback (wrong): *"Barglarda ko'zga ko'rinmaydigan mayda teshikchalar bor — ular nima deb ataladi?"*
- link_to_next: *"CO₂ va suv quyosh energiyasi bilan birlashib, o'simlikning ozuqasini — glukozani hosil qiladi."*

**Node 5 — Glukoza (Glucose)**
- Question: *"Fotosintezda hosil bo'lgan glukoza o'simlikka qanday foyda beradi?"*
- Type: short_answer
- Correct answer keywords: ["ozuqa", "energiya", "o'sish uchun", "quvvat"]
- PISA: L2 | Bloom's: Understand
- Feedback (wrong): *"Glukoza — bu o'simlikning taomi. Inson ovqat esa nima qiladi?"*
- link_to_next: *"Fotosintezning yana bir mahsuloti — kislorod — atmosferaga ajraladi."*

**Node 6 — Kislorod (Oxygen)**
- Question: *"O'simlik kislorodni qaerga chiqaradi va bu jarayon nima uchun muhim?"*
- Type: short_answer
- Correct answer keywords: ["atmosferaga", "barglar orqali", "hayvonlar nafas oladi", "hayot uchun zarur"]
- PISA: L2 | Bloom's: Understand
- Feedback (wrong): *"Kislorod — bu fotosintezning 'sovg'asi'. Biz uni qayerdan olamiz?"*
- link_to_next: *null (last node)*

---

### Walkthrough — Successful Completion

```
STUDENT opens Reaction Chain "Fotosintez zanjiri"
  → 6 nodes shown, all dark, node 1 pulsing
  → Momentum bar appears: 35s window (student PISA L2)

Node 1 (mc): Student selects "Yashil barglar quyosh nurini energiya sifatida yutadi"
  → Correct → Node 1 lights green → pulse travels to node 2 → +100 XP, +15 XP speed bonus
  → "link_to_next" shown 1.5 seconds: "Bu energiya suvni parchalash uchun ishlatiladi."

Node 2 (mc): Student selects "Ildizlar orqali tuproqdan"
  → Correct → Node 2 lights green → pulse travels to node 3 → +100 XP

Node 3 (short_answer): Student types "quyosh nurini yutadi va fotosintez uchun kerak"
  → Keyword match: "quyosh nurini yutadi" + "fotosintez" → Correct → +100 XP, +5 XP speed bonus
  → "link_to_next": "Xlorofill energiyasi CO₂ va suvni biriktirib, glukoza hosil qiladi."

Node 4 (mc): Student selects wrong option B "Tuproqdan, ildizlar orqali"
  → Wrong → node 4 flashes red → wrong_in_a_row = 1
  → Feedback: "Barglarda ko'zga ko'rinmaydigan mayda teshikchalar bor — ular nima deb ataladi?"
  → Node 4 question reappears
  Student selects correct option A → Correct → +100 XP (no speed bonus — bar partially drained)
  → wrong_in_a_row resets to 0

Node 5 (short_answer): Student types "o'sish uchun energiya beradi"
  → Keyword match: "energiya", "o'sish" → Correct → +100 XP

Node 6 (short_answer): Student types "atmosferaga chiqadi, hayvonlar nafas olish uchun"
  → Keyword match: "atmosferaga" + "nafas olish" → Correct → +100 XP

CHAIN COMPLETE → Victory animation: all 6 nodes glow gold, "chain spark" travels end-to-end
Text: "Fotosintez zanjiri to'liq! Ajoyib!"
XP summary: 600 base + 20 speed bonuses = 620 XP
Stars: 2 stars (1 wrong answer at node 4, but completed; 1-star for completion, 2-star for completing with 0 breaks)
Transition skill progress: +1 toward "L1->L2: sequence biological process steps and explain each step's role"
```

---

### Walkthrough — Chain Break Scenario

```
Student struggles with nodes 3, 4, 5 (open questions about mechanisms)

Node 3: wrong → wrong_in_a_row = 1
  Feedback shown → student retries → wrong again → wrong_in_a_row = 2
  (wrong twice on same node: counts as 2 consecutive wrongs; each retry of same node increments counter)
Node 4: wrong → wrong_in_a_row = 3 → CHAIN BREAK

"3 ta xato ketma-ket → zanjir uzildi" flash screen shows nodes 3, 3, 4 (the 3 breaking questions)
break_count = 1

Restart from node 1. Student now gets second attempt.
  Nodes 1-2: correct.
  Node 3: wrong → wrong_in_a_row = 1 → retry → correct (recovered) → wrong_in_a_row = 0
  Nodes 4-6: all correct.

CHAIN COMPLETE (break_count = 1)
XP: 200 base + speed bonuses
Stars: 1 star (completed, but with a break)
```

---

## Appendix A — Summary Card (Content-Ops Quick Reference)

| Property | Value |
|---|---|
| Mechanic ID | `reaction_chain` |
| Catalog | Interactive Catalog Pool (#5) |
| Bloom's | Remember → Understand → Apply |
| PISA levels | L1–L3 (optimal L2) |
| Grade band | G5-6 primary; G3-4 limited; G7-11 supported |
| Best subjects | Science, Biology, Chemistry, Math, History |
| Ineligible subjects | Tarbiya, Tasviriy Sanat, PE, Music |
| Chain modes | `ordered` (sequential) / `thematic` (decorative) |
| Node count | 6–10 |
| Break limit | 3 (fixed) |
| Momentum window | 15–45s (PISA-adaptive) |
| AI tier | Tier 1 (mc, short_answer) / Tier 3 (open_reasoning only) |
| Estimated cost (G5-6) | ~$0/session (no open_reasoning at this grade) |
| Device requirement | Low — any 2018+ mid-range mobile |
| Offline support | Yes (open_reasoning degrades to keyword match) |

---

*Definition authored by ReactionChainResearcher (Paperclip agent d54914cd-94f9-408b-a325-5a390da00d31)*
*Parent spec: NETS-Homework-Engine-UNIFIED.md v2.0, Section 6.9*
