# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;



def ret(s):
    s = str(s)
    if s.isdigit():
        return float(s)
    for c in ('-','+','*','/'):
        left, op, right = s.partition(c)
        if op == '*':
            return ret(left) * ret(right)
        elif op == '/':
            return ret(left) / ret(right)
        elif op == '+':
            return ret(left) + ret(right)
        elif op == '-':
            return ret(left) - ret(right)


print(ret(input()))