import random
n = int(input('Количество чисел в списке: '))
numbers = [random.randint(0, 2) for _ in range(n)]
print(numbers)
null = numbers.count(0)
i = 0
while i < len(numbers):
    if numbers[i] == 0:
        numbers.remove(0)
        i -= 1
    i += 1
print(numbers[::-1])