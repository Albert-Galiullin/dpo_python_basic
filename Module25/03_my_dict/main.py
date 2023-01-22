class MyDict(dict):
    def get(self, key, default_value = None):
        return super().get(key, 0)


new_dict = MyDict()
new_dict['Андрей'] = 20
new_dict['Сергей'] = 21
new_dict['Владимир'] = 19
print(new_dict)
print(new_dict.get('Петя'))
