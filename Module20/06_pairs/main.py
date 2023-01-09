# Вариант 1

import random
numbers = [random.randint(0, 100) for _ in range(10)]
numbers1 = []
numbers2 = []
i = 0

while i < len(numbers):
    numbers1.append(numbers[i])
    numbers1.append(numbers[i + 1])
    numbers2.append(tuple(numbers1))
    numbers1 = []
    i += 2

print('Решение по 1 варианту с помощью WHILE')
print(f'Оригинальный список: {numbers}')
print('Новый список: ', numbers2)

# Вариант 2
numbers3 = []
numbers4 = []

for index_i, i in enumerate(numbers):
    if index_i % 2 == 0:
        numbers3.append(i)
    else:
        numbers3.append(i)
        numbers4.append(tuple(numbers3))
        numbers3 = []


print()
print('Решение по второму варианту с помощью цикла FOR')
print(f'Оригинальный список: {numbers}')
print('Новый список по второму варианту: ', numbers4)





# result = [(i_key, i_key + 1) for i_key in original_list if i_key % 2 == 0]


