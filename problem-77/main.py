def get_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes


def solve():
    target_limit = 100
    while True:
        primes = get_primes(target_limit)
        ways = [0] * (target_limit + 1)
        ways[0] = 1

        for p in primes:
            for i in range(p, target_limit + 1):
                ways[i] += ways[i - p]

        for index, count in enumerate(ways):
            if count > 5000:
                return index

        target_limit *= 2


print(solve())
# 71