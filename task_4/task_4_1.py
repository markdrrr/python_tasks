# Дан список целых чисел.
# Создать новый список, каждый элемент которого
# равен исходному элементу умноженному на -2
number_integer = [5, 6, 10, 12, 15]
print(number_integer)
new_list_number = []
for i in number_integer: # решение №1
    new_number = i * -2
    new_list_number.append(new_number)
print(new_list_number)

number_integer2 = [7, 3, 1, 2, 5]
print(number_integer2)
new_list_number2 = []
i = 0  # счетчик для цикла
while i < len(number_integer2):  # решение №2
    new_number = number_integer2[i] * -2
    new_list_number2.append(new_number)
    i += 1
print(new_list_number2)

