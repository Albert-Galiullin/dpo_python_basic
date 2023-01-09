# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
# Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)

def slicer(a_tuple, b):
    new_tuple = []
    flag = True
    i = 0

    while i < len(a_tuple):
        if a_tuple[i] != b and flag:
            i += 1
        elif a_tuple[i] == b and flag:
            new_tuple.append(a_tuple[i])
            flag = False
            i += 1
        elif a_tuple[i] == b and flag:
            new_tuple.append(a_tuple[i])
            flag = False
            i += 1
        elif a_tuple[i] != b and flag == False:
            new_tuple.append(a_tuple[i])
            i += 1
        elif a_tuple[i] == b and flag == False:
            new_tuple.append(a_tuple[i])
            break



    return tuple(new_tuple)

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

