# По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y=kx+b, проходящей через эти точки
# print(" y = %.2f*x + %.2f" % (k, b))
while True:
    try:
        x1, y1, x2, y2 = map(float, input('Введите координаты точек "A" и "B" через запятую для построения '
                                          'уравнения прямой:\n').split(","))
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if b > 0:
            print(f'y = {round(k, 2)}*x+{round(b, 2)}')
        elif b < 0:
            print(f'y = {round(k, 2)}*x{round(b, 2)}')
        else:
            print(f'y = {round(k, 2)}*x')
        break
    except ValueError:
        print("Нужно ввести 4 числа")
