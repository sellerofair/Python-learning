from random import choice
from display_hangman import display_hangman

# Функции

def get_word(file):
    with open(file, encoding='utf-8') as f:
        return choice(f.read().split('\n')).upper()

def ask_answer():
    answer = input('Назови букву или слово целиком: ')
    while not answer.isalpha():
        answer = input('Нужны только буквы: ')
    return answer.upper()

def get_check(_checked):
    _check = ask_answer()
    while _check in _checked:
        print('Ты уже это говорил. Давай что-то новенькое:')
        _check = ask_answer()
    return _check

def get_map(_word):
    _word = list(_word)
    _letters = []
    _indices = []
    for i, c in enumerate(_word):
        if c != '_':
            _letters.append(c)
            _indices.append([i])
            for j in range(i + 1, len(_word)):
                if _word[j] == c:
                    _indices[-1].append(j)
                    _word[j] = '_'
    n = len(_letters)
    return [n, _letters, _indices, [False] * n, len(_word)]

def word_completion(_map):
    result = ['_'] * _map[4]
    for i, guessed in enumerate(_map[3]):
        if guessed:
            for j in _map[2][i]:
                result[j] = _map[1][i]
    return ''.join(result)

def play(word):
    word_map = get_map(word)
    checked = []
    tries = 0

    print(word)

    while True:
        display_hangman(tries)
        print(word_map[4], 'букв')
        print(word_completion(word_map) + '\n')

        if tries == 6:
            print(f'Ты проиграл. Это было слово {word}.')
            break

        check = get_check(checked)

        if len(check) == 1:
            if check in word_map[1]:
                word_map[3][word_map[1].index(check)] = True
                if word_completion(word_map) == word:
                    print(word)
                    print('Ты угадал последнюю букву! Ты победил!')
                    break
            else:
                checked.append(check)
                tries += 1
        else:
            if check == word:
                print('Поздравляю, ты угадал слово! Ты победил!')
                break
            else:
                checked.append(check)
                tries += 1

# Основной код

game = 'да'

print('\nДавайте играть в угадайку слов!')
while game == 'да':
    play(get_word('Hangman_words.txt'))
    game = input('\nЕсли хочешь сыграть еще, скажи "да": ')

print('\nСпасибо за игру\n')