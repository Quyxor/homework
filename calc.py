'''
В предыдущей задаче от вас требовалось реализовать функцию convert(expr),
которая принимала в качестве единственного аргумента математическое выражение
и возвращала его запись в ОПН.

Теперь от вас требуется написать программу "Калькулятор".

Он должен работать в двух режимах:
    в режиме Python-модуля
    в режиме исполняемого Python-скрипта.
'''
from task_rpn import convert
from operator import add, sub, mul, truediv


OP_DICT = {'^': pow, '*': mul, '/': truediv, '+': add, '-': sub}


def calc(expr):
    stack = []
    expr_conv = convert(expr).split()

    for char in expr_conv:
        if char in OP_DICT:
            b, a = stack.pop(), stack.pop()
            stack.append(OP_DICT[char](a, b))
        else:
            stack.append(float(char))

    return sum(stack)


if __name__ == '__main__':
    print(calc(input()))
