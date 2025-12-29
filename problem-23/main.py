import math

def getProperDivisorsSum(n):
    if n < 2:
        return 0
    total = 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

limit = 28123
abundant_numbers = []

for i in range(12, limit + 1):
    if getProperDivisorsSum(i) > i:
        abundant_numbers.append(i)

is_sum_of_two_abundant = [False] * (limit + 1)

for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        abundant_sum = abundant_numbers[i] + abundant_numbers[j]
        if abundant_sum <= limit:
            is_sum_of_two_abundant[abundant_sum] = True
        else:
            break

non_abundant_sum = 0
for i in range(1, limit + 1):
    if not is_sum_of_two_abundant[i]:
        non_abundant_sum += i

print(non_abundant_sum)
# 4179871