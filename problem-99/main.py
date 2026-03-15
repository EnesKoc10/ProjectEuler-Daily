import math


def solve():
    max_value = 0
    best_line = 0

    with open("0099_base_exp.txt", "r") as f:
        for index, line in enumerate(f, 1):
            base, exponent = map(int, line.split(","))

            current_value = exponent * math.log(base)

            if current_value > max_value:
                max_value = current_value
                best_line = index

    return best_line


print(solve())
# 709