import random
# create the tictactoe board

def board(spots):
    horizontal_boarder = "+---+---+---+"
    spacer_row = "|   |   |   |"
    row_123 = "| "+ spots[1] + " | " + spots[2] + " | " + spots[3] + " |"
    row_456 = "| "+ spots[4] + " | " + spots[5] + " | " + spots[6] + " |"
    row_789 = "| "+ spots[7] + " | " + spots[8] + " | " + spots[9] + " |"
    print(horizontal_boarder,row_123,horizontal_boarder,row_456,horizontal_boarder,row_789,horizontal_boarder, "\n", sep="\n")
    # horizontal wins
    if spots[1] == spots[2] == spots[3] != " ":
        print(spots[1] + " is the winner!")
        exit()
    if spots[4] == spots[5] == spots[6] != " ":
        print(spots[4] + " is the winner!")
        exit()
    if spots[7] == spots[8] == spots[9] != " ":
        print(spots[7] + " is the winner!")
        exit()
    # vertical wins
    if spots[1] == spots[4] == spots[7] != " ":
        print(spots[1] + " is the winner!")
        exit()
    if spots[2] == spots[5] == spots[8] != " ":
        print(spots[2] + " is the winner!")
        exit()
    if spots[3] == spots[6] == spots[9] != " ":
        print(spots[3] + " is the winner!")
        exit()
    # diagonal wins
    if spots[1] == spots[5] == spots[9] != " ":
        print(spots[1] + " is the winner!")
        exit()
    if spots[7] == spots[5] == spots[3] != " ":
        print(spots[7] + " is the winner!")
        exit()
    #print(horizontal_boarder,spacer_row,row_123,spacer_row,horizontal_boarder,spacer_row,row_456,spacer_row,horizontal_boarder,spacer_row,row_789,spacer_row,horizontal_boarder, sep="\n")


def Player_move(moved):
    open = get_available(moved)
    selection = ", ".join(open)
    # inp = int(input("Please input a number (" + selection + ") for your move: "))
    # if str(inp) not in open:
    #     print("Selection is invalid!")
    #     Player_move(moves)
    # if str(inp) in open:
    #     O = inp
    #     moves[O] = "O"
    while True:
        O = int(input("Please input a number (" + selection + ") for your move: "))
        if str(O) in open:
            moves[O] = "O"
            break
        print("Selection is invalid!")
    board(moves)

def CPU_move(moved):
    #print(moved)
    open = get_available(moved)
    move = random.choice(open)
    print("CPU Move: " + move)
    moves[int(move)] = "X"
    board(moves)

def get_available(available):
    open = []
    if " " in available.values():
        for i in available:
            if available[i] == " ":
                open.append(str(i))
    else:
        print("All available spots taken. Game over.")
        exit()
    return open

moves = {1: " ", 2: " ", 3: " ", 4: " ", 5: "X", 6: " ", 7: " ", 8: " ", 9: " "}
board(moves)
#print(get_available(moves))
while get_available(moves) is not None:
    Player_move(moves)
    CPU_move(moves)



# def Player_move(available):
#     #print(available)
#     #nones = not all(available.values())
#     #print(nones)
#     open = []
#     #if None in available[]:
#     if " " in available.values():
#         #for k, v in available:
#     #         if available[v] == " ":
#     #         print("available[v] is " + str(k))
#     #         open += str(k)
#     # else:
#     # print(available[v] + "was not None")
#         for i in available:
#             if available[i] == " ":
#                 #print("available[v] is " + str(i+1))
#                 open.append(str(i))
#             else:
#                 #print(str(i) + " was " + available[i] + " not None")
#                 None
#     else:
#         print("None was not in available.values()")
#     open = ", ".join(open)
#     O = int(input("Please input a number (" + open + ") for your move: "))
#     moves[O] = "O"
#     board(moves)