def solve():
    limit = 1000000
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    total_fractions = sum(phi[2:])
    return total_fractions


print(solve())
# 303963552391