def solve():
    limit = 50
    count = 0

    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            if x1 == 0 and y1 == 0: continue

            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    if x2 == 0 and y2 == 0: continue
                    if x1 == x2 and y1 == y2: continue

                    a2 = x1 * x1 + y1 * y1
                    b2 = x2 * x2 + y2 * y2
                    c2 = (x1 - x2) ** 2 + (y1 - y2) ** 2

                    sides = sorted([a2, b2, c2])
                    if sides[0] + sides[1] == sides[2]:
                        count += 1

    return count // 2


print(solve())
# 14234