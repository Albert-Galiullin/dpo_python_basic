def divider(a):

    i = 2
    while i <= a:
        if a % i == 0:
            j = i
            print()
            print('Наименьший делитель:', j)
            break
        i += 1


print()
a = int(input('Введите число: '))
divider(a)

