# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

def create_list():
    list_size = int(input('Введите размер списка '))
    some_list = []
    for _ in range(list_size):
        some_list.append(randint(1,10))
    return some_list

def multiplication_pair(list):
    result_list = []
    if len(list) % 2 == 0:
        for i in range(int(len(list)/2)):
            result_list.append(list[i] * list[len(list) - i -1])
    else:
        for i in range(int(len(list)/2) + 1):
            result_list.append(list[i] * list[len(list) - i -1])
    return result_list

some_list = create_list()
print(some_list)
print(multiplication_pair(some_list))