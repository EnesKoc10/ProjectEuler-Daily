def is_bouncy(n):
    digits = str(n)
    increasing = False
    decreasing = False
    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            increasing = True
        elif digits[i] > digits[i + 1]:
            decreasing = True
        if increasing and decreasing:
            return True
    return False


def solve():
    bouncy_count = 0
    n = 100
    while True:
        if is_bouncy(n):
            bouncy_count += 1

        if bouncy_count / n == 0.99:
            return n
        n += 1


print(solve())
# 1587000