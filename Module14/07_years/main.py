print()
a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))

for i in range(a, b):
    year = i
    dig1 =  i // 1000
    dig2 =  i // 100 - dig1 * 10

    count_d1 = 0
    for i in str(year):
        if i == str(dig1):
            count_d1 += 1

    count_d2 = 0
    for i in str(year):
        if i == str(dig2):
            count_d2 += 1

    if count_d1 >= 3 or count_d2 >= 3:
        print('Год: ', year)