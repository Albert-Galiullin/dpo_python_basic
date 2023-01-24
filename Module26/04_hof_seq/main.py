


# Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))
# Q(3) = Q(3-Q(3-1)+Q(3-Q(3-2))) = Q(3-2) + Q(3 -1) = Q(1) + Q(2) =  1 + 1 = 2
# Q(4) = Q(4-Q(4-1)+Q(4-Q(4-2))) = Q(4-2) + Q(4 -1) = Q(2) + Q(3) = 1 + 2 = 3
# Q(5) = Q(5-Q(5-1)+Q(5-Q(5-2))) = Q(5-3) + Q(5 -2) = Q(2) + Q(3)= 1 + 2 = 3

def QHofstadter(result):
    try:
        if result == [1, 1]:
            for i in range(2, 50):
                value = result[i - result[i - 1]] + result[i - result[i - 2]]
                result.append(value)
                yield value
            return list
        else:
            raise StopIteration
    except StopIteration:
        print("Неверный ввод")

hof_seq = QHofstadter([1, 1])

for i_value in hof_seq:
    print(i_value, end = ' ')

print("\n")
hof_seq = QHofstadter([1, 2])

for i_value in hof_seq:
    print(i_value, end = ' ')
