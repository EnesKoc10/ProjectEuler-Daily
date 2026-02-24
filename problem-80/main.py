from decimal import Decimal, getcontext


def solve():
    getcontext().prec = 105
    total_digital_sum = 0

    for n in range(1, 101):
        root = Decimal(n).sqrt()

        if root % 1 != 0:
            decimal_string = str(root).replace('.', '')[:100]
            total_digital_sum += sum(int(digit) for digit in decimal_string)

    return total_digital_sum


print(solve())
# 40886