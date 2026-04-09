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
    primes = get_primes(300000)
    target = 10 ** 10

    for i, p in enumerate(primes, 1):
        n = i
        if n % 2 == 1:
            remainder = (2 * n * p) % (p * p)
            if remainder > target:
                return n


print(solve())
# 21035