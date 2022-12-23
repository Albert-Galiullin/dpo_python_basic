
spisok = []

N = int(input('Количество элементов:  '))
for _ in range(N):
    number = int(input('Введите число: '))
    spisok.append(number)

step = int(input('Введите сдвиг: '))

print()
print('Сдвиг: ', step)
print('Изначальный список: ', spisok)

a = len(spisok)
b = a - step

spisok1 = []
spisok2 = []
j = 1
for i in spisok:
    if j > b :
        spisok1.append(i)
    else:
        spisok2.append(i)
    j += 1

for i in spisok2:
    spisok1.append(i)

print('Сдвинутый список: ', spisok1)
