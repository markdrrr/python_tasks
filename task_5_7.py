""" Дана целочисленная квадратная матрица. Найти в каждой строке
наи- больший элемент и поменять его местами с элементом главной диагонали."""
import random

n = 5  # размер матрицы
m = [[random.randint(1, 10) for i in range(n)] for i in range(n)]
for row in m:
    print(row)
max = 0
diagonal = 0
index_max_number = 0
for row in range(len(m)):
    max = 0
    stolb = 0
    for el in range(len(m[row])):
        if m[row][el] > max:
            max = m[row][el]
            index_max_number = el  # запоминаем индекс максимального значения из строки
    m[row][index_max_number] = m[row][diagonal]  # минаем максимальное значение из строки на число из диагонали
    diagonal += 1  # счетчик для диагонали

print()
print()
for row in m:
    print(row)
