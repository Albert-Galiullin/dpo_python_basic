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
        print(gr)
        return


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
cons(nice_list)


