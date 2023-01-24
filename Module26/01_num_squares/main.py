# Вариант 1.Итерация.

class SquareNumbers:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter ** 2

        else:
            raise StopIteration

my_square = SquareNumbers(limit = 10)
print('Решение мотодом итерации')
for num in my_square:
    print(num, end =' ')
print()


# Вариант 2.Генерация.

def square(number):

    for i in range(1, number + 1):
        b = i ** 2
        yield b

x_2 = square(number = 10)
print('Решение мотодом генерации')
for i_value in x_2:
    print(i_value, end = ' ')


# генераторное выражение
print()
print('Генераторное выражение')
square_gen = (num ** 2 for num in range(1, 11))
for i_num in square_gen:
    print(i_num, end =' ')
