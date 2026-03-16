class TicTacToe:
    """
    A basic 3x3 Tic-Tac-Toe implementation.
    Works fine for 3x3, but NOT designed for NxN or future extensions.
    """

    def __init__(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.current_player = "X"
        self.game_over = False
        self.winner = None

    def make_move(self, row, col):
        if self.game_over:
            print("Game is already over!")
            return False

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position!")
            return False

        if self.board[row][col] is not None:
            print("Cell already occupied!")
            return False

        self.board[row][col] = self.current_player

        if self._check_winner():
            self.game_over = True
            self.winner = self.current_player
        elif self._is_board_full():
            self.game_over = True
            self.winner = None  # Draw
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

        return True

    def _check_winner(self):
        b = self.board
        p = self.current_player

        # Check rows
        for row in range(3):
            if b[row][0] == p and b[row][1] == p and b[row][2] == p:
                return True

        # Check columns
        for col in range(3):
            if b[0][col] == p and b[1][col] == p and b[2][col] == p:
                return True

        # Check diagonals
        if b[0][0] == p and b[1][1] == p and b[2][2] == p:
            return True
        if b[0][2] == p and b[1][1] == p and b[2][0] == p:
            return True

        return False

    def _is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def display(self):
        symbols = {None: ".", "X": "X", "O": "O"}
        print()
        for row in self.board:
            print(" | ".join(symbols[cell] for cell in row))
            print("-" * 9)
        print(f"Current player: {self.current_player}")
        if self.game_over:
            if self.winner:
                print(f"Winner: {self.winner}")
            else:
                print("It's a draw!")
        print()


if __name__ == "__main__":
    game = TicTacToe()
    game.display()

    # Example game
    moves = [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]  # X wins top row
    for row, col in moves:
        print(f"Player {game.current_player} plays ({row}, {col})")
        game.make_move(row, col)
        game.display()
