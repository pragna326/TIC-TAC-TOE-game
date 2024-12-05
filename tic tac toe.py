def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Check if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player, board):
    """Get the player's move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if move < 0 or move >= 9 or board[row][col] != " ":
                print("Invalid move! Try again.")
            else:
                return row, col
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row, col = get_move(players[current_player], board)
        board[row][col] = players[current_player]

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
