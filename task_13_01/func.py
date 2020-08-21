class Func:
    def __init__(self, arg1, arg2, operator):
        self.arg1 = arg1
        self.arg2 = arg2
        self.operator = operator

    def process(self):
        if self.operator == '+':
            return self.add()
        elif self.operator == '-':
            return self.subtract()
        elif self.operator == '*':
            return self.mult()
        elif self.operator == '/':
            return self.divide()

    def add(self):
        return self.arg1 + self.arg2

    def subtract(self):
        return self.arg1 - self.arg2

    def mult(self):
        return self.arg1 * self.arg2

    def divide(self):
        return self.arg1 / self.arg2
