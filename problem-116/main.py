def count_ways(tile_length, total_length):
    ways = [0] * (total_length + 1)
    ways[0] = 1

    for i in range(1, total_length + 1):
        ways[i] = ways[i - 1]
        if i >= tile_length:
            ways[i] += ways[i - tile_length]

    return ways[total_length] - 1


def solve():
    total_length = 50
    red_ways = count_ways(2, total_length)
    green_ways = count_ways(3, total_length)
    blue_ways = count_ways(4, total_length)

    return red_ways + green_ways + blue_ways


print(solve())