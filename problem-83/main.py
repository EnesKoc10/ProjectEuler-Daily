import heapq


def solve():
    matrix = []
    with open("0083_matrix.txt", "r") as f:
        for line in f:
            matrix.append([int(x) for x in line.split(",")])

    rows = len(matrix)
    cols = len(matrix[0])

    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = matrix[0][0]

    priority_queue = [(matrix[0][0], 0, 0)]

    while priority_queue:
        current_dist, r, c = heapq.heappop(priority_queue)

        if current_dist > distances[r][c]:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = current_dist + matrix[nr][nc]
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(priority_queue, (new_dist, nr, nc))

    return distances[-1][-1]


print(solve())
# 425185