import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def satisfies_conjecture(n):
    k = 1
    while True:
        twice_square = 2 * (k ** 2)
        if twice_square >= n:
            break

        remainder = n - twice_square
        if is_prime(remainder):
            return True
        k += 1
    return False


def find_smallest_counterexample():
    number = 9
    while True:
        if not is_prime(number):
            if not satisfies_conjecture(number):
                return number
        number += 2


result = find_smallest_counterexample()
print(result)
# 5777