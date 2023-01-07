# Пример:
# Введите количество человек: 9
#
# Первая пара: Alexei Peter_I
# Вторая пара: Anna Peter_I
# Третья пара: Elizabeth Peter_I
# Четвёртая пара: Peter_II Alexei
# Пятая пара: Peter_III Anna
# Шестая пара: Paul_I Peter_III
# Седьмая пара: Alexander_I Paul_I
# Восьмая пара: Nicholaus_I Paul_I
#
# «Высота» каждого члена семьи:
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2

people = int(input('Введите количество человек: '))
tree = {}
for i in range(1, people):
    print(str(i) + '-я пара: ', end='')
    couple = input().split()
    tree[couple[0]] = couple[1]

# tree = {'Alexei': 'Peter_I',
#         'Anna': 'Peter_I',
#         'Elizabeth': 'Peter_I',
#         'Peter_II': 'Alexei',
#         'Peter_III': 'Anna',
#         'Paul_I': 'Peter_III',
#         'Alexander_I': 'Paul_I',
#         'Nicholaus_I': 'Paul_I'
#         }

tree_2 = {}
k = 0

for i, j in tree.items():
    if j not in tree_2 and i not in tree_2:
        tree_2[j] = k
        tree_2[i] = k + 1
        k += 1
    elif j in tree_2 and i not in tree_2 and j not in tree.keys():
        tree_2[i] = k
    elif j in tree_2 and i not in tree_2 and j in tree.keys():
        tree_2[i] = tree_2[j] + 1

for i in sorted(tree_2.keys()):
    print(i, ':', tree_2[i])





