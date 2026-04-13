def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def solve():
    limit = 10 ** 8
    max_root = int(limit ** 0.5)
    palindromic_sums = set()

    for i in range(1, max_root):
        current_sum = i * i
        for j in range(i + 1, max_root):
            current_sum += j * j
            if current_sum >= limit:
                break
            if is_palindrome(current_sum):
                palindromic_sums.add(current_sum)

    return sum(palindromic_sums)


print(solve())
# 2906969179