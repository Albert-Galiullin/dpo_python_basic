n = int(input('Кол-во чисел: '))
numbers = []
new_num = []
for i in range(n):
    num = int(input('Число: '))
    numbers.append(num)
print('Последовательность: ', numbers)

j = 0
for i in range(n):
    if numbers[n - i - 1] == numbers[n - i - 2]:
        j += 1


if j > 0 and n % 2 == 0:
   j += 1

if n % 2 == 0:
    for i in range(n):
        if n - i - 1 - j >= 0:
            new_num.append(numbers[n - i - 1 - j])
    if n - j < 0:
        app_num = 0
    else:
        app_num = n - j

    print('Нужно приписать чисел: ', app_num)


else:
    for i in range(n - 1):
        if n - i - 2 - j >= 0:
            new_num.append(numbers[n - i - 2 - j])
    if n - 1 - j < 0:
        app_num = 0
    else:
        app_num = n - 1 - j

    print('Нужно приписать чисел: ', app_num)

print(new_num)