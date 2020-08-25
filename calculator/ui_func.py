from func_logic import *
from exceptions import UnknownSymbol
import re


class UiFunc:
    @staticmethod
    def user_in_out(str_input):
            # str_input = input()

            # проверка на неизвестные символы
            error_symbol = re.findall(r'[^-+/*\d+?:\.\d+\s]', str_input)
            try:
                if error_symbol:
                    raise UnknownSymbol
            except UnknownSymbol as err:
                print(err)

            # собираем числа и операнды в список
            math_list = re.findall(r'[-+/*()]|\d+(?:\.\d+)?', str_input)

            # сокращаем операнды если список @math_list больше двух
            if len(math_list) > 2:
                while UiFunc.remove_optc(math_list)[0]:
                    pass

            # сокращаем отрецательное и положительное число в начале
            if math_list[0] == '-' or math_list[0] == '+':
                math_list[0] += math_list[1]
                math_list[0] = int(math_list[0])
                math_list.pop(1)
            elif math_list[-1] in ['-', '+', '/', '*']:  # если последний символ операнд, убераем его
                math_list.pop(-1)

            #  если в строке два числа вернем эти число
            if len(math_list) > 2:
                oprt = FuncLogic(math_list)
                result = oprt.doit()
                if result:
                    print('Результат', result)
                elif result == 0:
                    print('Результат', result)
            else:
                print(*math_list)

    # проверяем если есть последовательность операндов, сокращаем  их
    @staticmethod
    def remove_optc(lst):
        finish = len(lst)
        for i in range(len(lst) - 1):
            if i == finish - 2:
                return False, lst
            if lst[i] in ['+', '-'] and lst[i + 1] in ['+', '-']:
                if lst[i] == '+' and lst[i + 1] == '+':
                    lst[i] = '+'
                    lst.pop(i + 1)
                elif lst[i] == '-' and lst[i + 1] == '-':
                    lst[i] = '+'
                    lst.pop(i + 1)
                elif lst[i] == '-' and lst[i + 1] == '+':
                    lst[i] = '-'
                    lst.pop(i + 1)
                elif lst[i] == '+' and lst[i + 1] == '-':
                    lst[i] = '-'
                    lst.pop(i + 1)
                return True, None
