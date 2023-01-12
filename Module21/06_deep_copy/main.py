import copy

site = dict()
site['html'] = {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }

def deepc(site):
    for _ in range(ques):
        product = input('Введите название продукта для нового сайта: ').lower()
        print(f'Сайт для {product}:')
        site_copy = copy.deepcopy(site)
        site_copy['html']['head']['title'] = f'Куплю/продам {product} недорого'
        site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {product}'
        for i, j in site_copy.items():
            print(i, j)

ques = int(input('\nСколько будет сайтов: '))
deepc(site)

