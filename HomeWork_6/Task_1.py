# Задача 1. Создайте программу для игры в "Крестики-нолики".
from random import randint


def print_matrix(matrix):
    for i in range(3):
        for j in range(3):
            print(f"{matrix[i][j]} ", end='')
        print(" ")

def is_cell_valid(x, y):
    if x < 0 or y < 0 or x >=3 or y >=3:
        print("Не корректные координты")
        return False
    elif matrix[y][x] != '_':
        print('Эта точка занята')
        return False
    else:
        return True

def input_data_player(sign):
    print("Введите координаты ячеки через 'Enter':")
    x = int(input()) - 1
    y = int(input()) - 1

    if is_cell_valid(x, y):
        matrix[y][x] =  sign
    else:
        input_data_player(sign)

def turn_player(player, sign):
    print("")
    print(f"Ходит игрок {player}")
    input_data_player(sign)
    print_matrix(matrix)


def check_win(dot):
    for i in range(3):
        if  ((matrix[i][0] == dot and matrix[i][1] == dot and matrix[i][2] == dot) or
                (matrix[0][i] == dot and matrix[1][i] == dot and matrix[2][i] == dot)):
            return True
        elif ((matrix[0][0] == dot and matrix[1][1] == dot and matrix[2][2] == dot) or
              (matrix[2][0] == dot and matrix[1][1] == dot and matrix[0][2] == dot)):
            return True
        return False

def is_table_full():
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '_':
                return False
    return True

def game():
    global walker
    while True:
        if walker:
            turn_player(human_1,'X')
            walker = False
            if check_win('X'):
                print(f"{human_1} Вы выйграли!")
                break
            elif is_table_full():
                print("Ничья!")
                break
        else:
            turn_player(human_2,'O')
            walker = True
            if check_win('O'):
                print(f"{human_2} Вы выйграли!")
                break
            elif is_table_full():
                print("Ничья!")
                break


matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
SIGN_X = "X"
SIGN_O = "O"
human_1 = input('Введите имя первого игрока: ')
human_2 = input('Введите имя втрого игрока: ')
print_matrix(matrix)
walker = randint(0, 2)
game()
