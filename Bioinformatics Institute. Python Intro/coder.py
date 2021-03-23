base = input()          # исходные симводы
code = input()          # кодированные символы
coder = {}
encoder = {}
for i in range(len(base)):
    coder[base[i]] = code[i]
    encoder[code[i]] = base[i]
to_code = input()       # строка для кодирования
to_encode = input()     # строка для декодирования
coded = ''
for c in to_code:
    coded += coder[c]
encoded = ''
for c in to_encode:
    encoded += encoder[c]
print(coded)
print(encoded)