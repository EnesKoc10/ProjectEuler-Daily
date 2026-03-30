from math import comb


def solve():
    digits = 100

    increasing = comb(digits + 9, 9) - 1

    decreasing = comb(digits + 10, 10) - (digits + 1)

    duplicates = 9 * digits

    result = increasing + decreasing - duplicates
    return result


print(solve())
# 51161058134250