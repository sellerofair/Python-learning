# заполнение матрицы по спирали

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
i0, j0, i, j = 1, 0, 0, 0
i1, j1 = n - 1, n - 1
direction = 'right'
for x in range(1, n ** 2 + 1):
    matrix[i][j] = x
    if direction == 'right' and j + 1 > j1:
        direction = 'down'
        j1 -= 1
    if direction == 'down' and i + 1 > i1:
        direction = 'left'
        i1 -= 1
    if direction == 'left' and j - 1 < j0:
        direction = 'up'
        j0 += 1
    if direction == 'up' and i - 1 < i0:
        direction = 'right'
        i0 += 1
    j = j + (direction == 'right') - (direction == 'left')
    i = i + (direction == 'down') - (direction == 'up')
for row in matrix:
    print(*row, sep=' ')