# Game: Tic Tac Toe vs AI

## Type: Default Pool (also listed in Interactive Catalog)
## Bloom's: L1-L2 | PISA: L1

## What It Is
Classic 3×3 grid. Student answers a content question correctly to place their X.
AI opponent plays O using minimax strategy. First to 3 in a row wins.

## Matematika Use Cases
- Multiplication/division quick recall
- Formula recognition (which formula = which shape?)
- Number comparison (which is larger: ¾ or 0.8?)
- Basic arithmetic verification (is this calculation correct?)

## Item Format
Each move attempt = 1 question.
Wrong answer = X not placed, AI still plays O.
Game ends when student wins or AI wins.

## Items Per Session
4-6 questions total (enough for 2-3 games or 1 full game with retries)

## Output Format
{
  game_name: "Tic Tac Toe vs AI",
  items[]: {
    item_number,
    question_text,
    format (mc/tf),
    options[] (if mc),
    correct_answer,
    wrong_feedback: string
  }
}
