# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

array = [-2, -1, 0, 1, 2]
firstLineNumber = int(input("Введите номер строки 1 (от 1 до 5): "))
secondLineNumber = int(input("Введите номер строки 2 (от 1 до 5): "))
with open('file.txt','r') as f:
   line = f.readlines()
   firstMultiplier = int (line[firstLineNumber-1])
   secondMultiplier = int (line[secondLineNumber-1])
product = array[firstMultiplier] * array[secondMultiplier]
print(product)