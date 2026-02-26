def solve():
    matrix = []
    with open("0082_matrix.txt", "r") as f:
        for line in f:
            matrix.append([int(x) for x in line.split(",")])

    rows = len(matrix)
    cols = len(matrix[0])

    min_costs = [matrix[i][0] for i in range(rows)]

    for j in range(1, cols):
        current_column_costs = [min_costs[i] + matrix[i][j] for i in range(rows)]

        for i in range(1, rows):
            current_column_costs[i] = min(current_column_costs[i], current_column_costs[i - 1] + matrix[i][j])

        for i in range(rows - 2, -1, -1):
            current_column_costs[i] = min(current_column_costs[i], current_column_costs[i + 1] + matrix[i][j])

        min_costs = current_column_costs

    return min(min_costs)


print(solve())
# 260324