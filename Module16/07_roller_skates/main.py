
amount_rol = int(input('Кол-во коньков: '))
rols = []
for i in range(amount_rol):
    print('Размер',  str(i + 1)+'-й пары: ', end = '')
    rol = input()
    rols.append(rol)
rols.sort()
print(rols)

amount_people = int(input('\nКол-во людей: '))
legs = []
for i in range(amount_people):
    print('Размер ноги', str(i + 1) + '-го человека: ', end='')
    leg = input()
    legs.append(leg)
legs.sort()
print(legs)

count_ = 0
l = amount_people
i = 0
while i < l:
    for j in rols:
        if legs[i] <= j:

            legs.remove(legs[i])
            rols.remove(j)
            # print(rols)
            # print(legs)
            count_ += 1
            l -= 1
            i -= 1
    i += 1

print('Наибольшее кол-во людей, которые могут взять ролики: ', count_)
