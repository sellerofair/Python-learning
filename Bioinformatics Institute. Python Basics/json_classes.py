'''
Дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислить предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
'''


import json

from funcs import is_parent

data = input()
classes = {}

for class_dict in json.loads(data):
    classes[class_dict['name']] = class_dict['parents']

class_list = list(classes)
class_list.sort()

for class_name in class_list:
    child_number = 1
    for child in class_list:
        if child != class_name and is_parent(classes, class_name, child):
            child_number += 1
    print(class_name, ':', child_number)