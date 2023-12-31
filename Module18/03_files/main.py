# Пример 1:
# Название файла: @example.txt
# Ошибка: название начинается на один из специальных символов.
#
# Пример 2:
# Название файла: example.ttx
# Ошибка: неверное расширение файла.Ожидалось.txt или.docx.
#
# Пример 3:
#
# Название файла: example.txt
# Файл назван верно.

symbols = list('@№$%^&*()')
filename = input('Название файла: ')

if filename[:1] in symbols:
    print('Ошибка: название начинается на один из специальных символов')
elif not (filename.endswith('.txt') or filename.endswith('.docx')):
    print('Неверное расширение файла.Ожидалось.txt или.docx')
else:
    print('Файл назван верно')
