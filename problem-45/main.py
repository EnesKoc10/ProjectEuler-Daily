import math


def is_pentagonal(n):
    test = (math.sqrt(24 * n + 1) + 1) / 6
    return test.is_integer()


def find_next_number(start_h):
    h_index = start_h + 1
    while True:
        hex_num = h_index * (2 * h_index - 1)

        if is_pentagonal(hex_num):
            return hex_num

        h_index += 1


result = find_next_number(143)
print(result)
# 1533776805