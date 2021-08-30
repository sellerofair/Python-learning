# Координатные четверти

# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.

# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.

# Формат выходных данных
# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

# Примечание. Точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.


n = int(input())

result = {
    'Первая': 0,
    'Вторая': 0,
    'Третья': 0,
    'Четвертая': 0
}

for _ in range(n):
    [x, y] = [int(k) for k in input().split()]
    if x > 0:
        if y > 0:
            result['Первая'] += 1
        elif y < 0:
            result['Четвертая'] += 1
    elif x < 0:
        if y > 0:
            result['Вторая'] += 1
        elif y < 0:
            result['Третья'] += 1

for key, v in result.items():
    print(f'{key} четверть: {v}')
