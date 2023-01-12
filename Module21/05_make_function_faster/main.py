def calculating_math_func(data, fact_dict = {}):
    result = 1
    if data not in fact_dict:
        for index in range(1, data + 1):
            result *= index
            fact_dict[data] = result
    else:
        result = fact_dict[data]
        print('Значение факториала в словаре есть. Берем готовое')

    result /= data ** 3
    result = result ** 10
    return result


while True:
    number = int(input('Введите число: '))
    print(calculating_math_func(number))




