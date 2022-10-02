# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import random


def create_list():
    list_size = int(input('Введите размер списка '))
    some_list = []
    for _ in range(list_size):
        some_list.append(round((random() * 10),2))
    return some_list

def find_max_element(list):
    max = list[0] - int(list[0])
    element = 0
    for i in range(len(list)):
        element = list[i] - int(list[i])
        if element > max:
            max = element
    return max

def find_min_element(list):
    min = list[0] - int(list[0])
    element = 0
    for i in range(len(list)):
        element = list[i] - int(list[i])
        if element < min:
            min = element
    return min


def difference_between_min_max(list):
    return round(find_max_element(list) - find_min_element(list),2)

list = create_list()
print(list)
print(difference_between_min_max(list))
