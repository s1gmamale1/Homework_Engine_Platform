# Game: Tile Match

## Type: Default Pool
## Bloom's: L1-L2 | PISA: L1

## What It Is
Drag-and-drop matching pairs. Student matches terms to definitions, formulas to visuals,
fractions to decimals, numbers to expanded form, etc.

## Item Format
Each item = a PAIR: {left_item, right_item}
Student drags left items to match right items (or vice versa).

## Good Examples (Matematika)
- Formula ↔ Visual: "½ × b × h" ↔ [triangle area diagram]
- Fraction ↔ Decimal: "¾" ↔ "0.75"
- Number ↔ Expanded form: "325 146" ↔ "300 000 + 25 000 + 100 + 46"
- Term ↔ Definition: "maxraj" ↔ "kasrning pastki qismi"

## Bad Examples (DO NOT USE)
- Matching word "Algebra" to dictionary definition (too L1/trivial)
- Matching without visual component for Math

## Items Per Session
4-6 pairs per game

## Output Format
{
  game_name: "Tile Match",
  pairs[]: {
    pair_number,
    left_item: string,
    right_item: string,
    explanation: string (why they match)
  }
}
