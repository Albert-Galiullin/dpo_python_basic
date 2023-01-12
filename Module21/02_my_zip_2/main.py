def my_zip2(a1, b1, a_min, a_max, lst = []):
    if a_min == a_max:
        return lst
    else:
        # print(a1[a_min], b1[a_min])
        lst.append((a1[a_min], b1[a_min]))
        a_min += 1
        return my_zip2(a1, b1, a_min, a_max)


text = 'abcd'
a_tuple = (10, 20, 30, 40, 50)
a_min = 0
a_max = min(len(text), len(a_tuple))

pair = my_zip2(text, a_tuple, a_min, a_max)
print(pair)


