def summ(n):
    print()
    j = 0
    while n != 0:
        i = n % 10
        j += i
        n //= 10
    print('Сумма цифр равна:', j)
    return j
    
def quan(n):
    print()
    j = 0
    while n != 0:
        j += 1
        n //= 10
    print('Количество цифр равно:', j)
    return j

print()
n = int(input('Введите число: '))
a = summ(n)
b = quan(n)
print()
print('Разность суммы и количества цифр:', a -b)
