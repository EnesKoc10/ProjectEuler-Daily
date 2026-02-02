def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solve_spiral_primes():
    side_length = 1
    primes_count = 0
    total_diagonals = 1
    current_number = 1

    while True:
        side_length += 2
        for _ in range(4):
            current_number += (side_length - 1)
            if is_prime(current_number):
                primes_count += 1

        total_diagonals += 4

        if (primes_count / total_diagonals) < 0.10:
            return side_length


if __name__ == "__main__":
    result = solve_spiral_primes()
    print(result)
    # 26241