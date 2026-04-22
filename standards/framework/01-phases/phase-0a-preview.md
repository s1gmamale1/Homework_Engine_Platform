---
name: Phase 0-A — Theme Preview
status: v0.1 draft — validated against §22 only
layer: 1 (phase component)
source: UNIFIED-Buzan §4.4 (lines 550-588) + §22 session
---

# Phase 0-A — Theme Preview

## Purpose (WHAT)

Teaching phase that runs before any testing begins: the student reads, absorbs, and builds a mental model of the chapter content — bridging the gap between textbook reading and gamified homework so that no student enters the homework cold.

## Teaching methodology (family-specific — loaded from family adapter)

The Preview is NOT a summary. It is a **teaching session.** The universal principles (two-layer explanation, don't-assume) live in `00-core/core-principles.md` §1.4. The family-specific teaching methodology (genetic method, no-magic-moves, etc.) is loaded from the active family adapter (`02-families/family-*.md`).

**For Aniq Fanlar + Tabiy Fanlar**, the following five principles apply (see `02-families/family-aniq-fanlar.md` §Teaching Methodology for the authoritative version):

### 1. Genetic method (historical-genetic approach)
Teach a concept by retracing its birth: **original problem → struggle → invention → formalization → today's shorthand.** By the time the student meets the formula, they already know WHY it exists and what the world is like without it. The formula becomes inevitable, not arbitrary.

Example (§22): the Babylonian farmer's land problem (2000 BC) → geometric "completing the square" on clay → al-Khwarizmi's *al-jabr* systematizes it (820 AD) → modern `ax² + bx + c = 0` notation. Student sees the 4000-year journey BEFORE meeting the equation.

### 2. No magic moves — show every derivation
Every algebraic manipulation, every "trick" in the textbook must be traced to its source. If the textbook splits `10x` into `12x – 2x` without explanation, the Preview shows the factor-pair algorithm (`p + q = b`, `p · q = c`) that produces that split. Nothing falls from the sky.

Rule: if a step would make a student ask "where did that come from?", the Preview must answer BEFORE the student has to ask.

### 3. Origin journey IS the teaching (not a sidebar)
Panel 4 (Real-Life Research / Origin) is not supplementary history trivia — it is the **narrative backbone** of the Preview. The historical journey from original problem to modern solution IS how the concept is taught. In §22, the Babylonian farmer story was the first panel content, not a fun-fact at the end.

### 4. Translation skill — teach word→formula BEFORE testing it
**MUST INCLUDE IF** Phase 4 Real-Life is active for this family AND the lesson involves setting up equations from real-world constraints. **MUST SKIP IF** family skips Phase 4 (Language, History) OR lesson is pure procedure with no word problems.

When included, Preview Panel 2 (Better Explanation) or Panel 3 (Examples) must explicitly teach the PATTERN for converting a word problem into an equation:

1. **Identify the unknown** → give it a name (x)
2. **Express other quantities** in terms of x (e.g., "length is 10 more than width" → `x + 10`)
3. **Write the constraint** as an equation (e.g., "area = 24" → `x(x + 10) = 24`)
4. **Recognize the equation type** — is it linear? quadratic? How do you know?

The student must see this pattern in Preview BEFORE Phase 4 asks them to apply it. Phase 4 tests APPLICATION of Preview content — never introduces new skills.

Example (§22): Preview showed how the Babylonian farmer's "area = 24, length = width + 10" becomes `x(x + 10) = 24` → `x² + 10x – 24 = 0`. The translation pattern was taught. Phase 4 (Yashil Makon) then asked the same pattern with different numbers.

### 5. Two-layer explanation (rigor + dissection)
Every technical concept gets TWO presentations in sequence:
- **Layer 1 — Full mathematical rigor.** Teacher-level, complete derivation, correct notation, no shortcuts. Written in the tone of a physics PhD who explains from first principles.
- **Layer 2 — "In plain words" (Sodda so'zlar).** Everyday language dissection underneath. Not a summary — a RE-EXPLANATION using concrete metaphors, shorter sentences, zero jargon. Written so a struggling student locks the idea even if Layer 1 was too fast.

Both layers are always present for Panels 1-4. Layer 1 teaches; Layer 2 locks.

### 5. "Where does this come from" transparency
Never assume the student knows why a step is valid. If we write `x² + bx + c = (x + p)(x + q)`, we first expand `(x + p)(x + q) = x² + (p+q)x + pq` to show WHERE the template comes from. Every rewrite has a reason. Every substitution has a source. The student should never feel lost about the logical chain.

---

## Structure (HOW)

**Panel count:** 3–8 panels (adaptive by archetype — see Adaptable parameters).

**Fixed sequencing:** panels are always served in component-number order. Students may not skip panels but may re-read any panel freely.

**The 8 possible panel components:**

| # | Component | What It Delivers | Min Depth |
|---|-----------|-----------------|-----------|
| 1 | **Summary of Book Content** | A cleaner, more digestible reframing of what the textbook chapter covers. Plain language, better visual hierarchy. NOT a rewrite — a refocusing. | **8–10 sentences** |
| 2 | **Better Explanation** | Concepts the textbook assumes the student understands, clarified. Fills the gap between textbook language and student comprehension. | **8–10 sentences** |
| 3 | **Examples** | Additional worked examples beyond what the textbook provides, showing the concept in action step-by-step. | **8–10 sentences** |
| 4 | **Real-Life Research** | The origin story of the concept. Who discovered it? What problem did it solve? What changed in the world because of it? | **8–10 sentences** |
| 5 | **Personal Hook** | First-person address connecting the topic to the student's own life. "Remember when you saw...?" / "Maybe you've wondered why...?" | **8–10 sentences** |
| 6 | **Why This Matters** | Explicit statement of real-world relevance — not "it's on the exam" but genuine why-you-need-this. | **5–10 sentences** |
| 7 | **Industry Application** | How this concept is used in real industries, jobs, and technology. Shows career relevance. | **5–10 sentences** |
| 8 | **Additional Materials** | Curated external resources (videos, articles, simulators). Language does NOT matter — English, Russian, or Uzbek all permitted. Student selects the language they prefer. | **5–10 sentences** |

**Non-negotiable depth rule (from §22 session):** Panels 1–5 require 8–10 sentences minimum. Panels 6–8 require 5–10 sentences minimum. A panel with 2 sentences and a diagram is incomplete. Visual aids complement text — they do not replace minimum sentence counts.

**"In plain words" dissection (§22 addition):** After each panel that introduces a technical term or formula, a brief simplified re-explanation is rendered in a distinct visual block (e.g., light grey card): *"Oddiy qilib aytganda: ..."* ("In plain words: ..."). This block is always present for Panels 1–4 and optional for Panels 5–8 based on technical density.

**Visual generation (§22 addition):** Any concept that is spatial, relational, procedural, or geometric MUST have a visual aid. Full specification in `00-core/visual-generation.md`. Summary:
- **SVG** for shapes, graphs, coordinate planes (production default)
- **Mermaid DSL** for process diagrams, flowcharts, decision trees, mind maps
- **ASCII** as fallback only (prototyping environments)
- 1-3 visuals per Preview session, placed in Panels 2 (Better Explanation), 3 (Examples), or 4 (Origin)
- Max 1 visual per panel. Every SVG requires `<title>` + `<desc>` for accessibility.
- If agent cannot render SVG directly, emit structured JSON placeholder (see `visual-generation.md` §Agent production instruction) for downstream rendering.

**National Pride gate quote:** Before Panel 1 is displayed, a topic-relevant wisdom quote from `quotes_database.json` (subject-tagged, 55/45 national/global ratio) is shown full-screen. The "Davom etish" (Continue) button is disabled for 5 seconds with a visible countdown timer — ensuring the student reads the quote before proceeding. After 5 seconds the button activates. Skipped in Recovery Sessions and Boss-retry sessions.

**Buzan BOST injection — pre-reading and schema priming:**
- **Panel 1 (Summary):** G5+ renders as a Structural Scan — heading tree, bold-term chips, diagram thumbnails rather than flowing paragraphs. Trains Buzan scanning/skimming before deep reading. G3–4 keeps paragraph layout.
- **Panel 5 (Personal Hook):** Adds a schema activation prompt: *"Bu mavzu haqida nimalarni bilasiz?"* (What do you already know about this topic?). Student taps 2–3 keywords or types freely. This is the BOST "Prime" step — activating existing schemas so Phase 2 content anchors to what is already in memory. Tier 1, no scoring.
- **Panel 6 (Why This Matters):** Adds a learning-goals prompt: *"Bugun [Mavzu] haqida nimani bilmoqchisiz?"* (What do you want to learn about [Topic] today?). The student's response is stored and resurfaced in Phase 7 Reflection as a closure check. This is the BOST "Questions/Goals" step.
- **Not applied here:** Radiant Thinking, Peg System, Memory Palace — those are consolidation tools reserved for Phase 5. Applying them before the student has encountered content would be premature.

**Closing transition:** Phase 0-A always ends with the explicit transition sentence: *"Before we start — here are the key ideas you'll need."* This is the handoff trigger to Phase 0-B Flash Cards.

**Pronoun policy:** All student-facing Uzbek content uses "Siz" (formal). Never "sen". Russian: "Вы", never "ты". English: "you" naturally.

## Cognitive load

- **Bloom range:** L1 (Remember) → L3 (Apply). No evaluation or synthesis in the preview phase.
- **PISA range:** Not assessed. Preview is pure exploration — no right or wrong answers.
- **Scoring:** None. No XP, no HP, no penalties.
- **Time budget:** 2–3 minutes (student-paced, no timer pressure). Students may linger on any panel.
- **AI Tier:** Tier 2 (content generation), Tier 1 (delivery).

## Inputs

- Textbook chapter content (primary source — NETS transforms, never alters)
- `quotes_database.json` (for gate quote selection, subject-tagged)
- Subject family tag (determines panel selection defaults and mind-map likelihood)
- Archetype tag (determines panel count: 3 for Algorithm Review, 8 for Concept Intro — see Adaptable parameters)
- Grade band (G3–4 vs G5+ affects Panel 1 rendering mode)
- No outputs from prior phases are required (this is the first phase in the session)

## Outputs

Phase 0-A produces no scored data. It produces the following signals consumed downstream:

- **Schema activation keywords** (from Panel 5 prompt) → stored in session context, available to Phase 2 Story Mode for narrative anchoring
- **Learning goals string** (from Panel 6 prompt) → stored in session context, resurfaced in Phase 7 Reflection
- **Gate quote seen flag** → logged to session record (used by Recovery/Boss-retry logic to skip gate next time)
- **Phase 0-A completion flag** → required before Phase 0-B can unlock

## Adaptable parameters

| Parameter | Default | Override per archetype | Override per family |
|-----------|---------|------------------------|---------------------|
| Panel count | 5 | Algorithm Review: 3 | — |
| Panel count | 5 | Concept Intro: 8 | — |
| Panel count | 5 | Review/Spiral: 4 | — |
| Panel 1 render mode | Structural Scan (G5+) | G3–4: paragraph layout | — |
| "In plain words" block | Required Panels 1–4 | Optional: high-density technical panels only | Aniq Fanlar: always include for formula panels |
| Mind map inclusion | Relational/process concepts only | — | Tabiy Fanlar: encourage for process chains |
| Gate quote | Always shown | Skipped in Recovery + Boss-retry | — |
| BOST Panel 5 prompt | Free text + keyword tap | — | — |
| BOST Panel 6 prompt | Free text | — | — |

## Subject-specific examples

**Aniq Fanlar (Math/Geometry/Algebra):**
- Panel 3 (Examples) will contain step-by-step worked solutions. "In plain words" blocks required after each formula introduction.
- Mind maps appropriate for multi-step algorithm panels (e.g., order of operations flowchart in Mermaid `flowchart LR`).
- Panel 4 (Real-Life Research): mathematician origin stories (Al-Xorazmiy for algebra, Euclid for geometry).

**Til Fanlar (English/Ona Tili/Rus Tili):**
- Panel 2 (Better Explanation) often addresses grammar rule nuances that textbooks state without explaining.
- Panel 5 (Personal Hook): connect grammar/vocabulary to media the student already consumes (songs, games, social media).
- Mind maps appropriate for morphological trees or sentence structure diagrams.

**Tabiy Fanlar (Biology/Physics/Chemistry):**
- Panel 4 (Real-Life Research): discovery stories are especially powerful (e.g., Mendeleev's periodic table dream, discovery of DNA).
- Panel 7 (Industry Application): connect to medicine, engineering, environmental science.
- Mind maps strongly encouraged for biological process chains (e.g., photosynthesis flowchart, food web `graph TD`).

**Ijtimoiy Fanlar (History/Geography):**
- Panel 3 (Examples) replaced with primary source excerpts or case studies where available.
- Panel 7 (Industry Application): reframe as "modern relevance" — how does this historical event shape today's geopolitics/economics?
- Mind maps appropriate for cause-and-effect chains (e.g., `graph TD` for causes of WWI).

## Verification rules

1. **Panel count in bounds:** Panel count must be 3–8. Fewer than 3 = incomplete; more than 8 = spec violation.
2. **Min depth met:** Panels 1–5 must contain ≥8 sentences (excluding diagram captions). Panels 6–8 must contain ≥5 sentences. Test: count sentences excluding list bullets and diagram captions.
3. **No quiz items:** Phase 0-A must contain zero answer-input elements. No radio buttons, no text fields, no scoring triggers. Test: search rendered HTML for `<input>`, `<button class="answer">` — must return empty.
4. **Gate quote present:** A quote block from `quotes_database.json` must appear before Panel 1 with a 5-second countdown. Test: check for quote render + countdown timer render in session payload.
5. **Transition sentence present:** Final panel must end with the exact transition: *"Before we start — here are the key ideas you'll need."* (or its Uzbek/Russian equivalent). Test: string match on final panel content.
6. **Pronoun compliance:** Scan all Uzbek text for "sen" — must return zero occurrences. "Siz" form only.
7. **Textbook accuracy:** All factual content must trace to the textbook chapter. NETS refocuses and enriches; it does not introduce external curriculum. Test: manual review against chapter source.
8. **"In plain words" blocks present:** Every panel introducing a formula or technical term must have a corresponding simplified explanation block. Test: check for `[plain-words]` tag after formula-bearing panels.
9. **BOST prompts present in Panels 5 and 6:** Panel 5 must include the schema activation prompt; Panel 6 must include the learning goals prompt. Test: string match for prompt text in panel content.
10. **Phase 0-A completion flag emitted:** Session state must include `phase_0a_complete: true` before Phase 0-B renders.

## Integration points

**Entry:**
- Session bootstrap calls `render_phase_0a(chapter_id, archetype, grade_band)`.
- `quotes_database.json` is queried for subject-tagged quote → gate quote rendered.
- No dependency on prior phase outputs (first phase in session).

**Exit:**
- On student tap of transition button (end of final panel), session state records: `phase_0a_complete: true`, `schema_keywords: [...]`, `learning_goals: "..."`, `gate_quote_seen: true`.
- These signals are passed to session context store.
- Phase 0-B Flash Cards component is unlocked and auto-navigated to.

**Cross-references:**
- `00-core/pronoun-policy.md` — governs all student-facing language
- `00-core/content-architecture.md` — textbook-as-source-of-truth rule
- `00-core/context-policy.md` — panel content scope (current chapter only)
- `system/narrative/quotes_database.json` — gate quote source
- Phase 0-B (`phase-0b-flashcards.md`) — receives schema keywords for card relevance weighting
- Phase 7 Reflection — receives learning goals string for closure check

## UX/animation spec

**Layout:** Card-based. Each panel is a full-screen card with bottom navigation arrows and a progress indicator (e.g., "Panel 2 of 5").

**Gate quote screen:** Full-screen overlay with quote text centered, attribution line below. "Davom etish" button visible but greyed out with countdown circle (5-second). On activation, button brightens and becomes tappable. Fade-out transition to Panel 1.

**Panel entrance animation:** "Bubbly text entrance" — each sentence block fades in sequentially from top, with a slight upward translate (8px → 0px) and opacity 0 → 1 over 300ms per block, staggered 80ms apart. Diagrams and mind maps fade in as a single block after text settles.

**Panel transitions:** Slide + blur. Swiping or tapping "Next" triggers: current card slides left (translateX 0 → -100%) while simultaneously applying blur (filter: blur 0 → 4px), and incoming card slides in from right (translateX 100% → 0%) with blur clearing. Duration: 350ms, ease-in-out.

**"In plain words" block:** Distinct visual treatment — light grey rounded card (#F5F5F5), left border accent in subject color, italic body text. Appears inline below the technical paragraph it references.

**Mermaid mind map rendering:** Rendered inline within the panel card. Max width: 100% of card width. Scrollable horizontally if wider than viewport. Caption line below in 12px muted text.

**BOST Panel 5 prompt:** Appears as a soft-blue prompt box below the panel body. Keyword chip tray (pre-populated with 6–8 subject-relevant chips, student taps to select) + optional free-text field below. Chips selected turn solid blue. No scoring, no validation.

**BOST Panel 6 prompt:** Similar soft-blue prompt box. Single free-text field (multiline, max 3 lines). Placeholder: *"Bugun nimani bilmoqchisiz?"* Submitted on "Next" tap — field content saved to session context.

**Swipe support:** All panels are horizontally swipeable (left/right). Swipe velocity threshold: 0.3px/ms. Prevents accidental swipes.

**Progress bar:** Horizontal pill bar at top of card. Fills proportionally as panels are completed. Color: subject-family accent color.
