# Пример вызова функции:
# print(tpl_sort(6, 3, -1, 8, 4, 10, -5))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)

def tpl_sort(lst):
    flag = False
    for i in lst:
        if isinstance(i, float):
            flag = True
    if flag == False:
        new_list = tuple(sorted(list(lst)))
    else:
        new_list = lst
    return new_list

s_tuple = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(s_tuple))
s_tuple = (6, 3, -1.4, 8, 4, 10.5, -5)
print(tpl_sort(s_tuple))