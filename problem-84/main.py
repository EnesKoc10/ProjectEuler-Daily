import random

def solve():
    pos, doubles, cc_ptr, ch_ptr = 0, 0, 0, 0
    visits = [0] * 40
    cc = [0, 10] + [None] * 14
    ch = [0, 10, 11, 24, 39, 5, 'R', 'R', 'U', -3] + [None] * 6
    random.shuffle(cc)
    random.shuffle(ch)

    for _ in range(2000000):
        d1, d2 = random.randint(1, 4), random.randint(1, 4)
        doubles = doubles + 1 if d1 == d2 else 0
        if doubles == 3:
            pos, doubles = 10, 0
        else:
            pos = (pos + d1 + d2) % 40
            if pos == 30:
                pos = 10
            elif pos in [2, 17, 33]:
                card = cc[cc_ptr]
                cc_ptr = (cc_ptr + 1) % 16
                if card is not None: pos = card
            elif pos in [7, 22, 36]:
                card = ch[ch_ptr]
                ch_ptr = (ch_ptr + 1) % 16
                if card == 'R':
                    pos = {7:15, 22:25, 36:5}[pos]
                elif card == 'U':
                    pos = 28 if pos == 22 else 12
                elif card == -3:
                    pos = (pos - 3) % 40
                    if pos == 33:
                        card_cc = cc[cc_ptr]
                        cc_ptr = (cc_ptr + 1) % 16
                        if card_cc is not None: pos = card_cc
                elif card is not None:
                    pos = card
        visits[pos] += 1

    top = sorted(range(40), key=lambda i: visits[i], reverse=True)
    return "".join(f"{i:02d}" for i in top[:3])

print(solve())
# 101524