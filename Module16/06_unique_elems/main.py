spis1 = []
spis2 = []

for i in range(3):
    print('Ввведите',  str(i + 1)+'-е число для первого списка: ', end = '')
    number = input()
    spis1.append(number)
print(spis1)

for i in range(7):
    print('Введите',  str(i + 1)+'-е число для второго списка: ', end = '')
    number = input()
    spis2.append(number)
print(spis2)

spis1.extend(spis2)
print(spis1)
l = 10
i = 0
while i <  l:
    a = spis1.count(spis1[i])
    if a > 1:

        per = spis1[i]
        for _ in range(a - 1):
            spis1.remove(per)
            l -= 1

    i += 1
print(spis1)