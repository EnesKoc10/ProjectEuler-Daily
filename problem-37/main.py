import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_truncatable(n):
    str_n = str(n)

    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False

    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:i])):
            return False

    return True


truncatable_primes = []
number = 11

while len(truncatable_primes) < 11:
    if is_prime(number):
        if is_truncatable(number):
            truncatable_primes.append(number)
    number += 1

result = sum(truncatable_primes)
print(result)
# 748317