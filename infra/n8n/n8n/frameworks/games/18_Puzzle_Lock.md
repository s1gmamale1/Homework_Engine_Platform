# Puzzle Lock (Sliding Tile)

> Interactive Knowledge-Gated Mechanic #4 — Visual-Spatial Content Reconstruction

**Players:** 1 | **Mode:** Solo | **Buzan Integrated** | **Bloom's:** Apply/Analyze | **PISA:** 2-4 | **AI Tier:** Tier 1

---

## 1. Core Game Mechanics

Puzzle Lock presents a **sliding tile puzzle** (3x3 or 4x4 grid) where each tile carries a fragment of subject content — a map region, a timeline segment, a diagram piece, a sentence fragment, or a formula component. The tiles are **scrambled** at the start. The student must **slide tiles into the correct positions** to reconstruct the complete image or sequence. **Knowledge gating** controls every slide: correct answers execute the student's chosen move; wrong answers execute a random move instead.

- **Grid sizes by grade:**
  - **Grades 1-6:** 3x3 grid (8 tiles + 1 empty space). Timer: 3 minutes. Content: simple maps, 3-part diagrams, short sentence assembly, basic formula reconstruction.
  - **Grades 7-11:** 4x4 grid (15 tiles + 1 empty space). Timer: 5 minutes. Content: detailed geography maps, multi-event timelines, complex diagram assembly, multi-step equation reconstruction.
- **Correct answer:** The student's chosen tile slides into the empty space. The tile glows green briefly and locks into position. If the tile lands in its correct solved position, it gains a gold border (visual confirmation). The student retains control of the next move.
- **Wrong answer:** A **random valid adjacent tile** (any tile adjacent to the empty space) slides instead of the student's chosen tile. This tile slides in a random valid direction, potentially disrupting the student's progress. The tile flashes red. The student then regains control for the next move.
- **Goal:** Arrange all tiles into their correct positions before the timer expires. A completion animation assembles the full image/sequence.

**Reference image:** A small reference image showing the solved state is always visible in a corner of the screen (shrunk to ~15% of the puzzle area). For Grades 1-3, the reference is larger (~25%) and may include numbered positions on tiles as an additional hint. For Grades 10-11 on 4x4 grids, the reference can be toggled off by the student (risk/reward — no reference = +50 XP bonus on solve).

**Subject compatibility:** Best suited for visual-spatial content. Geography (assembling country/region maps, placing capitals), history (timeline assembly — ordering events chronologically), biology (diagram reconstruction — cell structures, organ systems), chemistry (periodic table segment assembly, molecular structure construction), math (formula/equation reconstruction, geometric proof assembly), language (sentence/paragraph assembly from fragments).

**Solvability guarantee:** The scrambling algorithm only produces solvable configurations (standard 15-puzzle parity rules apply). Every puzzle is guaranteed to be solvable within the time limit by a student who answers all questions correctly and uses optimal move strategy.

---

## 2. Tier-Based Access Control

Both tiers receive Puzzle Lock as part of the 28-mechanic core during Phase 3 sessions. Premium unlocks larger grids, competitive modes, and visual enhancements.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 Game Breaks (dual-catalog selection) | Same + on-demand access from Library |
| **Max Grid Size** | 3x3 (all grades), 4x4 (Grades 7+) | 3x3, 4x4, and 5x5 challenge grids (Grades 9+) |
| **Game Modes** | Solo puzzle solve only | Solo + Ghost Race (compete against a recorded best-time ghost) + Co-op Solve (two students share one puzzle, alternating turns) |
| **Visual Polish** | Standard tile slide animations, basic color coding | Enhanced particle effects on correct placement, animated image reveal as tiles approach solved state, custom tile themes (map textures, parchment, blueprint) |
| **Wrong Answer Consequence** | Random adjacent tile slides (may disrupt progress) | Same + random slide is highlighted in red with a "lost move" animation, making the cost of wrong answers visually salient |
| **Reference Image** | Always visible (scaled per grade) | Reference can be hidden for +50 XP bonus on solve (Grades 7+). "Blind Solve" mode available — no reference from the start. |
| **Streak Bonus** | Standard (+50 XP per 3-correct streak) | Amplified (+75 XP per 3-correct streak) + visual combo counter on puzzle |

> **Basic Tier Guarantee:** During Phase 3 sessions, Basic students receive the full learning experience. Ghost Race, Co-op Solve, 5x5 grids, and visual enhancements are enrichment, not required for PISA progression. The same puzzle content and knowledge-gating mechanics are presented to both tiers.

---

## 3. Buzan Integration: Spatial-Visual Memory Encoding

Puzzle Lock leverages **Tony Buzan's color, imagery, and spatial memory principles** to strengthen visual-spatial reasoning and content recall.

- **Color Hooks (Synesthesia):** Tiles that belong to the same content region share a subtle background tint. In a geography puzzle, tiles from the same country/region share a color (e.g., all Central Asian tiles share a warm gold tint, all European tiles share a cool blue). In a biology diagram, tiles from the same system share a color (e.g., circulatory = red, nervous = purple). This color coding provides a spatial-visual cue that helps students group related tiles mentally, even before they are adjacent on the grid. When a tile is placed in its correct position, the color briefly floods the entire grid (0.3s pulse), reinforcing the completed region.
- **Radiant Thinking (Image Hub):** The completed puzzle is treated as a radiant structure. When the final tile slides into place, the full image assembles and a "reveal" animation expands from the center tile outward, showing the complete diagram/map/timeline. The solved puzzle is then treated as a single visual unit — the student's brain encodes it as a complete image rather than 8/15/24 separate tiles. This is the core Buzan principle: the whole image is more memorable than the sum of its parts.
- **Imagery & Exaggeration:** Each tile carries not just a content fragment but also a micro-visual element that is exaggerated or distinctive (e.g., a map tile with an unusually shaped lake, a timeline tile with a dramatic event illustration, a cell diagram tile with a comically oversized mitochondrion). Per Buzan's principle, these distinctive visual features make individual tiles 3-7x more memorable, which aids the student in remembering where each tile belongs. When a tile is placed correctly, its distinctive feature is briefly highlighted.
- **Memory Palace Anchor (Puzzle Milestone — rare, ~5% of puzzles):** One tile in the puzzle carries a icon. Placing this tile in its correct position triggers a 5-second mini-palace sequence: a familiar location appears, and the completed image/fragment is "placed" at one location within it. Students who solve all Palace Puzzles across sessions unlock the "Visual Architect" achievement in the Bilim Bazasi.

---

## 4. Question Styles & Interaction Mechanics

Each slide attempt requires answering a subject question. The question style scales with the PISA level of the content and the student's grade band.

| PISA Level | Question Style | Puzzle Context | Cognitive Target | Wrong Answer Feedback |
|-----------|---------------|---------------|-----------------|----------------------|
| **L1** | Direct identification: "Which tile shows [X]?" or "What is this part of the map called?" with visual options | 3x3 simple maps, basic diagrams, picture assembly | Direct recall recognition — identify content elements visually | Visual hint appears (highlight on reference image showing where the content belongs). Random tile still slides. |
| **L2** | Property identification: "What property does this tile represent?" or "Which event happened first: [A] or [B]?" | 3x3 timelines, labeled diagrams, sentence assembly | Property/relationship identification within the content domain | Context clue shown (e.g., date range for timeline events, function hint for diagram parts). Random tile still slides. |
| **L3** | Causal/relational: "Why does [tile A] connect to [tile B]?" or "What happens when [process shown on tile] occurs?" | 3x3 or 4x4 process diagrams, causation timelines, multi-part systems | Causal reasoning — understand relationships between content fragments | Brief explanation of the relationship shown. Random tile still slides, potentially disrupting placement. |
| **L4** | Process analysis: "If you remove [tile] from the puzzle, what is missing from the complete picture?" | 4x4 complex diagrams, detailed maps, multi-system assemblies | Process analysis — understand the role of individual components within a system | System shows what the complete picture would look like without that component. Random tile still slides. |
| **L5** | Evaluation: "Which of these two tile arrangements is correct? Justify." | 4x4 ambiguous content (competing interpretations, multi-valid arrangements) | Evaluation — assess competing content arrangements, justify placement choice | Counter-evidence presented for the wrong arrangement. Random tile still slides. |
| **L6** | Synthesis: "Place these tiles to represent [alternative interpretation] of the content." | 4x4 open-ended content (multiple valid solved states representing different models/frameworks) | Synthesis — construct alternative valid arrangements based on different theoretical frameworks | Partial credit for arrangements that are valid under alternative frameworks. Random tile still slides. |

> **Interaction Model:** The puzzle grid occupies the center of the screen. The student taps/clicks a tile adjacent to the empty space to select it, then taps the empty space to propose the slide. A subject question appears in a panel above or below the grid. Correct answers execute the proposed slide with a smooth animation. Wrong answers execute a random slide — the system randomly selects one of the other valid adjacent tiles and slides it in a random valid direction. The timer counts down visibly. The reference image remains accessible throughout.

---

## 5. Victory Conditions & Scoring

### A. Puzzle Victory (Standard)

Arrange all tiles into their correct positions before the timer expires. Victory screen shows the completed image with a reveal animation. Scoring is based on the number of wrong answers during the solve:

- **Perfect Solve (0 wrong):** 300 XP. Full reveal animation with particle effects. "Perfect" badge for the session.
- **Strong Solve (<3 wrong):** 200 XP. Standard reveal animation. The random-slid tiles are marked with a faint red scar.
- **Solved (3+ wrong):** 100 XP. Reveal animation plays, but the board shows the number of disruptions. Encouraging "Hali emas" framing for the wrong answers — the puzzle was solved, but with significant interference.

### B. Timer Exhaustion (Defeat)

Timer reaches 0 with tiles still misplaced:

- **Below 50% tiles correct:** "Hali emas" screen. The solved puzzle is shown for 5 seconds. Student must replay this puzzle in the next session (tracked as a pending mastery item).
- **50-99% tiles correct:** Partial credit awarded. Remaining tiles are shown sliding into their correct positions. Student earns XP based on tiles correctly placed (see scoring table below). No forced replay — counted as a learning session, not a failure.

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Correct tile slide | +20 | Base reward per successful slide (student's chosen tile, question answered correctly) |
| Tile placed in correct position | +30 | Bonus when a tile lands in its solved position (gold border appears) |
| Perfect Solve (0 wrong) | 300 total | Flat reward: solved puzzle with zero wrong answers. Overrides per-tile XP. |
| Strong Solve (<3 wrong) | 200 total | Flat reward: solved puzzle with 1-2 wrong answers. Overrides per-tile XP. |
| Solved (3+ wrong) | 100 total | Flat reward: solved puzzle with 3 or more wrong answers. Overrides per-tile XP. |
| Wrong answer (random slide) | 0 | Random adjacent tile slides instead. No XP for that move. May disrupt progress. |
| Memory Palace tile placed | +130 | Rare tile placed correctly (base + bonus) |
| Blind Solve bonus (Premium) | +50 | Solved without reference image (Grades 7+) |
| 3-correct streak | +50 (Basic) / +75 (Premium) | Consecutive correct answers without any wrong |
| Timer exhaustion (<50%) | 0 | Must replay; no XP awarded on failed puzzle |
| Partial puzzle (50-99%) | Per-tile XP only | 20 XP per correct slide + 30 XP per tile in correct position. No completion bonus. |

### D. Ghost Race Mode (Premium)

In Ghost Race mode, the student competes against a recorded "ghost" of their own best previous solve on the same puzzle:

- **Ghost display:** A semi-transparent overlay shows the ghost's tile positions in real-time, progressing through the solve at the recorded pace.
- **Beating the ghost:** If the student solves the puzzle faster (fewer total moves, including random slides) than their ghost, they earn a +100 XP "Ghost Buster" bonus.
- **Losing to the ghost:** No penalty — the student's current solve still earns standard XP. The ghost is a personal challenge, not a punitive comparison.
- **Ghost updating:** Each new best time replaces the ghost. The student always races their own best performance.

### E. Co-op Solve Mode (Premium)

Two students share one puzzle and alternate turns:

- **Turn order:** Students alternate proposing slides. Student A proposes a slide and answers a question. If correct, their chosen tile slides. If wrong, a random tile slides. Then it's Student B's turn.
- **Shared knowledge gating:** Each student faces questions independently. Student A's wrong answer does not consume Student B's knowledge — each student's performance is tracked separately.
- **Co-op bonus:** If both students achieve a solve with fewer than 3 total wrong answers combined, each earns a +75 XP "Teamwork" bonus.
- **Communication:** Students can discuss strategy between turns but cannot share answers. The system detects answer-sharing patterns (both students answering identical questions correctly in rapid succession) and may serve alternate question variants.

---

*NETS Elite Mechanic Specification — Puzzle Lock (Sliding Tile) v1.0*
