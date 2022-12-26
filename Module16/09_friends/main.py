fri = int(input('Кол-во друзей: '))
credit = int(input('Долговых расписок '))
massiv1 = []
massiv2 = []

for i in range(credit):
    print(i+1, '-я расписка')
    get_ = int(input('Кому: '))
    give_= int(input('От кого: '))
    sum = int(input('Сколько: '))

    massiv1.append(get_)
    massiv1.append(give_)
    massiv1.append(sum)
    massiv2.append(massiv1)

    massiv1 = []
print(massiv2)

balans1 = 0
balans2 = 0
print('Баланс друзей:')

i = 1
j = 1
while j <= fri:
    while i <=  credit:
        if massiv2[i-1][0] == j:
            balans1 -= massiv2[i-1][2]
        if massiv2[i-1][1] == j:
            balans2 += massiv2[i-1][2]
        i += 1
    print(j, ':', balans1 + balans2)
    balans1 = 0
    balans2 = 0
    i = 1
    j += 1



