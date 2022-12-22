def geo(x, y, r):
  if x ** 2 + y ** 2 <= r ** 2:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')


print()
x = float(input('Введите число x: '))
y = float(input('Введите число y: '))
r = float(input('Введите радиус: '))
print()
geo(x, y, r)

