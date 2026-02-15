target_n, target_d = 3, 7
limit = 1_000_000

result_n = 0
result_d = 0

for d in range(limit, 0, -1):
    n = (target_n * d - 1) // target_d

    if result_n * d < n * result_d or result_d == 0:
        result_n = n
        result_d = d

        if target_n * d - target_d * n == 1:
            break

print(result_n)
# 428570