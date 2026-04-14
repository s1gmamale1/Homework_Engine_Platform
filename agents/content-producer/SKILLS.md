# SKILLS — Production Pipeline

---

## Assignment Handling

**Specific chapter:** Produce one docx for that chapter.
**Subject, no chapter:** Produce docx for EVERY chapter sequentially. One file per chapter.
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
   Write: The actual docx, phase by phase

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

This is your **closest guide**. It tells you:
- Grade-band progression tables (what G5 vs G6 vs G9 looks like)
- Terminology density per session
- Specific game mechanics and slot priority
- Boss parameters (HP overrides, hint tax, MC rules)
- Phase-by-phase tuning (what's different for THIS subject)
- Good/Bad examples with concrete content
- **If the Subject Framework overrides the Family Doc, follow the Subject Framework**

### 📖 READ NOW — Textbook TOC
`textbooks/grade_{N}/`

Scan the table of contents. Understand chapter structure. Count chapters if doing whole book.

### After Pre-Flight You Should Know:
- Which 3 games to use in Phase 3 (subject's mechanic emphasis → slot priority)
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
| Core concept explanation | Phase 2 Story Mode (3 segments, CPA) |
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

### 📖 READ IF NEEDED — National Pride Data
- `standards/system/narrative/quotes_database.json` — for Phase 0-A gate quote
- `standards/system/narrative/task_injections.json` — for Phase 4 Wise Status injection
- `standards/system/narrative/Bilarmidingiz_faktlar.md` — for between-phase "Did You Know" facts

### ✍️ WRITE — The Docx

Output file: `{Subject}_Grade{N}_Ch{N}_{lang}.docx`

Write each phase in order. For each phase, follow the template from SOUL.md (session structure table) + the UNIFIED spec section you just read + the Subject Framework's phase-specific tuning.

**Phase-by-phase checklist:**

| Phase | Write | Key Rules |
|---|---|---|
| 0-A | 8 components, gate quote, BOST goal | Visual-first, first-person POV ("sen"), no quiz. Store BOST learning goal for Phase 7. |
| 0-B | Flash card deck | 5-7 cards max (G5). Each = concept WITH visual. 1 Common Mistake card. Ends with [ MENING UY VAZIFAMNI BOSHLASH ]. |
| Header | Metadata table | Fan, Sinf, Darslik, Til, Bob, Standart kod, PISA target, Bloom's, Boss HP, Vaqt |
| 1 | 5-8 warm-up items + answers | CURRENT chapter. Tag each: `[Bloom: L1 \| PISA: L1]`. ≤2 min. |
| 2 | 3 CPA segments + 3 checkpoints + answers | Each segment MUST label: Muammo→Kurash→Kashfiyot→Yechim. Concrete→Pictorial→Abstract. Tag checkpoints: `[Bloom: L1-L2 \| PISA: L1-L2]`. |
| 3 | 3 games × 4-6 items + answers | ≥1 Interactive, ≥2 Default. Tag each: `[Bloom: L1-L3 \| PISA: L1-L2]`. |
| 4 | 1 scenario + W5H + 3 questions + answers | Modern professional. First-person. W5H mandatory G5-6. ~30% Wise Status. Tag: `[Bloom: L3-L4 \| PISA: L2-L3]`. (Ijtimoiy: Historical Projection.) |
| 5 | Formula-visual warmup (45s) + 1 Buzan exercise | Select by content type (hierarchical→Radiant, etc.). Explicitly verify SMASHIN' SCOPE. |
| 6 | 3-5 boss Qs + hints + rubric + answers | HP from Subject Framework. 40/40/20. Tag: `[Bloom: L3-L5 \| PISA: L2-L4 \| Damage: -XX HP]`. At least 1 word problem + 1 visual model Q. |
| 7 | Summary + 3 prompts + BOST recall + closing | **MUST resurface BOST goal from Phase 0-A**: "Bugun sen [goal] ni bilmoqchi eding. Bildingmi?" Spaced rep schedule. Third Renaissance closing (≥60% only). |

**CRITICAL: Every question/item must carry `[Bloom: LX | PISA: LX]` inline tag. A question without a tag is incomplete.**

---

## Step 5: Log + Next Chapter

### ✍️ UPDATE — STATUS.md

After every docx, update STATUS.md in the output directory:

```markdown
## Production Log

| # | File | Chapter | Status | Timestamp | Issues |
|---|------|---------|--------|-----------|--------|
| 1 | Matematika_Grade5_Ch1_uz.docx | Ch1 Natural sonlar | ✅ Done | 2026-04-15 14:22 | None |
| 2 | Matematika_Grade5_Ch2_uz.docx | Ch2 ... | 🔄 In progress | — | — |

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
