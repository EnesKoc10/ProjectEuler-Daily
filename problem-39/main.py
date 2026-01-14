def solve_problem_39():
    max_solutions = 0
    best_p = 0

    for p in range(2, 1001, 2):
        current_solutions = 0
        for a in range(2, p // 3):
            if (p * (p - 2 * a)) % (2 * (p - a)) == 0:
                current_solutions += 1

        if current_solutions > max_solutions:
            max_solutions = current_solutions
            best_p = p

    return best_p


print(solve_problem_39())
# 840