def solve_euler_numerator():
    coefficients = [2]

    k = 1
    while len(coefficients) < 100:
        coefficients.extend([1, 2 * k, 1])
        k += 1

    coefficients = coefficients[:100]

    num_prev2 = 1
    num_prev1 = 2

    for i in range(1, 100):
        current_a = coefficients[i]
        current_num = current_a * num_prev1 + num_prev2

        num_prev2 = num_prev1
        num_prev1 = current_num

    result_numerator = num_prev1
    digit_sum = sum(int(digit) for digit in str(result_numerator))

    return digit_sum


print(solve_euler_numerator())
# 272