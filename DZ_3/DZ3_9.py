# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

length, width = map(int, input("Введите количество столбцов и строк матрицы через пробел:\n").split())
a = []
for i in range(width):
    b = []
    for j in range(length):
        n = int(random.randint(0, 99))
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

biggest = 0 - 1
for j in range(length):
    minimal = 99 + 1
    for i in range(width):
        if a[i][j] < minimal:
            minimal = a[i][j]
    if minimal > biggest:
        biggest = minimal
print(f'Максимальный среди минимальных: {biggest}')
