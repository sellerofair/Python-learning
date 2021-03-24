'''
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов.
В i-й строке указано от каких классов наследуется i-й класс.
Класс может ни от кого не наследоваться.
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.
'''

from is_parent import is_parent

classes = {}

for _ in range(int(input())):
    req = input()
    pos = req.find(':')
    if pos == -1:
        classes[req] = {}
    else:
        new_cl = req[:pos - 1]
        classes[new_cl] = set(req[pos + 2:].split())

for _ in range(int(input())):
    class1, class2 = input().split()
    msg = 'No'
    if class1 in classes.keys() and class2 in classes.keys():
        if class1 == class2 or is_parent(classes, class1, class2):
            msg = 'Yes'
    print(msg)