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
    limit = 50000000
    prime_limit = int(limit ** 0.5) + 1
    primes = get_primes(prime_limit)

    found_numbers = set()

    for p2 in primes:
        square = p2 ** 2
        if square >= limit: break

        for p3 in primes:
            cube = p3 ** 3
            if square + cube >= limit: break

            for p4 in primes:
                fourth = p4 ** 4
                total = square + cube + fourth
                if total >= limit: break

                found_numbers.add(total)

    return len(found_numbers)


print(solve())
# 1097343