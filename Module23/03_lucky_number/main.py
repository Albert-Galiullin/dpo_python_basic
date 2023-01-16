import random

with open('out_file.txt', 'w', encoding='utf-8') as file1:
    sum_num = 0
    try:
        while sum_num <= 777:
            a = int(input('Введите число: '))
            if 13 == random.randint(1, 13):
                raise Exception('Вас постигла неудача!')
                break
            sum_num += a
            file1.write(str(a) + '\n')
    except Exception:
            print('Вас постигла неудача!')

file1 = open('out_file.txt', 'r', encoding='utf-8')
if sum_num > 777:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
print('Содержимое файла out_file.txt:')
for line in file1:
    print(line, end = '')

