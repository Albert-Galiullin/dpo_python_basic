class1 = list(range(160, 176 + 1, 2))
class2 = list(range(162, 180 + 1, 3))
class1.extend(class2)
class1.sort()
print('Отсортированный список учеников: ', class1)
