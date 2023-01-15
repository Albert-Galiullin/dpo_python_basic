def a_str(fil):
    i = 0
    for line in fil:
        i = i + 1
    return(i)

def a_word(fil):
    fil.seek(0)
    j = ''
    for line in fil:
        j += line
    j = j.replace('.',' ')
    j = j.replace(',',' ')
    j = j.replace('!',' ')
    j = j.replace('-','')
    j = j.split()

    a_count = 0
    for i in j:
        a_count += 1
    return a_count

def a_letter(fil):
    fil.seek(0)
    dic_let = dict()
    j = ''
    for line in fil:
        j += line.lower()

    for i in j:
        if i in dic_let and i.islower() :
            dic_let[i] += 1
        elif i.islower():
            dic_let[i] = 1
    sum_let = sum(dic_let.values())

    k = 50
    for i, j in dic_let.items():
        if j < k:
            k = j
            min_let = i
    return sum_let, min_let


file_from = open("zen.txt", "r", encoding="utf8")

print('Количество строк равно : ', a_str(file_from))
print('Количество слов равно : ', a_word(file_from))
print('Количество букв и самая редквя буква: ', a_letter(file_from))







