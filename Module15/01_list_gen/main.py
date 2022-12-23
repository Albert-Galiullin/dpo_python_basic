num = int(input('Введите число: '))
numbers = []

for number in range(1, num + 1):
    if number % 2 != 0:
        numbers.append(number)
print('Список из нечётных чисел от одного до N: ', numbers)

