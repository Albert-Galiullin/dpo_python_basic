def list_sort(lst):
    for current_element in range(len(lst) - 1):
        for i in range(len(lst) - 1 - current_element):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def main():
    task = [20, 10, -3, 1000, 10]
    print('Изначальный список:', task)
    list_sort(task)
    print('Отсортированный список:', task)


if __name__ == '__main__':
    main()
