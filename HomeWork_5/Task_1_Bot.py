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
    print("Условие задачи: На столе лежит 2021 конфета. Вы играете против Бота, делая ход друг после друга.\n"
          "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n"
          "Все конфеты оппонента достаются сделавшему последний ход. Удачи!")
    print(" ")


def processing_user_input(name):
    counter = int(input(f"Ходит {name}, введите колличество конфет, которое хотите взять (от 1 до 28 штук): "))
    while counter < 1 or counter > 28:
        counter = int(input("Количество конфет должно быть в диапазоне (от 1 до 28), попробуйте еще раз: "))
    return counter


def result_game(winner):
    if winner:
        return player
    else:
        return Bot_Vasya


number_candies = 2021
greetings()

player = input('Введите имя игрока: ')
Bot_Vasya = "Бот Вася"
walker = randint(0, 2)
player_counter = 0
Bot_Vasya_counter = 0
print(" ")
print(f"На столе {number_candies} конфет(а)")

while number_candies > 28:
    if walker:
        temp = processing_user_input(player)
        player_counter += temp
        number_candies -= temp
        print(f"{player} взял {temp} конфет(ы), теперь у него их {player_counter}")
        print(f"На столе {number_candies} конфет(а)")
        print(" ")
        walker = False
    else:
        temp = randint(1,29)
        Bot_Vasya_counter += temp
        number_candies -= temp
        print(f"{Bot_Vasya} взял {temp} конфет(ы), теперь у него их {Bot_Vasya_counter}")
        print(f"На столе {number_candies} конфет(а)")
        print(" ")
        walker = True

print(f"{result_game(walker)}, поздравляем вас, последний ход за вами, вы выиграли!")