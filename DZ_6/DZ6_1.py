# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода
# для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

from __future__ import print_function
from sys import getsizeof
from collections.abc import Mapping, Container


def deep_getsizeof(o, ids):
    """Find the memory footprint of a Python object

    This is a recursive function that drills down a Python object graph
    like a dictionary holding nested dictionaries with lists of lists
    and tuples and sets.

    The sys.getsizeof function does a shallow size of only. It counts each
    object inside a container as pointer only regardless of how big it
    really is.

    :param o: the object
    :param ids:
    :return:
    """
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):
        return r

    if isinstance(o, Mapping):
        return r + sum(d(k, ids) + d(v, ids) for k, v in o.iteritems())

    if isinstance(o, Container):
        return r + sum(d(x, ids) for x in o)

    return r


def simple_num2(num: int):
    """Нахождение указанного по счету простого числа"""
    global lst2
    for j in range(2, (num**2) + 1):
        for k in lst2:
            if j % k == 0:  # если делитель найден, число не простое
                break
        else:
            lst2.append(j)
    return lst2


i = int(input("Введите какое по счету простое число нужно: "))
lst2 = []
simple_num2(i)
print(f'{i}-ое простое число: {lst2[i-1]}')
print(f'{deep_getsizeof(simple_num2(i), set())} - бит выделено под функцию simple_num2 (вычислено с помощью deep_getsizeof)')
print(f'{getsizeof(lst2)} бит выделено под переменную lst2 (вычислено стандартным getsizeof)')
print(f'{getsizeof(simple_num2(i))} бит выделено под функцию simple_num2(i) (вычислено стандартным getsizeof)')
print(f'{getsizeof(i)} бит выделено под переменную i (вычислено стандартным getsizeof)')

"""Результаты вычислений памяти позволяют сделать вывод, что чем большее число ищем, тем больше памяти задействуется под список:
1)  300-ое простое число: 1987
    319636 - бит выделено под функцию simple_num2 (вычеслено с помощью deep_getsizeof)
    75672 бит выделено под переменную lst2 (вычислено стандартным getsizeof)
    75672 бит выделено под функцию simple_num2(i) (вычислено стандартным getsizeof)
    28 бит выделено под переменную i (вычислено стандартным getsizeof)
2)  500-ое простое число: 3571
    811912 - бит выделено под функцию simple_num2 (вычислено с помощью deep_getsizeof)
    194680 бит выделено под переменную lst2 (вычислено стандартным getsizeof)
    194680 бит выделено под функцию simple_num2(i) (вычислено стандартным getsizeof)
    28 бит выделено под переменную i (вычислено стандартным getsizeof)
    
Данные получены на 64-битной Ubuntu c Python 3.10
"""