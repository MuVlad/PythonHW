# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


def create_list_multipliers(n):
    list_multipliers = []
    d = 2
    while d <= n:

        if n % d == 0:
            list_multipliers.append(d)
            n = n / d
        else:
            d +=1
    return list_multipliers

number = int(input('Введите число '))
print(create_list_multipliers(number))