#   Дано число. Найти сумму и произведение его цифр.
number = int(input('>>> '))

sum = 0
product = 1

while number > 0:
    num = number % 10  # остаток от деления для получения числа
    sum = sum + num
    product = product * num
    number = number // 10  # деление нацело без остатка, что бы перейти к следующией цифре

print(f'Cумма: {sum}, произведение: {product}')
