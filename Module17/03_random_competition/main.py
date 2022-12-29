import random
team1 = [round(random.uniform(5, 10),2) for _ in range(20)]
print('Первая команда:', team1)
team2 = [round(random.uniform(5, 10),2) for _ in range(20)]
print('Вторая команда:', team2)
win = [(team1[x] if team1[x] >= team2[x] else team2[x]) for x in range(20)]
print('Победители тура:', win)