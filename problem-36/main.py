def is_palindrome(s):
    return s == s[::-1]


total_sum = 0

for number in range(1, 1000000):
    decimal_str = str(number)
    binary_str = bin(number)[2:]

    if is_palindrome(decimal_str) and is_palindrome(binary_str):
        total_sum += number

print(total_sum)
# 872187