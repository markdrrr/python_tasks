class Func:

    def add(self, arg1, arg2):
        return arg1 + arg2

    def subtract(self, arg1, arg2):
        return arg1 - arg2

    def mult(self, arg1, arg2):
        return arg1 * arg2

    def divide(self, arg1, arg2):
        try:
            result = arg1 / arg2
        except ZeroDivisionError:
            print('На ноль делить нельзя')
        else:
            return result
