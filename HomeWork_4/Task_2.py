# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def sort_list(some_list):
    sort_list = []
    for i in some_list:
        if i not in sort_list:
            sort_list.append(i)
    return sort_list



array = [ 3, 8, 23, 4, 3, -13, 0, -43, -13]
print(array)
print(sort_list(array))

