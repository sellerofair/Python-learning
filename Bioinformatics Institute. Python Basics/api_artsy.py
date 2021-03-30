'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy (ввести имя файла).
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения.
В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
'''


import requests
import json

res = requests.post('https://api.artsy.net/api/tokens/xapp_token', data={
    'client_id': '5bf0e7367d2f08ba9ed7',
    'client_secret': 'bda2337e5cab565c0cbd3834be11e73f'
})

j = json.loads(res.text)

token = j['token']

headers = {"X-Xapp-Token" : token}

art_list = []

with open(input('Input filename with artists\' IDs: '), encoding='UTF-8') as f:

    for artist_id in f:

        api_url = 'https://api.artsy.net/api/artists/' + artist_id.strip()

        res = requests.get(api_url, headers=headers)
        print(res.status_code)

        j = json.loads(res.text)
        art_list.append({
            'sortable_name': j['sortable_name'],
            'year': int(j['birthday'])
        })

art_list.sort(key=lambda art_dict: (art_dict['year'], art_dict['sortable_name']))
print(*[artist['sortable_name'] for artist in art_list], sep='\n')