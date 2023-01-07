text = input('Введите текст: ')
sym_dict = dict()

for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

print('Оригинальный словарь частот:')
for i in sorted(sym_dict.keys()):
    print(i, ':', sym_dict[i])

new_dict = {}
sp = ''
maxi = max(sym_dict.values())
for i in range(1, maxi + 1):
    for sym, qu in sym_dict.items():
         if qu == i:
            sp += sym
            new_dict[qu] = list(sp)

    sp = ''
print('Инвертированный словарь частот:')
for i in sorted(new_dict.keys()):
    print(i, ':', new_dict[i])