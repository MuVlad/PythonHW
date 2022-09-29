# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число: '))
whole_part = int(number)
fractional_part = number - int(number)

sum = 0
while whole_part > 0:
    sum += whole_part % 10
    whole_part = whole_part // 10
while fractional_part > 0:
    sum += int(fractional_part * 10)
    fractional_part = round(fractional_part * 10 - int(fractional_part * 10),5)

print(sum)
