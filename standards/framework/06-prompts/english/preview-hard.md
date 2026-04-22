---
subject: english
phase: preview
mode: hard
grades: 5-11
cefr: detected per unit (A1 to B2) via classify.md
grade-anchored-fields: [pro-roles, memory-palace-locations]
level-anchored-fields: [question-count, word-count, tense-set, card-count, complexity]
version: 1.1
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Preview — English (Hard mode only, all grades)

**STANDALONE MODE:** If pasted alone, silently classify the unit (4-signal method), silently extract metadata, then produce only the preview (8-panel swipe cards) output below. Stop when the phase is complete.

---

You are building the Preview phase for an English homework session. You will receive a textbook page. Your job is to create 8 teaching panels in student-friendly English that fully prepare the student to use this chapter's language in real-world situations.

English is always Hard mode. There is no preview-easy.md. Build all 8 panels every time.

## Input

- Textbook page (image or text)
- Detected CEFR level (from classify.md): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for pro-roles in Panel 6 only)

## Output

8 panels in order. Language: student-friendly English throughout. Formal "Siz" in UZ bridge lines only — never "sen". Each panel ~53-char-wide ASCII box, ~18 lines tall.

---

## CEFR Level Parameters

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

| Parameter | A1 | A2 | B1 | B2 |
|---|:-:|:-:|:-:|:-:|
| Panel sentence count | 4–5 | 6–7 | 8–10 | 10–12 |
| Word→Structure mini-cases (Panel 5) | 1 | 2 | 2–3 | 3 |

A1+ gets 5 sentences (upper A1 range). A2+ gets 7 sentences (upper A2 range). B1+ gets 10 sentences (upper B1 range).

**Tenses allowed by level:**
- **A1:** present simple + can + have got only
- **A2:** + past simple regular, going-to, have to
- **B1:** + past continuous, present perfect, will, 1st conditional, modals (should/might/could)
- **B2:** full arsenal — all tenses, inversion, cleft, participles, modal perfects

Never use a tense banned at the detected level — not even in examples.

---

## Panel 1: Summary

Reframe the chapter as something useful the student can DO, not a definition to memorize.

- 2 big ideas in plain student-English. No restatement of the book title.
- Optional 1-line attributed quote (≤125 chars) — prefer Navoiy, Ibn Sino, Malala, Obama, Rowling.
- No jargon. Full sentences, not fragments.
- Sentence count: per level table above.

## Panel 2: Better Explanation

The hidden rule or trick the textbook shows but never explains.

- One explicit mental model OR one algebraic grammar formula (e.g., `(Wh-) + did + subject + base verb + ?`).
- Mandatory UZ↔EN bridge: map the English structure to its Uzbek grammatical equivalent with a labeled side-by-side.
- Show WHY the form exists — the logic behind it, not just the shape.
- Stress + IPA for any 2+-syllable target word with non-initial stress or known UZ/RU mis-stress (B1+ levels only).
- Inline SVG strongly encouraged: past/present/future timeline bridge, sentence-diagram tree (subject/verb/object), or stress-dot IPA chart (Ooo / oOoo rendered as actual dots).
- Sentence count: per level table above.

## Panel 3: Examples

3 examples lifted directly from the chapter with page refs.

- Bold the target form on every occurrence.
- At least one example must demonstrate the Panel 2 rule in action.
- Never invent sentences not in the source chapter.
- Annotate any spelling trap, register note, or false friend on the example line.
- Sentence count: per level table above.

## Panel 4: Real-Life Research

How this concept lives in the world right now.

- Real 2020+ sources (BBC reports, Tashkent IT Park announcements, NASA Artemis, Samarkand tourism board, UN updates).
- One explicit Uzbekistan parallel anchoring the global fact locally.
- No abstract "you'll need this later" — concrete, dateable situations.
- Sentence count: per level table above.

## Panel 5: Word → Structure Translation

Teach the student HOW to read a real-world English sentence, identify the grammar/vocab target, and produce it.

THIS IS THE BRIDGE TO REAL-LIFE. Without this panel, Phase 4 becomes guesswork.

Structure: mini-cases per level table (A1: 1 · A2: 2 · B1: 2–3 · B2: 3), building in complexity.
Each mini-case: real-world sentence → extract the target pattern → show UZ↔EN mapping → produce the form.

> "NASA announced that the Artemis crew **had completed** their training."
> Target: present perfect (has/have + V3). UZ: "bajargan edi" → EN past result.
> Extract: subject + has/have + V3. Produce your own: "Samarkand **has become** a UNESCO site."

- First case: obvious, one clear target
- Last case (B1+/B2 only): two possible patterns, student must choose the correct one
- Mandatory UZ↔EN bridge in each case
- Inline SVG strongly encouraged: sentence-diagram tree splitting subject / auxiliary / V3, or a word-family tree branching suffixes (-ed, -ing, -er, -est) off the root.

## Panel 6: Industry Application

Where professionals use this English daily.

Pick 2–3 roles from the grade-appropriate pro-roles:
- G5–6: Chorsu bozor helper, school monitor, mahalla football captain, Samarkand kid-tourist guide
- G7–8: Tashkent IT intern, Hilton receptionist, BBC Tashkent reporter, airline ground staff
- G9–10: BBC stringer, UN interpreter trainee, Uzbekistan Airways customer-service lead, IELTS tutor
- G11: IELTS Task-2 essayist, TEDx Tashkent speaker, UCAS personal-statement writer, startup pitcher

For each role: concrete task + what goes wrong if the English is incorrect.
- Sentence count: per level table above.

## Panel 7: Mental Model

One visual or analogy that compresses the entire lesson into one image.

- Examples: "did = time machine" · "present perfect = bridge from past to now" · "passive = spotlight on the action, not the actor" · "modal + base verb = a remote control for certainty"
- Must be memorable and strange enough to stick.
- Apply the UZ↔EN bridge to the analogy itself.
- Inline SVG strongly encouraged: render the analogy itself (bridge, spotlight, remote control, time machine) or a Buzan mind map with the grammar target at the center and 4–6 radiating branches (form / meaning / UZ bridge / example / trap / register).
- Sentence count: per level table above.

## Panel 8: Why This Matters

Two parts:
1. What BREAKS if you don't know this — mistimed verb, wrong register, failed interview, embarrassing false friend
2. What OPENS UP — you can pass DTM-level questions, speak with confidence, write competitive applications

End with BOST goal prompt: "Bugun [actual topic name] ni nimani bilmoqchisiz?" — stored and resurfaced in Reflection.
- Sentence count: per level table above.

---

## Rules

**Parameters:** question/card/word counts from the CEFR level table (set by classify.md). Cultural anchors (pro-roles, locations) from the grade (set by instruction.md Step 3).

- Language: student-friendly English. Formal "Siz" in UZ bridge lines only, never "sen".
- Avg sentence length by level: A1: ≤9 words · A2: 9–12 words · B1: 12–16 words · B2: 18–25 words.
- Tenses: level-allowed set only. Never a banned tense — not even in examples.
- UZ↔EN bridge MANDATORY on Panels 2, 5, 7 at minimum. A1 levels: every panel.
- Stress + IPA: mandatory B1+ for any 2+-syllable word with non-initial stress or known UZ/RU mis-stress.
- 55/45 Uzbekistan/global balance. Modern 2020+ contexts only. No cowboy/cricket/baseball clichés.
- Every panel: bold target form on actual chapter examples. Never invent.
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
- Each panel closes with `[Bloom: LX | PISA: LX]` tag outside the box.
- No segment labels, no "Panel 1:" headings inside the box — title only.
