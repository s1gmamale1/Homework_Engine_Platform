# Memory Palace — Method of Loci Spatial Anchoring

**Default Mechanic #5**
**Bloom's Level:** Remember
**PISA Level:** 1-2
**AI Tier:** Tier 1 ($0)
**Research Basis:** Method of Loci (Maguire et al., 2003)
**Expected Gain:** +300% retention
**Session Phase:** Phase 3 (Game Breaks) or Phase 5 (Consolidation)

---

## 1. Core Game Mechanics

Memory Palace implements the **Method of Loci** — an ancient spatial memory technique validated by modern neuroscience. The student places 5 subject-relevant concepts at 5 distinct locations within a familiar mental space, then practices retrieving them through guided recall.

### 4-Step Process (3-4 minutes total)

**Step 1 — Select Palace (30 seconds):** The student chooses from 4 available palaces:
- **Registan Square (default):** 1) Ulugh Beg Madrasa entrance, 2) Sher-Dor lion mosaic, 3) Tilya-Kori dome, 4) Central fountain, 5) West archway
- **Student's Home:** 1) Front door, 2) Kitchen, 3) Living room TV, 4) Bedroom window, 5) Backyard gate
- **School:** 1) Main gate, 2) Classroom door, 3) Library shelves, 4) Sports field, 5) Cafeteria counter
- **Local Bazaar (Chorsu):** 1) Market entrance arch, 2) Spice stall, 3) Bread oven (tandir), 4) Fabric section, 5) Fruit pyramid display

**Step 2 — Place 5 Concepts at 5 Locations (60 seconds):** The system presents 5 concepts from the current lesson. For each concept, the student selects a palace location and places the concept there with a vivid mental image guided by the system.

**Step 3 — Guided Mental Walkthrough (30 seconds):** The student closes their eyes (screen dims). The AI narrates a walk through the palace in order, prompting visualization of each concept at its location with sensory cues.

**Step 4 — Recall Test (5 questions, 60 seconds):** The student answers 5 questions retrieving concepts from specific palace locations. Format: G1-4 = MC with visual hints, G5-7 = free recall with first-letter hint, G8-11 = open recall with no hints.

### Grade Scaling
- **G1-4:** 3 concepts at 3 locations. Home and School only. MC recall only.
- **G5-7:** Standard 5 concepts at 5 locations. All 4 palaces. First-letter hints.
- **G8-11:** 5 + 2 bonus concepts (7 total). No hints. Multi-step processes and abstract terms.

---

## 2. Tier-Based Access Control

| Feature | Basic Tier | Premium Tier |
|---------|-----------|--------------|
| **Session Access** | Available in Phase 3 Game Breaks | Same + on-demand access from Library |
| **Palace Options** | Registan + 1 unlocked per month | All 4 immediately + 2 exclusive (Silk Road Caravan, Samarkand Observatory) |
| **Concept Count** | 5 concepts (3 for G1-4) | Same + optional bonus for G8-11 (7 total) |
| **Visual Polish** | Static illustrations | Animated walkthroughs, ambient sound, particle effects |
| **Recall Mode** | Standard (MC/hints/open by grade) | Same + "Reverse Recall" — given concept, identify location |
| **Spaced Revisit** | Offered if recall < 60% | Automated spaced-repetition (1d, 3d, 7d, 14d) with notifications |
| **Palace Gallery** | View last palace created | Full history, heat map of strongest/weakest bonds |

> **Basic Tier Guarantee:** All students receive the full Method of Loci experience with 5 concepts and 4 palace options over time. Premium adds exclusive themes, animated polish, and automated spaced-revisit scheduling — but the core memory technique is identical across tiers.

---

## 3. Buzan Integration: Spatial Synesthesia

- **Location as Memory Anchor:** Each palace location serves as a fixed peg. Buzan emphasized that the brain remembers places better than abstract information — anchoring concepts to familiar locations makes recall automatic navigation rather than effortful retrieval.
- **Color Coding by Concept Family:** Concepts from the same family share a color within the palace. Biology = green shades, History = gold, Math = blue. The color gradient during walkthrough reinforces category membership.
- **Exaggerated Imagery (Bizarre > Literal):** The system suggests absurd, sensory-rich mental images. "The mitochondria isn't just at the fountain — it's *powering* the fountain, shooting water 10 meters high." Per Buzan: exaggerated imagery is 3-7x more memorable.
- **Sensory Layering (Synesthesia):** Each palace stop includes a non-visual cue: sound of bazaar spices, texture of madrasa tile work, smell of bread from the tandir. Multi-sensory encoding creates multiple retrieval paths.
- **Radiant Branching (Inter-Palace Connections):** When a student builds multiple palaces, the system draws connections between related concepts in different palaces, building radiant knowledge networks organically.

---

## 4. Question Styles & Interaction Mechanics

| PISA Level | Recall Question Format | Concept Complexity | Cognitive Target | Hint Level |
|------------|----------------------|-------------------|------------------|------------|
| **L1** | MC: "At the kitchen, you placed: A) Water B) Cell wall C) Oxygen" | Single concrete noun | Direct location-to-concept recall | Full visual hint: thumbnail of concept image |
| **L2** | MC with distractor + property hint | Term with definitional property | Property-assisted recall from location | First-letter hint + one defining property |
| **L3** | Free recall: "What at the West archway? C____" | Abstract concept or process step | Unaided retrieval with minimal cue | First letter + syllable count |
| **L4** | Process recall: "Walk through the 3 steps at the spice stall, in order" | Multi-step process or causal chain | Sequential recall from single anchor | First step's initial letter |
| **L5** | Cross-palace synthesis: "How does the fountain concept relate to the bazaar concept?" | Related concepts from different palaces | Analogical reasoning across domains | No hints |
| **L6** | Open extension: "Add a 6th concept. Where and what vivid image?" | Student-generated concept + novel association | Creation — design new palace node | No hints. Evaluated on placement logic, imagery, accuracy |

> **Placement Layer:** During Step 2, the system never rejects a student's location choice. If a location is already occupied, it gently redirects: "That spot already holds your previous concept. How about the tandir oven?" Focus is on *encoding quality*, not placement accuracy.

---

## 5. Victory Conditions & Scoring

### A. Grade Computation

This mechanic feeds **Type A (Accuracy-Based)** data into the student's learning curve:

| What Gets Recorded | Source | Curve Impact |
|---|---|---|
| Accuracy (%) | Correct recall answers / 5 total | Primary — determines Level |
| Recall speed | Seconds per correct answer | Secondary — feeds Efficiency metric |
| Hints used | Count of hints consumed | Tertiary — fewer hints = higher confidence |
| Attempts (cumulative) | Total palace sessions | Feeds curve-fitting (y = K × attempts^n) |

### B. Session Report Card

After this mechanic, the student sees:

```
Memory Palace — [Topic]
████████░░ 62% (Apprentice ↗)
Velocity: n=0.48 (improving)
Recall speed: 8s/answer (getting faster ✓)
~3 sessions to Proficient
```

### C. Outcome Grades

- **Perfect Recall (5/5):** "Ajoyib!" — Palace glows. Grade: Proficient ✓ or Mastered ★ if consistent across 3+ sessions
- **Strong (4/5):** "Yaxshi!" — 4 of 5 illuminated. Missed location shows faint pulsing outline
- **Partial (3/5):** "Hali emas" — Second walkthrough of 2 missed locations offered
- **Failed (0-2/5):** Grayscale palace. All 5 correct pairs revealed. Retry offered. If declined or second attempt fails, flagged as pending mastery.

### D. Long-Term Tracking

- **Palace Builder Badge:** 10 unique palaces built and recalled successfully
- **Memory Architect Achievement:** >80% recall across 20+ palaces
- **Palace Retirement:** 3 correct recalls across spaced sessions → "Mastered — Palace Retired" → Hall of Fame

### E. "Hali Emas" (Not Yet) Framing

There is no "fail" state — only "not yet." A student who scores 2/5 is showing the system which location-concept bonds need reinforcement. The grayscale palace display is a learning signal, not a shame signal. Every placement effort (Step 2) counts as encoding practice — the act of creating mental images strengthens memory even if recall is imperfect.

---

*NETS Elite Mechanic Specification — Memory Palace v1.0*
