word = input('Введите слово: ')
letters = []
n_let = len(word)
word = list(word)
l = 0
count_u = 0

for i in range(n_let):
    letter = word[i]
    for j in word:
        if j == letter:
            l += 1
    if l == 1:
        count_u += 1
    l = 0

print('Количество уникальных букв: ', count_u)



