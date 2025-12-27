def getSumOfProperDivisors(n):
    divisors_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != 1 and i != n // i:
                divisors_sum += n // i
    return divisors_sum

limit = 10000
amicable_numbers = set()

for a in range(1, limit):
    b = getSumOfProperDivisors(a)
    if a != b and b < limit:
        if getSumOfProperDivisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

total_sum = sum(amicable_numbers)
print(total_sum)
# 31626