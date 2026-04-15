# SKILLS — Production Pipeline

---

## ⚠️ FRAMEWORK COMPLIANCE — READ THIS FIRST

**You are a BUILDER, not a checkbox ticker.** The frameworks are your construction blueprints. Follow them to the letter.

**Authority chain (highest → lowest):**
1. **UNIFIED-Buzan** — defines WHAT each phase must contain (rules, structure, constraints, timing)
2. **Subject Framework** — defines HOW to build each phase for this specific subject (construction recipes, examples, game item formats, panel guides)
3. **Family Framework** — defines family-level patterns that subjects inherit
4. **This file (SKILLS.md)** — defines WHEN to read what and the production pipeline

**STRICT RULES:**
- The Subject Framework contains **construction recipes** for every phase. These are NOT suggestions — they are mandatory build instructions. Follow them exactly.
- When building Phase 3 games: read the Game Mechanic Doc for each game, THEN apply the Subject Framework's construction recipe on top. Every item must use the FULL mechanic — tile counts, node counts, difficulty progression, interaction model. **Bare numbers or 1-liner items = rejected output.**
- When building Phase 0-A panels: the Subject Framework has a Panel Construction Guide table. Each panel has a min depth (8-10 or 5-10 sentences). **1-2 sentence panels = rejected output.**
- When building Phase 1: the Subject Framework specifies format mixing rules and per-format construction recipes. **All-MC sprints = rejected output.** You MUST mix at least 2 of the 3 approved formats (MC, True/False, Yes/No/Not Given). **NEVER use fill-in-the-blank, gap-fill, speed match, drag-and-drop, or any format requiring typing in Phase 1. These are BANNED. Tap-only.**
- When building ANY phase: if the Subject Framework gives a construction recipe, follow it. If it gives examples of GOOD vs BAD content, study them. If it specifies difficulty progression (L1→L2→L3), apply it.
- **Every aspect of every mechanic must be utilized.** You are not listing items — you are building interactive educational content where every game has context, scenarios, interaction, feedback, and difficulty scaling.

**If you produce shallow, checklist-style output that ignores the construction recipes in the Subject Framework, your output is non-compliant and must be redone.**

---

## Assignment Handling

**Specific chapter:** Produce one .md for that chapter.
**Subject, no chapter:** Produce .md for EVERY chapter sequentially. One file per chapter.
**Unclear:** Ask: "Specific chapters or the whole book?"

---

## Pipeline Overview

```
STEP 1: PRE-FLIGHT (once per subject)
   Read: Family Doc (FULL) + Subject Framework (FULL) + Textbook TOC
   Result: You know mechanics, boss format, grade-band rules, chapter list

STEP 2: CHAPTER EXTRACTION (per chapter)
   Read: Textbook chapter section by section
   Result: You have the raw content mapped out

STEP 3: CONTENT MAPPING (per chapter)
   Map extracted content → session phases using Family + Subject framework knowledge
   Result: You know what goes where (which concepts in Story Mode, which in games, etc.)

STEP 4: DEEP READ + WRITE (per chapter)
   Read: UNIFIED-Buzan §5.1-§5.7 (the specific phase specs you're about to write)
   Read: Game Mechanic Docs for the 3 games you'll use
   Read: National Pride data (quotes_database.json, task_injections.json) if needed
   Write: The actual .md file, phase by phase

STEP 5: LOG
   Update STATUS.md
   Move to next chapter → back to Step 2
```

---

## Step 1: Pre-Flight (Once Per Subject)

### 📖 READ NOW — Family Doc (FULL)
`standards/library/subject-family/{Family}/{Family}_Subject_Family_Framework.md`

This tells you:
- Primary and secondary mechanics for this family
- Games to AVOID
- Boss format
- Good/Bad production examples
- Universal production rules adapted for this family
- Phase 5 Buzan technique recommendations

### 📖 READ NOW — Subject Framework (FULL)
`standards/library/subject-family/{Family}/{Subject}/{Subject}_Subject_Framework.md`

This is your **closest guide** and your **primary build instruction set**. It tells you:
- Grade-band progression tables (what G5 vs G6 vs G9 looks like)
- Terminology density per session
- Specific game mechanics and slot priority
- Boss parameters (HP overrides, hint tax, MC rules)
- **Phase 0-A Panel Construction Guide** — how to write each of the 8 panels for this subject
- **Phase 1 format mixing rules** — which formats to use, how to construct each, with examples
- **Phase 3 Game Construction Recipes** — how to build items for each game mechanic (tile content, node content, difficulty progression, good/bad examples)
- **Phase 7 Reflection guide** — session summary, metacognitive prompts, BOST recall, closing line
- Good/Bad examples with concrete content
- **If the Subject Framework overrides the Family Doc, follow the Subject Framework**

**⚠️ The Subject Framework's construction recipes are your BUILD instructions. UNIFIED tells you WHAT to include. The Subject Framework tells you HOW to build it. You must follow BOTH.**

### 📖 READ NOW — Textbook TOC
`textbooks/grade_{N}/`

Scan the table of contents. Understand chapter structure. Count chapters if doing whole book.

### After Pre-Flight You Should Know:
- Which 3 games to use in Phase 3 (subject's mechanic emphasis → slot priority)
- **How to BUILD items for each game** (construction recipes from Subject Framework)
- **How to write each Phase 0-A panel** (Panel Construction Guide from Subject Framework)
- **How to mix Phase 1 formats** (mixing rules + per-format recipes from Subject Framework)
- **How to write Phase 7 Reflection** (reflection guide from Subject Framework)
- Boss format and any HP/hint overrides for this grade
- Phase 4 format (Real-Life Challenge vs Historical Projection)
- Grade-band expectations (terminology count, Bloom's range, production level)
- Total chapter count and content scope

**Do NOT re-read Family Doc and Subject Framework for every chapter.** Only re-read if you compacted context and lost the knowledge.

---

## Step 2: Chapter Extraction (Per Chapter)

### 📖 READ NOW — Textbook Chapter
Read the assigned chapter fully. Extract:
- **Core concepts** introduced in this chapter
- **Key terminology** (new words, definitions)
- **Formulas/rules** (if applicable)
- **Worked examples** in the textbook
- **Figures/diagrams** described
- **Prerequisites** — what prior knowledge does this chapter assume?

Organize your extraction into a mental map: which concepts are the "main idea" vs "supporting detail."

---

## Step 3: Content Mapping (Per Chapter)

Using your Family + Subject framework knowledge, map the extracted content:

| Content Piece | Maps To |
|---|---|
| Core concept explanation | Phase 2 Story Mode (ONE continuous story with CPA woven in) |
| Key terminology | Phase 0-B Flash Cards + Phase 1 Memory Sprint warm-up |
| Formulas/rules | Phase 0-B Flash Cards |
| Practice-worthy skills | Phase 3 Games (pick 3 from subject's mechanic emphasis) |
| Real-world application angle | Phase 4 Real-Life Challenge (or Historical Projection) |
| The 5 most important takeaways | Phase 5 Consolidation mnemonic |
| Assessment-worthy questions | Phase 6 Boss (Easy/Medium/Hard distribution) |

**Decide your 3 Phase 3 games now.** Check subject framework's slot priority table. Verify: ≥1 Interactive, ≥2 Default.

---

## Step 4: Deep Read + Write (Per Chapter)

NOW you read the actual source docs for the phases you're writing.

### 📖 READ NOW — UNIFIED-Buzan Phase Specs
`standards/framework/NETS-Homework-Engine-UNIFIED-Buzan.md`

Read the sections you need:
- **§4.4** — Theme Preview (Phase 0-A) requirements (8 components)
- **§4.5** — Flash Cards (Phase 0-B) requirements
- **§5.1** — Memory Sprint (Phase 1) formats, scoring, adaptation
- **§5.2** — Story Mode (Phase 2) arc structure, CPA, checkpoints
- **§5.3** — Game Breaks (Phase 3) dual-catalog rule, Von Restorff anchor
- **§5.4** — Real-Life Challenge (Phase 4) POV rules, W5H scaffold, Wise Status
- **§5.5** — Consolidation (Phase 5) Buzan techniques, SMASHIN' SCOPE
- **§5.6** — Final Boss (Phase 6) HP, damage, hints, stars
- **§5.7** — Reflection (Phase 7) TEFCAS, BOST goal recall

You don't need to read all of these every time — read the ones you're less certain about. After the first chapter, you'll have them in context.

### 📖 READ NOW — Game Mechanic Docs (for your 3 chosen games)
`standards/system/games/Game_Mechanics_Docs/{NN}_{game}/`

Read the specific game docs for the 3 games you selected. These tell you the exact content format — how to structure items for Tile Match vs Codebreaker vs Reaction Chain, etc.

**Then apply the Subject Framework's Game Construction Recipes on top.** The Game Mechanic Doc tells you the mechanic. The Subject Framework tells you what content goes INTO that mechanic for this subject. You need BOTH. A game item without full context, scenarios, difficulty progression, and interaction detail is incomplete.

### 📖 READ IF NEEDED — National Pride Data
- `standards/system/narrative/quotes_database.json` — for Phase 0-A gate quote
- `standards/system/narrative/task_injections.json` — for Phase 4 Wise Status injection
- `standards/system/narrative/Bilarmidingiz_faktlar.md` — for between-phase "Did You Know" facts

### ✍️ WRITE — The Markdown File

Output file: `{Subject}_Grade{N}_Ch{N}_{lang}.md`

Write each phase in order. For each phase, you have THREE layers of instruction:
1. **UNIFIED-Buzan** — the WHAT (rules, structure, constraints)
2. **Subject Framework** — the HOW (construction recipes, examples, item formats)
3. **This checklist** — the minimum acceptance criteria

**⚠️ The checklist below is the MINIMUM. The Subject Framework's construction recipes define the QUALITY. If you only hit the checklist without following the construction recipes, your output will be shallow and non-compliant.**

**Phase-by-phase checklist + construction enforcement:**

| Phase | Write | Key Rules | ⚠️ Construction Source |
|---|---|---|---|
| 0-A | 8 panels (1-5: 8-10 sentences; 6-8: 5-10 sentences), gate quote, BOST goal | Visual + substantive, first-person POV ("Siz" formal — never "sen"), no quiz. Store BOST learning goal for Phase 7. | **Follow Subject Framework's Panel Construction Guide.** Each panel has specific content instructions. 1-2 sentence panels = rejected. |
| 0-B | Flash card deck | 5-7 cards max (G5). Each = concept WITH visual. 1 Common Mistake card. Ends with [ MENING UY VAZIFAMNI BOSHLASH ]. | Subject Framework §3.4 or §Pre-Session. |
| Header | Metadata table | Fan, Sinf, Darslik, Til, Bob, Standart kod, PISA target, Bloom's, Boss HP, Vaqt | — |
| 1 | 5-8 warm-up items + answers | CURRENT chapter. Tap-only: MC, True/False, Yes/No/Not Given. NO typing, NO drag-and-drop, NO open-ended. **MUST mix at least 2 of 3 formats.** Tag each: `[Bloom: L1 \| PISA: L1]`. ≤2 min. | **Follow Subject Framework's format mixing rules + per-format construction recipes.** All-MC = rejected. Each distractor must map to a real student error. |
| 2 | **ONE continuous story** + 3 checkpoints + answers | Write ONE flowing story where the character faces a problem, struggles, discovers the concept, and solves it. Problem→Struggle→Discovery→Solution are INGREDIENTS baked into the narrative — **NOT segments, NOT labels, NOT sections.** Do NOT write "Segment 1", "Muammo:", "Concrete:" etc. CPA for math is woven into the story naturally. 3 IELTS-style comprehension checkpoints after the story. Tag: `[Bloom: L1-L2 \| PISA: L1-L2]`. | **Follow Subject Framework's Story Mode arc table** for subject-specific scenarios, characters, and CPA guidance. The arc table shows INGREDIENTS — use them to build ONE story. |
| 3 | 3 games × 4-6 items + answers | ≥1 Interactive, ≥2 Default. Tag each: `[Bloom: L1-L3 \| PISA: L1-L2]`. | **Follow Subject Framework's Game Construction Recipes.** For EACH game: build the correct number of items, use the specified tile/node content, apply L1→L3 difficulty progression, include context and interaction detail. Bare numbers with no context = rejected. |
| 4 | 1 scenario + W5H + 3 questions + answers | Modern professional. First-person. W5H mandatory G5-6. ~30% Wise Status. Tag: `[Bloom: L3-L4 \| PISA: L2-L3]`. (Ijtimoiy: Historical Projection.) | **Follow Subject Framework's professional role list and construction rules.** |
| 5 | Formula-visual warmup (45s) + 1 Buzan exercise | Select by content type (hierarchical→Radiant, etc.). Explicitly verify SMASHIN' SCOPE. | **Follow Subject Framework's technique selection table.** |
| 6 | 3-5 boss Qs + hints + rubric + answers | HP from Subject Framework. 40/40/20. Tag: `[Bloom: L3-L5 \| PISA: L2-L4 \| Damage: -XX HP]`. At least 1 word problem + 1 visual model Q. | **Follow Subject Framework's Boss design rules and question examples.** |
| 7 | Summary + 3 prompts + BOST recall + closing | **MUST resurface BOST goal from Phase 0-A**: "Bugun Siz [goal] ni bilmoqchi edingiz. Bildingizmi?" Spaced rep schedule. Third Renaissance closing (≥60% only). | **Follow Subject Framework's Phase 7 Reflection guide.** Use the subject's specific metacognitive prompts. Generic prompts = rejected. |

**CRITICAL: Every question/item must carry `[Bloom: LX | PISA: LX]` inline tag. A question without a tag is incomplete.**

**CRITICAL: The Subject Framework's construction recipes are not optional. They define the difference between a checklist output and a properly built homework session. Read them. Follow them. Every aspect of every mechanic must be utilized.**

---

## Step 5: Log + Next Chapter

### ✍️ UPDATE — STATUS.md

After every .md file, update STATUS.md in the output directory:

```markdown
## Production Log

| # | File | Chapter | Status | Timestamp | Issues |
|---|------|---------|--------|-----------|--------|
| 1 | Matematika_Grade5_Ch1_uz.md | Ch1 Natural sonlar | ✅ Done | 2026-04-15 14:22 | None |
| 2 | Matematika_Grade5_Ch2_uz.md | Ch2 ... | 🔄 In progress | — | — |

Total: 1/12 chapters complete
```

Then → back to Step 2 for the next chapter.

---

## Context Management

**At ~90% capacity:**
1. Update STATUS.md with current progress
2. Summarize what you've learned from framework docs (keep the key rules, drop the verbatim text)
3. Compact context
4. Re-read SOUL.md (lean summary, reloads fast)
5. Read STATUS.md to find where you left off
6. If you lost Family/Subject framework knowledge → re-read them (Step 1)
7. Continue from next unfinished chapter (Step 2)

**Never restart from scratch. Never lose progress.**

---

## Red Lines

- Never modify framework documents (standards/ folder)
- Never delete existing files
- Never push to git
- Never access .env or credentials
- Output only to the assigned output_path
- When in doubt, log the issue and continue — never block the pipeline
