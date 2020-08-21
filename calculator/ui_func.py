from task_13_02.func import Func
from task_13_02.exceptions import *


class Calculate:
    @staticmethod
    def run():
        while True:
            try:
                first = int(input('Введите число: '))
                oprt = False
                while not oprt:
                    fnc = input('Введите знак операции: ')
                    try:
                        if fnc not in ['+', '-', '*', '/']:
                            raise OperationError('Неизвестный оператор !')
                        else:
                            oprt = True
                    except OperationError as error:
                        print(error)
                second = int(input('Введите второе число: '))
            except ValueError:
                print('Введите целое цисло !')
            else:
                result = Func(first, second, fnc).process()
                if result:
                    print('Результат: ', result)
