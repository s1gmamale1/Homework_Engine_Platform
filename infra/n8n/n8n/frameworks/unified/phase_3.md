### 5.3 Phase 3 -- Game Breaks: Active Practice (6-9 min standard / 10 min extended)


**Purpose:** Apply newly learned concepts through targeted game mechanics. Each game activates a specific cognitive skill.

**UPDATED 2026-04-07:** Tic Tac Toe vs AI added as a new mechanic — see §6.4 for the full game rules. It is selectable as one of the 3 game slots in Phase 3, particularly well-suited for recall-heavy content where strategic stakes (the tic-tac-toe board) make practice feel like a duel rather than a quiz.

| Parameter | Standard Mode | Extended Mode |
|---|---|---|
| Duration | 6-9 minutes total | 10 minutes |
| Games per session | 3 games x 2-3 min each | 3-4 games x 2-3 min |
| Placement | Interleaved between Story Mode segments | Same |
| Game selection | Based on subject, Bloom's target, and student PISA level | Same |
| AI Tier | Tier 1 (pre-generated items) | Same |

**Game Selection Algorithm:**
```
1. GET current topic's learning objectives
2. GET student's PISA level and weakest domain areas
3. GET student's in-progress transition skills
4. SELECT 3 game mechanics from TWO POOLS:
   - Default Pool: the 16 mechanics in §6 (Tile Match, Sentence Fill, Memory Sprint,
     Spaced Flashcards, Story Mode, Adaptive Quiz, Mystery Box, Movement Breaks,
     Why Chain, Peer Teaching, Real-Life Challenge, Reflection Journal, Memory Palace,
     Final Boss, Tic Tac Toe vs AI, Notebook Capture)
   - Interactive Catalog Pool: the 12 knowledge-gated games defined in
     standards/NETS-Interactive-Game-Catalog.md (see §6.9)
   DUAL-CATALOG RULE (NEW 2026-04-07):
   - At LEAST 1 of the 3 selected games MUST come from the Interactive Catalog Pool
   - At LEAST 2 of the 3 selected games MUST come from the Default Pool
   - At least 1 selection must match the student's CURRENT Bloom's level (reinforcement)
   - At least 1 selection must be one level ABOVE (stretch)
   - At least 1 must target a current transition skill
   - Subject-appropriate mechanics only (see Game Mechanic Decision Table §6.1
     and the Subject-to-Game Compatibility Matrix in NETS-Interactive-Game-Catalog.md)
5. LOAD pre-generated game_items tagged to THIS topic's standard_ref
6. CONSTRAINT: No mechanic appears more than 2x in one session
6b. BUZAN — Cortical Diversity Constraint (SOFT RECOMMENDATION, not a hard gate):
   - Tag each selected game's cortical modality:
     Verbal/Logical (Sentence Fill, Why Chain, Adaptive Quiz)
     Visual/Spatial (Tile Match, Memory Palace, Radiant Summary, Puzzle Lock, Memory Sprint)
     Kinesthetic/Motor (Notebook Capture, Movement Breaks)
     Strategic/Decision (Tic Tac Toe, Connect Four, Mystery Box)
     Productive/Generative (Peer Teaching, Reflection Journal)
   - RECOMMENDATION: At least 2 of the 3 selected games SHOULD come from DIFFERENT modalities
   - This ensures left+right brain synergy per session (Buzan's Cortical Skills principle)
   - ENFORCEMENT: This is a soft recommendation, not a production block. Sessions that naturally hit 2+ modalities (Story Mode = verbal/visual, Game Breaks = logical/spatial, Memory Palace = spatial/visual) comply automatically. A compliance check script (`scripts/check_cortical_diversity.py`) flags single-modality sessions for review but does NOT block production. Content creators should use judgment — purely mathematical chapters (e.g., algebra) may not naturally span modalities without artificial injection.
6c. BUZAN — Von Restorff Anchor:
   - The MIDDLE game (Game Break 2 of 3) is tagged as the "Von Restorff Anchor"
   - This game instance preferentially selects content items tagged "outstanding: true"
     (surprising facts, humorous framing, unusual visuals)
   - Rationale: the Sag (mid-session recall dip) is countered by an outstanding moment
7. ARRANGE interleaved with Story Mode segments
```

**Buzan also enhances individual game mechanics** — see §6.2 for per-game Buzan injections (Tile Match gets Dual Coding, Why Chain gets radiant visualization, Sentence Fill gets 80/20 keywords, etc.).