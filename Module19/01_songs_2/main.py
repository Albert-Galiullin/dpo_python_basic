violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

print(violator_songs)
print()

some_songs = []
amount = int(input('Сколько песен выбрать? '))
time = 0
for i in range(amount):
    print('Название',  str(i + 1)+'-й песни: ', end = '')
    song = input()
    for j in violator_songs.keys():
       if song == j:
            time += violator_songs[j]

print('Общее время звучания песен: ', round(time, 2), ' минуты')




































