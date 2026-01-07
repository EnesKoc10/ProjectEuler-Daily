def is_pandigital(multiplicand, multiplier, product):
    combined = str(multiplicand) + str(multiplier) + str(product)
    if len(combined) != 9:
        return False
    return set(combined) == set("123456789")

products = set()

for a in range(1, 10):
    for b in range(1000, 10000):
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)

for a in range(10, 100):
    for b in range(100, 1000):
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)

print(sum(products))
# 45228