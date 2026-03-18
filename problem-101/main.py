def get_term(n):
    return sum((-n) ** i for i in range(11))


def lagrange_interpolation(points, x):
    total = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        numerator = 1
        denominator = 1
        for j in range(n):
            if i == j: continue
            xj, _ = points[j]
            numerator *= (x - xj)
            denominator *= (xi - xj)
        total += yi * numerator // denominator
    return total


def solve():
    sequence = [get_term(n) for n in range(1, 12)]
    fit_sum = 0

    for k in range(1, 11):
        points = [(n, sequence[n - 1]) for n in range(1, k + 1)]
        fit = lagrange_interpolation(points, k + 1)
        fit_sum += fit

    return fit_sum


print(solve())
# 37076114526