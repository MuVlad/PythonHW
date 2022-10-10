# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def greetings():
    print("Добро пожаловать в игру конфеты!")
    print(" ")
    print("Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n"
          "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n"
          "Все конфеты оппонента достаются сделавшему последний ход. Удачи!")
    print(" ")


def lottery():
    player = randint(0, 2)
    if player:
        return  player1
    else:
        return player2


def processing_user_input(name):
    counter = int(input(f"Ходит игрок {name}, введите колличество конфет, которое хотите взять (от 1 до 28 штук): "))
    while counter < 1 or counter > 28:
        counter = int(input("Количество конфет должно быть в диапазоне (от 1 до 28), попробуйте еще раз: "))
    return counter


def result_game(winner):
    if winner:
        return player1
    else:
        return player2


number_candies = 121
greetings()

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя втрого игрока: ')
walker = lottery()
player_counter1 = 0
player_counter2 = 0
print(" ")
print(f"На столе {number_candies} конфет(а)")

while number_candies > 28:
    if walker:
        temp = processing_user_input(player1)
        player_counter1 += temp
        number_candies -= temp
        print(f"Игрок {player1} взял {temp} конфет(ы), теперь у него их {player_counter1}")
        print(f"На столе {number_candies} конфет(а)")
        print(" ")
        walker = False
    else:
        temp = processing_user_input(player2)
        player_counter2 += temp
        number_candies -= temp
        print(f"Игрок {player2} взял {temp} конфет(ы), теперь у него их {player_counter2}")
        print(f"На столе {number_candies} конфет(а)")
        print(" ")
        walker = True

print(f"Игрок {result_game(walker)}, поздравляем вас, последний ход за вами, вы выиграли!")