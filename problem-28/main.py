def solve_spiral_diagonal_sum(limit):
    total_sum = 1
    current_n = 3
    
    while current_n <= limit:
        step = current_n - 1
        top_right = current_n**2
        top_left = top_right - step
        bottom_left = top_left - step
        bottom_right = bottom_left - step
        
        total_sum += (top_right + top_left + bottom_left + bottom_right)
        current_n += 2
        
    return total_sum

limit_size = 1001
print(solve_spiral_diagonal_sum(limit_size))
# 669171001