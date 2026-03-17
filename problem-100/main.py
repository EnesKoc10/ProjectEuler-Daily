def solve():
    blue_discs = 15
    total_discs = 21
    limit = 10 ** 12

    while total_discs <= limit:
        next_blue = 3 * blue_discs + 2 * total_discs - 2
        next_total = 4 * blue_discs + 3 * total_discs - 3

        blue_discs = next_blue
        total_discs = next_total

    return blue_discs


print(solve())
# 756872327473