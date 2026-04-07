import math


def solve():
    turns = 15
    outcomes = {0: 1}

    for turn in range(1, turns + 1):
        red_discs = turn
        new_outcomes = {}

        for blue_count, ways in outcomes.items():
            new_outcomes[blue_count + 1] = new_outcomes.get(blue_count + 1, 0) + ways
            new_outcomes[blue_count] = new_outcomes.get(blue_count, 0) + ways * red_discs

        outcomes = new_outcomes

    winning_ways = sum(ways for blue_count, ways in outcomes.items() if blue_count > turns / 2)
    total_ways = math.factorial(turns + 1)

    prize_fund = total_ways // winning_ways
    return prize_fund


print(solve())
# 2269