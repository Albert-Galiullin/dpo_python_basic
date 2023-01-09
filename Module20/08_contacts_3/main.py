# Пример работы программы:
#
# Введите номер действия:
#  1. Добавить контакт
#  2. Найти человека
#
# 1
# Введите имя и фамилию нового контакта (через пробел): Иван Сидоров
# Введите номер телефона: 888
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#  1. Добавить контакт
#  2. Найти человека
#
# Введите имя и фамилию нового контакта (через пробел) : Иван Сидоров
# Такой человек уже есть в контактах.
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888}
#
# Введите номер действия:
#  1. Добавить контакт
#  2. Найти человека
#
# 1
# Введите имя и фамилию нового контакта (через пробел): Алиса Петрова
# Введите номер телефона: 999
# Текущий словарь контактов: {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
#
# Введите номер действия:
#  1. Добавить контакт
#  2. Найти человека
#
# 2
# Введите фамилию для поиска: Сидоров
# Иван Сидоров 888
#
# Введите номер действия:
#
#  1. Добавить контакт
#  2. Найти человека

def search_f(surn):
    for i, j in phonebook.items():
        if surn in i[0].lower():
            lst = (i[0] + ' ' + i[1] + ' ' +str(j))
        else:
            lst = ('Нет такого человека')
    return lst



phonebook = {}

while True:

    print('Введите номер действия: ')
    print('1.Добавить контакт: ')
    print('2.Найти человека: ')
    nums = int(input('1 или 2: '))

    if nums == 1:
        name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
        phone = int(input('Введите номер телефона: '))
        name = tuple(name)
        phonebook[name] = phone
        print('Текущий словарь контактов: ', phonebook)

    elif nums == 2:
        surname = input('Введите фамилию для поиска: ').lower()
        print(search_f(surname))


