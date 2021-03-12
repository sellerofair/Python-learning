'''
На вход подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек).
Вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен
сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
'''

matrix = []
s = input()
while s != 'end':
    matrix.append([int(c) for c in s.split()])
    s = input()
hight = len(matrix)
width = len(matrix[0])
new_matrix = []
for i in range(hight):
    new_matrix.append([])
    for j in range(width):
        if hight > 1:
            col_part = matrix[i - 1][j] + matrix[i - hight + 1][j]
        else:
            col_part = matrix[i][j] * 2
        if width > 1:
            row_part = matrix[i][j - 1] + matrix[i][j - width + 1]
        else:
            row_part = matrix[i][j] * 2
        new_matrix[i].append(col_part + row_part)
for row in new_matrix:
    print(*row, sep=' ')