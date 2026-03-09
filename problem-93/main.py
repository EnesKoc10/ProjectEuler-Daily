from itertools import combinations, permutations, product


def calculate_targets(digits):
    targets = set()
    for p in permutations(digits):
        for ops in product(['+', '-', '*', '/'], repeat=3):
            expressions = [
                "((%f %s %f) %s %f) %s %f" % (p[0], ops[0], p[1], ops[1], p[2], ops[2], p[3]),
                "(%f %s (%f %s %f)) %s %f" % (p[0], ops[0], p[1], ops[1], p[2], ops[2], p[3]),
                "(%f %s %f) %s (%f %s %f)" % (p[0], ops[0], p[1], ops[1], p[2], ops[2], p[3]),
                "%f %s ((%f %s %f) %s %f)" % (p[0], ops[0], p[1], ops[1], p[2], ops[2], p[3]),
                "%f %s (%f %s (%f %s %f))" % (p[0], ops[0], p[1], ops[1], p[2], ops[2], p[3])
            ]
            for expr in expressions:
                try:
                    res = eval(expr)
                    if res > 0 and res == int(res):
                        targets.add(int(res))
                except ZeroDivisionError:
                    continue
    return targets


def get_consecutive_length(targets):
    n = 1
    while n in targets:
        n += 1
    return n - 1


def solve():
    max_length = 0
    best_set = ""

    for digits in combinations(range(10), 4):
        targets = calculate_targets(digits)
        length = get_consecutive_length(targets)

        if length > max_length:
            max_length = length
            best_set = "".join(map(str, digits))

    return best_set


print(solve())
# 1258