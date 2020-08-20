class Petr:

    def __init__(self, height, weight, age):
        self.__height = height
        self.__weight = weight
        self.__age = age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def do_something(self):
        print('Что то делает')

    def is_here(self):
        print('Просто здесь')


class Ivan:

    def __init__(self, height, weight, age):
        self.__height = height
        self.__weight = weight
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def do_something(self):
        print('Чем то занимается')

    def is_here(self):
        print('Тоже просто тут здесь')


class Grisha:

    def __init__(self, height, weight, age):
        self.__height = height
        self.__weight = weight
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def do_something(self):
        print('Флим флап..')

    def is_here(self):
        print('Трум трум')


person1 = Petr(201, 120, 16)
print(person1.get_age())
person2 = Ivan(180, 79, 24)
print(person2.weight)
person3 = Grisha(160, 55, 19)
person3.is_here()
