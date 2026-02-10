import math


def solve_pell():
    max_x = 0
    result_d = 0

    for d in range(2, 1001):
        root = int(math.sqrt(d))
        if root * root == d:
            continue

        m = 0
        d_val = 1
        a = root

        num1, num = 1, a
        den1, den = 0, 1

        while num * num - d * den * den != 1:
            m = d_val * a - m
            d_val = (d - m * m) // d_val
            a = (root + m) // d_val

            num2 = num1
            num1 = num
            den2 = den1
            den1 = den

            num = a * num1 + num2
            den = a * den1 + den2

        if num > max_x:
            max_x = num
            result_d = d

    return result_d


print(solve_pell())
# 661