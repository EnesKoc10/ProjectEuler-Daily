def is_valid(grid, r, c, n):
    for i in range(9):
        if grid[r][i] == n or grid[i][c] == n:
            return False
    start_row, start_col = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == n:
                return False
    return True


def solve_sudoku(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(grid, r, c, n):
                        grid[r][c] = n
                        if solve_sudoku(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True


def solve():
    total_sum = 0
    with open("0096_sudoku.txt", "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 10):
        grid = []
        for j in range(1, 10):
            grid.append([int(d) for d in lines[i + j].strip()])

        if solve_sudoku(grid):
            total_sum += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]

    return total_sum


print(solve())
# 24702