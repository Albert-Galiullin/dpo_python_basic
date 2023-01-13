def cons(gr, new_list=None):
    new_list = new_list or []
    for i in gr:
        if isinstance(i, list):
            for j in i:
                new_list.append(j)
                flag = False
        else:
            new_list.append(i)
    # print(new_list)
    flag = True


    for i in new_list:
        if isinstance(i, list):
            flag = False

    if flag == False:
        gr = new_list
        cons(gr)
    else:
        gr = new_list
        print(sum(gr))
        return


groups = [[1, 2, [3, 4, [1, 1]]], [1], 3]
cons(groups)
