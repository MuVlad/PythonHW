# задача 4. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите число a "))
b = int(input("Введите число b "))
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)