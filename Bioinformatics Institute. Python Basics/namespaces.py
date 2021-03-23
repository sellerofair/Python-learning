'''
Эмулятор работы с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
На вход подаются следующие запросы:
create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var>
    при запросе из пространства <namespace>, или None, если такого пространства не существует
'''

def create(_namespaces, namespace, parent):
    _namespaces[namespace] = [
        set(),
        parent
    ]

def add(_namespaces, namespace, var):
    _namespaces[namespace][0].add(var)

def get(_namespaces, namespace, var):
    if var in _namespaces[namespace][0]:
        print(namespace)
    elif namespace != 'global':
        get(_namespaces, _namespaces[namespace][1], var)
    else:
        print('None')

commands = {
    'create': create,
    'add': add,
    'get': get
}

namespaces = {
    'global': [
        set()
    ]
}

for _ in range(int(input())):
    f, a, b = input().split()
    commands[f](namespaces, a, b)