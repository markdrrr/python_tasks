#  Написать программу, в которой вводятся два операнда Х и Y
#  и знак операции sign (+, –, /, *). Вычислить результат Z
#  в зависимости от знака. Предусмотреть реакции на возможный
#  неверный знак операции, а также на ввод Y=0 при делении.
#  Организовать возможность многократных вычислений без перезагрузки
#  программа (т.е. построить бесконечный цикл). В качестве символа
#  прекращения вычислений принять ‘0’ (т.е. sign='0').

while True:
    x = int(input('Введите первое значение: '))
    func = input('Введите знак операции: ')
    while func not in ['+', '-', '/', '*']:
        func = input('Введите верный знак операции: ')
    y = int(input('Введите второе значение: '))
    if func == '/' and y == 0:
        while y == 0:
            y = int(input('На 0 неделится, введите другое значение: '))
    if func == '+':
        print(f'{x} {func} {y} =', x + y)
    elif func == '-':
        print(f'{x} {func} {y} =', x - y)
    elif func == '/':
        print(f'{x} {func} {y} =', x / y)
    elif func == '*':
        print(f'{x} {func} {y} =', x * y)
    if func == 0:
        break
