'''
Напишите функцию get_days_to_new_year, которая возвращает количество дней,
оставшихся до нового года.
Датой наступления нового года считается 1 января.
Функция должна корректно работать при запуске в любом году,
т. е. грядущий год должен вычисляться программно.
Для решения задачи понадобится стандартный модуль datetime
Требуется реализовать только функцию,
решение не должно осуществлять операций ввода-вывода.
'''
from datetime import datetime, date


def get_days_to_new_year():

    now = datetime.now()
    new_year = date(now.year + 1, 1, 1)
    today = date(now.year, now.month, now.day)

    count = (new_year - today).days

    return count


if __name__ == '__main__':
    print(get_days_to_new_year())
