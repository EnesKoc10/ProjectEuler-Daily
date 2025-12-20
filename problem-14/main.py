def solve():
    limit = 1000000
    cache = {1: 1}
    
    def get_length(n):
        if n in cache:
            return cache[n]
        
        if n % 2 == 0:
            length = 1 + get_length(n // 2)
        else:
            length = 1 + get_length(3 * n + 1)
        
        cache[n] = length
        return length

    max_length = 0
    starting_number = 0

    for i in range(1, limit):
        current_length = get_length(i)
        if current_length > max_length:
            max_length = current_length
            starting_number = i
            
    return starting_number

print(solve())