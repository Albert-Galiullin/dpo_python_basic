students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def hobby(listing):
    lst = []
    string_sur = 0
    for i in listing:
        lst += listing[i]['interests']
        string_sur += len(listing[i]['surname'])

    return lst, string_sur


pairs = []
for i in students:
    pairs.append((i, students[i]['age']))
print('Список пар "ID студента — возраст": ', pairs)

print('Полный список интересов всех студентов:', set(hobby(students)[0]))
print('Общая длина всех фамилий студентов: ', hobby(students)[1])