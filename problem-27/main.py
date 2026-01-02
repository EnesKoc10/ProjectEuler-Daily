def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    max_primes = 0
    best_product = 0

    primes_under_1000 = [b for b in range(2, 1001) if is_prime(b)]

    for b in primes_under_1000:
        for a in range(-999, 1000):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
            
            if n > max_primes:
                max_primes = n
                best_product = a * b
                
    return best_product

if __name__ == "__main__":
    result = solve()
    print(result)