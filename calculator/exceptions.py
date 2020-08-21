class OperationError(Exception):
    def __init__(self, message='Ошибка'):
        super().__init__(message)
