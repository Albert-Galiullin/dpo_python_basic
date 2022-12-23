quantity = int(input('Введите количество клеток: '))
numbers = []
j = 1

for i in range(quantity):
    print('Эффективность ', j, ' клетки: ', end = '' )
    number = int(input())
    if j > number:
        numbers.append(number)
    j += 1
print('Неподходящие значения: ', end = ' ')

j = 0
for i in numbers:
    print(numbers[j], end = ' ')
    j += 1
