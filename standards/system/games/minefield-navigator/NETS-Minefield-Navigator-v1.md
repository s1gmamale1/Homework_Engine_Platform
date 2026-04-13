# NETS Minefield Navigator v1

**Status:** Draft for handoff
**Version:** 1.0
**Date:** 2026-04-12
**Phase:** 3 Interactive Catalog
**Game type:** Knowledge-gated navigation puzzle
**Depends on:** `NETS-Homework-Engine-UNIFIED.md`, `NETS-Interactive-Game-Catalog.md`, `NETS-Library-Framework.md`

---

## 1. Purpose

Minefield Navigator is a grid-based navigation game. The student must move from `Start` to `Exit` across a hidden-mine field. Every move is gated by a subject question.

This game tests two things at the same time:
- content mastery
- path planning under uncertainty

The board creates tension. The questions decide whether the student keeps control.

---

## 2. Core Rules

1. The board is a hidden-mine grid.
2. The student starts on one tile and must reach the exit tile.
3. Every move requires answering one question.
4. Correct answer: the student moves to the chosen adjacent tile.
5. Wrong answer: the system forces the student to an adjacent tile chosen by the AI.
6. If the forced tile contains a mine, the student loses one life.
7. The student has `3 lives`.
8. Reaching the exit is a win.
9. Losing all `3 lives` is a loss.
10. The student gets `2 runs`, with a different mine layout on retry.

---

## 3. Standard Shape

| Item | Standard Mode | Hard Mode |
|---|---|---|
| Grid | 5x5 | 6x6 |
| Mine count | 3-5 | 6-10 |
| Lives | 3 | 3 |
| Moves | Adjacent only | Adjacent only |
| Retry runs | 2 | 2 |

Adjacent means up, down, left, or right. No diagonal movement in the baseline version.

---

## 4. Core Loop

1. Show the board with `Start` and `Exit`.
2. Student selects an adjacent tile.
3. System asks one question.
4. If correct, move to the chosen tile.
5. If wrong, force a move to an adjacent tile.
6. Check whether the moved-to tile is safe or mined.
7. Update lives, board state, and progress.
8. Repeat until exit or zero lives.

---

## 5. Difficulty Design

Difficulty scales by:
- larger grid
- more mines
- smarter AI forced moves after wrong answers

Suggested bands:

| Level | Target | Design |
|---|---|---|
| Easy | lower readiness | 5x5, fewer mines, AI forced move is only mildly punishing |
| Medium | standard use | 5x5 or 6x6, balanced mine spread |
| Hard | advanced students | 6x6, more mines, AI forced move aims for higher danger |

The game should feel risky, but not random or unfair.

---

## 6. Subject Fit

| Family | Best use |
|---|---|
| Aniq Fanlar | coordinates, spatial logic, numeric movement |
| Tabiat Fanlari | map navigation, terrain, ecosystem zones |
| Ijtimoiy Fanlari | timeline traversal, route planning, region comparison |
| Til Fanlari | limited use only if the grid represents sequence/order clearly |

Strong use cases:
- coordinate plane movement
- geography map reading
- periodic table traversal
- historical timeline navigation

---

## 7. Recommended Subject Usage

### Subject family recommendation

| Family | Recommendation | Notes |
|---|---|---|
| Aniq Fanlar | Strong | Best fit for coordinates, grid logic, ordered traversal |
| Tabiat Fanlari | Strong | Works for map movement, terrain, classification zones |
| Ijtimoiy Fanlari | Good | Works for timeline or route progression if the board metaphor is clear |
| Til Fanlari | Limited | Use only when sequence/order/navigation meaning is strong |
| Tarbiya/Sanat | Not recommended | The navigation-risk structure is usually a poor fit |

### Specific subject examples

Strongest subject fits:
- Mathematics
- Geography
- History
- Physics
- Chemistry

Conditional fits:
- Biology
- Informatics

Avoid by default:
- Literature
- Art
- Music
- Tarbiya

---

## 8. Question Types

Minefield Navigator should use fast, decision-friendly question types because movement happens every turn.

### Allowed baseline types

| Question type | Use | Best fit |
|---|---|---|
| Multiple choice | Default per move | All supported subjects |
| Short answer | Medium+ difficulty, older students | Math, science, history |
| Tile match | Good for zone-based traversal or ordered mapping | Geography, chemistry, history |
| Flashcard-style quick recall | Good for low-friction early turns | Math facts, coordinates, terms |

### Use cautiously

| Question type | Why |
|---|---|
| Long open response | Too slow for per-move pacing |
| Notebook Capture | Too heavy for this mechanic's loop |
| Long Story Mode blocks | Breaks navigation rhythm |

### Recommended by tier

- **Basic:** mostly multiple choice and flashcard-style recall
- **Premium:** multiple choice, short answer, and occasional tile-match move gates

---

## 9. Difficulty and Question Level

Difficulty should affect both the board and the question layer.

| Difficulty | Board difficulty | Question difficulty | Typical question types |
|---|---|---|---|
| Easy | 5x5, fewer mines | recall / direct application | flashcard, MC |
| Medium | 5x5 or 6x6, balanced mines | application / interpretation | MC, short answer |
| Hard | 6x6, more mines, riskier forced moves | multi-step application / analysis | short answer, tile match, harder MC |

Hard mode is **Premium-only**.

---

## 10. Tier Division

| Dimension | Basic Tier | Premium Tier |
|---|---|---|
| Access | Available | Available |
| Board modes | Easy, Medium | Easy, Medium, Hard |
| Question types | MC + flashcard-style quick recall | MC + short answer + selective tile match |
| Attempt policy | Limited | No practical cap |
| Difficulty ceiling | Moderate | Full |

### Attempt policy

- **Basic:** `2 attempts` per assigned session instance
- **Premium:** effectively unlimited retries for practice mode

Premium should still keep one scored attempt for formal assignment contexts if the assignment system requires it, but practice access can remain open.

---

## 11. Buzan Integration

Minefield Navigator should use Buzan-aligned elements only where they strengthen navigation, recall, or transfer.

### What fits

- **Memory Palace logic:** the grid can function as a simple spatial memory board, where zones represent categories, concepts, or ordered steps.
- **Association Effect:** safe paths should be easier to remember when tiles are tied to meaningful visual anchors rather than abstract empty squares.
- **Radiant thinking:** branching route choice fits the student's need to compare multiple possible paths instead of following a single linear answer chain.
- **BOST-style review feel:** after a mine hit or wrong forced move, feedback should briefly restate the key idea so the student links the concept to the spatial location.

### What to avoid

- Do not overload the board with decorative visuals that obscure route planning.
- Do not force full mind-map complexity into a small navigation game.
- Do not use Buzan references as theme only; each use must improve memory, route choice, or concept linkage.

### Practical design rule

If a Minefield board uses themed zones, each zone should map cleanly to one of:
- a concept family
- a process stage
- a timeline segment
- a geography region

That keeps the board spatial, memorable, and instructionally useful.

---

## 12. Scoring

| Action | XP |
|---|---:|
| Correct answer | +50 |
| Safe move progress | +20 |
| Reach exit | +200 |
| Mine hit | -10 |
| Wrong answer | -5 |

This game should reward both mastery and survival, not just final win/loss.

---

## 13. Best Variations

### Coordinate Navigator
Student moves on a math grid using coordinate clues.

### Map Route Navigator
Student crosses a geography-style terrain map.

### Timeline Navigator
Student moves through ordered historical milestones.

### Cross-Subject Hazard Grid
Different rows or zones use different subject question pools.

---

## 14. Anti-Patterns

Reject the design if:
- movement is random even after correct answers
- the student can win by pure luck
- the forced move is always instant death
- the grid is decorative and not strategically meaningful
- the questions have no relation to the board metaphor
- Buzan-themed elements are pasted on without improving memory or navigation
- question formats are too slow for turn-by-turn play

---

## 15. Acceptance Checklist

The game is ready only if:
- correct answers preserve player control
- wrong answers remove control but do not make loss automatic
- the board offers meaningful route choice
- the mine layout creates tension without trapping the player unfairly
- the subject metaphor fits the movement system
- any Buzan-style spatial anchors improve recall or route reasoning
- the question format matches fast navigation pacing
- Basic and Premium rules are clearly separated
- the game works in two short runs

---

## 16. Story Mode Note

For future Story Mode work, Buzan integration should be explicit where relevant:
- narrative as memory scaffold, not just flavor text
- strong association hooks
- clear chunking
- visual/radiant structure where it improves recall

Story Mode and Minefield should stay consistent: Story Mode builds memorable structure, and Minefield can later reuse that structure spatially.

---

## 17. Canonical Example

**Good baseline:**  
`You are navigating a 5x5 hazard grid from Start to Exit. You choose one adjacent tile each turn. If you answer correctly, you move there. If you answer wrong, the AI forces an adjacent move. Some tiles are mined. You have 3 lives. Reach the exit before losing all lives.`

That is the core mechanic: knowledge decides control, and control decides survival.
