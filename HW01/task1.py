from collections import deque
import heapq

# Graph representation for BFS and DFS
graph = {
    0: [1, 3, 7],
    1: [4],
    3: [5],
    4: [6],
    5: [6],
    6: [],
    7: [4, 5]
}

# Weighted graph for Dijkstra's algorithm
city_graph_weighted = {
    0: {1: 2, 3: 2, 7: 3},
    1: {4: 4},
    3: {5: 7},
    4: {6: 4},
    5: {6: 2},
    6: {},
    7: {4: 5, 5: 6}
}

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# Dijkstra's Algorithm for Weighted Graph
def dijkstra(graph, start):
    min_distance = {node: float('infinity') for node in graph}
    min_distance[start] = 0
    pq = [(0, start)]
    came_from = {start: None}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < min_distance[neighbor]:
                min_distance[neighbor] = distance
                came_from[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return min_distance, came_from

def reconstruct_path(came_from, start, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return "Path does not exist"

# Run and display DFS order
print("DFS Order of nodes visited:")
dfs(graph, 0)
print("\n")

# Run and display BFS order
print("BFS Order of nodes visited:")
bfs(graph, 0)
print("\n")

# Run Dijkstra's algorithm and reconstruct paths
shortest_distances, paths_came_from = dijkstra(city_graph_weighted, 0)
for target in [7, 5, 6]:
    path = reconstruct_path(paths_came_from, 0, target)
    print(f"Shortest Path to {target} using Dijkstra's: {path} Distance = {shortest_distances[target]}")
