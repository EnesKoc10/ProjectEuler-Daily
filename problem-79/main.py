import collections
import os


def solve():
    file_path = "0079_keylog.txt"
    if not os.path.exists(file_path):
        return "Error: 0079_keylog.txt not found"

    with open(file_path, "r") as f:
        attempts = [line.strip() for line in f if line.strip()]

    graph = collections.defaultdict(set)
    nodes = set()

    for entry in attempts:
        d1, d2, d3 = entry[0], entry[1], entry[2]
        graph[d1].add(d2)
        graph[d2].add(d3)
        nodes.update([d1, d2, d3])

    passcode = ""
    while nodes:
        for node in sorted(nodes):
            is_first = True
            for other_node in nodes:
                if node in graph[other_node]:
                    is_first = False
                    break

            if is_first:
                passcode += node
                nodes.remove(node)
                break

    return passcode


print(solve())
# 73162890