'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B,
т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Программе на вход подаются две строки, содержащие url двух документов A и B.
Вывести Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Не все ссылки внутри HTML документа могут вести на существующие HTML документы.
'''

import re

import requests

a, b = input(), input()

res = requests.get(a)
msg = 'No'
if res.status_code == 200:
    ref_list = re.findall(r'<a href="(.*)">', res.text)
    for ref in ref_list:
        res = requests.get(ref)
        if res.status_code == 200:
            if b in res.text:
                msg = 'Yes'
                break

print(msg)