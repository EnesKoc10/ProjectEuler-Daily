def solve():
    total_sum = 0
    mod = 10**10

    for i in range(1, 1001):
        total_sum += pow(i, i, mod)

    result = total_sum % mod
    print(result)


if __name__ == "__main__":
    solve()
    # 9110846700