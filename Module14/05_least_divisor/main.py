def divider(a, b):
    if a < b:  # Определяем приблизительную максимальную границу для деления
        maxi_div = b / 2
    else:
        maxi_div = a / 2

    i = 2
    while i <= maxi_div:
        if a % i == 0 and b % i == 0:
            j = i
            print()
            print('Наименьший общий делитель:', j)
            break
        i += 1


print()
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
divider(a, b)

