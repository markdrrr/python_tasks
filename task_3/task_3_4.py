# Выводим на экран букву, которая находится в середине этой строки.
# Если эта центральная буква равна первой букве в строке, то создать
# и вывести часть строки между первым и последним символами исходной строки
str_line = input('Введите строку: ')
middle_str = int(len(str_line) / 2)
center_letter = str_line[middle_str]
print(center_letter)
if center_letter == str_line[0]:
    print(str_line[::])
