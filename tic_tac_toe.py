Blank = " "

def main():
    # Set player to be X's turn
    player = current_player("")

    # Make board
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9\n")
    
    board = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

    while not game_done(board, message=True):    
        play_game(player, board)
        display_board(board)
        player = current_player(player)

def display_board(board):
    
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

    return board

def current_player(player):
    if player == "" or player == "o":
        return "x"
    else:
        return "o"

# def next_player():
#     pass

def game_done(board, message=False):
    # Game is finished if all the squares are filled
    tie = True
    for square in range(9):
        if board[square] != "x" or board[square] != "o":
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    # Game is finished if someone has completed a row
    for row in range(3):
        if board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True
    # Game is finished if someone has completed a column
    for col in range(3):
        if board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True
    # Game is finished if someone has a diagonal
    if (board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True
    return False

def play_game(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    
    # Accept input from the user.
    if board[square-1] == "x" or board[square-1] == "o":
        print("That square is taken. Try again.")
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player 
        return True
    else:
        board[square - 1] = player 

if __name__ == "__main__":
    main()
