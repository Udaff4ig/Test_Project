per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Ставки банков: ", per_cent)
dep = list(per_cent.values())
money = float(input('Введите сумму вклада: '))
dep_1 = [dep[0]*money/100, dep[1]*money/100, dep[2]*money/100, dep[3]*money/100]
print("Прибыль за год: ", dep_1)
print("Максимальная сумма, которую вы можете заработать за год: ", max(dep_1))
