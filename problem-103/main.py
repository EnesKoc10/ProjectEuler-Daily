from itertools import combinations


def is_special_sum_set(s):
    subset_sums = set()
    for i in range(1, len(s) + 1):
        for combo in combinations(s, i):
            current_sum = sum(combo)
            if current_sum in subset_sums:
                return False
            subset_sums.add(current_sum)

    for i in range(1, (len(s) + 1) // 2):
        if sum(sorted(s)[:i + 1]) <= sum(sorted(s, reverse=True)[:i]):
            return False
    return True


def solve():
    base_set = [20, 31, 38, 39, 40, 42, 45]
    min_sum = sum(base_set)
    best_string = "".join(map(str, base_set))

    offsets = range(-3, 4)
    for d1 in offsets:
        for d2 in offsets:
            for d3 in offsets:
                for d4 in offsets:
                    for d5 in offsets:
                        for d6 in offsets:
                            for d7 in offsets:
                                current_set = sorted([
                                    base_set[0] + d1, base_set[1] + d2, base_set[2] + d3,
                                    base_set[3] + d4, base_set[4] + d5, base_set[5] + d6, base_set[6] + d7
                                ])

                                if len(set(current_set)) != 7: continue

                                current_sum = sum(current_set)
                                if current_sum < min_sum:
                                    if is_special_sum_set(current_set):
                                        min_sum = current_sum
                                        best_string = "".join(map(str, current_set))

    return best_string


print(solve())
# 20313839404245