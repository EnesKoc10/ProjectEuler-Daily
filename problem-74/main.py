import math


def get_digit_factorial_sum(num, factorials):
    total = 0
    if num == 0:
        return factorials[0]
    while num > 0:
        total += factorials[num % 10]
        num //= 10
    return total


def solve():
    factorials = [math.factorial(i) for i in range(10)]
    chain_lengths = {}
    total_sixty_chains = 0

    for i in range(1, 1000000):
        current = i
        path = []
        path_set = set()

        while current not in path_set:
            if current in chain_lengths:
                length = len(path) + chain_lengths[current]
                break

            path.append(current)
            path_set.add(current)
            current = get_digit_factorial_sum(current, factorials)
        else:
            length = len(path)

        chain_lengths[i] = length
        if length == 60:
            total_sixty_chains += 1

    return total_sixty_chains


print(solve())
# 402