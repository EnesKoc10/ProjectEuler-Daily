import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def find_triangular_number(limit):
    n = 1
    while True:
        triangular_num = n * (n + 1) // 2
        
        if count_divisors(triangular_num) > limit:
            return triangular_num
        n += 1

target_divisors = 500
result = find_triangular_number(target_divisors)
print(result)