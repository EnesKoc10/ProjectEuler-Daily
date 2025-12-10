x, y = 999, 999
palindrome = []


while True:
    palindrome = [i for i in str(x * y)]
    r_palindrome = palindrome[::-1]
    if palindrome == r_palindrome:
        break
    else:
        y -= 1
        if y < 100: 
            y = x
            x -= 1

print(palindrome)