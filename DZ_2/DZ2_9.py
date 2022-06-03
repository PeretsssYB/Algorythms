# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def sumdigits(n):
    """Расчет максимальной суммы цифр числа"""
    sum_max = 0
    while n > 0:
        n, d = divmod(n, 10)
        sum_max += d
    return sum_max


numb = list(map(int, (input("Введите через пробел несколько натуральных чисел:\n")).split()))
summa = max(numb, key=sumdigits)

print(f'Наибольшее число: {summa}\nСумма цифр числа: {sumdigits(summa)}')
