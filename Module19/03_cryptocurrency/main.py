data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
print()
print('1 задание:')
for i in data:
    print(i, ':', data[i])
    print()

print('\n2 задание:')
data['ETH']['total_diff'] = 100
print('ETH:',  data["ETH"])

print('\n3 задание:')
data['tokens'][0]['fst_token_info']['name'] = 'doge'
fst_name = data['tokens'][0]['fst_token_info']['name']
print("data['tokens'][0]['fst_token_info']['name'] =", fst_name)

print('\n4 задание:')
per = data['tokens'][0]['total_out']
data['ETH']['total_out'] = per
data['tokens'][0].pop('total_out') # total_out удален
print(data['tokens'][0].get('total_out'))# значение total_out присвоено
print(data['ETH'])

print('\n5 задание:')
old_price = data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = old_price # т.е.значение False
print(data['tokens'][1]['sec_token_info']['total_price'])

