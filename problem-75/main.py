import math


def solve():
    limit = 1500000
    triangle_counts = [0] * (limit + 1)

    m_limit = int(math.sqrt(limit / 2))

    for m in range(2, m_limit):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                perimeter = 2 * m * (m + n)

                for multiple in range(perimeter, limit + 1, perimeter):
                    triangle_counts[multiple] += 1

    singular_triangles = 0
    for count in triangle_counts:
        if count == 1:
            singular_triangles += 1

    return singular_triangles


print(solve())
# 161667