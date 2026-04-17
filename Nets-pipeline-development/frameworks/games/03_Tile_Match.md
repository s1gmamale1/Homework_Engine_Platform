# Tile Match: Concept-Definition Edition

**Mechanic Type:** Default Mechanic #3
**Bloom's Level:** Understand
**PISA Level:** 1-2
**AI Tier:** Tier 1 ($0 — rule-based, no LLM needed)
**Research Basis:** Dual Coding (Paivio, 1986)
**Expected Gain:** +25-40% recognition
**Session Phase:** Phase 3 (Game Breaks)

---

## 1. Concept-Definition Match Mechanics

All tiles are **face-up** from the start. The board is split into two columns:

- **Left Column (Concepts):** Terms, formulas, symbols, diagrams, dates, images — the "what."
- **Right Column (Definitions):** Explanations, descriptions, visual counterparts, examples, applications — the "meaning."

The student selects **one tile from the left** and **one tile from the right** to form a pair. The system evaluates the match:

- **Correct match:** Both tiles glow green, fade out (+100 XP, timer +3s bonus). The pair is removed from the board.
- **Incorrect match:** Both tiles shake red, flash the correct concept on the matched definition tile for 1.5s (instant feedback, no penalty to progress), timer -5s. Tiles return to selectable state.

### Board Sizes by Grade

| Grade Range | Pairs | Total Tiles | Timer | Notes |
|-------------|-------|-------------|-------|-------|
| Grades 1-2 | 4 | 8 | 3:00 | Large tiles, high-contrast colors |
| Grades 3-4 | 5 | 10 | 2:45 | |
| Grades 5-7 | 6 | 12 | 2:30 | |
| Grades 8-11 | 8 | 16 | 2:00 | |

**Distractor rule:** Every definition tile has exactly one correct concept match. No orphan tiles. No ambiguous pairs.

### Head-to-Head Mode (Premium)

Two students share the same board (synchronous, same session or Library on-demand). Rules:

- Both players race to claim pairs on the same board.
- If Player A claims a pair first, that pair is removed — Player B cannot claim it.
- Correct match: +100 XP + bonus speed points based on time elapsed since board appeared.
- Incorrect match: -5s penalty on that player's timer only, no visual reveal of correct answer to the opponent (anti-griefing).
- First player to claim >50% of pairs wins. If timer expires, most pairs claimed wins.
- Tiebreaker: whoever made fewer wrong attempts wins. Still tied = sudden death on the last remaining pair.

---

## 2. Tier-Based Access Control

Both tiers receive Tile Match as part of the 28-mechanic core during Phase 3 sessions. Premium unlocks additional modes and cosmetic polish.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 Game Breaks (dual-catalog selection) | Same + on-demand access from Library |
| **Game Modes** | Solo Concept-Definition Match only | Solo + Head-to-Head (synchronous 2-player) |
| **Max Board Size** | Up to 6 pairs (standard spec) | Up to 8 pairs (extended challenge) |
| **Visual Polish** | Standard tile animations, basic colors | Enhanced particle effects, custom tile themes, animated transitions |
| **Speed Mode** | Not available | Timer reduced by 25%, same pair count — pure fluency drill |
| **Wrong Match Feedback** | Shake + flash correct answer on definition tile (1.5s) | Same + optional "Why this is wrong" micro-explanation on tap |
| **Streak Bonus** | Standard (+50 XP per 3-correct streak) | Amplified (+75 XP per 3-correct streak) + visual combo counter |

> **Basic Tier Guarantee:** During Phase 3 sessions, Basic students receive the full learning experience. Head-to-Head and Speed Mode are enrichment, not required for PISA progression. The same concept-definition pairs are presented to both tiers — only the delivery mode and cosmetic polish differ.

---

## 3. Buzan Integration: Radiant Association

Tile Match implements **Tony Buzan's Radiant Thinking** principles to strengthen concept-definition neural pathways.

- **Color Hooks (Synesthesia):** Each concept family is assigned a distinct high-contrast color. Math formulas = blue, biological processes = green, historical dates = gold, literary terms = purple. When a student correctly matches a pair, the color briefly floods the entire board (0.3s pulse), reinforcing the category association. Wrong matches flash a muted gray (no positive color reinforcement).

- **Radiant Branches (Visual Tree):** When a student completes a concept family (e.g., all 3 fraction pairs), a "branch complete" animation draws connecting lines from all matched pairs to a central hub tile. This visually encodes the concept as a node in a larger knowledge network. Capturing a full branch grants a "Fog-Lifting" preview of the next related concept family's tiles in the following board.

- **Imagery & Exaggeration:** Definition tiles for abstract concepts include exaggerated visual metaphors (e.g., "Denominator" shown as a giant floor dividing a pizza, with a character slipping on it). Per Buzan's principle: bizarre imagery is 3-7x more memorable than literal text. These visuals persist in the student's match history gallery.

- **Memory Palace Anchor (Special Tile — rare, ~5% of boards):** One pair on the board carries a 🏛️ icon. Matching it triggers a 5-second mini-palace sequence: a familiar location appears (Registan, home, school), and the matched concept is placed at one location within it. Students who match all Palace Tiles across sessions unlock the "Memory Architect" achievement in the Bilim Bazasi.

---

## 4. Question Styles & Interaction Mechanics

Tile Match IS the question — there is no separate quiz layer. The interaction complexity scales with the PISA level of the content being tested.

| PISA Level | Concept Tile Type | Definition Tile Type | Cognitive Target | Distractor Style |
|------------|-------------------|---------------------|------------------|------------------|
| **L1** | Literal term + icon (e.g., "Triangle" with △) | Simple visual or 1-3 word label | Direct recall recognition | Obvious mismatches (circle icon for "Triangle" definition) |
| **L2** | Term alone or formula alone (e.g., "1/2", "Chloroplast") | Definition phrase or corresponding visual (fraction bar, cell diagram) | Property identification | Plausible distractors (wrong fraction visual that looks similar) |
| **L3** | Abstract concept or process name (e.g., "Photosynthesis") | Multi-step description or causal diagram | Causal/definitional pairing with inference | Same-family distractors (respiration description for photosynthesis) |
| **L4** | Scenario or case summary (e.g., "A plant in a dark room for 7 days...") | Outcome analysis or principle identification | Process analysis — apply rule to context | Competing hypotheses (each plausible, only one correct given the facts) |
| **L5** | Multi-source data snippet (chart excerpt, quote, measurement) | Interpretation or argument claim | Evaluation — synthesize from data to conclusion | Partially-correct claims (true statement but not supported by the given data) |
| **L6** | Open problem or paradox statement | Competing theoretical frameworks | Synthesis — map problem to best explanatory model | All frameworks are valid theories; only one best fits this specific problem |

> **Stranger Test Compliance:** A test player who has never seen the content must be able to complete L1-L2 boards using visual cues and prior knowledge alone, without text comprehension. L1 concept tiles always include an icon. L2 definition tiles always include a visual counterpart. L3+ may be text-only (reading comprehension is now part of the test).

---

## 5. Victory Conditions & Scoring

### A. Time Victory (Standard)

Match all pairs before the timer reaches zero. Victory screen shows:

- **Perfect Clear:** 0 wrong attempts. Confetti celebration + bonus 200 XP.
- **Flawless (1 wrong):** +100 XP bonus.
- **Cleared (2+ wrong):** Standard XP, no bonus. Encouraging "Hali emas" (not yet) framing for misses.

### B. Time Exhaustion (Defeat)

Timer reaches 0 with unmatched pairs remaining:

- **Below 60% matched:** "Hali emas" screen. Board is shown with all correct pairs revealed for 5 seconds. Student must replay this board in the next session (tracked as a pending mastery item).
- **60-99% matched:** Partial credit awarded. Unmatched pairs are shown with correct answers. Student earns XP for matched pairs only. No forced replay — counted as a learning session, not a failure.

### C. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Correct match | +100 | Base reward per pair |
| Speed bonus (per match) | +10-50 | Based on time remaining: 50+ sec = +50, 30-49 sec = +30, <30 sec = +10 |
| 3-correct streak | +50 (Basic) / +75 (Premium) | Consecutive correct matches without error |
| Perfect Clear | +200 | Zero wrong attempts all board |
| Flawless (1 wrong) | +100 | Single mistake recovery |
| Memory Palace match | +150 | Rare 🏛️ tile pair (base + bonus) |
| Branch complete | +100 | All pairs from one concept family matched |
| Wrong match | -5s timer | No XP penalty — the time cost is the penalty |
| Timer exhaustion (<60%) | 0 | Must replay; no XP awarded on failed board |

### D. Head-to-Head Victory (Premium Mode)

When two students compete on the same board:

- **Domination Victory:** First player to claim >50% of pairs wins instantly.
- **Time Victory:** If timer expires, player with most pairs wins.
- **Tiebreaker cascade:** Most pairs → fewest wrong attempts → speed on first correct match → sudden death on last unclaimed pair.
- **Winner bonus:** +150 XP + "Conqueror" badge for the session. Loser: standard XP for pairs they claimed (no shame in losing — the losing student's effort still counts toward mastery).

---

*NETS Elite Mechanic Specification — Tile Match: Concept-Definition Edition v1.0*
