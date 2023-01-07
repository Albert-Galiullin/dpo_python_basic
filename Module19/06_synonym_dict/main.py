# Введите количество пар слов: 3
# Первая пара: Привет - здравствуй
# Вторая пара: Печально - Грустно
# Третья пара: Весело - Радостно
#
# Введите слово: интересно
# Такого слова в словаре нет.
#
# Введите слово: здравствуйте
# Синоним: Привет
syn_dict = {}
synonyms = int(input('Введите количество пар слов через дефис: '))
for i in range(synonyms):
    print(str(i + 1) + '-я пара: ', end='')
    syn = input().lower()
    syn = syn.replace(" ", "").split('-')
    syn_dict[syn[0]] = syn[1]
print(syn_dict)

print()

for l in range(2):
    pr = False
    word = input('Введите слово: ')
    for i, j in syn_dict.items():
        if word == i:
            print('Синоним: ', j)
            pr = True
            break
        elif word == j:
            print('Синоним: ', i)
            pr = True
            break
    if pr == False:
        print('Такого слова в словаре нет.')


