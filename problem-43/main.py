from itertools import permutations


def solve():
    digits = '0123456789'
    primes = [2, 3, 5, 7, 11, 13, 17]
    total_sum = 0

    for p in permutations(digits):
        if p[0] == '0':
            continue

        number_str = "".join(p)
        is_valid = True

        for i in range(7):
            sub_num = int(number_str[i + 1:i + 4])
            if sub_num % primes[i] != 0:
                is_valid = False
                break

        if is_valid:
            total_sum += int(number_str)

    return total_sum


print(solve())
# 16695334890