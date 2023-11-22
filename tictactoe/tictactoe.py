def print_game_board(board):
    print("---------")
    for row in range(3):
        print("|", " ".join(board[row * 3:(row + 1) * 3]), "|")
    print("---------")
def get_user_move(board, player):
    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            if 1 <= x <= 3 and 1 <= y <= 3:
                index = (x - 1) * 3 + y - 1
                if board[index] == "_":
                    board[index] = player
                    return
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")
def check_winner(board, player):
    for i in range(3):
        if all(board[i * 3 + j] == player for j in range(3)):
            return True
        if all(board[j * 3 + i] == player for j in range(3)):
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False
def check_game_status(board):
    if check_winner(board, "X"):
        return "X wins"
    elif check_winner(board, "O"):
        return "O wins"
    elif "_" not in board:
        return "Draw"
    return "Game not finished"
board = ["_" for _ in range(9)]
current_player = "X"
while True:
    print_game_board(board)
    get_user_move(board, current_player)
    status = check_game_status(board)
    if status != "Game not finished":
        print_game_board(board)
        print(status)
        break
    current_player = "O" if current_player == "X" else "X"
