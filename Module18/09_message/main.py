# Пример 1:
# Сообщение: Это задание очень! простое.
# Новое сообщение: отЭ еинадаз ьнечо! еотсорп.
#
# Пример 2:
# Сообщение: Хотя, .возм: ожно и нет.
# Новое сообщение: ятоХ, мзов: онжо и тен.


text = input('Введите текст: ')
word = ''
new_text = ''
for char in text:
    if char.isalpha():
        word += char
    else:
        word = word[::-1]
        new_text += word + char
        word = ''
print(new_text)
