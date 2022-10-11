# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def red_file():
    with open("input_file.txt", 'r') as source:
        text_file = source.read()
    return text_file


def writing_file(string_coding):
    with open("output_file.txt", 'w') as file:
        file.write(string_coding)


def coding(txt):
    count = 1
    result = ""
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or txt[len(txt) - 2] != txt[-1]:
        result = result + str(count) + txt[-1]
    return result


def decoding(some_code):
    number = ''
    result = ''
    for i in range(len(some_code)):
        if not some_code[i].isalpha():
            number += some_code[i]
        else:
            result = result + some_code[i] * int(number)
            number = ''
    return result


print(red_file())
encoded = coding(red_file())
print(encoded)
writing_file(encoded)
print(decoding(encoded))
