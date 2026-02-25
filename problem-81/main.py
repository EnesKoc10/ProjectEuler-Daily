def solve():
    matrix = []
    with open("0081_matrix.txt", "r") as f:
        for line in f:
            matrix.append([int(x) for x in line.split(",")])

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        matrix[i][0] += matrix[i - 1][0]

    for j in range(1, cols):
        matrix[0][j] += matrix[0][j - 1]

    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


print(solve())
# 427337