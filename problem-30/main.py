powers = [i**5 for i in range(10)]
total_sum = 0

for number in range(2, 354295):
    digits_sum = 0
    temp = number
    
    while temp > 0:
        digits_sum += powers[temp % 10]
        temp //= 10
        
    if digits_sum == number:
        total_sum += number

print(total_sum)
# 443839