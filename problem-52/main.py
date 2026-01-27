def check_permuted_multiples():
    x = 1
    while True:
        target = sorted(str(x))

        if all(sorted(str(x * i)) == target for i in range(2, 7)):
            return x

        x += 1


result = check_permuted_multiples()
print(result)
# 142857