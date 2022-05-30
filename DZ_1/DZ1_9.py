# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

while True:
    try:
        a, b, c = map(int, input("Введите 3 числа через пробел:\n").split())
        if a < b < c:
            print(f'Среднее число: {b}')
            break
        elif a > b < c:
            print(f'Среднее число: {a}')
            break
        else:
            print(f'Среднее число: {c}')
            break
    except ValueError:
        print("Нужно ввести числа")
