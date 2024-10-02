from collections import deque

# BFS Implementation
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path
            visited.add(node)
    return None

# DFS Implementation
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

# Example City Road Network as a Graph
graph = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0, 7],
    4: [1],
    5: [1],
    6: [2],
    7: [3]
}

# Test BFS and DFS
bfs_result = bfs(graph, 0, 7)
dfs_result = dfs(graph, 0, 7)

print("BFS Result:", bfs_result)
print("DFS Result:", dfs_result)
