# Введите строку: я есть строка
# Самое длинное слово: строка
# Длина этого слова: 6

text = input('Введите строку: ').split()
len_text = 0
j = ''
for i in text:
    if len(i) > len_text:
        len_text = len(i)
        j = i
print('\nСамое длинное слово: ', j)

