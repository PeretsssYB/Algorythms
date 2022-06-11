# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

n = int(input("Веедите количество элементов массива:\n"))
arr = [randint(-99, 99) for i in range(n)] # создаем массив заданной длинны из случайных чисел
print(f'Массив: {arr}')
# находим индексы минимального и максимального элементов:
min_idx, max_idx = 0, 0
for i in range(1, n):
    if arr[i] < arr[min_idx]:
        min_idx = i
    elif arr[i] > arr[max_idx]:
        max_idx = i
print(f'Минимальный элемент: {arr[min_idx]}, Макимальный: {arr[max_idx]}')
# если минимальное число стоит после максимального, меняем их местами:
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx
# считаем сумму элементов:
mult = 0
for i in range(min_idx + 1, max_idx):
    mult += arr[i]
print(f'Сумма элементов: {mult}')
