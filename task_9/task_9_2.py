""" Создать lambda функцию, которая принимает на вход
неопределенное количество именных аргументов и выводит
словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5} """

double = lambda **kwargs: {k * 2: v for k, v in kwargs.items()}
print(double(hello=5, goodbye=7, howareyou=9))
