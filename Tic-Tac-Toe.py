def print_board(board):
    """Display the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Check if the given player has won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  
            return True
        if all(board[j][i] == player for j in range(3)):  
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False



board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

print("Welcome to Tic-Tac-Toe!")
while True:
    print_board(board)
    print(f"Player {players[turn]}'s turn.")
    
    row, col = map(int, input("Enter row and column (1-3) separated by a space: ").split())
    row -= 1
    col -= 1

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = players[turn]
    else:
        print("Invalid move, try again.")
        continue

    if check_winner(board, players[turn]):
        print_board(board)
        print(f"Player {players[turn]} wins!")
        break
    elif all(board[r][c] != " " for r in range(3) for c in range(3)):
        print_board(board)
        print("It's a draw!")
        break

    turn = 1 - turn
