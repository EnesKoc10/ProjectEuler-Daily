import itertools


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve():
    digits = "7654321"

    for length in range(len(digits), 0, -1):
        current_digits = digits[len(digits) - length:]
        permutations = itertools.permutations(current_digits)

        for p in permutations:
            number = int("".join(p))
            if is_prime(number):
                return number


result = solve()
print(result)
# 7652413