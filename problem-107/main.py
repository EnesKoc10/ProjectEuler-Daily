def solve():
    edges = []
    total_weight = 0
    with open("0107_network.txt", "r") as f:
        matrix = [line.strip().split(",") for line in f]

    num_vertices = len(matrix)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if matrix[i][j] != "-":
                weight = int(matrix[i][j])
                edges.append((weight, i, j))
                total_weight += weight

    edges.sort()

    parent = list(range(num_vertices))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    mst_weight = 0
    edges_count = 0
    for weight, u, v in edges:
        if union(u, v):
            mst_weight += weight
            edges_count += 1
            if edges_count == num_vertices - 1:
                break

    return total_weight - mst_weight


print(solve())
# 259679