import random
class Gardener:
    works = {0: 'окучивает', 1: 'поливает'}
    result_pot = []



    def __init__(self, name):
        self.name = name

    def print_work(self):
        print('{} {} и {}'.format(
            gardener.name, Gardener.works[0], Gardener.works[1]))

    def result(self):
        result_pot = [random.randint(7, 10) for quantity_pot in range(1, quantity_pot + 1)]
        for i in range(1, quantity_pot + 1):
            print('C {} картошки собрано {} клубней'.format(i, result_pot[i - 1]))
        print('Картошка выкопана.Хороший урожай у Садовника!!')

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}


    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()


    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]


    def grow_all(self):
        print('Картошка прорастает!')
        Gardener.print_work('')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False  # такой return поможет получить информацию о зрелости картошки снаружи этого объекта
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


gardener = Gardener('Садовник')
quantity_pot = 5
garden = PotatoGarden(quantity_pot)



for _ in range(3):
    garden.grow_all()


garden.are_all_ripe()
gardener.result()
