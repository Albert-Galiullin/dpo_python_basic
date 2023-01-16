file_in = open('calc.txt', 'r', encoding='utf-8')
sum = 0
for i_line in file_in:
    line = i_line.split()
    if len(line[1]) == 1 and line[1] in '+-/*':
        sum += eval(i_line)
    else:
        print('Обнаружена ошибка в строке: ', line)
        a = input('Хотите исправить? да/нет ').lower()
        if a == 'да':
            b = input('Введите исправленную строку: ')
            line = b.split()
            if len(line[1]) == 1 and line[1] in '+-/*':
                sum += eval(b)


print("Сумма результатов: ", sum)
file_in.close()



