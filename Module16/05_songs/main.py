violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
print(violator_songs)
some_songs = []
amount = int(input('Сколько песен выбрать? '))
time = 0
for i in range(amount):
    print('Название',  str(i + 1)+'-й песни: ', end = '')
    song = input()
    for i in range(len(violator_songs)):
       if song == violator_songs[i][0]:
            time += violator_songs[i][1]
            some_songs.append(song)
        # else:
        #     print('Такой песни не найдено')

print('Общее время звучания песен: ', time, ' минут')