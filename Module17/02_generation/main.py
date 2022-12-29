len_spis = int(input('Введите длину списка: '))
spis = [i for i in range(len_spis)]
print('Первоначальный список:', spis)
new_spis = [1 if spis.index(x) % 2 == 0 else spis.index(x) % 5 for x in spis]
print('Сгенерированный список:', new_spis)
