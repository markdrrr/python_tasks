#  Дан список целых чисел. Подсчитать сколько четных чисел в списке
numbers = input('Введите список целых чисел через пробел ')
list_numbers = numbers.split(' ')
counter = 0
for el in list_numbers:
    if int(el) % 2 == 0:
        counter += 1
print(*list_numbers)  # распаковка списка
print('Четных чисел в списке ', counter)
