# Дан список целых чисел.
# Создать новый список, каждый элемент которого
# равен исходному элементу умноженному на -2
number_integer = [5, 6, 10, 12, 15]
new_list_number = []
for i in number_integer:
    new_number = i * -2
    new_list_number.append(new_number)

print(number_integer)
print(new_list_number)
