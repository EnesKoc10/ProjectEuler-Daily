import itertools


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    primes = [n for n in range(1000, 10000) if is_prime(n)]

    for i in range(len(primes)):
        p1 = primes[i]
        if p1 == 1487:
            continue

        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            p3 = p2 + (p2 - p1)

            if p3 < 10000 and is_prime(p3):
                s1, s2, s3 = str(p1), str(p2), str(p3)
                if sorted(s1) == sorted(s2) == sorted(s3):
                    return s1 + s2 + s3


print(solve())
# 296962999629