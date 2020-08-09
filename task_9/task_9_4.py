"""Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный."""


def check_list(func):
    def remove_even(*args):
        new_args = tuple([args[-1 - i] for i in range(len(args))])
        result = func(*new_args)
        return result
    return remove_even


@check_list
def my_func(*args):
    print(*args)
    return args


my_func(1, 2, 3)
