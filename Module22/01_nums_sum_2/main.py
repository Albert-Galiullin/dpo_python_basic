def sum_txt(a_file):
    numbers_sum = 0
    file_from = open(a_file, "r", encoding="utf8")
    for line in file_from:
        clear_line = line.rstrip()
        if clear_line:
            numbers_sum += int(clear_line)
    file_from.close()
    return numbers_sum

file_in = open("answer.txt", "w", encoding="utf8")
file_in.write(str(sum_txt("numbers.txt")))
file_in.close()
