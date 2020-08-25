from func import Func


class FuncLogic:
    def __init__(self, math_list):
        self.math_list = math_list

    def doit(self):
        result = self.math_list[0]  # на случай если пришло только одно значение
        count = 1  # счетчик для принта разложение операций по очереди

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

    def preority(self):
        if '*' in self.math_list or '/' in self.math_list:
            for i in range(len(self.math_list)):
                if self.math_list[i] == '*':
                    index = i
                    return index
                elif self.math_list[i] == '/':
                    index = i
                    return index
        else:
            return 1
