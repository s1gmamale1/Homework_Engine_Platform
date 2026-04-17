# Tic Tac Toe vs AI

> Interactive Mechanic #1 / Default Mechanic #15 — Answer-to-Move Grid Conquest

**Players:** 1 | **Mode:** Student vs AI | **Buzan Integrated** | **Bloom's:** Remember / Apply | **PISA:** 2-3

---

## 1. Core Game Mechanics

Student plays a standard 3x3 Tic Tac Toe game against an AI opponent. The twist: **the student does not choose where their mark goes — their knowledge does.**

- **Correct answer →** the student's chosen tile (X or O) is placed on the **student's intended cell** (the cell they tapped before the question appeared).
- **Wrong answer →** the student's tile is placed on a **RANDOM empty cell** (0.2% mercy chance that it lands on the intended cell anyway — a hidden "lucky bounce" edge case).

The AI plays **optimally at all times** — it will not deliberately lose, make suboptimal moves, or show mercy. The AI uses a standard minimax algorithm, guaranteeing it never loses. The best possible outcome for the student is a draw.

**Game flow per session:**

- **3 games per session.** Each game is a fresh 3x3 board.
- Before each turn, the student taps their target cell, then answers a subject question (Math, Science, History, English — matching the current lesson).
- The AI responds immediately after the student's move resolves.
- Student's win rate across all 3 games is tracked on their profile permanently.

**Grade scaling:**

- **Grades 1-3:** Questions at PISA L1-L2 (direct recall, simple recognition). AI plays with a 1-move delay (shows "thinking..." animation) to reduce intimidation.
- **Grades 4-6:** Questions at PISA L2-L3 (property identification, basic inference). Standard AI speed.
- **Grades 7-9:** Questions at PISA L3-L4 (causal reasoning, process analysis). AI moves instantly — no delay.
- **Grades 10-11:** Questions at PISA L4+ (multi-step reasoning). AI moves instantly. Question difficulty increases with each consecutive correct answer (escalating challenge).

**Dual-Catalog Rule compliance:** Tic Tac Toe vs AI appears in **BOTH** the Default catalog (Mechanic #15) and the Interactive catalog (Mechanic #1). A session must still select at least 1 Interactive + 2 Default games — Tic Tac Toe can fulfill either slot, but not both simultaneously.

---

## 2. Tier-Based Access Control

Both tiers receive Tic Tac Toe vs AI as part of the 28-mechanic core during Phase 3 sessions. Premium unlocks additional board sizes and competitive features.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 Game Breaks (dual-catalog selection) | Same + on-demand access from Library |
| **Board Size** | Standard 3x3 only | 3x3 + 4x4 (Premium) + 5x5 (Premium, need 4-in-a-row to win) |
| **AI Difficulty** | Optimal (minimax) — unchangeable | Optimal + "Grandmaster" mode (AI plays 4x4 and 5x5 with alpha-beta pruning, deeper search) |
| **Win Rate Tracking** | Basic win/draw/loss counter on profile | Detailed analytics: win rate by subject, streak tracking, heat map of intended vs actual cell placements |
| **Cosmetic Themes** | Standard X/O marks, basic grid | Custom mark themes (swords vs shields, atoms vs molecules, historical figures), animated grid lines |
| **First-Move Advantage** | Student always goes first | Student goes first in Game 1, AI goes first in Game 2, alternating thereafter — true competitive balance |
| **"Study the Enemy" Replay** | Not available | After each game, student can replay the board in "sandbox mode" (no questions) to analyze what they could have done differently |

> **Basic Tier Guarantee:** During Phase 3 sessions, Basic students receive the full 3-game experience with optimal AI. The core learning mechanism (answer correctly = your move lands) is identical for both tiers. Premium adds larger boards and post-game analysis tools — these are enrichment, not required for PISA progression.

---

## 3. Buzan Integration: Color Warfare & Spatial Memory

Tic Tac Toe vs AI channels **Tony Buzan's color and imagery principles** to transform a simple grid into a spatial memory battlefield.

- **Color Hooks (Synesthesia — Board Identity):** The student's marks glow in their assigned mastery color (blue for Math lessons, green for Science, gold for History, purple for English). The AI's marks are always a neutral steel gray. This creates a visual story: "my knowledge has color; the machine has none." When the student wins or draws, their color floods the entire winning line (0.5s pulse), creating a strong positive emotional anchor.
- **Spatial Memory (Mind Mapping the Board):** Each of the 9 cells is subtly associated with a position keyword: center = "Heart," corners = "Pillars," edges = "Bridges." After 10+ games, the system generates a "Battle Map" showing which cells the student most frequently intended to claim — and how often wrong answers scattered their marks. This visual map reinforces the connection between knowledge accuracy and strategic control.
- **Imagery & Emotional Weight:** Winning lines are not simple strikes — they are rendered as breaking chains (liberation imagery), lightning bolts (power), or growing vines (organic mastery), chosen randomly per game. Per Buzan: emotionally-charged imagery is 5-10x more memorable than neutral marks. These victory images are saved to the student's gallery.
- **"Hali Emas" Defeat Reframing:** When the student loses (AI wins), the board does NOT show a grim X-through-line. Instead, the AI's winning line dims to gray, and a message appears: "Hali emas" (Not yet). The board then replays the student's wrong-answer moves in red, showing exactly which knowledge gaps cost them the game. Defeat becomes a diagnostic, not a punishment.

---

## 4. Question Styles & Interaction Mechanics

Tic Tac Toe vs AI uses subject questions as the gate for every student move. The AI's moves are automatic (no questions for the AI). Question complexity scales with PISA level.

| PISA Level | Question Style | Interaction Flow | Cognitive Target | Example (Math) |
|-----------|---------------|-----------------|-----------------|---------------|
| **L2** | Direct recall / recognition — single concept | Student taps cell → question appears (multiple choice, 4 options) → correct = mark on target, wrong = random cell | Remember — retrieve fact from memory | "What is 7 x 8?" Options: 54, 56, 48, 63 |
| **L3** | Property identification / simple inference | Same flow, but questions require one reasoning step beyond recall | Understand — identify relationship or property | "Which fraction is equivalent to 3/6?" Options: 2/5, 1/2, 4/9, 5/8 |
| **L3+** | Apply rule to unfamiliar context | Same flow, question may include a short scenario or diagram | Apply — use known procedure in new situation | "A rectangle has perimeter 24cm and width 5cm. What is its area?" Options: 35, 40, 20, 30 cm² |
| **L4** | Multi-step reasoning / process analysis | Same flow, question requires 2+ steps. Timer may appear (30s limit) for higher grades | Analyze — break down complex information | "If f(x) = 2x + 3 and g(x) = x - 1, what is f(g(5))?" Options: 11, 9, 13, 7 |

> **Interaction Design Note:** The student taps their desired cell FIRST, then the question appears. This creates intentional commitment — the student must live with the consequence of their knowledge accuracy. The "wrong = random" penalty is the core punishment mechanism. It makes knowledge gaps feel viscerally costly (your mark lands somewhere you didn't want it), which is far more motivating than a simple "try again" message.

---

## 5. Victory Conditions & Scoring

### A. Per-Game Outcomes

Each of the 3 games can end in one of three states:

- **Student Wins:** Student completes a 3-in-a-row. Since the AI plays optimally, this is only possible if the AI makes a bug (which it never does in standard mode). In practice, student wins are statistically near-zero — but the possibility remains for bug exploitation or AI tier downgrades in lower grades. *XP: +300 + "Impossible Happened" achievement (extremely rare).*
- **Draw:** Board fills with no winner. This is the expected best outcome against optimal AI. *XP: +200 + "Held the Line" badge.*
- **AI Wins:** AI completes a 3-in-a-row. This is the most common outcome. *XP: +50 per correct answer given during the game. "Hali emas" framing — defeat shown as diagnostic, not shame.*

### B. Session-Wide Outcome (3 Games)

| Session Result | Criteria | Consequence |
|---------------|----------|-------------|
| **Strong Session** | 2+ draws out of 3 games | +100 bonus XP, "Tactician" session badge, win rate improves |
| **Solid Session** | 1 draw, 2 losses | Standard XP from correct answers. Win rate updates. Encouraging message. |
| **Task Failed** | 0 draws, 3 losses (AI won all 3) | **Must redo homework in Duolingo Mode.** The lesson content is re-served as micro-drills until mastery improves. Student cannot advance to the next Phase 3 segment until Duolingo Mode clearance is achieved. |

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Correct answer (per question) | +50 | Base reward — each correct answer earns XP regardless of game outcome |
| Student wins a game | +300 | Near-impossible against optimal AI; reserved for edge cases |
| Draw | +200 | Expected best outcome; "Held the Line" recognition |
| AI wins (per game) | +0 | No game bonus, but keep accumulated correct-answer XP |
| Strong Session (2+ draws) | +100 | Bonus on top of per-game XP |
| Task Failed (3 losses) | 0 session bonus | Duolingo Mode trigger; must redo homework |
| 0.2% Mercy Bounce | +10 | Hidden bonus — student never told about the mercy mechanic |

### D. Win Rate & Profile Tracking

Every student has a **Tic Tac Toe Win Rate** displayed on their profile. This tracks draws + wins / total games. Since wins are near-impossible, the effective metric is **draw rate**. Benchmarks:

- **0-20% draw rate:** "Learning the Board" — knowledge gaps still significant.
- **20-40% draw rate:** "Holding Ground" — improving, core concepts solidifying.
- **40-60% draw rate:** "Formidable Opponent" — strong knowledge foundation.
- **60%+ draw rate:** "Unbreakable" — elite-level mastery. Student is ready for 4x4 board (Premium) or harder question sets.

---

*NETS Elite Mechanic Specification — Tic Tac Toe vs AI v1.0*
