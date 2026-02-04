import random


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(5):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_pair(p1, p2):
    s1 = str(p1)
    s2 = str(p2)
    return is_prime(int(s1 + s2)) and is_prime(int(s2 + s1))


def solve():
    limit = 10000
    primes = []
    is_p = [True] * limit
    for p in range(2, limit):
        if is_p[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                is_p[i] = False

    primes.remove(2)
    primes.remove(5)

    pairs = {}

    for i in range(len(primes)):
        p1 = primes[i]
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if is_pair(p1, p2):
                if p1 not in pairs: pairs[p1] = set()
                if p2 not in pairs: pairs[p2] = set()
                pairs[p1].add(p2)
                pairs[p2].add(p1)

    for p1 in primes:
        if p1 not in pairs: continue
        for p2 in pairs[p1]:
            if p2 < p1: continue
            common12 = pairs[p1].intersection(pairs[p2])
            for p3 in common12:
                if p3 < p2: continue
                common123 = common12.intersection(pairs[p3])
                for p4 in common123:
                    if p4 < p3: continue
                    common1234 = common123.intersection(pairs[p4])
                    for p5 in common1234:
                        if p5 < p4: continue
                        return p1 + p2 + p3 + p4 + p5


result = solve()
print(result)
# 26033