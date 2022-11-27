# Реализуйте алгоритм перемешивания списка.

import random
 
list = input('Введите список: ').split()
random.shuffle(list)
print(list)