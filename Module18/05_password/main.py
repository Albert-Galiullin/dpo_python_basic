# Придумайте пароль: qwerty
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty12
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qwerty123
# Пароль ненадёжный. Попробуйте ещё раз.
# Придумайте пароль: qWErty123
# Это надёжный пароль!

password = input('Придумайте пароль: ')
a = sum(i.isupper() for i in password)
b = sum(i.isdigit() for i in password)
while True:
    if a > 0 and b > 2:
        print(' Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    password = input('Придумайте пароль: ')
    a = sum(i.isupper() for i in password)
    b = sum(i.isdigit() for i in password)
