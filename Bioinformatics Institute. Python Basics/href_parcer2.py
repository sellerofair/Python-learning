
'''
На вход подается ссылка на HTML файл.
Необходимо найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида <a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
'''

import re

import requests

pattern = r'<a.*href\s*=\s*[\"\']([hHfF][tT]{1,2}[pP][sS]?://)?([\w\-\.]+)[\"\'/:\?]'

text = requests.get(input()).text
ref_list = [i[1] for i in re.findall(pattern, text) if i[1] != '..']

ref_list = list(set(ref_list))
ref_list.sort()
print(*ref_list, sep='\n')