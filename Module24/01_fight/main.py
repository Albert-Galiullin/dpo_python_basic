import random
class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def hit(self, target):
            target.health -= 20
    def result_print(self):
        print(attacker.name, 'атаковал', victim.name)
        print('У', victim.name, 'осталось здоровья', victim.health, '\n')

warriors = [Warrior('Воин1'), Warrior('Воин2')]
while True:
    i = random.randint(0, 1)
    attacker, victim = warriors[i], warriors[i - 1]
    attacker.hit(victim)
    attacker.result_print()
    if victim.health <= 0:
      print(attacker.name, 'победил!!!')
      break
