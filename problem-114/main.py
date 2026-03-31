def solve():
    length = 50
    min_block = 3
    ways = [0] * (length + 1)
    ways[0] = 1

    for i in range(1, length + 1):
        ways[i] = ways[i - 1]
        for block_size in range(min_block, i + 1):
            if i - block_size == 0:
                ways[i] += 1
            else:
                ways[i] += ways[i - block_size - 1]

    return ways[length]


print(solve())
# 16475640049