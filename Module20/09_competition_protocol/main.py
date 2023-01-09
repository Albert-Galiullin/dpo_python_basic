# 1 - я запись: 69485 Jack
# 2 - я запись: 95715 qwerty
# 3 - я запись: 95715 Alex
# 4 - я запись: 83647 M
# 5 - я запись: 197128 qwerty
# 6 - я запись: 95715 Jack
# 7 - я запись: 93289 Alex
# 8 - я запись: 95715 Alex
# 9 - я запись: 95715 M
# Итоги соревнований:
# 1 - е место.qwerty(197128)
# 2 - е место.Alex(95715)
# 3 - е место.Jack(95715)

def maxi(lst):
    j = '0'
    for i, l in lst.items():
        if int(l) > int(j):
            j = l
            k = i
    jk = (k +'(' + j + ')')
    # print(j, k)
    # print(protocol)
    protocol.pop(k)
    return jk



records = int(input('Сколько записей вносится в протокол? '))
protocol = {}
for i in range(1, records + 1):
    print(str(i) + '-я запись: ', end='')
    couple = input().split()
    if couple[1] not in protocol.keys():
        protocol[couple[1]] = couple[0]
    elif couple[1] in protocol.keys() and int(couple[0]) > int(protocol[couple[1]]):
        protocol.pop(couple[1])
        protocol[couple[1]] = couple[0]
print(protocol)

# protocol = {'Alex': '95715',
#             'qwerty': '197128',
#             'Jack': '95715',
#             'M': '95715'}

print('1 - е место.', maxi(protocol))
print('2 - е место.', maxi(protocol))
print('3 - е место.', maxi(protocol))