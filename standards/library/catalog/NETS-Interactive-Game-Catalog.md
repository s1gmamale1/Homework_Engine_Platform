# NETS Interactive Knowledge-Gated Game Catalog

**Version:** 1.0 — April 7, 2026
**Status:** Specification for Phase 3 Integration
**Applies To:** [[NETS-Homework-Engine-UNIFIED]] §5.3, §6.2, §6.3

> See also: [[HOME]] · [[NETS-UI-UX-Design-Spec]] · [[QUICK_REFERENCE]]
**Purpose:** Define all interactive game mechanics that gate progression behind subject-mastery questions. Every game in this catalog integrates directly with the PISA proficiency tracking, AI question generation, and XP economy.

---

## Core Design Philosophy

These are **NOT** standalone mini-games. They are **knowledge-gated experiences**.

| Traditional Game | NETS Adaptation |
|------------------|-----------------|
| Player moves → Game state changes | Player answers question correctly → Game state changes |
| Player moves wrong → Penalty/Undo | Player answers wrong → Strategic penalty (lost turn, forced move, reduced power) |
| Skill = Reflexes/Memorization | Skill = Subject Mastery + Strategic Application |
| Win/Loss = Binary | Win/Loss = Mastery Data + XP + Progression to Next Phase |

**The Golden Rule:** The game tests knowledge. The game board tests strategy. Success requires BOTH.

---

## Game Catalog

### 1. Tic Tac Toe vs AI
**Inspiration:** Classic Tic Tac Toe (Ancient Egypt/Rome, adapted for NETS)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | AI asks first question → determines who starts. On student's turn: AI asks question → correct answer places X on chosen tile → wrong answer places X randomly. AI plays optimally. First to 3-in-a-row wins. |
| **Knowledge Gate** | Every student turn requires answering a subject question. ≥60% correct places the tile. Wrong answer forces random placement (0.2% mercy chance it lands where chosen). |
| **Difficulty Scaling** | AI difficulty decreases after each wrong answer. Minimum floor: 60% of student's PISA level. AI plays at minimax depth calibrated to student level. |
| **Win/Loss/Retry** | Win = standard XP + bonus per remaining attempt. Loss = retry. 3 attempts max. All 3 failed = task failure. |
| **Best Subjects** | All subjects (universal fallback) |
| **Implementation Tier** | Phase 1 (MVP) |

---

### 2. Connect Four vs AI
**Inspiration:** Connect Four (Hasbro, 1974 / Howard Wexler, Ned Strongin)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | 7×6 grid. Student drops disc. First to connect 4 wins. AI takes turns immediately after. |
| **Knowledge Gate** | Before dropping disc, student answers question. Correct → disc drops in chosen column. Wrong → disc drops in random column (0.5% mercy). |
| **Difficulty Scaling** | AI uses minimax with depth scaling (2-6). Wrong answers reduce AI depth, giving student strategic breathing room. |
| **Win/Loss/Retry** | Win = standard XP + column bonus. 3 attempts max. All 3 failed = task failure. |
| **Best Subjects** | Math, Science, Biology, History |
| **Implementation Tier** | Phase 1 (MVP) |

---

### 3. Codebreaker
**Inspiration:** Mastermind (Mordecai Meirowitz, 1970) — Educational use documented in *CBE-Life Sciences Education* (PMC3022521)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | AI generates secret code (4-5 symbols). Student has 8 attempts to crack it. After each guess, AI gives feedback (right value + right position, right value + wrong position). |
| **Knowledge Gate** | Each guess attempt requires answering a question. Correct → guess submitted and scored. Wrong → guess attempt consumed WITHOUT submission (lost turn). |
| **Difficulty Scaling** | Code length (3 easy → 4 medium → 5 hard). Symbol pool size expands. Fewer allowed attempts at higher difficulty. |
| **Win/Loss/Retry** | Crack code in ≤8 attempts = WIN. Fail = LOSS + reveal code. 1 attempt. |
| **Best Subjects** | Math (number sequences), Chemistry (element symbols), Biology (taxonomic classifications), History (chronological dates) |
| **Implementation Tier** | Phase 1 (MVP) |

---

### 4. Memory Match Blitz
**Inspiration:** Classic Memory/Concentration (Centuries-old folk game, no single originator)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Grid of face-down cards (12-20 pairs). Student flips two trying to match. |
| **Knowledge Gate** | After matching two visually similar cards, student must answer a question to CONFIRM. Correct → cards stay revealed. Wrong → cards flip back + 5-second lockout. |
| **Difficulty Scaling** | Grid size (3×4 easy → 5×6 hard). Time per match decreases. Question difficulty scales with PISA level. |
| **Win/Loss/Retry** | ≥70% pairs matched = pass. <70% = retry. 2 attempts max. |
| **Best Subjects** | Biology (term↔definition, organ↔function), Chemistry (formula↔name), Language (word↔meaning), Math (graph↔formula) |
| **Implementation Tier** | Phase 1 (MVP) |

---

### 5. Reaction Chain
**Inspiration:** Original NETS concept (inspired by rhythm games: Guitar Hero, 2005 + chain-reaction puzzle mechanics)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Chain of 6-10 nodes on screen. Student taps nodes in correct sequence to complete chain reaction. |
| **Knowledge Gate** | Before each tap, quick question appears. Correct → node lights up, chain progresses. Wrong → reaction steps BACK one node. 3 wrong in a row = chain breaks completely, restart. |
| **Difficulty Scaling** | Chain length (3 easy → 10 hard). Faster question pace. Wrong answers push back more nodes at higher difficulty. |
| **Win/Loss/Retry** | Complete full chain within time limit = WIN. 3 chains total. Best score counted. |
| **Best Subjects** | Chemistry (reaction sequences), Biology (metabolic pathways, life cycles), Math (multi-step equations), History (event sequences) |
| **Implementation Tier** | Phase 2 (Enhancement) |

---

### 6. Word Ladder Climb
**Inspiration:** Word Ladder/Doublets (Lewis Carroll, 1877)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Start word → target word. Change one letter per step. Each step must be a valid word. |
| **Knowledge Gate** | Each letter change requires subject question. Correct → step accepted. Wrong → step rejected, stay at current rung. 60s timeout per rung = slide back one rung. |
| **Difficulty Scaling** | Ladder length (3 steps easy → 7 hard). Faster timers. Obscure vocabulary at higher difficulty. |
| **Win/Loss/Retry** | Reach target word before timeout = WIN. 2 climbs. Second climb = different word pair. |
| **Best Subjects** | Language (vocabulary), Biology (terminology chains), Chemistry (element name transformations) |
| **Implementation Tier** | Phase 2 (Enhancement) |

---

### 7. Puzzle Lock (Sliding Tile)
**Inspiration:** 15 Puzzle (Noyes Palmer Chapman, 1874)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | 3×3 or 4×4 scrambled grid with one empty space. Student slides tiles to arrange in order. |
| **Knowledge Gate** | Each slide requires question. Correct → tile slides into empty space. Wrong → WRONG tile slides (random adjacent). |
| **Difficulty Scaling** | Grid size (3×3 easy → 4×4 hard). Timer added at highest. More scrambled tiles initially. |
| **Win/Loss/Retry** | Solve within time limit = WIN. 1 attempt per puzzle. Fail → show solution, retry with new scramble. |
| **Best Subjects** | Math (number sequences), Chemistry (periodic table ordering), History (chronological event ordering) |
| **Implementation Tier** | Phase 2 (Enhancement) |

---

### 8. Blackjack 21 — Knowledge Edition
**Inspiration:** Classic Blackjack/21 (Origins ~1600s France)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Standard Blackjack rules. Draw cards, closest to 21 without busting wins. Student vs Dealer AI. |
| **Knowledge Gate** | Before HIT or STAND, answer question. Correct → choice executed. Wrong → AI makes choice FOR student (usually poorly). |
| **Difficulty Scaling** | Dealer stands on softer totals at higher difficulty (plays better). Fewer double-down opportunities. Harder math questions. |
| **Win/Loss/Retry** | Best of 3 hands. Win = standard XP + streak bonus. Loss = retry. |
| **Best Subjects** | Math (mental arithmetic), Probability, Statistics |
| **Implementation Tier** | Phase 2 (Enhancement) |

---

### 9. Territory Conquest
**Inspiration:** Risk (Albert Lamorisse, 1957) — simplified to 1v1 area control

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Map with 9-16 territories. Student and AI start with equal split. Turn-based attacks on adjacent territories. |
| **Knowledge Gate** | Attack requires question. Correct → territory flips. Wrong → attack fails AND lose one own territory (random, never starting). AI attacks on its turn with calibrated accuracy. |
| **Difficulty Scaling** | AI answer accuracy scales (easy: 50%, hard: 85%). Map size increases. Fewer safe starting positions. |
| **Win/Loss/Retry** | Control all territories = WIN. 1 battle. Loss = feedback on weak territories, retry allowed. |
| **Best Subjects** | Geography, History (conquest campaigns, territorial expansion), Cross-subject Big Boss review |
| **Implementation Tier** | Phase 3 (Premium) |

---

### 10. Escape Room: Subject Lock
**Inspiration:** Escape rooms (Real-world, 2007+ / Digital: "The Room" series, Fireproof Games)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Virtual room with 4 locked objects (door, chest, window, drawer). Each has code/password. Unlock all 4 → escape. |
| **Knowledge Gate** | Each object requires 2-3 correct answers to unlock. Unlocking reveals CLUES for other objects (cross-hinting). |
| **Difficulty Scaling** | Fewer clues at higher difficulty. Harder questions. Time limit: 5 min (easy) → 3 min (hard). |
| **Win/Loss/Retry** | Unlock all 4 within time = WIN. 2 escape attempts. Second attempt = different codes + layout. |
| **Best Subjects** | Any subject. Cross-subject escape rooms ideal for Big Boss weeks. |
| **Implementation Tier** | Phase 3 (Premium) |

---

### 11. Bridge Builder
**Inspiration:** Original NETS concept (inspired by physics bridge-building games: Bridge Constructor, Headup Games)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Gap must be crossed. Student places beams/cables/supports. Each piece costs budget points. Limited total budget. |
| **Knowledge Gate** | Placement requires question. Correct → piece placed, costs points. Wrong → piece NOT placed, points STILL deducted (wasted attempt). |
| **Difficulty Scaling** | Wider gaps, lower budgets, fewer allowed wrongs at higher difficulty. Physics complexity increases. |
| **Win/Loss/Retry** | Build stable bridge within budget = WIN. 2 tries. Budget/difficulty adjust on retry. |
| **Best Subjects** | Math (geometry, force calculations), Physics, Engineering concepts |
| **Implementation Tier** | Phase 3 (Premium) |

---

### 12. Minefield Navigator
**Inspiration:** Original NETS concept (inspired by Minesweeper, Curt Johnson, 1983 + navigation puzzles)

| Component | Specification |
|-----------|---------------|
| **Core Loop** | Grid (5×5 or 6×6) with hidden mines. Student navigates start→finish through safe tiles. |
| **Knowledge Gate** | Each move requires question. Correct → move to chosen tile. Wrong → FORCED to move to AI-chosen adjacent tile (likely mine). 3 lives total. |
| **Difficulty Scaling** | More mines (3 easy → 10 hard). Grid size increases. AI forced-choice becomes more strategic at higher difficulty. |
| **Win/Loss/Retry** | Reach exit = WIN. Hit 3 mines = LOSS. 2 runs. Different mine placement each run. |
| **Best Subjects** | Math (coordinate navigation), Geography (map reading), Cross-subject (abstract grid representation) |
| **Implementation Tier** | Phase 3 (Premium) |

---

## Integration Strategy

### Where Games Live in the Framework

| Context | Usage | Game Selection Logic |
|---------|-------|----------------------|
| **Phase 3 (Game Breaks)** | 2-3 games per homework session. Core practice. | Content creator tags game in JSON. Engine validates against Subject-to-Game Matrix. |
| **Mystery Box Event** | Random pop-up OR pre-placed. Single challenging question tied to game outcome. | Performance-based rewards. Correct answer = game win + reward. Wrong = participation XP only. |
| **Big Boss (Weekly)** | Territory Conquest, Escape Room, or Codebreaker configured for cross-subject review. | AI targets 3 weakest standards. Game difficulty = PISA level +1. |
| **Mythical Boss (Elite)** | Escape Room or Bridge Builder at PISA 5-6 difficulty. Zero hints. One attempt. | Multi-subject reasoning required. Win = 5× XP + exclusive title. |

### Game Selection & Validation Flow

```
1. Content creator defines homework assignment in JSON
2. Engine selects 2-3 game_items for Phase 3
3. VALIDATION:
   ├─ game_mechanic matches Subject-to-Game Matrix? (✅ proceed / ❌ reject)
   ├─ Questions tagged with standard_ref, blooms_level, pisa_level? (✅ proceed / ❌ reject)
   ├─ At least 2 different transition skills targeted? (✅ proceed / ❌ flag teacher)
4. BUILD game state (board, pieces, timer, AI opponent)
5. PRE-FETCH questions from content pool (Tier 1) OR request AI generation (Tier 2)
6. RUN game loop (student input → question → evaluation → board update)
7. RECORD mastery data (which standards were tested, win/loss, accuracy, time-per-question)
8. PASS data to Phase 6 (Boss) and Phase 7 (Reflection) for cross-phase synthesis
```

### JSON Configuration Example

```json
{
  "phase": 3,
  "game_mechanic": "connect_four_ai",
  "subject": "math",
  "standard_ref": "UZ-MATH-7-LINFUNC-03",
  "transition_skill": "L2->L3: interpret coordinate representations",
  "difficulty_tier": "medium",
  "questions_per_turn": 1,
  "board_config": {
    "rows": 6,
    "columns": 7,
    "connect_target": 4,
    "ai_depth": 4
  },
  "scoring": {
    "win_xp": 300,
    "partial_xp": 150,
    "loss_xp": 25,
    "mastery_weight": 0.8
  },
  "accessibility": {
    "screen_reader_compatible": true,
    "keyboard_navigation": true,
    "color_blind_palette": true,
    "timer_toggle": true
  }
}
```

### Scoring & Data Flow

Games do NOT output a simple win/loss. They output **granular mastery data**:

| Data Point | Captured | Used By |
|------------|----------|---------|
| Questions answered | Total count, correct/incorrect ratio | PISA level recalculation |
| Time per question | Average, variance, hesitation spikes | Flow state monitoring, anti-cheat |
| Strategic errors | Wrong moves despite correct answers | AI hint generation for Phase 7 |
| Knowledge gaps | Specific standards missed during game | Big Boss targeting, Spaced Repetition queue |
| Game outcome | Win/Loss/Attempts used | XP calculation, celebration tiers, teacher dashboard |

**Formula for Game XP:**
```
Base XP = 100 × (correct_answers / total_questions)
Strategy Bonus = 50 × (game_win ? 1 : 0)
Speed Bonus = 10 × (questions_under_5s)
Total Game XP = Base XP + Strategy Bonus + Speed Bonus
```

### Subject-to-Game Compatibility Matrix

| Game | Math | Science (Chem/Phys) | Biology | History | Language |
|------|:----:|:-------------------:|:-------:|:-------:|:--------:|
| Tic Tac Toe vs AI | ✅ | ✅ | ✅ | ✅ | ✅ |
| Connect Four vs AI | ✅ | ✅ | ✅ | ✅ | ✅ |
| Codebreaker | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Memory Match Blitz | ✅ | ✅ | ✅ | ✅ | ✅ |
| Reaction Chain | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Word Ladder Climb | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| Puzzle Lock | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| Blackjack 21 | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| Territory Conquest | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| Escape Room | ✅ | ✅ | ✅ | ✅ | ✅ |
| Bridge Builder | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Minefield Navigator | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ |

**Legend:** ✅ Primary fit | ⚠️ Works with adaptation | ❌ Not recommended

---

## Technical Implementation Guidelines

### 1. State Management Architecture
All games run as **client-side React components** wrapped in a `GameContainer` provider.
- **Global State:** Student profile, PISA level, current session ID, XP total (React Context)
- **Local State:** Board configuration, turn order, question queue, timer, attempt count (useReducer)
- **Sync:** Only sync on game completion or critical failure. Reduces API calls by 80%.

### 2. Question Delivery Pipeline
- **Tier 1 (Pre-fetched):** Batch load 10-15 questions from content pool BEFORE game starts. Zero latency during play.
- **Tier 2 (AI Fallback):** If pool exhausted, fetch from Ollama (`http://192.168.1.15:11434/api/chat`). 60s timeout. Cache response for next session.
- **Tier 3 (Static Fallback):** If Ollama unreachable, use hardcoded fallback questions from `data/phases.json`.

### 3. AI Opponent Configuration
For games with AI opponents (Tic Tac Toe, Connect Four, Territory, Blackjack):
- Use **Minimax algorithm** with alpha-beta pruning.
- **Depth scaling:** Maps directly to student PISA level.
  - PISA < 1.5 → Depth 2 (makes obvious mistakes)
  - PISA 1.5-2.5 → Depth 4 (plays competently)
  - PISA > 2.5 → Depth 6 (plays near-optimally)
- **Question gating overrides AI strength.** A student who answers correctly but plays poorly will still struggle. The AI adapts DOWN if the student misses 2+ questions in a row.

### 4. Accessibility Requirements (Mandatory)
Every game MUST pass:
- **WCAG 2.1 AA** color contrast ratios.
- **Full keyboard navigation** (Tab/Arrow/Enter/Space). No mouse-dependent actions.
- **Screen reader compatibility** (ARIA labels for board state, turn indicators, question prompts).
- **Timer toggle** for students with processing delays.
- **Color-blind safe palettes** (Never rely on red/green alone. Use shapes + colors).

---

## Quality Assurance Checklist

Before ANY game is deployed to production, it must pass:

| Check | Question | Pass/Fail |
|-------|----------|:---------:|
| **Knowledge Gate Fairness** | Does a wrong answer penalize gameplay proportionally (not punitively)? | |
| **Flow State Preservation** | Does difficulty auto-adjust after 2 consecutive wrong answers? | |
| **No Guessing Exploits** | Can a student win by random chance without knowing the content? (<10% win rate by luck) | |
| **Cross-Phase Data Flow** | Does the game record mastery data that Phase 6/7 actually uses? | |
| **Offline Fallback** | If Ollama is unreachable, does the game still function with pre-fetched/static questions? | |
| **Performance** | Does initial load take <1.5s? Does each question render in <0.2s? | |
| **Mobile Responsive** | Does the board/game UI scale correctly on 320px width screens? | |
| **Stranger Test** | Can a non-expert understand the rules in <30 seconds? | |

---

## Rollout Phases

| Phase | Timeline | Games | Rationale |
|-------|----------|-------|-----------|
| **MVP** | Sprint 1-2 | Tic Tac Toe, Connect Four, Memory Match Blitz, Codebreaker | Lowest build complexity. Proven mechanics. Universal subject fit. |
| **Enhancement** | Sprint 3-4 | Word Ladder, Puzzle Lock, Reaction Chain, Blackjack 21 | Medium complexity. Adds variety for returning students. |
| **Premium** | Sprint 5-6 | Territory Conquest, Escape Room, Bridge Builder, Minefield Navigator | Highest complexity. Reserved for Big Boss / Mythical Boss events. High reward, high prestige. |

---

## References & Inspirations

1. **Tic Tac Toe / Connect Four / Blackjack / Risk / Memory / Mastermind / 15 Puzzle / Word Ladder / Minesweeper** — Classic board/card/puzzle games with centuries of documented rules. Adapted here for educational knowledge-gating. Source adaptations documented via public domain rules and educational game design literature.
2. **Tower Defense** — Inspired by *Desktop Tower Defense* (2007, Paul Preece) and modern mobile TD mechanics.
3. **Reaction Chain** — Original NETS concept inspired by rhythm game progression mechanics (*Guitar Hero*, 2005, Harmonix).
4. **Bridge Builder** — Inspired by physics-based construction games (*Bridge Constructor*, Headup Games).
5. **Escape Room** — Inspired by real-world escape rooms (2007, Takao Kato) and digital puzzle games (*The Room* series, Fireproof Games).
6. **Educational Validation** — Mastermind's use in developing logic skills documented in *CBE-Life Sciences Education* (PMC3022521). Connect Four and Tic Tac Toe adaptations for classrooms documented in EF Teacher Zone and TES teaching resources.
7. **Gamification Theory** — Octalysis Framework (Yu-kai Chou), Hook Model (Nir Eyal), Flow State Theory (Csikszentmihalyi, 1990).

---

**Status:** Ready for engineering handoff. All games specified with rules, scaling, integration points, and QA gates.
