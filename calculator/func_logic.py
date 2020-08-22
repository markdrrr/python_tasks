from calculator.func import Func


class FuncLogic:
    def __init__(self, digit_list, oprt_list):
        self.digit_list = digit_list
        self.oprt_list = oprt_list

    def doit(self):
        summa = self.digit_list[0]
        for i in range(len(self.digit_list) - 1):
            result = self.process(self.oprt_list[i], summa, self.digit_list[i + 1])
            print(f'{i + 1})', summa, self.oprt_list[i], self.digit_list[i + 1],f'= {result}')
            summa = result
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

    # def preority(self):
    #     if '*' in self.oprt_list:
    #         return self.oprt_list.index('*')
