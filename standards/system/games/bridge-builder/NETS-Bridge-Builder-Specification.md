# NETS Bridge Builder — Game Mechanic Specification

**v1.1 — 2026-04-12** | Interactive Catalog Game #11 | Phase 3 | Constitution: UNIFIED v2.0

---

## Core Concept

A gap must be crossed. Student places structural elements (beams, cables, supports) by answering questions. Each piece costs budget points. Wrong answers waste budget without placing the piece. Build a stable bridge within budget to win.

**Inspiration:** Bridge Constructor (Headup Games) + NETS knowledge-gating model.

---

## How to Play

1. **Gap Presented** — Terrain, width, and load requirement shown.
2. **Budget Allocated** — Fixed points based on difficulty tier.
3. **Place Element** — Student selects where to place beam/cable/support.
4. **Answer Question** — Knowledge gate tied to the structural concept.
   - **Correct** → Element placed. Budget deducted.
   - **Wrong** → Element NOT placed. Budget STILL deducted (wasted).
5. **Repeat** — Until bridge spans gap or budget runs out.
6. **Load Test** — Simulated load crosses bridge. Stable = WIN. Collapse = FAIL.
7. **Retry** — Basic: **2 attempts max.** Premium: **3 attempts.** Budget adjusts on retry (+25%).

---

## Tier Overlay (Basic vs Premium)

| Dimension | Basic | Premium |
|-----------|-------|---------|
| **Availability** | Available (Phase 3 catalog game) | Available |
| **Content source** | Textbook-level questions (L1) | Textbook + extended materials (L1-L2+) |
| **Difficulty** | Standard physics — single/multi-force | AI adjusts harder: vector decomposition, optimization, supplementary problems |
| **Attempts** | **2 max.** Both fail → game marked failed | **3 attempts.** Budget adjusts each retry |
| **Budget** | Standard allocation | +15% budget bonus (more room for experimentation) |
| **Question types** | Numeric, MC (G1-5), short answer | Same + open reasoning for structural justification (G6+) |
| **AI evaluation** | Tier 1 (rule-based) + Tier 2 (open answers) | Tier 1 + Tier 2 + **Tier 3 (Socratic feedback on wrong placements)** |
| **Hints** | Pre-written hint arrays (1 per question) | Tier 3 dynamic hints — personalized to student's error |
| **Variations** | Classic, Time Attack | Classic, Time Attack + **Architect's Challenge, Earthquake Mode** |
| **Duolingo Mode** | Active (always) | Active (always) |

### Basic Failure Flow

```
Attempt 1 → Collapse / budget out
  → "Blueprint Review": shows which elements failed and why (stored feedback)
  → Retry with +25% budget
Attempt 2 → Collapse / budget out
  → Game marked FAILED. Duolingo Mode reviews the physics concepts.
  → No more retries this session.
```

### Premium Failure Flow

```
Attempt 1-2 → Collapse / budget out
  → Tier 3 Socratic feedback: "Which force was unbalanced? Where did load path break?"
  → Retry with +25% budget each time
Attempt 3 → Collapse / budget out
  → Game marked FAILED. Duolingo Mode activates.
```

---

## Structural Elements

| Element | Function | Question Theme | Visual |
|---------|----------|----------------|--------|
| **Support Beam** | Vertical load-bearing | Compression, weight distribution | Thick pillar, glows under load |
| **Horizontal Span** | Connects supports | Distance, geometry, material strength | Deck section, animates flow |
| **Tension Cable** | Holds span from above | Tension forces, angles, vectors | Taut wire, vibrates when loaded |
| **Foundation** | Anchors to terrain | Ground forces, stability, friction | Deep roots visual |
| **Cross-Brace** | Prevents lateral sway | Triangulation, rigidity | Diagonal bar, locks frame |

---

## Difficulty Scaling

| Tier | Gap Width | Budget | Max Wrong | Physics | Source |
|------|-----------|--------|-----------|---------|--------|
| Easy (PISA L2-3) | Narrow (3-4 elements) | 150% | 3 | Single forces | Textbook (both tiers) |
| Medium (PISA L3-4) | Standard (5-7 elements) | 100% | 2 | Multi-force, angles | Basic: textbook. Premium: + extended |
| Hard (PISA L5-6) | Wide (8-10 elements) | 75% | 1 | Vector decomposition | Premium only (extended materials) |

### Question Types by Tier & Grade

| Grade Band | Basic | Premium |
|-----------|-------|---------|
| Grades 1-4 | MC + visual matching ("Which shape is strongest?") | Same + guided reasoning ("Why is the triangle strong?") |
| Grade 5 | MC + numeric ("Calculate the load on this beam") | Same + short explanation ("Explain your calculation") |
| Grades 6-8 | Short answer + numeric (no MC) | Same + open reasoning ("Justify your support placement") |
| Grades 9-11 | Numeric + short derivation | Extended reasoning + optimization ("Minimize material while maintaining load capacity") |

---

## Scoring

| Outcome | XP |
|---------|-----|
| Bridge stable, budget remaining | Base 100 × (correct/total) |
| Strategy bonus (stable on first try) | +50 |
| Speed bonus (per question answered <5s) | +10 each |
| Perfect (zero wrong, budget surplus) | +100 bonus |
| Collapse / budget exhausted | 0 (retry available) |

---

## Subject Compatibility

| Subject | Fit | Basic Example | Premium Example |
|---------|-----|---------------|-----------------|
| **Math** | Primary | "Calculate span length given angle" | "Optimize beam angles to minimize total material" |
| **Physics** | Primary | "Which force — tension or compression?" | "Calculate resultant force vector at joint" |
| **Science** | Primary | "What material resists bending?" | "Compare tensile strength of steel vs aluminum alloy" |
| **Biology** | Adapted | "Which bone acts as a cross-brace?" | "Model skeletal load distribution in bipedal locomotion" |
| **History/Language** | Not recommended | — | — |

---

## Buzan Cognitive Science Integration

### TEFCAS Cycle

| Stage | Bridge Builder Moment |
|-------|----------------------|
| **Trial** | Student answers question to place element |
| **Event** | Element appears (correct) or vanishes with budget lost (wrong) |
| **Feedback** | Socratic hint: "Compression pushes down. Where do you see that?" Never reveals answer. |
| **Check** | IRT compares proficiency vs. item difficulty |
| **Adjust** | Next question difficulty adapts. Fewer budget points = higher stakes. |
| **Success** | Bridge holds under load test → XP + celebration |

On failure: *"Hali emas! Your engineering just gave us data. Which element failed first? That's your next Adjust."*

### MIG (Memory Graph Effects)

| Effect | Implementation |
|--------|---------------|
| **Primacy** | First element placed = foundation concept. Most remembered. Teach load-bearing here. |
| **Recency** | Final keystone placement = emotional peak. XP burst timed here. |
| **Association** | Link to local Uzbek bridges (irrigation canals, bazaar roofs). |
| **Von Restorff** | Dramatic failure animations — cable snaps with sparks. Weird = memorable. |
| **The Sag** | After 5-6 placements, "Blueprint Review" pause resets primacy curve. |

### Memory Systems

| System | Application |
|--------|------------|
| **Link System** | Bridge IS a chain: foundation → support → span → closure. Each triggers the next. |
| **Memory Palace** | Registan Square corners = structural zones. N: Compression. E: Tension. S: Load. W: Materials. |
| **SMASHIN' SCOPE** | Failed elements use ≥3 qualities: Synaesthesia (snap sound), Movement (recoil), Exaggeration (sparks). |

### Mind Mapping

| When | What |
|------|------|
| Pre-game | 4-branch Radiant Anchor: Foundation / Supports / Span / Load. 1 keyword per branch. Min 3 colors. |
| During game | Strategy sketch: map where elements go before placing. |
| Post-game (Phase 5) | Radiant Summary: drag-drop physics terms onto completed bridge Mind Map. |

### BOST Study Flow

| BOST Step | Bridge Builder Phase |
|-----------|---------------------|
| Browse + Mind Map | Pre-game: "What do you know about bridges?" |
| Questions/Goals | "One thing I want to figure out" — revisited in Phase 7 |
| Overview | 30s flashcard sprint: compression, tension, load |
| Inview | The game itself (Phase 3) |
| Review | Phase 5 consolidation + Phase 7 reflection |

**Spaced Repetition:** 10 min (Phase 5) → 24h (Memory Sprint) → 1 week (Boss Rematch) → 1 month (Champion's Arena).

### Speed Reading in Questions

- **Chunked format:** `[Beam: 10m] [Load: 500kg] → [Where: Support?]`
- **Guided pacer:** Focus dot at IRT-adjusted speed.
- **Pre-game Structural Skimming (30s):** Skim headings → build 3-branch Mind Map.

---

## Variations

| Variant | Description | Tier | Unlock |
|---------|-------------|------|--------|
| **Classic** | Standard gap crossing with budget | Both | Default |
| **Time Attack** | Same rules + 3-minute timer | Both | After 5 wins |
| **Architect's Challenge** | Peg System encoding (G6+): recall Peg images before placement | Premium | Level unlock |
| **Earthquake Mode** | Bridge built, then seismic test — reinforce under pressure | Premium | PISA L5+ |
| **Collaborative Build** | Two students share budget, alternate placements | Both | Future (multiplayer) |

---

## Edge Cases

```
Low-end devices: Skip Bridge Builder (high render). Substitute Tile Match / Adaptive Quiz.
AI unavailable: Pre-fetched Tier 1 questions. Hints fall back to stored arrays.
Budget exhausted: Collapse → retry with +25% budget.
G5 working memory: Max 4-5 elements. Simplify to 3-element bridges. No Peg variant.
Basic 2-attempt + Catch-Up: Still 2 attempts, but gap simplified (fewer elements).
Duolingo Mode: Always active both tiers — reviews physics concepts on fail.
```

---

## Locked Constraints

Phase 3 only (dual-catalog rule) | Mandatory `transition_skill` tag | No real-money advantage | Hidden difficulty labels | Accessibility: WCAG 2.1 AA | Duolingo Mode always active | Basic = full educational mission
