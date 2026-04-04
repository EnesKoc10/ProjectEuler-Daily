from itertools import permutations


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


prime_cache = {}


def is_prime_cached(n):
    if n not in prime_cache:
        prime_cache[n] = is_prime(n)
    return prime_cache[n]


def count_prime_sets(digits, last_prime=0):
    total = 0
    for i in range(1, len(digits) + 1):
        num = 0
        for j in range(i):
            num = num * 10 + digits[j]

        if num > last_prime and is_prime_cached(num):
            if i == len(digits):
                total += 1
            else:
                total += count_prime_sets(digits[i:], num)
    return total


def solve():
    grand_total = 0
    for p in permutations(range(1, 10)):
        grand_total += count_prime_sets(p)
    return grand_total


print(solve())
# 44680