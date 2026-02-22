def solve():
    limit = 1000000
    partitions = [1]
    n = 1

    while True:
        total = 0
        k = 1
        while True:
            pent_formula_positive = k * (3 * k - 1) // 2
            pent_formula_negative = -k * (3 * (-k) - 1) // 2

            indices = [pent_formula_positive, pent_formula_negative]
            found_any = False

            for index in indices:
                if index <= n:
                    sign = 1 if k % 2 == 1 else -1
                    total += sign * partitions[n - index]
                    found_any = True

            if not found_any:
                break
            k += 1

        current_partition = total % limit
        if current_partition == 0:
            return n

        partitions.append(current_partition)
        n += 1


print(solve())
# 55374