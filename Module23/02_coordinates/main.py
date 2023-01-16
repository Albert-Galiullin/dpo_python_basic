import random

def fun1(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def fun2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x

try:
    file = open('coordinates.txt', 'r', encoding ='utf-8')
    file_2 = open('result.txt', 'w', encoding ='utf-8')
    for line in file:
        nums_list = line.split()
        res1 = fun1(int(nums_list[0]), int(nums_list[1]))
        res2 = fun2(int(nums_list[0]), int(nums_list[1]))
        number = random.randint(0, 100)
        my_list = sorted([str(res1), str(res2), str(number)])
        file_2.write(' '.join(my_list) + '\n')
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ZeroDivisionError as exc:
    print(type(exc), "— деление на 0")
except ValueError as exc:
    print(type(exc), "— невозможно преобразовать к числу")
except TypeError as exc:
    print(type(exc), "ошибка в типе данных")
finally:
    file.close()
    file_2.close()
    print(file.closed)
    print(file_2.closed)

