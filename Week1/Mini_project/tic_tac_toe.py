# Mini-project 1: Tic Tac Toe


def create_board():
    """Return a fresh 3x3 board as a list of 9 empty strings."""
    return [" "] * 9


def display_board(board):
    """Print the board in a readable 3x3 grid."""
    print()
    for row in range(3):
        cells = board[row * 3 : row * 3 + 3]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]} ")
        if row < 2:
            print("  ---------")
    print()


def get_move(board, player):
    """Prompt the current player for a valid move (1-9)."""
    while True:
        try:
            move = int(input(f"  Player {player}, choose a cell (1-9): ")) - 1
            if move < 0 or move > 8:
                print("  Please enter a number between 1 and 9.")
            elif board[move] != " ":
                print("  That cell is already taken. Try again.")
            else:
                return move
        except ValueError:
            print("  Invalid input. Enter a number between 1 and 9.")


def check_winner(board, player):
    """Return True if the given player has a winning line."""
    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],             # diagonals
    ]
    return any(all(board[i] == player for i in line) for line in winning_lines)


def is_draw(board):
    """Return True if the board is full and no winner exists."""
    return all(cell != " " for cell in board)


def play_game():
    """Run a single game of Tic Tac Toe."""
    board = create_board()
    current_player = "X"
    scores = {"X": 0, "O": 0, "Draws": 0}

    print("\n" + "=" * 35)
    print("        TIC TAC TOE")
    print("=" * 35)
    print("  Cells are numbered 1-9:")
    print("   1 | 2 | 3")
    print("   ---------")
    print("   4 | 5 | 6")
    print("   ---------")
    print("   7 | 8 | 9")

    while True:
        display_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            scores[current_player] += 1
            print(f" Player {current_player} wins!\n")
        elif is_draw(board):
            display_board(board)
            scores["Draws"] += 1
            print(" It's a draw!\n")
        else:
            # Switch player and continue
            current_player = "O" if current_player == "X" else "X"
            continue

        # Round over show scores and ask to replay
        print(f"  Scores → X: {scores['X']}  O: {scores['O']}  Draws: {scores['Draws']}")
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! \n")
            break

        # Reset for next round
        board = create_board()
        current_player = "X"


if __name__ == "__main__":
    play_game()