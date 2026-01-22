def find_consecutive_integers(target_distinct_primes, consecutive_count):
    limit = 200000
    prime_counts = [0] * limit

    for i in range(2, limit):
        if prime_counts[i] == 0:
            for j in range(i, limit, i):
                prime_counts[j] += 1

        if i >= consecutive_count:
            match = True
            for k in range(consecutive_count):
                if prime_counts[i - k] != target_distinct_primes:
                    match = False
                    break

            if match:
                return i - consecutive_count + 1

    return None


result = find_consecutive_integers(4, 4)
print(result)
# 134043