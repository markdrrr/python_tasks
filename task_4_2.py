#  Дан список целых чисел. Подсчитать сколько четных чисел в списке
numbers = input('Введите список целых чисел через пробел ')
list_numbers = numbers.split(' ')
counter = 0
for el in list_numbers:  # решение №2
    if int(el) % 2 == 0:
        counter += 1
print(*list_numbers)  # распаковка списка
print('Четных чисел в списке ', counter)

new_numbers = input('Введите список целых чисел через пробел ')
new_list_numbers = new_numbers.split(' ')
new_counter = 0
i = 0  # счетчик для цикла
while i < len(new_list_numbers):  # решение №2
    if int(new_list_numbers[i]) % 2 == 0:
        new_counter += 1
    i += 1
print(*new_list_numbers)  # распаковка списка
print('Четных чисел в списке ', new_counter)
