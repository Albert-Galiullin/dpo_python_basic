numbers = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_numbers = []
j = 0
for i in numbers:
    if j % 2 == 0:
        new_numbers.append(i)
    j += 1
print('Первый день: ', new_numbers)
