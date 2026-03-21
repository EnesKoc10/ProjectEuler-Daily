import math


def is_pandigital(n):
    s = str(n)
    return len(s) == 9 and set(s) == set("123456789")


def solve():
    a, b = 1, 1
    k = 2
    log10_phi = math.log10((1 + math.sqrt(5)) / 2)
    log10_sqrt5 = math.log10(math.sqrt(5))

    while True:
        k += 1
        a, b = b, (a + b) % 1000000000

        if is_pandigital(b):
            first_digits_log = k * log10_phi - log10_sqrt5
            first_nine = int(pow(10, first_digits_log - int(first_digits_log) + 8))

            if is_pandigital(first_nine):
                return k


print(solve())
# 329468