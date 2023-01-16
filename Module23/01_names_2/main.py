with open('people.txt', 'r', encoding='utf-8') as file_in,\
        open('errors.log', 'w', encoding='utf-8') as log_file:
    count = 0
    i = 1
    for line in file_in:
        try:
            i_line = line.rstrip()
            if i_line.isalpha() and len(i_line) > 2:
                count += len(i_line)
            else:
                count += len(i_line)
                raise Exception (f"Ошибка: В строке {i} меньше 3 букв!")
            i += 1
        except Exception as exc:
            print(f'Ошибка: в строке {i} введено имя меньше 3 букв')
            log_file.write(str(exc))
    print('Общее количество символов: ', count)
