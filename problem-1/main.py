# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


sum = 0
i = 0

while True:
    if i == 1000:
        break
    
    # becomes zero when we take the modes of the specified numbers. In this way we got the number multiples
    if 0 == (i%3) or 0 == (i%5):
        sum += i
    i = i + 1

print(sum)
# Answer is 233168