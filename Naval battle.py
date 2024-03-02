#МОРСКОЙ БОЙ
from random import randint

accept_board = False
input_board = input('Давай настроим поле.\nВведи число от 5 до 25 (это будет ширина и высота поля):')
print(input_board)
while accept_board is False:
    if int(input_board) >= 5 and int(input_board) <= 25:
        accept_board = True
    else:
        if int(input_board) < 5 or int(input_board) > 25:
                print("Будь внимательнее!")
                input_board = input("Неоходимо ввести число ОТ 5 ДО 25:")
        
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
print("У тебя " + str(input_board) + " попыток!")

for turn in range(int(input_board) + 1):
    print("Попытка " + str(turn) + "/" + str(input_board) + "! Удачи!)")
    guess_row = int(input("Угадай строку: "))
    guess_col = int(input("Угадай столбик: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Поздравляю! Ты потопил мой корабль!)")
        break
    else:
        if guess_row not in range(int(input_board)) or guess_col not in range(int(input_board)):
            print("Ты ударил мимо нашего моря!")
        elif board [guess_row] [guess_col] == "X":
            print("В это место ты уже стрелял! Зря только снаряд потратил...")
        else:
            if turn < int(input_board) / 3:
                print("Извини, но ты промазал")
            elif turn < int(input_board) / 2:
                print("Мимо!")
            elif turn < int(input_board):
                print("Целься лучше!")
            else:
                print("Мазила! Игра окончена!")
            if turn < int(input_board):
                print("Попытка", turn + 1)
            board [guess_row] [guess_col] = "X"
            if turn < int(input_board):
                print_board(board)
        if turn == int(input_board):
            board[ship_row][ship_col] = "V"
            print_board(board)
