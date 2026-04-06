def solve():
    total_max_remainder = 0
    for a in range(3, 1001):
        max_r = 2 * ((a - 1) // 2) * a
        total_max_remainder += max_r
    return total_max_remainder

print(solve())
# 333082500