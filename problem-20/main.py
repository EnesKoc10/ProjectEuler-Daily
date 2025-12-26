result = 1
for i in range(1, 101):
    result *= i

digits_sum = 0
for digit in str(result):
    digits_sum += int(digit)


print(digits_sum)
# 648