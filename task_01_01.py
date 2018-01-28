'''
ЗАДАЧА_1:
Попросить пользователя ввести с клавиатуры год.

Если год високосный - вывести на экран "yes"
Если год не високосный - вывести на экран "no"

Год не является високосным в двух случаях:
    1. он кратен 100, но при этом не кратен 400
    2. либо он не кратен 4
'''

YEAR = int(input())

if YEAR >= 0:
    if (not YEAR % 100 and YEAR % 400) or YEAR % 4:
        print('no')
    else:
        print('yes')
