"""Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5), стоп(сброс скорости на 0),
отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные."""


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def __str__(self):
        return f'{self.__brand}, {self.__model}, {self.__year}, {self.__speed}'

    def up_speed(self):
        self.__speed += 5

    def down_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed


new_car = Car('Мерседес', 's600', 2020)
print(new_car)
new_car.up_speed()
new_car.up_speed()
new_car.up_speed()
print(new_car.speed)
new_car.speed = 10
print(new_car.speed)
new_car.stop()
print(new_car.speed)
