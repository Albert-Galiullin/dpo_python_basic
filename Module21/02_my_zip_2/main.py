def my_zip2(*agrs):
    # print(agrs)
    min_len = min(map(len, agrs))
    iterators = []
    for iterable in agrs:
        iterators.append(iter(iterable))
    return [tuple(map(next, iterators))
            for _ in range(min_len)]

# def my_zip2(a1, b1, a_min, a_max, lst = []):
#     if a_min == a_max:
#         return lst
#     else:
#         # print(a1[a_min], b1[a_min])
#         lst.append((a1[a_min], b1[a_min]))
#         a_min += 1
#         return my_zip2(a1, b1, a_min, a_max)


text = 'abcde'
a_tuple = (10, 20, 30, 40, 50)
b_tuple = (100, 200, 300, 400)

pair = my_zip2(text, a_tuple, b_tuple)
print(pair)



