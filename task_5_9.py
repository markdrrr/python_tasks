""" Для каждого натурального числа в промежутке от m до n вывести
все делители, кроме единицы и самого числа. m и n вводятся с клавиатуры"""
print('Введите промежуток два числа: ')
m = int(input())
n = int(input())
for number in range(m, n + 1):
    print(f'{number}:', end='')
    for i in range(2, number):
        if number % i == 0:
            print(i, end='')
    print()
