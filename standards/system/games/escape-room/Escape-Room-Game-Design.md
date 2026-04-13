# Escape Room: Subject Lock v1

**Status:** Draft for handoff
**Version:** 1.1
**Date:** 2026-04-12
**Layer:** Interactive Catalog Pool
**Game type:** Knowledge-gated puzzle room
**Depends on:** `NETS-Homework-Engine-UNIFIED.md`, `NETS-Interactive-Game-Catalog.md`, `NETS-Library-Framework.md`

---

## 1. Purpose

Escape Room is a multi-lock puzzle game. The student is placed in a virtual room and must unlock `4 objects` by answering subject questions. Solving one lock reveals clues for the others.

This game exists to test:
- multi-concept synthesis
- clue linking across tasks
- reasoning under time pressure

Its defining mechanic is **cross-hinting**. The room is not 4 isolated quizzes. Each solved lock narrows the search space for the others.

---

## 2. Core Rules

1. Every room has exactly `4 locked objects`:
   - Door
   - Chest
   - Window
   - Drawer
2. Each lock requires `2-3 correct answers`.
3. Solving a lock reveals clue payloads for other locks.
4. Discovered clues are stored in a visible `Clue Journal`.
5. The student may attempt the locks in any order.
6. The room ends in success only when all 4 locks are solved.
7. If time expires first, the student is `locked in`.

---

## 3. Standard Shape

| Item | Standard Mode | Hard Mode |
|---|---|---|
| Locks | 4 | 4 |
| Total questions | 9 | 9 |
| Timer | 5:00 to 4:00 | 3:00 |
| Hints | 1 per lock | 1 per lock or none in elite mode |
| Attempts | 2 runs | 1-2 depending on mode |

Question pattern by lock:
- Door: 3 questions
- Chest: 2 questions
- Window: 2 questions
- Drawer: 2 questions

---

## 4. Core Loop

1. Show room intro and start timer.
2. Student chooses any lock.
3. Lock presents its question set.
4. Correct answers progress the lock.
5. Wrong answers cost time and small XP.
6. Full lock solve opens the object and reveals clue payloads.
7. Clue payloads are added to the journal.
8. Student uses journal clues to solve remaining locks.
9. Escape occurs only when all 4 locks are open.

---

## 5. Lock Roles

| Lock | Role |
|---|---|
| Door | Main escape route, usually hardest |
| Chest | Often reveals a key word or number |
| Window | Often handles order, pattern, or arrangement |
| Drawer | Often reveals conceptual or riddle-style clue |

The lock types should feel different even when they use the same subject.

---

## 6. Clue Journal and Cross-Hinting

The Clue Journal is always visible during the session. It stores every discovered clue card.

Good clue design:
- narrows the answer space
- supports another lock
- does not directly give the final answer

Examples:
- `One digit of the door code is 6`
- `The chest answer starts with A`
- `The window pattern begins with the blue tile in the top-right`

Cross-hinting is the core value of the game. Without it, Escape Room collapses into 4 separate lock quizzes.

---

## 7. Timer, Hints, and Failure

### Timer
- Easy: `5:00`
- Medium: `4:00`
- Hard: `3:00`
- Elite: `2:30`

### Hints
- `1 hint` per lock
- hints cost XP
- hints narrow the search space but do not reveal the answer

### Wrong answers
- first wrong: retry with time tax
- second wrong: easier variant
- third wrong: lock may auto-solve with reduced reward, depending on mode

### Attempts
- standard room: `2 runs`
- retry resets the room with different codes or question order

---

## 8. Best Variations

### Single-Subject Room
All 4 locks come from the same subject or chapter.

### Cross-Subject Room
Each lock uses a different subject. Best for Big Boss review weeks.

### Mythical Boss Room
No hints, tighter timer, harder questions, one attempt, multi-subject only.

---

## 9. Subject Fit

| Family | Fit |
|---|---|
| Aniq Fanlar | Excellent |
| Til Fanlari | Good |
| Tabiat Fanlari | Excellent |
| Ijtimoiy Fanlari | Excellent |
| Tarbiya/Sanat | Limited |

Escape Room is strongest when the content naturally supports clues, patterns, ordering, evidence, or linked reasoning.

---

## 10. Buzan Integration

Escape Room is one of the best fits for Buzan's work when used properly.

Relevant integrations:
- **Memory Palace:** the room itself is the locus structure
- **Link System:** each solved lock points toward another
- **Radiant thinking:** the student branches across locks instead of following one linear chain
- **TEFCAS:** each attempt is trial -> feedback -> adjust -> success
- **Association:** object + clue + concept are remembered together

What to avoid:
- decorative Buzan references with no gameplay value
- clues that are so vague they do not support memory or reasoning

---

## 11. Anti-Patterns

Reject the design if:
- the locks can be solved fully independently
- clues directly give away answers
- all 4 locks feel mechanically identical
- the timer makes success impossible for the target student
- the room becomes a trivia quiz instead of a clue network

---

## 12. Acceptance Checklist

The game is ready only if:
- all 4 locks are clearly distinct
- the clue journal adds real value
- every clue helps another lock without fully solving it
- the room works in standard time limits
- the student can choose lock order freely
- Buzan integration improves memory, clue linkage, or branching reasoning

---

## 13. Canonical Example

**Baseline room:**  
`You are locked in Al-Khwarizmi's study. The door, chest, window, and drawer are all locked. Each object requires 2-3 correct answers. Every solved object reveals clue cards for the others. Use the clue journal to connect the room and unlock all 4 before time runs out.`

That is the core mechanic: solve, reveal, connect, escape.
