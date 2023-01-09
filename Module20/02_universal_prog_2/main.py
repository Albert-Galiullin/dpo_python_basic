#Вариант 1
def crypto(checking_list):
    return [v for i, v in enumerate(checking_list) if is_prime(i)]

# Вариант два с учетом словарей
def crypto2(checking_list):
    if isinstance(checking_list, dict):
        return [v for i, v in enumerate(checking_list.items()) if is_prime(i)]
    else:
        return [v for i, v in enumerate(checking_list) if is_prime(i)]



def is_prime(num):
    simple = False
    for i in range(2, num):
        if num % i == 0:
            simple = False
            break
        simple = True
    if num == 2:
        simple = True
    return simple

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(crypto('О Дивный Новый мир!'))
print(crypto2({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))

