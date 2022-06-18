# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

company = collections.namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'y'])
companies = []
quant = int(input('Введите количество предприятий: '))
total = 0
for i in range(quant):
    name = input(f"Введите название {i+1}-ого предприятия: ")
    q1 = int(input(f"Введите прибыль за 1 квартал {i+1} предприятия: "))
    q2 = int(input(f"Введите прибыль за 2 квартал {i+1} предприятия: "))
    q3 = int(input(f"Введите прибыль за 3 квартал {i+1} предприятия: "))
    q4 = int(input(f"Введите прибыль за 4 квартал {i+1} предприятия: "))
    y = q1 + q2 + q3 + q4
    total += y
    companies.append(company(name=name, q1=q1, q2=q2, q3=q3, q4=q4, y=y))
total_avg = total / quant
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companies:
    if company.y > total_avg:
        print(company.name)
print(f"Предприятия с прибылью неже средней {total_avg}: ")
for company in companies:
    if company.y < total_avg:
        print(company.name)
