class UnknownSymbol(Exception):
    def __init__(self, message='Неверный ввод'):
        super().__init__(message)


class NotPairedBrackets(Exception):
    def __init__(self, message='Непарные скобки'):
        super().__init__(message)


class IncorrectParentheses(Exception):
    def __init__(self, message='Неправильное расположение скобок'):
        super().__init__(message)
