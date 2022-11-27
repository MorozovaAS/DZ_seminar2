# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("Введите число N: "))
product = 1
for i in range(1, number + 1):
   product = product * i
   print (product, end=' ')