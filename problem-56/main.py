max_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        power = a ** b
        digit_sum = sum(int(digit) for digit in str(power))

        if digit_sum > max_sum:
            max_sum = digit_sum

print(max_sum)
# 972