import sympy


def find_prime_family_solution():
    primes = list(sympy.primerange(100000, 1000000))
    prime_set = set(primes)

    for prime in primes:
        s_prime = str(prime)

        for digit in '012':
            if digit in s_prime[:-1]:
                count = s_prime.count(digit)

                # We usually need to replace 3 digits to maintain divisibility rules
                if count == 3:
                    family = []
                    for replacement in '0123456789':
                        new_num_str = s_prime.replace(digit, replacement)

                        if new_num_str[0] == '0':
                            continue

                        new_num = int(new_num_str)
                        if new_num in prime_set:
                            family.append(new_num)

                    if len(family) == 8:
                        return min(family)


if __name__ == "__main__":
    result = find_prime_family_solution()
    print(result)
    # 121313