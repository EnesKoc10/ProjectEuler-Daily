def solve():
    target = 2000000
    closest_diff = target
    best_area = 0

    for width in range(1, 2000):
        for height in range(width, 2000):
            rectangles = (width * (width + 1) // 2) * (height * (height + 1) // 2)
            current_diff = abs(target - rectangles)

            if current_diff < closest_diff:
                closest_diff = current_diff
                best_area = width * height

            if rectangles > target + closest_diff:
                break

        if (width * (width + 1) // 2) ** 2 > target + closest_diff:
            break

    return best_area


print(solve())
# 2772