# Введите максимальное число: 10
# Нужное число есть среди вот этих чисел: 1 2 3 4 5
# Ответ Артёма: Да
#
# Нужное число  есть среди  вот этих чисел: 2 4 6 8 10
# Ответ Артёма: Нет
#
# Нужное число есть среди вот этих чисел: Помогите!
#
# Артём мог загадать следующие числа: 1 3 5


number = int(input('Введите максимальное число: '))
plenty = set()
for i in range(1, number +1):
    plenty.add(i)
plenty_copy = plenty.copy()
print(plenty)


while True:
    nums = input('Нужное число есть среди вот этих чисел? ').lower()

    if nums == 'помогите!':
        break
    else:
        nums = nums.split()

    answ = input('Ответ Артёма(да/нет): ').lower()
    plenty = plenty_copy.copy()
    if answ == 'да':
        for i in plenty:
            if str(i) not in nums:
                plenty_copy.discard(int(i))
                # print(plenty)
    elif answ == 'нет':
        for i in nums:
            if int(i) in plenty:
                plenty_copy.discard(int(i))
                # print(plenty)


print('Артём мог загадать следующие числа: ', end='')
for i in plenty_copy:
    print(i, end=' ')














