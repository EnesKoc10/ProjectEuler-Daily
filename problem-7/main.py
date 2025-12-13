def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = 3
counter = 2


while counter <= 10001:
    if isPrime(x):
        counter += 1
        x += 2
    else:
        x += 2

print(x-2)  
# 104743