import math


def solve():
    perimeter_limit = 1000000000
    total_perimeter_sum = 0

    for side in range(3, (perimeter_limit // 3) + 2, 2):
        for diff in [-1, 1]:
            third_side = side + diff
            perimeter = 2 * side + third_side

            if perimeter > perimeter_limit:
                continue

            height_sq = side ** 2 - (third_side // 2) ** 2
            height = math.isqrt(height_sq)

            if height * height == height_sq:
                if (height * third_side) % 2 == 0:
                    total_perimeter_sum += perimeter

    return total_perimeter_sum


print(solve())
# 518408346