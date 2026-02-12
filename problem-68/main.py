import itertools


def solve():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solutions = []

    for inner in itertools.permutations(numbers, 5):
        remaining = [n for n in numbers if n not in inner]

        for outer in itertools.permutations(remaining, 5):
            if 10 in inner:
                continue

            lines = [
                (outer[0], inner[0], inner[1]),
                (outer[1], inner[1], inner[2]),
                (outer[2], inner[2], inner[3]),
                (outer[3], inner[3], inner[4]),
                (outer[4], inner[4], inner[0])
            ]

            line_sums = [sum(line) for line in lines]

            if len(set(line_sums)) == 1:
                min_outer = min(outer)
                start_index = outer.index(min_outer)

                ordered_lines = lines[start_index:] + lines[:start_index]

                candidate = "".join(str(num) for line in ordered_lines for num in line)

                if len(candidate) == 16:
                    solutions.append(int(candidate))

    return max(solutions)


print(solve())
# 6531031914842725