def find_totient_maximum(limit):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    result = 1

    for p in primes:
        if result * p > limit:
            break
        result *= p

    return result


limit_value = 1000000
print(find_totient_maximum(limit_value))
# 510510