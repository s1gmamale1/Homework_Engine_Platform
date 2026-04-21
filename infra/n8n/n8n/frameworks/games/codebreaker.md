# Game: Codebreaker (Mastermind variant)

## Type: Interactive Catalog
## Bloom's: L2-L4 | PISA: L1-L2

## What It Is
Student guesses a secret "code" (pattern, rule, or answer) through limited attempts.
Each wrong attempt gives feedback clues. Content questions gate each guess.

## Matematika Use Cases
- "Find the rule" number sequences: 2, 4, 8, 16, __ (double each time)
- Missing number puzzles: 3 × __ = 24
- Ratio patterns: if 3:5, then 12:__
- Order of operations: which brackets change the answer?

## Item Format
Each item = a puzzle with:
- The pattern/sequence to decode
- 3-4 possible answers (only 1 correct)
- A clue given after wrong answer (narrows the options)

## Von Restorff Anchor (Slot 2 requirement)
At least 1 item must be surprising or visually distinctive:
- Unusual math fact: "Bu son 1 million gacha bo'lgan sonlarning o'rta arifmetig'i!"
- Unexpected pattern: a visual sequence not just numbers
- Humorous framing if appropriate for G5

## Items Per Session
4-6 puzzles per game

## Output Format
{
  game_name: "Codebreaker",
  items[]: {
    item_number,
    puzzle_description,
    options[],
    correct_answer,
    clue_on_wrong: string,
    is_von_restorff_anchor: boolean,
    surprise_element (if anchor): string
  }
}
