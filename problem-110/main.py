import math


def solve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    limit = 4000000
    min_n = float('inf')

    def find_min_n(index, current_n, current_divisors, last_exponent):
        nonlocal min_n

        if (current_divisors + 1) // 2 > limit:
            if current_n < min_n:
                min_n = current_n
            return

        if index == len(primes):
            return

        for exponent in range(1, last_exponent + 1):
            next_n = current_n * (primes[index] ** exponent)
            if next_n >= min_n:
                break
            find_min_n(index + 1, next_n, current_divisors * (2 * exponent + 1), exponent)

    find_min_n(0, 1, 1, 60)
    return min_n


print(solve())
# 9350130049860600