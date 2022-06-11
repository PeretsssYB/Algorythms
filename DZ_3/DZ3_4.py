# Определить, какое число в массиве встречается чаще всего.

from statistics import multimode
from random import randint

n = int(input("Веедите количество элементов массива:\n"))
arr = [randint(0, 9) for i in range(n)] # создаем массив заданной длинны из случайных чисел # создаем массив заданной длинны из случайных чисел
ct_arr = []
for el in arr:
    ct = arr.count(el)
    ct_arr.append(ct)  # создаем список количеств повторений елементов массива arr
print(f'Массив: {arr}\nКол-во: {ct_arr}\n'
      f'Наиболее часто повторяющийся элемент массива: {multimode(arr)}')
