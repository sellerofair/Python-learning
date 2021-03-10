# слабый вариант
# есть вероятность того, что не из всех наборов символы попадут в пароль

from random import choice

def generate_password(_length, _chars):
    pw = ''
    for _ in range(_length):
        pw += choice(_chars)
    return pw

digits = '0123456789'
lowercase_letters = 'ioabcdefghjklmnpqrstuvwxyz'
uppercase_letters = 'ILOABCDEFGHJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

number = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите необходимую длину пароля: '))
req_digits = input('Если необходимо использовать цифры (0123456789), введите "да": ') == 'да'
req_lower = input('Если необходимо использовать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ), введите "да": ') == 'да'
req_upper = input('Если необходимо использовать строчные буквы (abcdefghijklmnopqrstuvwxyz), введите "да": ') == 'да'
req_punctuation = input('Если необходимо использовать символы (!#$%&*+-=?@^_), введите "да": ') == 'да'
ex_complex = input('Если необходимо исключать неоднозначные символы (ilI1Lo0O), введите "да": ') == 'да'

if ex_complex:
    digits = digits[2:]
    lowercase_letters = lowercase_letters[2:]
    uppercase_letters = uppercase_letters[3:]
    punctuation = punctuation[1:]
if req_digits:
    chars += digits
if req_lower:
    chars += lowercase_letters
if req_upper:
    chars += uppercase_letters
if req_punctuation:
    chars += punctuation
print(chars)
for _ in range(number):
    print(generate_password(length, chars))