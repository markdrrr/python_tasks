"""Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)"""
import random

array = [random.randrange(0, 9) for i in range(random.randrange(7, 9))]
print(array)
section = 0
amount_over = 0
for i in range(len(array) - 1):
    a1 = array[i]
    a2 = array[i + 1]
    if array[i] < array[i + 1]:
        amount_over += 1
        continue
    else:
        if amount_over != 0:
            section += 1
            amount_over = 0

print('Количество участков массива, на котором элементы монотонно возрастают \n', section)
