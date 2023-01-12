# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
# Результат:
# < generator object < genexpr > at 0x00000204A4234048 >
#
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)

def my_zip(a1, b1):
    a_dict = []
    l_c = min(len(a1), len(b1))
      
    
    for i in range(l_c):
        a_dict[a1[i]] = b1[i]
    return a_dict


text = 'abcd'
a_tuple = (10, 20, 30, 40)
pair = zip(text, a_tuple)
print(pair)
for i in pair:
    print(i)

print('Вывод того же самого с помощью своей функции')
print(my_zip(text, a_tuple))

