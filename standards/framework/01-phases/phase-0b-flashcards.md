---
name: Phase 0-B — Flash Cards
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §4.5 (lines 589-625) + §22 session
---

# Phase 0-B — Flash Cards

## Purpose (WHAT)

Atomic recall reference deck that surfaces every formula, concept, rule, and definition the student will need during the homework — NOT a practice set. If an item asks the student to DO something, it does not belong here.

## Structure (HOW)

**Card count:** 2–12 cards per session.

**Cluster grouping (§22 addition):** Cards are organized into 4 clusters of approximately 3 cards each, following Buzan mind-map branch structure. Each cluster is a named group rendered as a tab or section divider:

| Cluster | Contents |
|---------|----------|
| **Names** | Key terms, vocabulary, terminology, classifications |
| **Formulas** | Equations, rules, procedures, algorithms |
| **Decisions** | Conditions, exceptions, boundaries, when-to-use rules |
| **Insights** | "Why it works" explanations, historical context hooks |

Clusters are presented in the order above. Within a cluster, card order follows Buzan's "most central concept first" — the most essential item in a cluster leads.

**Card anatomy:** Each card has exactly two faces:
- **Front (trigger):** The term, formula symbol, or rule name. Max 10 words. No context.
- **Back (definition + memory hook):** The full definition or formula + a 1-line Buzan mnemonic aid. The memory hook uses one of: acronym, vivid image, rhyme, story fragment, or association chain. Example back: *"Valence = number of bonds an atom can form. Hook: VALE — Valence Allows Linking Elements."*

**Visual on card back (optional):** For spatial/geometric concepts, the card back may include a small SVG diagram alongside the definition. Example: a flash card for "parabola" shows the definition text + a small 200×150 SVG of a U-shaped curve with labeled vertex and axis. Full visual spec in `00-core/visual-generation.md`. Max 0-2 visual cards per deck — most cards are text-only.

**Buzan memory hook rules:**
- Every card back must include exactly 1 memory hook line, prefixed with "Hook:".
- Hook must be memorable, concrete, and concise (≤15 words).
- Hooks use the student's language (Uzbek for UZ content, Russian for RU content).
- Hooks do not introduce new facts — they are mnemonic bridges only.

**What cards must contain:**

| Category | Description |
|----------|-------------|
| **All Key Formulas** | Every formula, equation, or rule the student will encounter in the homework. One per card. |
| **All Key Concepts** | Definitions, terminology, classifications. Example: "What is an oxide?" / "What does valence mean?" |
| **All Key Rules** | Conditions, exceptions, boundaries. Example: "Combustion requires 3 things: fuel, oxygen, heat. If any one is missing, fire stops." |

**What cards must NOT contain (exclusion list — hard rules):**
- NO practice problems or exercises
- NO worked examples (those belong in Phase 0-A Panel 3)
- NO mini-quizzes or checkpoint-style questions
- NO "try this" or "solve this" prompts
- NO scenario-based content
- NO hints or strategies (those belong in Story Mode, Phase 2)
- NO explanatory paragraphs — card back = definition + hook only

Each card = one formula, one concept, one rule, or one term. Nothing else. *(Buzan: "One Word Per Branch" applied to cards — max one chunk per card face.)*

**Returnable during homework:** A "Flash Cards" button remains accessible throughout all 7 phases of the homework session as a quick-access overlay. This is NOT a hint (no XP penalty), purely a reference tool. The overlay is dismissible at any time and returns the student to their current position in the session.

**Gateway:** Phase 0-B ends with the "Start my Homework" button — the explicit gateway into the 7-phase engine. Only after this button is pressed does the session timer start and XP accrual begin.

**Pronoun policy:** All student-facing Uzbek content uses "Siz" (formal). Never "sen". Russian: "Вы", never "ты".

## Cognitive load

- **Bloom range:** L1 (Remember) → L2 (Understand). Reference mode only — no application.
- **PISA range:** Not assessed. Reference is pure recall support, not an evaluation.
- **Scoring:** None. No XP, no HP, no penalties.
- **Time budget:** 1–2 minutes initial pass (student-paced). Re-access throughout session is on-demand with no time cost.
- **AI Tier:** Tier 1 (pre-generated cards from textbook + standards).

## Inputs

- Textbook chapter content — all key formulas, terms, and rules extracted
- Phase 0-A completion flag (0-B does not render until 0-A is complete)
- Schema activation keywords from Phase 0-A Panel 5 (used for card relevance weighting — cards matching activated schemas are surfaced first within their cluster)
- Subject family tag (influences cluster emphasis — e.g., Aniq Fanlar emphasizes Formulas cluster)
- Grade band (influences memory hook complexity)

## Outputs

Phase 0-B produces no scored data. It produces:

- **Phase 0-B completion flag** → required before the 7-phase engine unlocks
- **Cards seen set** → list of card IDs the student viewed on initial pass, logged to session record
- **Cards skipped set** → cards swiped past in < 2 seconds, flagged for potential re-surface in Phase 7 Reflection
- **Flash card deck** → persisted in session state and available to the returnable overlay throughout Phases 1–7

## Adaptable parameters

| Parameter | Default | Override per family | Override per archetype |
|-----------|---------|---------------------|------------------------|
| Card count | 6–8 | Aniq Fanlar: up to 12 (formula-dense chapters) | Review/Spiral: 4–6 (student already knows most) |
| Cluster emphasis | Balanced across 4 clusters | Aniq Fanlar: Formulas + Decisions lead | Til Fanlar: Names + Insights lead |
| Memory hook language | Match content language | — | — |
| Hook style | Any of 5 types | — | Younger grades (G3–5): vivid image hooks preferred |
| Cards seen threshold (fast-flip flag) | < 2 seconds per card = flagged | — | — |

## Subject-specific examples

**Aniq Fanlar (Math/Geometry/Algebra):**
- Formulas cluster dominates: each formula gets its own card. Example front: *"Aylana yuzasi"*. Back: *"S = πr² — Hook: S-aylana, r-radius. 'Pie are squared' (π·r²)."*
- Decisions cluster: when to use which formula variant (e.g., area vs circumference, when to factor vs use quadratic formula).
- Names cluster: geometric terms with precise definitions.

**Til Fanlar (English/Ona Tili/Rus Tili):**
- Names cluster dominates: vocabulary items, parts of speech, grammatical categories.
- Formulas cluster reframed as "Rules": sentence construction patterns, conjugation rules. Example front: *"Present Perfect formula"*. Back: *"have/has + past participle — Hook: HHPP — Have/Has + Past Participle."*
- Insights cluster: etymology hooks for vocabulary memorization.

**Tabiy Fanlar (Biology/Physics/Chemistry):**
- All 4 clusters typically populated. Chemistry sessions may have 10–12 cards for formula-heavy chapters.
- Decisions cluster: reaction conditions, safety rules, classification criteria. Example front: *"Kislota va asos reaksiyasi sharti"*. Back: *"pH < 7 = kislota, pH > 7 = asos — Hook: 7 = neytral, pastga = nordon, tepaga = achchiq."*
- Insights cluster: discovery-context hooks (e.g., "Mendeleev's nightmare that revealed the periodic table pattern").

**Ijtimoiy Fanlar (History/Geography):**
- Names cluster: key figures, dates, places, events.
- Formulas cluster reframed as "Frameworks": cause-effect models, economic principles, geographic classification rules.
- Insights cluster: motivations and consequences as mnemonic anchors.

## Verification rules

1. **Card count in bounds:** Total cards must be 2–12. Fewer than 2 = incomplete deck; more than 12 = spec violation.
2. **Cluster count:** Cards must be assigned to exactly 4 clusters: Names, Formulas, Decisions, Insights. Empty clusters are permitted but must be explicitly labeled as empty (not omitted).
3. **One concept per card:** Each card back must address exactly one formula, concept, or rule. Test: no card back should contain more than one definition, more than one formula, or conjunctions ("and also", "as well as") that join two distinct concepts.
4. **Memory hook present:** Every card back must include exactly one "Hook:" line. Test: count cards where "Hook:" prefix is absent — must return 0.
5. **No practice items:** Card backs must not contain questions, prompts to solve, or "try this" language. Test: scan card backs for "?", "solve", "calculate", "explain why" — must return 0 occurrences that constitute an exercise.
6. **Returnable button present:** Session UI must include a "Flash Cards" overlay trigger throughout Phases 1–7. Test: check session layout spec for persistent overlay button.
7. **"Start my Homework" button present:** Phase 0-B must end with this explicit gateway button. Test: check final card or post-deck screen for gateway button element.
8. **Phase 0-B completion flag emitted:** Session state must include `phase_0b_complete: true` before Phase 1 renders.
9. **Textbook coverage:** All key formulas and terms from the chapter that appear in the homework must have a corresponding flash card. No homework item should reference a formula or term that has no flash card. Test: cross-reference homework item tags against card deck.
10. **Pronoun compliance:** Scan all Uzbek text for "sen" — must return zero occurrences.

## Integration points

**Entry:**
- `render_phase_0b(chapter_id, grade_band, schema_keywords)` is called after Phase 0-A completion flag is received.
- Schema keywords from Phase 0-A Panel 5 are used to sort cards within clusters (matched cards surface first).
- No additional inputs required.

**Exit:**
- Student taps "Start my Homework" → session state records: `phase_0b_complete: true`, `cards_seen: [...]`, `cards_skipped_fast: [...]`.
- Flash card deck is persisted in session overlay store — available for on-demand access throughout Phases 1–7.
- Session timer starts. XP accrual begins.
- Phase 1 Memory Sprint component is initialized.

**Cross-references:**
- `00-core/pronoun-policy.md` — governs all student-facing language
- `00-core/content-architecture.md` — textbook-as-source-of-truth rule; cards derive from chapter only
- `00-core/gamification-economy.md` — confirms flash card access has no XP penalty
- Phase 0-A (`phase-0a-preview.md`) — completion flag dependency; schema keywords input
- Phase 1 (`phase-01-memory-sprint.md`) — unlocked after 0-B gateway
- Phase 7 Reflection — fast-flipped cards may be resurfaced as reflection prompts

## UX/animation spec

**Layout:** Full-screen card. One card displayed at a time. Cluster tab bar at top (4 tabs: Names / Formulas / Decisions / Insights) showing current cluster. Card position counter at bottom: *"3 / 12"*.

**3D flip animation:** Card face transition uses CSS `rotateY(180deg)`. Front face renders at 0deg; back face renders at 180deg with `backface-visibility: hidden`. On tap anywhere on card: rotate from 0deg → 180deg over 400ms with `ease-in-out` timing. On second tap: rotate back 180deg → 0deg. No slide — pure rotational flip.

**Swipe navigation:** Horizontal swipe advances to next card (swipe left) or goes back (swipe right). Swipe velocity threshold: 0.3px/ms. Card slides out in swipe direction, next card slides in from opposite side. Duration: 300ms.

**Memory hook styling:** On card back, the "Hook:" line is rendered in a distinct color (subject accent color), slightly larger font (14px vs 12px for definition body), with a small lightning bolt icon prefix. Visually separate from definition.

**Cluster divider:** Between clusters, a full-width cluster label card is shown (non-flippable). Background: subject accent color at 15% opacity. Text: cluster name centered, 20px semibold. Student swipes through it like any other card.

**"Start my Homework" gateway:** After the final card, a dedicated screen renders. Background: subject accent gradient. Centered: chapter title, session type badge, and a large primary button labeled *"Start my Homework"* (Uzbek: *"Dars boshlash"*). Subtle pulsing glow animation on the button to signal readiness. Tapping triggers session timer start.

**Overlay (returnable):** During Phases 1–7, a persistent floating button (bottom-right, 48×48px, card icon) opens the flash card overlay. Overlay slides up from bottom (translateY 100% → 0, 350ms ease-out). Full deck is accessible. Close button (X top-right) dismisses and returns student to their session position. Overlay does not pause the session timer.

**Progress indicator:** Pill-style progress bar on card bottom tracks position within full deck (not per-cluster). Fills left to right as cards are viewed.
