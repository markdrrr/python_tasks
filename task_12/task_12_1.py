""" Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения(==, < либо >),
сложения, вывод на экран. Перегрузить конструктор на обработку входных параметров
вида: одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)"""


class MyTime:

    def __init__(self, *args):
        if args:
            if type(args[0]) == str:
                str_list = args[0].split('.')
                self.__hours = int(str_list[0])
                self.__minutes = int(str_list[1])
                self.__seconds = int(str_list[2])
            else:
                hours = args[0]
                minutes = args[1]
                seconds = args[2]
                if int(hours) < 25:
                    self.__hours = hours
                else:
                    print('Не больше 24 часов')
                if minutes < 60:
                    self.__minutes = minutes
                else:
                    print('Не больше 59 минут')
                if seconds < 60:
                    self.__seconds = seconds
                else:
                    print('Не больше 59 секунд')
        else:
            self.__hours = self.__minutes = self.__seconds = 0

    # сравнение
    def __eq__(self, other):
        return self.__hours == other.__hours and self.__minutes == other.__minutes and self.__seconds == other.__seconds

    # строка
    def __str__(self):
        return f'{self.__hours} часов {self.__minutes} минут {self.__seconds} секунд'

    # сложение
    def __add__(self, other):
        seconds = self.__seconds + other.__seconds
        minutes = self.__minutes + other.__minutes
        hours = self.__hours + other.__hours
        if seconds > 59:
            seconds -= 60
            minutes += 1
        if minutes > 59:
            minutes -= 60
            hours += 1
        return MyTime(hours, minutes, seconds)

    # сравнение больше
    def __gt__(self, other):
        if self.__hours > other.__hours:
            return True
        elif self.__hours == other.__hours:
            if self.__minutes > other.__minutes:
                return True
            elif self.__minutes == other.__minutes:
                if self.__seconds > other.__seconds:
                    return True
        return False


a = MyTime()
print('a =', a)
b = MyTime(1, 12, 50)
print('b =', b)
c = MyTime('00.01.12')
print('c =', c)
d = b + c
print("d =", d)
print("d > b ", d > b)
