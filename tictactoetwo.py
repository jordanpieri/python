import random
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    horizontal_boarder = "+---+---+---+"
    spacer_row = "|   |   |   |"
    row_123 = "| "+ str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " |"
    row_456 = "| "+ str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " |"
    row_789 = "| "+ str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " |"
    print(horizontal_boarder,row_123,horizontal_boarder,row_456,horizontal_boarder,row_789,horizontal_boarder, "\n", sep="\n")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    available = []
    print("Make a selection from the available options:")
    for i in make_list_of_free_fields(board):
        available.append(board[i[0]][i[1]])
    print(available)
    inp = int(input())
    if inp in available:
        print("update the moves list with", inp)
        for i in make_list_of_free_fields(board):
            if board[i[0]][i[1]] == inp:
                moves[i[0]][i[1]] = "O"
                #return(board[i[0]][i[1]])
                display_board(moves)
                victory_for(moves, "O")
    else:
        print("Invalid selection,",inp,"please try again")
        enter_move(moves)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    listoftups = []
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) is int:
                listoftups.append((row,col))
    return(listoftups)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == board[0][1] == board[0][2] == sign:
        print(sign + " is the winner!")
        exit()
    if board[1][0] == board[1][1] == board[1][2] == sign:
        print(sign + " is the winner!")
        exit()
    if board[2][0] == board[2][1] == board[2][2] == sign:
        print(sign + " is the winner!")
        exit()
    # vertical wins
    if board[0][0] == board[1][0] == board[2][0] == sign:
        print(sign + " is the winner!")
        exit()
    if board[0][1] == board[1][1] == board[2][1] == sign:
        print(sign + " is the winner!")
        exit()
    if board[0][2] == board[1][2] == board[2][2] == sign:
        print(sign + " is the winner!")
        exit()
    # diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == sign:
        print(sign + " is the winner!")
        exit()
    if board[0][2] == board[1][1] == board[2][0] == sign:
        print(sign + " is the winner!")
        exit()
    if make_list_of_free_fields is None:
        print("Draw!")
        exit()

def draw_move(board):
    # The function draws the computer's move and updates the board.
    available = []
    for i in make_list_of_free_fields(board):
        available.append(board[i[0]][i[1]])
    x = random.choice(available)
    if x in available:
        print("update the moves list with", x)
        for i in make_list_of_free_fields(board):
            if board[i[0]][i[1]] == x:
                moves[i[0]][i[1]] = "X"
                display_board(moves)
                victory_for(moves, "X")

moves=[
    [1,2,3],
    [4,'X',6],
    [7,8,9]
]
#make_list_of_free_fields(moves)
display_board(moves)
enter_move(moves)
draw_move(moves)
enter_move(moves)
draw_move(moves)
enter_move(moves)
draw_move(moves)
enter_move(moves)
draw_move(moves)
enter_move(moves)
draw_move(moves)