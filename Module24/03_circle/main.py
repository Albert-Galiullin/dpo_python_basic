import math
class Сircle:

    def __init__(self, x=0, y=0, r=1, k = 1):
        self.x = x
        self.y = y
        self.r = r
        self.k = k
    def check_info(self):
        print('Площадь круга = ', math.pi * self.r ** 2 * self.k)
        print('Периметр круга = ', math.pi * self.r * 2 * self.k)


print('Введите координаты первого круга')
x1 = int(input('X = '))
y1 = int(input('Y = '))
r1 = int(input('Введите радиус круга: '))
# k1 = int(input('Введите коэффициент увеличения круга: '))

a = Сircle(x1, y1, r1)
a.check_info()

print('\nВведите координаты второго круга')
x2 = int(input('X = '))
y2 = int(input('Y = '))
r2 = int(input('Введите радиус круга: '))
# k2 = int(input('Введите коэффициент увеличения круга: '))

a = Сircle(x2, y2, r2)
a.check_info()

c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # Определяем длину гипотенузы между центрами окружностей
if r1 + r2 > c:
    print('Окружности пересекаются')
else:
    print('Окружности не пересекаются')
