'''
Напишите функцию get_quadrant_number, которая принимает координаты точки X и Y
и возвращает номер четверти, которой эта точка принадлежит.
Помните, что если точка лежит на оси, то она не принадлежит ни одной четверти,
в этом случаи нужно выбросить исключение типа ValueError без сообщения об ошибке.
'''


def get_quadrant_number(x, y):

    if not x or not y:
        raise ValueError

    if x > 0:
        return 1 if y > 0 else 4
    elif x < 0:
        return 2 if y > 0 else 3
