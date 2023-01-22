import random
import math

class Car:
    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)

    def __str__(self):
        return f'Координаты: X={round(self.x, 2)} Y={round(self.y, 2)}'


class Bus(Car):
    pay_coef = 0.02
    volume_pass = 60

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += Bus.pay_coef * self.passengers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.passengers > Bus.volume_pass:
            print('Достигнута максимальная вместимость автобуса.')
            left = Bus.volume_pass - (self.passengers + passengers)
            stayed = passengers - left
            print(f'Уехать смогли только {left} пассажиров, остались {stayed}.')
        else:
            self.passengers += passengers

    def exit(self, passengers):
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            self.passengers = 0
        else:
            self.passengers -= passengers

    def __str__(self):
        lines = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров.',
            f'У водителя {round(self.money, 2)} денег.',
        ]
        return '\n'.join(lines)


car = Car(0, 1, 80)
bus = Bus(1, 2, 50)



for passed_time in range(1, 10):
    print('\nКонтрольная точка для Car и Bas: ')

    car.move(random.randint(0, 360))
    print(car)

    flag = random.randint(1, 2)
    if flag == 1:
        if bus.passengers > 0:
            bus.exit(random.randint(1, 3))
    else:
        bus.enter(random.randint(1, 3))
    bus.move(random.randint(0, 360))
    print(bus)
