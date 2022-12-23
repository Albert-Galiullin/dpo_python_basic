kontey = []

N = int(input('Количество контейнеров:  '))
for _ in range(N):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Введен неверный вес')
        weight = int(input('Введите вес контейнера: '))
    kontey.append(weight)

new_weight = int(input('Введите вес нового контейнера: '))

j = 1
for i in kontey:
    if i < new_weight :
        num = j
        break
    j += 1

print('Номер, который получит новый контейнер: ', num)
