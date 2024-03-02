#МОРСКОЙ БОЙ
from random import randint

accept_board = False
input_board = input("Let's set up the board.\nEnter a number from 5 to 25 (this will be the width and height of the board):")
print(input_board)
while accept_board is False:
    if int(input_board) >= 5 and int(input_board) <= 25:
        accept_board = True
    else:
        if int(input_board) < 5 or int(input_board) > 25:
                print("Be more careful!")
                input_board = input("You must enter a number FROM 5 TO 25:")
        
board = []

for i in range(int(input_board)):
    board.append(["O"] * int(input_board))


def print_board(board):
    for row in board:
        #string = ' '.join(row)
        #new_board = string.replace("'", "").replace(",", "")
        print (' '.join(row))

def random_row(board_in):
    return randint(0, len(board_in) - 1)
def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)
#print(ship_row)
#print(ship_col)
print("You have " + str(input_board) + " attempts!")

for turn in range(int(input_board) + 1):
    print("Attempts " + str(turn) + "/" + str(input_board) + "! Good luck!)")
    guess_row = int(input("Guess the row: "))
    guess_col = int(input("Guess the col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my ship!)")
        break
    else:
        if guess_row not in range(int(input_board)) or guess_col not in range(int(input_board)):
            print("Oops, that's not even in the ocean!")
        elif board [guess_row] [guess_col] == "X":
            print("You've already shot at this place! It was a waste of a shell...")
        else:
            if turn < int(input_board) / 3:
                print("I'm sorry, but you missed")
            elif turn < int(input_board) / 2:
                print("Missed!")
            elif turn < int(input_board):
                print("Aim better!")
            else:
                print("It was the last shot! Game over!")
            if turn < int(input_board):
                print("Attempts", turn + 1)
            board [guess_row] [guess_col] = "X"
            if turn < int(input_board):
                print_board(board)
        if turn == int(input_board):
            board[ship_row][ship_col] = "V"
            print_board(board)
