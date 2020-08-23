class UnknownSymbol(Exception):
    def __init__(self, message='Неверный ввод'):
        super().__init__(message)
