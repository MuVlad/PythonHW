# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".


input_text=input("Введите текст через пробел: ")
text_remove = "абв"
result = [i for i in input_text.split() if text_remove not in i]
print(" ".join(result))
