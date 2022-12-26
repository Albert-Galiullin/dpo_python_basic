guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

print('Сейчас на вечеринке 5 человек: ', guests)
count_qu = 5
while True:
    com = input('Гость пришёл или ушёл? ')
    if com == 'Пора спать' or com == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

    quest = input('Имя гостя: ')

    if com == 'пришёл' or  com == 'пришел':
        if count_qu < 6:
            print('Привет,', quest)
            count_qu += 1
            guests.append(quest)
        else:
            print('Прости,', quest, 'но мест нет')
    elif com == 'ушёл' or com == 'ушел':
        print('Пока,', quest)
        count_qu -= 1
        guests.remove(quest)
    print('Сейчас на вечеринке ', count_qu, 'человек(а): ', guests)
