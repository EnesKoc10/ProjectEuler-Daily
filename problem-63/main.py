def solve_powerful_digit_counts():
    total_count = 0

    for base in range(1, 10):
        n = 1
        while True:
            power_result = base ** n
            digit_count = len(str(power_result))

            if digit_count == n:
                total_count += 1
                n += 1
            else:
                break

    return total_count


if __name__ == "__main__":
    result = solve_powerful_digit_counts()
    print(result)
    # 49