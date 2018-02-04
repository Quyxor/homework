'''
Файл "data.txt" заполнен случайными целыми числами,
числа разделены одним пробелом.

    Сформировать файл "out-1.txt" из элементов файла "data.txt",
    делящихся без остатка на n

    Сформировать файл "out-2.txt" из элементов файла "data.txt",
    возведенных в степень p

n и p - целые числа, вводимые с клавиатуры.
'''

n = int(input())
p = int(input())

with open('data.txt') as data, \
     open('out-1.txt', 'w') as out1, \
     open('out-2.txt', 'w') as out2:

    for line in data:
        lst = line.split()
        lst_n = [int(numb) for numb in lst if int(numb) % n == 0]
        lst_p = [int(numb) ** p for numb in lst]
        out1.write(' '.join(str(numb) for numb in lst_n))
        out2.write(' '.join(str(numb) for numb in lst_p))
