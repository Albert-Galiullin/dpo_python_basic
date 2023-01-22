class Person:
    __count = 0

    def __init__(self, surname, name, age):
        self.__surname = surname
        self.__name = name
        self.__age = age
        # self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return "Фамилия: {surname} Имя: {name}\tВозраст: {age}".format(surname = self.__surname, name = self.__name, age = self.__age)

    def check_info(self):
        pass

    def get_count(self):
        return self__count

    def get_age(self):
        return self.__age

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    # def set_age(self, age):
    #     if age in range(18,90):
    #         self.__age = age
    #     else:
    #         raise Exception("Недопустимый возраст")


class Employee(Person):
    def __init__(self, surname, name, age, salary = 0):
        super().__init__(surname, name, age)

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                "Компания {}\t Зарплата: {}".format(self.company, self.salary)
            )
        )
        return info


class Manager(Employee):
    def __init__(self, surname, name, age, company, salary = 13000):
        super().__init__(surname, name, age)
        self.salary = salary
        self.company = company

    def __str__(self):
        info = super().__str__()
        return info

class Agent(Employee):
    def __init__(self, surname, name, age, company, sales_vol, salary = 0):
        super().__init__(surname, name, age)
        self.sales_vol = sales_vol
        self.company = company
        self.salary = 5000 + self.sales_vol * 5 /100

    def __str__(self):
        info = super().__str__()
        return info

class Worker(Employee):
    def __init__(self, surname, name, age, company, work_hours, salary = 0):
        super().__init__(surname, name, age, salary)
        self.company = company
        self.work_hours = work_hours
        self.salary = 100 * self.work_hours

    def __str__(self):
        info = super().__str__()
        return info



# my_agent = Agent(surname = 'Brass', name='Bob', age = 25, company = 'Google', sales_vol = 200)
# print(my_agent)
#
# my_man = Manager(surname = 'Bru', name='Alex', age = 28, company = 'Google')
# print(my_man)
#
# my_worker = Worker(surname = 'Bru', name='Alex', age = 28, company = 'Google', work_hours = 200)
# print(my_worker)

a_list = [('manager', 'Petrov', 'Alexey', '25', 'UMS'),
          ('manager', 'Ivanov', 'Alexey', '27', 'UMS'),
          ('manager', 'Stepanov', 'Sergey', '27', 'UMS'),
          ('agent', 'Stepnov', 'Petr','27', 'UMS', 20000),
          ('agent', 'Savelev', 'Sergey','23', 'UMS', 40000),
          ('agent', 'Petrova', 'Olga','24', 'UMS', 30000),
          ('worker', 'Stupin', 'Petr','27', 'UMS', 200),
          ('worker', 'Vovkin', 'Sergey','23', 'UMS', 190),
          ('worker', 'Petrov', 'Sergey','24', 'UMS', 180)]

for i in a_list:

    if [i][0][0] == 'manager':
        a = Manager(i[1], i[2], i[3], i[4])
        print(a)
    elif [i][0][0] == 'agent':
        a = Agent(i[1], i[2], i[3], i[4], i[5])
        print(a)
    elif [i][0][0] == 'worker':
        a = Worker(i[1], i[2], i[3], i[4], i[5])
        print(a)
