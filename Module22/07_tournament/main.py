import os.path
def key_sort(elem):
    return elem[2]

def tour(file_from, file_in):
    i = 1
    j = 0
    lst = []
    for line in file_from:
        if i == 1:
            ball = int(line)
        else:
            a = line.split()
            b = int(a[2])
            if b > ball:
                lst.append(a)
                j += 1
        i += 1
    lst.sort(key = key_sort, reverse = True)

    file_in.write(str(j) + '\n')
    for i in range(len(lst)):
        str_a = str(i + 1)+') ' + lst[i][1][0] + '. ' + lst[i][0] + ' ' + lst[i][2]
        file_in.write(str_a + '\n')

    return


file_from = open("first_tour.txt", "r", encoding="utf8")
file_in = open("second_tour.txt", "w", encoding="utf8")

a = tour(file_from, file_in)
file_from.close()
file_in.close()

