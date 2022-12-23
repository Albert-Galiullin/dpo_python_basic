films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

love_list = []

N = int(input('Сколько фильмов хотите добавить?  '))
for _ in range(N):
    name = input('Введите название фильма: ')
    for i in films:
        if name == i:
            pr = True
            break
        else:
            pr = False
    if pr == False:
        print('Ошибка: фильма ', name, 'у нас нет:(' )
    else:
        love_list.append(name)

print('Ваш список любимых фильмов: ', end = ' ')
j = 0
for i in love_list:
    print(love_list[j], end = ' ')
    j += 1



