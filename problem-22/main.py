def solve():
    with open('0022_names.txt', 'r') as file:
        content = file.read()
    
    names = content.replace('"', '').split(',')
    names.sort()

    total_score = 0
    
    for index, name in enumerate(names):
        alphabetical_value = sum(ord(char) - 64 for char in name)
        position = index + 1
        total_score += alphabetical_value * position
        
    return total_score

if __name__ == "__main__":
    print(solve())
    # 871198282