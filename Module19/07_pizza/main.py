# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5

pizza_dict = {}
pizza = int(input('Введите количество заказов: '))
for i in range(pizza):
    print(str(i + 1) + '-й заказ: ', end='')
    piz = input().split()
    if piz[0] not in pizza_dict:
        pizza_dict[piz[0]] = {piz[1]:int(piz[2])}
    else:
        if piz[1] not in pizza_dict[piz[0]]:
            pizza_dict[piz[0]].update({piz[1]:int(piz[2])})
        else:
            pizza_dict[piz[0]][piz[1]] +=int(piz[2])
for i, j in pizza_dict.items():
    print(i,':')
    for l, k in j.items():
        print('    ', l, k)
