# NETS Library

The Library is the **content knowledge base** — the source of truth for everything students learn and interact with.

It is distinct from `system/games/` (which defines *how* games work mechanically) — the Library defines *what content* goes inside them.

---

## Structure

```
library/
├── framework/          ← Library Framework spec (rules for how content is organized)
├── catalog/            ← Master index of all games and activities
├── games/              ← Per-game content: questions, answers, rubrics, prompts
│   ├── _template/      ← Copy this when adding a new game
│   └── [game-name]/
└── content-templates/  ← Standard schemas: question types, rubric formats
```

---

## How content flows

```
Textbook → Content Engine (Codex) → Library/games/[game]/ → System/games/[game]/
```

1. Source material comes from textbooks (grade × subject × language)
2. Codex agent produces structured content per the `content-templates/` schemas
3. Output lands in `library/games/[game]/` organized by grade, subject, Bloom's level
4. The game engine in `system/games/[game]/` reads from here at runtime

---

## Standards every content item must carry

| Field | Description |
|-------|-------------|
| `standard_ref` | Textbook chapter/section reference |
| `blooms_level` | 1–6 (Remember → Create) |
| `pisa_level` | 1–6 |
| `transition_skill` | The transferable skill targeted |
| `language` | `uz` / `ru` |
| `grade` | 1–11 |
