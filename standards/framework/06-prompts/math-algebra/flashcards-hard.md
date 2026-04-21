# Prompt: Flash Cards — Math + Algebra — Hard Mode

You are building the Flash Card deck for a Math/Algebra homework session (Hard mode). You receive the textbook page and the Preview output from the previous step. Your job is to extract every formula, term, and rule the student will need and turn them into a reference deck.

Flash Cards are a REFERENCE tool, not practice. If a card asks the student to DO something — solve, calculate, explain — it does not belong here.

Hard mode has more phases (Real-Life, Final Challenge) so the deck must cover more ground — including formulas needed for word-problem translation and boss-level application.

## Input

- Textbook page (image or text)
- Preview output (from previous step)
- Grade: G5-6 (Matematika) or G7-9 (Algebra)

## Output

**8 cards** (G5-6) or **10-12 cards** (G7-9), organized into 4 clusters.

---

## Card Structure

Every card has exactly two faces:

**Front:** The term, formula name, or rule name. Max 10 words. No context, no explanation.

**Back:** Three parts:
1. Full definition or formula
2. Visual example in one line (formula shown in context or with a simple case)
3. `Hook:` — one-line mnemonic aid (≤15 words). Use: vivid image, rhyme, acronym, association, or story fragment. In Uzbek.

Example card:
> **Front:** Diskriminant
> **Back:** D = b² − 4ac — kvadrat tenglamaning yechimlar sonini aniqlaydi.
> Misol: a=1, b=−5, c=6 → D = 25−24 = 1 > 0 → ikkita yechim.
> Hook: "D musbat — ikkita eshik ochiq. D nol — bitta. D manfiy — yopiq."

---

## 4 Clusters

Organize cards into these clusters in this order:

| Cluster | What goes here | Math examples |
|---------|---------------|---------------|
| **Names** | Key terms, vocabulary, classifications | "Kvadrat tenglama", "Diskriminant", "Ildiz", "Parabola" |
| **Formulas** | Equations, rules, procedures | "D = b²−4ac", "x = (−b±√D)/2a", "S = ½ah" |
| **Decisions** | When to use what, conditions, exceptions | "D > 0 → 2 yechim, D = 0 → 1, D < 0 → yechim yo'q", "Nol ga bo'lish mumkin emas" |
| **Insights** | Why it works, connection to origin, real-world bridge | "Diskriminant — tenglama 'xarakterini' ko'rsatadi", "Al-Xorazmiy geometrik usulda yechgan" |

Most important card in each cluster goes first.

---

## Required Cards

- Every formula from the textbook page → gets a card
- Every new term → gets a card
- **1 "Common Mistake" card** — typical error + fix. Place in Decisions cluster.
  > Front: "Tez-tez uchraydigan xato"
  > Back: [the error] → [why it's wrong] → [the fix]
  > Hook: [memorable reminder]
- G7-9: **1 notation card** — correct way to write equations, function notation, or balance notation. Place in Formulas cluster.
- **1 word-problem bridge card** — key phrase that signals which formula to use. Place in Decisions cluster.
  > Front: "Matnli masalada qaysi formulani tanlash"
  > Back: "'har biri' → ko'paytirish. 'qancha qoldi' → ayirish. 'teng taqsimlash' → bo'lish."
  > Hook: "Kalit so'z — formulaga yo'l ko'rsatuvchi."

---

## Rules

- One concept per card. No "and also" joining two ideas.
- NO practice problems, NO "solve this", NO questions on cards
- Every card back includes exactly one `Hook:` line
- Language: Uzbek, "Siz" formal
- Cards are returnable throughout homework — student can open them anytime, no penalty
- 0-2 cards may include a visual description: `[Diagram: ...]`
- Cover everything — Real-Life scenario and Final Challenge will reference these formulas. No formula should appear in a later phase without a card for it.
