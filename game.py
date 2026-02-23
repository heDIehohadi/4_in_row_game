ROWS = 6
COLS = 7
board = []
def create_board():
    
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(" ")
        board.append(row)
    return board


def print_board(board):

    for i in range(COLS):
        print( i + 1, end="    ")
    print()
    
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print()
    print()


def drop_piece(board, col, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = piece
            return True
    return False


def check_winner(board, piece):

    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    return False


def board_full(board):
    for c in range(COLS):
        if board[0][c] == " ":
            return False
    return True


def play_game():
    board = create_board()
    turn = 0

    print_board(board)

    while True:
        if turn % 2 == 0:
            piece = "X"
            player = 1
        else:
            piece = "O"
            player = 2

        col = input(f"Player {player} ({piece}) choose column (1-7): ")

        if not col.isdigit():
            print("Please enter a number")
            continue

        col = int(col) - 1

        if col < 0 or col >= COLS:
            print("Invalid column")
            continue

        if not drop_piece(board, col, piece):
            print("Column is full")
            continue

        print_board(board)

        if check_winner(board, piece):
            print(f"Player {player} wins!")
            break

        if board_full(board):
            print("Draw!")
            break

        turn += 1


play_game()

