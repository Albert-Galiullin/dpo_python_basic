file_from = open("zen.txt", "r", encoding="utf8")
a_comtr = []
for line in file_from:
    a_comtr.append(line.rstrip('\n'))
file_from.close()


file_in = open("contr_zen.txt", "w", encoding="utf8")
for i in range(len(a_comtr)-1, -1, -1):
    file_in.write(a_comtr[i]+'\n')
file_in.close()