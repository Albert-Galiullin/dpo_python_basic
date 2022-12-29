0
sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

spis = [x for x in range(1, sticks + 1)]
win = []

for i in range(1, throws + 1):
    print('Бросок ', i)
    throw1 = int(input('Cбиты палки  с  номера: '))
    throw2 = int(input('по номер: '))
    for j in range(throw1, throw2 + 1):
        win.append(j)

print('Все палки: ', spis)
print('Сбитые палки: ', win)

spis2 = [thr for thr in spis if thr not in win]
print('Несбитые палки: ', spis2)

line = ''

spis3 = ['I' if i not in win else '.' for i in range(1, sticks + 1)]
print(''.join(spis3))

