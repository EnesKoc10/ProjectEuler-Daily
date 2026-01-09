import math

def solve():
    factorials = [math.factorial(i) for i in range(10)]
    total_sum = 0
    
    for number in range(10, 2540161):
        digit_sum = 0
        temp_number = number
        
        while temp_number > 0:
            digit_sum += factorials[temp_number % 10]
            temp_number //= 10
            
        if digit_sum == number:
            total_sum += number
            
    return total_sum

result = solve()
print(result)
# 40730