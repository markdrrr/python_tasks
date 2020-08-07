"""  В массиве целых чисел с количеством элементов 19 определить
максимальное число и заменить им все четные по значению элементы"""
array = [i for i in range(19)]
print(array)
# находим максимальное число
for el in array:
    max = array[0]
    if el > max:
        max = el
# заменяем максимальным числом все четные значения
index = 0
for el in array:
    if el % 2 == 0:
        array[index] = max
    index += 1
print(array)
