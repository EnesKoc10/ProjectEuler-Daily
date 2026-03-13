def solve():
    mod = 10 ** 10
    exponent = 7830457
    multiplier = 28433

    power_part = pow(2, exponent, mod)
    result = (multiplier * power_part + 1) % mod

    return str(result).zfill(10)


print(solve())
# 8739992577