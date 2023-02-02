import requests
import json

req = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(req.text)  # преобразуем в словарь - десериализация JSON
n_data = dict()

for key, value in data.items():
    if key in('name', 'max_atmosphering_speed', 'starship_class', 'pilots'):
        n_data[key] = value

for key in n_data :
    if key == 'pilots':
        n_data[key] = []

urls = ['https://swapi.dev/api/people/13/', 'https://swapi.dev/api/people/14/',
'https://swapi.dev/api/people/25/', 'https://swapi.dev/api/people/31/']


for url in urls:
    resp = requests.get(url)
    data = json.loads(resp.text)

    dict_pilot = {
    'name': data.get('name'),
    'height': data.get('height'),
    'mass': data.get('mass'),
    'homeworld': data.get('homeworld')
    }
    resp2 = requests.get(data.get('homeworld'))
    data2 = json.loads(resp2.text)
    dict_pilot['planet'] = data2.get('name')

    n_data[key].append(dict_pilot)

with open('req.json', 'w') as file:
    json.dump(n_data, file, indent=4)

with open('req.json', 'r') as file:
    for line in file:
        print(line, end='')

