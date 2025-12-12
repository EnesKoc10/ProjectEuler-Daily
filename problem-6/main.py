limit = 100


sum_of_squares = (limit * (1 + limit) / 2) ** 2
square_of_sum = (limit ** 3) / 3 + (limit ** 2) / 2 + limit / 6

print(sum_of_squares - square_of_sum)
#25164150.0