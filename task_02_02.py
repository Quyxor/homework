'''
Напишите функцию bubble_sort(lst), которая принимает список из чисел,
и выполняет сортировку списка по возрастанию методом пузырька
и возвращает получившийся список.

(!) Запрещено использовать встроенные возможности языка для сортировки.
(!) Т.к. готовый код данной задачи легко нагуглить,
то необходимо пояснить каждую строчку в коде с помощью комментариев!

Требуется реализовать только функцию,
решение не должно осуществлять операций ввода-вывода.
'''

def bubble_sort(lst):
    # длинна списка = количеству элементов,
    # индекс последнего элемента на единицу меньше
    i = len(lst) - 1
    not_ordered = True # критерий остановка цикла while

    while not_ordered:
        not_ordered = False # по умолчанию, думаем, что список отсортирован

        for j in range(0, i): # будем перебирать элементы с индексами от 0 до i
            # если элемент списка больше своего соседа справа, то
            # мы меняем их местами, тем самым продвигая элемент с большим
            # значением в правую сторону, а меньший в левую
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                # признак того, что нашлась хотя бы одна пара, которую поменяли
                # местами, а соответственно список еще не был отсортирован
                not_ordered = True
        # т.к. после первого прогона, наибольший элемент займет свое место,
        # встанет под последним индексом списка, то при следующем прогоне нет
        # смысла вести с ним сравнение, уменьшаем диапазон прогона,
        # для сокращения времени работы цикла
        i -= 1

    return lst # возвращаем отсортированый список
