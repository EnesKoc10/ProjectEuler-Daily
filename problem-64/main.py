import math


def solve_odd_periods(limit):
    odd_period_count = 0

    for n in range(2, limit + 1):
        root = math.isqrt(n)
        if root * root == n:
            continue

        m = 0
        d = 1
        a0 = root
        a = root
        period_length = 0

        while a != 2 * a0:
            m = d * a - m
            d = (n - m * m) // d
            a = (a0 + m) // d
            period_length += 1

        if period_length % 2 != 0:
            odd_period_count += 1

    return odd_period_count


result = solve_odd_periods(10000)
print(result)
# 1322