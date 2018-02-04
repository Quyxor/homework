'''
Реализуйте модуль number_system
для перевода числа из одной системы счисления в другую.
Модуль должен содержать 6 функций для перевода из десятичной системы счисления
в двоичную, восьмеричную, шестнадцатиричную и наоборот
'''

CHAR_DICT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '0': 0,
            'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def all2dec(input_str, base):

    result = []

    for ind, char in enumerate(input_str[::-1]):

        if char in CHAR_DICT:
            char = CHAR_DICT[char]
            result.append(char * base ** ind)

    return sum(result)


def dec2all(input_numb, base):

    result = []

    while input_numb or input_numb >= base - 1:
        div_res = input_numb % base
        result.append(str(div_res) if div_res < 10 else get_key(div_res))
        input_numb //= base

    return ''.join(result[::-1])


def get_key(numb):
    for key, value in CHAR_DICT.items():
        if value == numb:
            return key


def bin2dec(number):
    return all2dec(number, 2)


def oct2dec(number):
    return all2dec(number, 8)


def hex2dec(number):
    return all2dec(number, 16)


def dec2bin(number):
    return dec2all(number, 2)


def dec2oct(number):
    return dec2all(number, 8)


def dec2hex(number):
    return dec2all(number, 16)


if __name__ == '__main__':
    print(bin2dec("1010011010"))
    print(oct2dec("755"))
    print(hex2dec("abcde*f"))
    print(dec2bin(250))
    print(dec2oct(250))
    print(dec2hex(250))
