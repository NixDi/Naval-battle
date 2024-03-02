#МОРСКОЙ БОЙ
from random import randint

board = []
for i in range(5):
    board.append(["O"] * 5)

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
print("У тебя 5 попыток!")

for turn in range(6):
    print("Попытка " + str(turn) + "/5! Удачи!)")
    guess_row = int(input("Угадай строку: "))
    guess_col = int(input("Угадай столбик: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Поздравляю! Ты потопил мой корабль!)")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Ты ударил мимо нашего моря!")
        elif board [guess_row] [guess_col] == "X":
            print("В это место ты уже стрелял! Зря только снаряд потратил...")
        else:
            if turn < 2:
                print("Извини, но ты промазал")
            elif turn < 4:
                print("Мимо!")
            elif turn < 5:
                print("Целься лучше!")
            else:
                print("Мазила! Игра окончена!")
            if turn < 5:
                print("Попытка", turn + 1)
            board [guess_row] [guess_col] = "X"
            if turn < 5:
                print_board(board)
        if turn == 5:
            board[ship_row][ship_col] = "V"
            print_board(board)