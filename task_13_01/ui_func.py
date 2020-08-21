from task_13_01.func import Func


class Calculate:
    @staticmethod
    def run():
        while True:
            first = int(input('Введите число: '))
            fnc = input('Введите знак операции: ')
            second = int(input('Введите второе число: '))
            result = Func(first, second, fnc).process()
            print(result)
