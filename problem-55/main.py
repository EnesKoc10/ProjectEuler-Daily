def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    current_value = n
    for _ in range(50):
        reversed_value = int(str(current_value)[::-1])
        current_value += reversed_value
        if is_palindrome(current_value):
            return False
    return True

lychrel_count = 0
for number in range(1, 10000):
    if is_lychrel(number):
        lychrel_count += 1

print(lychrel_count)
# 249