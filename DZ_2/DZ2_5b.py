# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

numb = [i for i in range(32, 128)]
symb = [chr(i) for i in range(32, 128)]
asc = dict(zip(numb, symb))
for i in asc:
    if i < 100:
        print(f' {i} это "{asc[i]}"', end=' | ')
    else:
        print(f'{i} это "{asc[i]}"', end=' | ')
    if (i - 1) % 10 == 0:
        print()



for i in range(32, 128):
    print("%4d - %s" % (i, chr(i)), end=' | ')
    if (i - 1) % 10 == 0:
        print()