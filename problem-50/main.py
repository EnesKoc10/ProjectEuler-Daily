def solve():
    limit = 1000000
    primes = []
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False

    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit, p):
                is_prime[i] = False

    prime_set = set(primes)
    cumulative_sums = [0]
    current_sum = 0
    for p in primes:
        current_sum += p
        if current_sum >= limit:
            break
        cumulative_sums.append(current_sum)

    max_length = 0
    result_prime = 0
    n = len(cumulative_sums)

    for i in range(n):
        for j in range(i + max_length + 1, n):
            current_diff = cumulative_sums[j] - cumulative_sums[i]
            if current_diff in prime_set:
                max_length = j - i
                result_prime = current_diff

    return result_prime


print(solve())
# 997651