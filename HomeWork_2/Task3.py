# Задача 3. Реализуйте алгоритм перемешивания списка. 
# Список размерностью 10 задается случайными целыми числами, выводится на экран, 
# затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!

from random import Random, randint


random_list = []
for i in range(10):
    random_list.append(randint(-10,10))
print(random_list)


for i in range(len(random_list) -1):
   swap = randint(0,len(random_list) -1)
   temp =random_list[swap]
   random_list[swap] = random_list[i]
   random_list[i] = temp

print(random_list)