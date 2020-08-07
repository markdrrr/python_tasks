# Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 1 2 3 4 5 ->  2 3 4 5 1
# решение №1
numbers = input('Введите числа через пробел ')
list_numbers = numbers.split(' ')  # список чисел
old_list = list_numbers.copy()  # копируем первый список
element = list_numbers.pop(0)  # запоминаем удаленный элемент
list_numbers.append(element)  # добавляем удаленный элемент в конец списка
print(*old_list, '->', *list_numbers)

# решение №2
numbers2 = input('Введите числа через пробел ')
list_numbers2 = numbers2.split(' ')
old_list2 = list_numbers2.copy()
new_list2 = []  # создаем пустой список, который будем заполнять
element2 = list_numbers2.pop(0)
for i in range(len(list_numbers2)):
    new_list2.append(list_numbers2[i])
else:
    new_list2.append(element2)
print(*old_list2, '->', *new_list2)

# решение №3
numbers3 = input('Введите числа через пробел ')
list_numbers3 = numbers3.split(' ')
old_list3 = list_numbers3.copy()
new_list3 = []
element3 = list_numbers3.pop(0)
i = 0  # счетчик для цикла
while i < len(list_numbers3):
    new_list3.append(list_numbers3[i])
    i += 1
else:
    new_list3.append(element3)
print(*old_list3, '->', *new_list3)
