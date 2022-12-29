spisok1 = [x for x in range(1, 13) if x % 4 == 1]
print(spisok1)
spisok2 = [x for x in range(1, 13) if x % 4 == 2]
print(spisok2)
spisok3 = [x for x in range(1, 13) if x % 4 == 3]
print(spisok3)
spisok4 = [x for x in range(1, 13) if x % 4 == 0]
print(spisok4)
spisok = []
spisok.append(spisok1)
spisok.append(spisok2)
spisok.append(spisok3)
spisok.append(spisok4)
print(spisok)