import math

def is_pentagonal(n):
    if n < 1:
        return False
    val = (math.sqrt(24 * n + 1) + 1) / 6
    return val.is_integer()

def solve():
    pentagonals = []
    i = 1
    while True:
        p_k = i * (3 * i - 1) // 2
        for p_j in reversed(pentagonals):
            if is_pentagonal(p_k - p_j) and is_pentagonal(p_k + p_j):
                return p_k - p_j
        pentagonals.append(p_k)
        i += 1

if __name__ == "__main__":
    result = solve()
    print(result)
    #5482660