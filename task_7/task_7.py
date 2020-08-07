"""  Написать программу, со следующим интерфейсом: пользователю предоставляется
 на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
 от одного до двенадцати. После программа запрашивает ввести численное значение.
 Затем программа выдает конвертированный результат. Использовать функции из первого задания.
 Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты """
run = True


def convert(menu, number):
    if menu == 1:
        return number * 2.54
    elif menu == 2:
        return number * 0.39
    elif menu == 3:
        return number * 1.61
    elif menu == 4:
        return number * 0.62
    elif menu == 5:
        return number * 0.45
    elif menu == 6:
        return number * 2.2
    elif menu == 7:
        return number * 28.35
    elif menu == 8:
        return number * 0.035
    elif menu == 9:
        return number * 4.55
    elif menu == 10:
        return number * 0.22
    elif menu == 11:
        return number * 0.57
    elif menu == 12:
        return number * 1.76


while run:
    menu = int(input('Введите от 1 до 12: '))
    if menu in [i for i in range(13)]:
        if menu == 0:
            print('Closed')
            run = False
        else:
            number = int(input('Введите значение: '))
            print(convert(menu, number))
