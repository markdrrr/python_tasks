"""В заданной строке расположить в обратном порядке все слова.
Разделителями слов считаются пробелы."""
user_str = 'aaaa ssss vvvv bbbb'
list_str = user_str.split(' ')
size = len(list_str)
new_list_str = []
for i in range(size):
    new_list_str.append(list_str[size - 1 - i])
print(*list_str)
print(' '.join(new_list_str))
