import math
class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return 'х = ' +str(self.x) + ' у = ' + str(self.y) + ' r = '+ str(self.r)

    def get_area(self):
        print('Площадь круга = ', round(self.r * self.r * math.pi,4))

    def get_perimeter(self):
        print('Периметр круга = ', round(2 * self.r * math.pi,4))

    def scale(self, k):
        self.r *= k
        print(f'Радиус после увеличения в {k} раз = ', self.r)
        return

    def is_intersect(self, other):
        if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2:
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')



print('Окружность 1')
c1 = Circle(0, 0, 1)
print(c1)
c1.get_area()
c1.get_perimeter()
c1.scale(2)
c1.get_area()
c1.get_perimeter()

print('\nОкружность 2')

c2 = Circle(3, 3, 3)
print(c2)
c2.get_area()
c2.get_perimeter()
c2.scale(2)
c2.get_area()
c2.get_perimeter()

print('\nПересечение:')
c1.is_intersect(c2)
