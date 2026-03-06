from itertools import combinations


def solve():
    digits = list(range(10))
    cubes = list(combinations(digits, 6))

    square_numbers = [
        (0, 1), (0, 4), (0, 9), (1, 6), (2, 5),
        (3, 6), (4, 9), (6, 4), (8, 1)
    ]

    def can_display(c1, c2):
        c1 = set(c1)
        c2 = set(c2)
        if 6 in c1 or 9 in c1:
            c1.add(6);
            c1.add(9)
        if 6 in c2 or 9 in c2:
            c2.add(6);
            c2.add(9)

        for d1, d2 in square_numbers:
            if not ((d1 in c1 and d2 in c2) or (d1 in c2 and d2 in c1)):
                return False
        return True

    count = 0
    num_cubes = len(cubes)
    for i in range(num_cubes):
        for j in range(i, num_cubes):
            if can_display(cubes[i], cubes[j]):
                count += 1

    return count


print(solve())
# 1217