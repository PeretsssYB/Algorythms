# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


from random import randint

n = int(input("Веедите количество элементов массива:\n"))
arr = [randint(-99, 99) for i in range(n)] # создаем массив заданной длинны из случайных чисел  # создаем массив заданной длинны из случайных чисел
el, idx = 0, -1
while el < n:
    if arr[el] < 0 and idx == -1:
        idx = el
    elif arr[idx] < arr[el] < 0:
        idx = el
    el += 1
print(f'Массив: {arr}\nМаксимальный отрицательный элемент: {arr[idx]}\n'
      f'Позиция элемента: {idx + 1}')
