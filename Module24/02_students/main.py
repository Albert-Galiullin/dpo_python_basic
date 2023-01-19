class Student:
    def __init__(self, full_name, n_group, grade):
        self.full_name = full_name
        self.n_group = n_group
        self.grade = grade

    def average_grade(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        result = f'{self.full_name} {self.n_group} {self.grade} {self.average_grade()}'
        return result

students = []
students.append(Student('Петров Василий', 1, [4, 5, 5, 3, 4]))
students.append(Student('Сергеев Алексей', 2, [3, 5, 4, 3, 4]))
students.append(Student('Иванов Сергей', 4, [2, 4, 5, 3, 4]))
students.append(Student('Костина Ольга', 1, [3, 5, 4, 3, 4]))
students.append(Student('Яскевич Алексей', 3, [4, 4, 4, 3, 4]))
students.append(Student('Кузьменко Сергей', 1, [4, 5, 5, 3, 5]))
students.append(Student('Галиуллин Альберт', 1, [4, 5, 5, 4, 4]))
students.append(Student('Семенов Александр', 2, [4, 5, 4, 5, 4]))
students.append(Student('Лаврова Лариса', 4, [4, 5, 5, 5, 4]))
students.append(Student('Пьянкова Татьяна', 3, [5, 5, 5, 5, 5]))

students2 = sorted(students, key=lambda student: student.average_grade())
print(*students2, sep='\n')


