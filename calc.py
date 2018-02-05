'''
В предыдущей задаче от вас требовалось реализовать функцию convert(expr),
которая принимала в качестве единственного аргумента математическое выражение
и возвращала его запись в ОПН.
Теперь от вас требуется написать программу "Калькулятор".
Он должен работать в двух режимах:
    в режиме Python-модуля
    в режиме исполняемого Python-скрипта.
'''
from operator import add, sub, mul, truediv, pow


OP_DICT = {'^': pow, '*': mul, '/': truediv, '+': add, '-': sub}
OPS = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

def exist_precedence(prev_char, that_char):

    return OPS[prev_char] >= OPS[that_char]

def pop_greater(ops, op):
    out = []

    while True:
        if not ops:
            break

        if not exist_precedence(ops[-1], op):
            break

        out.append(ops.pop())
        out.append(' ')

    return out


def pop_until(ops):
    out = []

    while True:
        op = ops.pop()

        if op == '(':
            break

        out.append(op)
        out.append(' ')

    return out


def convert(expr):
    temp_expr = ''.join(expr.split())

    output = []
    stack = []

    for char in temp_expr:
        if char == '(':
            stack.append(char)
            continue
        elif char == ')':
            output.extend(pop_until(stack))
            continue
        elif char in OPS:
            output.extend(pop_greater(stack, char))
            stack.append(char)
            continue
        elif char.isdigit() or char.isalpha():
            output.append(char)
            output.append(' ')

    reversed_stack = stack[::-1]

    for elem in reversed_stack:
        output.append(elem)

        if elem != reversed_stack[-1]:
            output.append(' ')

    return ''.join(output)


def calc(expr):
    stack = []
    expr_conv = convert(expr).split()

    for char in expr_conv:
        if char in OP_DICT:
            b, a = stack.pop(), stack.pop()
            stack.append(OP_DICT[char](a, b))
        else:
            stack.append(int(char))

    return sum(stack)


if __name__ == '__main__':
    print(calc(input()))
