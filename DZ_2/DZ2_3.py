# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести
# на экран. Например, если введено число 3486, то надо вывести число 6843.

while True:
    try:
        numb = int(input("Введите любое число цифрами:\n"))
        rev_numb = 0
        while numb > 0:
            n1 = numb % 10
            rev_numb = (rev_numb * 10) + n1
            numb = numb // 10
        print(f'Введенное число в обратном порядке: {rev_numb}')
        break
    except ValueError:
        print("Необходимо вводить цифры")
