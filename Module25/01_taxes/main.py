class Property:

    __count_task = 0
    task_rate = 0

    def __init__(self, worth, funds):
        self.worth = worth
        self.funds = funds

    def get_count(self):
        return self.__count_task

    def task(self):
        self.sum_task = round(self.worth * self.task_rate)
        print('Сумма налога составляет: ', self.sum_task)
        Property.__count_task += self.sum_task

    def lack_funds(self):
        if self.funds >= Property.__count_task:
            print('Денежных средств на оплату налогов хватает')
        else:
            print('Денежных средств на оплату налогов не хватает')


class Apartment(Property):
    task_rate = 1/500

class Car(Property):
    task_rate = 1 / 200

class CountryHouse(Property):
    task_rate = 1 / 1000


a_worth = int(input('Введите стоимость квартиры (0 в случае отсутствия): '))
b_worth = int(input('Введите стоимость дачи (0 в случае отсутствия): '))
c_worth = int(input('Введите стоимость автомобиля (0 в случае отсутствия): '))
own_funds = int(input('Введите сумму собственнных средств: '))

a = CountryHouse(a_worth, own_funds)
b = Apartment(b_worth, own_funds)
c = Car(c_worth, own_funds)
a.task()
b.task()
c.task()
a.lack_funds()

