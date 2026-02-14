def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def get_primes(limit):
    primes = []
    sieve = [True] * limit
    for p in range(2, limit):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                sieve[i] = False
    return primes


def solve():
    limit = 10 ** 7
    prime_search_limit = 5000
    primes = get_primes(prime_search_limit)

    relevant_primes = [p for p in primes if 2000 < p < 5000]

    min_ratio = float('inf')
    result_n = 0

    for i in range(len(relevant_primes)):
        for j in range(i + 1, len(relevant_primes)):
            p1 = relevant_primes[i]
            p2 = relevant_primes[j]
            n = p1 * p2

            if n > limit:
                break

            phi = (p1 - 1) * (p2 - 1)

            if is_permutation(n, phi):
                ratio = n / phi
                if ratio < min_ratio:
                    min_ratio = ratio
                    result_n = n

    return result_n


print(solve())