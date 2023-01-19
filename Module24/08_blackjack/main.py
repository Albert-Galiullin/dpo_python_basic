import random
class PlayingCard:
    def __init__(self, cost_card, name_card):
        self.cost_card = cost_card
        self.name_card = name_card


class Player:
    def __init__(self, name, points = 0):
        self.name = name
        self.points = points

class Game:
    sum_points = 0

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2


    def game_process(self, card_1, card_2, su_1, su_2):
        if self.sum_points > 21:
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            print(self.player_1.points, card_1.name_card, su_1)
            print('Игра закончена')
            game.winner()
            exit()

        else:
            self.player_1.points += card_1.cost_card
            self.player_2.points += card_2.cost_card
            self.sum_points = (self.player_1.points + self.player_2.points)
            print(self.player_1.points, card_1.name_card, su_1)

    def winner(self):
        if self.player_1.points == self.player_2.points:
            print('Ничья')
        elif  self.player_1.points > 21 and self.player_2.points <= 21:
            print(f'Победил {self.player_2.name}')
        elif  self.player_1.points > 21 and self.player_2.points > 21:
            print(f'Победил {self.player_2.name}. Игрок сгорел')
        elif  self.player_2.points > 21 and self.player_1.points <= 21:
            print(f'Победил {self.player_1.name}')
        elif  self.player_2.points > self.player_1.points:
            print(f'Победил {self.player_2.name}')
        elif  self.player_1.points > self.player_2.points:
            print(f'Победил {self.player_1.name}')
        else:
            print('Победителей нет')
        print(f'У игрока {self.player_1.points} очков, у комьютера - {self.player_2.points}')


play_card_2 = PlayingCard(2, 'Двойка')
play_card_3 = PlayingCard(3, 'Тройка')
play_card_4 = PlayingCard(4, 'Четверка')
play_card_5 = PlayingCard(5, 'Пятерка')
play_card_6 = PlayingCard(6, 'Шестерка')
play_card_7 = PlayingCard(7, 'Семерка')
play_card_8 = PlayingCard(8, 'Восьмерка')
play_card_9 = PlayingCard(9, 'Девятка')
play_card_10 = PlayingCard(10, 'Десятка')
play_card_11 = PlayingCard(11, 'Туз')
play_card_12 = PlayingCard(10, 'Валет')
play_card_13 = PlayingCard(10, 'Дама')
play_card_14 = PlayingCard(10, 'Король')

deck = [play_card_2, play_card_3, play_card_4, play_card_5, play_card_6, play_card_7, play_card_8, play_card_9,
        play_card_10, play_card_11, play_card_12, play_card_13, play_card_14]

suit = ['пики', 'бубны', 'крести', ' черви']

player = Player('Игрок')
comp = Player('Компьютер')
game = Game(player, comp)

cards_was = []

while True:
    r_1 = random.randint(0, 12)
    m_1 = random.randint(0, 3)
    r_2 = random.randint(0, 12)
    m_2 = random.randint(0, 3)

    while True:
        s = str(r_1) + str(m_1)
        t = str(r_2) + str(m_2)
        if  s == t or s in cards_was or t in cards_was:
            r_2 = random.randint(0, 12)
            m_2 = random.randint(0, 3)
        else:
            cards_was.append(s)
            cards_was.append(t)
            break


    request = input('Введите "взять" чтобы продолжить или "стоп" чтобы остановиться: ')
    if request == "взять":
        game.game_process(deck[r_1], deck[r_2], suit[m_1], suit[m_2])
    elif request == 'стоп':
        break
game.winner()




