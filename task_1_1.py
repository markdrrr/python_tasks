import math

# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение
a = int(input('Введите число: '))
b = int(input('Введите второе число: '))
action = input('Введите + или - или *: ')
if action == '+':
    print('Результат: ', a + b)
elif action == '-':
    print('Результат: ', a - b)
elif action == '*':
    print('Результат: ', a * b)
else:
    print('Ввели неверное значение')

# Даны действительные числа x и y. Получить....
x = int(input('Введите число: '))
y = int(input('Введите второе число: '))
result = (x - y) / 1 + x * y
print('Формула равна', result)

# Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.
a = int(input('Введите длину ребра куба: '))
v = a ** 3
s = 4 * a ** 2
print("Объем куба", v)
print("Площадь стороны", s)

# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
a, b = (int(input('Катет а: ')), int(input('Катет b: ')))
g = math.sqrt(a ** 2 + b ** 2)
s = a * b / 2
print('Гипотенуза: ', g)
print('Площадь: ', s)