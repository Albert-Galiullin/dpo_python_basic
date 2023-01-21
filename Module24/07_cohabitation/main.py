from random import randint, choice
class House:
    food = 50
    money = 0


class Person:

    def __init__(self, name, apartment):
        self.name = name
        self.satiety = 50
        self.apartment = apartment

    def eat(self):  # ест
        self.satiety += 1
        apartment.food -= 1
        return f'ест, сытость {self.satiety} еда {apartment.food}'

    def work(self):  # работает
        self.satiety -= 1
        apartment.money += 1
        return f'работает, сытость {self.satiety} деньги {apartment.money}'

    def play(self):  # играет
        self.satiety -= 1
        return f'играет, сытость {self.satiety}'

    def repast(self):  # идет в магазин
        apartment.food += 1
        apartment.money -= 1
        return f'идет в магазин, еда {apartment.food} деньги {apartment.money}'



apartment = House()
person_1 = Person('Вася', apartment)
person_2 = Person('Федя',apartment)

for i in range(365):  # пробуем прожить год
    number_cubes = randint(1, 6)
    person = choice([person_1, person_2])  # рандомно выбираем персону
    if person.satiety < 0:  # голоден - умер. завершаем эксперимент
        print(f'К сожалению, {person.name} помер с голоду ')
        break
    if person.satiety < 20 and apartment.food >= 10:
        text = person.eat()
    elif apartment.food < 10:
        text = person.repast()
    elif apartment.money < 50:
        text = person.work()
    elif number_cubes == 1:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play()
    print(person.name, text)

print('выжили' if i == 364 else 'все плохо')
