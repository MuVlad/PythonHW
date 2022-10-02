# Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


def create_list():
    list_size = int(input("Задайте размер списка: "))
    some_list = []
    for _ in range(list_size):
        some_list.append(randint(1, 10))
    return some_list

def sum_position(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum

some_list = create_list()
print(some_list)
print(sum_position(some_list))