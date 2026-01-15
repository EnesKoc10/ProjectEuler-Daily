def solve():
    constant_digits = ""
    number = 1

    while len(constant_digits) < 1000000:
        constant_digits += str(number)
        number += 1

    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = 1

    for i in indices:
        digit = int(constant_digits[i - 1])
        result *= digit

    return result


if __name__ == "__main__":
    print(solve())
    # 210