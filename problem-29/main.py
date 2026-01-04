distinct_powers = set()

for a in range(2, 101):
    for b in range(2, 101):
        distinct_powers.add(a**b)

result = len(distinct_powers)
print(result)
# 9183