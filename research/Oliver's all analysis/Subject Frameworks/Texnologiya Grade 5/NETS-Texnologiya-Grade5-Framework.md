# NETS Homework Framework — Grade 5 (Uzbek) — Texnologiya (Technology)

**Version:** 3.1 (audited & revised)
**Date:** 2026-04-08
**Status:** Production-ready specification — single source of truth for Grade 5 uz Texnologiya homework.
**Supersedes:** v3.0 (Qwen baseline, same date)
**Audit:** Cross-checked against Universal Specs by Claude 2026-04-08; 8 fixes applied (4 MAJOR, 4 MINOR). See §20 changelog.

**Pipeline position:**

```
Universal Framework (NETS-Homework-Engine-UNIFIED.md v2.0, 2026-04-07)
        │
        ▼
Psychology Filter (qwen-grade5-psychology-findings.md)
        │
        ▼
THIS DOCUMENT  ←  Grade 5 uz Texnologiya adapted spec
        │
        ▼
Per-chapter homework sessions (produced by content team / openclaw)
```

**Source documents:**
- `NETS-Homework-Engine-UNIFIED.md` — master spec (the WHAT)
- `NETS-Homework-Engine-Blueprint.docx` — universal session lifecycle (the HOW)
- `NETS-Homework-Engine-Standards-Summary.docx` — standards/PISA framework
- `NETS-Homework-Engine-Blueprint-Summary.docx` — phase summary
- `qwen-grade5-psychology-findings.md` — Grade 5 cognitive/psychological research
- `5-sinf_texnologiya_2020_(elekton_darslikbot).pdf` — Grade 5 Texnologiya textbook (Tohirov, Mirahmedova, Shamsiyeva, "Sharq" NMK, 2020, 240pp, ISBN 978-9943-5997-4-1)

This is a **delta layer** — overrides, parameter tunings, and Texnologiya-specific selections on top of the universal blueprint. Anything not mentioned here inherits from UNIFIED unchanged.

---

## §0. Resolution Log — Design Decisions

Texnologiya is a **practical, hands-on life-skills subject** with two parallel tracks (Technology & Design vs. Service). This creates unique challenges for a digital homework engine. These are the calls made:

| # | Topic | Decision | Reasoning |
|---|---|---|---|
| 1 | **Two-track textbook** — students study EITHER Technology & Design OR Service, not both | **BOTH tracks included in framework.** Content tagged by track. Teacher assigns track per student. Engine selects appropriate items. | Schools assign tracks by gender or preference, but the engine must serve both. Tagging allows flexible assignment. |
| 2 | **Session duration** | **35–45 min Standard** (same as Science) | User instruction; consistent across Grade 5 subjects. |
| 3 | **Notebook Capture frequency** | **1 in every 2 sessions** (higher than Science's 1-in-3) | Texnologiya is inherently about making/drawing/designing. Sketches, diagrams, design plans, food prep sequences, embroidery patterns — all benefit from physical drawing. Highest-leverage mechanic for this subject. |
| 4 | **MC in Boss** | **30% allowed** at G5 (same as Science) | Universal "no MC" too strict for 10–11. MC useful for tool identification, material classification, safety rule recognition. |
| 5 | **Adaptive Quiz** | **BANNED** for G5 (same as Science) | IRT feels like endless testing at age 10. |
| 6 | **Peer Teaching** | **BANNED** (same as Science — Uzbek classroom culture: 35–38 students, teacher-centered) | Consistent with Grade 5 psychology filter. |
| 7 | **Flash Card count** | **5–7 cap** (Cowan WM ceiling) | Consistent with Grade 5 psychology filter. |
| 8 | **Why Chain depth** | **2 levels max** (conservative WM safety) | Consistent with Grade 5 psychology filter. |
| 9 | **Boss HP** | **Tiered 30/50/80 by PISA level** (same as Science) | Differentiated instruction. |
| 10 | **Story Mode segments** | **3 segments × 90 sec** structurally + total 5–7 min including game-break interleaving | Consistent with universal spec. |
| 11 | **Memory Palace vs labeled diagrams** | **Labeled diagram recall is default** for Texnologiya; Memory Palace is alternative for chapters where loci feel natural (e.g., workshop walkthrough, kitchen tour) | Diagrams beat loci for tool identification, process flows, construction plans. Memory Palace useful for spatial processes (workshop layout, kitchen zones). |
| 12 | **Practical work in homework** | **Homework engine covers theoretical/conceptual knowledge ONLY.** Actual hands-on work (cutting wood, cooking, sewing) happens in class. Homework prepares the mind; class builds the hands. | Digital homework cannot replace physical practice. But it CAN teach safety, sequencing, material properties, tool recognition, and design thinking — all prerequisites for effective workshop/kitchen time. |
| 13 | **PISA mapping** | **Track-aware triple-tag**: Track 1 (Tech & Design) leans **PISA Science L1→L2** (materials/energy/mechanisms) + Creative Thinking + TR. Track 2 (Service) leans **PISA Creative Thinking** (design/textile/culinary creativity) + TR + Reading L1→L2 (recipe/instruction comprehension). PISA Science applies only to genuinely scientific content (food chemistry, fabric properties, energy systems). | Texnologiya doesn't fit cleanly into PISA Math/Reading. Forcing PISA Science onto cooking/embroidery is indefensible. The two tracks need different primary domains. |
| 14 | **Safety-critical content** | **Any question involving workshop/kitchen safety gets DOUBLE weight in scoring and ZERO tolerance for wrong answers.** Wrong safety answer = immediate scaffold + worked example + re-ask. No partial credit. | Safety is non-negotiable. A wrong answer about machine guards or knife handling is a real-world danger. |
| 15 | **Cultural anchoring** | **Uzbek traditional crafts central:** kashtachilik (embroidery), atlas/adras fabric science, national dishes (qaynatma sho'rva, mastava, somsa), local materials (paxta/cotton, yog'och/wood types). Global tech context secondary. | Textbook explicitly centers Uzbek material culture. NETS preserves and amplifies this. |
| 16 | **AI tier cost strategy** | **Per-phase T1/T2/T3 budget** ($3–5/student/year). Notebook Capture (T3 vision) heavily used. | Consistent with universal cost targets. |
| 17 | **Anti-cheat cultural framing** | **Mother-as-supervisor as collaborative scaffolding** (not cheating). For Texnologiya, mother may actively help with cooking/sewing tasks at home — this is PEDAGOGICALLY APPROPRIATE, not cheating. | Home economics IS home learning. Mother helping with a salad recipe or embroidery stitch is the textbook's intent. |
| 18 | **Personal Hook track-matching** | Theme Preview Panel 5 (Personal Hook) MUST be track-aware. Track 1 anchors to father/grandfather/uncle making things; Track 2 anchors to mother/grandmother/aunt cooking/sewing/embroidering. Mixed framing for Combined Bob 3 (Energy). | Hardcoded paternal anchor would alienate Service track students. Maternal anchor would alienate Tech & Design students. Track-aware framing is mandatory. |

---

## §1. Audience Profile

**Inherited from `qwen-grade5-psychology-findings.md` §1–2 + §7 (universal Grade 5 Uzbek base).** Texnologiya-specific deltas noted inline.

| Dimension | Value (from qwen research) | Texnologiya Delta |
|---|---|---|
| Age | 10–11 years old | — |
| Cognitive stage | Late concrete operational (Piaget) — concrete reasoning solid, abstract emerging but unreliable | **Spatial reasoning still developing** — 2D diagrams before 3D mental rotation. All technical drawings must be 2D-first with clear labeling. |
| Working memory | 4–5 chunks (Cowan, 2001) | **Procedural sequences max 3 steps** at a time. Break "cut → measure → sew" into sub-steps. |
| Sustained academic attention | 20–30 min (35–40 min gamified) | **Hands-on planning tasks hold attention longer** (up to 40 min) because they feel like "doing" not "studying." |
| Reading level | Lexile 830–1010L | Technical vocabulary (duradgorlik, polimer, gazlama, andaza) must be defined on first use with visual + Uzbek plain-language equivalent. |
| Receptive vocabulary | 12,000–14,000 words | — |
| Productive vocabulary | 6,000–8,000 words | — |
| Metacognitive monitoring accuracy | 0.4–0.5 correlation with actual performance | **Structured reflection only.** "Which tool would you use for X?" works. "Describe your design thinking process" is too abstract. |
| Self-concept fragility | High — public failure causes lasting disengagement | **"I'm not good with my hands"** is a common self-limiting belief at this age. Never reinforce. Frame all failure as "you haven't practiced this YET." |
| Peer comparison sensitivity | Peaks at this age | **Cooperative design challenges** (class-wide goals) work better than individual competition. |
| Productive struggle ceiling | ~30 sec before scaffolding required | — |
| Recovery time after wrong answer | 30–90 sec before re-engagement | — |
| Schooling structure | Grade 5 = first year of basic secondary | — |
| Class size (Uzbek urban) | 35–38 students | Workshop/kitchen supervision is 1 teacher for 35+ students with tools. Safety awareness is critical. |
| Device reality | Shared family smartphone — mobile-first non-negotiable | **All technical diagrams must be legible on 5" screen.** No tiny tool labels. |
| Internet | 89–93% mobile penetration | — |
| After-school window | 2–3 hours, peak 17:00–19:00 | — |
| Primary homework supervisor | Mother (cultural norm, Grades 5–7) | **Mother is an ACTIVE CO-TEACHER for Texnologiya Service track** (cooking, sewing). Frame homework as "learn together" not "test alone." |
| Primary language | Uzbek (Latin script). Russian/English in Additional Materials only. | — |

---

## §2. Subject Identity — What Is "Grade 5 Texnologiya"?

**Texnologiya** = Technology / Practical Life Skills. Grade 5 is the **first year of integrated technology education** in the Uzbek curriculum, combining engineering concepts, material science, life skills, and traditional crafts.

**Subject scope:**
- **Track 1 — Technology & Design:** Modern machinery, woodworking, polymer materials, 3D modeling, energy systems, transport design
- **Track 2 — Service:** Food preparation, table culture, textile science, sewing, embroidery (Uzbek traditional crafts)
- **Cross-cutting:** Safety awareness, environmental responsibility, project planning, design thinking

**Pedagogical posture:** *Making, planning, and understanding how things work.* Texnologiya at this age is about:
- **Understanding materials** — what they are, where they come from, what they can do
- **Understanding tools** — what each tool does, when to use it, how to use it safely
- **Understanding processes** — the sequence of steps to make something
- **Understanding design** — why things are shaped/sized the way they are
- **Understanding culture** — how Uzbekistan's crafts, food, and materials connect to the student's heritage

**Important:** This textbook has a **two-track system**. Students are assigned ONE track per school. The homework engine must support both tracks but serve only the assigned track per student.

### Textbook Source

| Field | Value |
|---|---|
| Title | Texnologiya 5-sinf |
| Authors | O'. O. Tohirov, D. S. Mirahmedova, Z. S. Shamsiyeva |
| Publisher | "Sharq" nashriyot-matbaa AJ, Bosh tahririyati, Toshkent |
| Year | 2020 |
| Pages | 240 |
| ISBN | 978-9943-5997-4-1 |
| Approved by | O'zbekiston Respublikasi Xalq ta'limi vazirligi |

### Chapter Map → Session Map

**TRACK 1: Texnologiya va Dizayn (Technology & Design)**

| Bob | Title (Uzbek) | English | Pages | Sessions | Domain |
|---|---|---|---|---|---|
| 1 | Zamonaviy texnika va texnologiyalar | Modern Technology & Technologies | 6–14 | 2 | Engineering |
| 2.1 | Yog'ochga ishlov berish | Woodworking | 15–75 | 6 | Materials/Craft |
| 2.2 | Polimer materiallarga ishlov berish | Polymer Materials & 3D | 76–93 | 3 | Materials/Design |

**TRACK 2: Servis Xizmati (Service)**

| Bob | Title (Uzbek) | English | Pages | Sessions | Domain |
|---|---|---|---|---|---|
| 1.1 | Ovqatlanish madaniyati | Food Culture | 96–102 | 2 | Culinary |
| 1.2 | Oziq-ovqat mahsulotlariga ishlov berish | Food Processing | 103–125 | 4 | Culinary |
| 2.1 | Gazlamashunoslik | Fabric Science | 127–162 | 4 | Textile |
| 2.2 | Tikuvchilik | Sewing & Design | 163–182 | 4 | Textile/Craft |
| 2.3 | Kashtachilik | Embroidery (Folk Craft) | 183–196 | 3 | Traditional Craft |

**COMBINED (Both Tracks)**

| Bob | Title (Uzbek) | English | Pages | Sessions | Domain |
|---|---|---|---|---|---|
| 3 | Energiya ishlab chiqarish va undan foydalanish | Energy Production & Use | 200–220 | 3 | Engineering/Science |

**Total:** 3 main bobs per track + 1 combined bob · **~21–24 homework sessions per track** to produce.

### Standard Code Pattern

`UZ-TEX-5-{TOPIC}-{SEQ}` — e.g., `UZ-TEX-5-WOOD-01`, `UZ-TEX-5-COOK-03`, `UZ-TEX-5-SEW-02`.
Alias dotted: `TEX.5.{bob}.{section}.{seq}`.

Track tags: `track:tech_design` or `track:service` on every content item.

---

## §3. PISA Mapping — Grade 5 Texnologiya Target

Texnologiya does not map cleanly to a single PISA domain. We use a **track-aware triple-tagging strategy** because the two tracks have fundamentally different epistemological centers — Tech & Design is closer to engineering/science, Service is closer to creative/practical arts.

### Track 1 — Tech & Design primary tagging

| Primary Tag | Coverage | Purpose |
|---|---|---|
| **PISA Science L1→L2** (PRIMARY) | Materials properties (wood/polymer), energy types, physical processes, mechanism cause-effect | Core scientific reasoning for engineering content |
| **PISA Creative Thinking** (SECONDARY) | Design challenges, invention scenarios, "what if you had no X?" problems | Design problem-solving |
| **Custom TR L1→L4** (ALWAYS) | Tool selection, process sequencing, safety judgment, design evaluation | Practical reasoning |

### Track 2 — Service primary tagging

| Primary Tag | Coverage | Purpose |
|---|---|---|
| **PISA Creative Thinking** (PRIMARY) | Recipe variation, pattern design, color/material combination, stitch innovation, presentation aesthetics | Creative making is the heart of Service content |
| **PISA Reading L1→L2** (SECONDARY) | Recipe/instruction comprehension, ordering steps, interpreting diagrams | Procedural literacy |
| **PISA Science L1→L2** (CONDITIONAL) | Only for genuinely scientific content: food chemistry (yeast, baking, nutrition), fabric properties (weave, dye, fiber), heat/cold cooking effects | Don't force-fit Science onto pure craft content |
| **Custom TR L1→L4** (ALWAYS) | Tool/utensil selection, process sequencing, hygiene/safety judgment, design evaluation | Practical reasoning |

### Combined Bob 3 — Energy
Both tracks: PISA Science L1→L2 (PRIMARY) + Creative Thinking + TR. Energy content is genuinely scientific for both tracks.

### Technical Reasoning (TR) Track — Custom 4-Level Scale

### Technical Reasoning (TR) Track — Custom 4-Level Scale (universal across both tracks)

| TR Level | What Student Can Do | Example | Bloom's Pairing |
|---|---|---|---|
| **TR-L1** | Identify tools, materials, and basic safety rules by name | "This is a duradgorlik dastgohi (carpentry bench)" | Remember |
| **TR-L2** | Explain what a tool does, why a material is chosen, sequence steps for a simple process | "Yog'och needs to be measured before cutting because..." | Understand, Apply |
| **TR-L3** | Analyze a design problem, select appropriate tools/materials, justify choices, identify safety risks in a scenario | "For making a bookshelf, use yog'och not polimer because..." | Analyze |
| **TR-L4** | Design a solution to a novel problem, evaluate trade-offs, propose improvements to an existing design | "If you had no 3D ruchka, how else could you make this? Compare options." | Evaluate, Create |

**Grade 5 target:** TR-L1 → TR-L2 as the dominant scaffold, with TR-L3 stretch goals for top quartile.

### Mandatory `transition_skill` Tags for G5 Texnologiya

Every task must carry one of:

- `L1→L2: identify tools/materials and explain their purpose`
- `L1→L2: sequence steps in a simple making process`
- `L1→L2: recognize safety rules and explain why they matter`
- `L2→L3: select appropriate tools/materials for a given task`
- `L2→L3: analyze a design and suggest improvements`
- `L2→L3: predict what happens if a step is skipped or done wrong`
- `L3→L4: design a solution using available materials, evaluate trade-offs`

DRAFT tasks without one of these tags are rejected by content review.

### PISA Science Sub-Domains Used

| Sub-Domain | Texnologiya Connection |
|---|---|
| Physical systems | Materials (wood, polymer, fabric), energy types, mechanisms |
| Earth & space | Natural resources (cotton, wood types), environmental impact |
| Living systems | Food science (vegetables, eggs, nutrition) — Service track |

---

## §4. Psychology Filter — Applied Parameters

### 4.1 Session Timing (inherits Universal §4.1, tuned for Texnologiya)

| Parameter | Universal | Grade 5 Texnologiya |
|---|---|---|
| **Standard session total** | 30–45 min | **35–45 min** (includes 0-A + 0-B + 7 phases) |
| **Single phase max** | varies | **5–9 min** (hard ceiling) |
| **Inter-phase break** | varies | **5–15 sec** loading screen with "Did You Know" |
| **Daily homework cap** | not specified | **1–2 sessions / 30–60 min total** |
| **Recommended deployment window** | not specified | **17:00–19:00** (Uzbek after-dinner norm) |

### 4.2 Difficulty Calibration (overrides Universal §9)

| Parameter | Universal | Grade 5 Texnologiya |
|---|---|---|
| **Flow state success rate** | 70–80% | **75–85%** (higher floor for kids) |
| **Adapt frequency** | every 3–5 questions | **every 3–4 questions** |
| **Difficulty visibility** | not specified | **HIDDEN** — never show "Easy/Medium/Hard" |
| **Pass threshold** | not specified | **60% minimum** |
| **Tier-down trigger** | <60% | **<70%** (catch slipping students 10 pts earlier) |
| **Productive struggle ceiling** | not specified | **30 seconds** before scaffolding |
| **Wrong answer language** | "Try again" | **"Hali emas" / "Not yet"** (+40% persistence, Yeager 2019) |
| **New technical terms** | not capped | **max 1–2 per session** (vocab ceiling) |
| **New concepts per instruction** | not capped | **max 3** (Cowan WM) |
| **Safety questions** | standard scoring | **DOUBLE weight, ZERO tolerance for wrong answers** |

### 4.3 Banned Techniques for G5 Texnologiya (filter list)

These are **filtered OUT** from the universal mechanic/feature roster:

1. ❌ Public displays of wrong answers — fragile self-concept
2. ❌ Absolute-rank leaderboards — only improvement ranking or class goals
3. ❌ Real-time multiplayer competition — skill gaps demoralize
4. ❌ Pure discovery / unbounded sandbox — lacks self-direction
5. ❌ Random rewards without competence link
6. ❌ Purchasable cosmetics — earned only
7. ❌ Abstract-only puzzles — CPA mandatory (even for Texnologiya)
8. ❌ Complex multi-step instructions without worked examples
9. ❌ Delayed feedback (>seconds)
10. ❌ "You're smart" / ability praise — use effort + strategy
11. ❌ The word "wrong" — use "not yet" / "not quite" / "close — here's why"
12. ❌ Brain breaks every 5 min — disruptive at this attention span
13. ❌ Learning styles matching (visual/auditory/kinesthetic)
14. ❌ Why Chain ≥3 levels — over WM ceiling for G5
15. ❌ Visible difficulty labels in UI — triggers self-handicapping
16. ❌ Group/peer-correction as primary feedback — solo-first for concept acquisition
17. ❌ **Adaptive Quiz** mechanic — IRT feels like endless test
18. ❌ **Peer Teaching** mechanic — Uzbek classroom culture mismatch
19. ❌ **Actual hands-on tasks as homework** — cutting, cooking, sewing happen in class. Homework teaches the *thinking* before the *doing*.

### 4.4 Mandatory Additions for G5 Texnologiya

1. ✅ **CPA progression** — Concrete (real tool/photo) → Pictorial (diagram/label) → Abstract (definition/process) for every concept
2. ✅ **Dual coding** — Story Mode never text-only, image+text always
3. ✅ **Worked example before independent practice** — show the complete process before asking student to plan it
4. ✅ **Spaced retrieval** — Memory Sprint pulls Day 1/3/7/14, not just current chapter
5. ✅ **Effort + strategy feedback** — never ability framing
6. ✅ **Cultural anchors** — Uzbek crafts (kashtachilik, atlas, paxta), national dishes, local materials, Central Asian inventors
7. ✅ **Mobile-first portrait, low-bandwidth** — shared family smartphone
8. ✅ **Variable-ratio reward windows** — opportunity earned via competence
9. ✅ **Hidden difficulty tiering** — adapts silently
10. ✅ **30-second productive struggle window** before scaffolding
11. ✅ **Safety-first scoring** — safety questions carry 2× weight, zero tolerance
12. ✅ **Track-aware content** — every item tagged `track:tech_design` or `track:service`; engine serves only assigned track

---

## §5. Pre-Homework — Sessions 0-A and 0-B

Both run before the 7-phase engine. Timer does not start until the student taps **"Boshlash" / "Start my Homework"**. No XP, no scoring, no penalties.

### 5.1 Session 0-A — Theme Preview (Swipe Deck)

**Refers to:** Universal §4.4. The 8 panels are mandatory; this section tunes them for Grade 5 Texnologiya.

**Duration:** 2–3 min, student-paced
**Format:** Vertical swipe deck (TikTok/Tinder-style cards)
**Tier:** AI Tier 2 generates personalized framing per student PISA level + track assignment

| Parameter | Universal | Grade 5 Texnologiya |
|---|---|---|
| Panel count | 8 mandatory | 8 — unchanged |
| Reading level | not specified | **Lexile 830–1010L**, average sentence ≤14 words, active voice |
| Visual-first ratio | "preferred" | **Mandatory** — every panel leads with photo/diagram/short clip of tools, materials, or finished products; text is secondary |
| Language | not specified | **Uzbek only** for student-facing text; Russian/English permitted only in Additional Materials |
| POV | first-person | **Second-person Uzbek** — *"Sen bilasanmi…?"* / *"Sen ko'rganmisan…?"* |
| Personal Hook (panel 5) | not specified | **TRACK-AWARE — mandatory.** Track 1 (Tech & Design): anchor to father/grandfather/uncle/older brother making/fixing/building (*"Sen bobongiz yoki dadangiz biror narsa yasaganini ko'rganmisan?"*). Track 2 (Service): anchor to mother/grandmother/aunt/older sister cooking/sewing/embroidering (*"Sen onangiz yoki buvingiz osh pishirayotganda yoki kashta tikayotganda kuzatganmisan?"*). Combined Bob 3 (Energy): mixed — anyone in family using/discussing electricity/water/heat at home. **Avoid** abstract engineering concepts. |
| Industry Application (panel 7) | not specified | Use jobs G5 students recognize: `duradgor` (carpenter), `oshpaz` (cook), `tikuvchi` (seamstress), `kashtachi` (embroiderer), `muhandis` (engineer), `me'mor` (architect). **Avoid** "software developer," "robotics engineer." |
| Real-Life Research (panel 4) | not specified | Lead with **Uzbek material culture** when possible. Cotton (paxta) → textile industry. Wood carving → Khiva/Bukhara architecture. Embroidery → Silk Road heritage. National dishes → culinary tradition. |
| Additional Materials (panel 8) | "any language" | Video > article. YouTube short showing a craftsperson at work / 360° photo of a workshop > written article. Allow English/Russian/Uzbek mix. |
| Animation language | per UI/UX spec | Whoosh + letter-assembly transition — 400ms whoosh + 600ms assembly. Keep it fast — engagement at this age. |
| Skip behavior | swipe / dots | Both. Pagination dots double as "I'm done" jump. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate. |
| Did You Know | universal §6.5 | Inject **one** Did You Know themed to upcoming topic between panels 4 and 5. |

**Mandatory 8 components** (in order):

1. **Summary of Book Content** — 2-3 sentence textbook section summary
2. **Better Explanation** — same concept rephrased with metaphor + concrete analogy
3. **Examples** — 2-3 short examples (Concrete → Pictorial, never abstract-only)
4. **Real-Life Research** — Uzbek craft/tradition origin story
5. **Personal Hook** — direct "you" framing tied to student's daily life
6. **Why This Matters** — connects to safety, daily decisions, family traditions
7. **Industry Application** — Uzbek professionals using this skill
8. **Additional Materials** — links/embeds in any language

**Quality gate:** Run the **"10-year-old Stranger Test"** before publishing. Show the 8 panels to someone who's never seen the textbook. If they can describe what skill is being learned and feel curious, it passes. If lost or bored, rewrite.

### 5.2 Session 0-B — Flash Cards

**Refers to:** Universal §4.5. The carousel is mandatory; this section tunes the deck for Grade 5 Texnologiya.

**Duration:** 1–2 min initial pass, **returnable throughout homework via floating "Flash Cards" button** (NOT a hint, no penalty)
**Tier:** AI Tier 1 (pre-generated per chapter)

| Parameter | Universal | Grade 5 Texnologiya |
|---|---|---|
| **Card count per session** | not capped | **5–7 cards max** (Cowan WM 4–5 + 1–2 buffer). Never more than 7. |
| Card categories | Formula/Concept/Rule/Definition | Prefer **Concept** (tool names, material types), **Rule** (safety rules, process sequences), and **Definition** (technical terms) |
| One concept per card | mandatory | **Strictly enforced** — no compound cards. |
| Visual on every card | not specified | **Mandatory** — front shows term + photo/drawing of the tool/material. Text-only forbidden. |
| Carousel layout | 3D circular | Center 1.0× sharp, neighbors 0.7× blurred. Tap to flip. |
| Flip animation | 500ms | **600ms** for G5 (extra processing time) |
| Tap-to-flip prompt | fades after 2s | Visible **3–4 sec** for first-time confidence |
| Language | not specified | **Uzbek only.** Front in Uzbek; back in plain Uzbek with one Russian equivalent in parentheses if commonly bilingual (e.g., `dastgoh` / `станок`). |
| Cyclic loop | yes | **Yes** — loop "ding" sound signals deck completion. |
| Returnable mid-homework | yes | **MANDATORY for Texnologiya** — tool identification and process sequences often need reference. NOT counted as hint. |
| "Boshlash" button styling | per UI/UX | **Visually rewarding** — full-width, primary color (`#F59E0B` Texnologiya amber accent), gentle pulse animation. |
| Scoring | none | None — verify NO XP, NO timer, NO completion gate |

**Quality gate:** Every Flash Card must pass the **"5-second readability test"** — a G5 student reads front, flips, reads back, feels they "got it" in under 5 seconds per side.

---

## §6. The 7-Phase Engine — Grade 5 Texnologiya

### 6.1 Phase 1 — Memory Sprint (≤2 min, 5–7 items)

| Parameter | Spec |
|---|---|
| Item count | 5–7 (low end — WM ceiling + warm-up buffer) |
| Format mix | Tile Match (tool ↔ name / material ↔ property), Quick MC (safety rules, classification), Sentence Fill (process sequences). **No pure typed recall** (slow + frustrating). |
| Source | **Spaced retrieval pull** — Day 1/3/7/14 schedule from prior chapters, plus 1–2 items from current chapter glossary |
| Visual scaffolding | Every term must show with its visual representation (tool photo, material sample, safety icon) |
| Safety items | Any safety-related recall item gets **priority placement** (first 2 items) |
| Streak bonus | Visible at 3+ correct (fire animation) |
| Wrong answer feedback | Immediate, soft, 5–10 sec positive framing window before next question |
| Remediation gate | <60% → route to remediation chapter before Story Mode (UNIFIED §5.1) |

### 6.2 Phase 2 — Story Mode (5–7 min)

**Story arc for Texnologiya:** Universal Problem → Struggle → Discovery → Solution maps to **real making/crafting stories**.

**Structure:** 3 segments × ~90 sec each, interleaved with checkpoint games. Total ~5–7 min including checkpoints.

| Story arc beat | Texnologiya version |
|---|---|
| **Problem** | Someone needs to make/fix/do something. *"Malikaning buvisi kelin bo'lib kelganida kashta tikishni bilmas edi. U qanday o'rgangan?"* / *"Bobur yog'ochdan qush uyasi yasamoqchi, lekin qaysi asbob kerakligini bilmaydi."* |
| **Struggle** | First attempts fail — wrong tool, wrong material, wrong sequence. *"U birinchi marta pichoq bilan kesishga urindi, lekin yog'och yorilib ketdi."* |
| **Discovery** | The concept/technique/tool is introduced. *"Ustozi dedi: 'Avval o'lcha, keyin belgila, keyin kes. Uch marta o'lcha — bir marta kes.'"* |
| **Solution** | Character succeeds with the right knowledge. *"Endi Bobur biladi — arrani to'g'ri ushlash, sekin va tekis surish kerak."* |

**Hard rules for G5 Texnologiya Story Mode:**

- **CPA mandatory** — every concept touches Concrete (real tool/photo) → Pictorial (diagram/label) → Abstract (the rule/process). 60–70% of exposures need a concrete or pictorial anchor.
- **Real craftspeople / makers preferred** over invented scenarios. Pool: Uzbek woodcarvers (Khiva, Bukhara), embroiderers (Margilan, Shakhrisabz), cooks (national dish masters), modern makers (3D printing labs, textile factories). **Use Central Asian / Uzbek makers wherever the topic allows.**
- **Stranger Test** applies: a reader who's never seen the textbook should understand the process from the narrative alone.
- **Checkpoint questions are process comprehension, not recall.** "Why did the wood split?" YES. "What is the name of this tool?" NO (that's Memory Sprint).
- **Reading level cap:** Lexile 830–1010L. Average sentence ≤14 words. Avoid passive voice.
- **Max 2 retries per checkpoint** → simplified scaffold version.
- **Safety moments:** If the story involves a tool or process with safety implications, a **safety checkpoint** is inserted: "What should the character check before starting?"

**Domain-specific Story Mode tuning:**

| Domain | Problem hook | Predict gate | Results gate | Explain gate |
|---|---|---|---|---|
| Woodworking (Track 1) | Character tries to make something from wood | "Which tool should they use?" MC | Show tool in action, result | "Why that tool?" Tile-Match tool→purpose |
| Polymer/3D (Track 1) | Character needs a specific shape | "What happens if we heat this?" MC | Show melting/molding process | "Why does it change?" Why-Chain (2 levels) |
| Cooking (Track 2) | Character prepares a dish | "What's the next step?" ordering | Show finished dish + process | "Why this order?" open reasoning |
| Textile/Sewing (Track 2) | Character needs to make clothing item | "Which fabric is right?" MC | Show measuring, cutting, sewing | "Why this measurement?" diagram labeling |
| Embroidery (Track 2) | Character learns a stitch pattern | "What comes next in the pattern?" | Show completed embroidery | "Why this stitch order?" sequence reasoning |
| Energy (Combined) | Character needs power for something | "Which energy source works here?" | Show energy conversion | "Why this type?" cause-effect chain |

### 6.3 Phase 3 — Game Breaks (6–9 min, 3 games)

**Universal rule:** 3 games per session, ≥1 from Interactive Catalog + ≥2 from Default 16. Grade 5 Texnologiya overrides the *selection priority*.

**Slot rules for G5 Texnologiya:**

> **Slot 1:** Tile Match OR Memory Match Blitz (tool identification, material classification — visual recognition warmup)
> **Slot 2:** Why Chain (max 2 levels) OR Codebreaker OR Mystery Box (process reasoning, cause-effect)
> **Slot 3:** **Notebook Capture in 1 of every 2 sessions**; otherwise Tic Tac Toe vs AI, Escape Room, or Connect Four vs AI

**Selection algorithm:**
1. **Reinforcement game** at student's current Bloom's level on chapter's main concept
2. **Stretch game** one Bloom's level above
3. **Transition-skill game** scaffolding the TR-L1→L2 (or L2→L3) skill chosen for the session

### 6.4 Phase 4 — Real-Life Challenge (3–5 min)

**First-person expert POV mandatory** (UNIFIED §5.4). Expert must be a Uzbek-context role:

- Track 1 → *"Sen duragarsan / muhandissan / 3D dizaynersan…"*
- Track 2 → *"Sen oshpazsan / tikuvchisan / kashtachisan…"*
- Combined → *"Sen energetiksan / loyihachisan…"*

**Hard rules:**
- First-person address only. *"Sen duragarsan…"* Never "Bobur duragardir…"
- **Real Uzbek context preferred** — local bazaars, family events (to'y, sayil), household needs, school projects
- **Tricky distractors** — at least one plausible-but-wrong answer requiring reasoning to eliminate
- **Justify your answer** — student MUST explain reasoning; AI evaluates the *reasoning*, not just the choice
- **Safety judgment:** Every RLC includes at least one safety-related decision point
- **Eligibility gate:** PISA Reading L2+. Below L2 → fallback adaptive scaffolded version

### 6.5 Phase 5 — Consolidation (3–5 min)

**Default technique for G5 Texnologiya: Labeled diagram / process flow recall.** Show a diagram (tool layout, process sequence, stitch pattern) with labels removed, student fills them back in.

**Per-chapter Phase 5 default:**

| Bob | Diagram template | Labels to fill |
|---|---|---|
| 1 (Modern Tech) | Technology classification chart | texnika turlari, vazifalar |
| 2.1 (Woodworking) | Workshop layout + tool board | duradgorlik dastgohi, arra, iskana, rubanok |
| 2.2 (Polymer/3D) | 3D pen workflow diagram | issiqlik, ekstruziya, qotish |
| 1.1 (Food Culture) | Dasturxon (table setting) layout | tarelka, stakan, pichoq, vilka, qoshiq |
| 1.2 (Cooking) | Recipe process flow chart | tayyorlash, to'g'rash, aralashtirish, pishirish, bezash |
| 2.1 (Fabric) | Fabric weave diagram (polotno/sarja) | tanda, arqoq, to'qish |
| 2.2 (Sewing) | Apron pattern pieces | old qism, orqa qism, bog'ich, cho'ntak |
| 2.3 (Embroidery) | Stitch pattern sequence | chok turi, yo'nalish, takrorlash |
| 3 (Energy) | Energy conversion diagram | mexanik→elektr, quyosh→issiqlik, etc. |

**Alternative technique (Memory Palace) — for chapters where spatial walkthrough feels natural:**

| Bob | Palace location | Why this place |
|---|---|---|
| 2.1 (Woodworking) | Duradgorlik ustaxonasi (workshop) | Tool locations, safety zones, material storage |
| 1.2 (Cooking) | Oshxona (kitchen) — real Uzbek kitchen | Work zones: prep, cooking, cleaning, storage |
| 3 (Energy) | Power plant / hydroelectric station (Charvak SES) | Energy flow: water → turbine → generator → grid |

**Structure for Memory Palace alternative:** 5 loci tied to 5 concepts; each locus has location image + concept text + visual mnemonic + 1 recall question. End with 3-question recall test cycling through loci.

**Duration cap:** 3–5 min. Should feel calm and confident, not stressful. The "I'm ready" moment before Boss.

### 6.6 Phase 6 — Final Boss / Sub Boss (6–8 min)

**Tiered boss HP defaults (based on student PISA level):**

| Student PISA level | Boss tier | HP | Pattern |
|---|---|---|---|
| Below L1 (baseline) | Sub Boss Easy | **30 HP** | TR-L1 questions only, scaffolded |
| L1–L2 (median G5) | Sub Boss Medium | **50 HP** | TR-L1–L2 mix, win expected after 1 retry |
| L2–L3 (top quartile) | Sub Boss Hard | **80 HP** | TR-L2–L3 mix, real challenge |
| L3+ (top decile) | Big Boss + occasional Mythical | **80–100 HP** | TR-L3–L4 stretch |

**Boss content for Texnologiya MUST include (5 questions, distribution Easy 40% / Medium 40% / Hard 20%):**
- 1 tool/material identification question (Tier 1 rule-based or MC)
- 1 process sequencing question (put steps in order / what comes next)
- 1 safety judgment question (**DOUBLE weight**, zero tolerance for wrong)
- 1 design analysis question (why is this shaped this way? what would improve it?)
- Optional Hard: 1 invention/design challenge (solve a novel problem with available materials) — Sub Boss Hard / Big Boss only

**MC allowed at G5 Boss:** **Up to 30%** of questions may be multiple choice.

**Each Boss question MUST carry:**
- Step-by-step worked solution (visible after answer)
- 2–3 progressive **Hints** (revealed on request, not auto-pushed)
- **Common Errors** list — at least 1 known wrong answer with diagnostic explanation

**Difficulty labels (`[EASY]` / `[MEDIUM]` / `[HARD]`) are INTERNAL ONLY** — never shown to student in UI.

**Mechanics:**
- **Hint tax:** −5 HP each (gentler — encourage hint use over giving up)
- **Combo bonus:** 3 in a row → 2× damage on next
- **Max attempts:** 3, with growth-mindset framing on retry (*"Hali emas — yana bir bor sinaymiz"*)

**Mastery Stars (1–3):**

| Stars | Condition |
|---|---|
| ⭐ 1 | Boss defeated (any number of attempts within retry limit) |
| ⭐⭐ 2 | Boss defeated in ≤2 attempts AND >50% HP remaining |
| ⭐⭐⭐ 3 | Boss defeated on FIRST attempt, no hints used, >80% HP remaining |

**Failure → Boss Regeneration:** If student fails all retries, Tier 3 AI runs **Socratic tutoring** based on wrong answers, then **regenerates new boss questions** tailored to the gap for next session continuation. Auto-flags teacher dashboard after **3 failed sessions on the same standard**.

**Big Boss + Mythical Boss** apply per UNIFIED §5.6, capped at 75–85% target rate within the boss.

### 6.7 Phase 7 — Reflection (1–2 min)

**Duration cap:** 1–2 min only — metacognition is limited at this age.

**Tier 2 AI generates ONE prompt per session, selected from a bank by accuracy bucket:**

| Accuracy bucket | Prompt style | Texnologiya example |
|---|---|---|
| **≥80% (mastery)** | Strategy reflection — what worked | *"Qaysi asbobni to'g'ri tanlading? Nima uchun?"* |
| **60–79% (passing)** | Struggle + recovery — what was hard, how solved | *"Qaysi jarayon qiyin bo'ldi? Siz uni qanday hal qildingiz?"* |
| **<60% (Duolingo Mode)** | Support-seeking — what's still unclear | *"Buni yaxshiroq tushunish uchun nima kerak? Qaysi qism chalkash bo'ldi?"* |

**Universal Texnologiya prompts (rotate when not bucket-overridden):**
- *"Bugun qaysi asbob yoki material haqida yangidan bildingiz?"*
- *"Agar sizda [asbob] bo'lmasa, nima bilan almashtirardingiz?"*
- *"Bu ko'nikma uyda yoki maktabda qayerda kerak bo'ladi?"*

**Rules:**
- Min 1 sentence (universal asks 10 chars; G5 should not be pushed to write essays)
- Bloom's = Create, PISA = L3-4 (metacognitive only — not advanced reasoning)
- **Effort + strategy language only** — never "Were you smart enough?" Always "What strategy did you try?"
- Privacy: student-only; teacher sees aggregate themes
- Optional peer-explanation prompt: *"Bu mavzuni darsda yo'q bo'lgan do'stingizga qanday tushuntirgan bo'lardingiz?"*

---

## §7. Content Rules

### 7.1 Narrative Voice

| Element | Rule |
|---|---|
| POV | Second-person (*"Sen ko'rasanmi?"*). Never third-person observer. |
| Tone | Curious, warm, hands-on. The student is a maker/apprentice figuring things out alongside the narrator. |
| Language register | Conversational Uzbek. Technical terms defined inline with visual + plain language. |
| Sentence length | Average ≤14 words. |
| Sentence structure | Active voice. *"Arra yog'ochni kesadi"* YES. *"Yog'och arra tomonidan kesiladi"* NO. |
| Vocabulary | Stay within ~12,000 word receptive range. Define new technical terms with visual + repeat 3+ times across session. |
| Cultural anchors | Uzbek names (Gulnora, Bekzod, Aziza, Sardor, Malika, Jasur, Dilnoza, Otabek). Uzbek places (Tashkent, Samarkand, Bukhara, Khiva, Fergana, Margilan, Chirchiq). Uzbek crafts, foods, materials. |
| Maker references | Mix global inventors with Uzbek/Central Asian craftspeople. At least 1 Uzbek craftsperson per 5 sessions. |

### 7.2 Visuals

| Rule | Detail |
|---|---|
| Every concept gets a visual | CPA mandatory: real photo of tool/material OR diagram OR pictorial representation. No text-only concept introductions. |
| Mobile-first sizing | All visuals legible on a 5" smartphone screen. No tiny tool labels, no fine diagram detail. |
| Animation budget | Universal motion principles (≤800ms, transform+opacity only). |
| Dark mode default | Per UI/UX spec subject color: Texnologiya = `#F59E0B` (amber) primary, `#10B981` (emerald) accent. |

### 7.3 "Did You Know" Facts (Loading Screen + Phase Transitions)

For G5 Texnologiya the **Fun Facts pool** should be heavily craft/technology-themed AND age-appropriate:

- ✅ "Did you know? The first sewing machine was invented in 1790 by Thomas Saint — it was made of wood!"
- ✅ "Did you know? Uzbek atlas fabric uses a special ikat dyeing technique that's over 1,000 years old."
- ✅ "Did you know? A 3D pen heats plastic to 180°C — hot enough to melt ice cream instantly!"
- ✅ "Did you know? Cotton (paxta) is Uzbekistan's most important crop — it's called 'white gold'."
- ✅ "Did you know? The world's oldest embroidered fabric was found in a Scythian tomb in the Altai mountains."
- ❌ Anything involving dangerous machinery without safety context
- ❌ Complex industrial processes beyond G5 comprehension

**Quote Cards** for Texnologiya loading screens should preferentially cite makers, inventors, and craftspeople — especially Uzbek ones.

**Frequency:** 1 Did You Know per phase transition (loading screen, ≤8 sec each, AI Tier 2 generated/curated).

---

## §8. Game Catalog Selections — Final List

### 8.1 Default 16 Mechanics — Usage at G5 Texnologiya

| # | Mechanic | Use? | Notes |
|---|---|---|---|
| 1 | Memory Sprint | YES (P1 default) | Flexible format, mix MC + Tile Match |
| 2 | Spaced Flashcards | YES | Tool names, material types, safety rules (also 0-B) |
| 3 | Tile Match | **YES (HIGHEST priority)** | Tool↔name, material↔property, safety rule↔situation |
| 4 | Sentence Fill | LIMITED | Process sequences only; sparingly |
| 5 | Memory Palace | YES (alternative) | Workshop/kitchen walkthroughs where spatial memory helps |
| 6 | Story Mode | YES (P2 default) | Maker/craftsperson narratives with Stranger Test |
| 7 | Adaptive Quiz | **NO** | IRT feels like endless test; G7+ only |
| 8 | Mystery Box | **YES (high priority)** | "What's inside?" — material identification, tool mystery |
| 9 | Movement Breaks | YES | Optional 30-sec stretch between phases |
| 10 | Why Chain | **YES (high priority, max 2 levels)** | Process reasoning is heart of Texnologiya |
| 11 | Peer Teaching | **NO** | Uzbek classroom culture mismatch |
| 12 | Real-Life Challenge | YES (P4 default) | First-person expert POV, safety judgment required |
| 13 | Reflection Journal | YES (P7 default) | 1-sentence minimum |
| 14 | Final Boss | YES (P6 default) | Tiered HP, MC 30% allowed, safety questions 2× weight |
| 15 | Tic Tac Toe vs AI | YES | Familiar game, recall under stakes |
| 16 | **Notebook Capture** | **YES (HIGHEST priority for Texnologiya)** | **1 in every 2 sessions** — design sketches, process diagrams, stitch patterns |

### 8.2 Interactive Game Catalog 12 — Usage at G5 Texnologiya

| Mechanic | Use? | Notes |
|---|---|---|
| Tic Tac Toe vs AI | YES | (also in Default 16) |
| Connect Four vs AI | YES | Visual strategy, material classification gates |
| Codebreaker (Mastermind) | YES | Process deduction — "what's the hidden sequence?" |
| Memory Match Blitz | YES | Tool photo pairs, material samples |
| Reaction Chain | LIMITED | Process sequences (cooking steps, sewing sequence) |
| Word Ladder Climb | NO | Language game, not Texnologiya fit |
| Puzzle Lock (Sliding) | YES | Ordering tasks (tool use sequence, recipe steps) |
| Blackjack 21 | NO | Gambling theme inappropriate |
| Territory Conquest | NO | Geography fit, not Texnologiya |
| Escape Room | YES | 4 locks, 5-min limit, workshop/kitchen-themed |
| Bridge Builder | LIMITED | Engineering design — save for G8+ Physics |
| Minefield Navigator | NO | Stress-inducing for G5 |

---

## §9. Notebook Capture — Texnologiya Task Pool

Notebook Capture (Universal §6.8) is the **highest-leverage mechanic** for Grade 5 Texnologiya. Use in **1 of every 2 sessions minimum.**

| Task type | Example prompt |
|---|---|
| **Tool identification drawing** | *"Daftaringga 3 ta duradgorlik asbobini chiz va nomini yoz: arra, iskana, rubanok."* |
| **Process flow diagram** | *"Salat tayyorlash tartibini 5 qutida chiz: yuvish → to'g'rash → aralashtirish → bezash → tortiq qilish."* |
| **Design sketch** | *"Qush uyasi loyihasini chiz. Uzunligi, kengligi va balandligini belgila. Kirish teshigi qayerda bo'ladi?"* |
| **Stitch pattern** | *"Kashta chok namunasi: 5 ta chok chiz va har birining yo'nalishini strelka bilan ko'rsat."* |
| **Material comparison** | *"Yog'och, polimer va gazlamani taqqosla. Har birining 2 ta xususiyatini yoz."* |
| **Safety checklist** | *"Duradgorlik ustaxonasida 5 ta xavfsizlik qoidasini yoz. Nima uchun har biri muhim?"* |
| **Pattern design** | *"Fartuk uchun bezak naqshini chiz. Qaysi ranglardan foydalanasan? Nima uchun?"* |
| **Energy flow diagram** | *"Charvak SESda suv elektr energiyasiga qanday aylanishini 4 bosqichda chiz."* |

**AI vision evaluation rubric:** Lenient on artistic skill, **strict on conceptual accuracy**. A child's stick-figure drawing of "measure → mark → cut → sand → finish" is a CORRECT woodworking process even if it's not pretty. Safety checklists must be conceptually complete.

**Latency:** ≤10 sec Tier 3 vision processing, with human fallback if exceeded.

**Accessibility:**
- Visually impaired → audio task substitute (describe the tool/process verbally)
- Motor disability → teacher toggle OFF
- No notebook → in-app sketch (max 80% XP per UNIFIED §6.8)

---

## §10. Anti-Cheat Tuning for Grade 5 Texnologiya

| Rule | Universal | Grade 5 Texnologiya |
|---|---|---|
| Speed anomaly threshold | varies | **Be lenient** — kids click fast or stare at diagrams for minutes |
| Length anomaly | varies | Don't expect long typed answers — short sentences normal |
| Paste detection | enabled | **Keep enabled** (mother might be helping by typing) |
| Vocabulary jump | enabled | Calibrate against Lexile 830–1010 baseline + technical terms |
| Verdict ladder | 0=CLEAN, 1=MONITOR, 2=SOFT_WARNING, 3+=TEACHER_ALERT | Same |
| Soft warning language | not specified | **NEVER blame the child.** Frame as *"Biz X ni payqadik — hammasi yaxshimi?"* |
| **Mother-helping reality** | not addressed | Add TEACHER_NOTE: *"For Texnologiya Service track, mother helping with cooking/sewing tasks is EXPECTED and pedagogically appropriate — not cheating."* |
| **Safety question monitoring** | not specified | **Elevated scrutiny on safety questions** — any wrong safety answer triggers immediate scaffold regardless of anti-cheat verdict |

---

## §11. Cultural and Regional Anchors

### 11.1 Always-Include List

- **Names** (rotate): Aziza, Bekzod, Gulnora, Sardor, Malika, Jasur, Dilnoza, Otabek, Farrux, Nodira
- **Places**: Tashkent, Samarkand, Bukhara, Khiva, Fergana, Margilan (textile center), Shakhrisabz, Pamir, Aral Sea, Charvak reservoir, Chimgan mountains
- **Foods**: plov, non, somsa, choy, mastava, qaynatma sho'rva, lag'mon, manti
- **Crafts**: kashtachilik (embroidery), atlas/adras (ikat fabric), kulolchilik (pottery), yog'och o'ymakorligi (wood carving)
- **Materials**: paxta (cotton), ipak (silk), yog'och (wood — terak, yong'oq, dub), jun (wool)
- **Currency**: so'm
- **Makers/Craftspeople**: Uzbek woodcarvers (Khiva masters), Margilan silk weavers, Shakhrisabz embroiderers, Tashkent engineers, local artisans
- **Historical figures**: Al-Khwarizmi (mathematical foundations of design), Ulugh Beg (astronomical instruments as engineering), local ustoz (master craftsperson) traditions

### 11.2 Avoid

- Direct comparisons to Western lifestyles
- Pork or alcohol references
- Politically sensitive topics
- Anything implying the child's family is poor or struggling
- Overly industrial/urban contexts that rural students can't relate to
- Dangerous machinery descriptions without explicit safety framing

---

## §12. Assessment, Scoring & Escalation

### 12.1 Pass Threshold

- **60% minimum** to pass session (G5 override)
- Below 60% → **Duolingo Mode** triggers automatically
- **Safety questions: ZERO tolerance** — wrong safety answer = immediate scaffold + re-ask, regardless of overall score

### 12.2 Score → Reward Mapping

| Score | Rating (Uzbek) | Reward |
|---|---|---|
| 100% | *Mukammal!* | Confetti, max XP, title: *"Usta"* (Master craftsperson) — effort-framed |
| 90–99% | *A'lo!* | Full XP + streak fire animation |
| 80–89% | *Juda yaxshi!* | First-time-80%+ bonus XP |
| 60–79% | *O'tdi!* | Standard XP, repass offered (max 2 attempts) |
| <60% | *Hali emas* (never "Failed") | Duolingo Mode, 0 XP this attempt |

**Avatar/cosmetic items:** earned only via competence thresholds — never purchasable. Texnologiya-specific earnables: tool badges, craft frames, material collection items.

### 12.3 Duolingo Mode (<60% Pass)

1. Identify wrong questions
2. Re-present with additional scaffolding (worked example + hint exposed)
3. Reduce difficulty by 1 tier
4. Repeat until 60% achieved
5. **Auto-flag teacher dashboard after 3 consecutive failed sessions on the same standard**

### 12.4 Answer Checking (Dual Pathway)

| Task type | Method | Latency |
|---|---|---|
| MC, Tile Match, Sentence Fill, ordering, binary | Tier 1 rule-based exact match | <100 ms |
| Open reasoning (RLC, Boss explanations, Reflection) | Tier 3 AI semantic evaluation | ≤5 sec, human fallback if >10 sec |
| Notebook Capture (sketches, diagrams) | Tier 3 vision rubric scoring | ≤10 sec, human fallback |

---

## §13. AI Tier Strategy (Cost-Aware)

Inherits UNIFIED §13 budget targets ($3–5/student/year).

| Phase | Tier | Why |
|---|---|---|
| Session 0-A Theme Preview | T2 | Personalized framing per student profile + track |
| Session 0-B Flash Cards | T1 | Pre-generated per chapter |
| Memory Sprint | T1 | Pre-generated MC/Tile Match items |
| Story Mode | T1 (scripted media + checkpoints) | Static maker narratives + scripted gates |
| Game Breaks | T1 | Pre-generated game pools per chapter |
| Real-Life Challenge | T2 | Multi-path reasoning evaluation, adaptive prompts |
| Consolidation | T1 + T2 | Standard pool + flow-state adjustment |
| Final Boss | T2 normally; **T3 generative on failure only** | Socratic re-teach + question regeneration |
| Reflection | T2 | One AI-tailored prompt per session |
| Notebook Capture | T3 vision | Rubric-driven scoring |
| Did You Know facts | T2 | Curated/generated theme-aware insights |

**Cost note — Notebook Capture budget impact:** At 1-in-2 sessions × ~45 sessions/year = ~22 Tier 3 vision calls per student/year. At ~$0.02 per vision call (current pricing), this adds **~$0.44/student/year** for vision specifically. Combined with other Tier 2/3 phases, full per-student annual Texnologiya cost projects to **~$1.80–2.40**, comfortably within the universal $3–5 envelope. Re-validate if vision pricing changes or Notebook frequency increases.

---

## §14. Teacher Overrides

### 14.1 Allowed

- Session mode (Standard 35–45 / Extended 45–60)
- Track assignment (Technology & Design OR Service)
- Boss HP modifier 50–150%
- Difficulty floor (student PISA ±1)
- Game pool selection (Auto / Manual)
- RLC required/optional (default: required for Texnologiya)
- Notebook Capture frequency

### 14.2 Cannot Override

- 7-phase structure
- Sessions 0-A and 0-B (always present)
- Boss is mandatory
- Stranger Test on Story Mode
- `transition_skill` tag requirement
- 60% pass threshold
- Banned mechanics list (§4.3)
- Cultural framing (Uzbek language, anchors)
- Safety question double-weight scoring
- Track-aware content delivery

---

## §15. Tagging Schema (per UNIFIED §16)

```json
{
  "task_id": "UZ-TEX-5-WOOD-03-T07",
  "textbook_ref": {
    "book": "Texnologiya 5-sinf (Tohirov, Mirahmedova, Shamsiyeva, 2020)",
    "chapter": 2,
    "section": "2.1",
    "pages": [30, 31],
    "track": "tech_design"
  },
  "standard_ref": {
    "primary": "UZ-TEX-5-WOOD-03",
    "alias": "TEX.5.2.1.3"
  },
  "pisa_ref": {
    "domain": "Science",
    "sub_domain": "Physical systems — materials and tools",
    "level_target": 2,
    "transition_skill": "L1→L2: identify tools and explain their purpose",
    "technical_reasoning_level": 2
  },
  "blooms_level": "Understand",
  "game_mechanic": "tile_match",
  "phase": "game_break",
  "prompt_uz": "Quyidagi asboblarni mos vazifalariga moslashtiring: arra — kesish, iskana — silliqlash, rubanok — tekislash.",
  "expected_uz": "Arra → Yog'ochni kesish, Iskana → Teshik ochish/yoyish, Rubanok → Yog'och sirtini tekislash.",
  "evaluation_tier": 1,
  "estimated_time_sec": 45,
  "is_safety_critical": false
}
```

---

## §16. Content Production Checklist

For each of the ~21–24 sessions (per track), content team must produce:

- [ ] Theme Preview 8-panel deck (Tier 2 prompt + assets) — Lexile 830–1010L, second-person Uzbek, track-specific
- [ ] Flash Card pool: 5–7 cards (Concept/Rule/Definition; visual mandatory — tool photos, material samples)
- [ ] 30–50 Memory Sprint items (mixed Tile Match/MC/Sentence Fill, spaced retrieval, safety items prioritized)
- [ ] 1 Story Mode arc (3 segments × 90 sec) with maker/craftsperson narrative + 2 checkpoint sets, Stranger Test passed
- [ ] 6–9 Game Break activities across 3+ mechanics per slot rules
- [ ] 1 Real-Life Challenge case (first-person expert + Uzbek context + safety judgment + inquiry hook)
- [ ] 1 labeled diagram (default Phase 5) OR Memory Palace (workshop/kitchen walkthrough alternative)
- [ ] 1 Sub Boss Easy + 1 Sub Boss Medium + 1 Sub Boss Hard question pool — each with worked solution + hints + Common Errors
- [ ] 1 Big Boss pool (cross-session, 3 weakest standards)
- [ ] Reflection prompt bank (3 accuracy buckets + 3 universal)
- [ ] 3 Did You Know facts (theme-aware, age-appropriate, craft/tech-themed)
- [ ] All items dual-coded (`UZ-TEX-5-...` + alias)
- [ ] All items carry `transition_skill` from §3 list
- [ ] All items tagged with correct `track:tech_design` or `track:service`
- [ ] Notebook Capture task (1 in every 2 sessions)
- [ ] Safety questions identified and marked `is_safety_critical: true`

**Total estimated content per session:** ~80–120 task units. **Total for Grade 5 Texnologiya (~45 sessions across both tracks):** ~3,600–5,400 task units.

---

## §17. Sample Chapter Walkthrough — Bob 2.1 "Yog'ochga Ishlov Berish" (Woodworking), Session: Asboblar (Tools)

This is the **reference implementation**. Every other chapter session should match this shape.

### 17.1 Session Metadata

| Field | Value |
|---|---|
| Bob | 2.1: Yog'ochga ishlov berish (Woodworking) |
| Section | Asboblar va ularning vazifalari (Tools and their purposes) |
| Textbook pages | 24–30 |
| Track | Technology & Design |
| Standard ref | `UZ-TEX-5-WOOD-02` / `TEX.5.2.1.2` |
| PISA target | Science L2, TR-L2 |
| Bloom's coverage | Understand, Apply (with light Remember warm-up in P1) |
| Transition skill | `L1→L2: identify tools and explain their purpose` |
| Total session time | 38 min (incl. 0-A + 0-B) |
| Mode | Standard |

### 17.2 Pre-Homework

**Theme Preview (8 panels, ~3 min, student-paced):**

1. **Summary** — *"Yog'ochga ishlov berish uchun turli asboblar kerak. Har bir asbobning o'z vazifasi bor: kesish, silliqlash, tekislash, teshik ochish."*
2. **Better Explanation** — *"Asbob — bu sening qo'lingni kuchliroq qiladigan narsa. Qo'ling bilan yog'ochni sindira olmaysan, lekin arra bilan kesishing mumkin."*
3. **Examples** — Photo of arrа (saw) cutting wood, rubanok (plane) smoothing a board, iskana (chisel) carving a detail — each with arrows
4. **Real-Life Research** — *"Xiva va Buxoroda yog'och o'ymakorligi ming yillik an'ana. Ustalar avlodan-avlodga asbob ishlatish sirini o'tkazib kelishgan."*
5. **Personal Hook** — *"Sen hech qachon bobongiz yoki dadangiz biror narsa yasaganini ko'rganmisan?"*
6. **Why This Matters** — *"Asboblarni to'g'ri tanlash va xavfsiz ishlatish — hayotingda kerak bo'ladigan ko'nikma. Uyda rafka osish, stul tuzatish — hammasi shundan boshlanadi."*
7. **Industry Application** — *"Duradgorlar uy, mebel, eshik yasaydi. Me'morlar bino loyihalashtiradi. Muhandislar mashina qismlarini yaratadi."*
8. **Additional Materials** — Video of a Khiva woodcarver at work; 360° photo of a school workshop; Russian tool glossary

**Flash Cards (~2 min, 6 cards):**

| # | Front | Back | standard_ref | TR | transition_skill |
|---|---|---|---|---|---|
| 1 | 🔪 **Arra** (saw) | Yog'ochni kesish uchun ishlatiladi. Tishlari yog'ochni mayda qilib kesadi. | `UZ-TEX-5-WOOD-02-FC1` | TR-L1 | identify tools and explain their purpose |
| 2 | 🔨 **Rubanok** (plane) | Yog'och sirtini tekislash uchun. Pichoq ingichka qatlamni oladi. | `UZ-TEX-5-WOOD-02-FC2` | TR-L1 | identify tools and explain their purpose |
| 3 | 🔧 **Iskana** (chisel) | Yog'ochda o'yma naqsh va teshiklar qilish uchun. | `UZ-TEX-5-WOOD-02-FC3` | TR-L1 | identify tools and explain their purpose |
| 4 | 📏 **Chizg'ich va qalam** | O'lchash va belgilash — har qanday ishning birinchi qadami. | `UZ-TEX-5-WOOD-02-FC4` | TR-L1 | identify tools and explain their purpose |
| 5 | ⚠️ **Xavfsizlik ko'zoynagi** | Ko'zni yog'och chipalaridan himoya qiladi. Har doim taqish shart! | `UZ-TEX-5-WOOD-02-FC5` | TR-L1 (`is_safety_critical: true`) | recognize safety rules and explain why they matter |
| 6 | 🪑 **Duradgorlik dastgohi** | Yog'ochni mahkamlash uchun ish stoli. Ish paytida yog'och siljimasligi kerak. | `UZ-TEX-5-WOOD-02-FC6` | TR-L1 | identify tools and explain their purpose |

→ **Boshlash** button → timer starts.

### 17.3 The 7-Phase Session

**Phase 1 — Memory Sprint (2 min, 6 items):** Tile Match (tool photo ↔ tool name) + MC (safety rules). Pulls 2 items from Bob 1 (modern technology types — interleaving).

**Phase 2 — Story Mode (6 min, 3 × 90 sec segments interleaved with games):**

- **Segment 1 — Problem (90 sec):** *"Sardor maktabning duradgorlik ustaxonasiga birinchi marta kirdi. Devorda turli asboblar osilgan edi. Ustozi dedi: 'Bugun sen oddiy taxta yasaysan. Lekin avval asboblarni tanib olishing kerak.' Sardor hayron bo'lib qoldi — arrаmi, rubanokmi, iskanami — qaysi birini birinchi olish kerak?"*
  - Checkpoint: *"Sardor yog'ochni kesish uchun qaysi asbobni olishi kerak? Nima uchun?"*
- **Game 1 — Tile Match (2 min):** Match 6 tool photos to their names and purposes.
- **Segment 2 — Struggle/Discovery (90 sec):** Sardor arrani oldi, lekin noto'g'ri ushladi. Ustozi tushuntirdi: *"Arrani ikki qo'l bilan ushla. Bir qo'l dastasida, ikkinchi qo'l ustida. Sekin va tekis sur. Shoshilma — uch marta o'lcha, bir marta kes."*
  - Checkpoint: *"Nima uchun 'uch marta o'lcha, bir marta kes' deyishadi?"*
- **Game 2 — Why Chain (2 min, 2 levels max):** Why measure first → what happens if you don't → why accuracy matters
- **Segment 3 — Solution (90 sec):** Sardor to'g'ri o'lchadi, to'g'ri belgiladi, to'g'ri kesdi. Taxtasi tekis va chiroyli chiqdi. Ustozi maqtadi: *"Yaxshi duradgor shunday boshlanadi."*
  - Checkpoint: *"Sardorning birinchi taxtasi nima uchun muvaffaqiyatli chiqdi?"*

**Phase 3 — Game Break finale + Notebook Capture (5 min):** Notebook task — *"Daftaringga 4 ta asbobni chiz: arra, rubanok, iskana, chizg'ich. Har birining yoniga qisqa vazifasini yoz."* AI vision evaluates labels for conceptual correctness; stick figures fully accepted.

**Phase 4 — Real-Life Challenge (4 min):** *"Sen uyda kichik rafka yasamoqchisan. Devorda: arra, bolt, mix, mix qoqadigan bolg'a, chizg'ich, qalam, rubanok, va mixlanadigan taxta bor. Rakfani yasash uchun qaysi 5 ta narsani sanab ber va qanday tartibda ishlatasan?"* with safety checkpoint: *"Ishni boshlashdan OLDIN nima qilishing kerak?"* Justification required; AI evaluates reasoning.

**Phase 5 — Consolidation (3 min):** **Labeled diagram recall** — show workshop tool board from textbook with labels removed; student drags 6 tool names back into place.

**Phase 6 — Sub Boss Medium (7 min, 50 HP, 5 questions):**

Each question carries: `standard_ref`, `pisa_level`, `tr_level`, `transition_skill`, `is_safety_critical`.

| # | Question | Type | Diff | Damage | Tags |
|---|---|---|---|---|---|
| 1 | *"Arra qaysi materialni kesish uchun ishlatiladi?"* | MC | easy | −10 | `WOOD-02-B1` · Science L1 · TR-L1 · *identify tools/materials* · safety: false |
| 2 | *"Yog'ochdan buyum yasash tartibini to'g'ri joylashtir: o'lchash → belgilash → kesish → silliqlash → yig'ish."* | Ordering | med | −15 | `WOOD-02-B2` · Science L2 · TR-L2 · *sequence steps in a making process* · safety: false |
| 3 | *"Duradgorlik ustaxonasida ishlashdan OLDIN qaysi xavfsizlik qoidalarini bajarish SHART? 3 tasini yoz."* | Open reasoning | med | −15 | `WOOD-02-B3` · Science L2 · TR-L2 · *recognize safety rules* · **safety: true (2× weight, zero tolerance)** |
| 4 | *"Nima uchun rubanok yog'och sirtini tekislaydi? Arradan farqi nima?"* | Open + compare | med | −5 | `WOOD-02-B4` · Science L2 · TR-L2 · *select appropriate tools for a task* · safety: false |
| 5 | *"Agar senda rubanok bo'lmasa, yog'och sirtini qanday tekislashing mumkin? Bitta alternativa taklif qil va sababini tushuntir."* | Open + creative | hard | −5 | `WOOD-02-B5` · Creative Thinking + Science L2 · TR-L3 · *design a solution using available materials* · safety: false |

Each Q has worked solution + 2-3 hints + Common Errors. Combo bonus 3-in-row → 2× next damage. Hint tax −5 HP. Max 3 attempts with growth-mindset framing.

**Phase 7 — Reflection (2 min):** Tier 2 generates 1 prompt by accuracy bucket. Min 1 sentence. Effort-praise framing only.

**Did You Know facts at phase transitions:**
1. *"Did you know? The word 'duradgor' comes from Persian — 'dura' means tree, 'gar' means worker. A tree-worker!"*
2. *"Did you know? A sharp saw cuts BETTER than a dull one — and is actually SAFER because you don't have to push as hard."*
3. *"Did you know? Khiva's woodcarvers can make patterns so detailed that a single door takes 3 months to carve."*

### 17.4 Post-Session

Per §12.2 score → reward mapping. Auto-flag teacher if 3 consecutive sub-60% sessions on this standard.

---

## §18. Open Questions / Things to Validate Before Production

1. **Two-track assignment operational logic** — §0 #1 says "teacher assigns track per student"; the *implementation* (teacher dashboard UX, school-wide default, mid-year switch handling) needs engineering spec.
2. **Notebook Capture 1-in-2 frequency** — verify with teachers given practical nature of subject; engineering needs to confirm Tier 3 vision throughput at scale.
3. **Did You Know fact pool** — needs Uzbek-language curation for crafts, tools, makers (~60–80 facts).
4. **Uzbek craftsperson content accuracy** — verify Khiva woodcarvers, Margilan weavers, Shakhrisabz embroiderers material with cultural reviewer.
5. **Boss questions for embroidery/crafts** — how to assess "quality" of a stitch pattern digitally? AI vision rubric needed for Service track Notebook Capture grading.
6. **Adaptive scaffolded fallback for below-L2 students** — needs explicit specification (mirrors Science G5 §18 #7 — likely a shared fix across all G5 frameworks).
7. **Bob 3 (Energy) combined track delivery** — §2 chapter map declares it combined; confirm with curriculum specialist that BOTH tracks really cover Bob 3 in equal depth.
8. **"Duradgor" etymology fact** — verify Persian roots before shipping the §17.4 Did You Know (or replace with verified alternative).
9. **Track 2 PISA primary = Creative Thinking** (per §3 update) — confirm with PISA framework specialist that Service-track tagging is defensible against PISA 2022 Creative Thinking rubric.
10. **Mythical Boss HP cap** — UNIFIED §5.6 sets 80–100 HP for Mythical tier; confirm §6.6 row for L3+ top decile aligns and isn't double-counting.

---

## §19. Production Handoff

This framework is the **input contract** for the content team / openclaw when producing per-section homework lessons.

**What every produced session must do:**
1. Match the **shape** of §17 (Theme Preview → Flash Cards → 7 Phases → Post-session)
2. Apply **all** parameters from §4 (timing, difficulty, formats)
3. Use **Uzbek language only** for student-facing text
4. Include **at least one Notebook Capture task** in every 2nd session
5. Include **at least one Did You Know fact** per phase transition
6. Use **first-person Expert POV** for every Real-Life Challenge
7. Use **real Uzbek craftspeople / makers / contexts** wherever possible
8. Include **at least one safety question** in every Boss fight
9. Tag every item with `standard_ref`, `pisa_level`, `transition_skill`, `blooms_level`, `track` per §15
10. Mark safety-critical items with `is_safety_critical: true`
11. Generate boss questions to hit the **75–85% expected success rate**
12. Validate against §18 Open Questions before deploying

---

## §20. Versioning and Review

- **v3.1 (2026-04-08, post-audit)** — Claude audit pass against Universal Specs. 8 fixes:
  - **§0** added decision #18 (Personal Hook track-matching)
  - **§3** rewritten with track-aware triple-tagging (Track 1 = Science primary, Track 2 = Creative Thinking primary, Science conditional only for genuinely scientific content)
  - **§5.1** Personal Hook now mandatorily track-aware (Track 1 = paternal anchor, Track 2 = maternal anchor)
  - **§13** added Tier 3 vision cost projection (~$0.44/student/year for Notebook Capture, total ~$1.80–2.40/student/year, fits universal budget)
  - **§17.1** Bloom's claim corrected from 4 levels to 2 (Understand, Apply with light Remember warm-up)
  - **§17.2** Flash Cards now carry per-item `standard_ref` + TR level + transition_skill columns
  - **§17.3** Boss questions now carry per-item tags including `is_safety_critical` flag
  - **§18** removed items #2 and #7 (already resolved in §0 #14 and #17 respectively); soften duradgor etymology to "verify before shipping"; added Mythical HP cap verification
- **v3.0 (2026-04-08)** — first Texnologiya framework (Qwen). Built from scratch using Science Merged Framework as template. 20 sections.
- **Textbook source:** Texnologiya 5-sinf, Tohirov/Mirahmedova/Shamsiyeva, "Sharq" NMK, 2020, 240pp, ISBN 978-9943-5997-4-1.
- **Reviewers needed:** product/pedagogy lead, 1+ Uzbek Texnologiya teacher (both tracks), content team lead, safety officer.
- **Next revision trigger:** after 5+ chapters of Grade 5 Texnologiya homework are produced and stress-tested with real students.
- **Sibling adaptations to be created later, same template:**
  - `grades/5/uz/tech_design/` (Track 1 standalone)
  - `grades/5/uz/service/` (Track 2 standalone)
  - `grades/6-11/uz/technologiya/` (older grades, subject splits)
  - Russian-language siblings under `grades/5/ru/`

---

**End of framework.** Single source of truth for Grade 5 uz Texnologiya homework production going forward.
