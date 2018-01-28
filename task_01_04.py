'''
ЗАДАЧА_3:
Напишите программу, предлагающую пользователю ввести три вершины.
Координаты X и Y (2 числа), заданы как целые числа, т.е. int.
Нужно определить является ли треугольник, с указанными координатами, прямоугольным.
В решении использовать только математические и логические операторы.
В вычислениях запрещено(!!!) переходить в дробные числа.

Если треугольник прямоугольный - вывести на экран "yes"
Если треугольник не прямоугольный - вывести на экран "no"
'''

#Координаты вершины A
AVERTEX_X = int(input())
AVERTEX_Y = int(input())
#Координаты вершины B
BVERTEX_X = int(input())
BVERTEX_Y = int(input())
#Координаты вершины C
CVERTEX_X = int(input())
CVERTEX_Y = int(input())

#Координаты вектора AB
AB_VECTOR_X = BVERTEX_X - AVERTEX_X
AB_VECTOR_Y = BVERTEX_Y - AVERTEX_Y
#Координаты вектора CB
CB_VECTOR_X = BVERTEX_X - CVERTEX_X
CB_VECTOR_Y = BVERTEX_Y - CVERTEX_Y
#Координаты вектора AC
AC_VECTOR_X = CVERTEX_X - AVERTEX_X
AC_VECTOR_Y = CVERTEX_Y - AVERTEX_Y
#Координаты вектора BC
BC_VECTOR_X = CVERTEX_X - BVERTEX_X
BC_VECTOR_Y = CVERTEX_Y - BVERTEX_Y
#Координаты вектора BA
BA_VECTOR_X = AVERTEX_X - BVERTEX_X
BA_VECTOR_Y = AVERTEX_Y - BVERTEX_Y
#Координаты вектора CA
CA_VECTOR_X = AVERTEX_X - CVERTEX_X
CA_VECTOR_Y = AVERTEX_Y - CVERTEX_Y

#Скалярное произведение векторов
ABCB = AB_VECTOR_X * CB_VECTOR_X + AB_VECTOR_Y * CB_VECTOR_Y
ACBC = AC_VECTOR_X * BC_VECTOR_X + AC_VECTOR_Y * BC_VECTOR_Y
BACA = BA_VECTOR_X * CA_VECTOR_X + BA_VECTOR_Y * CA_VECTOR_Y

#Если скалярное произведение векторов = 0, то угол между ними = 90°
if not ABCB or not ACBC or not BACA:
    print('yes')
else:
    print('no')
