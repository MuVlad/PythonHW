# задача 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# - 

try:
    day_of_week = int(input("Введите день недели:" ))
    if 6 <= day_of_week <= 7:
        print(f"{day_of_week} -> да")
    elif 0 < day_of_week < 6:
        print(f"{day_of_week} -> нет")
    else:
        print("Это не день недели")
except:
    print("Необходимо ввести число!")