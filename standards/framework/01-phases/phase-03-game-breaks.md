---
name: Phase 3 — Game Breaks
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §5.3 (lines 810-865) + §22 session
---

# Phase 3 — Game Breaks

> **ACTIVE FOR: All families.** This is REAL practice — not warm-up (that is Phase 1 Memory Sprint). Game Breaks build and deepen skill through gamified repetition and dopamine engagement loops.

---

## Purpose (WHAT)

Apply and consolidate newly introduced concepts through three sequenced game mechanics that each target a specific cognitive skill. Game Breaks are the primary scored practice block of the session — they drive mastery through repetition made engaging, not through narrative or transfer (those are Phase 2 and Phase 4).

Phase 3 is scored and contributes 30% of the session's total score.

---

## Structure (HOW)

**Three games per session, sequenced with transitions:**

```
[Game 1] → slide+blur transition, "1/3" indicator → [Game 2 — Von Restorff Anchor] → slide+blur, "2/3" → [Game 3] → phase exit
```

**Game selection rules (DUAL-CATALOG RULE):**

```
SELECT 3 games such that:
  - AT LEAST 2 come from the Default Pool (16 mechanics)
  - AT LEAST 1 comes from the Interactive Catalog (7 games)
  - AT LEAST 1 matches student's CURRENT Bloom's level (reinforcement)
  - AT LEAST 1 is ONE LEVEL ABOVE student's current level (stretch)
  - AT LEAST 1 targets a current in-progress transition skill
  - No mechanic appears more than 2x in one session
  - All 3 must be subject-appropriate (see Subject-to-Game Compatibility Matrix)
```

**Game mechanics live in their own docs — do NOT duplicate them here:**
- Default Pool (16 mechanics): `standards/library/catalog/NETS-Game-Catalog-Summary.md`
- Interactive Catalog (7 games): `standards/library/catalog/NETS-Interactive-Game-Catalog.md`
- Detailed game specs: `system/games/Game_Mechanics_Docs/` (19 numbered docs)
- Subject-to-Game Compatibility Matrix: `standards/library/catalog/NETS-Interactive-Game-Catalog.md`

This component spec governs SELECTION RULES and INTEGRATION. Game internals are the catalog's responsibility.

**Aniq Fanlar mandatory rule (from §22 session):**
For all Math family subjects, Adaptive Quiz is mandatory in Phase 3 and is the **only capture-bearing game** within the phase. Adaptive Quiz must be one of the three selected slots. It may be Game 1, 2, or 3.

**Capture rule:**
Any calculation step in any game triggers Notebook Capture. Reference: `00-core/capture-rule.md`. The mechanic itself (camera icon → confirm dialog) is shared UX defined in that primitive. This component does not re-specify it.

**Buzan — Von Restorff Anchor:**
Game 2 of 3 is tagged as the Von Restorff Anchor. The content pipeline preferentially loads items tagged `outstanding: true` (surprising facts, humorous framing, unusual visuals) into Game 2. Rationale: the mid-session recall dip (Sag effect) is countered by a memorable/outstanding moment at the session midpoint.

**Buzan — Cortical Diversity (soft recommendation):**
```
Tag each selected game's cortical modality:
  Verbal/Logical:        Sentence Fill, Why Chain, Adaptive Quiz
  Visual/Spatial:        Tile Match, Memory Palace, Radiant Summary, Puzzle Lock, Memory Sprint
  Kinesthetic/Motor:     Notebook Capture, Movement Breaks
  Strategic/Decision:    Tic Tac Toe vs AI, Connect Four, Mystery Box
  Productive/Generative: Peer Teaching, Reflection Journal

RECOMMENDATION: At least 2 of the 3 selected games SHOULD come from different modalities.
ENFORCEMENT: Soft. A compliance script flags single-modality sessions for review but does NOT
block production. Purely mathematical chapters may not naturally span modalities — use judgment.
```

**Removed games (NEVER select or reference):**
Blackjack 21, Bridge Builder, Minefield Navigator, Escape Room, Codebreaker.

**Frozen games (v2+ only — do NOT use in v1 production):**
Why Chain, Territory Conquest, Connect Four, Word Ladder, Puzzle Lock, Reaction Chain.
These games are designed and specced in the catalog but deferred from v1 for simplicity. They may be activated after pilot validation.

**v1 active game pool (ship confidently):**
Tile Match, Memory Match (Blitz), Sentence Fill, Adaptive Quiz, Notebook Capture.
These 5 mechanics are proven, simple, tap-based, instantly understood, work on any phone.

---

## Cognitive load

| Axis | Range |
|------|-------|
| Bloom's taxonomy | L2 (Understand) — L4 (Analyze) |
| PISA | L2 — L3 |
| Time budget | 18–23 min total (standard) · up to 30 min (extended) |
| Per-game budget | 6–8 min each (standard) |
| Cognitive mode | Retrieval practice → application → pattern recognition |
| Score weight | 30% of session total |

---

## Inputs

- Phase 1 and Phase 2 (if applicable) aggregate outputs: score %, skill breakdown, PISA estimate
- Current `standard_ref` (topic tag — used to load pre-generated game items)
- Student PISA level and weakest skill axis (from `00-core/routing-algorithm.md`)
- Student in-progress transition skills
- Subject family tag (determines compatibility matrix and Aniq Fanlar override)
- Grade band (determines item difficulty tier distribution: 40% easy / 40% medium / 20% hard)
- `00-core/capture-rule.md`
- Subject-to-Game Compatibility Matrix (`standards/library/catalog/NETS-Interactive-Game-Catalog.md`)

---

## Outputs

- Per-game: score %, item-level correct/incorrect, time-per-item, skill tags `[Bloom: LX | PISA: LX]`
- Phase aggregate: `phase_03_score` (% of available points), skill axis deltas
- Capture events: list of items where Notebook Capture was triggered (passed to Phase 7 analytics)
- Von Restorff item IDs logged (for session-level recall analysis downstream)
- Updated PISA level estimate (if game performance diverges from prior estimate)

---

## Adaptable parameters

| Parameter | Default | Override per family | Override per archetype |
|-----------|---------|---------------------|------------------------|
| Game count | 3 | — | Extended mode: 3–4 |
| Items per game | 5–8 | Aniq Fanlar: Adaptive Quiz may auto-extend by difficulty | Review archetype: upper bound |
| Difficulty distribution | 40% easy / 40% medium / 20% hard | — | — |
| Adaptive Quiz requirement | Optional | Aniq Fanlar: MANDATORY, capture-bearing | — |
| Interactive Catalog minimum | 1 of 3 | — | — |
| Default Pool minimum | 2 of 3 | — | — |
| Von Restorff slot | Game 2 | — | — |

---

## Subject-specific examples

**Aniq Fanlar (Mathematics — Grade 7, Algebra: linear equations)**

Slot 1 (Default, reinforcement): Sentence Fill — equation components drag into position; targets Bloom L2 (understand structure).
Slot 2 (Von Restorff Anchor, Default): Tic Tac Toe vs AI — student wins squares by solving short linear equations; outstanding items: equations that appear in real engineering contexts (bridge load, electricity bills).
Slot 3 (Interactive, stretch + Adaptive Quiz): Adaptive Quiz — multi-step equation solving with Notebook Capture on each calculation step; targets Bloom L3–L4.

**Tabiy Fanlar (Biology — Grade 8, photosynthesis)**

Slot 1 (Default, reinforcement): Tile Match — match process names to equation fragments; Bloom L2.
Slot 2 (Von Restorff Anchor, Interactive): Puzzle Lock — inputs to the light-dependent reaction must be placed correctly to "unlock" the next stage; outstanding item: the fact that one tree produces ~100 kg of oxygen per year.
Slot 3 (Default, stretch): Why Chain — "Why does photosynthesis stop at night? → Why does glucose production stop? → Why does this affect cellular respiration?"; Bloom L4.

**Til Fanlar (English — Grade 9, Present Perfect)**

Slot 1 (Default, reinforcement): Sentence Fill — gap-fill with Present Perfect vs. Past Simple in authentic-looking news headlines; Bloom L2.
Slot 2 (Von Restorff Anchor, Default): Memory Palace — student mentally places five irregular past participles in rooms of the IT Park building; outstanding item: an unusual real verb ("to broadcast → broadcast").
Slot 3 (Interactive, stretch): an Interactive Catalog game appropriate to grammar practice (see Compatibility Matrix).

**Ijtimoiy Fanlar (History — Grade 10, causes of WWI)**

Slot 1 (Default, reinforcement): Tile Match — match events to dates and actors; Bloom L2.
Slot 2 (Von Restorff Anchor, Interactive): Knowledge-gated interactive game (see Compatibility Matrix); Von Restorff item: the assassination route Gavrilo Princip took — he had turned back twice before the car reversed into his position.
Slot 3 (Default, stretch): Why Chain — causal chain from assassination to mobilization; Bloom L4.

---

## Verification rules

1. **Count rule:** Exactly 3 game slots per standard session (3–4 for extended). Fewer than 3 = production block.
2. **Dual-catalog rule:** At least 1 game from Interactive Catalog + at least 2 from Default Pool. Violation = production block.
3. **Aniq Fanlar override:** If `subject_family == "aniq-fanlar"`, Adaptive Quiz must be present. Missing = production block.
4. **Capture rule:** Any calculation step question in any game must carry a Notebook Capture trigger. Reference `00-core/capture-rule.md`. Calculation questions without capture trigger = violation.
5. **No removed games:** Games from the removed list (Blackjack, Bridge Builder, Minefield Navigator, Escape Room, Territory Conquest, Codebreaker) must never appear in slot selection.
6. **Bloom/PISA tags:** Every item carries `[Bloom: LX | PISA: LX]`. Missing tags = production block.
7. **Von Restorff slot:** Game 2 must be tagged `von_restorff_anchor: true`. Missing tag = non-blocking warning.
8. **Cortical diversity check:** `scripts/check_cortical_diversity.py` flags sessions where all 3 games share a single cortical modality. Non-blocking — content creator judgment applies.
9. **No Story Mode in game slots:** "Story Mode" is not a game mechanic selectable for Phase 3. It is a retired universal phase. Selecting it as a Phase 3 game is a production error.
10. **Difficulty distribution:** Item mix across all 3 games should approximate 40/40/20 (easy/medium/hard). `scripts/check_blueprint_compliance.py` flags sessions outside 35–45% easy band.

---

## Integration points

**Entry (called by Phase 2 exit or Phase 1 exit for non-Language families):**
- Receives: prior phase aggregate scores, updated PISA estimate, current `standard_ref`, family tag, grade band
- Loads: game selection algorithm output (3 pre-selected games with pre-generated items)
- Guard: no guard condition — Phase 3 runs for all families

**Exit (calls Phase 4):**
- Emits: `phase_03_score`, per-skill axis results, capture event list, PISA estimate update
- Phase 4 uses `phase_03_score` to confirm student is above 60% passing threshold before proceeding
- Below 60%: `00-core/routing-algorithm.md` may route to remediation variant (see routing-algorithm for full logic)

**Cross-references:**
- `00-core/capture-rule.md` — Notebook Capture mechanic
- `00-core/routing-algorithm.md` — 60% pass threshold, post-phase routing
- `00-core/skill-taxonomy.md` — maps game outputs to the 6 skill axes
- `00-core/hp-damage-baseline.md` — Phase 3 items are NOT HP-damage items (HP system applies in Phase 6 Final Boss)
- `00-core/difficulty-adaptation.md` — item difficulty tier rules
- `standards/library/catalog/NETS-Game-Catalog-Summary.md` — Default Pool game specs
- `standards/library/catalog/NETS-Interactive-Game-Catalog.md` — Interactive Catalog + Compatibility Matrix
- `system/games/Game_Mechanics_Docs/` — per-game detailed specifications

---

## UX/animation spec

**Between-game transitions:**
- Animation: slide (outgoing game card slides left, incoming slides in from right) + blur (outgoing card blurs out over 200ms)
- Progress indicator: persistent "N/3" counter in the top-right corner of the phase container, updates on each transition
- No score reveal between games — cumulative score shown only at phase exit

**Within-game chrome:**
- Shared card chrome (borders, background, header) defined in shared UX spec (`system/ui-ux/`)
- Each game's internal layout is specified in its own Game Mechanic Doc
- Phase-specific: a thin Phase 3 color stripe at top of the card (distinct from Phase 1 and Phase 4 color stripe)

**Notebook Capture UX (shared with Phase 4):**
- Defined in `00-core/capture-rule.md`
- Trigger: calculation step confirmed correct → camera icon appears bottom-right
- Flow: tap camera icon → "Save to Notebook?" confirm dialog → confirm → brief green flash → dismissed
- This component does not re-specify internal capture UX — reference the primitive

**Von Restorff Anchor visual signal:**
- No explicit "this is special" label shown to student
- Outstanding items may have a subtle ambient effect (e.g., a faint color pulse on the card background on entry) — not a popup or announcement
- The "outstanding" designation is pipeline metadata, not a student-facing badge

**Phase exit screen:**
- Shows Phase 3 aggregate score with a short skill-breakdown bar (memory / application / critical thinking axes)
- 3-second auto-advance with a tap-to-skip option
- Score feeds into the session progress ribbon visible throughout
