import requests


def get_value(card):
    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    v = card[0]
    return values[v] if v in values else int(v)


def score_hand(hand):
    values = sorted([get_value(c) for c in hand], reverse=True)
    suits = [c[1] for c in hand]

    counts = {v: values.count(v) for v in set(values)}
    counts_sorted = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    distinct_values_sorted = [x[0] for x in counts_sorted]
    frequencies = [x[1] for x in counts_sorted]

    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and max(values) - min(values) == 4

    if is_straight and is_flush and max(values) == 14: return (10, values)
    if is_straight and is_flush: return (9, values)
    if frequencies == [4, 1]: return (8, distinct_values_sorted)
    if frequencies == [3, 2]: return (7, distinct_values_sorted)
    if is_flush: return (6, values)
    if is_straight: return (5, values)
    if frequencies == [3, 1, 1]: return (4, distinct_values_sorted)
    if frequencies == [2, 2, 1]: return (3, distinct_values_sorted)
    if frequencies == [2, 1, 1, 1]: return (2, distinct_values_sorted)
    return (1, values)


def solve():
    url = "https://projecteuler.net/project/resources/p054_poker.txt"
    data = requests.get(url).text.strip().split('\n')

    player1_wins = 0

    for line in data:
        cards = line.split()
        hand1 = cards[:5]
        hand2 = cards[5:]

        if score_hand(hand1) > score_hand(hand2):
            player1_wins += 1

    print(player1_wins)


if __name__ == "__main__":
    solve()
    # 376