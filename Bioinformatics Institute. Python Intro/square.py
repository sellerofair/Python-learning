shape = input()
if shape == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif shape == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif shape == 'круг':
    r = float(input())
    print(3.14 * r ** 2)
else:
    print('Неизвестная фигура!')