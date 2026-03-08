def solve():
    limit = 10000000
    cache = [0] * limit
    cache[1] = 1
    cache[89] = 89

    count_89 = 0

    for i in range(1, limit):
        current = i
        chain = []

        while True:
            if current < limit and cache[current] != 0:
                result = cache[current]
                break

            chain.append(current)

            next_val = 0
            temp = current
            while temp > 0:
                digit = temp % 10
                next_val += digit * digit
                temp //= 10
            current = next_val

        for num in chain:
            if num < limit:
                cache[num] = result

        if result == 89:
            count_89 += 1

    return count_89


print(solve())
# 8581146