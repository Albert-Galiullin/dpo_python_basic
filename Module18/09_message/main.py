# Пример 1:
# Сообщение: Это задание очень! простое.
# Новое сообщение: отЭ еинадаз ьнечо! еотсорп.
#
# Пример 2:
# Сообщение: Хотя, возм: ожно и нет.
# Новое сообщение: ятоХ, мзов: онжо и тен.

import string
text = 'Это задание очень! простое.'

text = text.split()
text1 = [word[::-1] for word in text]

print(text1)

word_t = ''
znak = ''
text2 = []
for i in text1:
    for j in i:
        if j not in string.punctuation:
            word_t += j

        else:
            znak += j
    i = word_t + znak
    text2.append(i)
    print(i)
    word_t = ''
    znak = ''

text2 = ' '.join(word for word in text2)
print(text2)
