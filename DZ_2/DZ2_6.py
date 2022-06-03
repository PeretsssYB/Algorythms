# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно
# сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

numb = random.randint(0, 101)
i = 0
while i <= 10:
    a = int(input("Введите загаданное число от 0 до 100: "))
    if a > numb:
        i += 1
        print(f"Нет, загаданное число меньше. Осталось {10 - i} попыток.")
    elif a < numb:
        i += 1
        print(f"Нет, загаданное число больше. Осталось {10 - i} попыток.")
    else:
        print(f"Вы угадали! Потрачено {i} попыток")
        break
else:
    print(f'Загаданное число {numb}. Вы потратили все попытки')
