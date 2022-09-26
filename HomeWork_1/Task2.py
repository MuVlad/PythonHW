# задача 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите значение переменой X "))
y = int(input("Введите значение переменой Y "))
z = int(input("Введите значение переменой Z "))

first_predicate = not(x or y or z)
second_predicate = not x and (not y) and (not z)
result = first_predicate == second_predicate

print(result)
