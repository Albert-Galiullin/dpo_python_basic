members = {
    ('Иванов', 'Петр') : 40,
    ('Иванова', 'Светлана') : 39,
    ('Иванова', 'Ирина') : 15,
    ('Иванов', 'Сергей') : 10,
    ('Петров', 'Петр'): 41,
    ('Петрова', 'Александра'): 38,
    ('Петрова', 'Светлана'): 11,
    ('Петров', 'Андрей'): 7,
    ('Николаев', 'Петр'): 37,
    ('Николаева', 'Александра'): 34,
    ('Николаев', 'Вадим'): 11,
    ('Николаев', 'Олег'): 9,
}

surname = input('Введите фамилию: ').lower()
for i, j in members.items():
    if surname in i[0].lower():
        print(i[0], i[1], j)
