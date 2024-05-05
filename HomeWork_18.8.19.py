tickets = int(input("Введите желаемое к приобретению количество билетов: "))
all_price = 0
for i in range(tickets):
    i += 1
    age = int(input(f" Введите возраст посетителя {i} : "))
    if age < 18:
        all_price += 0
    elif 18 <= age < 25:
        all_price += 990
    else:
        all_price += 1390
if tickets > 3:
    print("Скидка за количество билетов составила: ", all_price / 100 * 10)
    all_price -= all_price / 100 * 10
print("Общая стоимость билетов = ", all_price)
