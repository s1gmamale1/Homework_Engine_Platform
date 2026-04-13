# NETS Homework Engine — UI/UX & Animation Design Specification

**Date:** 2026-04-07
**Status:** Design addition (does not modify framework)
**Scope:** Visual design, animation language, and interaction patterns for the full student journey — from loading screen through Pre-Homework, the 7-phase engine, and session completion.
**Applies To:** Implementation teams building the student-facing app. Framework spec ([[NETS-Homework-Engine-UNIFIED]]) remain the authoritative rules; this doc defines *how it looks and feels*.

> See also: [[HOME]] · [[NETS-Homework-Engine-UNIFIED]] · [[NETS-Interactive-Game-Catalog]]

---

## 1. Loading Screens — COD-Style Quote Cards + Did You Know

### 1.1 Purpose

Loading screens are no longer empty waits. They become tiny content moments the student actually enjoys. Three overlapping content types rotate freely — subject-relevance is a *nice-to-have*, not a requirement. The goal is personality, not pedagogy.

| Type | Source | Tone |
|---|---|---|
| **Quote Cards** | Historical figures, scientists, authors, philosophers, athletes, anyone — with citation | Inspirational, "Call of Duty multiplayer loadout screen" |
| **Fun Facts** | Random "wait, really?" facts — science, history, trivia, animal weirdness, space, language | Conversational, curiosity-driven |
| **Corny Lines** | One-liner jokes, dad jokes, LLM-style loading quips (think Qwen / Gemini / Claude loading messages), motivational nonsense, absurdist encouragement | Playful, self-aware, slightly unhinged |

### 1.2 When They Appear

```
┌────────────────────────────────────────────────────────────┐
│  SESSION START                                              │
│     └─ [LOADING SCREEN 1] Quote Card (subject-relevant)    │
│          → Theme Preview opens                              │
│                                                              │
│  PHASE TRANSITIONS (automatic)                               │
│     └─ [LOADING SCREEN] Did You Know (1 per transition)    │
│                                                              │
│  MID-SESSION SURPRISE (~60% session progress)                │
│     └─ [LOADING SCREEN] Quote Card (deliberate injection)   │
│          Student can swipe to dismiss or let it auto-advance│
│                                                              │
│  BOSS INTRO / MYTHICAL BOSS APPEARANCE                       │
│     └─ [LOADING SCREEN] Quote Card — epic tone              │
└────────────────────────────────────────────────────────────┘
```

**Mid-session trigger rule:** Engine picks a random point between 55-65% of predicted session time and inserts a loading screen between phases. This is NOT a pause the student requested — it's a "breath moment" the system grants. Dismissable with a swipe.

### 1.3 Quote Card Layout

```
┌──────────────────────────────────────────────────────┐
│                                                        │
│       ▓▓▓▓▓▓▓  (subtle animated background —           │
│       ▓     ▓   particles, slow gradient shift,         │
│       ▓     ▓   subject-themed: atoms for chemistry,   │
│       ▓     ▓   equations for math, etc.)              │
│                                                        │
│                                                        │
│           "We live in a society exquisitely             │
│            dependent on science and technology,         │
│            in which hardly anyone knows anything        │
│            about science and technology."              │
│                                                        │
│                         — Carl Sagan                    │
│                   The Demon-Haunted World, 1995         │
│                                                        │
│                                                        │
│     ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░░░░░░░░  [loading bar]        │
│                                                        │
│              swipe to skip  →                          │
└──────────────────────────────────────────────────────┘
```

**Visual notes:**
- Dark cinematic background (like COD loadout screen) — not pure black, deep navy / charcoal with subject-colored highlights
- Quote text fades in word-by-word (typing-feel, ~30ms per word)
- Citation (author + source + year) fades in after quote completes, 400ms delay
- Loading bar at bottom fills over actual load time — if load finishes early, bar snaps to full and pauses ~1.2s so student can finish reading
- Swipe-to-skip gesture: right-swipe dismisses; left-swipe requests *next* quote (student can rotate through 2-3 before the system advances)

### 1.4 Did You Know Card Layout

```
┌──────────────────────────────────────────────────────┐
│                                                        │
│              💡  DID YOU KNOW?                          │
│                                                        │
│                                                        │
│     The word "oxygen" comes from Greek words            │
│     meaning "acid producer" — because scientists        │
│     originally thought ALL acids contained oxygen.      │
│     They were wrong.                                    │
│                                                        │
│                                                        │
│     ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬░░░░░░░░░                        │
└──────────────────────────────────────────────────────┘
```

**Visual notes:**
- Lighter background than Quote Cards — "daytime" vs COD's "cinematic night"
- Icon pulses softly (subtle scale 0.95 → 1.05 over 1.5s)
- Text types in character-by-character (~18ms per character, faster than quote cards)
- No author/citation — this is knowledge, not attribution
- Auto-advances, no swipe required (shorter average read time)

### 1.5 Content Sourcing Rules

Subject-relevance is **optional**. Rotate freely across all three content types. The point is vibe and variety, not structured pedagogy — the framework already covers pedagogy elsewhere.

| Rule | Detail |
|---|---|
| **Relevance optional** | Content may or may not relate to the current subject. It's fine either way. Mixing irrelevant fun facts with on-topic quotes keeps the rotation fresh. |
| **Citation mandatory for Quote Cards only** | Real quotes need author + source (book/paper/speech) + year. No "Anonymous" quotes. No fabricated quotes attributed to real people. Fun Facts and Corny Lines do NOT need citations. |
| **Historical diversity in Quote pool** | Scientists, authors, artists, philosophers, athletes, musicians across cultures. Include Uzbek / Central Asian / Islamic Golden Age figures (Al-Khwarizmi, Al-Biruni, Ibn Sina, Ulugh Beg) alongside Western and global voices. |
| **Length** | Quote Cards: 1-3 sentences. Fun Facts: 1-2 sentences. Corny Lines: 1 short sentence ideally. |
| **Quality bar for Corny Lines** | Must be actually charming or funny — not mean, not edgy, not punching down. "Loading your homework... and your destiny" good. Sarcasm about the student's intelligence bad. Think Qwen/Gemini/Claude's goofy loading quips or old LoadingReady Run tip cards. |
| **Fun Fact verification** | Fun Facts must be true. "Octopuses have three hearts" good. Made-up trivia bad. |

### 1.6 Content Examples

**Quote Cards:**
- *"We live in a society exquisitely dependent on science and technology, in which hardly anyone knows anything about science and technology."* — Carl Sagan, *The Demon-Haunted World*, 1995
- *"The ink of the scholar is more sacred than the blood of the martyr."* — attributed to Muhammad, hadith tradition
- *"I have not failed. I've just found 10,000 ways that won't work."* — Thomas Edison
- *"Mathematics is the language in which God has written the universe."* — Galileo Galilei, *Il Saggiatore*, 1623

**Fun Facts:**
- Did you know? Octopuses have three hearts, nine brains, and blue blood.
- Did you know? Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that's still edible.
- Did you know? The Eiffel Tower gets about 15 cm taller in summer because the iron expands in the heat.
- Did you know? Bananas are technically berries, but strawberries aren't.

**Corny Lines (Qwen/LLM-style loading quips):**
- Loading your homework... and your destiny.
- Teaching electrons to behave. Please wait.
- Convincing the pixels to line up...
- Reticulating splines. (If you get this joke, you're old.)
- Doing math so you don't have to. Oh wait.
- Warming up the neural networks with a cup of chai.
- Counting to infinity. Twice. Almost done.
- Ctrl+Z on your excuses. Loading homework.
- Polishing your knowledge crown.
- Waking up the historians. They hit snooze.
- Turns out "hard work" was under the C: drive the whole time.
- Your brain called. It's excited.

---

## 2. Theme Preview — Panel-Based Book Layout

### 2.1 Core Interaction Model

Theme Preview is **NOT a scroll**. It's a **panel deck** — one panel per section, swipeable left/right like a physical book with a whoosh transition.

```
 ◄────────── SWIPE LEFT/RIGHT ──────────►

   ┌─────┐   ┌─────┐   ┌─────┐
   │     │   │     │   │     │
   │ 2/8 │   │ 3/8 │   │ 4/8 │
   │     │ → │     │ ← │     │
   │     │   │     │   │     │
   └─────┘   └─────┘   └─────┘

           [current]
```

Only the current panel is visible. Neighboring panels are queued but not shown until swipe.

### 2.2 Panel Content Mapping

One panel per §4.4 component — 8 panels total:

| Panel | Content |
|---|---|
| 1 | **Summary of Book Content** |
| 2 | **Better Explanation** |
| 3 | **Examples** |
| 4 | **Real-Life Research** (origin story) |
| 5 | **Personal Hook** |
| 6 | **Why This Matters** |
| 7 | **Industry Application** |
| 8 | **Additional Materials** (links deck) |

### 2.3 Panel Layout

```
┌──────────────────────────────────────────────────┐
│  ◄                    2 / 8                   ►  │   ← pagination dots
│                                                    │
│     ▓▓▓▓▓▓  section icon                           │
│                                                    │
│     BETTER EXPLANATION                             │
│     ─────────────────                              │
│                                                    │
│     [Hero visual — diagram, photo, or              │
│      short video clip autoplaying silently]        │
│                                                    │
│                                                    │
│     When the book says "oxygen is chemically       │
│     active," it means oxygen is the element        │
│     that wants to bond with almost everything.     │
│     Think of it as the social butterfly of         │
│     the periodic table.                            │
│                                                    │
│                                                    │
│  ● ○ ○ ○ ○ ○ ○ ○                                  │   ← progress dots
│                                                    │
│              swipe  ◄  ►  to continue              │
└──────────────────────────────────────────────────┘
```

### 2.4 Transition Animation: "Whoosh + Letter Assembly"

Every swipe triggers a two-stage animation:

**Stage 1 — WHOOSH (400ms)**
- Current panel slides out in the swipe direction
- Motion blur on the outgoing panel (CSS `filter: blur(4px)` ramping from 0 → 4 → 0)
- Subtle "whoosh" sound effect (can be muted)
- Parallax: background image shifts at 60% of panel speed (creates depth)

**Stage 2 — LETTER ASSEMBLY (600ms, overlaps with stage 1 by 150ms)**
- New panel's hero visual fades in at 40% opacity, scales up from 0.95 → 1.0
- New panel's heading (e.g., "BETTER EXPLANATION") assembles letter-by-letter:
  - Letters appear in **random positions** scattered around final location
  - Each letter flies toward its final slot on a bezier curve, ~30ms stagger between letters
  - Letters arrive with a tiny overshoot (spring damping) → settle
- Body text fades in as a block, 200ms after heading completes
- Icon rotates/scales in separately (independent timing, ~800ms total)

**Sound:** Soft paper-rustle on whoosh, subtle typing-click bursts on letter assembly. All muteable.

**Reverse swipe:** Same animation plays in reverse — letters disassemble into random positions and fly off, new (previous) panel whooshes in.

### 2.5 Controls and Behaviors

| Gesture / Control | Behavior |
|---|---|
| **Swipe left** | Next panel |
| **Swipe right** | Previous panel |
| **Tap left edge** | Previous panel (accessibility) |
| **Tap right edge** | Next panel |
| **Pagination dots (top)** | Tap any dot → jump directly to that panel (skip animation, hard cut) |
| **Progress dots (bottom)** | Visual indicator only, not tappable |
| **Pinch-zoom on hero visual** | Opens lightbox (photo/diagram viewer) — does NOT advance panel |
| **Double-tap body text** | Reveals "highlight mode" — student can mark text to revisit later (saved to their Flash Cards deck with 📌 marker) |
| **Long-press panel** | Shows panel menu: "Translate" / "Read aloud" / "Save note" |

### 2.6 Exit Behavior

- Reaching Panel 8 + swiping left (forward) → transitions into Flash Cards session (0-B)
- Transition is NOT a whoosh — it's a **page-flip** animation: the whole panel deck rotates forward along its left edge (180° Y-axis rotation, 700ms) revealing the Flash Cards carousel behind it
- From Panel 8, student can also tap explicit **"To Flash Cards →"** button if they don't want to swipe

---

## 3. Flash Cards — 3D Circular Carousel

### 3.1 Spatial Model

Flash Cards are arranged on an **invisible horizontal circle** (carousel rotating around a vertical axis). Only 3 cards are visible at any time:

```
                            [center, facing student]
                            ┌────────┐
                            │        │
                            │ FRONT  │  ← 1.0× scale, sharp, fully opaque
                            │        │
                            └────────┘
             ↖                                  ↗
    ┌────┐                                          ┌────┐
    │    │                                          │    │
    │ ←  │  ← 0.7× scale, blurred, 60% opacity      │ →  │
    │    │     (previous card)                       │    │
    └────┘                                          └────┘
                     (next card)
```

All other cards in the deck exist on the carousel but are hidden behind the visible three until the student rotates the carousel.

### 3.2 Rotation Animation

**Swipe left** (advance) → carousel rotates counterclockwise:
- Center card shrinks and slides left (1.0× → 0.7× scale, 0 → -120px X, 100% → 60% opacity, 0 → 4px blur)
- Right card grows and slides to center (0.7× → 1.0× scale, +120px → 0 X, 60% → 100% opacity, 4 → 0 blur)
- Hidden next-next card appears on the right at 0.7×
- Cubic-bezier `(0.25, 0.46, 0.45, 0.94)` — "ease-out" feel, 500ms duration
- All three cards move simultaneously, synchronized

**Swipe right** (go back) → same animation mirrored.

The **circle** nature means swiping past the last card loops to the first. A subtle "ding" sound + a brief pulsing ring around the counter indicates the loop.

### 3.3 Card Layout (Front)

```
┌────────────────────────────────┐
│                                  │
│   ⚡ FORMULA                      │   ← card type tag (color-coded)
│                                  │
│                                  │
│          E = mc²                  │   ← the term / formula / concept
│                                  │
│                                  │
│      tap to flip  ↺              │   ← hint text, fades after 2s
│                                  │
│                                  │
│       3 / 24                      │   ← card position in deck
└────────────────────────────────┘
```

### 3.4 Card Layout (Back)

```
┌────────────────────────────────┐
│                                  │
│   ⚡ FORMULA                      │
│                                  │
│   Energy equals mass times        │
│   the speed of light squared.     │
│                                  │
│   • E = energy (joules)           │
│   • m = mass (kg)                 │
│   • c = speed of light (3×10⁸ m/s)│
│                                  │
│   Einstein, 1905.                 │
│                                  │
│      tap to flip back  ↺          │
└────────────────────────────────┘
```

### 3.5 Flip Animation

- **Trigger:** Tap anywhere on the center card (only center is tappable)
- **Animation:** Card rotates 180° around its vertical Y-axis
- **Timing:** 500ms, easing `cubic-bezier(0.4, 0.0, 0.2, 1)` (material design "standard")
- **Midpoint effect:** at 90° (card edge-on to viewer), a subtle light-glint sweeps across the card edge
- **Back-face culling:** front hidden during second half, back hidden during first half (CSS `backface-visibility: hidden`)
- **3D realism:** `perspective: 1000px` on parent, card tilts slightly based on device gyroscope (mobile only, ±5° max)
- **Tap again:** flips back using the same animation (continues rotation to 360°, does not reverse)

### 3.6 Card Type Color Coding

| Type | Tag Color | Icon |
|---|---|---|
| **Formula** | Electric blue | ⚡ |
| **Concept** | Warm amber | 💡 |
| **Rule** | Deep red | ⚠ |
| **Definition** | Forest green | 📖 |

### 3.7 In-Session Quick Access (During Homework)

Within the 7-phase homework, the Flash Cards deck is accessible via a **persistent floating button** in the bottom-right corner:

```
                                              ┌───┐
                                              │ ⚡│  ← Flash Cards button
                                              │ 24│  ← deck count
                                              └───┘
```

- Tap → Flash Cards carousel slides up from the bottom as a bottom-sheet (40% screen height) overlaying the current homework phase
- The underlying homework pauses while the sheet is open (any running timer freezes)
- Student can browse without penalty (not counted as a hint)
- Tap outside or swipe down → sheet dismisses, homework resumes
- Button pulses subtly if student has been stuck on a question > 30 seconds (hint: "maybe check your Flash Cards?")

---

## 4. Homework Engine Animations — Per-Phase UI/UX

This section defines the visual / motion language for each of the 7 phases. Consistent across all subjects.

### 4.1 Phase Transition (Global)

Between every phase: a full-screen **phase card** appears for 1.5 seconds.

```
┌──────────────────────────────────────┐
│                                        │
│          ░░░░░░░░░░░                   │  ← progress ring (filled per phase)
│          ░         ░                   │
│          ░    P3   ░                   │  ← phase number
│          ░         ░                   │
│          ░░░░░░░░░░░                   │
│                                        │
│        GAME BREAKS                     │  ← phase name
│        Active Practice                 │  ← tagline
│                                        │
│      ─── 6-9 minutes ───               │  ← expected duration
│                                        │
└──────────────────────────────────────┘
```

**Motion:**
- Ring fills from 0% → 100% for previous phase as card enters (500ms)
- New phase number counts up (P1 → P2 → P3, not snap) via morph animation
- Phase name types in letter-by-letter (matches Theme Preview style for consistency)
- Card slides away upward after 1.5s (total screen time), revealing the phase UI below

### 4.2 Memory Sprint (Phase 1) — Pulse & Streak

- **Timer bar** at top of screen pulses red when < 30s remaining
- **Correct answer:** card flashes green, +XP pops out of the answer area and flies to the top-right XP counter
- **Streak indicator** (fire icon): grows with each consecutive correct answer. At 3+ streak: screen edges emit subtle heat haze. At 5+: full screen vignette flashes orange briefly.
- **Wrong answer:** card shakes left-right 3× (80ms each), background flashes red once, no penalty animation (this is warm-up)

### 4.3 Story Mode (Phase 2) — Cinematic Text + Parallax

- **Background:** full-bleed hero image for each story segment (problem / struggle / discovery / solution beats)
- **Text delivery:** narration appears in a lower-third text box that slides up from bottom, text types in at reading speed (~180 WPM)
- **Parallax scroll:** as the student reads, the background gently drifts (subtle Ken Burns effect, 1.02× slow zoom over 90s)
- **Checkpoint transition:** background desaturates to 50%, a question card slides up from bottom with a soft pop
- **Correct checkpoint:** card dismisses upward, background re-saturates, next beat fades in
- **Wrong checkpoint:** card shakes, textbook page reference pulses in the top-right ("📖 Darslik: sahifa 52") — pulsing animation draws the eye

### 4.4 Game Breaks (Phase 3) — Per-Game UI

Each mini-game has its own visual language. Common elements:

- **Game intro card** (800ms): game name + icon + brief rule reminder, then slides away
- **Score HUD** in top bar: current game score, best score, XP earned this game
- **Combo meter** on the right edge: vertical bar that fills with each correct answer, empties on wrong
- **End-of-game summary:** confetti burst (magnitude proportional to score), star rating (1-3), XP breakdown animation (each XP category flies in one at a time)

**Tic Tac Toe vs AI specific:**
- 3×3 board center-screen, cells glow softly when hoverable
- Student taps a cell → cell highlights in blue → AI question modal slides in from the right
- On correct: X **burns into** the cell with a quick flame effect (200ms)
- On wrong: X **glitches** to a random cell with distortion shader (400ms)
- AI's turn: O **etches** into its chosen cell with a digital circuit trace animation (350ms)
- Win: winning line draws across the board in gold, board explodes into particles

**Mystery Box specific:**
- Appears as a floating 3D box center-screen, slowly rotating
- Ambient glow in a random color (hints at rarity but doesn't spoil)
- Student taps → box pauses → question modal appears
- On answer: box CRACKS open in half (top half flies upward), contents shoot out like a CS:GO case-opening:
  - XP number flies out first
  - Then the reward item (if earned) with a flash burst
  - Rarity indicated by item glow: white (common) → blue → purple → gold → red (Mythical Boss Ticket)

### 4.5 Real-Life Challenge (Phase 4) — Newsroom / Case File Aesthetic

- **Scenario introduction:** slides in as a "case file" document — manila folder opens, papers inside flutter, revealing the scenario text
- **Student's role badge** prominent at top: "YOU ARE: [Role]" with a role-specific icon (badge for inspector, stethoscope for doctor, etc.)
- **Evidence sections** can be tapped to expand (accordion animation)
- **Answer submission:** student's typed response appears in a "report" panel with a typewriter effect as they type
- **AI evaluation:** "ANALYZING RESPONSE..." indicator (spinning dots) for up to 3 seconds, then score reveals with a "VERDICT" stamp animation (rubber-stamp hitting the page)

### 4.6 Consolidation (Phase 5) — Memory Palace Visual

- **Memory Palace interior:** 3D-ish isometric room with shelves, doors, objects
- Each concept is a glowing object placed in the room
- Student taps objects to review; objects pulse when tapped
- **Walk-through animation:** camera slowly pans across the room, stopping briefly at each concept
- Color palette: warm, soft, low-stimulation (this is the "breath" phase before boss)

### 4.7 Boss Fight (Phase 6) — Epic Cinematic

**Sub Boss:**
- Boss appears as a stylized illustrated character or abstract entity (subject-themed)
- HP bar prominent at top (full-width, red → orange → green based on remaining HP)
- Student's answers manifest as "attacks" that fly toward the boss
- Correct = boss recoils, HP decreases with a damage number pop-up ("-20")
- Combo 3+ = student's attack glows gold and deals 2× damage with an enhanced visual
- Hint tax = boss HEALS (HP bar fills slightly, green sparkles rise from boss) — visually reinforces the cost
- Victory = boss shatters into particles, starburst overlay, star rating animation (stars fly in from offscreen and slam into position)

**Big Boss:**
- Same as Sub Boss but boss is **larger** (1.5×), has a different color palette (purple/gold), and the background is more dramatic (storm clouds, darker)
- Intro card: "⚔ BIG BOSS — [Weekly Challenge]" with thunder sound

**Mythical Boss:**
- Full cinematic cutscene intro (2-3 seconds):
  - Screen shakes
  - Dark vignette closes in
  - Red alert border flashes
  - Text materializes: **"⚠ A MYTHICAL BOSS HAS APPEARED ⚠"** with subject-appropriate mythological styling
- Boss is massive (2.5× normal), glowing, with particle effects around it
- Background: completely different — star field, abyss, or subject-specific legendary setting
- Music shifts to an epic orchestral track (if enabled)
- No hint button visible (it's disabled at all — enforce visually)
- Victory animation is extreme: slow-motion explosion, camera zoom, screen flash, title card "MYTHICAL BOSS DEFEATED" with the student's exclusive title unveiling

### 4.7.B Notebook Capture — Camera & Upload UX *(NEW 2026-04-07)*

When a Notebook Capture task appears (Framework §6.8), the screen transforms into an offline-friendly task card that walks the student through paper work + photo upload.

**Stage 1 — Task Card**

```
┌────────────────────────────────────────────┐
│                                              │
│    📓  NOTEBOOK TASK                          │
│    ──────────────                             │
│                                              │
│    Sketch the free-body diagram for          │
│    a block sliding down a 30° ramp.          │
│    Label all forces. Show the net            │
│    force vector.                             │
│                                              │
│    💡 Tip: take your time. The session       │
│    is paused — no timer pressure.            │
│                                              │
│                                              │
│    ┌────────────────────────────┐            │
│    │   📷  I'M DONE — UPLOAD     │            │
│    └────────────────────────────┘            │
│                                              │
│         Need help? Tap a hint  ▼             │
└────────────────────────────────────────────┘
```

- Background dims slightly to communicate "session paused"
- Soft background animation: a notebook icon flips through pages slowly (subliminal "go offline" cue)
- The session timer is FROZEN — visible at the top with a small ❄ icon to communicate the pause

**Stage 2 — Camera Capture**

When the student taps UPLOAD, the camera opens directly (with permission already granted at app onboarding):

```
┌────────────────────────────────────────────┐
│  ◀ Back                              [⚡]    │   ← back + flashlight toggle
│                                              │
│    ┌──────────────────────────────────┐     │
│    │                                    │     │
│    │     ╱─────────────────╲             │     │
│    │    ╱                   ╲            │     │
│    │   ╱   live camera view  ╲           │     │   ← page-edge detection
│    │  ╱     with detected     ╲          │     │     overlay (pulsing
│    │ │       page outline       │        │     │     green rectangle when
│    │  ╲                         ╱        │     │     a page is found)
│    │   ╲                       ╱         │     │
│    │    ╲                     ╱          │     │
│    │     ╲___________________╱           │     │
│    │                                      │     │
│    └──────────────────────────────────┘     │
│                                              │
│    ✓ Page detected · ✓ In focus · ✓ Lit     │   ← real-time validation
│                                              │
│           ┌──────┐                           │
│           │  ◯   │   ← shutter button        │
│           └──────┘                           │
│                                              │
│    📁 Pick from gallery instead              │
└────────────────────────────────────────────┘
```

**Real-time validation indicators** (small badges above the shutter):
- ✓ Page detected — turns green when edge detection finds a rectangular bound
- ✓ In focus — turns green when Laplacian variance > 100
- ✓ Lit — turns green when mean brightness is 60-200/255
- All three must be green for the shutter to enable. If any is red, a small tip appears: *"Move closer"*, *"Hold steady"*, *"Find brighter light"*.

**Stage 3 — Confirmation Preview**

After capture, the student sees their photo with auto-cropping applied to the detected page:

```
┌────────────────────────────────────────────┐
│                                              │
│    Looks good?                               │
│                                              │
│    ┌──────────────────────────────────┐     │
│    │                                    │     │
│    │    [auto-cropped page preview]    │     │
│    │                                    │     │
│    │    (any detected faces or          │     │
│    │     personal info shown            │     │
│    │     blurred with a small 🔒       │     │
│    │     icon overlay)                  │     │
│    │                                    │     │
│    └──────────────────────────────────┘     │
│                                              │
│    📑 + Add another page (1/3)               │
│                                              │
│    ┌──────────┐    ┌──────────────────┐     │
│    │  RETAKE  │    │  SEND FOR REVIEW │     │
│    └──────────┘    └──────────────────┘     │
└────────────────────────────────────────────┘
```

- Multi-page support: student can add up to 3 photos for one task (e.g., a 2-page proof). They are stitched server-side and evaluated as one submission.
- Privacy: any faces detected by client-side ML get auto-blurred with a small 🔒 lock icon shown in the corner. The student can tap the lock to reveal what was blurred and why.

**Stage 4 — AI Vision Evaluation Loading**

```
┌────────────────────────────────────────────┐
│                                              │
│    🔍  Reading your work...                  │
│                                              │
│         ╱╲                                   │
│        ╱  ╲    (animated magnifying          │
│       ╱    ╲    glass scanning the           │
│      ╱______╲   notebook icon)               │
│        ││                                    │
│        ╱╲                                    │
│                                              │
│    "Did you know? Leonardo da Vinci          │
│     wrote his notebooks in mirror            │
│     writing — possibly to make them          │
│     harder for others to read."              │
│                                              │
│    ▬▬▬▬▬▬▬▬▬▬░░░░░░░░░░  3-8 sec            │
└────────────────────────────────────────────┘
```

A "Did You Know" card appears during the wait so the loading screen has personality (consistent with §1).

**Stage 5 — Feedback Reveal**

```
┌────────────────────────────────────────────┐
│                                              │
│    ✓  85% — Strong work!                    │
│                                              │
│    ┌──────────────────────────────────┐     │
│    │   [student's photo, with AI       │     │
│    │    annotations overlaid:           │     │
│    │                                    │     │
│    │    ✓ green check on gravity        │     │
│    │      vector (correct direction)    │     │
│    │                                    │     │
│    │    ✓ green check on normal force   │     │
│    │      (correct angle)               │     │
│    │                                    │     │
│    │    ⚠ red circle on friction        │     │
│    │      vector (wrong direction)]     │     │
│    │                                    │     │
│    └──────────────────────────────────┘     │
│                                              │
│    Your free-body diagram correctly          │
│    shows gravity and normal force, but       │
│    the friction vector is pointing the       │
│    wrong way. Friction opposes motion —      │
│    re-check the direction.                   │
│                                              │
│    ┌──────────┐    ┌──────────────────┐     │
│    │ TRY AGAIN│    │  ACCEPT & MOVE ON│     │
│    └──────────┘    └──────────────────┘     │
└────────────────────────────────────────────┘
```

- AI annotations overlay the photo in real time — green checks for correct elements, red circles for problem areas, with subtle pulsing animation to draw attention
- Specific written feedback below the photo, never reveals the exact answer
- TRY AGAIN button is offered if score < 60% (sends back to Stage 1 with the same prompt)
- ACCEPT moves on, adds XP based on the score, and continues the homework session (timer unfreezes)

**Sound design:**
- Capture shutter: classic camera click
- Validation tick (each ✓ turning green): soft ping
- AI evaluation start: gentle whoosh
- Score reveal: subtle chime if ≥60%, neutral tone if <60% (NEVER a sad/failure sound — coaching framing per Framework §6.6)

**Reduced motion mode:** static feedback (no pulsing annotations, no whoosh) — green/red coloring still applied for clarity.

### 4.8 Reflection (Phase 7) — Quiet Journal

- Minimal UI — background fades to a soft cream/paper texture
- Reflection prompt appears centered in a handwritten-style font
- Student's input field looks like a journal page
- Low ambient sound (soft pen-scratching on paper as student types)
- "Save reflection" button appears once minimum character count is met, glows gently

---

## 5. Session Completion — Score Tier Celebrations

From Framework §6.6, each score tier gets a distinct celebration animation:

### 5.1 100% — Perfect

- Full-screen white flash (200ms)
- Confetti cannon from both bottom corners (1000+ particles)
- Student's avatar pops up center-screen with a crown descending onto it
- "PERFECT!" text in giant gold letters, letter-by-letter assembly with a sparkle per letter
- Fireworks in background
- Title card: "YOU EARNED: Perfectionist (temporary title)"
- Sound: triumphant orchestral sting

### 5.2 99% — Almost Perfect (Tease)

- Similar to 100% but SCALED DOWN 80%
- "ALMOST PERFECT!" text
- A cheeky overlay: "So close! One more point!" with a winking avatar
- Sound: triumphant but with a playful "dip" at the end

### 5.3 90-98% — Excellent

- Green glow across screen edges
- Fire streak animation across the student's streak icon
- "EXCELLENT!" text, medium size
- XP counter ticks up with a satisfying rapid count
- Sound: strong positive chime

### 5.4 80-89% — Very Good

- Warm amber glow
- "VERY GOOD!" text
- First-time-80% bonus XP pops separately with "+BONUS!" tag
- Sound: positive chime, softer than Excellent

### 5.5 60-79% — Passing + Repass Offer

- Neutral blue background
- "PASSED" text (medium, no exclamation)
- XP counter ticks up normally
- Modal slides up: "You passed! Want to try again for a better score?" with **Try Again** / **Finish** buttons
- Sound: gentle confirmation chime

### 5.6 Below 60% — Duolingo Mode Entry

- NO failure animation — critically, avoid any "you failed" framing
- Screen fades to a soft coaching color (teal)
- Avatar appears with a encouraging gesture
- Text: "Let's work on the tricky parts together."
- "Continue to practice" button (not "retry failed")
- Sound: calm, encouraging tone (NOT a sad/negative sound)

---

## 6. Universal Motion Principles

Applied across every animation in NETS:

| Principle | Rule |
|---|---|
| **Duration ceiling** | No single animation exceeds 800ms. Exception: boss intros (up to 3s) and panel transitions (up to 700ms). |
| **Easing default** | `cubic-bezier(0.4, 0.0, 0.2, 1)` (material standard) unless explicitly different |
| **Stagger** | When multiple elements animate together, stagger by 50-80ms for a "cascading" feel |
| **60 FPS target** | Never animate properties that trigger layout reflow (width/height/top/left). Always use transform + opacity. |
| **Reduced motion** | Respect `prefers-reduced-motion` — swap complex animations for simple fades under 200ms. Never block users. |
| **Sound optional** | All sound effects are muteable via a persistent toggle. Audio defaults OFF on first launch; student opts in. |
| **Haptics** | On mobile, tap gestures get subtle haptic tick; correct answers get a gentle pulse; wrong answers get a short double-tick |
| **Accessibility** | Every animated UI element must have a static alt-state and screen-reader label. Animations are decoration, not required for function. |

---

## 7. Color System (Subject-Themed)

Each subject has a primary color that appears in Theme Preview backgrounds, phase cards, and boss glows:

| Subject | Primary | Accent |
|---|---|---|
| **Mathematics** | #3B82F6 (blue) | #FBBF24 (gold) |
| **Physics / Science** | #8B5CF6 (purple) | #10B981 (emerald) |
| **Chemistry (Kimyo)** | #EF4444 (crimson) | #F59E0B (amber) |
| **Biology (Biologiya)** | #10B981 (emerald) | #84CC16 (lime) |
| **History / Tarix** | #92400E (bronze) | #FCD34D (pale gold) |
| **Literature / Adabiyot** | #7C2D12 (burgundy) | #FDE68A (cream) |
| **English / Russian / Uzbek** | #0EA5E9 (sky) | #F472B6 (rose) |

Backgrounds use dark-mode variants by default (primary at 15% on near-black), accents used for highlights, CTAs, and reward moments.

---

## 8. Implementation Notes for Designers

- **Prototype tool:** Figma with the Figma Motion plugin, or Framer for higher-fidelity interaction prototypes
- **Export format:** Lottie JSON for complex animations (letter assembly, boss shatter, confetti). Native CSS/JS for simple transitions
- **Asset size budget:** no single Lottie file > 200KB, no image hero > 800KB (compress with WebP + AVIF fallback)
- **Test matrix:** iPhone SE (small screen), Galaxy A-series (mid Android), iPad (tablet), low-end school laptop (Chromebook). If any of these drops below 30 FPS, the animation is over-budget.
- **Reference vibes:**
  - Loading screens → Call of Duty multiplayer (loadout screen with tips)
  - Panel transitions → iOS Weather app full-screen swipes
  - Flash card carousel → Apple Cover Flow (deprecated but visually iconic)
  - Boss fights → Pokémon Stadium / Undertale (stylized, not photorealistic)
  - Mystery Box → CS:GO case opening
  - Case file (Real-Life Challenge) → Return of the Obra Dinn / Papers, Please

---

**End of Design Spec.** Pairs with `NETS-Homework-Engine-UNIFIED.md` (rules) and `NETS-Homework-Engine-Blueprint.docx` (session flow).
