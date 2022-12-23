word = input('Введите слово: ')
letters1 = []
letters2 = []
n_let = len(word)
word = list(word)

l = 0
count_u = 0

n_let2 =  n_let // 2

for i in range(n_let2):
    letters1.append(word[i])

for i in range(n_let2):
    n_let -= 1
    letters2.append(word[n_let])

if letters1 == letters2:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')

