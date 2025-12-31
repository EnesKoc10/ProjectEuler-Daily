def findFibonacciIndexByDigits(target_digits):
    first = 1
    second = 1
    index = 2
    
    while len(str(second)) < target_digits:
        first, second = second, first + second
        index += 1
        
    return index

result = findFibonacciIndexByDigits(1000)
print(result)
# 4782