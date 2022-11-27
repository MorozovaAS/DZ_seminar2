#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите число: '))*100
sum = 0
while number > 0:
   sum += number % 10
   number = int(number/10)
print(int(sum))

