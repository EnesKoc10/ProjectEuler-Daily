def roman_to_int(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total

def int_to_minimal_roman(n):
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ""
    for value, symbol in mapping:
        while n >= value:
            result += symbol
            n -= value
    return result

def solve():
    total_saved = 0
    try:
        with open("0089_roman.txt", "r") as f:
            for line in f:
                original = line.strip()
                decimal_value = roman_to_int(original)
                minimal = int_to_minimal_roman(decimal_value)
                total_saved += len(original) - len(minimal)
    except FileNotFoundError:
        return "Error: roman.txt not found"
    return total_saved

print(solve())
# 743