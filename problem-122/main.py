def solve():
    target_limit = 200
    min_costs = [100] * (target_limit + 1)

    def find_path(current_path, current_depth, max_depth):
        if current_depth == max_depth:
            return

        last_val = current_path[-1]
        for i in range(len(current_path) - 1, -1, -1):
            next_val = last_val + current_path[i]

            if next_val <= target_limit:
                if next_val > last_val:
                    if current_depth + 1 < min_costs[next_val]:
                        min_costs[next_val] = current_depth + 1
                    find_path(current_path + [next_val], current_depth + 1, max_depth)

    for d in range(1, 13):
        find_path([1], 0, d)

    return sum(min_costs[2:])


print(solve())
# 1582