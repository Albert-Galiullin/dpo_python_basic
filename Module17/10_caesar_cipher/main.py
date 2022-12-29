alphabit = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя')

text = input('Введите сообщение: ')
step = int(input('Введите сдвиг:'))
step = step % 33

sh_word = []
for char in range(len(text)):
    if text[char] in alphabit:
        sh = alphabit.index(text[char]) + step
        sh_word.append(alphabit[sh])
    else:
        sh_word.append(text[char])

print(''.join(sh_word))