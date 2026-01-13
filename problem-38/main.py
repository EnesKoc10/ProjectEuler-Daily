def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")


def solve():
    largest_pandigital = 0

    for i in range(1, 10000):
        concatenated_string = ""
        n = 1

        while len(concatenated_string) < 9:
            concatenated_string += str(i * n)
            n += 1

        if len(concatenated_string) == 9:
            if is_pandigital(concatenated_string):
                result = int(concatenated_string)
                if result > largest_pandigital:
                    largest_pandigital = result

    return largest_pandigital


print(solve())
# 932718654