import os.path

def cipher(file_from, file_in):
    alphabit_low = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    alphabit_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')

    i = 1
    for line in file_from:
        step = i % 26
        sh_word = []
        for char in range(len(line)):
            if line[char] in alphabit_low:
                sh = alphabit_low.index(line[char]) + step
                sh_word.append(alphabit_low[sh])
            elif line[char] in alphabit_up:
                sh = alphabit_up.index(line[char]) + step
                sh_word.append(alphabit_up[sh])
            else:
                sh_word.append(line[char])
            i_text = ''.join(sh_word)
        print(i_text)
        file_in.write(i_text)
        i += 1
    return


file_from = open("text.txt", "r", encoding="utf8")
file_in = open("cipher_text.txt", "w", encoding="utf8")

a = cipher(file_from, file_in)
file_from.close()
file_in.close()


