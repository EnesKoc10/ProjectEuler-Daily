def sum_of_primes(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit, p):
                primes[i] = False
                
    return sum(p for p, is_prime in enumerate(primes) if is_prime)

limit = 2000000


result = sum_of_primes(limit)

print(result)
# 142913828922