def app_def(i_line):
    a1 = 'НЕ присутствуют все три поля'
    a2 = 'Поле имени содержит НЕ только буквы'
    a3 = 'Поле «Имейл» НЕ содержит @ и.(точку)'
    a4 = 'Поле «Возраст» НЕ является числом от 10 до 99'

    try:
        if len(i_line) < 3:
            log_file2.write(' '.join(i_line) + ' ' + a1 + '\n')
            raise IndexError(a1)
        elif not i_line[0].isalpha():
            log_file2.write(' '.join(i_line) + ' ' + a2 + '\n')
            raise NameError(a2)
        elif '@' not in i_line[1] and '.' not in i_line[1]:
            log_file2.write(' '.join(i_line) + ' ' + a3 + '\n')
            raise SyntaxError(a3)
        elif int(i_line[2]) < 10 or int(i_line[2]) > 99:
            log_file2.write(' '.join(i_line) + ' ' + a4 + '\n')
            raise ValueError(a4)
        else:
            log_file1.write(' '.join(i_line)  + '\n')
    except IndexError:
        print('Ошибка. Смотри log файл')
    except NameError:
        print('Ошибка. Смотри log файл')
    except SyntaxError:
        print('Ошибка. Смотри log файл')
    except ValueError:
        print('Ошибка. Смотри log файл')


file_in = open('registrations.txt', 'r', encoding='utf-8')
log_file1 = open('registrations_good.log', 'w', encoding='utf-8')
log_file2 = open('registrations_bad.log', 'w', encoding='utf-8')

for line in file_in:
    i_line = line.split()
    app_def(i_line)

file_in.close()
log_file1.close()
log_file2.close()