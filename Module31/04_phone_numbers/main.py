import re

phone_list = ['9999999999', '999999-999', '99999x9999', '8999999999']

def check(lst) -> None:
    for i in lst:
        res = re.findall(r'[8-9]\d{9}', i)
        if len(res) > 0 and len(i) == 10:
            print(i, 'всё в порядке')
        else:
            print(i, 'не подходит')

check(phone_list)
