def solve():
    limit = 100000
    target_k = 10000

    radicals = [1] * (limit + 1)

    for i in range(2, limit + 1):
        if radicals[i] == 1:
            for j in range(i, limit + 1, i):
                radicals[j] *= i

    sorted_elements = []
    for n in range(1, limit + 1):
        sorted_elements.append((radicals[n], n))

    sorted_elements.sort()

    return sorted_elements[target_k - 1][1]


print(solve())
# 21417