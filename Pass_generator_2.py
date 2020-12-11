# хороший вариант

from random import choice, shuffle

# Функции

def is_valid(data, _minimum):
    return data.isdigit() and int(data) >= _minimum

def asq_numeric(greeting, alarm, minimum):
    data = input(greeting)
    while not is_valid(data, minimum):
        data = input(alarm + ' Повторите ввод: ')
    return int(data)

def generate_password(_length, _min_length, _chars):
    pw = ''
    # используем все необходимые наборы символов
    for i in range(_min_length):
        pw += choice(_chars[i])

    # добиваем остатки случайными символами из случайных наборов
    for _ in range(_length - _min_length):
        pw += choice(choice(_chars))
    
    # перемешиваем пароль иначе первые наборы первых символов будут повторяться
    pw = list(pw)
    shuffle(pw)
    pw = ''.join(pw)

    return pw

# Основной код

run = 'да'

while run == 'да':

    print()
    print('Определите требования к паролю:')
    reqirements = [
        input('Если необходимо использовать цифры (0123456789), введите "да": ') == 'да',
        input('Если необходимо использовать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ), введите "да": ') == 'да',
        input('Если необходимо использовать строчные буквы (abcdefghijklmnopqrstuvwxyz), введите "да": ') == 'да',
        input('Если необходимо использовать символы (!#$%&*+-=?@^_), введите "да": ') == 'да',
    ]

    # минимально возможная длина пароля, при которой поместятся символы из каждого необходимого набора
    min_length = sum(reqirements)

    # если не выбран ни один набор символов, откуда тогда набрать пароль???
    if min_length == 0:
        print('!!! Не выбраны символы для генерации !!!')
    
    # в противном случае выполняем основной цикл программы
    else:

        need_complex = input('Если необходимо исключать неоднозначные символы (ilI1Lo0O), введите "да": ') != 'да'

        chars = [
            '01' * need_complex + '23456789',
            'io' * need_complex + 'abcdefghjklmnpqrstuvwxyz',
            'ILO' * need_complex + 'ABCDEFGHJKMNPQRSTUVWXYZ',
            '!' * need_complex + '#$%&*+-=?@^_'
        ]
        
        # исключаем из списка ненужные наборы символов
        for i in range(3, -1, -1):
            if not reqirements[i]:
                del chars[i]

        number = asq_numeric(
            'Введите количество паролей для генерации: ',
            'Количество паролей должно быть натуральным числом.',
            1
        )

        length = asq_numeric(
            'Введите необходимую длину паролей: ',
            f'Длина паролей должна быть натуральным числом больше {min_length}.',
            min_length
        )

        print()
        for _ in range(number):
            print(generate_password(length, min_length, chars))
    
    print()
    run = input('Если нужно сгенерировать еще пароли, введите "да": ')