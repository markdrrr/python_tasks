from func import Func
from exceptions import *

count = 1


class FuncLogic:
    count = 1  # счетчик для принта разложение операций по очереди

    def __init__(self, math_list):
        self.math_list = math_list
        self.count = 1

    def doit(self):
        global count
        result = self.math_list[0]  # на случай если пришло только одно значение

        # проверяем на дробные и целые числа и перезаписываем в список
        for i in range(len(self.math_list)):
            if type(self.math_list[i]) != int:
                if '.' in self.math_list[i]:
                    self.math_list[i] = float(self.math_list[i])
                elif self.math_list[i].isdigit():
                    self.math_list[i] = int(self.math_list[i])

        # проходим по списку и решаем в последовательности по приоретету
        while len(self.math_list) > 1:
            i = self.preority()  # проверяем приоретет для умножения и деления
            levoe_chislo = self.math_list[i - 1]
            pravoe_chislo = self.math_list[i + 1]
            oprt = self.math_list[i]
            result = self.process(oprt, levoe_chislo, pravoe_chislo)
            print(f'{count})', levoe_chislo, oprt, pravoe_chislo, f'= {result}')
            count += 1

            self.math_list[i - 1] = result  # перезаписываем результат вычисления в левое число
            self.math_list.pop(i + 1)  # удаляем число с права
            self.math_list.pop(i)  # удаляем операнд

            if not result:  # проверка что бы не возвращать значение None
                return result
            elif result == 0:
                return 0
        return result

    def process(self, oprt, arg1, arg2):
        f = Func()
        if oprt == '+':
            return f.add(arg1, arg2)
        elif oprt == '-':
            return f.subtract(arg1, arg2)
        elif oprt == '*':
            return f.mult(arg1, arg2)
        elif oprt == '/':
            return f.divide(arg1, arg2)
        elif oprt == '**':
            return f.power(arg1, arg2)

    def preority(self):
        if '**' in self.math_list:
            for i in range(len(self.math_list)):
                if self.math_list[i] == '**':
                    index = i
                    return index
        elif '*' in self.math_list or '/' in self.math_list:
            for i in range(len(self.math_list)):
                if self.math_list[i] == '*':
                    index = i
                    return index
                elif self.math_list[i] == '/':
                    index = i
                    return index
        else:
            return 1

    # проверяем что бы скобки были парные
    @staticmethod
    def paired_brackets(lst):
        sum1 = sum2 = 0
        for el in lst:
            if el == '(':
                sum1 += 1
            elif el == ')':
                sum2 += 1
        return True if sum1 == sum2 else False

    @staticmethod
    def ping_pong(lst):
        # проверяем парные ли скобки, верно ли они расположены
        # и возвращаем индекс и конец скобок в списке
        start, finish = FuncLogic.start_finish_skobki(lst)
        new_lst = lst[start + 1:finish]  # значение из скобок
        new_oprt = FuncLogic(new_lst)
        result = new_oprt.doit()  # производим операцию со значением взятых из скобок
        lst[start] = result  # перезаписываем результат вычисления из скобок в индекс
        sum_remove_numbers = finish - start
        new_dlina_lst = len(lst) - sum_remove_numbers
        while len(lst) > new_dlina_lst:  # удаляем индексы значений над которыми произвели операцию
            lst.pop(start + 1)

    @staticmethod
    def start_finish_skobki(lst):
        if FuncLogic.paired_brackets(lst):  # проверяем что бы скобки были парные
            # ищем начало и конец скобок
            for i in range(len(lst)):
                if lst[i] == ')':
                    finish = i
                    for z in range(finish + 1):
                        if lst[finish - z] == '(':
                            start = finish - z
                            return start, finish
                        elif finish - z == 0:
                            raise IncorrectParentheses
        else:
            raise NotPairedBrackets
