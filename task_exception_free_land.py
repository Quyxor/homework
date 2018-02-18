'''
Напишите функцию get_free_land, которая принимает два аргумента, оба из которых кортежи:

    площадь садового участка в сотках и соотношение сторон
    ширину и длину одной грядки в метрах.

Функция разбивает грядки на участке и возвращает количество незанятого места в квадратных метрах.

1 сотка - это квадрат земли площадью 100м2.

В случае ошибок нужно выбросить исключение типа ValueError с сообщеним:

    "Не задана площадь участка"
    "Не задана площадь грядки"
    "Размер грядки больше размера участка"
'''
from collections import namedtuple
from math import sqrt


ERRORS = {
    'empty_plot': "Не задана площадь участка",
    'empty_bed': "Не задана площадь грядки",
    'wrong_bed': "Размер грядки больше размера участка"
}


def get_named_tuple(some_tuple, name, *args):
    try:
        Record = namedtuple(name, *args)
        return Record(*some_tuple)
    except:
        raise('Некорректные входные данные: {}'.join(some_tuple))


def get_sides(area):
    x, y = map(int, area.ratio.split(':'))
    area_m = area.weav * 100
    return sqrt(area_m / x), sqrt(area_m / y)


def get_free_land(plot, bed):
    plot_named = get_named_tuple(plot, 'Plot', ['weav', 'ratio'])
    bed_named = get_named_tuple(bed, 'Bed', ['width', 'length'])

    if plot_named.weav <= 0:
        raise ValueError(ERRORS['empty_plot'])

    x, y = get_sides(plot_named)

    if (
        max(bed_named.width, bed_named.length) > max(x, y) or
        min(bed_named.width, bed_named.length) > min(x, y)
    ):
        raise ValueError(ERRORS['wrong_bed'])

    if bed_named.width <= 0 or bed_named.length <= 0:
        raise ValueError(ERRORS['empty_bed'])

    return plot_named.weav * 100 % int(bed_named.width) * int(bed_named.length)
