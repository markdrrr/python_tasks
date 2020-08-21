"""Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle(атрибуты: координаты центра(тип Point),
длина радиуса; методы: нахождение периметра и площади окружности),
Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
Square(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:

    def perimeter(self):
        pass

    def square(self):
        pass

    class Circle:

        def __init__(self, x, y, length_radius):
            self.length_radius = length_radius
            self.center_coordinates = Point(x, y)

        def perimeter(self):
            return 2 * 3.141592 * self.length_radius

        def square(self):
            return 3.141592 * self.length_radius ** 2

    class Triangle:

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def perimeter(self):
            return self.a + self.b + self.c

        def square(self):
            return (self.perimeter() * (self.perimeter() - self.a) * (self.perimeter() - self.b) * (
                    self.perimeter() - self.c)) ** 0.5

    class Square:

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def perimeter(self):
            return 4 * self.a

        def square(self):
            return self.a ** 2


list_figure = [Figure.Circle(2, 2, 2), Figure.Triangle(1, 2, 3), Figure.Square(4, 4)]
for el in list_figure:
    print('Квадрат фигуры = ', el.square())
