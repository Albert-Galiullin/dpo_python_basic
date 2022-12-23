nums_list = []

N = int(input('Кол-во видеокарт: '))
for _ in range(N):
    num = int(input('Видеокарта: '))
    nums_list.append(num)

maximum = nums_list[1]

for i in nums_list:
    if maximum < i:
        maximum = i

new_nums_list = []
for i in nums_list:
    if i != maximum:
        new_nums_list.append(i)


print('Старый список видеокарт: ', nums_list)

print('Новый список видеокарт: ', new_nums_list)



