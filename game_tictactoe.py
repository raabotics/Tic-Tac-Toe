# TIC TAC TOE GAME that is displayed in console
#
# Creates the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# initiates the loop by default
game_still_going = True

# Winner by default
winner = None

# Who's turn is it?
current_player = "X"

valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# displays the board

def display_board():

    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Executes the game
def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)
        flip_player()
        check_if_game_over()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("It's a tie!")


def handle_turn(player):
    # Let the current player choose where to place the symbol X or O
    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in valid_input:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("This position is already taken.\nTry again.")

    board[position] = player
    display_board()


# changes players
def flip_player():

    global current_player
    # change player from x to o
    if current_player == "X":
         current_player = "O"

    # change player from o to x
    elif current_player == "O":
        current_player = "X"
    return


def check_if_game_over():

    check_for_winner()
    check_for_tie()


def check_for_winner():

    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

# Set up global variables
    global game_still_going
# check for same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Check which row won and who is the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
        # Check which column won and who is the winner
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return


def check_diagonals():

    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Check which diagonal won and who is the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_for_tie():
    # Set up global variable
    global game_still_going
    # if no one has won yet, check if there are empty spots in list
    if "-" not in board:
        game_still_going = False
    return

play_game()