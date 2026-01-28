import math


def solve():
    count = 0
    limit = 1000000

    for n in range(1, 101):
        for r in range(0, n + 1):
            combinations = math.comb(n, r)
            if combinations > limit:
                count += 1

    return count


if __name__ == "__main__":
    result = solve()
    print(result)
    # 4075