found = False
n = 1
factors = range(1, 20)


while not found:
    found = True
    for x in factors:
        if n % x != 0:
            found = False
    if found == False:
        n += 1

print(n)