# Prompt: Flash Cards — Math + Algebra — Easy Mode

You are building the Flash Card deck for a Math/Algebra homework session (Easy mode). You receive the textbook page and the Preview output from the previous step. Your job is to extract every formula, term, and rule the student will need and turn them into a reference deck.

Flash Cards are a REFERENCE tool, not practice. If a card asks the student to DO something — solve, calculate, explain — it does not belong here.

## Input

- Textbook page (image or text)
- Preview output (from previous step)
- Grade: G5-6 (Matematika) or G7-9 (Algebra)

## Output

**5-7 cards** (G5-6) or **6-8 cards** (G7-9), organized into 4 clusters.

---

## Card Structure

Every card has exactly two faces:

**Front:** The term, formula name, or rule name. Max 10 words. No context, no explanation.

**Back:** Three parts:
1. Full definition or formula
2. Visual example in one line (formula shown in context or with a simple case)
3. `Hook:` — one-line mnemonic aid (≤15 words). Use: vivid image, rhyme, acronym, association, or story fragment. In Uzbek.

Example card:
> **Front:** Yuza formulasi (to'g'ri to'rtburchak)
> **Back:** S = a × b — tomonlarni ko'paytiramiz.
> Misol: a = 5 m, b = 3 m → S = 15 m²
> Hook: "Stol ustini bo'yash uchun ikkala tomonni bilish kerak."

---

## 4 Clusters

Organize cards into these clusters in this order:

| Cluster | What goes here | Math examples |
|---------|---------------|---------------|
| **Names** | Key terms, vocabulary, classifications | "Natural son", "Kasr", "O'zgaruvchi", "Koeffitsient" |
| **Formulas** | Equations, rules, procedures | "S = a × b", "a(b+c) = ab + ac", "x = (c−b)/a" |
| **Decisions** | When to use what, conditions, exceptions | "Maxrajlar teng bo'lsa — suratlarni qo'shing", "Nol ga bo'lish mumkin emas" |
| **Insights** | Why it works, connection to origin | "Ko'paytirish — bu tez qo'shish usuli", "Al-Xorazmiy bu usulni tartibga solgan" |

Most important card in each cluster goes first.

---

## Required Cards

- Every formula from the textbook page that appears in the homework → gets a card
- Every new term introduced in the chapter → gets a card
- **1 "Common Mistake" card** — show the typical error and the fix. Place in Decisions cluster.
  > Front: "Tez-tez uchraydigan xato"
  > Back: [the error] → [why it's wrong] → [the fix]
  > Hook: [memorable reminder]

---

## Rules

- One concept per card. No "and also" joining two ideas.
- NO practice problems, NO "solve this", NO questions on cards
- Every card back includes exactly one `Hook:` line
- Language: Uzbek, "Siz" formal
- Cards are returnable throughout homework — student can open them anytime, no penalty
- 0-2 cards may include a visual description on the back: `[Diagram: ...]`
- Cover everything the student will encounter in the homework — no formula or term should appear later without a card for it
