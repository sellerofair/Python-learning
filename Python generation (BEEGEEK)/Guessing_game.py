from random import randint

def is_valid_max(data):
    return data.isdigit() and int(data) > 1

def is_valid(data, maximum):
    return data.isdigit() and 1 <= int(data) <= maximum

def max_request():
    print()
    max_n = input('Какое максимальное число мне можно загадать? ')
    while not is_valid_max(max_n):
        max_n = input('Введи натуральное число больше 1: ')
    return int(max_n)

def one_shot(maximum, try_num):
    print()
    shot = input(f'Попытка № {try_num}: ')
    while not is_valid(shot, maximum):
        shot = input(f'А может быть все-таки введем целое число от 1 до {maximum}? ')
    return int(shot)

game = 'да'

print()
print('Добро пожаловать в числовую угадайку')

while game == 'да':

    max_n = max_request()

    n = randint(1, max_n)

    print(f'Я загадал число от 1 до {max_n}, а ты попробуй угадать')

    tries = 1
    m = one_shot(max_n, tries)
    while m != n:
        if m > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        tries += 1
        m = one_shot(max_n, tries)
    
    print()
    print('Вы угадали, поздравляем!')
    print(f'Потребовалось попыток: {tries}')
    print()
    game = input('Если хочешь сыграть еще, скажи "да": ')

print()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print()