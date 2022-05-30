# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

while True:
    numb = str(input('Введите 3х значное число:\n'))
    if int(numb) > 99 and int(numb) < 1000:
        suma, mult = 0, 1
        for i in numb:
            suma += int(i)
            mult *= int(i)
        print(f'Сумма цифр составляет {suma} \nПроизведение цифр: {mult}')
        break
    else:
        print("требуется ввести 3х значное число цифрами")
