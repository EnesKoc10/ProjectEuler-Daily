def get_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0


def solve():
    origin_count = 0
    with open("0102_triangles.txt", "r") as f:
        for line in f:
            coords = list(map(int, line.split(",")))
            x1, y1, x2, y2, x3, y3 = coords

            main_area = get_area(x1, y1, x2, y2, x3, y3)
            area1 = get_area(0, 0, x1, y1, x2, y2)
            area2 = get_area(0, 0, x2, y2, x3, y3)
            area3 = get_area(0, 0, x3, y3, x1, y1)

            if abs(main_area - (area1 + area2 + area3)) < 1e-9:
                origin_count += 1

    return origin_count


print(solve())
# 228