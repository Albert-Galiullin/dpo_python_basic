from abc import ABC


class Figure():
    """
    Абстрактный базовый класс фигура

    Args and attrs:
        length (int): длина фигуры
        width (int): ширина(высота) фигуры
    """
    def __init__(self,length: int, width: int) -> None:
        self.length = length
        self.width = width

class ResizableMixin:

    def square(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class SurfaceAreaMixin:
    """Клас-миксин для нахождения площади поверхности 3D фигуры"""

    def __init__(self):
        self.surface = None

    def surface_area(self) -> int:
        surface_area = 0
        for surface in self.surfaces:
            # print(surface_area(self))
            surface_area += surface.area(self)

        return surface_area


class Rectangle(Figure, ResizableMixin):
    """Прямоугольник. Родительский класс: Figure"""

class Square(Figure, ResizableMixin):
    """Квадрат. Родительский класс: Figure"""
    def __init__(self,length: int, height=None) -> None:
        super().__init__(length, length)



class  Triangle(Figure, ResizableMixin):
    """Треугольник. Родительский класс: Figure"""
    def __init__(self, length: int, height: int) -> None:
        super().__init__(length, height * 0.5)

class Cube(Square, SurfaceAreaMixin):
    """ Класс Куб"""
    def __init__(self, length: int):
        super().__init__(length=length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

class Piramid(Square, Triangle, SurfaceAreaMixin):
    """ Класс Пирамида"""
    def __init__(self, length: int, height: int) -> None:
        super().__init__(length=length, height=height)
        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]


rect_1 = Rectangle(length=5, width=6)
rect_2 = Square(length=7)
rect_3 = Triangle(length=5, height=6)
rect_4 = Cube(length=7)
# rect_5 = Piramid(length=5, height=6)
print(rect_1.area())
print(rect_2.area())
print(rect_3.area())
print(rect_4.surface_area())
# print(rect_5.surface_area())
