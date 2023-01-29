import math



class Square:
    """Класс Квадрат"""
    def __init__(self, le: int) -> int:
        self.figure_name = "Квадрат"
        self.le = le

    @property
    def square(self) -> float:
        return self.le ** 2

    @property
    def perimeter(self) -> float:
        return 4 * self.le


class Triangle:
    """Класс Треугольник"""
    def __init__(self, le: int, h: int) ->int:
        self.figure_name = "Треугольник"
        self.le = le
        self.h = h

    @property
    def square(self) -> float:
        return 0.5 * self.le * self.h

    @property
    def perimeter(self) -> float:
        return 2 * math.sqrt(self.h ** 2 + (self.le / 2) ** 2) + self.le


class Cube(Square):
    """ Класс Куб"""
    def __init__(self, le: int) ->int:
        super().__init__(le)
        self.figure_name = 'Куб'

    @property
    def square(self) -> float:
        return 6 * super().square

    @property
    def perimeter(self) ->int:
        return 3 * super().perimeter


class Pyramid(Triangle, Square):
    """ Класс Пирамида"""
    def __init__(self, le: int, h: int) -> int:
        super().__init__(le, h)
        self.figure_name = 'Пирамида'

    @property
    def square(self) -> int:
        side_square = 4 * super().square
        base_square = self.le ** 2
        return side_square + base_square

    @property
    def perimeter(self) -> int:
        return 2 * super().perimeter + 2 * self.le


m = Square(2)
print(m.square)
print(m.perimeter)

p = Pyramid(6, 4)
print(p.square)
print(p.perimeter)

p = Cube(5)
print(p.square)
print(p.perimeter)
