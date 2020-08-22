from calculator.func_logic import *
import re


class UiFunc:
    @staticmethod
    def user_in_out():
        in_input = False
        while not in_input:
            str_input = input()
            digit_list = re.split(r"[+\-*/]", str_input)
            try:
                digit_list = list(map(lambda x: int(x), digit_list))
            except ValueError:
                print('Неверная операция')
                continue
            else:
                in_input = True
            if len(digit_list) < 2:  # если введино только одно число
                print(digit_list[0])
                continue
            oprt_list = re.findall(r'[+\-*/]', str_input)
            oprt = FuncLogic(digit_list, oprt_list)
            result = oprt.doit()
            if result:
                print('Результат', result)
