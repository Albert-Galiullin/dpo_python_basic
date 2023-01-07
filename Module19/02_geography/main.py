country = int(input('Количество стран: '))
coun_dict = {}
for i in range(country):
    print(str(i + 1)+'-я страна и ее города: ', end = '')
    coun = input().split()
    coun_dict[coun[0]] = coun[1:]

print()
print(coun_dict)
print()

for i in range(3):
    print(str(i + 1) + '-й город: ', end='')
    city = input()
    pr = False
    for key, value in coun_dict.items():

        for k in value:
            if k == city:
                print('Город', city, 'расположен в стране', key)
                pr = True
                break

    if not pr:
        print('По городу', city, 'данных нет')




