import zipfile
from operator import itemgetter

import os

def a_letter(fil):

    dic_let = dict()
    j = ''
    for line in fil:
        j += line

    for i in j:
        if i in dic_let:
            dic_let[i] += 1
        elif i.isalpha():
            dic_let[i] = 1


    dic_let2 = dict(sorted(dic_let.items(), key=itemgetter(1),  reverse = True))

    print(dic_let2)

    return

archive = 'voyna-i-mir.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall()

file_from = open("voyna-i-mir.txt", "r", encoding="utf8")

a_letter(file_from)