import math


def solve():
    limit = 1000000
    count = 0
    m = 0

    while count < limit:
        m += 1
        for ab_sum in range(2, 2 * m + 1):
            hypotenuse_sq = ab_sum ** 2 + m ** 2
            hypotenuse = math.isqrt(hypotenuse_sq)

            if hypotenuse * hypotenuse == hypotenuse_sq:
                if ab_sum <= m:
                    count += ab_sum // 2
                else:
                    count += m - (ab_sum + 1) // 2 + 1

    return m


print(solve())
# 1818