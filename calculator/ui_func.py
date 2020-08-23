from calculator.func_logic import *
from calculator.exceptions import *
import re


class UiFunc:
    @staticmethod
    def user_in_out():
        in_input = False
        while not in_input:
            str_input = input()

            # проверка на неизвестные символы
            error_symbol = re.findall(r'[^-+/*\d+?:\.\d+\s]', str_input)
            try:
                if error_symbol:
                    raise UnknownSymbol
            except UnknownSymbol as err:
                print(err)
                continue
            math_list = re.findall(r'[-+/*()]|\d+(?:\.\d+)?', str_input)

            # проверка на отрецательное и положительное число в начале
            if math_list[0] == '-' or math_list[0] == '+':
                math_list[0] += math_list[1]
                math_list[0] = int(math_list[0])
                math_list.pop(1)

            oprt = FuncLogic(math_list)
            result = oprt.doit()
            if result:
                print('Результат', result)
            elif result == 0:
                print('Результат', result)
