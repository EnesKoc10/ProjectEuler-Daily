import math

numerator_product = 1
denominator_product = 1

for d in range(10, 100):
    for n in range(10, d):
        n_str = str(n)
        d_str = str(d)
        
        common_digit = set(n_str) & set(d_str)
        
        if len(common_digit) == 1 and '0' not in common_digit:
            digit = common_digit.pop()

            new_n_str = n_str.replace(digit, '', 1)
            new_d_str = d_str.replace(digit, '', 1)
            
            # Avoid division by zero
            if new_d_str != '0':
                new_n = int(new_n_str)
                new_d = int(new_d_str)
                
                if n / d == new_n / new_d:
                    numerator_product *= n
                    denominator_product *= d

final_gcd = math.gcd(numerator_product, denominator_product)
result_denominator = denominator_product // final_gcd

print(result_denominator)