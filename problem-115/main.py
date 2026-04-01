def count_fill_ways(m, n):
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in range(1, n + 1):
        ways[i] = ways[i - 1]
        for block_size in range(m, i + 1):
            if i - block_size == 0:
                ways[i] += 1
            else:
                ways[i] += ways[i - block_size - 1]
    return ways[n]


def solve():
    m = 50
    target = 1000000
    n = m

    while True:
        if count_fill_ways(m, n) > target:
            return n
        n += 1


print(solve())
# 168