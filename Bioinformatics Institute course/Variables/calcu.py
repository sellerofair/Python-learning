a, b, op = float(input()), float(input()), input()
if op == '+':
    print(a + b)
if op == '-':
    print(a - b)
if op == '*':
    print(a * b)
if op == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
if op == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
if op == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
if op == 'pow':
    print(a ** b)
