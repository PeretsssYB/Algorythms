# Определить, является ли год, который ввел пользователь, високосным или нет.
# Високосным годом является тот год, который нацело делится на 4,
# кроме столетий (исключением являются столетия делящиеся на 400).

while True:
    try:
        year = int(input("Введите год для проверки:\n"))
        if year % 4 != 0:  # or year % 100 == 0:
            print(f'Год {year} не является високосным')
            break
        elif year % 400 == 0:
            print(f'Год {year} является високосным')
            break
        elif year % 100 == 0:
            print(f'Год {year} не является високосным')
            break
        else:
            print(f'Год {year} является високосным')
            break
    except ValueError():
        print('Нужно ввести год числами')