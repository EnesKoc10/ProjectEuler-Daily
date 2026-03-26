def solve():
    singles = list(range(1, 21)) + [25]
    doubles = [2 * x for x in singles]
    triples = [3 * x for x in range(1, 21)]

    all_hits = []
    for x in singles: all_hits.append(x)
    for x in doubles: all_hits.append(x)
    for x in triples: all_hits.append(x)

    checkouts = 0

    for last_dart in doubles:
        if last_dart < 100:
            checkouts += 1

        for i in range(len(all_hits)):
            first_dart = all_hits[i]
            if first_dart + last_dart < 100:
                checkouts += 1

            for j in range(i, len(all_hits)):
                second_dart = all_hits[j]
                if first_dart + second_dart + last_dart < 100:
                    checkouts += 1

    return checkouts


print(solve())
# 38182