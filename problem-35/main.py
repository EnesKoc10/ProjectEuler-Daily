def get_primes(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit, p):
                primes[i] = False
    return primes

def is_circular(n, prime_lookup):
    s = str(n)
    for i in range(len(s)):
        rotation = int(s[i:] + s[:i])
        if not prime_lookup[rotation]:
            return False
    return True

limit = 1000000
prime_lookup = get_primes(limit)
circular_primes_count = 0

for n in range(limit):
    if prime_lookup[n]:
        if is_circular(n, prime_lookup):
            circular_primes_count += 1

print(circular_primes_count)
# 55