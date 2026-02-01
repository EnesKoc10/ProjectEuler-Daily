def solve():
    numerator = 3
    denominator = 2
    count = 0

    for _ in range(1, 1000):
        if len(str(numerator)) > len(str(denominator)):
            count += 1

        next_numerator = numerator + 2 * denominator
        next_denominator = numerator + denominator

        numerator = next_numerator
        denominator = next_denominator

    return count


result = solve()
print(result)
# 153