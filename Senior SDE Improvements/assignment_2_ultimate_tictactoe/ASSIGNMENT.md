# Assignment 2: Ultimate Tic-Tac-Toe (Inheritance & Abstraction)

## Difficulty: ★★★☆☆
## Focus: Inheritance, Method Overriding, Abstraction, Reusing Base Class Logic

---

## Background

This is the exact type of problem asked in SDE2 interviews. You're given a working `TicTacToe` base class. Your job is to **subclass** it to implement Ultimate Tic-Tac-Toe — a game where each cell of a 3x3 grid contains an entire Tic-Tac-Toe game inside it.

**Rules:** https://www.thegamegal.com/2018/09/01/ultimate-tic-tac-toe/

---

## Files

| File | What To Do |
|------|-----------|
| `game.py` | Base `TicTacToe` class. You may modify it if needed, but the goal is to **extend**, not rewrite. |
| `ultimate.py` | **Create this file.** Your `UltimateTicTacToe` class goes here. |
| `test_game.py` | Test suite. **Do NOT modify.** All tests must pass. |

---

## Rules of Ultimate Tic-Tac-Toe

1. The board is a **3x3 grid of sub-boards**, each sub-board is a **3x3 Tic-Tac-Toe game**.
2. The **first move** can be in ANY sub-board, at any position.
3. When a player places a mark at local position `(r, c)` within a sub-board, the **next player MUST play in sub-board `(r, c)`** on the outer grid.
4. If the target sub-board is **already won or full**, the next player may play in **ANY available sub-board**.
5. A player **wins a sub-board** by getting 3 in a row within that sub-board.
6. A player **wins the game** by winning **3 sub-boards in a row** on the outer grid (row, column, or diagonal).
7. If all sub-boards are decided (won or drawn) and no one has 3 outer in a row, it's a **draw**.

---

## Requirements

### Your `UltimateTicTacToe` class MUST:

1. **Inherit from `TicTacToe`** (the class in `game.py`).

2. **Override `make_move`** with signature: `make_move(outer_row, outer_col, inner_row, inner_col)`
   - Validates outer position (0-2) and inner position (0-2)
   - Enforces the "sent to sub-board" rule (rule 3 above)
   - Enforces the "free choice when target is won/full" rule (rule 4)
   - Rejects moves in won or full sub-boards
   - Rejects moves after game is over
   - Returns `True` for valid moves, `False` for invalid

3. **Use `TicTacToe` instances as sub-boards.** Each of the 9 sub-boards should be a `TicTacToe` object. Reuse the base class — don't rewrite win-checking logic.

4. **Implement these query methods:**
   - `get_sub_board_cell(outer_row, outer_col, inner_row, inner_col)` → `"X"`, `"O"`, or `None`
   - `get_sub_board_winner(outer_row, outer_col)` → `"X"`, `"O"`, or `None`
   - `get_active_sub_board()` → `(row, col)` tuple or `None` (None = free choice)

5. **Track outer game state** — use the base `TicTacToe`'s properties (`game_over`, `winner`, `current_player`) for the overall game state.

---

## Design Decisions You Need to Make

These are the things an interviewer would evaluate:

- **What to inherit vs. what to override?** The base class has `make_move`, `_check_winner`, `_switch_player`, etc. Which do you reuse? Which do you override?
- **How to compose sub-boards?** Each sub-board IS a TicTacToe. How do you store and interact with them?
- **Where does the "sending" logic live?** This is new behavior unique to Ultimate. How do you cleanly add it?
- **How to track outer-board wins?** You have 9 sub-boards with winners. The outer game is itself a tic-tac-toe of winners. Can you reuse TicTacToe for this too?

---

## Hints

1. Your class will likely have a **3x3 grid of `TicTacToe` objects** for the sub-boards.
2. Consider using **another `TicTacToe` instance** to track the outer game (which sub-boards are won by whom).
3. The base class's `current_player` and `game_over` should be used for the OUTER game state. Don't create parallel state.
4. When a sub-board is won, "place" the winner's mark on the outer board.

---

## Run Tests

```bash
cd assignment_2_ultimate_tictactoe
pytest test_game.py -v
```

---

## Evaluation Criteria

| Criteria | What I'm Looking For |
|----------|---------------------|
| **Inheritance** | Did you actually subclass TicTacToe, or did you just write a new class? |
| **Reuse** | Are you reusing base class win-checking for sub-boards and outer board? |
| **Abstraction** | Is the boundary between "outer game logic" and "sub-board logic" clean? |
| **Encapsulation** | Is internal state (sub-boards, active board tracking) properly hidden behind methods? |
| **No duplication** | Did you avoid rewriting win-check / board-full logic that's already in the base class? |
| **Correctness** | All tests pass |

---

## Get Started

1. Read `game.py` — understand the base class API
2. Read `test_game.py` — understand what interface is expected
3. Create `ultimate.py` with your `UltimateTicTacToe` class
4. Run tests incrementally — start with the inheritance tests, then basic moves, then sending logic
5. Run `pytest test_game.py -v` and get everything green

Good luck — this is your interview redemption round.
