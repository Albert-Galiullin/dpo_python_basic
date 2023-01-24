def value(to_find):
    for x in list_1:
        for y in list_2:
            result = x * y
            # print(x, y, result)
            if result == to_find:
                yield f'Искомые числа: {x} * {y} = {result}'
                # can_continue = False
                # break

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
# to_find = 56
# can_continue = True

x_y = value(to_find = 56)
for i_value in x_y:
    print(i_value, end = ' ')
