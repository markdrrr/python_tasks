""" Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка. """


def check_list(func):
    def remove_even(args):
        new_list = [el for el in args if el % 2 == 0]
        result = func(new_list)
        return result
    return remove_even


@check_list
def my_func(list_number):
    print(list_number)
    return list_number


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
my_func(numbers)
