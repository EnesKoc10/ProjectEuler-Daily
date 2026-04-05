def solve():
    results = []
    for base in range(2, 100):
        for exponent in range(2, 10):
            number = base ** exponent
            digit_sum = sum(int(d) for d in str(number))

            if digit_sum == base:
                results.append(number)

    results.sort()
    return results[29]


print(solve())
# 248155780267521