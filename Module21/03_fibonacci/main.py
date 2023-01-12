def lst(st1, st2, ps1, pos):
    if ps1 == pos:
        return st2
    else:
        st3 = st1 + st2
        st1 = st2
        st2 = st3
        print(st3, '- позиция: ', ps1 + 1)
        ps1 += 1
        return lst(st1, st2, ps1, pos)

print('Вычисление позиции по ряду Фибоначчи')
num_pos = int(input('Введите позицию в ряде Фибоначчи: '))
print()
start1 = 0
start2 = 1
pos1 = 1
a = lst(start1, start2, pos1, num_pos)
print('\nНа позиции', num_pos, ' нахлждится число', a)


# 0 + 1 = 1
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# 5 + 8 = 13