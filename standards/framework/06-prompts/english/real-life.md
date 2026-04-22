---
subject: english
phase: real-life
mode: hard
grades: 5-11
cefr: A1+ to B2
version: 1.0
supersedes: reference_nets_english_master_instruction.md (Section 7 per-phase block)
originSessionId: 190c4f0e-0c6e-4917-937c-8be234f1347a
---
# Prompt: Real-Life Challenge — English (Phase 4)

You are building the Real-Life Challenge (Phase 4) for an English Hard mode session. The student has completed Preview, Flash Cards, Sprint, Reading, and Game Breaks. Now they apply everything to ONE deep real-world scenario as THE EXPERT.

This phase tests whether Preview's Word→Structure Translation teaching actually worked. The student must read a scenario, identify the language target in context, and produce correct English under professional pressure.

## Input

- Textbook page (image or text)
- All previous phase outputs
- Grade: G5–G11 (English)

## Output

ONE scenario with 3 open-ended questions. Answer key included.

---

## Scenario Construction

**First-person POV mandatory.** The student IS the professional.

> "You are [role]. Your task is..."

Never third person ("Dilnoza needs to..."). Always direct: "You", "Your".

**Pick a professional role from the grade-appropriate list:**
- G5–6: LOCAL ONLY — Chorsu bozor helper, mahalla football captain, school monitor, young Samarkand kid-tourist guide, family bakery helper, Telegram-group admin
- G7–8: Tashkent IT intern, Chorsu export seller, Hilton Tashkent receptionist, BBC Tashkent young reporter, NASA young-scholar, airline ground staff, CoderDojo mentor
- G9–10: NASA stringer, BBC Tashkent reporter trainee, UN interpreter trainee, airline cabin crew applicant, Uzbekistan Airways customer-service lead, Presidential School IELTS tutor, Samarkand heritage-site docent
- G11: IELTS Task-2 essayist, TEDx Tashkent speaker, Cambridge UCAS personal-statement writer, startup pitch presenter (Tashkent IT Park), UN MUN delegate

**Apply the Wise Status Injection Recipe:**
1. Assign a high-status, credible professional role
2. Anchor the scenario in UZ (55%) or global (45%) — do not exceed 45% global
3. Close the scenario frame with: "Your precision builds the Third Renaissance." OR "Your accuracy meets Global Standards."

**G5–6: W5H scaffold required.** Include 4 of 6 W5H branches (Who / What / When / Where / Why / How) as visible scaffolding inside the scenario prompt.

**Scope lock:** Every skill tested must have been taught in Preview. No new grammar or vocabulary. Same difficulty as the hardest Preview example — different context, different numbers/names.

---

## Sub-question construction

3 questions per scenario:
1. **Application** — use the chapter's grammar/vocab to complete a realistic task (Bloom L3)
2. **Analysis** — compare two English options and explain which is correct for this context (Bloom L4)
3. **Transfer** — adapt the language from this scenario to a different but related professional moment (Bloom L4–L5)

Each question:
- Requires producing English (writing a sentence, a short dialogue, a 2–3 sentence response)
- Uses grade-allowed tenses only in the model answer
- Tagged: `[Bloom: LX | PISA: LX]`

---

## Example (G7 pro-role)

> You are a **BBC Tashkent junior reporter**. Your editor has asked you to write a 3-sentence update on the new IT Park expansion in Tashkent. You **have already** visited the site and interviewed two engineers. Your accuracy meets Global Standards.

> **Q1.** Write 3 sentences reporting what you saw at the IT Park. Use the present perfect at least once.
> `[Bloom: L3 | PISA: L2]`
> Model answer: "The new IT Park expansion **has added** 15,000 square metres of co-working space. Engineers **have installed** fibre-optic cables across the entire building. The project **has already attracted** 20 international startups."

> **Q2.** Your editor says: "Use past simple, not present perfect." Which sentence below fits the past simple correctly — and why?
> A) "The engineers installed the cables last Tuesday." B) "The engineers have installed the cables last Tuesday."
> `[Bloom: L4 | PISA: L2]`
> Model answer: A is correct. "Last Tuesday" is a fixed past time → past simple. Present perfect is banned when the time is named.

> **Q3.** Now write one sentence about the IT Park for a formal UN report. Upgrade the register from your news update.
> `[Bloom: L4 | PISA: L3]`
> Model answer: "The Tashkent IT Park expansion, completed in March 2024, **has significantly enhanced** Uzbekistan's digital infrastructure capacity."

---

## Rules

- ONE scenario only — not multiple
- First-person "You" POV. Never third person.
- All grammar must come from Preview content — no new methods
- Every question tagged with Bloom + PISA
- G5–6: W5H scaffold visible in scenario prompt
- Model answers use grade-allowed tenses only — never a banned tense
- Language: student-facing English. UZ bridge allowed in model answers.
- No bazaar/village/shopkeeper clichés
- Apply Wise Status Injection Recipe on every scenario
- **Visuals:** Generate actual SVG code inline where visuals aid understanding. Priority: SVG > Mermaid > ASCII. Use SVG for: timelines (past/present/future bridge), stress-dot patterns (Ooo / oOoo rendered as actual dots), IPA pronunciation charts, sentence diagrams (subject/verb/object trees), word-family trees (suffix branching), collocation grids, Buzan mind maps for vocabulary domains. Use Mermaid for: concept maps, decision trees, grammar-rule flowcharts. Keep SVGs under 300×200px, legible on mobile. Place SVG immediately after the text it illustrates. ASCII boxes still OK for the 8-panel preview card layout — they are the UI chrome, not the teaching visual.
