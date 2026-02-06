import collections


def solve_cubic_permutations(target_count):
    cubes_map = collections.defaultdict(list)
    n = 1

    while True:
        cube = n ** 3
        sorted_digits = "".join(sorted(str(cube)))

        cubes_map[sorted_digits].append(cube)

        if len(cubes_map[sorted_digits]) == target_count:
            return min(cubes_map[sorted_digits])

        n += 1


result = solve_cubic_permutations(5)
print(result)
# 127035954683