# Пример 1:
# Введите IP: 128.16.35.a4
# a4 — это не целое число.
#
# Пример 2:
# Введите IP: 240.127.56.340
# 340 превышает 255.
#
# Пример 3:
# Введите IP: 34.56.42, 5
# Адрес — это четыре числа, разделённые точками.
#
# Пример 4:
# Введите IP: 128.0.0.255
# IP - адрес корректен.


ip_address = input('Введите IP: ').split('.')

i = 0
pr = True
while i < 4:
    if not ip_address[i].isdigit():
       print(ip_address[i], '— это не целое число')
       pr = False
       break


    elif int(ip_address[i]) > 255:
       print(ip_address[i], 'превышает 255.')
       pr = False
       break


    elif len(ip_address) < 4:
       print('Адрес — это четыре числа, разделённые точками.')
       pr = False
       break

    i += 1

if pr:
    print('IP - адрес корректен.')




