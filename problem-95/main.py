def solve():
    limit = 1000000
    divisor_sums = [0] * (limit + 1)

    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sums[j] += i

    max_chain_length = 0
    smallest_member = 0
    processed = [False] * (limit + 1)

    for i in range(1, limit + 1):
        if processed[i]:
            continue

        current_chain = []
        current = i

        while current <= limit and not processed[current]:
            current_chain.append(current)
            processed[current] = True
            current = divisor_sums[current]

        if current in current_chain:
            chain_start_index = current_chain.index(current)
            actual_chain = current_chain[chain_start_index:]
            chain_length = len(actual_chain)

            if chain_length > max_chain_length:
                max_chain_length = chain_length
                smallest_member = min(actual_chain)

    return smallest_member


print(solve())
# 14316