import collections


def generate_polygonal_numbers():
    formulas = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2)
    }

    polygonal_data = collections.defaultdict(list)
    for sides, formula in formulas.items():
        n = 1
        while True:
            val = formula(n)
            if val > 9999:
                break
            if val >= 1000:
                polygonal_data[sides].append(val)
            n += 1
    return polygonal_data


def find_cyclic_set(current_set, remaining_sides, polygonal_data):
    if not remaining_sides:
        if str(current_set[-1])[2:] == str(current_set[0])[:2]:
            return current_set
        return None

    last_two = str(current_set[-1])[2:]

    for side_count in list(remaining_sides):
        for number in polygonal_data[side_count]:
            if str(number)[:2] == last_two:
                new_remaining = remaining_sides.copy()
                new_remaining.remove(side_count)

                result = find_cyclic_set(current_set + [number], new_remaining, polygonal_data)
                if result:
                    return result
    return None


def solve():
    data = generate_polygonal_numbers()

    for start_number in data[8]:
        remaining = {3, 4, 5, 6, 7}
        result = find_cyclic_set([start_number], remaining, data)
        if result:
            print(f"Set: {result}")
            print(f"Sum: {sum(result)}")
            return


solve()
# 28684