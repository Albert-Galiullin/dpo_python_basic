def conc(pl):
    players1 = []
    players2 = []
    for i, j in players.items():
        players1.extend(i)
        players1.extend(j)
        players2.append(tuple(players1))
        players1 = []
    return players2

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print(conc(players))
