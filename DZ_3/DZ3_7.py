# В одномерном массиве целых чисел определить два наименьших элемента. Они могут
# быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

n = int(input("Веедите количество элементов массива:\n"))
arr = [randint(0, 99) for i in range(n)]
print(f'Массив: {arr}')
min1 = min(arr)  # минимальный элемент 1
arr.remove(min1)
min2 = min(arr)  # минимальный элемент 2 (из оставшихся)
print(f'Минимальный элемент 1: {min1},'
      f' Минимальный элемент 2: {min2}')
