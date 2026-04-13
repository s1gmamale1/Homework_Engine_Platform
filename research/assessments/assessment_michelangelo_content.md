# HES v2.0 Content Pipeline & Production Volume Assessment

**Analyst:** Michelangelo (Agent 71ccba21)
**Date:** April 2, 2026
**Task:** TMN-22 — Content Pipeline & Production Volume Assessment
**Source Document:** `HOMEWORK_STANDARDS.md` (v1.0, April 1, 2026 — 2,063 lines)
**Prior Analysis:** `analysis_michelangelo_synthesis.md` (TMN-8 cross-criteria gap analysis)

---

## 1. Executive Summary

**Verdict: MAJOR PRODUCTION GAPS — NOT LAUNCHABLE WITHOUT SIGNIFICANT CONTENT INVESTMENT**

The HES v2.0 spec is a well-designed pedagogical engine. It is *not* a content-ready production specification. The document defines *how* content should behave (game mechanics, timing, XP, adaptation algorithms) but does not define *what content exists* or *how it gets created at scale*.

Key findings:

- **Minimum ~76,000 unique content items** needed for 3 core subjects across 11 grades (~30 chapters each). With 6 subjects referenced in the spec, that number exceeds **152,000 items**.
- **2,970 unique story segments** requiring either video production (74+ hours) or illustrated panel production (8,900–14,850 panels), multiplied by 3 language narration tracks.
- **3 subjects have no PISA framework or game adaptation specs** (English, History, CS) despite being referenced in §9.7.
- **Grades 1-2 have no Story Mode narrative framework** — a gap affecting 1.6M students (estimated ~18% of the 8.8M target).
- **Zero content authoring pipeline defined** — no tooling, no content team structure, no review workflow, no calibration process for IRT question banks.
- **Section 3.2 is a placeholder** — "Continue with detailed specifications for each of the 14 games" was never written.

The spec tells you *what* to build but gives content teams almost nothing to *build against* at scale.

---

## 2. Content Volume Matrix

### 2.1 Assumptions

| Parameter | Value | Source |
|-----------|-------|--------|
| Grades | 11 (Grades 1–11) | §4.1–4.3, §8.1 |
| Core subjects (with PISA specs) | 3 (Math, Reading, Science) | §4.1–4.3 |
| Additional subjects (mentioned, unspecified) | 3 (English, History, CS) | §9.7 |
| Chapters per grade per subject | ~30 | Task brief (consistent with §2.3 "Chapter 4.2" numbering pattern) |
| Homework sessions per chapter | 1 | §2.1 (single homework session structure) |
| Total chapters (3 core subjects) | 11 × 3 × 30 = **990** | Calculated |
| Total chapters (6 subjects) | 11 × 6 × 30 = **1,980** | Calculated |

### 2.2 Per-Game Content Items (3 Core Subjects Only)

| Game / Content Type | Items per Chapter | Total (990 chapters) | Notes |
|---------------------|-------------------|----------------------|-------|
| **Story Mode segments** | 3 segments × 90s | **2,970 segments** | Video or illustrated panels; each needs script, media, narration |
| **Story Mode comprehension checks** | 4–6 questions | **3,960–5,940** | 1-2 questions between each of 3 segments |
| **Memory Sprint questions** | 6–10 unique questions (pool) | **5,940–9,900** | Must draw from *previous* chapters; pool must be large for non-repetition |
| **Adaptive Quiz (IRT-calibrated)** | 20–30 items minimum | **19,800–29,700** | Each item requires pre-calibrated θ, α, c parameters (§11.5) |
| **Final Boss questions** | 15–21 per chapter (3 attempts × 5–7 Qs, all unique per anti-cheat) | **14,850–20,790** | Must be regenerable or pool must be deep; PISA-tagged and tier-tagged |
| **Tile Match pair sets** | 2–3 unique sets | **1,980–2,970** | 4–6 pairs per set = 7,920–17,820 individual tile items |
| **Sentence Fill passages** | 3–5 passages | **2,970–4,950** | 3–5 blanks each; word bank generation rules vary by grade band |
| **Why Chain seed prompts** | 2–3 chains | **1,980–2,970** | 3–5 "why" levels each; need expected reasoning paths per level |
| **Mystery Box problem sets** | 2–3 sets | **1,980–2,970** | Mixed problems from current + previous chapters |
| **Flashcards** | 5–10 cards | **4,950–9,900** | Need front/back/example; spaced repetition algorithm drives review |
| **Real-Life Challenge scenarios** | 1 per chapter | **990** | Must be culturally authentic Uzbek context; multi-step with rubric |
| **Peer Teaching scenarios** | 2–3 per chapter | **1,980–2,970** | 3 scenario types (explain, help, correct); AI-evaluated |
| **Movement Breaks** (Gr 1-4 only) | 2–3 per chapter | **720–1,080** | 4 grades × 3 subjects × 30 chapters × 2.5 avg |
| **Memory Palace setups** | 1 per chapter | **990** | 5 concepts per palace; template-driven but need concept mapping |
| **Reflection Journal prompts** | AI-generated (templates) | **~990 templates** | Lower production burden; template-driven per performance patterns |

### 2.3 Total Content Item Count (3 Core Subjects)

| Category | Low Estimate | High Estimate |
|----------|-------------|---------------|
| Story Mode (segments + checks) | 6,930 | 8,910 |
| Question banks (Sprint + Quiz + Boss) | 40,590 | 60,390 |
| Game content (Tile + Sentence + Why + Mystery + Flash) | 13,860 | 23,760 |
| Scenarios (Real-Life + Peer + Movement + Palace) | 4,680 | 6,030 |
| Templates (Reflection) | 990 | 990 |
| **TOTAL (3 subjects)** | **~67,050** | **~100,080** |

**Midpoint estimate: ~76,000 unique content items for 3 core subjects.**

### 2.4 If 6 Subjects Are In Scope

The spec references English, History, and CS in §9.7 (Parent Engagement Portal: "Per-subject performance: Math, Reading, Science, English, History, CS"). If these 3 additional subjects require the same content depth:

| Scope | Low Estimate | High Estimate | Midpoint |
|-------|-------------|---------------|----------|
| 3 core subjects | 67,050 | 100,080 | ~76,000 |
| 6 subjects | 134,100 | 200,160 | ~152,000 |

**This is the critical ambiguity in the spec.** Are English, History, and CS full HES subjects with 7-step journeys and 14-game support? Or are they tracked for grades only? The spec provides zero game adaptation details, zero PISA matrices, and zero content examples for these 3 subjects.

### 2.5 Content Volume Matrix — Detailed Breakdown by Grade Band

| Grade Band | Grades | Subjects | Chapters | Story Segments | Question Pool (all types) | Game Items | Scenarios | **Subtotal** |
|------------|--------|----------|----------|----------------|--------------------------|------------|-----------|-------------|
| **Gr 1-2** | 2 | 3 | 180 | 540 | 7,380–11,340 | 2,520–4,320 | 1,260–1,620 | **11,700–17,820** |
| **Gr 3-4** | 2 | 3 | 180 | 540 | 7,380–11,340 | 2,520–4,320 | 900–1,080 | **11,340–17,280** |
| **Gr 5-6** | 2 | 3 | 180 | 540 | 7,380–11,340 | 2,520–4,320 | 720–900 | **11,160–17,100** |
| **Gr 7-8** | 2 | 3 | 180 | 540 | 7,380–11,340 | 2,520–4,320 | 720–900 | **11,160–17,100** |
| **Gr 9-11** | 3 | 3 | 270 | 810 | 11,070–17,010 | 3,780–6,480 | 1,080–1,530 | **16,740–25,830** |
| **TOTAL** | 11 | 3 | 990 | 2,970 | 40,590–62,370 | 13,860–23,760 | 4,680–6,030 | **~67,050–100,080** |

---

## 3. Localization Assessment

### 3.1 Language Variants Required

Per §9.7 and §2.3:

| Language | Script | Primary Use |
|----------|--------|-------------|
| Uzbek (Latin) | Latin alphabet | Official state script; primary instruction medium |
| Uzbek (Cyrillic) | Cyrillic alphabet | Widely used by older generation; many existing textbooks |
| Russian | Cyrillic | Instruction language in ~30% of schools; significant minority |

### 3.2 Localization Scope

| Content Type | Translation Strategy | Volume (per language) | Total (3 languages) |
|-------------|---------------------|----------------------|---------------------|
| **Story Mode scripts** | Full cultural adaptation needed (not just translation) | 990 chapter scripts (~500–800 words each) | 2,970 scripts |
| **Story Mode narration** | Full re-recording per language | 74.25 hours of narrated audio | **222.75 hours** |
| **Question text** | Translation + validation for mathematical/scientific accuracy | ~76,000 items | ~228,000 items |
| **UI strings** | Standard translation | ~500–1,000 strings | ~1,500–3,000 strings |
| **Real-Life Challenges** | Cultural adaptation (not just translation — Russian-language students may need different cultural references) | 990 scenarios | 2,970 scenarios |
| **Parent Portal content** | Translation + cultural adaptation | ~100 templates | ~300 templates |
| **SMS notifications** | Translation | ~50 templates | ~150 templates |

### 3.3 Total Estimated Word Count

| Content Type | Words per Item | Items (3 subjects) | Words per Language | Words (3 languages) |
|-------------|---------------|--------------------|--------------------|---------------------|
| Story Mode scripts | 650 avg | 990 | 643,500 | 1,930,500 |
| Questions (all types) | 35 avg | 76,000 | 2,660,000 | 7,980,000 |
| Real-Life Challenges | 150 avg | 990 | 148,500 | 445,500 |
| Peer Teaching scenarios | 80 avg | 2,475 | 198,000 | 594,000 |
| UI + templates | — | — | 50,000 | 150,000 |
| **TOTAL** | | | **~3,700,000** | **~11,100,000** |

**~11.1 million words total across 3 languages** for 3 core subjects. For 6 subjects: **~22.2 million words**.

### 3.4 Critical Localization Question

The spec does not answer: **Is translation sufficient, or does each language need culturally adapted content?**

- Uzbek Latin → Uzbek Cyrillic: Script transliteration is mostly mechanical (some vocabulary differences exist between Latin-educated and Cyrillic-educated populations, but core academic content is identical).
- Uzbek → Russian: **Not just translation.** Russian-language schools in Uzbekistan serve a different demographic. Cultural references (Uzbek names, Uzbek-specific scenarios like plov preparation, cotton harvest) may resonate differently. The spec mandates Uzbek cultural elements (§2.3, §11.9) — it's unclear whether Russian-language versions should maintain identical cultural framing or adapt.

**Recommendation:** Treat Uzbek Latin → Cyrillic as transliteration (low cost). Treat Uzbek → Russian as full localization requiring cultural review (high cost).

---

## 4. Specification Gaps for Content Teams

### 4.1 Critical Gaps (Block Production)

| # | Gap | Section | Impact | Severity |
|---|-----|---------|--------|----------|
| 1 | **Grades 1-2 have no Story Mode narrative framework** | §2.3 | Narrative table starts at Grade 3. 1.6M students (~18% of target) have no story content spec. Content teams cannot begin Grade 1-2 story production. | **BLOCKER** |
| 2 | **Section 3.2 is a placeholder** | §3.2 | Text reads: "Continue with detailed specifications for each of the 14 games including: Complete mechanics, UI wireframes, XP awards..." This was never written. The Appendix (§11) partially covers this, but §3.2 promised grade-level adaptations and accessibility requirements per game — those are missing for most games. | **BLOCKER** |
| 3 | **No content authoring pipeline defined** | Absent | Who creates content? What tools do they use? What's the review/approval workflow? What's the content management system? Without this, 76,000+ items cannot be produced. | **BLOCKER** |
| 4 | **IRT calibration process undefined** | §11.5 | Adaptive Quiz requires pre-calibrated items with difficulty (θ), discrimination (α), and guessing (c) parameters. Calibration requires **pilot testing with real students** — typically 200+ responses per item. For 19,800–29,700 items, this is a massive data collection effort. No calibration plan exists. | **BLOCKER** |
| 5 | **Which textbooks?** | §5.2 | "Preserve core concepts exactly as presented in textbook." But which textbooks? Uzbekistan has multiple publishers. Are they nationally standardized? Who provides digital access to textbook content for adaptation? What happens when textbooks are updated mid-year? | **BLOCKER** |
| 6 | **3 subjects (English, History, CS) have no specs** | §9.7 vs §4.1-4.3 | Referenced in parent portal but have zero PISA matrices, zero game adaptation rules, zero content examples. Content teams have nothing to build against. | **BLOCKER** |

### 4.2 Major Gaps (Impede Production Quality)

| # | Gap | Section | Impact | Severity |
|---|-----|---------|--------|----------|
| 7 | **Anti-cheat "question regeneration" mechanism undefined** | §2.7 | Spec says "Every boss attempt generates NEW questions on same concepts." Is this AI-generated in real-time? Or drawn from a large pre-authored pool? If AI-generated: quality control? If pool: pool size per chapter? | **MAJOR** |
| 8 | **AI-driven games lack boundary specs** | §11.6 (Why Chain) | Why Chain is "AI-driven" but spec only provides example dialogues, not: acceptable response parsing rules, fallback for off-topic answers, language quality thresholds, how to handle student responses in 3 different languages. | **MAJOR** |
| 9 | **No content versioning strategy** | Absent | With 76,000+ items across 3 languages, how are content updates, corrections, and textbook alignment changes managed? | **MAJOR** |
| 10 | **Music, Art, Physical Education not addressed** | Absent | These are part of the K-11 curriculum. Are they explicitly out of scope? No statement either way. | **MAJOR** |
| 11 | **Story Mode media format not decided** | §11.9 | "Video: 30 fps, 720p minimum OR Illustrated panels: 1280×720." For 2,970 segments, this is a fundamental production decision that affects budget by 10–50×. | **MAJOR** |
| 12 | **Offline question pool sizing** | §9.5 | "Pre-generated pool of 3× expected question volume per cached session." For a chapter with 30+ questions across all games, that's 90+ cached questions per session × 7 sessions = 630+ questions pre-cached. Pool generation process undefined. | **MAJOR** |

### 4.3 Minor Gaps (Should Be Resolved Before Scale)

| # | Gap | Section | Impact |
|---|-----|---------|--------|
| 13 | Movement Breaks specified as "self-report" honor system (§11.12) — no verification | §11.12 | Data quality |
| 14 | Peer Teaching AI evaluation criteria undefined beyond "check for key terms, logical flow, correct facts" | §11.11 | Grading consistency |
| 15 | Memory Palace concept-to-location mapping not specified per subject | §11.14 | Content team ambiguity |
| 16 | Reflection Journal "teacher sees summary only" — summarization algorithm undefined | §11.10 | Privacy/utility tradeoff |

---

## 5. Media Production Requirements

### 5.1 Story Mode — The Dominant Cost Driver

Story Mode requires either video or illustrated panels for **2,970 unique segments** (3 subjects × 11 grades × 30 chapters × 3 segments per chapter).

#### Option A: Video Production

| Parameter | Value |
|-----------|-------|
| Total segments | 2,970 |
| Duration per segment | 90 seconds |
| Total runtime | 2,970 × 90s = 267,300s = **74.25 hours** |
| Format | 30 fps, 720p minimum, 16:9 |
| Narration languages | 3 (Uzbek Latin, Uzbek Cyrillic, Russian) |
| Total narrated video hours | 74.25 × 3 = **222.75 hours** |

**Production cost class (industry benchmarks):**
- Simple 2D animation: $1,000–5,000/minute → 4,455 minutes × $3,000 avg = **~$13.4M**
- AI-generated video (2026 capabilities): $100–500/minute → 4,455 minutes × $300 avg = **~$1.3M**
- Add 3× narration recording: $50–200/hour × 222.75 hours = **$11K–45K**

#### Option B: Illustrated Panels

| Parameter | Value |
|-----------|-------|
| Total segments | 2,970 |
| Panels per segment | 3–5 (estimated based on 90-second segments) |
| Total panels | **8,910–14,850** |
| Format | 1280×720 minimum, consistent art style per grade band |
| Art styles needed | 5 grade bands × consistent style = 5 art style guides |

**Production cost class:**
- Professional illustration: $100–500/panel → **$891K–$7.4M**
- AI-assisted illustration with human QA: $20–80/panel → **$178K–$1.2M**

#### Option C: Hybrid (Recommended for Reality)

Illustrated panels for Grades 1-6 (visual-heavy per §8.1), text-heavy for Grades 7-11:
- Grades 1-6: 6 grades × 3 subjects × 30 chapters × 3 segments × 4 panels = **6,480 panels**
- Grades 7-11: 5 grades × 3 subjects × 30 chapters × 3 segments = **1,350 text-focused segments** (minimal illustration)

### 5.2 Audio Production

| Content | Volume | Per Language | Total (3 languages) |
|---------|--------|-------------|---------------------|
| Story Mode narration | 74.25 hours | 74.25 hours | 222.75 hours |
| Memory Sprint question audio (optional) | ~165 hours at reading speed | 165 hours | 495 hours |
| Game UI sounds | ~50 unique sounds | Same | 50 sounds |
| Success/failure/combo SFX | 14 games × ~5 variants | Same across languages | 70 sound effects |

### 5.3 Total Media Production Summary

| Media Type | Volume | Cost Range (USD) |
|-----------|--------|-----------------|
| Story Mode video OR panels | 74.25 hrs video / 8,910–14,850 panels | $1.3M–$13.4M (video) or $178K–$7.4M (panels) |
| Audio narration (3 languages) | 222.75+ hours | $11K–$45K (studio) |
| Sound effects | ~120 unique sounds | $5K–$15K |
| Art style guides (5 grade bands) | 5 comprehensive guides | $25K–$100K |
| **ESTIMATED MEDIA TOTAL** | | **$220K–$13.6M** |

The range is enormous because the spec doesn't commit to video vs. panels, and doesn't specify whether AI-generated content is acceptable.

---

## 6. Production Timeline Estimate (Order of Magnitude)

### 6.1 Assumptions for Timeline

- Content team of 20 writers + 10 reviewers + 5 media producers
- AI-assisted content generation for question banks (realistic for 2026)
- Illustrated panels (not full video) for Story Mode
- IRT calibration via simulated response data + 2-month pilot

### 6.2 Phase Breakdown

| Phase | Duration | Dependencies | Output |
|-------|----------|-------------|--------|
| **Phase 0: Spec Completion** | 4–6 weeks | Resolve all 6 blocker gaps (§4.1) | Complete spec for all 6 subjects, narrative frameworks, authoring pipeline |
| **Phase 1: Content Architecture** | 4–6 weeks | Phase 0 | Textbook mapping, chapter structure, content management system, style guides |
| **Phase 2: Core Content Authoring (3 subjects)** | 16–24 weeks | Phase 1 | ~76,000 items drafted across Math, Reading, Science |
| **Phase 3: Media Production** | 12–20 weeks (parallel with Phase 2) | Art style guides from Phase 1 | 8,910–14,850 panels, audio narration, SFX |
| **Phase 4: IRT Calibration** | 8–12 weeks | Phase 2 (question banks exist) | Pilot testing, item parameter calibration |
| **Phase 5: Localization** | 8–12 weeks (parallel with Phase 4) | Phase 2 | 3-language versions of all content |
| **Phase 6: QA & Cultural Review** | 6–8 weeks | Phases 3, 4, 5 | Content accuracy, cultural authenticity, PISA alignment |
| **Phase 7: Additional Subjects** | 12–16 weeks | Phase 0 (subject specs) | English, History, CS content |

### 6.3 Total Timeline

| Scope | Best Case | Likely Case | Worst Case |
|-------|-----------|-------------|------------|
| 3 core subjects (parallel execution) | **8–10 months** | **12–14 months** | **18+ months** |
| 6 subjects | **12–14 months** | **16–20 months** | **24+ months** |

**Critical path:** Phase 0 (spec completion) → Phase 1 (architecture) → Phase 2 (content authoring) → Phase 4 (IRT calibration). The IRT calibration alone requires real student data, which means you cannot have a fully adaptive system at launch without a multi-month pilot program.

---

## 7. Missing Subject Coverage

### 7.1 Subjects Referenced but Unspecified

| Subject | Where Referenced | What's Missing | Production Impact |
|---------|-----------------|----------------|-------------------|
| **English** | §9.7 (Parent Portal), §3.1 (Flashcards example: "English as Foreign Language") | No PISA matrix, no progression table, no game adaptation rules, no content examples beyond one flashcard | Cannot produce any English content |
| **History** | §9.7, §2.4 (Why Chain example: "Silk Road"), §2.5 (Real-Life: "merchant on the Silk Road") | No PISA matrix, no progression table, scattered examples only | Cannot produce systematic History content |
| **Computer Science** | §9.7 only | Zero mentions anywhere else in the 2,063-line spec | Cannot produce any CS content |

### 7.2 Subjects Not Mentioned At All

| Subject | Status | K-11 Curriculum Relevance |
|---------|--------|--------------------------|
| Music | Absent | Part of Uzbekistan K-11 curriculum |
| Art | Absent | Part of Uzbekistan K-11 curriculum |
| Physical Education | Absent | Part of Uzbekistan K-11 curriculum |
| Geography | Absent | Part of Uzbekistan K-11 curriculum (referenced incidentally in cross-subject examples) |
| Uzbek Language/Literature | Absent | Core subject in Uzbekistan K-11 curriculum |
| Foreign Languages (beyond English) | Absent | Common in K-11 curriculum |

### 7.3 The Subject Scope Decision

The spec is fundamentally ambiguous about subject scope:

- **§1.2 (Principle 1):** Implies ALL subjects ("Textbook is Source of Truth")
- **§4.1–4.3 (PISA Matrices):** Only 3 subjects (Math, Reading, Science)
- **§9.7 (Parent Portal):** 6 subjects (adds English, History, CS)
- **Title:** "Universal Learning Flow for All Subjects & Grades" — implies *all* subjects

**Until subject scope is explicitly decided, content teams cannot plan resources.** This is the single most important decision for production planning.

---

## 8. Summary Findings Table

| Dimension | Status | Key Number | Verdict |
|-----------|--------|------------|---------|
| Content volume (3 subjects) | Calculable | ~76,000 items | Massive but achievable with AI assistance |
| Content volume (6 subjects) | Calculable | ~152,000 items | Requires dedicated content org |
| Localization | Requirements clear, process undefined | ~11.1M words (3 subjects, 3 languages) | Major effort, needs localization partner |
| Story Mode media | Format undecided | 2,970 segments | Decision needed: video vs. panels vs. hybrid |
| Spec completeness for content teams | Major gaps | 6 blocker-level gaps | **Cannot begin production** |
| IRT calibration | Process undefined | 19,800–29,700 items need calibration | Requires multi-month pilot |
| Content QA | Process undefined | No review workflows exist | **Cannot ensure quality** |
| Timeline (3 subjects) | Estimated | 12–14 months (likely) | Aggressive but possible |
| Timeline (6 subjects) | Estimated | 16–20 months (likely) | Requires parallel teams |

---

## 9. Recommendations (Prioritized)

1. **Decide subject scope immediately.** 3 subjects vs. 6 subjects is a 2× difference in everything — budget, team, timeline.
2. **Write the Grades 1-2 narrative framework** before any content production begins.
3. **Choose media format** (video / panels / AI-generated / hybrid) for Story Mode. This is a 10–50× cost swing.
4. **Define the content authoring pipeline** — tooling, CMS, workflow, roles. Without this, 76,000+ items cannot be managed.
5. **Design the IRT calibration plan** — this is the longest-lead item. Consider launching with non-adaptive quiz mode and calibrating post-launch.
6. **Complete Section 3.2** — the placeholder needs per-game grade-level adaptations and accessibility specs.
7. **Establish cultural review board** — Uzbek educators, cultural consultants, and linguists must validate content before launch.
8. **Clarify the textbook question** — identify specific textbooks, secure digital content rights, plan for textbook update cycles.

---

*Assessment complete. All estimates include explicit assumptions. Numbers represent 3 core subjects unless otherwise stated. The 6-subject scenario doubles most figures.*

*This document does not sugarcoat. The HES v2.0 engine design is excellent. The content production readiness is not.*
