palindrom = 0

for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        carpim = x * y
        
        carpim_str = str(carpim)
        if carpim_str == carpim_str[::-1]:
            
            
            if carpim > palindrom:
                palindrom = carpim
              

print(palindrom)
# 906609