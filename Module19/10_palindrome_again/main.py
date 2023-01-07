word = input('Введите строку: ').lower()
sym = set()

for i in word:
    if i in sym:
        sym.remove(i)
    else:
        sym.add(i)

if len(sym) > 1:
    print('Нельзя сделать полиндром')
else:
    print('Можно сделать полиндром')

