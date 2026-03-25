def count_solutions(n):
    num_divisors = 1
    temp_n = n
    d = 2
    while d * d <= temp_n:
        exponent = 0
        while temp_n % d == 0:
            exponent += 1
            temp_n //= d
        num_divisors *= (2 * exponent + 1)
        d += 1
    if temp_n > 1:
        num_divisors *= 3
    return (num_divisors + 1) // 2

def solve():
    target = 1000
    n = 1
    while True:
        if count_solutions(n) > target:
            return n
        n += 1

print(solve())
# 180180