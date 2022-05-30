# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string


numb = [i for i in range(1, 27)]
alfabet = dict(zip(numb, list(string.ascii_letters)))
while True:
    try:
        letter = int(input("Введите номер буквы:\n"))
        if 0 < letter < 27:
            print(f'Под этим номером в алфавите буква "{str(alfabet[letter]).upper()}"')
            break
        else:
            print('В алфавите 26 букв')
    except ValueError:
        print("Необходимо ввести число")
