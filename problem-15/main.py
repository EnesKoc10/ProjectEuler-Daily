import math

grid_size = 20
total_steps = grid_size * 2
right_steps = grid_size

routes = math.comb(total_steps, right_steps)

print(routes)