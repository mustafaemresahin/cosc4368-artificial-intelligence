import math
import heapq

# Calculate Euclidean distance as the heuristic
def euclidean_distance(node, goal):
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)

# A* Algorithm
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: euclidean_distance(start, goal)}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        neighbors = get_neighbors(current, rows, cols)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + grid[neighbor[0]][neighbor[1]]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + euclidean_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

def get_neighbors(node, rows, cols):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < rows and 0 <= y < cols:
            neighbors.append((x, y))
    return neighbors

# Example Grid with Travel Times
grid = [
    [1, 3, 1, 4],
    [2, 1, 5, 1],
    [1, 1, 3, 1]
]

# Test A* Algorithm
start = (0, 0)
goal = (2, 3)
path = astar(grid, start, goal)

print("A* Path:", path)
