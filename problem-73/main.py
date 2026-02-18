def count_fractions_in_range(limit):
    count = 0
    stack = [(1, 3, 1, 2)]

    while stack:
        n1, d1, n2, d2 = stack.pop()

        n_mid = n1 + n2
        d_mid = d1 + d2

        if d_mid <= limit:
            count += 1
            stack.append((n_mid, d_mid, n2, d2))
            stack.append((n1, d1, n_mid, d_mid))

    return count


limit = 12000
result = count_fractions_in_range(limit)
print(result)
# 7295372