"""Найти в матрице первую строку, все элементы которой равны нулю.
Все элементы столбца с таким же номером уменьшить вдвое"""
def find(matrix):
    k = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                k += 1
            if k == 3:
                row = i
                break
        k = 0

    for i in range(3):
        matrix[i][row] /= 2

    return matrix

matrix = [
    [1, 2, 3],
    [0, 0, 0],
    [4, 4, 6]
]

result = find(matrix)
print(result)


