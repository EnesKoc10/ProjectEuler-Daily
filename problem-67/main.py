def solve_maximum_path_sum(file_path):
    with open(file_path, 'r') as file:
        triangle = [[int(number) for number in line.split()] for line in file]

    for row_index in range(len(triangle) - 2, -1, -1):
        for col_index in range(len(triangle[row_index])):
            left_child = triangle[row_index + 1][col_index]
            right_child = triangle[row_index + 1][col_index + 1]
            triangle[row_index][col_index] += max(left_child, right_child)

    return triangle[0][0]

result = solve_maximum_path_sum('0067_triangle.txt')
print(result)
# 7273