def opposit(number):
    i = ''
    j = ''

    number1 = int(number)
    while number1 != 0:
        digit = number1 % 10
        i += str(digit)
        number1 //= 10

    number2 = str(number)
    l = 0
    for k in number2:
      l += 1
      if k == '.':
        l = 0

    number2 = round((number - int(number)) * 10 ** l)

    while number2 != 0:
        digit = number2 % 10
        j += str(digit)
        number2 //= 10

    opp_num = i + '.' + j

    return opp_num




print()
num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))

print()
opp1 = opposit(num_1)
print('Первое число наоборот: ', opp1)
opp2 = opposit(num_2)
print('Второе число наоборот: ', opp2)

print()
summ = float(opp1) + float(opp2)
print('Сумма: ', summ)


