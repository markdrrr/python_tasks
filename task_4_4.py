#  Дан список. Создать новый список, сдвинутый на 1 элемент влево Пример: 1 2 3 4 5 ->  2 3 4 5 1
numbers = input('Введите числа через пробел ')
list_numbers = numbers.split(' ')
old_list = list_numbers.copy()
element = list_numbers.pop(0)  # запоминаем удаленный элемент
list_numbers.append(element)  # добавляем удаленный элемент в конец списка
print(*old_list, '->', *list_numbers)
