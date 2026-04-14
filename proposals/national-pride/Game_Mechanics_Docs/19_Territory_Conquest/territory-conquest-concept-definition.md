# Territory Conquest: Concept-Definition Edition

> Interactive Knowledge-Gated Mechanic #10 — Simplified Risk-Style 1v1 Area Control

**Players:** 1-6 (1 Student + up to 5 AIs) | **Modes:** Standard Duel, FFA, One-for-All (Premium) | **Buzan Integrated** | **Bloom's:** Apply/Analyze | **PISA:** 3 | **AI Tier:** Tier 1

---

## 1. Core Game Mechanics

Territory Conquest is a **simplified Risk-style area control game** played on a hex or square grid map. Each cell on the map represents a territory. The student and AI opponents take turns expanding and attacking.

- **Setup:** Each entity (student + AIs) starts with a Capital territory and 2-3 adjacent starter territories. Unclaimed neutral territories fill the remaining map.
- **Attack Phase:** On their turn, the student selects an adjacent enemy or neutral territory to attack. A **subject question** appears. Correct answer = attack succeeds, territory is captured. Wrong answer = attack fails and the student loses one of their own territories adjacent to the target (retreat penalty).
- **Reinforcement Phase:** After each turn, the active entity receives reinforcement troops equal to the number of territories they control divided by 3 (minimum 1). Reinforcements can be placed on any owned territory.
- **AI Behavior:** AI entities act on their turns using a weighted strategy: prefer attacking weaker neighbors, defend capitals when threatened, expand into neutral territory when safe. AI "difficulty" scales with grade level (lower grades = AI makes suboptimal choices more often).

**Map scale increases dynamically with player count:**

- **2 entities (1 Student + 1 AI):** 8x8 grid (64 territories).
- **3 entities (1 Student + 2 AIs):** 8x8 grid.
- **4 entities (1 Student + 3 AIs):** 10x10 grid (100 territories).
- **5 entities (1 Student + 4 AIs):** 10x10 grid.
- **6 entities (1 Student + 5 AIs):** 12x12 grid (144 territories).

**Reinforcement Event (~10% chance mid-game):** After turn 6, there is a 10% chance per turn of a "Reinforcement Event" — a random neutral territory spawns a bonus army. The first entity to answer a bonus question correctly claims it. This prevents stalemates and adds unpredictability.

**Cross-Subject Review (Big Boss / Mythical Boss):** In review sessions, questions rotate across all subjects the student has studied. A math question may lead to capturing a territory, then a history question on the next attack. This forces cross-domain retrieval under strategic pressure.

### Strategic Victory Conditions

Two paths to victory exist:

- **Strategic Victory (Turn 12):** If no entity has achieved Total Domination by turn 12, the game ends. The entity controlling the most territories wins. Ties broken by: (1) most capital captures, (2) most contiguous territory chain, (3) coin flip.
- **Total Domination:** Capture all enemy capitals. Instant win regardless of turn count. This is the highest-difficulty path and requires sustained correct-answer streaks across multiple subjects.

**FFA (Free-for-All) Mode (Premium):** All entities are independent. Last player standing (most territories at Turn 12 or last capital remaining) wins. Temporary alliances are not allowed — pure competition.

**One-for-All Mode (Premium):** 5 AIs coordinate against the student. The student is the underdog defending their capital against a coalition. Victory requires capturing at least 2 AI capitals before Turn 12. This is the highest-stakes mode and awards the most XP.

---

## 2. Tier-Based Access Control

Territory Conquest is part of the 28-mechanic core. Basic students receive the standard duel experience; Premium unlocks multiplayer variants and strategic depth.

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 Game Breaks (dual-catalog selection) | Same + on-demand access from Library |
| **Game Modes** | Standard Duel only (1 Student vs 1 AI) | Standard Duel + FFA (up to 6 entities) + One-for-All (5 AIs vs student) |
| **Max Map Size** | 8x8 grid only | Up to 12x12 grid (scales with player count) |
| **AI Count** | 1 AI enemy only | 1-5 AI enemies |
| **Visual Polish** | Standard map rendering, basic territory colors | Animated troop movements, territory glow effects, battle animations |
| **Reinforcement Events** | Not available | 10% chance per turn mid-game — bonus territory spawns |
| **Victory Paths** | Total Domination only (capture all enemy territories) | Total Domination + Strategic Victory (Turn 12 count) + One-for-All underdog challenge |

> **Basic Tier Guarantee:** The Standard Duel (1v1) provides the full strategic learning experience. The core mechanic — answering correctly to expand, answering wrongly to lose ground — is identical across tiers. Premium adds scale, variant modes, and cosmetic depth.

---

## 3. Buzan Integration: Spatial-Territorial Memory

Territory Conquest leverages **Tony Buzan's spatial memory and color association** principles to bind content knowledge to geographic positions on the map.

- **Color Hooks (Territory Identity):** Each player's territories are rendered in a distinct high-contrast color (student = blue, AI-1 = red, AI-2 = green, etc.). When a territory changes hands, the color transition animates with a 0.5s pulse — the old color "retreats" as the new color "advances." This creates a vivid visual narrative of conquest that the student remembers far better than abstract scores.
- **Radiant Branches (Contiguous Territory Chains):** When a student controls a contiguous chain of 5+ territories, a glowing border appears connecting them — a "supply line." This visual chain reinforces the concept that knowledge builds cumulatively. Breaking an enemy's supply line (capturing a key territory) triggers a "Supply Line Severed" notification, reinforcing strategic cause-and-effect.
- **Imagery & Exaggeration (Capital Monuments):** Each capital displays a subject-specific monument icon (e.g., a math capital shows a giant calculator, a history capital shows a fortress). When a capital is captured, the monument "falls" with dramatic animation, and the conquering player's monument rises in its place. This exaggerated imagery creates strong episodic memories tied to the content questions that enabled the capture.
- **Memory Palace Anchor (Conquest Chronicle — rare, ~5% of captured territories):** Occasionally, a captured territory contains a Chronicle Scroll. Reading it places the territory and the question that captured it into the student's Conquest Chronicle — a persistent gallery showing their strategic history across sessions. Students who collect Chronicle Scrolls from all subjects unlock the "Grand Strategist" achievement in the Bilim Bazasi.

---

## 4. Question Styles & Interaction Mechanics

Territory Conquest gates every attack and defense behind subject questions. The question complexity scales with the PISA level being targeted.

| PISA Level | Question Type | Attack Scenario | Cognitive Target | Feedback Style |
|-----------|--------------|---------------|-----------------|---------------|
| **L1** | Direct recall (e.g., "What is 7 x 8?") | Attack neutral territory — simple fact check | Automatic retrieval fluency | Instant: correct = green flash + territory captured; wrong = red flash + retreat |
| **L2** | Property identification (e.g., "Which of these is a prime number?") | Attack lightly defended territory — requires basic reasoning | Concept application in context | Correct answer shows brief explanation; wrong answer shows correct answer + territory loss |
| **L3** | Multi-step reasoning (e.g., "If x + 5 = 12, what is x x 3?") | Attack enemy territory — requires inference chain | Causal analysis under pressure | Step-by-step breakdown shown after answer; wrong answer costs territory and shows full solution |
| **L4** | Scenario analysis (e.g., data interpretation from a chart) | Attack fortified territory — complex problem with distractors | Evaluation of evidence, discrimination between plausible options | Full solution path shown; territory loss includes "What went wrong" hint |
| **L5** | Multi-source synthesis (e.g., combine two facts to derive a third) | Attack capital — hardest questions guard capitals | Synthesis across information sources | Detailed explanation; capital defense questions trigger "Siege Mode" — 2 questions in a row, both must be correct |
| **L6** | Novel problem requiring original reasoning | Final Boss capital — mythic difficulty | Original creation/solution under maximum strategic pressure | Full worked solution + "General's Analysis" explaining the reasoning approach. Wrong answer = immediate capital defense counterattack. |

> **Cross-Subject Gate Rule:** In Big Boss review sessions, consecutive attacks never draw from the same subject. If the last attack was math, the next will be history, science, or language. This forces cognitive flexibility and prevents subject-specific warm-up bias.

---

## 5. Victory Conditions & Scoring

### A. Total Domination Victory

Capture all enemy capitals. The victory screen shows:

- **Flawless Conquest:** No territories lost during the entire campaign. Bonus +500 XP + "Undefeated Warlord" badge.
- **Hard-Fought Victory:** Lost 1-3 territories. Bonus +200 XP.
- **Narrow Victory:** Lost 4+ territories. Standard XP. "Hali emas" framing for lost territories — they are shown on the recap map with correct answers.

### B. Strategic Victory (Turn 12)

If no Total Domination occurs by turn 12, the entity with the most territories wins:

- **Student wins:** +300 XP + "Strategist" badge. Map recap shows all territories controlled at game end.
- **Student loses:** "Hali emas" screen. The map is shown with all correct answers for territories the student failed to capture. XP awarded for each territory successfully captured during the game (no XP for the loss itself).

### C. One-for-All Victory (Premium)

Student must capture at least 2 AI capitals before Turn 12:

- **Victory:** +500 XP + "Underdog Champion" badge — the highest single-game XP reward in Territory Conquest.
- **Defeat:** +100 XP per captured territory (encouragement: "You held the line against 5 armies"). Map recap shows which capitals were closest to falling.

### D. Scoring Breakdown

| Event | XP | Notes |
|-------|----|-------|
| Correct attack (neutral territory) | +80 | Base reward for expansion |
| Correct attack (enemy territory) | +120 | Higher value for dislodging an opponent |
| Capital capture | +250 | Major milestone — requires harder questions |
| Territory lost (own) | -20 | Small penalty for failed attack or defense |
| Flawless Conquest | +500 | Zero territories lost entire game |
| Hard-Fought Victory | +200 | Lost 1-3 territories |
| Strategic Victory (Turn 12) | +300 | Most territories at game end |
| One-for-All Victory | +500 | Captured 2+ AI capitals vs 5 AIs |
| Reinforcement Event claim | +60 | Answered bonus question correctly |
| Chronicle Scroll found | +100 | Rare discovery bonus |
| Capital defense (correct) | +150 | Successfully defended your capital |

### E. Defeat Framing

Loss is always framed as **"Hali emas"** (not yet). The defeat screen shows the map with the student's remaining territories highlighted in gold, and all lost territories display the correct answers they missed. The message reads: "Your empire will rise again. Study these territories and return stronger." No punishment beyond lost time — the student retains partial XP for territories captured and is encouraged to retry.

---

*NETS Elite Mechanic Specification — Territory Conquest: Concept-Definition Edition v1.0*
