# Введите строку: aaAAbbсaaaA
# Закодированная строка: a2A2b2с1a3A1

text = input('Введите строку: ')
text = list(text)
j = text[0]
new_text = ''
coun = 1

for i in text[1:]:
    if i != j:
        new_text += j + str(coun)
        j = i
        coun = 1
    else:
        coun += 1
new_text += j + str(coun)
print('Закодированная строка: ', new_text)




