from operator import itemgetter
def a_letter(fil):
    fil.seek(0)
    dic_let = dict()
    j = ''
    for line in fil:
        j += line.lower()

    for i in j:
        if i in dic_let:
            dic_let[i] += 1
        elif i.isalpha():
            dic_let[i] = 1
    sum_let = sum(dic_let.values())
    dic_let2 = dict(sorted(dic_let.items(), key=itemgetter(1),  reverse = True))
    print(dic_let2)
    for i, j in dic_let2.items():
        file_in.write(i + ' ' + str(round(j/sum_let, 3)
) + '\n')

    return

file_from = open("text.txt", "r", encoding="utf8")
file_in = open("analysis.txt", "w", encoding="utf8")

a_letter(file_from)
