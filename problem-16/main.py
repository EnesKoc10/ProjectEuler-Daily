number = 2**1000
string_number = str(number)
digit_sum = sum(int(digit) for digit in string_number)

print(digit_sum)
# 1366