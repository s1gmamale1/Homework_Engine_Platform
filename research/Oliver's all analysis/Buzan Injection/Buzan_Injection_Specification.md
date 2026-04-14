# Buzan 34-Method Injection Specification — NETS Homework Engine

**Version:** 1.0 | April 2026 | For: NETS Content & Engineering Teams
**Sacred Rule:** Content is sacred. Buzan = the HOW, never the WHAT.
**Methods:** All 34 Buzan methods injected across 5 layers.

---

## Table of Contents

1. [BOST & TEFCAS Alignment (Sprint 1)](#deliverable-3-bost--tefcas-alignment-sections)
2. [Content Pipeline Quality Gates (Sprint 1)](#deliverable-13-content-pipeline-quality-gates)
3. [UI/UX Spec Amendments (Sprint 1)](#deliverables-15-18-uiux-spec-amendments)
4. [AI Tutor Language (Sprint 1)](#deliverables-22-24-ai-tutor-language)
5. [Radiant Summary Game Mechanic (Sprint 2)](#nets-game-mechanic--full-definition-radiant-summary)
6. [Peg System Game Mechanic (Sprint 2)](#nets-game-mechanic--full-definition-peg-system)
7. [Phase 1 & Phase 2 Amendments (Sprint 2)](#sprint-2-phase-1--phase-2-amendments)
8. [Phase 3-7 + Phase 0-A Amendments (Sprint 3)](#sprint-3-phase-3-7--phase-0-a-amendments)
9. [UI/UX Feature Specs (Sprint 3)](#sprint-3-uiux-feature-specs)
10. [Future Roadmap (Sprint 4)](#sprint-4-future-roadmap-items)

---



# Buzan Injection — Deliverable 3: BOST & TEFCAS Alignment Sections

**Status:** Amendment to NETS-Homework-Engine-UNIFIED.md preamble  
**Methods Injected:** #11 (TEFCAS), #27 (BOST)  
**Layer:** B (Cross-Cutting) + A (Phase-Bound)  
**Sacred Rule:** Content unchanged. This is a framing/documentation alignment only.

---

## Section A: TEFCAS — The Cognitive Engine Behind the 7-Phase Flow

The NETS 7-Phase Homework Engine is structurally aligned with Tony Buzan's **TEFCAS** model — the brain's natural cybernetic learning loop. TEFCAS is not a new addition; it is the *naming* of what the engine already does. Making this alignment explicit allows the AI tutor to use TEFCAS vocabulary consistently and gives content authors a shared mental model.

### TEFCAS-to-NETS Phase Mapping

| TEFCAS Step | Definition | NETS Phase | How It Already Works |
|---|---|---|---|
| **T — Trial** | The initial attempt | Phase 3: Game Breaks | Student attempts practice problems for the first time. The "Try-All" approach — every attempt generates data for the system. |
| **E — Event** | The outcome of the trial | Phase 3: Per-question result | Each question answered produces a binary outcome (correct/incorrect) plus metadata (time, hesitation, hint usage). |
| **F — Feedback** | Sensory info from the event | Phase 3: Immediate feedback | The system provides instant per-item feedback — correct answer shown, explanation on wrong, streak/combo displayed. |
| **C — Check** | Compare Feedback vs. Goal | IRT Engine (Section 9) | The IRT engine recalculates student Theta (proficiency) after each response. Compares current performance against target PISA level. The brain's "Comparator" = the adaptive difficulty engine. |
| **A — Adjust** | Modify approach for next trial | IRT Difficulty Adjustment + Phase 5 | The engine adjusts difficulty tier (below 60% → reduce, above 90% → increase). Phase 5 Consolidation targets specifically the weak concepts identified during Check. |
| **S — Success** | Achieving the target | Phase 6: Boss Defeat | The Final Boss is defeated. The student has demonstrated competence at their target PISA level. Dopamine reward = XP, stars, badges. |

### Key Maxim (system-wide)

> **"There is no such thing as failure, only feedback."**

This maxim governs ALL failure states in NETS. When a student gets a question wrong, misses a Memory Sprint item, or fails the Final Boss — the system treats the outcome as **Feedback (F)**, not as failure. The AI tutor language (see AI Tutor Language spec) enforces this framing via "Hali emas!" (Not yet!) responses.

### TEFCAS in Failure Flow (Phase 6)

When a student fails the Final Boss:

```
1. TRIAL (T):     Student attempted the Boss questions
2. EVENT (E):     Boss HP > 0 after all questions (defeat)
3. FEEDBACK (F):  System identifies WHICH learning objectives failed
4. CHECK (C):     IRT compares failed objectives against student's current Theta
5. ADJUST (A):    Socratic tutoring guides student to specific weak branches
                  + Boss questions regenerated (same standards, new context)
6. SUCCESS (S):   Student re-attempts and defeats the Boss
```

The Socratic tutoring prompts in Phase 6 explicitly walk the student through C → A → S:
- **Check:** "Let's look at where the gap is..."
- **Adjust:** "How would you approach this differently?"
- **Success:** "Now try again with your adjusted strategy."

### TEFCAS in Reflection (Phase 7)

Phase 7 reflection prompts use TEFCAS vocabulary:

| Performance Band | TEFCAS-Framed Prompt |
|---|---|
| ≥ 80% accuracy | "What was your best **Trial** today? What strategy led to **Success**?" |
| 60-79% accuracy | "Your brain received some **Feedback** today. Which **Adjustment** helped you most?" |
| < 60% accuracy | "Every **Trial** grows your brain. What **Feedback** will you use to **Adjust** for next time?" |

---

## Section B: BOST — The Study Technique the Engine Models

The Buzan Organic Study Technique (BOST) is a structured path for tackling any subject. The NETS 7-Phase flow already maps to BOST at approximately 80%. Two small additions close the remaining gap.

### BOST-to-NETS Alignment Table

| BOST Step | Purpose | NETS Phase | Status | Gap / Addition |
|---|---|---|---|---|
| **Browse** | Flip through material to get a "feel" | Phase 0-A: Theme Preview (Panels 1-4) | ALIGNED | Panel 1 (Summary) shows chapter overview. No change needed. |
| **Time & Amount** | Set boundaries to reduce anxiety | Session timer display | ALIGNED | Timer already shows estimated remaining time. No change needed. |
| **Prime** | Surface what you already know | Phase 0-A Panel 5 + Phase 1 Memory Sprint | PARTIAL | **ADD:** "What do you already know about [Topic]?" prompt to Panel 5 (Personal Hook). Student taps 2-3 keywords from a pre-set list or types freely. This primes existing schemas before new content. Tier 1. |
| **Questions/Goals** | Define what you want to extract | Phase 0-A Panel 6 (Why This Matters) | PARTIAL | **ADD:** "What's one thing you want to figure out about [Topic] today?" prompt to Panel 6. Student's answer is stored and resurfaced in Phase 7 Reflection to check if the goal was met. Tier 1. |
| **Overview** | Big picture / headings | Phase 0-B: Flash Cards | ALIGNED | Flash Cards surface all key formulas, concepts, and rules. No change needed. |
| **Preview** | Diagrams / summaries / bold text | Phase 2: Story Mode (Segment 1) | ALIGNED | The Problem beat of the story arc sets context. No change needed. |
| **Inview** | Detailed reading with momentum | Phase 2-3: Story Mode + Game Breaks | ALIGNED | Core content delivery and active practice. Story Mode maintains momentum per existing spec. |
| **Review** | Final synthesis | Phase 5 + Phase 7: Consolidation + Reflection | ALIGNED | Mnemonic Lock synthesizes concepts; Reflection Journal enables metacognition. No change needed. |

### Required Additions (2 prompts)

**Addition 1 — Prior Knowledge Prompt (Panel 5)**

```json
{
  "panel": 5,
  "component": "personal_hook",
  "addition": "prior_knowledge_prompt",
  "prompt_uz": "Bu mavzu haqida nimalarni bilasiz? 2-3 ta kalit so'z tanlang yoki yozing.",
  "prompt_en": "What do you already know about this topic? Pick 2-3 keywords or type freely.",
  "interaction": "keyword_chips_or_freetext",
  "scoring": "none",
  "ai_tier": 1,
  "data_use": "stored → fed to Session Assembler to prioritize schema-linked content in Phase 2"
}
```

**Addition 2 — Learning Goal Prompt (Panel 6)**

```json
{
  "panel": 6,
  "component": "why_this_matters",
  "addition": "learning_goal_prompt",
  "prompt_uz": "Bugun [Mavzu] haqida nimani bilmoqchisiz?",
  "prompt_en": "What's one thing you want to figure out about [Topic] today?",
  "interaction": "single_line_text_input",
  "scoring": "none",
  "ai_tier": 1,
  "data_use": "stored → resurfaced in Phase 7 Reflection: 'Remember, you wanted to learn [X]. Did you figure it out?'"
}
```

### BOST Alignment Score

| Before injection | After injection |
|---|---|
| 6/8 BOST steps aligned (75%) | **8/8 BOST steps aligned (100%)** |

---

## Implementation Notes

- These sections are inserted into the UNIFIED spec preamble (after Section 1.3 "No Busywork Rule", before Section 2).
- No existing content is modified. Two new subsections are added: "1.4 TEFCAS — The Cognitive Engine" and "1.5 BOST — The Study Technique Model."
- The two Panel additions (Prior Knowledge + Learning Goal) are amendments to Section 4.4 (Theme Preview).
- AI Tier impact: Tier 1 only. Both prompts are template-based with variable slots.
- Cost impact: Zero marginal cost.


---


# Buzan Injection — Deliverable 13: Content Pipeline Quality Gates

**Status:** Amendment to NETS-Homework-Engine-UNIFIED.md Section 10 (Textbook-to-NETS Content Pipeline)  
**Methods Injected:** #12 (Dual Coding), #13 (Schema Theory), #22 (80/20 Rule), #32 (SMASHIN' SCOPE)  
**Layer:** B (Cross-Cutting) + E (Content Pipeline)  
**Sacred Rule:** These gates check HOW content is delivered, never change WHAT content says.

---

## QG-1: 80/20 Keyword Extraction Rule (Method #22)

**Pipeline Stage:** Phase 2 — Task Generator  
**Applies to:** Every `narrative_segment` (Story Mode content)

### Rule

For every `narrative_segment`, the content author must extract and tag the **`keywords_80_20`** array — the approximately 20% of words that carry 80% of the conceptual value.

### Schema Addition

```json
{
  "narrative_segment": {
    "existing_fields": "...",
    "keywords_80_20": {
      "type": "array",
      "min_items": 3,
      "max_items": 8,
      "description": "The 20% of words carrying 80% of conceptual value in this segment",
      "items": {
        "keyword_uz": "string (required)",
        "keyword_ru": "string (optional)",
        "importance": "primary | secondary",
        "textbook_page": "integer (source page reference)"
      }
    }
  }
}
```

### Usage Downstream

| Consumer | How It Uses `keywords_80_20` |
|---|---|
| **Focus Guide** (Phase 2) | Pacer emphasizes (bold/highlight) keywords as it passes over them |
| **Radiant Summary** (Phase 5) | Keywords become the branch labels on the radiant map |
| **Flash Cards** (Phase 0-B) | Primary keywords become card fronts |
| **Memory Sprint** (Phase 1) | Keywords from previous chapters feed the recall item pool |
| **Supernova Sprint** (Phase 5) | Central keyword for the association burst |

### Validation Rule

```
IF narrative_segment.keywords_80_20 IS EMPTY OR NULL:
  → Block: content stays in DRAFT status
  → Flag: "Missing 80/20 keyword extraction"
```

---

## QG-2: Dual Coding Check (Method #12)

**Pipeline Stage:** Phase 3 — Quality Assurance  
**Applies to:** Every `game_item`, `mnemonic_exercise`, and `boss_question`

### Rule

Every content block must engage **at least 2 encoding channels**. This is the system-wide enforcement of Paivio's Dual Coding Theory — combining two representation systems doubles the chance of recall.

### Encoding Channel Tags

Each content block must declare which channels it uses:

| Channel | Code | What It Means | Examples |
|---|---|---|---|
| Verbal/Textual | `VRB` | Words, sentences, labels | Sentence Fill, text-based quiz |
| Visual/Pictorial | `VIS` | Images, diagrams, icons, colors | Tile Match images, diagram labels |
| Spatial/Locational | `SPA` | Position, layout, movement through space | Memory Palace, map exercises |
| Auditory | `AUD` | Sound, rhythm, music, spoken word | TTS narration, rhyme-based mnemonics |
| Kinesthetic/Motor | `KIN` | Drag, draw, tap, physical action | Notebook Capture, drag-and-drop, Order Steps |

### Schema Addition

```json
{
  "game_item": {
    "existing_fields": "...",
    "encoding_channels": {
      "type": "array",
      "min_items": 2,
      "items": {
        "type": "string",
        "enum": ["VRB", "VIS", "SPA", "AUD", "KIN"]
      },
      "description": "Must contain at least 2 distinct channels"
    }
  }
}
```

### Validation Rule

```
IF content_block.encoding_channels.length < 2:
  → Block: content stays in DRAFT status
  → Flag: "Dual Coding violation — only 1 encoding channel declared"
  → Suggested fix: "Add a visual/spatial/auditory element to complement the verbal content"
```

### Common Dual Coding Pairs by Game Mechanic

| Game Mechanic | Typical Pair | Notes |
|---|---|---|
| Tile Match | VRB + VIS | Text ↔ Image matching |
| Memory Palace | SPA + VIS + VRB | Spatial location + visual image + verbal label |
| Sentence Fill | VRB + VIS | Text with visual context/diagram |
| Why Chain | VRB + VIS | Verbal reasoning with branching visual |
| Notebook Capture | KIN + VIS | Physical drawing + visual output |
| Tic Tac Toe vs AI | VRB + SPA | Verbal answer + spatial board position |
| Radiant Summary | VIS + VRB + SPA | Visual map + keyword labels + spatial layout |
| Peg System | VIS + VRB | Number-Shape image + concept keyword |

---

## QG-3: SMASHIN' SCOPE Quality Gate (Method #32)

**Pipeline Stage:** Phase 3 — Quality Assurance  
**Applies to:** Every `mnemonic_exercise` content block (Memory Palace scenes, Peg associations, Link Chain stories, Radiant Summaries, Supernova prompts)

### Rule

Every mnemonic exercise must score **6 or higher out of 12** on the SMASHIN' SCOPE checklist. This ensures mnemonic content is vivid, multi-sensory, and memorable — not dry or abstract.

### The 12 SMASHIN' SCOPE Criteria

| # | Letter | Criterion | What to Check | Score |
|---|---|---|---|---|
| 1 | **S** | Synaesthesia | Does the content engage multiple senses? (see it + hear it + feel it) | 0 or 1 |
| 2 | **M** | Movement | Is there action, motion, or dynamic change in the mnemonic imagery? | 0 or 1 |
| 3 | **A** | Association | Does the mnemonic link the new concept to something the student already knows? | 0 or 1 |
| 4 | **S** | Substitution* | Is an abstract concept replaced with a concrete, tangible image? (*Age-appropriate replacement for Buzan's original "Sexuality" criterion*) | 0 or 1 |
| 5 | **H** | Humor | Is there something funny, absurd, or smile-inducing? | 0 or 1 |
| 6 | **I** | Imagination | Does it go beyond literal representation into creative/fantastical territory? | 0 or 1 |
| 7 | **N** | Number | Are specific quantities, counts, or numbered sequences included? | 0 or 1 |
| 8 | **S** | Symbolism | Does it use recognizable symbols, icons, or cultural references? | 0 or 1 |
| 9 | **C** | Color | Are distinct, vivid colors specified (not grayscale or monochrome)? | 0 or 1 |
| 10 | **O** | Order | Is there a clear sequence or spatial arrangement? | 0 or 1 |
| 11 | **P** | Positive | Is the tone encouraging, upbeat, or inspiring? (No fear-based mnemonics) | 0 or 1 |
| 12 | **E** | Exaggeration | Is something deliberately oversized, extreme, or surprising? | 0 or 1 |

*Note: Buzan's original "S" was "Sexuality" — repurposed as "Substitution" (concrete for abstract) for age-appropriateness in a K-11 education system.*

### Scoring

```
SMASHIN_SCOPE_SCORE = sum of all 12 criteria (0 or 1 each)

IF SMASHIN_SCOPE_SCORE >= 6:
  → PASS: content approved for mnemonic exercise pool
IF SMASHIN_SCOPE_SCORE < 6:
  → RETURN: content sent back with specific criteria flagged for enrichment
  → Message: "Mnemonic content scores [X]/12 on SMASHIN' SCOPE. 
    Minimum 6 required. Missing: [list unmet criteria]. 
    Enrich with [specific suggestions]."
```

### Schema Addition

```json
{
  "mnemonic_exercise": {
    "existing_fields": "...",
    "smashin_scope": {
      "score": "integer (0-12)",
      "breakdown": {
        "synaesthesia": "boolean",
        "movement": "boolean",
        "association": "boolean",
        "substitution": "boolean",
        "humor": "boolean",
        "imagination": "boolean",
        "number": "boolean",
        "symbolism": "boolean",
        "color": "boolean",
        "order": "boolean",
        "positive": "boolean",
        "exaggeration": "boolean"
      },
      "reviewer_notes": "string (optional — justification for borderline scores)"
    }
  }
}
```

### Example — Memory Palace Scored

**Topic:** Water Cycle (Science G5)  
**Mnemonic:** "At the Hovli gate, clothes are drying — the Sun is pulling water into the sky as invisible steam. A giant cloud forms over the poplar tree like a white cotton candy mountain..."

| Criterion | Present? | Evidence |
|---|---|---|
| Synaesthesia | YES | Visual (clothes drying) + thermal (Sun heat) |
| Movement | YES | Water "pulled into the sky," cloud "forms" |
| Association | YES | Clothes drying = everyday experience |
| Substitution | YES | Invisible evaporation → visible steam/clothes |
| Humor | NO | — |
| Imagination | YES | "Cotton candy mountain" cloud |
| Number | NO | — |
| Symbolism | YES | Hovli gate = home/start of journey |
| Color | YES | White cloud, yellow sun |
| Order | YES | Gate → Tree → Pool (spatial sequence) |
| Positive | YES | Encouraging, wonder-inducing tone |
| Exaggeration | YES | "Giant" cloud, "mountain" |

**Score: 10/12** — PASS

---

## QG-4: Schema Activation Check (Method #13)

**Pipeline Stage:** Phase 4 — Session Assembly  
**Applies to:** Session plan generation (the Session Assembler algorithm)

### Rule

Every new concept introduced in Phase 2 (Story Mode) must have **at least one prerequisite concept** that was activated in Phase 1 (Memory Sprint) or Phase 0-B (Flash Cards) of the **same session**.

This enforces Schema Theory: new information anchors better when it connects to existing knowledge structures that are already active in working memory.

### Algorithm Addition

```
DURING session_plan.build():

  FOR EACH new_concept IN phase_2_narrative_segments:
    prerequisite_list = new_concept.prerequisites[]
    
    activated_in_session = [
      items in phase_1_memory_sprint WHERE standard_ref IN prerequisite_list,
      items in phase_0b_flash_cards WHERE standard_ref IN prerequisite_list
    ]
    
    IF activated_in_session.length == 0:
      → WARNING: "Schema gap: [new_concept] has no prerequisite activated in P1 or P0-B"
      → AUTO-FIX: Insert one prerequisite recall_item into Phase 1 Memory Sprint
      → IF Memory Sprint is at capacity (8 items): replace the lowest-priority item
      → LOG: "Schema Activation auto-fix applied for [standard_ref]"
```

### Validation Rule

```
IF session_plan has any concept with zero prerequisite activation:
  → Soft block (auto-fixable): Session Assembler auto-inserts prerequisite
  → Hard block (if no prerequisite exists in content pool): 
    Flag for content author: "No prerequisite content exists for [standard_ref]. 
    Create a recall_item for [prerequisite_standard_ref]."
```

---

## Summary of Pipeline Changes

| Gate | Pipeline Stage | Content Type | Minimum | Action on Fail |
|---|---|---|---|---|
| **QG-1: 80/20 Keywords** | Task Generator | `narrative_segment` | 3-8 keywords tagged | Block → DRAFT |
| **QG-2: Dual Coding** | QA | `game_item`, `mnemonic_exercise`, `boss_question` | 2+ encoding channels | Block → DRAFT |
| **QG-3: SMASHIN' SCOPE** | QA | `mnemonic_exercise` | 6/12 score | Return for enrichment |
| **QG-4: Schema Activation** | Session Assembly | Session plan | 1+ prerequisite per new concept | Auto-fix or flag |

All gates are **additive** — they supplement existing pipeline checks, they do not replace any.


---


# Buzan Injection — Deliverables 15-18: UI/UX Spec Amendments

**Status:** Amendment to NETS-UI-UX-Design-Spec  
**Methods Injected:** #2 (7 Laws), #6 (Simplified Laws), #9 (Color-Coded Zones), #17 (Saccade Optimization), #19 (Peripheral Vision)  
**Layer:** C (UI/UX)  
**Sacred Rule:** These change how content is displayed, never what content says.

---

## UI-1: Radiant UI Standard — The 7 Laws (Deliverable 15, Method #2)

Any UI element in NETS that displays information radiantly — Phase 5 Radiant Summary, Bilim Bazasi knowledge map, Phase 0-A topic structure, any mind-map output — MUST comply with Buzan's 7 Laws.

### The 7-Point Radiant Compliance Checklist

Every radiant UI component must pass ALL 7 before deployment:

| # | Law | Requirement | Fail Example | Pass Example |
|---|---|---|---|---|
| 1 | **Central Image** | The center of the radiant display contains a colorful image or icon representing the topic. Never start with text alone. | Plain text "Photosynthesis" in the center | Sun icon with green leaves in the center |
| 2 | **Organic Branches** | Branches use curved, organic lines. No straight connector lines. CSS `border-radius` or SVG curves mandatory. | Straight lines from center to nodes | Curved, flowing lines that taper from thick (center) to thin (tip) |
| 3 | **Hierarchy (BOIs)** | Main branches (Basic Ordering Ideas) are visually thicker/bolder than sub-branches. Clear parent-child distinction. | All branches same thickness | Main branches 4px, sub-branches 2px, leaf branches 1px |
| 4 | **One Keyword Per Branch** | Each branch displays exactly one keyword or short label. No sentences on branches. | "The process of water evaporating from surfaces" on a branch | "Bug'lanish" (Evaporation) |
| 5 | **Emphasis** | Visual hierarchy through size variation — main branch labels larger, sub-branch labels smaller. Bold for primary, regular for secondary. | All labels same font size | Main: 16px bold, Sub: 14px regular, Leaf: 12px light |
| 6 | **Association** | Connections between related branches shown via arrows, dashed lines, or shared color. Cross-links visible. | Isolated branches with no visual connections | Dashed arrow from "Condensation" branch to "Precipitation" branch |
| 7 | **3+ Colors** | Minimum 3 distinct colors per radiant display. Each main branch has its own color zone. | Monochrome blue map | Blue (Water), Green (Plants), Yellow (Sun), Brown (Soil) |

### Implementation for Developers

```css
/* Radiant UI Base Rules */
.radiant-branch {
  border-radius: 50%;          /* Law 2: organic curves */
  stroke-linecap: round;       /* Law 2: no sharp edges */
}
.radiant-branch--main {
  stroke-width: 4px;           /* Law 3: thick main branches */
  font-size: 16px;
  font-weight: 700;
}
.radiant-branch--sub {
  stroke-width: 2px;           /* Law 3: thinner sub-branches */
  font-size: 14px;
  font-weight: 400;
}
.radiant-branch--leaf {
  stroke-width: 1px;
  font-size: 12px;
  font-weight: 300;
}
.radiant-center {
  min-width: 80px;
  min-height: 80px;            /* Law 1: prominent central image */
}
/* Law 7: enforced via per-branch color class assignment */
```

---

## UI-2: G5-6 Simplified Radiant Rules (Deliverable 16, Method #6)

For Grade 5-6 students (ages 10-12), all radiant UI components apply additional constraints that respect the Working Memory ceiling (~4-5 chunks) and developmental stage.

### Simplified Rules (G5-6 Override)

| Rule | Standard (G7+) | Simplified (G5-6) | Rationale |
|---|---|---|---|
| **Orientation** | Any | **Landscape only** | Provides "freedom of movement," prevents vertical margin restriction |
| **Max main branches** | 6-8 | **4-5 maximum** | Respects WM ceiling of 4-5 chunks |
| **Branch style** | Organic, varied thickness | **Extra thick, exaggerated curves** | More visually stimulating for younger brains |
| **Label format** | Keyword text | **Icon-First: image/icon BEFORE text label** | Children are naturally visual; lowers literacy barrier |
| **Interaction** | Drag-and-drop keywords | **Tap-to-select from 3 options** (drag optional) | Reduces fine-motor demand |
| **Color** | 3+ colors | **Exactly 4-5 colors** (one per main branch, high saturation) | Clear, simple color zones without overwhelm |

### Icon-First Rule Detail

On every radiant branch for G5-6:
1. The **icon/image appears first** (left side or above)
2. The **keyword text appears second** (right side or below)
3. If screen width is constrained, the icon is shown and text is available on tap

```
[icon: sun] Bug'lanish     ← G5-6: icon leads
Bug'lanish [icon: sun]     ← G7+: text can lead
```

---

## UI-3: Subject Color System (Deliverable 17, Method #9)

Each of the 5 NETS subject families receives a distinct primary color. This color extends to all in-session elements: radiant maps, loading screens, phase headers, Bilim Bazasi zones, progress bars.

### Subject Family Color Assignments

| Subject Family | Subjects | Primary Color | Hex | Accent | Usage |
|---|---|---|---|---|---|
| **Aniq Fanlar** (Exact Sciences) | Mathematics, Informatika | Deep Blue | `#1565C0` | `#42A5F5` | Phase headers, radiant branch default, progress bar |
| **Tabiat Fanlari** (Natural Sciences) | Science, Biology, Chemistry, Physics, Geography | Forest Green | `#2E7D32` | `#66BB6A` | Phase headers, radiant branch default |
| **Til Fanlari** (Languages) | Uzbek Tili, English, Russian | Warm Amber | `#E65100` | `#FFA726` | Phase headers, radiant branch default |
| **Ijtimoiy Fanlar** (Social Sciences) | History, Huquq (Law) | Royal Purple | `#6A1B9A` | `#AB47BC` | Phase headers, radiant branch default |
| **Tarbiya / San'at** (Values & Arts) | Tarbiya, Tasviriy San'at, Musiqa, Texnologiya, Jismoniy Tarbiya | Warm Red | `#C62828` | `#EF5350` | Phase headers, radiant branch default |

### Application Rules

1. **Phase header bar** uses the subject's primary color as background
2. **Radiant maps** use the subject color for the central node; BOI branches use distinct hues derived from the accent color
3. **Bilim Bazasi** knowledge map zones are color-coded by subject family
4. **Loading screen** background gradient uses the subject's primary → accent
5. **Progress bar** fill color matches the subject family
6. **Within a radiant map**, each main branch uses a DIFFERENT color (even within the same subject). The subject family color is the central node only.

### Accessibility

- All color pairs must meet **WCAG 2.1 AA** contrast ratio (4.5:1 for normal text, 3:1 for large text)
- For color-blind students: each branch also has a **distinct line pattern** (solid, dashed, dotted, dash-dot) as a secondary differentiator
- Dark mode: colors shift to lighter variants with same hue relationships

---

## UI-4: Reading Optimization (Deliverable 18, Methods #17, #19)

These typography and layout rules optimize the mechanics of reading — reducing saccade distance, leveraging peripheral vision, and preventing line-skipping errors during rapid eye movement.

### Text Container Rules

| Parameter | Value | Rationale |
|---|---|---|
| **Column width** | **50-75 characters per line** (66 ideal) | Optimal saccade distance. Eye can use peripheral vision for line edges, reducing fixation count. |
| **Line height** | **1.5x font size** (minimum 1.4x) | Prevents "line-skipping" errors during rapid vertical saccades. |
| **Font family** | **Arimo** (primary), Noto Sans (fallback) | High-legibility sans-serif with full Uzbek Latin + Cyrillic coverage. |
| **Font size** | **16px** base (mobile), **18px** base (tablet/desktop) | Below 14px causes fixation duration increase of 20-30%. |
| **Paragraph spacing** | **1.2em** between paragraphs | Visual breathing room between thought units. |
| **Text alignment** | **Left-aligned** (ragged right) | Justified text creates uneven word spacing that disrupts saccade rhythm. |
| **Max container width** | **640px** on desktop | Even on wide screens, text stays within optimal character count. |

### Where These Rules Apply

| Component | Apply? | Notes |
|---|---|---|
| Phase 2: Story Mode narrative text | **YES** (mandatory) | Primary reading surface |
| Phase 0-A: Theme Preview panels | **YES** (mandatory) | Pre-reading surface |
| Phase 0-B: Flash Card text | **YES** (mandatory) | Reference reading |
| Phase 4: Real-Life Challenge scenario | **YES** (mandatory) | Complex reading under time pressure |
| Phase 6: Boss question text | **YES** (mandatory) | High-stakes reading |
| Game mechanic instructions | YES (recommended) | Brief text, less critical |
| Navigation / UI chrome | NO | Different design constraints |

### Font Specification

```css
/* Primary reading surfaces */
.reading-surface {
  font-family: 'Arimo', 'Noto Sans', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  max-width: 640px;
  text-align: left;
  color: #1a1a2e;            /* High contrast on white */
  letter-spacing: 0.01em;    /* Slight letter spacing aids character recognition */
}

@media (min-width: 768px) {
  .reading-surface {
    font-size: 18px;
  }
}

/* Uzbek Cyrillic override (slightly wider characters) */
.reading-surface[lang="uz-Cyrl"] {
  letter-spacing: 0.02em;
}
```

---

## Summary of UI/UX Amendments

| Deliverable | Methods | What It Adds | Where in UI/UX Spec |
|---|---|---|---|
| 15: Radiant UI Standard | #2 | 7-point compliance checklist for all radiant displays | New section: "Radiant UI Design Standard" |
| 16: G5-6 Simplified Rules | #6 | Landscape-only, max 4-5 branches, Icon-First, thick curves | Subsection of Radiant UI Standard: "Grade 5-6 Override" |
| 17: Subject Color System | #9 | 5 subject family colors with hex values and application rules | New section: "Subject Color System" |
| 18: Reading Optimization | #17, #19 | Column width, line height, font, alignment rules | New section: "Reading Optimization Typography" |

All amendments are additive. No existing UI/UX spec content is modified.


---


# Buzan Injection — Deliverables 22-24: AI Tutor Language

**Status:** New companion document — AI Prompt Template Library  
**Methods Injected:** #7 (Supernova Effect), #10 (Hali emas / TEFCAS reframe), #11 (TEFCAS full loop)  
**Layer:** D (AI Tutor Language)  
**AI Tier:** Tier 1 — all templates are pre-authored with variable slots. Zero generative AI cost.  
**Sacred Rule:** Language changes how the system SPEAKS, not what content it teaches.

---

## Part 1: "Hali emas!" — Universal Failure Response System (Deliverable 22, Method #10)

### Core Rule

**The words "Wrong," "Incorrect," "Noto'g'ri," and "Xato" are BANNED from all AI tutor responses across all phases.**

Every failure state uses: **"Hali emas!"** (Not yet!) + a TEFCAS-framed follow-up.

### Phase-by-Phase Failure Templates

#### Phase 1: Memory Sprint

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Wrong recall answer | "Hali emas! Bu yerda boshqa javob kerak. Qayta o'ylab ko'ring." | "Not yet! A different answer is needed here. Think again." |
| 0-2 correct out of 5-8 | "Hali emas! Miyangiz hozir eslamoqda. Ertaga bu so'zlar osonroq bo'ladi." | "Not yet! Your brain is remembering right now. Tomorrow these will be easier." |
| Sprint accuracy < 60% | "Hali emas! Sizga bir oz ko'proq mashq kerak. Keling, avval eslaymiz." | "Not yet! You need a bit more practice. Let's recall first." |

#### Phase 2: Story Mode Checkpoints

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Wrong checkpoint answer (1st attempt) | "Hali emas! Hikoyaga qaytib qarang — javob o'sha yerda." | "Not yet! Look back at the story — the answer is in there." |
| Wrong checkpoint answer (2nd attempt) | "Hali emas! Mana maslahat: [simplified_hint]. Yana bir bor urinib ko'ring." | "Not yet! Here's a hint: [simplified_hint]. Try once more." |
| Wrong checkpoint answer (3rd/simplified) | "Hali emas, lekin yaqinlashyapsiz! To'g'ri javob: [answer]. Keling, nimaga ekanini tushunaylik." | "Not yet, but you're getting closer! The correct answer is: [answer]. Let's understand why." |

#### Phase 3: Game Breaks

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Wrong game answer | "Hali emas! Miyangiz hozir Feedback oldi. Keyingi urinish yaxshiroq bo'ladi." | "Not yet! Your brain just got some Feedback. The next try will be better." |
| Streak broken | "Streak to'xtadi — lekin Feedback qo'lga kiritildi! Yangi streak boshlang." | "Streak stopped — but Feedback captured! Start a new streak." |
| Low game score | "Hali emas! Bu o'yin sizning Adjust bosqichingiz — keyingisida kuchliroq bo'lasiz." | "Not yet! This game is your Adjust stage — you'll be stronger next time." |

#### Phase 4: Real-Life Challenge

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Wrong sub-question | "Hali emas! Mutaxassis sifatida qayta o'ylang — yana qaysi ma'lumot kerak?" | "Not yet! Think again as the expert — what other information do you need?" |
| Weak reasoning | "Hali emas! Javobingiz yaxshi, lekin NIMA UCHUN tushuntiring." | "Not yet! Your answer is good, but explain WHY." |

#### Phase 5: Consolidation

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Memory Palace: concept not recalled | "Hali emas — Saroyingiz qurilgan! Ertaga qaytib borsak, eslay olasiz." | "Not yet — your Palace is built! When we visit tomorrow, you'll remember." |
| Radiant Summary: wrong branch placement | "Hali emas! Bu tushuncha boshqa shoxga tegishli. Qayta joylang." | "Not yet! This concept belongs on a different branch. Re-place it." |
| Peg System: wrong association | "Hali emas! Raqam shaklini eslang — [peg_image]. Bu qaysi tushunchaga bog'langan?" | "Not yet! Remember the number shape — [peg_image]. Which concept does this connect to?" |

#### Phase 6: Final Boss

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Wrong Boss answer | "Hali emas! Miyangiz Feedback oldi. Keling, Tekshiramiz (Check) — qayerda tushunmovchilik bor?" | "Not yet! Your brain received Feedback. Let's Check — where is the gap?" |
| Boss defeat (HP > 0) | "Hali emas! Boss hali yengilmagan — lekin sizning Bilim Bazangiz kuchaydi. Keling, Moslashtiramiz (Adjust) va qayta urinamiz." | "Not yet! The Boss isn't defeated — but your Knowledge Base grew stronger. Let's Adjust and try again." |
| Boss defeat (2nd attempt fail) | "Hali emas! Keyingi darsda davom etamiz. Bugungi Feedback — kelajakdagi Successingiz uchun poydevor." | "Not yet! We'll continue next session. Today's Feedback is the foundation for your future Success." |

#### Phase 7: Reflection

| Trigger | Template (Uzbek) | Template (English equivalent) |
|---|---|---|
| Low session accuracy (< 60%) | "Bugun ko'p Feedback oldingiz — bu ajoyib! Har bir Feedback miyangizni kuchaytiryapti." | "You received a lot of Feedback today — that's great! Every Feedback is strengthening your brain." |

---

## Part 2: TEFCAS Socratic Prompts for Phase 6 & 7 (Deliverable 23, Method #11)

### Phase 6: Post-Failure Socratic Tutoring

When a student fails a Boss question, the Socratic tutoring sequence walks them through TEFCAS steps C → A → S:

**Sequence (3 prompts, delivered one at a time):**

```
PROMPT 1 — CHECK (C):
  UZ: "Keling, tekshiramiz. [Failed_concept] haqida nima bilasiz? 
       Qaysi qadamda to'xtab qoldingiz?"
  EN: "Let's check. What do you know about [failed_concept]? 
       Which step did you get stuck on?"
  
  [Student responds or selects from options]

PROMPT 2 — ADJUST (A):
  UZ: "Yaxshi. Endi moslashtiramiz. Agar [failed_concept] o'rniga 
       [simpler_analogy] deb o'ylasangiz — javob qanday o'zgaradi?"
  EN: "Good. Now let's adjust. If instead of [failed_concept] 
       you think of it as [simpler_analogy] — how does the answer change?"
  
  [Student responds]

PROMPT 3 — SUCCESS (S):
  UZ: "Ajoyib! Endi qayta urinib ko'ring. Sizning yangi strategiyangiz 
       bilan Success ga erishishingiz mumkin."
  EN: "Excellent! Now try again. With your new strategy, 
       you can achieve Success."
  
  [Regenerated Boss question presented]
```

### Phase 7: TEFCAS Reflection Prompts

These replace the existing generic reflection prompts with TEFCAS-structured metacognition:

| Performance | Prompt 1 (Trial) | Prompt 2 (Feedback) | Prompt 3 (Adjust/Success) |
|---|---|---|---|
| **≥ 80%** | "Bugungi eng yaxshi Trial (urinish) qaysi edi?" | "Qaysi Feedback sizga eng ko'p yordam berdi?" | "Keyingi darsda qanday Success (muvaffaqiyat) ga erishmoqchisiz?" |
| **60-79%** | "Bugun nechta Trial qildingiz? Qaysi biri eng qiyin bo'ldi?" | "Miyangiz qanday Feedback oldi? Nimani o'rgandingiz?" | "Keyingi safar nimani Adjust (moslashtirish) qilasiz?" |
| **< 60%** | "Har bir Trial miyangizni kuchaytiryapti. Bugun nimaga urindingiz?" | "Eng muhim Feedback nima edi? Bu sizga nima o'rgatdi?" | "Bitta kichik Adjust tanlang — keyingi safar nima qilasiz boshqacha?" |

**Goal recall (from BOST Addition 2):**

At the end of every Phase 7, regardless of performance:

```
UZ: "Eslatma: Bugun siz '[stored_learning_goal]' ni bilmoqchi edingiz. 
     Bilb oldingizmi?"
EN: "Remember: Today you wanted to learn '[stored_learning_goal]'. 
     Did you figure it out?"

[Student responds: Yes / Partially / Not yet]
```

---

## Part 3: Buzan-Inspired Tutor Voice Style Guide (Deliverable 24, Methods #7, #10, #11)

### Voice Principles

1. **Brain-science language, not generic praise.** Say "Your brain just formed a new connection" instead of "Good job!"
2. **TEFCAS vocabulary embedded naturally.** Use Trial, Feedback, Adjust, Success as everyday words.
3. **Radiant/Supernova metaphors.** Knowledge "radiates," ideas are "sparks," learning "branches out."
4. **Always positive framing.** Even when correcting, frame as growth.
5. **Uzbek-first.** All templates authored in Uzbek with English equivalents for reference.

### Template Library (30+ phrases)

#### On Correct Answer (any phase)

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 1 | "Miyangiz yangi aloqa yaratdi!" | "Your brain just made a new connection!" | Any correct answer |
| 2 | "Bilim Bazangizga yangi shox qo'shildi!" | "A new branch added to your Knowledge Base!" | After a concept is mastered |
| 3 | "Supernovangiz porlayapti — yana bir uchqun!" | "Your Supernova is glowing — another spark!" | During streaks |
| 4 | "Radiant kuch! Bilimingiz tarqalmoqda." | "Radiant power! Your knowledge is spreading." | After multi-step reasoning |
| 5 | "TEFCAS: Trial → Success! Muvaffaqiyat!" | "TEFCAS: Trial → Success! Achievement!" | After boss question correct |

#### On Streak

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 6 | "[X] ta uchqun ketma-ket! Supernovangiz portlamoqda!" | "[X] sparks in a row! Your Supernova is exploding!" | Streak of 3+ |
| 7 | "Miyangizning har ikki yarmi ishlayapti — sinergiya!" | "Both halves of your brain are working — synergy!" | After visual+verbal correct |
| 8 | "Radiant streak! Bilimingiz barcha yo'nalishda o'smoqda." | "Radiant streak! Your knowledge is growing in all directions." | Streak of 5+ |

#### On Incorrect Answer (Hali emas variants — supplements Part 1)

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 9 | "Hali emas — lekin miyangiz hozir o'rganmoqda!" | "Not yet — but your brain is learning right now!" | General wrong answer |
| 10 | "Feedback olindi! Bu sizning keyingi Success uchun yoqilg'i." | "Feedback received! This is fuel for your next Success." | After wrong answer with effort shown |
| 11 | "Miyangiz Adjust rejimida — yangi strategiya sinab ko'ring." | "Your brain is in Adjust mode — try a new strategy." | After 2nd wrong attempt |
| 12 | "Har bir xato — yangi neyron aloqasi. Davom eting!" | "Every mistake — a new neural connection. Keep going!" | Encouragement after struggle |

#### On Phase Transitions

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 13 | "Primacy effekti ishga tushdi — eng muhim narsalar hozir yodda qoladi." | "Primacy effect activated — the most important things will stick now." | Start of Phase 1 |
| 14 | "Hikoya vaqti! Miyangiz eng yaxshi hikoyalar orqali o'rganadi." | "Story time! Your brain learns best through stories." | Start of Phase 2 |
| 15 | "O'yin tanaffusi! Von Restorff effekti — g'ayrioddiy narsalar yodda qoladi." | "Game break! Von Restorff effect — unusual things stick in memory." | Start of Phase 3 |
| 16 | "Siz endi mutaxassisiz. Real hayot vazifasi boshlandi." | "You're the expert now. Real-life challenge begins." | Start of Phase 4 |
| 17 | "Mnemonic Lock! Tushunchalarni uzoq muddatli xotiraga qulflash vaqti." | "Mnemonic Lock! Time to lock concepts into long-term memory." | Start of Phase 5 |
| 18 | "Boss jangi! Barcha bilimlaringizni ko'rsating." | "Boss battle! Show everything you've learned." | Start of Phase 6 |
| 19 | "Recency effekti — oxirgi narsalar ham yodda qoladi. Keling, fikrlaymiz." | "Recency effect — the last things also stick. Let's reflect." | Start of Phase 7 |

#### On Boss Defeat (Victory)

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 20 | "TEFCAS to'liq tsikl — SUCCESS! Boss yengildi!" | "TEFCAS full cycle — SUCCESS! Boss defeated!" | Boss defeated |
| 21 | "Bilim Bazangiz kengaydi! Yangi hududlar ochildi." | "Your Knowledge Base expanded! New territories unlocked." | Boss defeated, new content unlocked |
| 22 | "Supernovangiz yangi yulduzlar yaratdi!" | "Your Supernova created new stars!" | Boss defeated with high score |

#### On Boss Defeat (Loss — extends Hali emas)

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 23 | "Boss hali yengilmagan — lekin TEFCAS davom etmoqda. Adjust vaqti." | "Boss not defeated yet — but TEFCAS continues. Time to Adjust." | Boss loss, retry available |
| 24 | "Miyangiz kuchli Feedback oldi. Bu keyingi urinishda quvvatga aylanadi." | "Your brain received strong Feedback. This becomes power in the next attempt." | Boss loss |

#### On Session Complete

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 25 | "Bugungi dars tugadi! Miyangiz [X] ta yangi aloqa yaratdi." | "Today's lesson complete! Your brain made [X] new connections." | Session end |
| 26 | "Buzan intervallari ishga tushdi — ertaga bu tushunchalar mustahkamlanadi." | "Buzan intervals activated — tomorrow these concepts will be reinforced." | Session end, spaced rep scheduled |
| 27 | "Bilim Bazangiz [X]% ga o'sdi. Radiating knowledge!" | "Your Knowledge Base grew by [X]%. Radiating knowledge!" | Session end with progress |

#### On Specific Mechanics

| # | Uzbek | English Equivalent | When to Use |
|---|---|---|---|
| 28 | "Saroyingiz qurilmoqda! Har bir joy — yangi xotira." | "Your Palace is being built! Every place — a new memory." | Memory Palace placement |
| 29 | "Raqam shakli = tushuncha. Peg tizimi ishlamoqda!" | "Number shape = concept. Peg System working!" | Peg System association |
| 30 | "Zanjir tuzilmoqda! Har bir bo'g'in — keyingisini eslatadi." | "Chain forming! Each link reminds you of the next." | Link Chain mechanic |
| 31 | "Radiant xarita kengaymoqda — yana bir shox!" | "Radiant map expanding — another branch!" | Radiant Summary |
| 32 | "80/20 qoidasi — eng muhim so'zlarni topdingiz!" | "80/20 rule — you found the most important words!" | Keyword identification in any phase |

---

## Implementation Notes

- All 32 templates are **Tier 1** (pre-authored, variable slot insertion). Zero LLM cost.
- Templates are stored as a JSON lookup table keyed by `trigger_event` + `performance_band` + `phase`.
- The `[X]`, `[failed_concept]`, `[stored_learning_goal]`, etc. are variable slots filled by the session engine.
- Templates rotate — the system should NOT repeat the same template in consecutive sessions. Use a simple round-robin or weighted random per student.
- All templates available in both Uzbek and Russian. The student's language preference determines which is displayed.
- Templates are **additive** — they supplement, not replace, the existing Phase 7 prompt generation logic in Section 5.7 of the UNIFIED spec.


---


# NETS Game Mechanic — Full Definition: Radiant Summary

**Version:** 1.0  
**Date:** April 2026  
**Buzan Methods Injected:** #1 (Radiant Thinking), #2 (7 Laws of Mind Mapping), #7 (Supernova Effect)  
**Status:** READY FOR REVIEW  
**Constitution:** `NETS-Homework-Engine-UNIFIED.md` v2.0  
**Sacred Rule:** Content unchanged. The radiant map organizes EXISTING textbook concepts — never invents new ones.

---

## 1. What It Is

A visual consolidation mechanic where the student completes a partially-built radiant map of the lesson's key concepts. The map follows Buzan's 7 Laws of Mind Mapping: central image, organic curved branches, one keyword per branch, hierarchy via BOIs, 3+ colors. The student drags keywords or icons onto the correct branches, completing the map and locking the lesson's conceptual structure into long-term memory.

Optionally includes a **Supernova Sprint** micro-round: a 30-second timed association burst from one keyword.

This mechanic fills the undefined "Mind maps" slot listed in UNIFIED spec Phase 5 (G5-7 Consolidation techniques).

---

## 2. How It Is Played

### Step-by-step flow

**Phase A — Map Presentation (10 seconds)**
1. A partially completed radiant map appears on screen (landscape orientation)
2. Central image is pre-placed (e.g., a Sun icon for "Photosynthesis")
3. Main branches (BOIs) are drawn with labels — these are given, not guessed
4. Sub-branches have **empty slots** (dashed outlines) where keywords belong
5. A pool of **draggable keyword chips** sits at the bottom of the screen
6. Student has 10 seconds to study the existing structure before interaction begins

**Phase B — Keyword Placement (60-90 seconds)**
7. Student drags a keyword chip from the pool onto an empty branch slot
8. **Correct placement:** chip locks with a green pulse animation; branch thickens
9. **Wrong placement:** chip bounces back to pool with a soft shake; branch flashes amber
10. Repeat until all empty slots are filled or timer expires
11. Distractors: the keyword pool contains 2-3 extra chips that do NOT belong on the map (tests discrimination)

**Phase C — Supernova Sprint (30 seconds, optional)**
12. After map completion, one keyword from the map is highlighted as the "Supernova seed"
13. A 30-second timer starts
14. Student types or selects associated words as fast as possible
15. Each valid association appears as a radiating spark from the central keyword
16. Invalid associations are silently ignored (no penalty, no disruption to flow)

**Phase D — Review & Score**
17. Completed map displayed in full with all branches filled
18. Incorrectly placed items (if any) shown with corrections
19. XP awarded
20. Map saved to student's Bilim Bazasi for future review

### Core Loop Summary
```
Study map (10s) → Drag keywords to branches (60-90s) → Supernova Sprint (30s, optional) → Review & Score
```

---

## 3. Input Format (Content Author Schema)

```json
{
  "radiant_summary_instance": {
    "id": "rs_sci_g5_ch4_photosynthesis_v1",
    "topic_code": "SCI-G5-CH4-PHOTO",
    "textbook_ref": {
      "book": "Tabiiy fanlar 5-sinf (Grey, 2024)",
      "chapter": 4,
      "pages": "38-41",
      "topic": "Fotosintez"
    },
    "standards": {
      "uz_code": "UZ-SCI-5-LIFE-03",
      "alias": "SCI.5.4.1.3",
      "pisa_level": 2,
      "pisa_domain": "Science",
      "pisa_process": "Explain phenomena scientifically",
      "transition_skill": "L1→L2: organize related concepts into hierarchical categories"
    },
    "central_image": {
      "id": "img_photosynthesis_sun",
      "desc": "Bright sun with green leaf overlay",
      "label_uz": "Fotosintez"
    },
    "main_branches": [
      {
        "boi_label_uz": "Kerakli moddalar",
        "boi_label_ru": "Необходимые вещества",
        "color": "#2E7D32",
        "sub_branches": [
          {
            "slot_type": "empty",
            "correct_keyword_uz": "Yorug'lik",
            "correct_keyword_ru": "Свет"
          },
          {
            "slot_type": "empty",
            "correct_keyword_uz": "Suv",
            "correct_keyword_ru": "Вода"
          },
          {
            "slot_type": "empty",
            "correct_keyword_uz": "CO₂",
            "correct_keyword_ru": "CO₂"
          }
        ]
      },
      {
        "boi_label_uz": "Hosil bo'ladi",
        "boi_label_ru": "Образуется",
        "color": "#E65100",
        "sub_branches": [
          {
            "slot_type": "empty",
            "correct_keyword_uz": "Shakar",
            "correct_keyword_ru": "Сахар"
          },
          {
            "slot_type": "empty",
            "correct_keyword_uz": "Kislorod",
            "correct_keyword_ru": "Кислород"
          }
        ]
      },
      {
        "boi_label_uz": "Qayerda",
        "boi_label_ru": "Где",
        "color": "#1565C0",
        "sub_branches": [
          {
            "slot_type": "empty",
            "correct_keyword_uz": "Xloroplast",
            "correct_keyword_ru": "Хлоропласт"
          },
          {
            "slot_type": "prefilled",
            "keyword_uz": "Barg",
            "keyword_ru": "Лист"
          }
        ]
      }
    ],
    "distractor_keywords": [
      { "keyword_uz": "Oqsil", "keyword_ru": "Белок" },
      { "keyword_uz": "Ildiz", "keyword_ru": "Корень" }
    ],
    "supernova_seed": {
      "keyword_uz": "Fotosintez",
      "valid_associations_uz": ["Quyosh", "Barg", "Kislorod", "Xlorofill", "Yashil", "Energiya", "O'simlik", "Shakar", "CO2", "Suv"],
      "min_valid_for_bonus": 5
    },
    "smashin_scope": {
      "score": 8,
      "breakdown": {
        "synaesthesia": true,
        "movement": true,
        "association": true,
        "substitution": true,
        "humor": false,
        "imagination": true,
        "number": true,
        "symbolism": true,
        "color": true,
        "order": false,
        "positive": true,
        "exaggeration": false
      }
    }
  }
}
```

**Required fields per instance:** `central_image`, `main_branches` (2-5), `sub_branches` per BOI (1-4 each), `distractor_keywords` (2-3).  
**Optional:** `supernova_seed` (if omitted, Supernova Sprint is skipped).  
**Pipeline gate:** `smashin_scope.score` must be ≥ 6/12 (see Pipeline QA Gates).

---

## 4. Output / Evaluation

### Keyword Placement (Phase B)

| Result | Criteria | Scoring |
|---|---|---|
| Correct first try | Keyword placed on correct branch on first attempt | 80 XP per keyword |
| Correct second try | Keyword placed correctly after one wrong attempt | 40 XP per keyword |
| Not placed / wrong | Keyword not placed or placed incorrectly at timeout | 0 XP (shown with correction) |
| Distractor avoided | Student did NOT drag a distractor onto the map | +20 XP per distractor correctly ignored |
| Distractor placed | Student dragged a distractor onto a branch | -10 XP (bounces back with correction) |

### Supernova Sprint (Phase C)

| Result | Criteria | Scoring |
|---|---|---|
| Valid association | Word matches pre-approved list or Tier 1 fuzzy match | 30 XP per word |
| 5+ valid in 30 seconds | Meets minimum for bonus | +100 XP bonus |
| 8+ valid in 30 seconds | Exceptional | +200 XP bonus |
| Invalid association | Word not in approved list and no fuzzy match | 0 XP (silently ignored) |

### Maximum Scores by Grade

| Grade | Branches (empty slots) | Max Placement XP | Supernova | Total Max |
|---|---|---|---|---|
| G5 | 4 BOIs, 5-6 empty slots | 480 + 60 (distractors) = 540 | 100 bonus + ~150 words = 250 | **790 XP** |
| G6-7 | 5 BOIs, 7-8 empty slots | 640 + 60 = 700 | 200 bonus + ~240 words = 440 | **1140 XP** |

---

## 5. PISA Mapping

| PISA Level | How Radiant Summary operates |
|---|---|
| L1 | Recall keywords and place them on pre-labeled branches (simple categorization) |
| L2 | Discriminate between correct keywords and distractors; understand hierarchical relationships |
| L3 | Recognize cross-branch associations (e.g., CO₂ connects to both "Input" and "Where" branches) |
| L4 | Not this mechanic's primary domain — Final Boss handles L4+ |

**Primary PISA level:** L1-L2 (standard), L3 (when cross-branch association arrows are tested).  
**Transition skills scaffolded:**
- `L1→L2`: "Organize related concepts into hierarchical categories"
- `L2→L3`: "Identify relationships between categories in a structured representation"

---

## 6. Bloom's Band

| Bloom Level | Radiant Summary role |
|---|---|
| **Remember** | Recall keywords from the lesson |
| **Understand** | Place keywords in correct hierarchical positions (demonstrates understanding of relationships) |
| **Analyze** | Supernova Sprint — generating associations requires analytical decomposition |
| Create | Not this mechanic's domain |

**Primary band: Remember → Understand**  
**Secondary (Supernova only): Analyze**

---

## 7. Subject Eligibility

| Subject | Eligible | Best For |
|---|---|---|
| Science G5 | YES | Classification, process decomposition (photosynthesis, water cycle) |
| Math G5 | YES | Formula components, geometry properties, number families |
| History G5 | YES | Event categorization (Silk Road: trade, culture, geography, technology) |
| Geografiya G5 | YES | Biome classification, map symbol categories |
| Texnologiya G5 | YES | Tool categories, safety rule groups, process steps |
| Tarbiya G5 | YES | Virtue categorization, moral reasoning branches |
| Tasviriy Sanat G5 | YES | Color theory, art elements, composition principles |
| Language Sciences | YES | Vocabulary clustering, grammar rule families |

**No subject bans.** Content-agnostic — any subject with 2+ hierarchical categories benefits.

---

## 8. Grade Eligibility

| Grade band | Status | BOI count | Empty slots | Distractors | Supernova |
|---|---|---|---|---|---|
| G3-4 | Introductory | 2-3 | 3-4 | 1 | No |
| G5-6 | Standard | 3-4 | 5-6 | 2 | Optional (seed word only) |
| G7-9 | Full | 4-5 | 7-8 | 2-3 | Yes (full 30s sprint) |
| G10-11 | Advanced | 5-6 | 8-10 | 3 | Yes + student adds own branches |

**G5-6 Simplified Rules (from UI-2):**
- Landscape orientation mandatory
- Max 4 main branches (WM ceiling)
- Icon-First: central image and branch icons appear BEFORE text labels
- Extra thick, exaggerated curved branches
- Tap-to-select from 3 options (drag optional)

---

## 9. Parameters / Difficulty Knobs

| Parameter | Range | Default (G5) | Effect |
|---|---|---|---|
| `boi_count` | 2-6 | 4 | More BOIs = wider map, more categorization |
| `empty_slots_total` | 3-10 | 5 | More empty slots = more placement decisions |
| `distractor_count` | 1-4 | 2 | More distractors = harder discrimination |
| `study_time` | 5-15s | 10s | Shorter study = harder (less time to pre-plan) |
| `placement_time` | 30-120s | 60s | Shorter = more pressure |
| `supernova_enabled` | true/false | false (G5) | Adds Analyze-level challenge |
| `supernova_time` | 15-45s | 30s | Shorter = more pressure |
| `prefilled_ratio` | 0.0-0.7 | 0.3 | Higher = more pre-filled branches (easier) |

**Anti-difficulty-spike rule:** `empty_slots_total` may increase by at most 2 between sessions for the same student.

---

## 10. Failure / Retry Behavior

### During placement (Phase B)
- **Wrong placement:** Chip bounces back to pool. Student can try again with a different slot. No attempt limit per chip — the student keeps trying until correct or timer expires.
- **Timer expired:** Remaining empty slots are auto-filled with correct keywords (shown in amber, not green). Student sees what they missed.
- **All distractors placed:** If a student places all distractors, the system gently nudges: "Hali emas! Barcha so'zlar xaritaga tegishli emas. 2 ta ortiqcha bor." (Not yet! Not all words belong on the map. 2 are extra.)

### After completion
- No retry within the session. The completed map is saved.
- Incorrectly placed or unplaced keywords are added to next session's Memory Sprint as priority items.
- **Hali emas framing:** Missing keywords shown as "Hali emas — keyingi safar topasiz!" (Not yet — you'll find it next time!)

---

## 11. Anti-Cheat Surface

| Signal | Detection | Response |
|---|---|---|
| All keywords placed in < 5 seconds | Timer check (Tier 1) | `SOFT_WARNING` — likely random guessing |
| Identical placement pattern across students | Cross-session pattern match (Tier 2) | `TEACHER_ALERT` if 3+ students have identical wrong-then-correct sequence |
| Supernova associations copy-pasted | Clipboard monitor (Tier 2) | `SOFT_WARNING` logged |

**Anti-cheat priority: LOW.** The mechanic's value is in the encoding act (drag-and-place), which cannot be meaningfully cheated — even random placement forces the student to see the correct structure during review.

---

## 12. Dual-Catalog Role

**Catalog: Default Pool — fills the "Mind maps" slot for G5-7**

**Session selection eligibility:**
- Primary home: Phase 5 (Consolidation / Mnemonic Lock)
- Also eligible: Phase 3 (Game Breaks) as a "Conceptual Organizer" round
- Counts as 1 of the 3 games required from the Default Pool
- Cannot be selected twice in the same session
- Subject frameworks may increase or decrease its priority weight

---

## 13. Cost Profile

| Layer | Work done | Cost |
|---|---|---|
| **Tier 1** | Map rendering, drag-and-drop interaction, keyword matching, XP calculation, Supernova word matching against pre-approved list | ~$0.0001 per round |
| **Tier 2** | Supernova Sprint fuzzy matching for G7+ open input (1 classifier call per batch of responses) | ~$0.001 per Supernova round |
| **Tier 3** | None | $0 |

**Estimated per-round cost: < $0.002**

---

## 14. Device Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Screen | 1024×768 (landscape) | 1280×720+ |
| Touch | Required (tap + drag for G5+, tap-to-select for G3-4) | Stylus optional |
| Bandwidth | ~200KB map assets (pre-cached) | Any connection |
| Offline | Full offline after cache | N/A |

---

## 15. Radiant UI Compliance (7 Laws Checklist)

Every Radiant Summary map MUST pass:

| # | Law | How This Mechanic Implements It |
|---|---|---|
| 1 | Central Image | `central_image` field mandatory — colorful icon, never text-only |
| 2 | Organic Branches | SVG curved paths with `stroke-linecap: round`, tapering width |
| 3 | Hierarchy | BOI branches 4px, sub-branches 2px, keyword chips 1px border |
| 4 | One Keyword/Branch | Each sub-branch slot accepts exactly one keyword chip |
| 5 | Emphasis | BOI labels 16px bold, sub-branch labels 14px regular |
| 6 | Association | Cross-branch arrows rendered for related concepts (content author marks these) |
| 7 | 3+ Colors | Each BOI has a distinct `color` field — enforced in schema (minimum 3 unique) |

---

## 16. Worked Example — Science G5: Photosynthesis

**Student:** 10-year-old G5, Standard mode

**Map presented:**
- Center: Sun + leaf icon labeled "Fotosintez"
- Branch 1 (green): "Kerakli moddalar" → 3 empty slots
- Branch 2 (orange): "Hosil bo'ladi" → 2 empty slots
- Branch 3 (blue): "Qayerda" → 1 empty slot + 1 pre-filled ("Barg")

**Keyword pool (8 chips):** Yorug'lik, Suv, CO₂, Shakar, Kislorod, Xloroplast, *Oqsil* (distractor), *Ildiz* (distractor)

**Student's actions:**
1. Drags "Yorug'lik" → "Kerakli moddalar" slot 1 → CORRECT (80 XP)
2. Drags "Suv" → "Kerakli moddalar" slot 2 → CORRECT (80 XP)
3. Drags "Oqsil" → "Kerakli moddalar" slot 3 → WRONG (bounces back, -10 XP)
4. Drags "CO₂" → "Kerakli moddalar" slot 3 → CORRECT (40 XP, second try)
5. Drags "Shakar" → "Hosil bo'ladi" slot 1 → CORRECT (80 XP)
6. Drags "Kislorod" → "Hosil bo'ladi" slot 2 → CORRECT (80 XP)
7. Drags "Xloroplast" → "Qayerda" slot → CORRECT (80 XP)
8. "Ildiz" left in pool (distractor avoided, +20 XP)
9. "Oqsil" left in pool (distractor correctly rejected after initial attempt, +20 XP)

**Placement score:** 80+80+40+80+80+80+20+20-10 = **470 XP**

**Supernova Sprint (not enabled for G5 default):** Skipped.

**Map saved to Bilim Bazasi.** "Oqsil" flagged for next session Memory Sprint (student confused it with an input of photosynthesis).

---

## Cross-References

- **UNIFIED spec §5.5** — Phase 5: Mnemonic Lock (Radiant Summary's home phase)
- **Sprint1-UI-UX-Amendments.md, UI-1** — Radiant UI Standard (7 Laws compliance)
- **Sprint1-UI-UX-Amendments.md, UI-2** — G5-6 Simplified Radiant Rules
- **Sprint1-Pipeline-QA-Gates.md, QG-3** — SMASHIN' SCOPE quality gate
- **Sprint1-Pipeline-QA-Gates.md, QG-1** — 80/20 keywords feed branch labels
- **NETS-Memory-Palace-Definition.md** — Sister mechanic in Phase 5 (spatial vs hierarchical encoding)
- **Game Mechanics DOCUMENTATION.md** — Follows same format conventions


---


# NETS Game Mechanic — Full Definition: Peg System

**Version:** 1.0  
**Date:** April 2026  
**Buzan Method Injected:** #29 (Peg System — Number-Shape, Number-Rhyme)  
**Status:** READY FOR REVIEW  
**Constitution:** `NETS-Homework-Engine-UNIFIED.md` v2.0  
**Sacred Rule:** Content unchanged. The peg images encode EXISTING textbook concepts — never invent new ones.

---

## 1. What It Is

A mnemonic mechanic that uses visual "pegs" — memorable images permanently associated with numbers 1-10 — as hooks for lesson concepts. The student associates each lesson concept with a numbered peg image, then is tested by being shown the peg and recalling the concept (or vice versa).

This mechanic fills the undefined "Peg system" slot listed in UNIFIED spec Phase 5 (G5-7 Consolidation techniques).

**Two peg types available:**
- **Number-Shape:** Each digit looks like an object (1 = Candle/Sham, 2 = Swan/Oqqush, 3 = Heart/Yurak...)
- **Number-Rhyme:** Each digit rhymes with a word in Uzbek (1 = Bir/Shir (lion), 2 = Ikki/Tikki (needle)...)

---

## 2. How It Is Played

### Step-by-step flow

**Phase A — Peg Introduction (first time only, 30 seconds)**
1. If the student has never used Peg System before, show the 5 pegs with their images
2. Student taps each peg to see the image and hear the number-shape association
3. "1 — Sham (Candle). Bitta sham — bir xil shakl!" (1 — Candle. One candle — same shape!)
4. This introduction is shown ONCE per student, then skipped in future sessions

**Phase B — Concept Association (45-60 seconds)**
5. Lesson's 5 key concepts appear in a list on the left
6. The 5 peg images appear in numbered order on the right
7. Student drags each concept to a peg (or taps concept then taps peg)
8. For each association, a brief "link sentence" appears to strengthen the connection:
   - System-generated: "Sham (1) yonmoqda — Fotosintez ham yorug'lik bilan boshlanadi!"
   - (Candle (1) is burning — Photosynthesis also starts with light!)
9. All 5 associations formed → brief review (all 5 shown together for 5 seconds)

**Phase C — Recall Test (45-60 seconds)**
10. Pegs shown one at a time in random order (NOT sequential)
11. For each peg: "Sham (1) — bu nima edi?" (Candle (1) — what was this?)
12. Student selects from 5 concept options (the 5 lesson concepts, shuffled)
13. **Correct:** Green highlight, peg + concept shown together
14. **Wrong:** Amber highlight, correct answer revealed with link sentence
15. After all 5 tested: reverse round — concept shown, student selects correct peg number

**Phase D — Score & Save**
16. Score summary shown
17. Peg associations saved to student profile for spaced repetition
18. XP awarded

### Core Loop Summary
```
Learn pegs (first time only) → Associate concepts to pegs (45-60s) → Recall test (45-60s) → Score
Total: 2-3 minutes
```

---

## 3. The Peg Set (Culturally Adapted for Uzbekistan)

### Number-Shape Pegs (Default for G5-6)

| # | Shape | Uzbek Name | Image Description | Visual Anchor |
|---|---|---|---|---|
| 1 | Candle | Sham | A tall, thin burning candle | Vertical line = 1 |
| 2 | Swan | Oqqush | A graceful white swan on water | Curved neck = 2 |
| 3 | Heart | Yurak | A red heart (two bumps + point) | Two curves + point = 3 |
| 4 | Sailboat | Yelkanli kema | A small boat with triangular sail | Sail shape = 4 |
| 5 | Hook | Ilgak | A metal hook (like a coat hook) | Hook shape = 5 |
| 6 | Elephant trunk | Fil xortumi | An elephant with curled trunk | Curled trunk = 6 |
| 7 | Cliff | Qoya | A cliff edge with a flag on top | Cliff angle = 7 |
| 8 | Snowman | Qorbobo | Two-ball snowman | Two circles = 8 |
| 9 | Balloon | Shar | A balloon on a string | Round top + string = 9 |
| 10 | Bat & ball | To'p va tayoq | A cricket/baseball bat with ball | 1 + 0 = bat + ball |

### Number-Rhyme Pegs (Alternative for G7+)

| # | Rhyme | Uzbek | Image | Why It Rhymes |
|---|---|---|---|---|
| 1 | Bir → Shir | Lion | A roaring lion | Bir/Shir rhyme in Uzbek |
| 2 | Ikki → Tikki | Needle | A sewing needle | Ikki/Tikki near-rhyme |
| 3 | Uch → Kuch | Fist/Power | A strong fist | Uch/Kuch rhyme |
| 4 | To'rt → Tort | Cake | A birthday cake | To'rt/Tort identical sound |
| 5 | Besh → Tesh | Hole | A deep hole in the ground | Besh/Tesh rhyme |
| 6 | Olti → Bolti | Bolt/Screw | A large metal bolt | Olti/Bolti rhyme |
| 7 | Yetti → Yetti (Bigfoot) | Yeti | A snow yeti in mountains | Yetti/Yeti identical |
| 8 | Sakkiz → Yakkiz | Solo hiker | A lone hiker with backpack | Sakkiz/Yakkiz near-rhyme |
| 9 | To'qqiz → So'qqiz | Bubblegum | A pink bubblegum bubble | To'qqiz/So'qqiz near-rhyme |
| 10 | O'n → To'n | Coat | A traditional Uzbek chapan coat | O'n/To'n rhyme |

**Selection rule:** Number-Shape is default for G5-6 (more visual, lower literacy demand). Number-Rhyme available as teacher/student toggle for G7+ (adds auditory encoding = extra Dual Coding channel).

---

## 4. Output / Evaluation

### Association Phase (Phase B)
No scoring — the learning is in forming the association. All placements accepted.

### Recall Test (Phase C)

| Direction | Result | Scoring |
|---|---|---|
| Peg → Concept | Correct on first try | 60 XP |
| Peg → Concept | Correct on second try | 30 XP |
| Peg → Concept | Wrong (both tries) | 0 XP, correct shown |
| Concept → Peg | Correct | 40 XP |
| Concept → Peg | Wrong | 0 XP, correct shown |
| **All 10 correct (both directions)** | Perfect round bonus | +100 XP |

### Maximum Score

| Round | Max XP |
|---|---|
| 5 Peg → Concept (all correct first try) | 300 XP |
| 5 Concept → Peg (all correct) | 200 XP |
| Perfect bonus | 100 XP |
| **Total max** | **600 XP** |

---

## 5. PISA Mapping

| PISA Level | How Peg System operates |
|---|---|
| L1 | Recall single concepts via visual cue (peg → concept) |
| L2 | Bi-directional recall (both peg → concept AND concept → peg) |
| L3 | Not this mechanic's domain |

**Primary PISA level:** L1-L2.  
**Transition skills:** `L1→L2: "Use visual mnemonic anchors to organize and retrieve factual information"`

---

## 6. Bloom's Band

| Bloom Level | Peg System role |
|---|---|
| **Remember** | Primary — encode and retrieve concept-peg pairs |
| **Understand** | Secondary — the "link sentence" requires understanding WHY the concept connects to the peg image |
| Apply+ | Not this mechanic's domain |

**Primary band: Remember**

---

## 7. Subject Eligibility

| Subject | Eligible | Best For |
|---|---|---|
| Science G5 | YES | 5 key terms per lesson (e.g., 5 stages of water cycle) |
| Math G5 | YES | 5 formula names, 5 geometric properties |
| History G5 | YES | 5 key dates, 5 historical figures per chapter |
| Geografiya G5 | YES | 5 map symbols, 5 biome names |
| All others | YES | Any subject with 5 discrete facts to memorize |

**No subject bans.** The mechanic is concept-agnostic.

---

## 8. Grade Eligibility

| Grade band | Status | Pegs used | Peg type | Recall format |
|---|---|---|---|---|
| G3-4 | Introductory | 3 pegs (1-3) | Number-Shape only | Peg → Concept only (one direction) |
| G5-6 | Standard | 5 pegs (1-5) | Number-Shape default | Both directions |
| G7-9 | Full | 5-7 pegs | Number-Shape or Number-Rhyme (student choice) | Both directions + timed |
| G10-11 | Advanced | 10 pegs | Either set | Both directions + student creates own link sentences |

---

## 9. Parameters / Difficulty Knobs

| Parameter | Range | Default (G5) | Effect |
|---|---|---|---|
| `peg_count` | 3-10 | 5 | More pegs = more associations to form and recall |
| `peg_type` | shape / rhyme | shape | Rhyme adds auditory channel |
| `association_time` | 30-90s | 45s | Less time = harder encoding |
| `recall_time` | 30-90s | 60s | Less time = more pressure |
| `bidirectional` | true/false | true | One direction = easier |
| `timed_recall` | true/false | false (G5) | Adds time pressure to recall |
| `student_link_sentences` | true/false | false | Student writes own links (G10+) |

---

## 10. Failure / Retry Behavior

- **Wrong recall:** Correct answer revealed with the link sentence. Concept added to next session's Memory Sprint as priority item.
- **0 out of 5 recalled:** "Hali emas! Peg rasmlarini eslang — ular sizning xotira ilgaklaringiz." (Not yet! Remember the peg images — they are your memory hooks.)
- **No retry within session.** Spaced repetition handles reinforcement.
- Peg associations saved and revisited per Buzan Review Intervals (10min → 24h → 1w → 1mo).

---

## 11. Anti-Cheat Surface

| Signal | Detection | Response |
|---|---|---|
| All associations formed in < 3 seconds | Timer (Tier 1) | `SOFT_WARNING` |
| All recalls correct in < 5 seconds | Timer (Tier 1) | Suspicious but not flagged (pegs are designed to be fast) |

**Anti-cheat priority: LOWEST.** The mechanic's value is in the encoding act. Even memorizing the answer sequence requires using the pegs — which is the goal.

---

## 12. Dual-Catalog Role

**Catalog: Default Pool — fills the "Peg system" slot for G5-7**

**Session selection eligibility:**
- Primary home: Phase 5 (Consolidation / Mnemonic Lock)
- Also eligible: Phase 3 (Game Breaks) when integrated with Tic Tac Toe vs AI
- Counts as 1 of the 3 Default Pool selections
- Cannot appear in same session as Radiant Summary (consolidation slot is shared — one OR the other)

### Tic Tac Toe Integration

When Peg System and Tic Tac Toe are both selected in a session:
- The 9 Tic Tac Toe cells are labeled with peg numbers (1-9)
- To place an X on cell #3, the student must recall: "Yurak (3) — bu nima edi?" (Heart (3) — what was this?)
- Correct recall of the pegged concept = X placed
- This merges spatial strategy (Tic Tac Toe) with mnemonic retrieval (Peg System)

---

## 13. Cost Profile

| Layer | Work done | Cost |
|---|---|---|
| **Tier 1** | Peg image serving, drag-and-drop, recall matching, link sentence display, XP | ~$0.0001 |
| **Tier 2** | None (all link sentences pre-authored) | $0 |
| **Tier 3** | None | $0 |

**Estimated per-round cost: < $0.001** — cheapest mechanic in the catalog.

---

## 14. Device Requirements

| Requirement | Minimum |
|---|---|
| Screen | 1024×768 |
| Touch | Tap required, drag optional (tap-to-select fallback) |
| Bandwidth | ~100KB peg images (pre-cached) |
| Offline | Full offline after cache |

---

## 15. Worked Example — History G5: Silk Road Key Facts

**Topic:** 5 key facts about the Silk Road  
**Peg type:** Number-Shape

**Associations formed:**

| Peg # | Peg Image | Concept | Link Sentence |
|---|---|---|---|
| 1 | Sham (Candle) | Ipak Yo'li boshlangan yil: mil. avv. II asr | "Sham yonmoqda — Ipak Yo'lining birinchi savdo karvoni yo'lga chiqmoqda!" |
| 2 | Oqqush (Swan) | Samarqand — asosiy shahar | "Oqqush Samarqand hovuzida suzmoqda — go'zal shahar!" |
| 3 | Yurak (Heart) | Ipak — asosiy tovar | "Yurak ipakdan tikilgan — eng qimmatli mato!" |
| 4 | Yelkanli kema (Sailboat) | Dengiz yo'li — alternativa | "Kema bilan ham borsa bo'lardi — lekin cho'l yo'li arzonroq edi!" |
| 5 | Ilgak (Hook) | Madaniy almashish — asosiy natija | "Ilgakka turli xalqlar madaniyati ilingan — hammasi aralashtb!" |

**Recall test:**
- Shown: Swan image → "Bu nima edi?" → Student selects "Samarqand" → CORRECT (60 XP)
- Shown: Hook image → "Bu nima edi?" → Student selects "Ipak" → WRONG → Correct shown: "Madaniy almashish" (0 XP)
- ... (continues for all 5 + reverse direction)

**"Madaniy almashish"** added to tomorrow's Memory Sprint.

---

## Cross-References

- **UNIFIED spec §5.5** — Phase 5: Mnemonic Lock (Peg System's home phase)
- **Sprint1-AI-Tutor-Language.md, #29** — Peg-specific tutor phrases
- **Sprint1-Pipeline-QA-Gates.md, QG-3** — SMASHIN' SCOPE for link sentences
- **Game Mechanics DOCUMENTATION.md, #11** — Tic Tac Toe (integration partner)
- **Sprint2-Radiant-Summary-Specification.md** — Sister mechanic (cannot co-occur in same session Phase 5)


---


# Buzan Injection — Sprint 2: Phase 1 & Phase 2 Amendments

**Methods Injected:** #28 (Link System), #34 (Buzan Review Intervals), #16 (Fixation Training), #18 (Regression Elimination), #21 (Sub-vocalization Elimination), #23 (Meta-Guiding)  
**Sacred Rule:** Content unchanged. These change delivery formats and reading mechanics, not lesson content.

---

## PART 1: Phase 1 Amendments (Memory Sprint)

### A. Link Chain — New Memory Sprint Format #6 (Method #28)

**What it adds:** A sixth approved format for Phase 1 Memory Sprint, alongside Quick MC, Speed Match, Flash Sprint, Fill-in-Blanks, and Order Steps.

#### Format Definition

| Field | Value |
|---|---|
| **Name** | Link Chain |
| **Type** | Memory Sprint format (not a standalone game mechanic) |
| **Duration** | ≤ 2 minutes (within existing Memory Sprint time cap) |
| **Items** | 5 sequential items from previous chapters |
| **AI Tier** | Tier 1 (pre-generated link stories) |

#### How It Works

**Study Phase (15 seconds):**
1. 5 items from previous chapters are displayed in a numbered list
2. A pre-authored "link story" appears beneath, connecting all 5 items in a vivid chain:
   - Example: "A **Candle** (Sham) lights up a **Swan** (Oqqush) who swims to **Samarkand** carrying **Silk** (Ipak) that floats on **Water** (Suv)..."
3. The story uses SMASHIN' SCOPE principles: movement, exaggeration, humor, color
4. Student reads the story for 15 seconds

**Recall Phase (45 seconds):**
5. The story disappears
6. Items are presented OUT OF ORDER as 5 rapid questions:
   - "What came after the Swan?" → Student selects from 4 options
   - "What was the 3rd item in the chain?" → Student selects
   - "What triggered the Silk to appear?" → Student selects
7. Scoring: +60 XP per correct, +100 bonus for all 5 correct

#### When to Use Link Chain

| Best For | Not Recommended |
|---|---|
| Sequential content (process steps, historical timelines) | Unrelated vocabulary items (use Flash Sprint instead) |
| Science processes (water cycle, digestion steps) | Mathematical formulas (use Speed Match instead) |
| Historical cause-effect chains | Abstract concepts with no natural sequence |

#### Link Story Quality Gate

Every link story must score **6+/12 on SMASHIN' SCOPE** (same gate as all mnemonic content). The story must use the TEXTBOOK'S actual terms — never substitute or simplify them.

#### Content Author Schema Addition

```json
{
  "memory_sprint_item": {
    "format": "link_chain",
    "items": [
      { "order": 1, "term_uz": "Bug'lanish", "standard_ref": "UZ-SCI-5-EARTH-04" },
      { "order": 2, "term_uz": "Kondensatsiya", "standard_ref": "UZ-SCI-5-EARTH-04" },
      { "order": 3, "term_uz": "Yog'ingarchilik", "standard_ref": "UZ-SCI-5-EARTH-04" },
      { "order": 4, "term_uz": "Oqim", "standard_ref": "UZ-SCI-5-EARTH-04" },
      { "order": 5, "term_uz": "Shimilish", "standard_ref": "UZ-SCI-5-EARTH-04" }
    ],
    "link_story_uz": "Bug'lanish — Quyosh issiqligida suv UCHIB ketdi! Osmonda sovib KONDENSATSIYA bo'ldi — katta bulut! Bulut og'irlashdi va YOG'INGARCHILIK boshlandi — yomg'ir! Suv tog'dan pastga OQIM bo'lib oqdi... va nihoyat tuproqqa SHIMILIB ketdi!",
    "smashin_scope_score": 8,
    "recall_questions": [
      { "question_uz": "Bug'lanishdan keyin nima bo'ldi?", "correct": "Kondensatsiya", "distractors": ["Oqim", "Shimilish", "Yog'ingarchilik"] },
      { "question_uz": "3-chi bosqich nima edi?", "correct": "Yog'ingarchilik", "distractors": ["Bug'lanish", "Oqim", "Kondensatsiya"] }
    ]
  }
}
```

---

### B. Buzan Review Intervals — SM-2 Floor Constraints (Method #34)

**What it adds:** Four mandatory review touchpoints that override the SM-2 spaced repetition algorithm when SM-2 would schedule a review LATER than Buzan's intervals.

#### The Rule

```
Buzan_mandatory_touchpoints = [
  { interval: "~10 minutes",  where: "Phase 5 of SAME session" },
  { interval: "~24 hours",    where: "Phase 1 Memory Sprint of NEXT session" },
  { interval: "~1 week",      where: "Phase 1 Memory Sprint, 7 days later" },
  { interval: "~1 month",     where: "Phase 1 Memory Sprint, 30 days later" }
]

FOR EACH concept learned in current session:
  sm2_next_review = SM2.calculate_next_review(concept)
  buzan_next_mandatory = Buzan_mandatory_touchpoints.next_upcoming()
  
  actual_next_review = MIN(sm2_next_review, buzan_next_mandatory)
  // Whichever schedules the review SOONER wins
```

#### How Each Touchpoint Maps

| Touchpoint | NETS Implementation | Already Exists? |
|---|---|---|
| **~10 min** | Phase 5 Consolidation of the same session. Concepts learned in Phase 2 appear in Phase 5 (Radiant Summary, Peg System, Memory Palace, or other mnemonic). | YES — Phase 5 already reviews same-session content |
| **~24 hours** | Phase 1 Memory Sprint of the NEXT day's session. Concepts from yesterday are prioritized in the recall item selection algorithm. | PARTIAL — SM-2 may schedule later. **ADD:** Buzan 24h floor forces concepts into next-day Sprint regardless of SM-2 score. |
| **~1 week** | Phase 1 Memory Sprint, ~7 days after initial learning. | PARTIAL — SM-2 handles this but may delay for "Easy" rated items. **ADD:** Buzan 1w floor forces review even for "Easy" items. |
| **~1 month** | Phase 1 Memory Sprint, ~30 days after initial learning. | PARTIAL — same issue. **ADD:** Buzan 1mo floor. |

#### Amendment to Memory Sprint Item Selection Algorithm

Current algorithm (UNIFIED spec §5.1):
```
1. GET all recall_items from chapters BEFORE current
2. PRIORITIZE by forgetting curve (wrong → approaching threshold → not seen in 7+ days)
3. FILTER to 5-8 items
4. RANDOMIZE order
```

**Add after step 2:**
```
2b. INJECT Buzan mandatory items:
    FOR EACH concept WHERE buzan_touchpoint is due today:
      IF concept NOT already in prioritized list:
        INSERT concept at HIGH priority (above "approaching threshold", below "wrong in previous session")
      IF prioritized list exceeds 8 items after injection:
        DROP lowest-priority non-Buzan item
    
    LOG: "Buzan Review: [N] mandatory items injected into Memory Sprint"
```

#### Missed Session Handling

If a student misses a session (e.g., the 24h touchpoint falls on a day with no homework):
- The touchpoint shifts to the NEXT available session
- It does NOT skip — the touchpoint is delayed, never dropped
- If two Buzan touchpoints stack (e.g., 24h and 1w both due), both concepts enter the Sprint (may displace more lower-priority items)

---

## PART 2: Phase 2 Amendments (Story Mode)

### C. Focus Guide — Adaptive Reading Pacer (Methods #16, #21, #23)

**What it adds:** An optional visual pacing system for Story Mode text that trains speed reading mechanics — fixation chunking, sub-vocalization elimination, and meta-guiding — without changing any content.

#### How It Works

1. During Story Mode narrative segments, a **highlight bar** moves across the text
2. The bar highlights **3-5 words at a time** (one semantic chunk)
3. The bar advances automatically at a speed calibrated to the student's reading level
4. The bar speed is **5-10% faster** than the student's established reading pace (pushing gently beyond sub-vocalization speed)
5. Students can tap to pause/resume the guide
6. The guide is **optional** — toggled on/off via a small "Focus" icon in the reading toolbar

#### Speed Calibration

```
student_reading_wpm = derived from Story Mode time-per-segment data (tracked automatically)

focus_guide_wpm = student_reading_wpm × 1.07  // 7% faster (middle of 5-10% range)

// Adaptive adjustment after each segment:
IF student answered checkpoint correctly AND did not tap pause:
  focus_guide_wpm += 5  // Student keeping up — push slightly more
IF student answered checkpoint incorrectly OR tapped pause 2+ times:
  focus_guide_wpm -= 10  // Too fast — pull back
  
MIN_WPM = 80   // Never slower than 80 WPM (below this, reading is not the issue)
MAX_WPM = 300  // Never faster than 300 WPM (above this, comprehension drops)
```

#### Visual Specification

```css
.focus-guide-highlight {
  background: rgba(255, 213, 79, 0.35);  /* Soft amber highlight */
  border-radius: 3px;
  transition: left 0.15s ease-out;        /* Smooth movement between chunks */
  padding: 2px 0;
}

.focus-guide-toggle {
  position: fixed;
  bottom: 16px;
  right: 16px;
  /* Small eye icon — tap to toggle */
}
```

#### Grade Behavior

| Grade | Default state | Speed range | Chunk size |
|---|---|---|---|
| G3-4 | OFF (available on toggle) | 80-150 WPM | 2-3 words |
| G5-6 | OFF (recommended, prompted once) | 100-200 WPM | 3-4 words |
| G7-9 | OFF (available) | 120-250 WPM | 3-5 words |
| G10-11 | OFF (available) | 150-300 WPM | 4-5 words |

**Never forced ON.** The Focus Guide is always optional. Students who prefer natural reading are never penalized.

#### AI Tier & Cost

- **Tier 1:** Chunk boundaries pre-computed during content pipeline (word grouping based on syntactic structure). Speed calculation is arithmetic.
- **Cost:** Zero marginal cost. Computation is client-side.

---

### D. Forward Momentum Rule (Method #18)

**What it adds:** For G5-6 students, Story Mode text presentation becomes forward-biased. After advancing to the next narrative segment, the previous segment fades and requires a deliberate button press to revisit.

#### How It Works

1. Student reads Segment 1 and answers Checkpoint 1
2. Student swipes/taps to advance to Segment 2
3. **Segment 1 fades to 30% opacity and becomes non-scrollable**
4. A small "Qaytish" (Go Back) button appears at the top of the faded segment
5. Tapping "Qaytish" restores the segment to full visibility for 30 seconds, then re-fades
6. This friction discourages unconscious regressions while preserving deliberate re-reading

#### Grade Behavior

| Grade | Forward Momentum |
|---|---|
| G3-4 | OFF (free scrolling — young readers need to re-read frequently) |
| G5-6 | ON by default (toggleable off in settings) |
| G7+ | OFF (students at this level have established reading habits) |

#### Rationale

Buzan identifies **regressions** (re-reading previous text) as the #1 speed killer. For G5-6, unconscious back-skipping is common and reduces both speed and comprehension (by breaking the flow of thought). The Forward Momentum Rule creates just enough friction to make regressions conscious — the student can still go back, but must choose to.

---

## Summary

| Deliverable | Method(s) | Phase | Type |
|---|---|---|---|
| Link Chain format | #28 | Phase 1 | New Memory Sprint format (6th) |
| Buzan Review Intervals | #34 | Phase 1 + system-wide | SM-2 algorithm floor constraints |
| Focus Guide | #16, #21, #23 | Phase 2 | Optional reading pacer feature |
| Forward Momentum Rule | #18 | Phase 2 | G5-6 regression elimination |


---


# Buzan Injection — Sprint 3: Phase 3-7 + Phase 0-A Amendments

**Methods Injected:** #4 (Radiant Problem Solving), #5 (Decision Mapping), #14 (Von Restorff), #15 (Anti-Cheat Radiant Signature), #24 (Pre-reading), #25 (Cortical Synergy), #26 (Primacy & Recency), #30 (Major System), #33 (The MIG)  
**Sacred Rule:** Content unchanged. All amendments change delivery mechanics, selection algorithms, or scaffolding — never textbook content.

---

## 1. Phase 0-A: Structural Scan for Panel 1 (Method #24)

### What Changes

Theme Preview Panel 1 ("Summary of Book Content") gains an optional **Structural Scan** layout that trains pre-reading/scanning skills before deep reading in Phase 2.

### Structural Scan Layout

Instead of rendering the chapter summary as flowing paragraphs, the Structural Scan presents:

1. **Heading Tree** — The chapter's heading hierarchy displayed as an indented outline:
   ```
   4-bob: Fotosintez
     ├── 4.1 Yorug'lik va o'simliklar
     ├── 4.2 Fotosintez jarayoni
     │     ├── Kerakli moddalar
     │     └── Hosil bo'ladigan moddalar
     └── 4.3 Xlorofill
   ```

2. **Bold-Term Highlights** — All bold/key terms from the chapter extracted and displayed as a horizontal chip row:
   `Fotosintez` `Xlorofill` `CO₂` `Kislorod` `Shakar` `Barg`

3. **Diagram Thumbnail Grid** — Small preview images of all diagrams/figures in the chapter (tappable to enlarge)

### Design Rules

- Structural Scan is the **default layout for G5+**. Flowing paragraph layout remains available as a toggle ("Batafsil" / Detailed).
- For G3-4: flowing paragraph layout remains default (reading skill insufficient for scanning).
- The content is identical — only the visual arrangement changes.
- No scoring, no interaction beyond tapping diagram thumbnails.

### Content Author Schema Addition

```json
{
  "theme_preview_panel_1": {
    "layout": "structural_scan",
    "heading_tree": [
      { "level": 1, "text_uz": "4-bob: Fotosintez" },
      { "level": 2, "text_uz": "4.1 Yorug'lik va o'simliklar" },
      { "level": 2, "text_uz": "4.2 Fotosintez jarayoni" },
      { "level": 3, "text_uz": "Kerakli moddalar" },
      { "level": 3, "text_uz": "Hosil bo'ladigan moddalar" },
      { "level": 2, "text_uz": "4.3 Xlorofill" }
    ],
    "bold_terms": ["Fotosintez", "Xlorofill", "CO₂", "Kislorod", "Shakar", "Barg"],
    "diagram_thumbnails": [
      { "id": "fig_4_1", "desc": "Fotosintez jarayoni diagrammasi", "page": 39 },
      { "id": "fig_4_2", "desc": "Barg tuzilishi", "page": 40 }
    ]
  }
}
```

---

## 2. Phase 3: Cortical Diversity Constraint (Method #25)

### What Changes

The Phase 3 game selection algorithm (UNIFIED spec §5.3) gains a new constraint ensuring each session activates multiple cognitive modalities.

### Cortical Modality Tags

Every game mechanic in both pools (Default + Interactive) receives a modality tag:

| Modality | Code | Game Mechanics |
|---|---|---|
| **Verbal / Logical** | `VL` | Sentence Fill, Adaptive Quiz, Why Chain, Codebreaker |
| **Visual / Spatial** | `VS` | Tile Match, Memory Palace, Radiant Summary, Puzzle Lock, Memory Sprint |
| **Kinesthetic / Motor** | `KM` | Notebook Capture, Movement Breaks |
| **Strategic / Decision** | `SD` | Tic Tac Toe, Connect Four, Blackjack 21, Mystery Box |
| **Productive / Generative** | `PG` | Peer Teaching, Reflection Journal |

### Selection Rule Addition

```
EXISTING RULE: 3 games per session (≥1 Interactive, ≥2 Default)

NEW CONSTRAINT — Cortical Diversity:
  selected_games = select_3_games(existing_rules)
  
  modalities = unique(game.modality FOR game IN selected_games)
  
  IF modalities.count < 2:
    REPLACE the game with lowest priority_score with the highest-scoring 
    game from a DIFFERENT modality
    
  // Ensures at least 2 different cortical modalities per session
```

### Example

Session selects: Sentence Fill (`VL`), Adaptive Quiz (`VL`), Codebreaker (`VL`) — all verbal/logical.

Cortical Diversity triggers: Replace Codebreaker with Tile Match (`VS`) or Puzzle Lock (`VS`) — now the session has VL + VS = 2 modalities.

---

## 3. Phase 3: Von Restorff Anchor (Method #14)

### What Changes

One game per session is tagged as the **Von Restorff Anchor** — the deliberately unusual, surprising, or visually striking moment that exploits the Von Restorff Effect (outstanding items are remembered better).

### How It Works

```
DURING session_plan.build():

  // After game selection, identify the anchor
  von_restorff_anchor = game_at_position_2  // Middle game (Sag position)
  
  // The anchor game instance gets a special content flag:
  von_restorff_anchor.content_flag = "outstanding"
  
  // Content pipeline must ensure this game instance contains at least ONE:
  //   - Unusual visual (unexpected image, vivid color, surprising diagram)
  //   - Surprising fact (a "Did you know?" embedded in a question)
  //   - Humorous framing (a funny scenario wrapping a real question)
  //   - Exaggerated element (deliberately oversized number, extreme comparison)
```

### Content Author Requirement

For each lesson's game content pool, at least **3 items** must be tagged `outstanding: true`. These items are preferentially selected when the game is assigned as Von Restorff Anchor.

```json
{
  "game_item": {
    "existing_fields": "...",
    "outstanding": true,
    "outstanding_type": "surprising_fact",
    "outstanding_detail": "Students learn that a single tree can produce enough oxygen for 2 people — framed as 'Your backyard tree is breathing for your whole family!'"
  }
}
```

### Position Rationale

The Von Restorff Anchor is always the **middle game** (Game Break 2 of 3). This is the "Sag" position on Buzan's MIG graph — recall naturally dips in the middle of a session. The outstanding moment resets attention and creates a memorable peak that bridges the primacy/recency gap.

---

## 4. Phase 4: W5H Radiant Analysis Scaffold (Method #4)

### What Changes

Real-Life Challenge (Phase 4) gains an optional pre-solution scaffolding step: a **W5H Radiant Frame** (Who/What/Where/When/Why/How) that forces structured problem decomposition before the student writes their answer.

### How It Works

1. Scenario text is presented (existing — no change)
2. **NEW STEP:** Before the answer area opens, a 6-branch radiant frame appears:
   ```
           WHO
            |
   WHERE -- [PROBLEM] -- WHAT
            |
           WHEN
          /    \
       WHY     HOW
   ```
3. Each branch has a short text input field (1-2 words or a phrase)
4. Student fills **at least 4 of 6 branches** (minimum enforced)
5. After filling, the answer area opens for the full response
6. The W5H frame stays visible as a sidebar reference while writing

### Grade Differentiation

| Grade | Minimum branches | W5H scaffold |
|---|---|---|
| G5-6 | 4 of 6 | Mandatory (always shown) |
| G7-8 | 5 of 6 | Default ON, toggleable off |
| G9+ | Optional | Available via "Tahlil" (Analyze) button |

### Scoring

The W5H frame itself is NOT scored. It is a scaffolding tool. The student's final answer (which benefits from the structured thinking) is scored using the existing rubric.

### AI Tier

- Tier 1: The frame is a static UI component with text inputs.
- No AI evaluation of W5H content.

---

## 5. Phase 5: Major System for G7+ (Method #30)

### What Changes

Phase 5 Consolidation technique table gains a new entry for G7+: the **Major System** (phonetic digit code) for memorizing numbers — dates, constants, statistical data.

### How It Works

The Major System maps each digit to a consonant sound:

| Digit | Consonant(s) | Uzbek Adaptation | Mnemonic |
|---|---|---|---|
| 0 | S, Z | S, Z | **S**ifr (zero) |
| 1 | T, D | T, D | **T**ik (upright, like 1) |
| 2 | N | N | **N** has 2 legs |
| 3 | M | M | **M** has 3 legs |
| 4 | R | R | Fou**r** ends in R |
| 5 | L | L | **L**atin 50 = L |
| 6 | J, Ch, Sh | J, Ch, Sh | **J** mirror = 6 |
| 7 | K, G | K, G | **K** looks like two 7s |
| 8 | F, V | F, V | **F** in cursive = 8 |
| 9 | P, B | P, B | **P** mirror = 9 |

Vowels (a, e, i, o, u) and W, H, Y are fillers — they don't count.

### Session Flow

1. System presents a number to memorize (e.g., **1441** — birth year of Alisher Navoi)
2. System shows the consonant conversion: 1-4-4-1 → T-R-R-T
3. System suggests a memorable word: **"TURT"** (Turtle → Toshbaqa)
4. A vivid image is shown: "Toshbaqa Alisher Navoiy kitobini o'qimoqda!" (A turtle reading a Navoi book!)
5. Student confirms or creates their own word (advanced option)
6. Recall test: "Navoiy qachon tug'ilgan?" → Student recalls Turtle → T-R-R-T → 1441

### Availability

| Aspect | Rule |
|---|---|
| Grade | G7+ only (abstract phonetic mapping exceeds G5-6 developmental stage) |
| Subjects | History (dates), Chemistry (constants), Physics (constants), Math (Pi digits) |
| AI Tier | Tier 2 (word generation from consonant string requires LLM; pre-generation preferred) |
| Frequency | 1-2 numbers per session maximum (cognitive overhead is high) |

### Phase 5 Technique Table Update

| Grade Band | Available Techniques (updated) |
|---|---|
| 1-2 | Chunking, Rhymes, Songs |
| 3-4 | Memory Palace intro, Acronyms, Dual coding |
| 5-7 | Full Memory Palace (Loci), **Peg System**, **Radiant Summary**, Link System |
| 7-9 | All G5-7 + **Major System (phonetic code)**, Spaced retrieval mastery |
| 10-11 | All G7-9 + Self-directed systems, Autonomous consolidation |

---

## 6. Phase 5: Link System Technique (Method #28 extension)

### What Changes

Link System (already defined as Memory Sprint format "Link Chain" in Sprint 2) is also available as a Phase 5 Consolidation technique for sequential content.

### When Phase 5 Uses Link System (vs Memory Palace vs Radiant Summary)

| Content Type | Best Technique | Why |
|---|---|---|
| **Sequential process** (water cycle, digestion) | **Link System** | Chain preserves ORDER — each item triggers the next |
| **Spatial facts** (locations, map features) | **Memory Palace** | Loci leverages spatial memory |
| **Hierarchical categories** (classifications, concept families) | **Radiant Summary** | Branches show RELATIONSHIPS between categories |
| **Discrete facts** (5 key terms, 5 dates) | **Peg System** | Pegs give random-access to numbered items |

The session assembler selects the technique based on the content's `structure_type` tag:

```json
{
  "mnemonic_exercise": {
    "structure_type": "sequential | spatial | hierarchical | discrete",
    "technique": "auto"  // Session assembler picks based on structure_type
  }
}
```

---

## 7. Phase 6: Decision Map Boss Question Format (Method #5)

### What Changes

Final Boss gains a new question format: **Decision Map** — for questions that involve choosing between competing options with trade-offs.

### How It Works

1. Central problem statement displayed in the center
2. Two (or three) competing options radiate as branches from the center
3. Each option has 2-3 pro/con sub-branches (partially filled by the system)
4. Student must:
   a. Complete the missing pro/con branches (drag from a pool)
   b. Assign weights (1-5 scale) to each pro and con
   c. Select their recommended option
   d. Write a 1-2 sentence justification

### Question Schema

```json
{
  "boss_question": {
    "format": "decision_map",
    "problem_uz": "Shahar hokimiyati yangi park qurmoqchi. Ikki joy taklif qilingan.",
    "options": [
      {
        "label_uz": "A joy: Shahar markazi",
        "pros_given": ["Hammaga yaqin"],
        "pros_missing": ["Transport qulay"],
        "cons_given": ["Yer narxi yuqori"],
        "cons_missing": ["Shovqin ko'p"]
      },
      {
        "label_uz": "B joy: Shahar chekkasi",
        "pros_given": ["Yer arzon"],
        "pros_missing": ["Toza havo"],
        "cons_given": ["Transportda muammo"],
        "cons_missing": ["Odamlar kam keladi"]
      }
    ],
    "scoring_rubric": {
      "branch_completion": "50% — correctly placing missing pros/cons",
      "weight_assignment": "25% — reasonable weight distribution (not all 5s)",
      "justification": "25% — reasoning references at least 2 pros/cons"
    },
    "pisa_level": 4,
    "blooms": "evaluate"
  }
}
```

### Availability

- **Boss tiers:** Big Boss and Mythical Boss only (Sub Boss uses standard question formats)
- **Question distribution:** Maximum 1 Decision Map per Boss fight
- **Subjects:** All subjects where trade-off decisions exist (Geography, Science, History, Tarbiya)
- **AI Tier:** Tier 1 (pre-authored options and scoring rubric)

---

## 8. Phase 7: TEFCAS Reflection Prompts (Method #11)

Already fully defined in Sprint 1 — `Sprint1-AI-Tutor-Language.md`, Part 2. No additional specification needed. This section confirms the Phase 7 amendment is complete.

---

## 9. Anti-Cheat: Radiant Signature Check #7 (Method #15)

### What Changes

Section 13 (Anti-Cheat System) gains a 7th integrity check: **Radiant Response Signature Analysis**.

### Concept

AI-generated text and copy-pasted answers tend to be **perfectly linear** — sequential logic, standard vocabulary, no personal markers. Genuine student responses trained in radiant thinking show **idiosyncratic patterns** — non-linear associations, personal keywords, varied sentence structure, informal language.

### Signal Features

| Feature | Linear (suspicious) | Radiant (authentic) |
|---|---|---|
| Sentence structure | All sentences same length and pattern | Varied — short bursts + longer reasoning |
| Vocabulary | Textbook-standard throughout | Mix of textbook terms + personal/informal words |
| Logic flow | A → B → C → D (perfectly sequential) | A → C → B → "reminds me of" → D (associative jumps) |
| Personal markers | Zero personal references | "Men o'ylayman..." (I think), "Bu menga... eslatadi" (This reminds me of) |
| Keyword reuse | Each term used exactly once | Key terms repeated in different contexts (natural reinforcement) |

### Detection Algorithm

```
FOR EACH open_text_response IN [Phase 4 answers, Phase 6 Boss answers, Peer Teaching]:

  linear_score = (
    sentence_length_variance(response)      // Low variance = suspicious
    + vocabulary_diversity_index(response)   // Low diversity = suspicious
    + personal_marker_count(response)        // Zero markers = suspicious
    + associative_jump_count(response)       // Zero jumps = suspicious
  )
  
  IF linear_score < THRESHOLD:
    flag = "RADIANT_SIGNATURE_MISSING"
    severity = "SOFT_WARNING"
    // Does NOT auto-fail — adds to teacher dashboard pattern
    
  IF linear_score < THRESHOLD AND (
    response_time < 30 seconds for 200+ word answer OR
    clipboard_paste_detected
  ):
    flag = "HIGH_PROBABILITY_AI_OR_COPY"
    severity = "TEACHER_ALERT"
```

### AI Tier & Cost

- **Tier 2:** The signature analysis requires a lightweight text classifier (not a full LLM call). Estimated ~$0.0005 per response analyzed.
- Only applied to open-text responses in Phase 4, Phase 6, and Peer Teaching. NOT applied to MC, drag-and-drop, or other closed-format interactions.

---

## 10. Primacy, Recency & MIG Formalization (Methods #26, #33)

### What Changes

Documentation-only. Adds an explicit paragraph to the UNIFIED spec preamble explaining that the 7-phase structure is the MIG (Most Important Graph in the World) in action.

### Text to Add

> **The MIG Alignment.** The NETS 7-phase structure is a direct implementation of Buzan's "Most Important Graph in the World" (MIG), which describes how recall varies during a learning session:
> 
> - **Primacy Effect:** Recall is highest at the start → Phase 1 (Memory Sprint) places the most important recall items first.
> - **Recency Effect:** Recall is highest at the end → Phase 7 (Reflection) ensures the last mental act is metacognitive consolidation.
> - **Association Effect:** We remember what connects to existing knowledge → Phase 0-A/0-B (Theme Preview, Flash Cards) activate prior schemas.
> - **Von Restorff Effect:** We remember the outstanding → Phase 3 (Game Breaks) mid-session anchor provides a memorable peak.
> - **The Sag:** Recall dips in the middle → Phase 3 Game Breaks deliberately break the session into shorter sub-sessions, resetting the Primacy/Recency curve multiple times.
> 
> The 7-phase structure is not arbitrary. It is engineered to maximize recall at every point in the session by exploiting these five memory effects.

---

## Summary

| # | Method | Phase | Type |
|---|---|---|---|
| 24 | Pre-reading (Structural Scan) | P0-A | Panel 1 layout redesign |
| 25 | Cortical Synergy | P3 | Game selection algorithm constraint |
| 14 | Von Restorff Anchor | P3 | Content tagging + position rule |
| 4 | Radiant Problem Solving (W5H) | P4 | Pre-solution scaffold |
| 30 | Major System | P5 (G7+) | New consolidation technique |
| 28 | Link System (P5 extension) | P5 | Technique selection logic |
| 5 | Decision Mapping | P6 | New Boss question format |
| 11 | TEFCAS Reflection | P7 | Already complete (Sprint 1) |
| 15 | Anti-Cheat Radiant Signature | Section 13 | New Check #7 |
| 26+33 | Primacy/Recency + MIG | Preamble | Documentation formalization |


---


# Buzan Injection — Sprint 3: UI/UX Feature Specs

**Methods Injected:** #1 (Radiant Navigation), #16/#21/#23 (Focus Guide visual), #20 (Semantic Chunking)  
**Deliverables:** 19-21  
**Sacred Rule:** These change visual presentation, never content.

---

## 1. Focus Guide Visual Specification (Deliverable 19, Methods #16, #21, #23)

Functional behavior already defined in `Sprint2-Phase1-Phase2-Amendments.md`, Part 2C. This section defines the visual/animation spec for the UI/UX design document.

### Visual Elements

| Element | Specification |
|---|---|
| **Highlight shape** | Rounded rectangle spanning the current chunk (3-5 words) |
| **Highlight color** | `rgba(255, 213, 79, 0.35)` — soft amber (non-intrusive) |
| **Animation** | Smooth slide to next chunk: `transition: left 0.15s ease-out` |
| **Chunk gap** | When highlight moves to next chunk, previous chunk returns to normal text (no lingering highlight) |
| **Toggle button** | Small eye icon (open eye = ON, closed eye = OFF), positioned bottom-right of reading surface |
| **Toggle state** | Persists per session. Resets to OFF at session start (never auto-enabled). |
| **Speed indicator** | Tiny WPM number in the toggle button corner (visible only when ON): e.g., "142" |
| **Pause behavior** | Tap anywhere on text to pause. Tap again to resume. Paused state shows a subtle pulsing highlight at current position. |

### Responsive Layout

| Screen | Behavior |
|---|---|
| Mobile (< 768px) | Highlight spans full line width if chunk is near edge. Toggle button bottom-center. |
| Tablet (768-1024px) | Standard behavior. Toggle bottom-right. |
| Desktop (> 1024px) | Standard behavior. Text container already capped at 640px. |

### Accessibility

- Focus Guide does NOT interfere with screen readers (highlight is purely visual CSS, no DOM reflow)
- Color contrast of highlighted text meets WCAG AA (amber on white = 3.2:1 for large text — passes)
- Students with photosensitive conditions: highlight can be switched to underline mode (bottom border instead of background)

---

## 2. Semantic Chunking Rendering Rule (Deliverable 20, Method #20)

### What It Is

Story Mode text for G5-6 is rendered with slightly wider gaps between semantic chunks (3-5 word groups), training the eye to fixate on meaningful units rather than individual words.

### Visual Specification

```css
/* Applied to Story Mode narrative text for G5-6 only */
.chunked-text .chunk {
  display: inline;
  margin-right: 0.4em;  /* Extra gap between chunks (normal word gap = ~0.25em) */
}

/* Visual: no borders, no backgrounds — just spacing */
/* The chunks are invisible to the student as "chunks" — 
   they just experience slightly more rhythmic text */
```

### Chunk Boundary Rules

Chunks are pre-computed in the content pipeline (not client-side). Boundaries follow syntactic structure:

| Priority | Boundary Rule | Example |
|---|---|---|
| 1 | After punctuation (comma, period, semicolon) | "Quyosh chiqdi, / suv bug'landi." |
| 2 | Between subject and predicate | "O'simliklar / oziq tayyorlaydi." |
| 3 | Between verb phrase and object | "Barg / yorug'likni yutadi." |
| 4 | After 5 words (fallback maximum) | "Bu jarayon fotosintez deb / ataladi." |

### Schema Addition

```json
{
  "narrative_segment": {
    "existing_fields": "...",
    "chunks": [
      { "text_uz": "Quyosh chiqdi,", "words": 2 },
      { "text_uz": "suv bug'landi.", "words": 2 },
      { "text_uz": "O'simliklar", "words": 1 },
      { "text_uz": "oziq tayyorlaydi.", "words": 2 }
    ]
  }
}
```

### Grade Behavior

| Grade | Chunking | Gap size |
|---|---|---|
| G3-4 | Aggressive (2-3 words per chunk) | 0.5em |
| G5-6 | Standard (3-5 words per chunk) | 0.4em |
| G7+ | None (standard word spacing) | Normal |

---

## 3. Radiant Journey Map (Deliverable 21, Method #1 extension)

### What It Is

An alternative to the linear chapter list for the "Learning Journey" sidebar. Displays the subject's chapters as a radiant map where the current chapter is the active branch, completed chapters are solid, and future chapters are dimmed.

### Visual Specification

```
                    [Ch 7: Hayvonot]  (dimmed)
                   /
    [Ch 6: Ekologiya] (dimmed)
    /
[Subject Center Icon] ---- [Ch 5: O'simliklar] (ACTIVE — glowing border)
    \
    [Ch 4: Suv sikli] (completed — solid, green check)
    \
     [Ch 3: Tuproq] (completed — solid, green check)
      \
       [Ch 2: Havo] (completed)
        \
         [Ch 1: Tabiat] (completed)
```

### Design Rules

| Element | Specification |
|---|---|
| **Center node** | Subject icon + subject name (e.g., leaf icon + "Tabiiy Fanlar") |
| **Completed chapters** | Solid branch, green checkmark badge, full opacity |
| **Active chapter** | Glowing border (pulsing animation), highlighted branch, full opacity |
| **Future chapters** | Dimmed (40% opacity), dashed branch line |
| **Branch style** | Organic curves (Buzan Law #2), tapering from thick (early) to thin (future) |
| **Tap behavior** | Tap completed chapter → shows chapter Mind Map summary (from Bilim Bazasi). Tap future → "Tez kunda!" (Coming soon!) |
| **Orientation** | Landscape when sidebar is expanded; collapses to linear list on mobile |

### Where It Appears

- **Subject overview screen** (when student selects a subject from their dashboard)
- **Session sidebar** (collapsible, showing current position in the subject journey)
- NOT in-session Phase screens (too much visual overhead during active learning)

### Implementation Priority

**Lower priority than other UI amendments.** This is a navigation enhancement, not a learning mechanic. Can be implemented after all phase-specific UI work is complete.

---

## Summary

| Deliverable | Method(s) | What It Is |
|---|---|---|
| 19: Focus Guide visual | #16, #21, #23 | Animation spec, toggle design, responsive rules |
| 20: Semantic Chunking | #20 | Inter-chunk spacing rule for G5-6 Story Mode |
| 21: Radiant Journey Map | #1 | Alternative chapter navigation as radiant map |


---


# Buzan Injection — Sprint 4: Future Roadmap Items

**Methods Injected:** #3 (Group Mind Mapping), #8 (Secret Symbols), #31 (SEM³)  
**Priority:** Lower — post-MVP or Premium features  
**Sacred Rule:** Content unchanged.

---

## 1. Group Mind Mapping — Post-MVP Brief (Method #3, Deliverable 25)

### Concept

A collaborative radiant mapping mechanic where multiple students contribute branches to a shared map. Requires multiplayer infrastructure (async at minimum).

### MVP Fallback (Single-Player Simulation)

Until multiplayer is available:
1. Student builds a 4-branch Radiant Summary of the lesson (existing mechanic)
2. AI generates a simulated "classmate's map" with 3 overlapping branches and 1 unique branch
3. Student must **merge** the two maps:
   - Identify overlapping concepts (tap to confirm match)
   - Evaluate the classmate's unique branch: "Is this correct? Does it belong?"
   - Add one of their own unique branches that the classmate "missed"

### Full Multiplayer Version (Future)

1. Teacher assigns a topic to the class
2. Each student individually creates a 3-branch map (2 minutes)
3. Maps are pooled and the AI clusters them by concept overlap
4. Each student receives a "partner map" (real classmate, anonymized)
5. Student merges their map with the partner's, producing a richer combined map
6. Class-wide "Master Map" generated from all merged maps — displayed on teacher dashboard

### Dependencies

- Async multiplayer backend (not currently in NETS architecture)
- Student identity anonymization for map sharing
- Teacher dashboard merge visualization

### Recommendation

**Defer to Phase 2 roadmap.** The MVP fallback (AI-simulated classmate) can be built with current Tier 2 infrastructure and provides 80% of the pedagogical value.

---

## 2. Secret Symbols — Personal Symbol Library (Method #8, Deliverable 26)

### Concept

Students create and save personal symbols (icons, stickers, or simple drawings) that they associate with concepts. These symbols persist in their Bilim Bazasi and reappear whenever the concept resurfaces in future sessions.

### How It Works

1. During Phase 5 (Consolidation), after completing a Radiant Summary or Peg System round, the student is offered: "Shu tushuncha uchun o'z belgingizni yarating!" (Create your own symbol for this concept!)
2. Student either:
   - **Selects** from a library of 50+ pre-designed icons (star, fire, lightning, heart, tree, etc.)
   - **Draws** a simple symbol using finger/stylus on a small canvas (Tier 3 vision for interpretation)
3. The symbol is saved to `student_profile.symbol_library[concept_id]`
4. In future sessions:
   - When the concept appears in Memory Sprint, the student's symbol is shown alongside it
   - In Bilim Bazasi, the concept node uses the student's symbol instead of the default icon
   - In Radiant Summary, the student's symbol appears on the branch for that concept

### Implementation Tiers

| Feature | Tier | Cost |
|---|---|---|
| Pre-set icon selection (50+ icons) | Tier 1 | Zero |
| Student-drawn symbol (saved as image) | Tier 1 (just stores the image) | Storage only (~5KB per symbol) |
| AI interpretation of drawn symbol | Tier 3 (vision model) | ~$0.02 per interpretation |
| Symbol appearing in future sessions | Tier 1 (lookup from student profile) | Zero |

### Recommendation

**MVP: Pre-set icon selection only.** Drawing + AI interpretation deferred until Tier 3 vision budget is validated (same dependency as Notebook Capture / Tasviriy Sanat Maker-First).

---

## 3. SEM³ — Memory Matrix Data Model (Method #31, Deliverable 27)

### Concept

An invisible data structure underneath the Bilim Bazasi that tracks not just WHAT a student has learned, but HOW each concept was encoded. This powers smarter session assembly — if a concept was only encoded verbally (Sentence Fill), the assembler can prioritize a visual encoding (Tile Match) next time.

### Matrix Schema

```json
{
  "student_memory_matrix": {
    "student_id": "420d17a7-...",
    "concepts": {
      "UZ-SCI-5-LIFE-03": {
        "label_uz": "Fotosintez",
        "encoding_history": [
          { "date": "2026-04-10", "mechanic": "story_mode", "channels": ["VRB"] },
          { "date": "2026-04-10", "mechanic": "tile_match", "channels": ["VRB", "VIS"] },
          { "date": "2026-04-10", "mechanic": "memory_palace", "channels": ["SPA", "VIS", "VRB"] },
          { "date": "2026-04-11", "mechanic": "peg_system", "channels": ["VIS", "VRB"] },
          { "date": "2026-04-17", "mechanic": "radiant_summary", "channels": ["VIS", "VRB", "SPA"] }
        ],
        "channel_coverage": {
          "VRB": 5,
          "VIS": 4,
          "SPA": 2,
          "AUD": 0,
          "KIN": 0
        },
        "encoding_score": 0.73,
        "weakest_channel": "AUD",
        "recommended_next_mechanic": "link_chain"
      }
    }
  }
}
```

### How the Session Assembler Uses It

```
DURING session_plan.build():
  
  FOR EACH concept scheduled for review:
    matrix = student_memory_matrix.concepts[concept_id]
    
    IF matrix.channel_coverage has any channel at 0:
      PREFER game mechanic that uses that channel
      // e.g., if AUD = 0, prefer a mechanic with audio (Link Chain with TTS)
    
    IF matrix.encoding_score < 0.5:
      DOUBLE the concept's priority in Memory Sprint
      FLAG: "Under-encoded concept: [concept_id] — needs multi-channel reinforcement"
```

### Bilim Bazasi Visualization

The Bilim Bazasi knowledge map can display encoding richness visually:
- **Fully encoded concepts** (4+ channels covered): Bright, fully colored node
- **Partially encoded** (2-3 channels): Semi-bright node
- **Under-encoded** (1 channel): Dim node with a "strengthen" icon

### Dependencies

- Requires encoding channel tags on all game mechanics (already defined in Sprint 1 QG-2: Dual Coding)
- Requires Session Assembler integration (algorithm update)
- Bilim Bazasi UI update for encoding richness visualization

### Recommendation

**Build the data model now (it's just a JSON schema + write-on-play logging).** Defer the Session Assembler integration and Bilim Bazasi visualization to a later sprint. The data collection has zero cost and will be valuable when the integration is built.

---

## Summary

| Deliverable | Method | Priority | Dependency |
|---|---|---|---|
| 25: Group Mind Mapping | #3 | POST-MVP | Multiplayer backend |
| 26: Secret Symbols | #8 | MVP (icons only) | None for pre-set; Tier 3 vision for drawing |
| 27: SEM³ Memory Matrix | #31 | Data model NOW, integration LATER | Encoding channel tags (already in Sprint 1) |


---

