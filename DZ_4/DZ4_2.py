# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#     Без использования «Решета Эратосфена»;
#     Используя алгоритм «Решето Эратосфена»
import trace

import time
import cProfile


def simple_num1(num: int):  # Решето Эратосфена
    """Сложность алгоритма O(n log(log n)) (цикл внутри цикла, с каждой итерацией цикл все меньше)"""
    global arr, lst1
    arr = [idx for idx in range((num**2) + 1)]
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < len(arr):  # перебор всех элементов до заданного числа
        if arr[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < len(arr):
                arr[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1
    lst1 = [arr[_] for _ in arr if arr[_] > 1]
    return lst1


def simple_num2(num: int):  # без "Решета Эратосфена"
    """Сложность алгоритма О(n**2) (цикл в цикле)"""
    global lst2
    for j in range(2, (num**2) + 1):
        for k in lst2:
            if j % k == 0:  # если делитель найден, число не простое
                break
        else:
            lst2.append(j)
    return lst2


i = int(input("Введите число: "))
lst2, lst1 = [], []
begin1 = time.perf_counter()
# cProfile.run('simple_num1(i)')
simple_num1(i)
print(#f'Массив после "Решета": {lst1}\n'
      f'{i}-ое простое число: {lst1[i-1]}')
print(f'Время выполнения 1: {time.perf_counter() - begin1}')
begin2 = time.perf_counter()
# cProfile.run('simple_num2(i)')
simple_num2(i)
print(#f'Массив: {lst2}\n'
      f'{i}-ое простое число: {lst2[i-1]}')
print(f'Время выполнения 2: {time.perf_counter() - begin2}')
"""Время выполнения: 
при 10  чисел:   |  при 50 чисел:
    1 - 0.0002  |  1 - 0.0067
    2 - 0.0001  |  2 - 0.0139
при 100:         |  при 500
    1 - 0.0092  |  1 - 0.1759
    2 - 0.0351  |  2 - 11.1019
"""
