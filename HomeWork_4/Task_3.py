# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randint

k = int(input('Введите натуральную степень k '))

def write_file(st):
    with open('Task_3.txt', 'w') as data:
        data.write(st)

def create_list_koef(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))
    return list

def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

koef = create_list_koef(k)
write_file(create_str(koef))