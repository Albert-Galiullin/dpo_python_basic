# решение с помощью рекурсии
def lst(st, n):
    if st == n:
        return
    else:
        print(st + 1)
        st += 1
        return lst(st, n)


int_num = int(input('Введите целое число: '))
start = 0
a = lst(start, int_num)
