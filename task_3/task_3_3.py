# Если длина строки больше 10 символов, то создаем новую строку с 3 восклицательными знаками в конце  ('!!!')
# и вывести на экран. Если меньше 10, то вывести на экран второй символ строки
str_line = input('Введите строку: ')
if len(str_line) > 10:
    print(f'{str_line} !!!')
else:
    print(str_line[1])