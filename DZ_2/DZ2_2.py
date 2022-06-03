# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

while True:
    try:
        numb = input("Введите натуральное число цифрами:\n")
        count_chet, count_nechet = 0, 0
        for i in numb:
            if int(i) % 2 == 0:
                count_chet += 1
            else:
                count_nechet += 1
        print(f'В введенном числе {count_chet} четные цифры и {count_nechet} нечетные')
        break
    except ValueError:
        print("Необходимо вводить цифры")
