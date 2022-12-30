text = input('Введите строку: ')

for i in text:
    if i == 'h':
        index1 = text.index(i)
        break

for i in range(-1, (-1) * len(text), -1):
    if text[i] == 'h':
        index2 = len(text) + i
        break

text2 = []

for i in range(index2 - index1):
    text2.append(text[i])

print('Развёрнутая последовательность между первым и последним h: ', ''.join(text2[index2: index1: -1]))
