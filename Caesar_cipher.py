language = input('Выберите язык ("ру" - русский, иначе английский): ') == 'ру'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' if language else 'abcdefghijklmnopqrstuvwxyz'

direction = input('Выберите направление кодирования ("ш" - шифрование, иначе дешифрование): ') == 'ш'
length = len(alphabet)

rot = input(f'Выберите шаг сдвига от 1 до {length - 1}: ')
while not (rot.isdigit() and 1 <= int(rot) < length):
    rot = input(f'Введите натуральное число от 1 до {length - 1}: ')
rot = int(rot)

if direction:
    key = alphabet[rot:] + alphabet[:rot]
else:
    key = alphabet[-rot:] + alphabet[:-rot]

message = list(input('Введите сообщение:\n'))

for i, c in enumerate(message):
    if c.isalpha():
        d = key[alphabet.find(c.lower())]
        if c.isupper():
            d = d.upper()
        message[i] = d

print('Шифрованное' if direction else 'Дешифрованное', 'сообщение:')
print(''.join(message))