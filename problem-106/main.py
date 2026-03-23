from itertools import combinations


def count_comparisons(n):
    total_tests = 0
    indices = list(range(n))

    for size in range(2, n // 2 + 1):
        for subset_a_indices in combinations(indices, size):
            remaining_indices = [i for i in indices if i not in subset_a_indices]
            for subset_b_indices in combinations(remaining_indices, size):
                if subset_a_indices[0] > subset_b_indices[0]:
                    continue

                needs_test = False
                for i in range(size):
                    if subset_a_indices[i] > subset_b_indices[i]:
                        needs_test = True
                        break

                if needs_test:
                    total_tests += 1

    return total_tests


def solve():
    return count_comparisons(12)


print(solve())
# 21384