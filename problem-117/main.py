def solve():
    length = 50
    ways = [0] * (length + 1)
    ways[0] = 1

    for i in range(1, length + 1):
        ways[i] += ways[i - 1]

        if i >= 2:
            ways[i] += ways[i - 2]
        if i >= 3:
            ways[i] += ways[i - 3]
        if i >= 4:
            ways[i] += ways[i - 4]

    return ways[length]


print(solve())
# 100808458960497