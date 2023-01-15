# Пример 1
#
# Введите строку: programm test
#
# Куда хотите сохранить документ? Введите последовательность папок(через пробел):
#
# Users Roman PycharmProjects Skillbox Module22
#
# Введите имя файла: my_document
#
# Файл успешно сохранён!
#
# Содержимое файла: programm test
#
# Пример 2
#
# Введите строку: testiruyem
# Куда хотите сохранить документ?
# Введите последовательность папок(через пробел):
# Users Roman PycharmProjects Skillbox Module22
#
# Введите имя файла: my_document
#
# Вы действительно хотите перезаписать файл? да
#
# Файл успешно перезаписан!

import os

def save(text):
    print('Куда хотите сохранить документ?')
    path_i = input('Введите последовательность папок(через пробел): ')
    path_i = 'C:\\' + path_i.replace(' ','\\')

    if not os.path.exists(path_i):
        print('Такого пути не существует')
        return

    name_fil = input('Введите имя файла: ')
    path_i = os.path.join(path_i, name_fil)
    print(path_i)
    if os.path.exists(path_i):
        ans = input('Вы действительно хотите перезаписать файл? ').lower()
        if ans == 'да':
            file_result = open(path_i, "w", encoding="utf8")
            file_result.write(text)
            print('Фвйл успешно перезаписан')
        else:
            return
    else:
            file_result = open(path_i, "w", encoding="utf8")
            file_result.write(text)
            print('Фвйл успешно сохранен')

text = input('Введите строку: ')
save(text)

























