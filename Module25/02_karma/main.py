import random

class Simulator_life:

    __point_carma = 0
    count_day = 0
    dict_raise = {1: 'KillError',
                 2: 'DrunkError',
                 3: 'CarCrashError',
                 4: 'GluttonyError',
                 5: 'DepressionError'
                 }

    def one_day(self):

        chance = random.randint(1, 10)
        if chance != 1:
            point = random.randint(1, 7)
            Simulator_life.__point_carma += point
            Simulator_life.count_day += 1
            print(f'День {Simulator_life.count_day}. Выпало {point} очков.Общий итог - {Simulator_life.__point_carma}')

        else:
            i_raise = random.randint(1, 5)
            Simulator_life.count_day += 1
            text = f'День {Simulator_life.count_day}.Raise {Simulator_life.dict_raise[i_raise]}'
            print(text)
            log_file.write(text + '\n')

    def get_count(self):
        return Simulator_life.__point_carma



person = Simulator_life()
with open('karma.log', 'w', encoding='utf8') as log_file:
    while person.get_count() < 500:
        person.one_day()



