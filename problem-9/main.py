def specialPythagoreanTriplet():
    limit_sum = 1000
    
    for a in range(1, limit_sum // 3 + 1):
        
        numerator = limit_sum * limit_sum - 2 * limit_sum * a
        denominator = 2 * (limit_sum - a)
        
        if numerator % denominator == 0:
            b = numerator // denominator
        
            if a < b:
                c = limit_sum - a - b

                if b < c:
                    product = a * b * c
                    return product
    
    return None

print(specialPythagoreanTriplet())
# 31875000