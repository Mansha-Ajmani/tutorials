board = [" "] * 9

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("-" * 5)
    print(board[3], "|", board[4], "|", board[5])
    print("-" * 5)
    print(board[6], "|", board[7], "|", board[8])

def check_win(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(board[a]==p and board[b]==p and board[c]==p for a,b,c in wins)

player = "X"

for _ in range(9):
    print_board()
    pos = int(input(f"Player {player}, enter position (0-8): "))
    if board[pos] == " ":
        board[pos] = player
        if check_win(player):
            print_board()
            print(player, "wins")
            break
        player = "O" if player == "X" else "X"
else:
    print_board()
    print("Draw")
