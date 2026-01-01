def get_cycle_length(d):
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    
    if d == 1:
        return 0
    
    remainder = 1
    length = 0
    
    while True:
        remainder = (remainder * 10) % d
        length += 1
        if remainder == 1:
            return length

def solve():
    max_length = 0
    result_d = 0
    
    for d in range(2, 1000):
        current_length = get_cycle_length(d)
        if current_length > max_length:
            max_length = current_length
            result_d = d
            
    return result_d


print(solve())
# 983