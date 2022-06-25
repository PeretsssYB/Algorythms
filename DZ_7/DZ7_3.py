# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод
# сортировки, который не рассматривался на уроках

import random


def select_median(ar, pivot_fn=random.choice):
    if len(ar) % 2 == 1:
        return find_idx(ar, len(ar) / 2, pivot_fn)
    else:
        return 0.5 * (find_idx(ar, len(ar) / 2 - 1, pivot_fn) +
                      find_idx(ar, len(ar) / 2, pivot_fn))


def find_idx(ar, k, pivot_fn):
    """
    :param ar: список
    :param k: индекс
    :param pivot_fn: функция выбора индекса разделения списка, по умолчанию выбирает случайно
    :return: k-тый элемент списка(ar)
    """

    pivot = pivot_fn(ar)

    lows = [el for el in ar if el < pivot]
    highs = [el for el in ar if el > pivot]
    pivots = [el for el in ar if el == pivot]

    if k < len(lows):
        return find_idx(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return find_idx(highs, k - len(lows) - len(pivots), pivot_fn)


m = int(input('Введите натуральное число: '))
arr = []
while len(arr) < 2*m + 1:  # Создаем список от 1 до 2m+1 из неповторяющихся значений
    el = random.randint(1, 2*m+1)
    if el not in arr:
        arr.append(el)
print(f'Длинна массива {len(arr)} элементов\n'
      f'Исходный массив: {arr}')

median = select_median(arr)

print(f'Медиана = {median}\n'
      f'Отсортированный список: {sorted(arr)}')
