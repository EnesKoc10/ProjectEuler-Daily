def solve():
    k_limit = 12000
    n_limit = 2 * k_limit
    min_product_sum = [2 * n_limit] * (k_limit + 1)

    def find_combinations(product, total, count, start):
        k = product - total + count
        if k <= k_limit:
            if product < min_product_sum[k]:
                min_product_sum[k] = product

            for i in range(start, (n_limit // product) * 2):
                new_product = product * i
                new_total = total + i
                if new_product > n_limit:
                    break
                find_combinations(new_product, new_total, count + 1, i)

    find_combinations(1, 1, 1, 2)

    unique_minimal_numbers = set(min_product_sum[2:])
    return sum(unique_minimal_numbers)


print(solve())