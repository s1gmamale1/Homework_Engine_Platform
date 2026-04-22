# Prompt: Preview — English — Easy Mode

You are building the Preview phase for an English homework session in Easy mode. Used for vocabulary-only units and review chapters with no new grammar. You will receive a textbook unit. Your job is to create 5 teaching panels in student-friendly English.

## Input

- Textbook unit (image or text)
- Detected CEFR level (from `classify.md`): A1 · A1+ · A2 · A2+ · B1 · B1+ · B2
- Grade (for pro-roles in Panel 5 only)

## Output

5 panels in order. Student-facing English throughout. UZ bridge lines use formal "Siz" — never "sen".

Sentence count per panel by CEFR level: A1: 4-5 · A2: 6-7 · B1: 8-10 · B2: 10-12.

---

## Panel 1: Summary

Reframe the unit around something useful the student can DO with the new vocabulary — not a restatement of the book title.

- 2 big ideas in plain student-English
- Optional 1-line attributed quote (≤125 chars) — prefer Navoiy, Ibn Sino, Malala, Obama
- No jargon, no fragments

## Panel 2: Better Explanation

The hidden rule or trick the textbook shows but never explains.

- One mental model, spelling rule, or stress pattern the chapter demonstrates by example only
- Mandatory UZ↔EN bridge on at least one target item
- Stress + IPA for any 2+-syllable word with non-initial stress or known UZ/RU mis-stress (B1+ only)

## Panel 3: Examples

3 examples lifted directly from the chapter with page refs.

- Bold the target word or form on every occurrence
- At least one example must demonstrate the Panel 2 rule in action
- Annotate any spelling trap, false friend, or register note inline
- Never invent sentences not in the source chapter

## Panel 4: Real-Life Research

How this vocabulary lives in the world right now.

- Real 2020+ sources (BBC, Tashkent IT Park, NASA, Samarkand tourism board, UN updates)
- One explicit Uzbekistan parallel anchoring the global fact locally
- Concrete, dateable situations — no abstract "you'll need this later"

## Panel 5: Industry Application

Where professionals use this English daily. Pick 2-3 roles from the grade-appropriate set:

- **G5-6:** Chorsu bozor helper, school monitor, mahalla football captain, Samarkand kid-tourist guide
- **G7-8:** Tashkent IT intern, Hilton receptionist, BBC Tashkent reporter, airline ground staff
- **G9-10:** BBC stringer, UN interpreter trainee, Uzbekistan Airways customer-service lead, IELTS tutor
- **G11:** IELTS Task-2 essayist, TEDx Tashkent speaker, UCAS personal-statement writer, startup pitcher

For each role: concrete task + what goes wrong if the English is incorrect.

---

## Rules

- Language: student-friendly English. UZ bridge lines use formal "Siz" only, never "sen".
- Avg sentence length by level: A1 ≤9 words · A2 9-12 · B1 12-16 · B2 18-25.
- Tenses: level-allowed set only — never a banned tense, not even in examples.
- UZ↔EN bridge: A1 every panel · A2+ Panels 2 and 5 minimum.
- 55/45 Uzbekistan/global balance. Modern 2020+ contexts only. No cowboy/cricket/baseball clichés.
- Every example bold-marks the target form and traces to the actual chapter — never invent.
- Each panel closes with `[Bloom: LX | PISA: LX]` tag.
- Visuals: inline SVG where it aids understanding (stress-dot pattern, word-family tree, collocation grid). Under 300×200px. Priority SVG > Mermaid > ASCII.
