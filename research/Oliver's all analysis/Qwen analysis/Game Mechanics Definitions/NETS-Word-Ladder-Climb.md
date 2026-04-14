# NETS Game Mechanic Definition: Word Ladder Climb

**Catalog:** Interactive Catalog Pool — Game #6
**Version:** 1.0 — 2026-04-11
**Status:** Draft → QA Review
**Author:** WordLadderResearcher (ADS-25)
**Parent Task:** [ADS-17] → [ADS-25]

---

## Design Questions — Resolved

Before the 15-section definition, the five open design questions are settled here. Every section below is built on these decisions.

### Q1. Language — Uzbek ladders, English only (CEFR subject), or both depending on subject?

**Decision: Subject-dependent. Two language modes.**

| Subject | Language Mode | Rationale |
|---|---|---|
| English (CEFR) | English-only ladder | The word transformation IS the CEFR vocabulary skill being exercised. Mixing Uzbek defeats the purpose. |
| Uzbek Language / Adabiyot | Uzbek-only ladder | Native morphological awareness in the primary language of instruction. |
| Biology (see Q3) | Uzbek-primary, with transliterated bio-terms as needed | Biology terms in the Uzbek curriculum are a mix of Uzbek and Latin-rooted loan words; Morphological Chain variant handles this. |
| All other PISA-rigorous subjects | Not eligible (see Section 6) | Word Ladder Climb is a language-family mechanic. PISA Math, History, Geography use other Interactive Catalog games. |

There is no "both simultaneously" mode. Each instance of the game runs in one language. Subject eligibility (Section 6) enforces this.

---

### Q2. Ladder rule — change 1 letter per step, or any transformation? Must each intermediate word be a real dictionary word?

**Decision: Two rule modes, linked to subject family.**

| Mode | Where Used | Transformation Rule | Dictionary Constraint |
|---|---|---|---|
| **Classic Letter-Swap Ladder** | English CEFR, Uzbek Language | Exactly 1 letter may be changed per step (substitution only — no insertion, deletion, or rearrangement). | Every intermediate word MUST be a valid word in an approved dictionary (Uzbek NSM dictionary for Uz; Oxford Elementary/Intermediate for English CEFR). Non-words are rejected instantly by the validation engine. |
| **Morphological Chain** | Biology | Each step changes exactly 1 morphological unit: a prefix, a root, or a suffix. The intermediate string does NOT need to be a standalone dictionary word, but MUST be a recognized morphological unit in the content-tagged term bank. | Validated against the Biology term bank (UZ-BIO morpheme registry), not a general dictionary. |

The Classic mode is the default. Morphological Chain is a declared variant that content authors activate in the JSON schema (`"ladder_mode": "morphological"`). The UI presentation differs (see Section 2 — Input Format).

---

### Q3. Biology terminology — "biology terminology" rarely differs by 1 letter. How does this actually work?

**Decision: Keep biology, use Morphological Chain variant. Remove biology from Classic mode.**

Classic 1-letter ladders do not work for biology terms. "MITOSIS" and "MEIOSIS" differ by 2 letters and positions; "CHLOROPLAST" and "CHROMOSOME" are not connectable by single-letter steps. Forcing classic rules onto biology would require contrived 3-letter bio-abbreviations, which would feel fake and fail the Textbook-first principle.

The Morphological Chain solves this legitimately:

**Biology example:** Start = `PHOTO-SYNTHESIS`, Target = `PHOTO-SYSTEM`

| Step | Transformation | What Changed |
|---|---|---|
| PHOTOSYNTHESIS | (start) | — |
| PHOTO + LYSIS | `synthesis` → `lysis` | Changed the suffix/root (both are Greek: "putting together" → "breaking apart") |
| PHOTO + SYSTEM | `lysis` → `system` | Changed the root | 

Each step is gated by a biology question (see Q4). The morphological transformation is tracked separately from the question answer. Students who answer wrong still have to make A step — but the system forces an incorrect-direction step (see Section 9 — Failure/Retry Behavior).

**What biology gets from this mechanic:** Students build morphological awareness of scientific Latin/Greek roots — a documented PISA Reading skill that transfers across science texts. Research: Rastle et al. (2008) shows morphological awareness training improves reading of unfamiliar scientific words by 30-40%.

---

### Q4. Subject question gating — is the subject question separate from the word change?

**Decision: Yes. Fully separate. The question earns the right to move; the student then chooses where to move.**

The two-step flow per rung:

```
RUNG N:
  Step A — QUESTION: System presents a subject question (PISA-calibrated to student's level)
            Student answers.
            ↓ CORRECT: Student earns a "valid move token"
            ↓ WRONG:   System forces a "random move" — system picks the next word/morpheme, not the student

  Step B — MOVE (if correct): Student picks which letter/morpheme to change and what to change it to.
            Validation engine checks: is this a valid word/morpheme? Is it a real step toward the target?
            If the student picks a dead-end word (e.g., correct word, but it blocks all future paths to the target),
            the engine warns: "Sahih so'z, lekin oldindan o'ylang — bu so'zdan manzilga yetish qiyin." ("Valid word, 
            but think ahead — it's hard to reach the target from here.")
            Student can undo once (before confirming the step) — this is free, not a hint.
```

This separation is important:
- The subject question tests **content knowledge** (what the lesson is about)
- The word transformation tests **language/morphological awareness** (the meta-skill of this game)
- Students can win even with imperfect strategy if their content knowledge is strong (they get the tokens; the path is theirs to navigate)
- Students with perfect strategy but weak content knowledge will have random moves inserted, creating noise they must recover from

---

### Q5. Hints / skips budget per ladder?

**Decision: 2 free hints per ladder, 0 skips. Hints are word-direction hints only.**

| Resource | Default | Below-L2 students | Effect | Cost |
|---|---|---|---|---|
| **Hint** | 2 per ladder | 3 per ladder | Reveals which position in the current word is the "best" position to change (not what to change it to). Tier 1 — pre-calculated from the optimal path. | -25% XP from that rung's earned reward |
| **Skip (question)** | 0 | 0 | Not available. The question is the gate. There is no bypass. | — |
| **Undo (move)** | 1 per rung (free) | 1 per rung (free) | Take back a placed word/morpheme choice before confirming. Not a hint — no XP cost, no hint consumed. | Free |

**Rationale for no skip:** The question is the content-learning component. Skipping it breaks the mechanic entirely — the student would just be playing a word game with no subject learning. The game exists to make content practice feel strategic, not to offer a word puzzle with optional education.

---

## Section 1 — Core Loop

The micro-loop of one complete rung (one step up the ladder):

```
START OF RUNG:
┌─────────────────────────────────────────────────────────────────────┐
│  UI: Ladder board shown.                                            │
│  Current word highlighted. Target word shown at top.               │
│  "Rung N of M" counter visible.                                    │
└─────────────────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────────────────┐
│  QUESTION PHASE (subject question)                                  │
│  System presents 1 PISA-calibrated question from current topic.    │
│  Format: MC (G1-4), short open answer (G5+)                       │
│  Timer: 45 seconds                                                 │
└─────────────────────────────────────────────────────────────────────┘
            ↓ (answer submitted)
        ┌──────────────┐
        │ CORRECT?     │
        └──────┬───────┘
      YES      │       NO
       ↓       │       ↓
┌──────────┐   │  ┌─────────────────────────────┐
│ EARN     │   │  │ RANDOM MOVE:                │
│ MOVE     │   │  │ System selects the next     │
│ TOKEN    │   │  │ word/morpheme automatically. │
│          │   │  │ Not necessarily toward goal. │
└────┬─────┘   │  └──────────────┬──────────────┘
     ↓         │                 ↓
┌──────────────────────────────────────────────────────┐
│  MOVE PHASE (student-controlled if earned)           │
│  Student taps which letter/morpheme to change.       │
│  Then types/selects the replacement.                 │
│  Validation: Is this a valid word/morpheme step?     │
│    → If invalid: prompt to try again (no cost)       │
│    → If valid dead-end: warn (student can undo free) │
│    → If valid and viable: confirm → place on ladder  │
└──────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────┐
│  POST-RUNG FEEDBACK                                 │
│  Correct question: +XP shown, chain counter +1      │
│  Wrong question: "Random move!" flash, -no XP       │
│  Word placed: ladder board animates up one rung     │
│  Brief "Did You Know..." fact (subject-relevant)    │
└─────────────────────────────────────────────────────┘
            ↓
    Reached target word?
        YES → WIN SEQUENCE
        NO  → Next rung (loop back to top)
        Max rungs exceeded → LADDER COLLAPSE (see Section 9)
```

**WIN SEQUENCE:**
```
Target word glows → ladder completion animation → XP awarded → 
"Tabriklaymiz! [N] qadam — [N] to'g'ri javob" (Congratulations! N steps, N correct answers)
→ Subject mastery snippet: "Siz [standard_code] ni mashq qildingiz."
→ Return to Phase 3 game queue
```

---

## Section 2 — Input Format

Content authors provide a Word Ladder item via the following JSON schema.

### 2.1 Classic Letter-Swap Ladder (Language subjects)

```json
{
  "mechanic": "word_ladder_climb",
  "ladder_mode": "classic",
  "language": "uz",
  "subject": "uz_language",
  "grade": 5,
  "standard_ref": {
    "primary": "UZ-UZL-5-VOCAB-03",
    "alias": "UZL.5.2.1.3"
  },
  "textbook_ref": {
    "textbook_id": "uzl-5-2023-uz",
    "chapter": "So'z tarkibi",
    "section": "Qo'shimchalar",
    "page_range": "44-49"
  },
  "pisa_ref": {
    "domain": "reading",
    "proficiency_level": 2,
    "process_category": "access_and_retrieve",
    "transition_skill": "L1->L2: morphological pattern recognition in vocabulary"
  },
  "blooms_level": "understand",
  "start_word": "ODAM",
  "target_word": "AYOL",
  "optimal_path": ["ODAM", "ADAM", "AYAM", "AYOL"],
  "optimal_path_length": 3,
  "max_rungs_allowed": 6,
  "dictionary_id": "uz-nsm-2022",
  "questions": [
    {
      "rung": 1,
      "question_text": "So'zning tarkibida necha qism bo'lishi mumkin?",
      "question_type": "mc",
      "options": ["1 yoki 2", "2 yoki 3", "3 yoki 4", "faqat 1"],
      "correct_answer": "2 yoki 3",
      "pisa_level": 2,
      "blooms": "remember",
      "transition_skill": "L1->L2: recall grammatical unit count",
      "explanation_on_wrong": "O'zbek so'zi odatda ildiz va qo'shimchadan tashkil topadi — ba'zan faqat ildizdan."
    },
    {
      "rung": 2,
      "question_text": "\"Adam\" so'ziga qo'shimcha qo'shib yangi so'z hosil qiling.",
      "question_type": "open_short",
      "correct_answer_concepts": ["Adamning", "Adamcha", "Adamday"],
      "pisa_level": 2,
      "blooms": "apply",
      "transition_skill": "L1->L2: apply suffix to produce new word form",
      "scoring_rubric": "Any valid suffixed form of Adam earns full marks."
    },
    {
      "rung": 3,
      "question_text": "\"Ayol\" va \"Odam\" so'zlarining umumiy ma'nosi nima?",
      "question_type": "open_short",
      "correct_answer_concepts": ["inson", "odam", "kishi", "insoniyat"],
      "pisa_level": 2,
      "blooms": "understand",
      "transition_skill": "L2->L3: identify shared semantic field across words",
      "scoring_rubric": "Any answer identifying the shared human/person semantic field earns full marks."
    }
  ],
  "ai_tier": 1,
  "difficulty_knobs": {
    "optimal_path_length": 3,
    "max_rungs_allowed": 6,
    "question_pisa_level": 2,
    "hint_budget": 2
  }
}
```

### 2.2 Morphological Chain (Biology)

```json
{
  "mechanic": "word_ladder_climb",
  "ladder_mode": "morphological",
  "language": "uz",
  "subject": "biology",
  "grade": 7,
  "standard_ref": {
    "primary": "UZ-BIO-7-CELL-02",
    "alias": "BIO.7.1.2.2"
  },
  "textbook_ref": {
    "textbook_id": "bio-7-2023-uz",
    "chapter": "Hujayra",
    "section": "Hujayra organoidlari",
    "page_range": "18-25"
  },
  "pisa_ref": {
    "domain": "science",
    "proficiency_level": 2,
    "process_category": "explain",
    "transition_skill": "L1->L2: recognize morphological relationships between science terms"
  },
  "blooms_level": "understand",
  "start_term": "FOTOSINTEZ",
  "target_term": "FOTOSISTEMA",
  "morpheme_bank_id": "uz-bio-g7-morphemes",
  "chain_steps": [
    { "from": "FOTOSINTEZ", "to": "FOTOLIZ", "changed_unit": "sintez→liz", "morpheme_meaning": "synthesis→splitting" },
    { "from": "FOTOLIZ", "to": "FOTOSISTEMA", "changed_unit": "liz→sistema", "morpheme_meaning": "splitting→system" }
  ],
  "optimal_chain_length": 2,
  "max_steps_allowed": 5,
  "questions": [
    {
      "step": 1,
      "question_text": "Fotosintezda yorug'lik energiyasi nimaga aylanadi?",
      "question_type": "mc",
      "options": ["Kimyoviy energiyaga", "Issiqlik energiyasiga", "Elektr energiyasiga", "Mexanik energiyaga"],
      "correct_answer": "Kimyoviy energiyaga",
      "pisa_level": 2,
      "blooms": "understand",
      "transition_skill": "L1->L2: explain energy transformation in photosynthesis"
    },
    {
      "step": 2,
      "question_text": "Fotosistema I va Fotosistema II qaysi organoidda joylashgan?",
      "question_type": "mc",
      "options": ["Xloroplast", "Mitoxondriya", "Endoplazmatik to'r", "Ribosoma"],
      "correct_answer": "Xloroplast",
      "pisa_level": 2,
      "blooms": "remember",
      "transition_skill": "L1->L2: locate organelle by function"
    }
  ],
  "ai_tier": 1,
  "difficulty_knobs": {
    "chain_length": 2,
    "max_steps_allowed": 5,
    "question_pisa_level": 2,
    "hint_budget": 2
  }
}
```

### 2.3 Required Author-Provided Fields Summary

| Field | Required | Notes |
|---|---|---|
| `ladder_mode` | Yes | `"classic"` or `"morphological"` |
| `language` | Yes | `"uz"` or `"en"` |
| `subject` | Yes | Must match eligibility matrix (Section 6) |
| `grade` | Yes | G1-11 |
| `standard_ref.primary` | Yes | `UZ-{SUBJ}-{GRADE}-{TOPIC}-{SEQ}` |
| `textbook_ref` | Yes | Chapter, section, page range |
| `pisa_ref` (full) | Yes | Domain, level, process, `transition_skill` |
| `blooms_level` | Yes | Per-item and per-ladder |
| `start_word` / `target_word` | Yes | For classic mode |
| `start_term` / `target_term` | Yes | For morphological mode |
| `optimal_path` (classic) | Yes | Pre-calculated by author, validated by system |
| `chain_steps` (morphological) | Yes | Each step's from/to and morpheme_meaning |
| `questions[]` | Yes | One question object per rung/step |
| `max_rungs_allowed` | Yes | Must be ≥ optimal_path_length and ≤ optimal_path_length × 2 |
| `dictionary_id` | Classic only | Which approved dictionary validates words |
| `morpheme_bank_id` | Morphological only | Which biology term bank validates steps |

---

## Section 3 — Output / Evaluation

### 3.1 Per-Rung Evaluation

| Event | Correct/Wrong? | XP | Notes |
|---|---|---|---|
| Subject question — correct | Correct | +100 XP base per rung | Earns move token |
| Subject question — wrong | Wrong | 0 XP for this rung | Triggers random move |
| Move — reaches target in optimal path length | Bonus | +50 XP bonus | Speed precision bonus |
| Hint used | — | -25% XP for that rung | Word-direction hint consumed |
| Undo used | — | No XP effect | Free reversal of move choice |

### 3.2 Partial Credit (Open Short Answer questions)

Tier 1 keyword matching for short open answers:

```
AI_TIER: 1 (rule-based keyword match)

For open_short questions:
  1. Strip punctuation, lowercase student answer
  2. Check against correct_answer_concepts[] list (fuzzy match: Levenshtein ≤ 2)
  3. IF match found AND answer length >= 3 chars: CORRECT (100%)
  4. IF partial keyword match (≥1 of 3 required concepts present): PARTIAL (50%)
  5. IF no match: WRONG (0%)
  6. IF answer is blank after 45 seconds: WRONG + "Javob berilmadi" flag

Fallback for ambiguous short answers:
  → Tier 2 check: keyword semantic equivalence via lightweight NLP model
  → Returns within 2 seconds
  → Result: CORRECT / PARTIAL / WRONG with confidence score
  → Log: question_id, student_answer, tier_used, confidence
```

### 3.3 End-of-Ladder Evaluation

| Outcome | Criteria | Rating | Consequence |
|---|---|---|---|
| **Perfect Ladder** | Target reached + all questions correct + ≤ optimal_path_length steps | ★★★ | Full XP + "Mukammal!" badge flash |
| **Clean Ladder** | Target reached + ≥70% questions correct + ≤ optimal_path_length + 2 steps | ★★ | 80% XP |
| **Reached Target** | Target reached by any path | ★ | 50% XP |
| **Ladder Collapse** | Max rungs exceeded without reaching target | Fail | 0 XP, Duolingo Mode activated for this mechanic slot |
| **Abandoned** | Student quits mid-ladder | Fail | 0 XP, Duolingo Mode |

---

## Section 4 — PISA Mapping

### 4.1 PISA Level Coverage

Word Ladder Climb primarily operates at PISA Reading Levels 1-3. It does not scale to L4-6 on its own.

| Ladder Configuration | PISA Level | Domain | Process | Transition Skill Targeted |
|---|---|---|---|---|
| Classic, 3-step, MC questions | L1 | Reading | Access and Retrieve | L0→L1: recognize familiar word patterns |
| Classic, 4-step, MC + short answer | L2 | Reading | Access and Retrieve | L1→L2: morphological pattern recognition in vocabulary |
| Classic, 5-step, open short | L2-3 | Reading | Integrate and Interpret | L2→L3: infer meaning from morphological change across context |
| Morphological, 2-step, MC questions | L2 | Science/Reading | Explain | L1→L2: recognize morphological relationships between science terms |
| Morphological, 3-step, open short | L2-3 | Science/Reading | Interpret | L2→L3: interpret how term structure maps to function |

### 4.2 PISA Content and Context

| PISA Category | Value | Notes |
|---|---|---|
| **Domain** | Reading (primary) | Even when in Biology, the morphological chain exercises reading-domain skills |
| **Content** | Texts (literary/informational depending on subject) | Vocabulary in context |
| **Process** | Access & Retrieve (L1-2); Integrate & Interpret (L2-3) | Depends on question configuration |
| **Context** | Educational (school-setting vocabulary/biology tasks) | |

### 4.3 Transition Skills Library for Word Ladder Climb

Authors must tag each ladder with one of these approved transition skills (or propose a new one through the content pipeline):

| Transition Skill Tag | Description | Applicable Level |
|---|---|---|
| `L0→L1: recognize familiar word patterns` | Student can identify word-family patterns (cat/bat/hat) | G1-3 classic |
| `L1→L2: morphological pattern recognition in vocabulary` | Student recognizes how changing one letter changes word meaning/class | G4-6 classic |
| `L2→L3: infer meaning from morphological change across context` | Student uses the ladder word sequence to infer semantic relationships | G5-7 classic |
| `L1→L2: recognize morphological relationships between science terms` | Student matches prefix/root/suffix to biological function | G6-8 morphological |
| `L2→L3: interpret how term structure maps to function` | Student explains what the morphological change implies about biological role | G7-9 morphological |

---

## Section 5 — Bloom's Band

| Bloom's Level | How It Appears in Word Ladder Climb |
|---|---|
| **Remember** | Subject questions targeting recall of vocabulary definitions, formulas, or biological facts; Classic Ladder — recognizing valid words in the dictionary |
| **Understand** | Subject questions requiring interpretation; understanding that changing a letter changes word class or meaning |
| **Apply** | Selecting the correct letter to change to advance toward the target; applying morphological knowledge strategically |
| **Analyze** | Planning the multi-step path (which direction minimizes rungs?); understanding dead-end avoidance |
| ~~Evaluate~~ | Not reached by this mechanic at its current design scope |
| ~~Create~~ | Not reached by this mechanic at its current design scope |

**Primary band:** Remember → Understand → Apply (the game always exercises all three in one session).
**Stretch band:** Analyze (students who think ahead about path planning).

The mechanic **does not natively reach Evaluate or Create.** Do not assign it to topics where the primary Bloom's target is L5-6. Use Final Boss or Real-Life Challenge for those.

---

## Section 6 — Subject Eligibility

### 6.1 Eligibility Matrix

| Subject | Classic Mode | Morphological Mode | Reason |
|---|---|---|---|
| **English (CEFR)** | ✅ PRIMARY USE | ❌ | Classic ladder trains English phoneme/grapheme awareness. Core CEFR L1-B2 vocabulary mechanic. |
| **Uzbek Language (Ona tili)** | ✅ | ❌ | Uzbek word-family patterns, suffix awareness, agglutinative morphology practice. |
| **Adabiyot (Literature)** | ✅ (vocabulary from texts) | ❌ | Literary vocabulary, archaic terms, synonyms from assigned literary texts. |
| **Biology** | ❌ | ✅ PRIMARY USE | Biology terms require Morphological Chain. Classic mode produces nonsense paths. |
| **Chemistry** | ❌ | ⚠️ Limited | Only for very short element/compound abbreviation pairs (e.g., Mg→Mn). Requires explicit CMS approval. Not a default use case. |
| **Mathematics** | ❌ | ❌ | Mathematical vocabulary is too sparse in overlapping letter patterns to produce valid ladders. Use Tile Match or Sentence Fill instead. |
| **Physics** | ❌ | ❌ | Same as Mathematics. |
| **History** | ❌ | ❌ | Historical terms are proper nouns, dates, places — not amenable to letter-swap ladders. |
| **Geography** | ❌ | ❌ | Geographic terms are proper nouns. Not eligible. |
| **Tarbiya / Social Studies** | ❌ | ❌ | Reflective subject. Word Ladder does not map to Chill Mode shape. |
| **Tasviriy Sanat** | ❌ | ❌ | Maker-First shape. Word Ladder not suited to art vocabulary acquisition (use Tile Match). |
| **Texnologiya** | ❌ | ❌ | Technical vocabulary is too domain-specific and sparse in shared letter patterns. |
| **Informatika** | ❌ | ⚠️ Limited | Only for very short programming keywords with valid intermediate forms. Rare. Requires CMS approval. |
| **Russian Language** | ✅ | ❌ | Same justification as Uzbek Language. Uses Russian NSM dictionary for validation. |

### 6.2 Ineligibility Rationale (Why the Catalog Says "Language/Biology Only")

The Game Catalog Summary correctly restricts Word Ladder Climb to "language vocabulary, biology terminology." This section documents why:

1. **Classic mode requires dense word-family networks.** English and Uzbek have hundreds of 3-5 letter words that connect via single-letter changes. Math, History, Geography do not.
2. **Morphological mode requires productive morpheme systems.** Biology has Greek/Latin root-prefix-suffix systems with dense combinatorial space. Other sciences are sparser.
3. **The mechanic's learning ROI is maximized in language domains.** Morphological awareness is most directly measured in PISA Reading. Using it in Math would distract from the actual Math content.

---

## Section 7 — Grade Eligibility

| Grade Band | Classic Mode | Morphological Mode | Notes |
|---|---|---|---|
| **G1-2** | ⚠️ Simplified only | ❌ | Only 3-letter words, 2-step ladders, MC questions only. Recommended only with teacher override. Young students have limited spelling awareness. |
| **G3-4** | ✅ | ❌ | 3-4 letter words, 3-step ladders, MC questions. Movement Breaks still mandatory in G3-4 — Ladder replaces one game slot but Movement Break occurs between phases. |
| **G5-6** | ✅ RECOMMENDED | ✅ RECOMMENDED | Default eligibility window for both modes. 4-5 letter words / 3-step morphological chains. Short-open questions introduced in G5. |
| **G7-8** | ✅ | ✅ | Longer words (5-6 letters), 4-step chains, open-short questions dominant. |
| **G9-11** | ✅ (English CEFR) | ✅ (Biology) | Advanced vocabulary, 5-step ladders/chains, no word bank support. Academic register expected. |

**Grade-specific constraints:**

- **G1-2:** Content author must explicitly set `"grade_simplified": true` in the JSON. System enforces max 3 letters, 2 rungs, MC questions only.
- **G3-4:** Word bank for move hints enabled (student can see a 3-word suggestion list when making a move). Not a hint — it's a move vocabulary scaffold.
- **G5+:** Word bank disabled by default. Students type or select from the alphabet keyboard. No suggestion list.
- **G8+:** No hint budget pre-loaded. Students start with 0 hints; must earn them via question streaks (see difficulty knobs, Section 8).

---

## Section 8 — Parameters / Difficulty Knobs

The adaptive engine controls the following parameters independently:

| Parameter | What It Controls | G3-4 Default | G5-6 Default | G7-8 Default | G9-11 Default |
|---|---|---|---|---|---|
| `ladder_length` | Optimal path length (rungs/steps) | 2 | 3 | 4 | 5 |
| `max_rungs_allowed` | Maximum rungs before Ladder Collapse | 4 | 6 | 8 | 10 |
| `word_length` (classic) | Length of start/target words | 3 letters | 4-5 letters | 5-6 letters | 6-7 letters |
| `chain_depth` (morphological) | Number of morphological steps | — | 2 | 3 | 4 |
| `question_pisa_level` | Target PISA level of the gate questions | L1 | L2 | L2-3 | L3 |
| `question_type` | MC / open_short / open_extended | MC only | MC + open_short | open_short dominant | open_short + open_extended |
| `hint_budget` | Free hints per ladder | 2 | 2 | 1 | 0 (earn via streaks) |
| `word_bank` (classic move) | Show 3-word move suggestions | ON | OFF | OFF | OFF |
| `timer_per_question` | Seconds per gate question | 60s | 45s | 40s | 35s |
| `random_move_recovery` | Can student earn back a lost rung via next correct answer? | YES | YES | NO | NO |

**Adaptive Engine Rules:**

```
AFTER each completed ladder in the session:

IF accuracy_on_questions >= 80%:
  → Increase ladder_length by 1 (if not already at grade max)
  → Increase question_pisa_level by 0.5 (if not already at grade ceiling)

IF accuracy_on_questions < 50%:
  → Decrease ladder_length by 1 (minimum = 2)
  → Decrease question_pisa_level by 0.5 (minimum = L1)
  → Activate word_bank if not already active

IF student uses all hints in first 2 rungs on two consecutive ladders:
  → Flag for teacher review (vocabulary gap suspected)
  → Decrease question_pisa_level by 1 for next session
```

**Random Move Recovery** (G3-6 only): If the student answers the NEXT rung's question correctly after a random move, the system will "re-route" the ladder: if the random move ended on a viable intermediate word, the student continues from there; if the random move ended on a dead-end word, the system restores the previous position and the student takes their earned move normally. This prevents one wrong answer from permanently collapsing a young student's game.

---

## Section 9 — Failure / Retry Behavior

### 9.1 Per-Rung Wrong Answer: "Hali emas" (Not Yet)

When a gate question is answered wrong:

```
1. UI: Answer tiles shake (3x, 100ms) — standard NETS wrong-answer animation
2. Feedback: "Hali emas! To'g'ri javob: [X]" displayed for 2 seconds
3. "Random Move" banner flashes: "Tasodifiy qadam!"
4. System selects a valid dictionary word adjacent (1 step) to current word,
   chosen randomly from all valid neighbors — NOT necessarily toward the target.
   For morphological mode: system selects a random valid morpheme substitution.
5. Ladder advances (or laterals, or regresses) by this random step.
6. No XP for this rung.
7. Play continues from the new position.
```

**Tone:** "Hali emas" ("Not yet") is used throughout the Uzbek LMS as the standard wrong-answer phrase for formative practice contexts. This is not a penalty — it is a redirect. The animation is brief; the game continues immediately.

### 9.2 Ladder Collapse (Max Rungs Exceeded)

```
IF rungs_used > max_rungs_allowed AND target NOT reached:

1. UI: Ladder animation collapses (falling tiles)
2. "Narvon qulab tushdi! [N] ta to'g'ri javob bilan qayta urinib ko'ring."
   ("The ladder collapsed! Try again with [N] correct answers.")
3. Duolingo Mode activates for this game slot:
   → Student is shown the 3 questions they got most wrong
   → System generates a SHORTER ladder (optimal_path_length - 1)
   → Student reattempts
   → If reattempt fails again: 0 XP for this slot, session continues to next game
4. Teacher flagged if collapse + reattempt-fail happens in same session × 3 sessions.
```

### 9.3 Session-Level Retry

Word Ladder Climb does not have its own session-level retry mechanic beyond the standard Duolingo Mode (§6.6 of UNIFIED). After a Ladder Collapse, the slot is treated the same as any other failed game slot: Duolingo Mode is activated for that one slot, and the session continues. The student does not repeat the entire Phase 3.

### 9.4 Edge Case: Valid But Dead-End Move

If a student earns a move token but selects a word that is valid in the dictionary BUT has no valid onward path to the target:

```
System response: "Sahih so'z! Lekin bu so'zdan [TARGET]ga yetish qiyin — 
qaytadan o'ylang yoki bekor qiling."
("Valid word! But reaching [TARGET] from here is difficult — reconsider or undo.")

Student options:
  → UNDO (free, no XP cost, no hint consumed): returns to previous word, re-selects move
  → CONFIRM ANYWAY: student keeps the word. Now max_rungs_allowed - 1 (one rung shorter budget).
    System updates the path and continues. Student may need to use hints to escape.
```

---

## Section 10 — Anti-Cheat Surface

### 10.1 Tier 2 Monitoring Points

Word Ladder Climb has a moderate anti-cheat surface. All monitoring is Tier 2 (pattern analysis, no generative AI required).

| Monitoring Point | What Is Detected | Response |
|---|---|---|
| **Answer timing** | Question answered in < 2 seconds (for non-MC questions) | Flag as suspicious. Log for teacher review. Do not auto-invalidate. |
| **Move timing** | Move selected in < 0.5 seconds (player likely had word pre-chosen) | Acceptable for MC (word bank visible). Flag for open-move (G5+) if pattern persists across ladder. |
| **Tab / app switching during question** | Student switches tab/app mid-question | Timer pauses. Question is regenerated on return (different question, same PISA level). Counter logged: `tab_switches_this_session`. If > 3: flag to teacher. |
| **Identical answers across students** | Two students in same class submit identical open_short answers verbatim | Flag both to teacher. No auto-penalty. |
| **Dictionary lookup behavior** | External keyboard activity (clipboard paste) during move selection | Paste is blocked on the move input field by the client. If bypass detected (injection-style): flag as integrity issue, invalidate current ladder. |
| **Implausible vocabulary for grade level** | G3 student uses IELTS-band-8 vocabulary in an open_short answer | Flag for teacher review. Not auto-wrong. |
| **Always optimal path selection** | Student consistently selects the single-optimal path with 0 dead-ends across 5+ ladders | Flag for review. May indicate pre-knowledge of content; schedule a variation ladder or switch game mechanics. |

### 10.2 What Word Ladder Climb Does NOT Monitor

- Typing speed on open answers (speed varies too much by device/motor skill)
- Which letter positions the student explores before confirming (speculative hovering is normal exploration)
- Whether the student has a physical word ladder cheat sheet (undetectable; not worth trying)

---

## Section 11 — Telemetry Emitted

All events below are emitted in real-time to the NETS analytics pipeline. Teacher dashboard and mastery map consume these events.

### 11.1 Session-Level Events

```json
{
  "event": "word_ladder_session_start",
  "student_id": "...",
  "ladder_id": "...",
  "standard_ref": "UZ-UZL-5-VOCAB-03",
  "ladder_mode": "classic",
  "language": "uz",
  "grade": 5,
  "pisa_level_at_start": 1.8,
  "optimal_path_length": 3,
  "max_rungs_allowed": 6,
  "hint_budget": 2,
  "timestamp": "2026-04-11T14:23:00Z"
}

{
  "event": "word_ladder_session_end",
  "student_id": "...",
  "ladder_id": "...",
  "outcome": "completed | collapsed | abandoned",
  "rating": "3_star | 2_star | 1_star | fail",
  "rungs_used": 4,
  "correct_questions": 2,
  "wrong_questions": 1,
  "hints_used": 1,
  "undos_used": 0,
  "random_moves_triggered": 1,
  "xp_earned": 225,
  "duration_seconds": 148,
  "timestamp": "2026-04-11T14:25:28Z"
}
```

### 11.2 Per-Rung Events

```json
{
  "event": "word_ladder_rung",
  "rung_number": 2,
  "question_id": "q-rung-2-vocab03",
  "question_correct": true,
  "answer_time_ms": 12400,
  "move_chosen": "ADAM→AYAM",
  "move_valid": true,
  "move_optimal": true,
  "hint_consumed": false,
  "undo_used": false,
  "xp_this_rung": 100
}

{
  "event": "word_ladder_rung",
  "rung_number": 3,
  "question_id": "q-rung-3-vocab03",
  "question_correct": false,
  "answer_time_ms": 5200,
  "random_move_word": "AXOL",
  "random_move_valid": true,
  "hint_consumed": false,
  "xp_this_rung": 0
}
```

### 11.3 Teacher Dashboard Aggregates (derived)

| Metric | How Computed | Displayed As |
|---|---|---|
| `question_accuracy_by_standard` | Correct / Total questions per standard_ref | Mastery % per standard |
| `ladder_completion_rate` | Completed ladders / Total attempted (per student) | Student progress bar |
| `avg_rungs_used_vs_optimal` | Mean(rungs_used - optimal_path_length) per student | Efficiency score |
| `hint_usage_rate` | Total hints used / Total ladders (per student) | Vocabulary support flag |
| `random_move_frequency` | random_moves_triggered / Total rungs | Content difficulty signal |
| `tab_switch_count` | Cumulative tab_switches across session | Integrity alert if > 3 |
| `transition_skill_progress` | % correct questions tagged to student's in_progress transition skill | Mastery map update |

### 11.4 Mastery Map Update

After every Word Ladder session, the student's mastery map is updated for:
- The `standard_ref` of the completed ladder
- The `transition_skill` targeted by this ladder
- The `pisa_ref.proficiency_level` (increment if ★★★ rating, decrement if Collapse × 2)

---

## Section 12 — Dual-Catalog Role

**Pool: Interactive Catalog Pool — Slot #6**

Word Ladder Climb is an Interactive Catalog game, not a Default Pool game. This means:

- It fills the mandatory "≥1 from Interactive Catalog" slot in Phase 3 game selection (§5.3 of UNIFIED, Dual-Catalog Rule)
- It is NOT a Default Pool game and cannot fill the "≥2 from Default Pool" slots
- When Word Ladder Climb is selected for a session, the remaining 2 slots MUST come from the Default Pool (e.g., Sentence Fill + Tile Match)
- The engine selects Word Ladder Climb only when the session subject is in the eligible list (English, Uzbek Language, Adabiyot, Biology/Russian — see Section 6)

**Why it belongs in the Interactive Catalog (not Default Pool):**

The Default Pool contains core pedagogy mechanics that map 1:1 to Bloom's/PISA bands and cover all subjects. Word Ladder Climb is a knowledge-gated game derived from a classic puzzle mechanic (the word ladder game, patented by Lewis Carroll, 1879). It adds strategic meta-gameplay (path planning, dead-end avoidance) on top of the content question gate. This strategic layer — "choosing the right word to maximize future options" — is the distinguishing feature of Interactive Catalog games. The Default Pool equivalents (Sentence Fill, Tile Match) cover vocabulary without this strategic layer.

**Session Selection Trigger:** The Phase 3 engine selects Word Ladder Climb when:
- Subject is English, Uzbek Language, Adabiyot, or Biology
- Student's PISA level is L1-3 in the Reading domain
- Student's engagement score has not been flagged as "low" in the last 2 sessions (if low, engine picks Territory Conquest or Reaction Chain instead for higher novelty)
- Device supports text input (always true for NETS target devices)

**Fallback:** If no eligible ladder is available in the content pool for the current standard_ref, engine logs `CATALOG_FALLBACK: word_ladder_no_content` and selects Reaction Chain or Connect Four as a replacement.

---

## Section 13 — Cost Profile

### 13.1 Tier Breakdown

| Component | AI Tier | Cost Driver | Notes |
|---|---|---|---|
| Ladder board rendering | Tier 1 | Static UI | Dictionary lookup is local (cached word graph) |
| Gate question delivery | Tier 1 | Pre-generated question pool | Questions are pre-authored in JSON, served from DB |
| MC answer checking | Tier 1 | Rule-based exact match | Instant, no model call |
| Open_short answer checking | Tier 1 (primary) | Keyword matching against concepts list | Fallback only |
| Open_short — ambiguous | Tier 2 | Lightweight NLP semantic match | ~2s, used <20% of open_short questions |
| Dictionary validation (classic) | Tier 1 | Pre-cached word graph, O(1) lookup | Word graph pre-built per grade × language |
| Morpheme validation (morphological) | Tier 1 | Pre-cached term bank | Biology morpheme bank is small (~500 terms per grade) |
| Hint generation | Tier 1 | Pre-calculated optimal paths | Hints are the next optimal position, pre-computed at content time |
| Telemetry emission | Tier 1 | Event queue, async | No synchronous cost |
| Teacher dashboard aggregation | Tier 1 | Batch analytics job (nightly) | Not real-time |

**Tier 3 (Generative AI): ZERO calls during normal play.** Word Ladder Climb is a Tier 1 mechanic with a Tier 2 fallback for open-answer edge cases. No generative AI is involved unless the student's Ladder Collapse routes into Duolingo Mode and the Final Boss follows — but that is the Final Boss's Tier 3 cost, not Word Ladder's.

### 13.2 Estimated Cost Per Student Per Session

| Component | Estimated Cost |
|---|---|
| 3-rung ladder × 1 per session (Phase 3 slot) | ~$0.0001 (DB reads, validation) |
| Tier 2 NLP fallback (20% of open_short sessions) | ~$0.0003 per occurrence |
| **Total per Word Ladder Climb session** | **< $0.001** |

This fits comfortably within the $3-5/student/year national scale target. Word Ladder Climb is among the cheapest Interactive Catalog games.

---

## Section 14 — Device Requirements

### 14.1 Minimum Specifications

| Requirement | Minimum | Notes |
|---|---|---|
| **Processor** | 1.2 GHz ARM or equivalent | Ladder board animation is light CSS — no GPU required |
| **RAM** | 1 GB | Local word graph (Classic) fits in < 5 MB RAM |
| **Display** | 480px width minimum | Ladder board reflows for small screens |
| **Connectivity** | 50 Kbps average | Questions pre-fetched at session start; ladder runs offline after fetch |
| **Input** | Touch (drag not required; tap + keyboard) | Classic mode: tap letter tiles + on-screen keyboard. Morphological mode: tap morpheme tiles. |
| **Camera** | Not required | No Notebook Capture in Word Ladder Climb |
| **Special hardware** | None | |

### 14.2 Offline Mode

Word Ladder Climb supports offline play. At session start, the engine pre-fetches:
- The complete ladder JSON (start word, target word, all gate questions)
- The relevant word graph (Classic) or morpheme bank (Morphological) for this grade/subject

All gameplay can proceed without connectivity after this pre-fetch. Telemetry events are queued locally and synced when connectivity is restored. If pre-fetch fails (no connectivity at session start), the engine skips Word Ladder Climb and selects a pre-cached Default Pool game instead.

### 14.3 Excluded Devices / Contexts

- **No camera required** — unlike Notebook Capture, Word Ladder Climb does not need camera hardware.
- **No audio required** — all feedback is visual. No sound-dependent mechanics.
- **Low-end device flag:** Word Ladder Climb is NOT on the "skip on low-end devices" list (unlike Bridge Builder and Minefield Navigator). It runs on any NETS-minimum-spec device.

---

## Section 15 — Worked Example

### Subject: English CEFR — Grade 5 — Classic Letter-Swap Mode

**Context:** This example is drawn from the Grade 5 English CEFR textbook (Uz edition), Unit 3: "Clothes and Colours." Learning objective UZ-ENG-5-VOCAB-07 covers clothing and adjective vocabulary.

**Ladder Parameters:**
- Start word: `COAT`
- Target word: `JEANS`

Wait — 4 letters vs. 5 letters. Classic mode only allows same-length words (letter substitution, no insertion/deletion). Let me pick a valid pair:

- Start word: `COLD`
- Target word: `WARM`
- Optimal path: `COLD → CORD → WORD → WARD → WARM`
- Optimal path length: 4 rungs
- Max rungs allowed: 8
- Language: English
- Dictionary: Oxford Elementary (G5 CEFR A1-A2 wordlist)

---

**RUNG 1:**

*Question (PISA L2 / Reading / Access & Retrieve):*
"What do you wear in cold weather to keep warm?"

*Options (MC):*
A) Sunglasses  B) A coat and scarf  C) Sandals  D) A swimsuit

*Correct: B*

*Student answers B → earns move token.*

*Student's move:* Changes `C` → `C...O...R...D`. Types `CORD`.

*Validation:* CORD is in the Oxford Elementary dictionary. ✅ Valid step.

*Ladder board:* `COLD → [CORD]` (CORD highlighted, glowing).

*XP: +100. Running total: 100.*

*Post-rung fact:* "Did you know? The word 'cord' also means a thick string — like the cord in a hoodie!"

---

**RUNG 2:**

*Question (PISA L2 / Reading / Access & Retrieve):*
"Which of these is a word for something you use when it rains?"
A) Umbrella  B) Gloves  C) Hat  D) Boots

*Correct: A*

*Student answers A → earns move token.*

*Student's move:* Changes `C` → `WORD`.

*Validation:* WORD is in the Oxford Elementary dictionary. ✅ Valid step.

*Ladder board:* `COLD → CORD → [WORD]`

*XP: +100. Running total: 200.*

---

**RUNG 3:**

*Question (PISA L2-3 / Reading / Integrate & Interpret):*
"Look at the two words below. What do they have in common?
`WARM` / `SOFT`
A) Both describe textures  B) Both describe how something feels on your skin  C) Both are verbs  D) Both describe colours"

*Correct: B*

*Student answers C (wrong!) → random move triggered.*

*Random move:* System selects `WARD` (valid dictionary word, 1 letter from WORD, within the Oxford G5 wordlist). Ladder advances to `WARD`.

*Feedback:* "Hali emas! To'g'ri javob: B — 'Both describe how something feels on your skin'. Tasodifiy qadam: WARD!"

*XP: +0. Running total: 200.*

---

**RUNG 4:**

*Question (PISA L2 / Reading / Access & Retrieve):*
"What does 'warm' mean? Choose the best answer:
A) Very hot  B) Pleasantly hot — not too hot, not cold  C) Cold  D) Wet"

*Correct: B*

*Student answers B → earns move token.*

*Student's move:* Student sees they are at `WARD` and the target is `WARM`. They change `D` → `M`: `WARM`.

*Validation:* WARM is in the Oxford Elementary dictionary. WARM = TARGET. ✅ LADDER COMPLETE!

---

**Win Sequence:**

```
🎉 NARVON YAKUNLANDI! (Ladder Complete!)
PATH: COLD → CORD → WORD → WARD → WARM (4 rungs — optimal path!)
Correct questions: 3/4 (75%)
Hints used: 0
Rating: ★★ (2-star — reached target, ≥70% correct, optimal path length)
XP earned: 200 + 40 (2-star bonus) = 240 XP
Transition skill practiced: L1→L2: morphological pattern recognition in vocabulary ✅
Standard: UZ-ENG-5-VOCAB-07 updated in mastery map.
```

---

### Subject: Biology — Grade 7 — Morphological Chain Mode

**Context:** Grade 7 Biology, Chapter 1: "Hujayra" (The Cell). Learning objective UZ-BIO-7-CELL-02: identify organelles and their functions. Morphological Chain variant.

**Chain Parameters:**
- Start term: `FOTOSINTEZ`
- Target term: `FOTOSISTEMA`
- Chain: `FOTOSINTEZ → FOTOLIZ → FOTOSISTEMA`
- Chain length: 2 steps
- Language: Uzbek (biology terms)
- Morpheme bank: `uz-bio-g7-morphemes`

---

**STEP 1:**

*Question (PISA L2 / Science / Explain):*
"Fotosintezda qaysi organoid asosiy rol o'ynaydi?"

*Options (MC):*
A) Ribosoma  B) Mitoxondriya  C) Xloroplast  D) Vakuola

*Correct: C*

*Student answers C → earns move token.*

*Student's move:* Change `sintez` → `liz` (morpheme substitution: Greek *synthesis* → *lysis*).

*Validation:* `FOTOLIZ` is in the G7 Biology morpheme bank. ✅

*Feedback:* "'Liz' Greek tilida 'parchalash' degani — fotolizda yorug'lik suv molekulasini parchalaydi."

*XP: +100.*

---

**STEP 2:**

*Question (PISA L2 / Science / Explain):*
"Fotosistema I va II qayerda joylashgan?"

*Options (MC):*
A) Ribosomada  B) Xloroplastning tilakoid membranasida  C) Yadroda  D) Sitoplazmada

*Correct: B*

*Student answers B → earns move token.*

*Student's move:* Change `liz` → `sistema`.

*Validation:* `FOTOSISTEMA` = TARGET TERM. ✅ CHAIN COMPLETE!

---

**Win Sequence:**

```
ZANJIR YAKUNLANDI! (Chain Complete!)
PATH: FOTOSINTEZ → FOTOLIZ → FOTOSISTEMA (2 steps — optimal!)
Correct questions: 2/2 (100%)
Hints used: 0
Rating: ★★★ (3-star — perfect chain)
XP earned: 200 + 100 (3-star bonus) = 300 XP
Transition skill practiced: L1→L2: recognize morphological relationships between science terms ✅
Standard: UZ-BIO-7-CELL-02 updated in mastery map.
```

---

## Appendix: Glossary of Terms Used in This Document

| Term | Definition |
|---|---|
| **Rung** | One step in a Classic Letter-Swap Ladder (one letter changed, one question answered) |
| **Step** | One step in a Morphological Chain (one morpheme changed, one question answered) |
| **Ladder Collapse** | When the student exceeds max_rungs_allowed without reaching the target |
| **Random Move** | A system-chosen word/morpheme step triggered by a wrong gate-question answer |
| **Move Token** | Earned right to make a student-chosen word/morpheme step (earned by correct gate question) |
| **Morpheme Bank** | Pre-approved registry of biological morphemes used to validate Morphological Chain steps |
| **Hali emas** | "Not yet" — standard NETS Uzbek phrase for formative wrong-answer feedback |
| **Optimal Path** | The shortest valid sequence from start word to target word, pre-calculated at content authoring time |
| **Dead-End Word** | A valid dictionary word with no onward path to the target word |
| **Transition Skill** | Specific PISA sub-skill being scaffolded (e.g., "L1→L2: morphological pattern recognition") |
| **Dual-Catalog Rule** | Phase 3 selection rule: ≥1 Interactive Catalog game + ≥2 Default Pool games per session |

---

*Document produced by WordLadderResearcher agent (ADS-25) — Class A EDU / NETS project.*
*For questions, reference [ADS-25](/ADS/issues/ADS-25) or contact the parent task [ADS-17](/ADS/issues/ADS-17).*
